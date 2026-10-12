import os
import sys
import random
import logging
import numpy as np
import torch

def set_seed(seed: int = 42) -> None:
    """Sets random seed across all libraries for deterministic reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False

def get_device() -> torch.device:
    """Selects the best available device (cuda or cpu)."""
    if torch.cuda.is_available():
        device = torch.device("cuda")
        logging.info(f"Using GPU device: {torch.cuda.get_device_name(0)}")
    else:
        device = torch.device("cpu")
        logging.info("Using CPU device.")
    return device

def setup_logger(name: str, log_dir: str, log_filename: str = "train.log") -> logging.Logger:
    """Configures structured logging to stdout and log file."""
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, log_filename)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    # Console Handler
    c_handler = logging.StreamHandler(sys.stdout)
    c_handler.setFormatter(formatter)
    logger.addHandler(c_handler)
    
    # File Handler
    f_handler = logging.FileHandler(log_path, mode="a", encoding="utf-8")
    f_handler.setFormatter(formatter)
    logger.addHandler(f_handler)
    
    return logger

class MetricWriter:
    """Telemetry writer tracking epoch metrics into JSON and TensorBoard if available."""
    def __init__(self, log_dir: str):
        self.log_dir = log_dir
        self.history = {}
        os.makedirs(log_dir, exist_ok=True)
        self.tb_writer = None
        
        # Suppress any noisy stderr on import if tensorboard/tf has numpy 2.0 version conflicts
        try:
            devnull = open(os.devnull, 'w')
            old_stderr = os.dup(2)
            os.dup2(devnull.fileno(), 2)
            try:
                from torch.utils.tensorboard import SummaryWriter
                self.tb_writer = SummaryWriter(log_dir)
            finally:
                os.dup2(old_stderr, 2)
                os.close(old_stderr)
                devnull.close()
        except Exception:
            self.tb_writer = None

    def add_scalar(self, tag: str, scalar_value: float, step: int) -> None:
        if tag not in self.history:
            self.history[tag] = []
        self.history[tag].append({"step": step, "value": float(scalar_value)})
        if self.tb_writer is not None:
            try:
                self.tb_writer.add_scalar(tag, scalar_value, step)
            except Exception:
                pass

    def close(self) -> None:
        import json
        history_path = os.path.join(self.log_dir, "scalars.json")
        with open(history_path, "w", encoding="utf-8") as f:
            json.dump(self.history, f, indent=2)
        if self.tb_writer is not None:
            try:
                self.tb_writer.close()
            except Exception:
                pass

