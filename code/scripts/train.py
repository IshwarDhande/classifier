#!/home/eshwar/code/simulator_persuasion/code/venv2/bin/python
import os
import sys
import argparse

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.config import load_config
from src.utils import set_seed, get_device, setup_logger, MetricWriter
from src.model import build_tokenizer, build_model
from src.dataset import create_dataloaders
from src.trainer import Trainer

def parse_args():
    parser = argparse.ArgumentParser(description="Train BERT classification model.")
    parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="Path to YAML experiment config file."
    )
    parser.add_argument("--epochs", type=int, default=None, help="Override number of epochs.")
    parser.add_argument("--batch_size", type=int, default=None, help="Override batch size.")
    parser.add_argument("--lr", type=float, default=None, help="Override learning rate.")
    parser.add_argument("--seed", type=int, default=None, help="Override random seed.")
    return parser.parse_args()

def main():
    args = parse_args()
    config = load_config(args.config)
    
    # Overrides
    if args.epochs is not None:
        config["training"]["num_epochs"] = args.epochs
    if args.batch_size is not None:
        config["training"]["batch_size"] = args.batch_size
    if args.lr is not None:
        config["training"]["learning_rate"] = args.lr
    if args.seed is not None:
        config["training"]["seed"] = args.seed
        
    log_dir = config["paths"]["log_dir"]
    logger = setup_logger("train_pipeline", log_dir=log_dir, log_filename="train.log")
    logger.info(f"Loaded config from {args.config}")
    logger.info(f"Task: {config['task']['name']} | Dataset: {config['task']['dataset_variant']}")
    
    set_seed(config["training"]["seed"])
    device = get_device()
    
    tokenizer = build_tokenizer(config["model"]["pretrained_name"])
    train_loader, val_loader, test_loader = create_dataloaders(config, tokenizer)
    logger.info(f"Dataset loaded: Train ({len(train_loader.dataset)}), Val ({len(val_loader.dataset)}), Test ({len(test_loader.dataset) if test_loader else 0})")
    
    model = build_model(
        pretrained_name=config["model"]["pretrained_name"],
        num_labels=config["task"]["num_labels"],
        id2label=config["task"]["id2label"],
        label2id=config["task"]["label2id"],
        dropout_rate=config["model"]["dropout_rate"]
    )
    
    tb_dir = os.path.join(log_dir, "tensorboard")
    writer = MetricWriter(tb_dir)
    
    trainer = Trainer(
        model=model,
        tokenizer=tokenizer,
        config=config,
        device=device,
        writer=writer
    )
    
    trainer.train(train_loader, val_loader, test_loader)
    writer.close()
    logger.info("Training pipeline finished successfully.")

if __name__ == "__main__":
    main()
