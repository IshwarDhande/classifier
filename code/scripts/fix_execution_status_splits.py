#!/home/eshwar/code/simulator_persuasion/code/venv2/bin/python
"""
Extracts canonical, leakage-safe 70/15/15 splits from complete_unified_corpus.csv
into code/data/execution_status/execution_status_training/dataset_2/
strictly adhering to generalized_dataset_methodology.md
"""

import os
import pandas as pd

ROOT_DIR = "/home/eshwar/code/response"
MASTER_CSV = os.path.join(ROOT_DIR, "code/data/execution_status/complete_unified_corpus.csv")
OUT_DIR = os.path.join(ROOT_DIR, "code/data/execution_status/execution_status_training/dataset_2")

def main():
    print(f"Reading master corpus from: {MASTER_CSV}")
    df = pd.read_csv(MASTER_CSV)
    
    # Verify columns
    assert "split" in df.columns, "split column missing from master"
    assert "utterance" in df.columns, "utterance column missing from master"
    assert "execution_status" in df.columns, "execution_status column missing from master"
    
    # Verify zero scenario leakage in master
    if "task_or_scenario_id" in df.columns:
        scenarios_by_split = df.groupby("task_or_scenario_id")["split"].nunique()
        leaking = (scenarios_by_split > 1).sum()
        assert leaking == 0, f"Found {leaking} leaking scenarios in master!"
        print("[Pass] Verified 0 scenario leakage across master splits.")
        
    split_map = {
        "train": "train.csv",
        "validation": "val.csv",
        "test": "test.csv"
    }
    
    os.makedirs(OUT_DIR, exist_ok=True)
    
    for split_val, filename in split_map.items():
        subset = df[df["split"] == split_val].copy().reset_index(drop=True)
        subset["serial_id"] = [f"{i:04d}" for i in range(1, len(subset) + 1)]
        
        out_df = subset[["serial_id", "utterance", "execution_status"]]
        out_path = os.path.join(OUT_DIR, filename)
        out_df.to_csv(out_path, index=False)
        
        class_dist = out_df["execution_status"].value_counts().to_dict()
        pct = (len(out_df) / len(df)) * 100
        print(f"Exported {filename} -> {len(out_df)} rows ({pct:.1f}%) | Classes: {class_dist}")

if __name__ == "__main__":
    main()
