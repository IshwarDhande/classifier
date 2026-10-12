import os
import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer
from typing import Dict, List, Tuple, Any, Optional

def normalize_label_str(val: Any) -> str:
    """Normalizes label string for case/format agnostic matching."""
    s = str(val).strip().lower().replace("_", " ")
    return " ".join(s.split())

class TextClassificationDataset(Dataset):
    """PyTorch Dataset for BERT sequence classification."""
    
    def __init__(
        self,
        csv_file: str,
        tokenizer: AutoTokenizer,
        text_column: str,
        label_column: str,
        label2id: Dict[str, int],
        max_length: int = 128
    ):
        if not os.path.exists(csv_file):
            raise FileNotFoundError(f"Dataset CSV not found at: {csv_file}")
            
        self.df = pd.read_csv(csv_file)
        self.tokenizer = tokenizer
        self.text_column = text_column
        self.label_column = label_column
        self.max_length = max_length
        self.label2id = label2id
        
        # Build normalized lookup map: normalized_label -> id
        self.norm_label_map = {}
        for original_lbl, lbl_id in self.label2id.items():
            self.norm_label_map[normalize_label_str(original_lbl)] = lbl_id
            
        # Clean dataframe
        self.df[self.text_column] = self.df[self.text_column].fillna("").astype(str)
        self.df = self.df[self.df[self.text_column].str.strip() != ""].reset_index(drop=True)
        
        # Validate and convert labels
        self.labels = []
        for raw_val in self.df[self.label_column]:
            norm_val = normalize_label_str(raw_val)
            if norm_val not in self.norm_label_map:
                raise ValueError(
                    f"Label '{raw_val}' (normalized '{norm_val}') in {csv_file} not in configured labels: {list(self.label2id.keys())}"
                )
            self.labels.append(self.norm_label_map[norm_val])

    def __len__(self) -> int:
        return len(self.df)

    def __getitem__(self, idx: int) -> Dict[str, torch.Tensor]:
        utterance = self.df.iloc[idx][self.text_column]
        target_label = self.labels[idx]
        
        encoding = self.tokenizer(
            utterance,
            truncation=True,
            padding="max_length",
            max_length=self.max_length,
            return_tensors="pt"
        )
        
        item = {
            "input_ids": encoding["input_ids"].squeeze(0),
            "attention_mask": encoding["attention_mask"].squeeze(0),
            "labels": torch.tensor(target_label, dtype=torch.long),
            "utterance": utterance
        }
        
        if "token_type_ids" in encoding:
            item["token_type_ids"] = encoding["token_type_ids"].squeeze(0)
            
        return item

def collate_fn(batch: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Custom collator handling string utterances alongside tensors."""
    input_ids = torch.stack([item["input_ids"] for item in batch])
    attention_mask = torch.stack([item["attention_mask"] for item in batch])
    labels = torch.stack([item["labels"] for item in batch])
    utterances = [item["utterance"] for item in batch]
    
    batch_dict = {
        "input_ids": input_ids,
        "attention_mask": attention_mask,
        "labels": labels,
        "utterance": utterances
    }
    
    if "token_type_ids" in batch[0]:
        batch_dict["token_type_ids"] = torch.stack([item["token_type_ids"] for item in batch])
        
    return batch_dict

def create_dataloaders(
    config: Dict[str, Any],
    tokenizer: AutoTokenizer
) -> Tuple[DataLoader, DataLoader, Optional[DataLoader]]:
    """Creates train, validation, and test PyTorch DataLoaders."""
    text_col = config["task"]["text_column"]
    label_col = config["task"]["label_column"]
    label2id = config["task"]["label2id"]
    max_len = config["model"]["max_seq_length"]
    train_bs = config["training"]["batch_size"]
    eval_bs = config["training"]["eval_batch_size"]
    
    train_dataset = TextClassificationDataset(
        csv_file=config["data"]["train_file"],
        tokenizer=tokenizer,
        text_column=text_col,
        label_column=label_col,
        label2id=label2id,
        max_length=max_len
    )
    
    val_dataset = TextClassificationDataset(
        csv_file=config["data"]["val_file"],
        tokenizer=tokenizer,
        text_column=text_col,
        label_column=label_col,
        label2id=label2id,
        max_length=max_len
    )
    
    test_dataset = None
    if config["data"].get("test_file") and os.path.exists(config["data"]["test_file"]):
        test_dataset = TextClassificationDataset(
            csv_file=config["data"]["test_file"],
            tokenizer=tokenizer,
            text_column=text_col,
            label_column=label_col,
            label2id=label2id,
            max_length=max_len
        )
        
    train_loader = DataLoader(
        train_dataset,
        batch_size=train_bs,
        shuffle=True,
        collate_fn=collate_fn,
        drop_last=False
    )
    
    val_loader = DataLoader(
        val_dataset,
        batch_size=eval_bs,
        shuffle=False,
        collate_fn=collate_fn,
        drop_last=False
    )
    
    test_loader = None
    if test_dataset:
        test_loader = DataLoader(
            test_dataset,
            batch_size=eval_bs,
            shuffle=False,
            collate_fn=collate_fn,
            drop_last=False
        )
        
    return train_loader, val_loader, test_loader
