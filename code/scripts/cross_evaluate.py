#!/home/eshwar/code/simulator_persuasion/code/venv2/bin/python
import os
import sys
import json
import argparse
import pandas as pd
import torch
from torch.utils.data import DataLoader

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.model import load_model_and_tokenizer
from src.dataset import TextClassificationDataset, collate_fn
from src.evaluator import compute_metrics
from src.utils import get_device

def evaluate_on_file(model, tokenizer, csv_file, text_col, label_col, device):
    id2label = model.config.id2label
    label2id = model.config.label2id
    label_names = [id2label[i] if i in id2label else id2label[str(i)] for i in range(len(label2id))]
    
    dataset = TextClassificationDataset(
        csv_file=csv_file,
        tokenizer=tokenizer,
        text_column=text_col,
        label_column=label_col,
        label2id=label2id,
        max_length=128
    )
    loader = DataLoader(dataset, batch_size=64, shuffle=False, collate_fn=collate_fn)
    
    y_true, y_pred = [], []
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
            
    metrics = compute_metrics(y_true, y_pred, label_names)
    return {
        "accuracy": round(metrics["accuracy"], 4),
        "macro_f1": round(metrics["macro_f1"], 4),
        "samples": len(dataset)
    }

def main():
    parser = argparse.ArgumentParser(description="Cross-dataset transfer evaluation.")
    parser.add_argument("--task", type=str, choices=["execution_status", "response_category"], required=True)
    parser.add_argument("--d2_model_dir", type=str, required=True, help="Model trained on dataset_2")
    parser.add_argument("--combined_model_dir", type=str, required=True, help="Model trained on combined")
    parser.add_argument("--output_file", type=str, default=None)
    args = parser.parse_args()
    
    device = get_device()
    
    if args.task == "execution_status":
        text_col = "utterance"
        label_col = "execution_status"
        test_sets = {
            "d2_test": "code/data/execution_status/execution_status_training/dataset_2/test.csv",
            "combined_test": "code/data/execution_status/execution_status_training/combined/test.csv",
            "srcc_test": "code/data/execution_status/srcc/test.csv"
        }
    else:
        text_col = "utterance"
        label_col = "response_category"
        test_sets = {
            "d2_test": "code/data/response_dataset_training/dataset_2/test.csv",
            "combined_test": "code/data/response_dataset_training/combined/test.csv",
            "srcc_test": "code/data/srcc/test.csv"
        }
        
    print(f"\n=======================================================")
    print(f" CROSS-DATASET EVALUATION: {args.task.upper()}")
    print(f"=======================================================")
    
    models = {
        "Trained_on_dataset_2": args.d2_model_dir,
        "Trained_on_combined": args.combined_model_dir
    }
    
    results = {}
    for mod_name, mod_dir in models.items():
        if not os.path.exists(mod_dir):
            print(f"Skipping {mod_name}: path does not exist {mod_dir}")
            continue
        print(f"Loading {mod_name} from {mod_dir}...")
        model, tokenizer = load_model_and_tokenizer(mod_dir)
        model.to(device).eval()
        
        results[mod_name] = {}
        for test_name, test_path in test_sets.items():
            if os.path.exists(test_path):
                res = evaluate_on_file(model, tokenizer, test_path, text_col, label_col, device)
                results[mod_name][test_name] = res
                print(f"  [{test_name}] (N={res['samples']}) -> Acc: {res['accuracy']:.4f} | Macro F1: {res['macro_f1']:.4f}")
                
    if args.output_file:
        os.makedirs(os.path.dirname(args.output_file), exist_ok=True)
        with open(args.output_file, "w") as f:
            json.dump(results, f, indent=2)
        print(f"\nSaved cross-evaluation summary to {args.output_file}")

if __name__ == "__main__":
    main()
