import os
from typing import Dict, Any, Optional
import yaml

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def _deep_update(source: Dict[str, Any], overrides: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively updates a dictionary."""
    for key, val in overrides.items():
        if isinstance(val, dict) and key in source and isinstance(source[key], dict):
            source[key] = _deep_update(source[key], val)
        else:
            source[key] = val
    return source

def resolve_path(path_str: str) -> str:
    """Converts a relative path to absolute relative to repository root."""
    if os.path.isabs(path_str):
        return path_str
    return os.path.join(ROOT_DIR, path_str)

def load_config(config_path: str, base_config_path: Optional[str] = None) -> Dict[str, Any]:
    """Loads a task YAML config, merging it with base_config.yaml."""
    if base_config_path is None:
        base_config_path = os.path.join(ROOT_DIR, "code", "configs", "base_config.yaml")
        
    config: Dict[str, Any] = {}
    if os.path.exists(base_config_path):
        with open(base_config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f) or {}
            
    full_config_path = resolve_path(config_path)
    if not os.path.exists(full_config_path):
        raise FileNotFoundError(f"Configuration file not found: {full_config_path}")
        
    with open(full_config_path, "r", encoding="utf-8") as f:
        task_config = yaml.safe_load(f) or {}
        
    config = _deep_update(config, task_config)
    
    # Resolve relative paths
    if "data" in config:
        for k in ["train_file", "val_file", "test_file"]:
            if k in config["data"]:
                config["data"][k] = resolve_path(config["data"][k])
                
    if "paths" in config:
        for k in ["output_dir", "log_dir", "report_dir"]:
            if k in config["paths"]:
                config["paths"][k] = resolve_path(config["paths"][k])
                
    # Build label mapping
    if "task" in config and "labels" in config["task"]:
        labels = config["task"]["labels"]
        config["task"]["label2id"] = {lbl: idx for idx, lbl in enumerate(labels)}
        config["task"]["id2label"] = {idx: lbl for idx, lbl in enumerate(labels)}
        config["task"]["num_labels"] = len(labels)
        
    return config
