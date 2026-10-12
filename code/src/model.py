import os
from typing import Dict, Tuple
from transformers import AutoConfig, AutoModelForSequenceClassification, AutoTokenizer

def build_tokenizer(pretrained_name: str = "bert-base-uncased") -> AutoTokenizer:
    """Loads tokenizer from pretrained checkpoint or local path."""
    tokenizer = AutoTokenizer.from_pretrained(pretrained_name)
    return tokenizer

def build_model(
    pretrained_name: str,
    num_labels: int,
    id2label: Dict[int, str],
    label2id: Dict[str, int],
    dropout_rate: float = 0.1
) -> AutoModelForSequenceClassification:
    """Builds BERT sequence classification model with label mappings."""
    config = AutoConfig.from_pretrained(
        pretrained_name,
        num_labels=num_labels,
        id2label=id2label,
        label2id=label2id,
        classifier_dropout=dropout_rate
    )
    
    model = AutoModelForSequenceClassification.from_pretrained(
        pretrained_name,
        config=config
    )
    return model

def save_model_and_tokenizer(
    model: AutoModelForSequenceClassification,
    tokenizer: AutoTokenizer,
    output_dir: str
) -> None:
    """Saves serialized weights, huggingface config, and tokenizer files."""
    os.makedirs(output_dir, exist_ok=True)
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)

def load_model_and_tokenizer(
    model_dir: str
) -> Tuple[AutoModelForSequenceClassification, AutoTokenizer]:
    """Loads saved model and tokenizer from artifact directory."""
    if not os.path.exists(model_dir):
        raise FileNotFoundError(f"Model directory not found at: {model_dir}")
        
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForSequenceClassification.from_pretrained(model_dir)
    return model, tokenizer
