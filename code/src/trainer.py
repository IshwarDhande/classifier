import os
import time
import logging
from typing import Dict, Any, Tuple, List
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from src.utils import MetricWriter
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    get_linear_schedule_with_warmup
)
from src.evaluator import compute_metrics, save_evaluation_artifacts
from src.model import save_model_and_tokenizer

logger = logging.getLogger("trainer")

class Trainer:
    """Manages model training, validation, early stopping, and artifact checkpointing."""
    
    def __init__(
        self,
        model: AutoModelForSequenceClassification,
        tokenizer: AutoTokenizer,
        config: Dict[str, Any],
        device: torch.device,
        writer: MetricWriter
    ):
        self.model = model.to(device)
        self.tokenizer = tokenizer
        self.config = config
        self.device = device
        self.writer = writer
        
        self.num_epochs = config["training"]["num_epochs"]
        self.learning_rate = float(config["training"]["learning_rate"])
        self.weight_decay = float(config["training"]["weight_decay"])
        self.warmup_ratio = float(config["training"]["warmup_ratio"])
        self.patience = int(config["training"]["patience"])
        self.grad_accum_steps = int(config["training"].get("gradient_accumulation_steps", 1))
        
        self.output_dir = config["paths"]["output_dir"]
        self.best_model_dir = os.path.join(self.output_dir, "best_model")
        self.report_dir = config["paths"]["report_dir"]
        self.label_names = config["task"]["labels"]
        
    def _create_optimizer_and_scheduler(self, total_training_steps: int):
        no_decay = ["bias", "LayerNorm.weight"]
        optimizer_grouped_parameters = [
            {
                "params": [
                    p for n, p in self.model.named_parameters()
                    if not any(nd in n for nd in no_decay)
                ],
                "weight_decay": self.weight_decay,
            },
            {
                "params": [
                    p for n, p in self.model.named_parameters()
                    if any(nd in n for nd in no_decay)
                ],
                "weight_decay": 0.0,
            },
        ]
        
        optimizer = torch.optim.AdamW(optimizer_grouped_parameters, lr=self.learning_rate)
        warmup_steps = int(total_training_steps * self.warmup_ratio)
        scheduler = get_linear_schedule_with_warmup(
            optimizer,
            num_warmup_steps=warmup_steps,
            num_training_steps=total_training_steps
        )
        return optimizer, scheduler

    def evaluate(self, dataloader: DataLoader) -> Tuple[float, Dict[str, Any], List[int], List[int], List[str]]:
        """Runs evaluation over a dataloader."""
        self.model.eval()
        total_loss = 0.0
        y_true = []
        y_pred = []
        utterances = []
        
        with torch.no_grad():
            for batch in dataloader:
                input_ids = batch["input_ids"].to(self.device)
                attention_mask = batch["attention_mask"].to(self.device)
                labels = batch["labels"].to(self.device)
                
                kwargs = {
                    "input_ids": input_ids,
                    "attention_mask": attention_mask,
                    "labels": labels
                }
                if "token_type_ids" in batch:
                    kwargs["token_type_ids"] = batch["token_type_ids"].to(self.device)
                    
                outputs = self.model(**kwargs)
                loss = outputs.loss
                total_loss += loss.item() * len(labels)
                
                preds = torch.argmax(outputs.logits, dim=1)
                y_true.extend(labels.cpu().tolist())
                y_pred.extend(preds.cpu().tolist())
                utterances.extend(batch["utterance"])
                
        avg_loss = total_loss / len(dataloader.dataset)
        metrics = compute_metrics(y_true, y_pred, self.label_names)
        return avg_loss, metrics, y_true, y_pred, utterances

    def train(self, train_loader: DataLoader, val_loader: DataLoader, test_loader: DataLoader = None):
        """Full training loop with validation, early stopping and best model saving."""
        total_steps = (len(train_loader) // self.grad_accum_steps) * self.num_epochs
        optimizer, scheduler = self._create_optimizer_and_scheduler(total_steps)
        
        logger.info(f"Starting training for {self.num_epochs} epochs | Total training steps: {total_steps}")
        best_val_macro_f1 = -1.0
        epochs_no_improve = 0
        global_step = 0
        
        for epoch in range(1, self.num_epochs + 1):
            epoch_start_time = time.time()
            self.model.train()
            train_loss = 0.0
            
            for step, batch in enumerate(train_loader, start=1):
                input_ids = batch["input_ids"].to(self.device)
                attention_mask = batch["attention_mask"].to(self.device)
                labels = batch["labels"].to(self.device)
                
                kwargs = {
                    "input_ids": input_ids,
                    "attention_mask": attention_mask,
                    "labels": labels
                }
                if "token_type_ids" in batch:
                    kwargs["token_type_ids"] = batch["token_type_ids"].to(self.device)
                    
                outputs = self.model(**kwargs)
                loss = outputs.loss / self.grad_accum_steps
                loss.backward()
                train_loss += loss.item() * self.grad_accum_steps * len(labels)
                
                if step % self.grad_accum_steps == 0 or step == len(train_loader):
                    torch.nn.utils.clip_grad_norm_(self.model.parameters(), max_norm=1.0)
                    optimizer.step()
                    scheduler.step()
                    optimizer.zero_grad()
                    global_step += 1
                    
            avg_train_loss = train_loss / len(train_loader.dataset)
            
            # Validation Step
            val_loss, val_metrics, val_true, val_pred, val_utts = self.evaluate(val_loader)
            epoch_time = time.time() - epoch_start_time
            
            # Log to TensorBoard
            self.writer.add_scalar("Loss/train", avg_train_loss, epoch)
            self.writer.add_scalar("Loss/val", val_loss, epoch)
            self.writer.add_scalar("Accuracy/val", val_metrics["accuracy"], epoch)
            self.writer.add_scalar("Macro_F1/val", val_metrics["macro_f1"], epoch)
            self.writer.add_scalar("Learning_Rate", scheduler.get_last_lr()[0], epoch)
            
            logger.info(
                f"Epoch {epoch:02d}/{self.num_epochs:02d} ({epoch_time:.1f}s) | "
                f"Train Loss: {avg_train_loss:.4f} | "
                f"Val Loss: {val_loss:.4f} | "
                f"Val Acc: {val_metrics['accuracy']:.4f} | "
                f"Val Macro F1: {val_metrics['macro_f1']:.4f}"
            )
            
            # Checkpoint Best Model
            if val_metrics["macro_f1"] > best_val_macro_f1:
                best_val_macro_f1 = val_metrics["macro_f1"]
                epochs_no_improve = 0
                logger.info(f"--> New best Val Macro F1: {best_val_macro_f1:.4f}. Saving checkpoint to {self.best_model_dir}")
                save_model_and_tokenizer(self.model, self.tokenizer, self.best_model_dir)
            else:
                epochs_no_improve += 1
                logger.info(f"No improvement for {epochs_no_improve}/{self.patience} epochs.")
                if epochs_no_improve >= self.patience:
                    logger.info(f"Early stopping triggered at epoch {epoch}.")
                    break
                    
        logger.info(f"Training completed. Best Validation Macro F1: {best_val_macro_f1:.4f}")
        
        # Final Test Evaluation using Best Model
        if test_loader is not None:
            logger.info(f"Loading best checkpoint from {self.best_model_dir} for test set evaluation...")
            self.model = AutoModelForSequenceClassification.from_pretrained(self.best_model_dir).to(self.device)
            test_loss, test_metrics, test_true, test_pred, test_utts = self.evaluate(test_loader)
            
            logger.info(
                f"Test Evaluation Results | "
                f"Test Loss: {test_loss:.4f} | "
                f"Test Acc: {test_metrics['accuracy']:.4f} | "
                f"Test Macro F1: {test_metrics['macro_f1']:.4f}"
            )
            
            artifact_paths = save_evaluation_artifacts(
                metrics=test_metrics,
                y_true=test_true,
                y_pred=test_pred,
                utterances=test_utts,
                label_names=self.label_names,
                report_dir=self.report_dir,
                prefix="test"
            )
            logger.info(f"Saved test evaluation artifacts to {self.report_dir}")
            return test_metrics
            
        return val_metrics
