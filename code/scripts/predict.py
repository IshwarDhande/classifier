#!/home/eshwar/code/simulator_persuasion/code/venv2/bin/python
import os
import sys
import argparse
import torch
import torch.nn.functional as F
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.model import load_model_and_tokenizer
from src.utils import get_device

def predict_single(model, tokenizer, text: str, device):
    inputs = tokenizer(
        text,
        truncation=True,
        padding="max_length",
        max_length=128,
        return_tensors="pt"
    ).to(device)
    
    with torch.no_grad():
        logits = model(**inputs).logits
        probs = F.softmax(logits, dim=1).squeeze(0)
        pred_idx = torch.argmax(probs).item()
        
    id2label = model.config.id2label
    label_name = id2label[pred_idx] if pred_idx in id2label else id2label[str(pred_idx)]
    
    confidences = {}
    for idx, p in enumerate(probs):
        lbl = id2label[idx] if idx in id2label else id2label[str(idx)]
        confidences[lbl] = round(p.item(), 4)
        
    return label_name, confidences

def main():
    parser = argparse.ArgumentParser(description="Run inference using a trained BERT classifier.")
    parser.add_argument("--model_dir", type=str, required=True, help="Path to saved best_model directory.")
    parser.add_argument("--text", type=str, default=None, help="Single utterance to classify.")
    parser.add_argument("--input_csv", type=str, default=None, help="Input CSV file for batch inference.")
    parser.add_argument("--text_col", type=str, default="utterance", help="Text column name for batch inference.")
    parser.add_argument("--output_csv", type=str, default=None, help="Output CSV path for batch predictions.")
    args = parser.parse_args()
    
    device = get_device()
    model, tokenizer = load_model_and_tokenizer(args.model_dir)
    model.to(device).eval()
    
    if args.text:
        pred_label, confs = predict_single(model, tokenizer, args.text, device)
        print(f"\nUtterance: \"{args.text}\"")
        print(f"Predicted Class: {pred_label}")
        print(f"Class Probabilities: {confs}\n")
        
    if args.input_csv:
        df = pd.read_csv(args.input_csv)
        if args.text_col not in df.columns:
            raise ValueError(f"Column '{args.text_col}' not found in {args.input_csv}")
            
        preds = []
        confidences = []
        for text in df[args.text_col]:
            p_lbl, conf = predict_single(model, tokenizer, str(text), device)
            preds.append(p_lbl)
            confidences.append(conf[p_lbl])
            
        df["predicted_label"] = preds
        df["prediction_confidence"] = confidences
        
        out_csv = args.output_csv or args.input_csv.replace(".csv", "_predictions.csv")
        os.makedirs(os.path.dirname(os.path.abspath(out_csv)), exist_ok=True)
        df.to_csv(out_csv, index=False)
        print(f"Batch predictions saved to: {out_csv}")

if __name__ == "__main__":
    main()
