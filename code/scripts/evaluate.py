#!/home/eshwar/code/simulator_persuasion/code/venv2/bin/python
import os
import sys
import argparse
import torch
from torch.utils.data import DataLoader

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.model import load_model_and_tokenizer
from src.dataset import TextClassificationDataset, collate_fn
from src.evaluator import compute_metrics, save_evaluation_artifacts
from src.utils import get_device, setup_logger

def parse_args():
    parser = argparse.ArgumentParser(description="Evaluate saved BERT model on a test CSV dataset.")
    parser.add_argument("--model_dir", type=str, required=True, help="Path to saved model directory.")
    parser.add_argument("--test_csv", type=str, required=True, help="Path to test CSV file.")
    parser.add_argument("--text_col", type=str, default="utterance", help="Text column name.")
    parser.add_argument("--label_col", type=str, default=None, help="Label column name (auto-detected if None).")
    parser.add_argument("--output_dir", type=str, required=True, help="Directory to save evaluation artifacts.")
    parser.add_argument("--prefix", type=str, default="eval", help="Artifact file prefix.")
    parser.add_argument("--batch_size", type=int, default=64, help="Evaluation batch size.")
    return parser.parse_args()

def main():
    args = parse_args()
    logger = setup_logger("evaluate", log_dir=args.output_dir, log_filename=f"{args.prefix}.log")
    device = get_device()
    
    logger.info(f"Loading model and tokenizer from: {args.model_dir}")
    model, tokenizer = load_model_and_tokenizer(args.model_dir)
    model.to(device)
    model.eval()
    
    id2label = model.config.id2label
    label2id = model.config.label2id
    label_names = [id2label[i] if i in id2label else id2label[str(i)] for i in range(len(label2id))]
    
    # Auto-detect label column if not provided
    label_col = args.label_col
    if label_col is None:
        import pandas as pd
        df_cols = list(pd.read_csv(args.test_csv, nrows=1).columns)
        for cand in ["response_category", "execution_status", "label", "target"]:
            if cand in df_cols:
                label_col = cand
                break
        if label_col is None:
            raise ValueError(f"Could not auto-detect label column in {args.test_csv}. Please provide --label_col.")
            
    dataset = TextClassificationDataset(
        csv_file=args.test_csv,
        tokenizer=tokenizer,
        text_column=args.text_col,
        label_column=label_col,
        label2id=label2id,
        max_length=128
    )
    
    loader = DataLoader(dataset, batch_size=args.batch_size, shuffle=False, collate_fn=collate_fn)
    logger.info(f"Loaded {len(dataset)} samples from {args.test_csv}")
    
    y_true, y_pred, utterances = [], [], []
    with torch.no_grad():
        for batch in loader:
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            labels = batch["labels"].to(device)
            
            kwargs = {"input_ids": input_ids, "attention_mask": attention_mask}
            if "token_type_ids" in batch:
                kwargs["token_type_ids"] = batch["token_type_ids"].to(device)
                
            logits = model(**kwargs).logits
            preds = torch.argmax(logits, dim=1)
            
            y_true.extend(labels.cpu().tolist())
            y_pred.extend(preds.cpu().tolist())
            utterances.extend(batch["utterance"])
            
    metrics = compute_metrics(y_true, y_pred, label_names)
    logger.info(f"Results -> Accuracy: {metrics['accuracy']:.4f} | Macro F1: {metrics['macro_f1']:.4f}")
    
    artifacts = save_evaluation_artifacts(
        metrics=metrics,
        y_true=y_true,
        y_pred=y_pred,
        utterances=utterances,
        label_names=label_names,
        report_dir=args.output_dir,
        prefix=args.prefix
    )
    logger.info(f"Artifacts saved: {artifacts}")

if __name__ == "__main__":
    main()
