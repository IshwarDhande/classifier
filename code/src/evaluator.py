import os
import json
from typing import Dict, List, Any, Optional
import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    classification_report,
    confusion_matrix
)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def compute_metrics(
    y_true: List[int],
    y_pred: List[int],
    label_names: List[str]
) -> Dict[str, Any]:
    """Computes comprehensive classification metrics."""
    acc = float(accuracy_score(y_true, y_pred))
    
    macro_p, macro_r, macro_f1, _ = precision_recall_fscore_support(
        y_true, y_pred, average="macro", zero_division=0
    )
    weighted_p, weighted_r, weighted_f1, _ = precision_recall_fscore_support(
        y_true, y_pred, average="weighted", zero_division=0
    )
    
    cls_report = classification_report(
        y_true,
        y_pred,
        target_names=label_names,
        output_dict=True,
        zero_division=0
    )
    
    cm = confusion_matrix(y_true, y_pred, labels=list(range(len(label_names)))).tolist()
    
    return {
        "accuracy": acc,
        "macro_f1": float(macro_f1),
        "macro_precision": float(macro_p),
        "macro_recall": float(macro_r),
        "weighted_f1": float(weighted_f1),
        "weighted_precision": float(weighted_p),
        "weighted_recall": float(weighted_r),
        "per_class": cls_report,
        "confusion_matrix": cm,
        "label_names": label_names
    }

def plot_confusion_matrix(
    cm: List[List[int]],
    label_names: List[str],
    output_path: str,
    title: str = "Confusion Matrix"
) -> None:
    """Plots and saves normalized confusion matrix heatmap."""
    cm_arr = np.array(cm, dtype=float)
    row_sums = cm_arr.sum(axis=1, keepdims=True)
    # Avoid zero division
    norm_cm = np.divide(cm_arr, row_sums, out=np.zeros_like(cm_arr), where=row_sums != 0)
    
    fig, ax = plt.subplots(figsize=(8, 6), dpi=150)
    cax = ax.matshow(norm_cm, cmap="Blues", alpha=0.85)
    fig.colorbar(cax)
    
    num_classes = len(label_names)
    ax.set_xticks(range(num_classes))
    ax.set_yticks(range(num_classes))
    ax.set_xticklabels(label_names, rotation=45, ha="left", fontsize=9)
    ax.set_yticklabels(label_names, fontsize=9)
    
    ax.set_xlabel("Predicted Label", fontweight="bold", labelpad=10)
    ax.set_ylabel("True Label", fontweight="bold", labelpad=10)
    ax.set_title(title, pad=20, fontweight="bold")
    
    # Annotate counts and percentages in each cell
    for i in range(num_classes):
        for j in range(num_classes):
            raw_val = int(cm_arr[i, j])
            pct_val = norm_cm[i, j]
            text = f"{raw_val}\n({pct_val:.1%})"
            color = "white" if pct_val > 0.5 else "black"
            ax.text(j, i, text, ha="center", va="center", color=color, fontsize=8)
            
    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()

def save_evaluation_artifacts(
    metrics: Dict[str, Any],
    y_true: List[int],
    y_pred: List[int],
    utterances: List[str],
    label_names: List[str],
    report_dir: str,
    prefix: str = "test"
) -> Dict[str, str]:
    """Saves metrics JSON, confusion matrix PNG, and error analysis CSV."""
    os.makedirs(report_dir, exist_ok=True)
    
    # 1. Save JSON metrics
    metrics_path = os.path.join(report_dir, f"{prefix}_metrics.json")
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)
        
    # 2. Save Confusion Matrix plot
    cm_path = os.path.join(report_dir, f"{prefix}_confusion_matrix.png")
    plot_confusion_matrix(
        cm=metrics["confusion_matrix"],
        label_names=label_names,
        output_path=cm_path,
        title=f"{prefix.title()} Confusion Matrix"
    )
    
    # 3. Save Error Analysis CSV
    error_csv_path = os.path.join(report_dir, f"{prefix}_error_analysis.csv")
    records = []
    for idx, (utt, true_id, pred_id) in enumerate(zip(utterances, y_true, y_pred), start=1):
        true_name = label_names[true_id]
        pred_name = label_names[pred_id]
        records.append({
            "sample_id": idx,
            "utterance": utt,
            "true_label": true_name,
            "predicted_label": pred_name,
            "is_correct": true_id == pred_id
        })
        
    df_err = pd.DataFrame(records)
    df_err.to_csv(error_csv_path, index=False)
    
    # Also save filtered misclassifications only
    misclass_csv_path = os.path.join(report_dir, f"{prefix}_misclassified_samples.csv")
    df_misclass = df_err[~df_err["is_correct"]]
    df_misclass.to_csv(misclass_csv_path, index=False)
    
    return {
        "metrics_json": metrics_path,
        "confusion_matrix": cm_path,
        "error_analysis_csv": error_csv_path,
        "misclassified_csv": misclass_csv_path
    }
