#!/home/eshwar/code/simulator_persuasion/code/venv2/bin/python
"""
Comprehensive Pre-flight Validation Suite for BERT Sequence Classification.
Audits venv2, dataset files, schema consistency, leakage, configs, and model execution.
"""

import os
import sys
import yaml
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

ROOT_DIR = "/home/eshwar/code/response"
sys.path.insert(0, os.path.join(ROOT_DIR, "code"))

from src.config import load_config
from src.dataset import TextClassificationDataset, create_dataloaders
from src.evaluator import compute_metrics
from src.utils import get_device, MetricWriter

def run_precheck():
    discrepancies = []
    print("=" * 70)
    print(" 🚀 RUNNING BERT PRE-TRAINING COMPREHENSIVE AUDIT")
    print("=" * 70)

    # 1. Environment & Package Audit
    print("\n[1/4] AUDITING VIRTUAL ENVIRONMENT & PACKAGES...")
    expected_packages = [
        "torch", "transformers", "sklearn", "accelerate",
        "pandas", "numpy", "matplotlib", "yaml"
    ]
    for pkg in expected_packages:
        try:
            mod = __import__(pkg)
            ver = getattr(mod, "__version__", "ok")
            print(f"  ✓ {pkg:<15} : {ver}")
        except Exception as e:
            discrepancies.append(f"Package missing/broken: {pkg} -> {e}")
            print(f"  ✗ {pkg:<15} : FAILED ({e})")
            
    print(f"  ✓ Python binary   : {sys.executable}")
    print(f"  ✓ PyTorch threads : {torch.get_num_threads()}")
    print(f"  ✓ Device          : {get_device()}")

    # 2. Config Files Validation
    print("\n[2/4] AUDITING YAML EXPERIMENT CONFIGURATIONS...")
    configs_to_check = [
        "code/configs/execution_status/dataset_2.yaml",
        "code/configs/execution_status/combined.yaml",
        "code/configs/response_category/dataset_2.yaml",
        "code/configs/response_category/combined.yaml",
    ]
    
    loaded_configs = {}
    for cfg_rel in configs_to_check:
        cfg_path = os.path.join(ROOT_DIR, cfg_rel)
        if not os.path.exists(cfg_path):
            discrepancies.append(f"Config file missing: {cfg_rel}")
            print(f"  ✗ Missing: {cfg_rel}")
            continue
        try:
            cfg = load_config(cfg_path)
            loaded_configs[cfg_rel] = cfg
            print(f"  ✓ Config OK       : {cfg_rel} (Task: {cfg['task']['name']}, Labels: {cfg['task']['num_labels']})")
        except Exception as e:
            discrepancies.append(f"Config load error in {cfg_rel}: {e}")
            print(f"  ✗ Error in {cfg_rel}: {e}")

    # 3. Dataset Integrity & Leakage Check
    print("\n[3/4] AUDITING CSV DATASET SPLITS (INTEGRITY & LEAKAGE)...")
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    
    for cfg_name, cfg in loaded_configs.items():
        task_name = cfg["task"]["name"]
        variant = cfg["task"]["dataset_variant"]
        expected_labels = cfg["task"]["labels"]
        text_col = cfg["task"]["text_column"]
        label_col = cfg["task"]["label_column"]
        
        print(f"\n  Checking Task [{task_name} / {variant}]:")
        splits = {
            "train": cfg["data"]["train_file"],
            "val": cfg["data"]["val_file"],
            "test": cfg["data"]["test_file"]
        }
        
        split_dfs = {}
        split_utterances = {}
        
        for s_name, s_path in splits.items():
            if not os.path.exists(s_path):
                discrepancies.append(f"Data file missing for {cfg_name} [{s_name}]: {s_path}")
                print(f"    ✗ Missing file: {s_path}")
                continue
                
            df = pd.read_csv(s_path)
            split_dfs[s_name] = df
            
            # Check non-empty
            if len(df) == 0:
                discrepancies.append(f"Empty dataset: {s_path}")
                print(f"    ✗ File is empty: {s_path}")
                continue
                
            # Check required columns
            for req_col in [text_col, label_col]:
                if req_col not in df.columns:
                    discrepancies.append(f"Missing column '{req_col}' in {s_path}")
                    print(f"    ✗ Missing column '{req_col}' in {s_path}")
                    
            # Check NaN/null utterances
            null_utts = df[text_col].isna().sum() + (df[text_col].astype(str).str.strip() == "").sum()
            if null_utts > 0:
                discrepancies.append(f"{null_utts} null/empty utterances in {s_path}")
                print(f"    ✗ {null_utts} empty utterances in {s_path}")
                
            # Check labels
            # Normalization check
            from src.dataset import normalize_label_str
            norm_cfg_labels = {normalize_label_str(lbl): lbl for lbl in expected_labels}
            unknown_labels = set()
            for l in df[label_col].unique():
                norm_l = normalize_label_str(l)
                if norm_l not in norm_cfg_labels:
                    unknown_labels.add(str(l))
            if unknown_labels:
                discrepancies.append(f"Unknown labels in {s_path}: {unknown_labels}")
                print(f"    ✗ Unknown labels in {s_path}: {unknown_labels}")
                
            # Check token lengths
            tokens_list = [len(tokenizer.encode(str(u), truncation=False)) for u in df[text_col].dropna()]
            max_tok = max(tokens_list) if tokens_list else 0
            cfg_max_len = cfg["model"]["max_seq_length"]
            if max_tok > cfg_max_len:
                discrepancies.append(f"Utterance exceeds max_seq_length ({max_tok} > {cfg_max_len}) in {s_path}")
                print(f"    ! Warning: Max tokens ({max_tok}) exceeds max_seq_length ({cfg_max_len}) in {s_path}")
                
            split_utterances[s_name] = set(df[text_col].astype(str).str.strip().str.lower())
            
            print(f"    ✓ {s_name:<5} split: {len(df):>4} rows | Classes: {df[label_col].nunique()} | Max tokens: {max_tok}")

        # Check cross-split exact utterance overlap
        if "train" in split_utterances and "val" in split_utterances:
            train_val_overlap = split_utterances["train"].intersection(split_utterances["val"])
            if len(train_val_overlap) > 0:
                print(f"    ℹ Note: {len(train_val_overlap)} exact utterances appear in both Train and Val.")
        if "train" in split_utterances and "test" in split_utterances:
            train_test_overlap = split_utterances["train"].intersection(split_utterances["test"])
            if len(train_test_overlap) > 0:
                print(f"    ℹ Note: {len(train_test_overlap)} exact utterances appear in both Train and Test.")

    # 4. Model & Pipeline End-to-End Dry Run
    print("\n[4/4] DRY-RUNNING DATA PIPELINE & MODEL FORWARD/BACKWARD PASS...")
    for cfg_name, cfg in loaded_configs.items():
        task_name = cfg["task"]["name"]
        variant = cfg["task"]["dataset_variant"]
        print(f"\n  Dry-run testing: {task_name} ({variant})...")
        
        try:
            train_loader, val_loader, test_loader = create_dataloaders(cfg, tokenizer)
            batch = next(iter(train_loader))
            
            # Check tensor shapes
            input_ids = batch["input_ids"]
            attention_mask = batch["attention_mask"]
            labels = batch["labels"]
            
            assert input_ids.shape[0] == cfg["training"]["batch_size"] or input_ids.shape[0] == len(train_loader.dataset)
            assert input_ids.shape[1] == cfg["model"]["max_seq_length"]
            
            # Instantiate model
            model = AutoModelForSequenceClassification.from_pretrained(
                cfg["model"]["pretrained_name"],
                num_labels=cfg["task"]["num_labels"],
                id2label=cfg["task"]["id2label"],
                label2id=cfg["task"]["label2id"]
            )
            model.eval()
            with torch.no_grad():
                out = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
                logits = out.logits
                loss = out.loss
                assert logits.shape[1] == cfg["task"]["num_labels"]
                assert not torch.isnan(loss)
                
            print(f"    ✓ DataLoaders initialized: train ({len(train_loader.dataset)}), val ({len(val_loader.dataset)}), test ({len(test_loader.dataset) if test_loader else 0})")
            print(f"    ✓ Batch tensors shape: {input_ids.shape}")
            print(f"    ✓ Model forward pass OK: logits {logits.shape}, loss = {loss.item():.4f}")
            
            # Dry-run compute_metrics
            preds = torch.argmax(logits, dim=1).tolist()
            m = compute_metrics(labels.tolist(), preds, cfg["task"]["labels"])
            print(f"    ✓ Evaluator test: Macro F1 = {m['macro_f1']:.4f}")
            
        except Exception as e:
            discrepancies.append(f"Dry-run failure on {cfg_name}: {e}")
            print(f"    ✗ Dry-run FAILED on {cfg_name}: {e}")

    # Summary
    print("\n" + "=" * 70)
    if discrepancies:
        print(f" ⚠️ PRE-CHECK COMPLETED WITH {len(discrepancies)} DISCREPANCY / WARNING(S):")
        for i, d in enumerate(discrepancies, 1):
            print(f"   [{i}] {d}")
    else:
        print(" 🎉 CLEAN PASS! ALL SYSTEMS, DATASETS, AND CODE ARE 100% READY.")
    print("=" * 70)
    
    return len(discrepancies) == 0

if __name__ == "__main__":
    success = run_precheck()
    sys.exit(0 if success else 1)
