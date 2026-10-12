# BERT Sequence Classification Pipeline

This directory contains the training and evaluation pipeline for BERT (`bert-base-uncased`) classifiers across two dialogue perception tasks:
1. **Execution Status Classification** (3 classes: `Not Started`, `In Progress`, `Completed`)
2. **Response Category Classification** (5 classes: `very_negative`, `negative`, `indifferent`, `positive`, `very_positive`)

---

## Environment

This project is configured to use the `venv2` virtual environment:

- **Virtual Environment Path**: `/home/eshwar/code/simulator_persuasion/code/venv2`
- **Python Binary**: `/home/eshwar/code/simulator_persuasion/code/venv2/bin/python`

All CLI scripts in `scripts/` have shebangs pointing directly to `venv2` and can be executed directly.

---

## Directory Layout

```
code/
├── configs/
│   ├── base_config.yaml                      # Base hyperparameters & venv2 definition
│   ├── execution_status/
│   │   ├── dataset_2.yaml                    # Task 1 on dataset_2
│   │   └── combined.yaml                     # Task 1 on dataset_2 + srcc
│   └── response_category/
│       ├── dataset_2.yaml                    # Task 2 on dataset_2
│       └── combined.yaml                     # Task 2 on dataset_2 + srcc
├── data/
│   ├── execution_status/execution_status_training/
│   │   ├── dataset_2/                        # Original benchmark splits
│   │   └── combined/                         # Combined dataset_2 + srcc splits
│   └── response_dataset_training/
│       ├── dataset_2/                        # Original benchmark splits
│       └── combined/                         # Combined dataset_2 + srcc splits
├── src/                                      # Shared modular engine
│   ├── config.py
│   ├── dataset.py
│   ├── model.py
│   ├── trainer.py
│   ├── evaluator.py
│   └── utils.py
├── scripts/                                  # Executables
│   ├── train.py
│   ├── evaluate.py
│   ├── cross_evaluate.py
│   ├── predict.py
│   ├── run_execution_status.sh
│   ├── run_response_category.sh
│   └── run_all.sh
├── models/                                   # Saved best_model/ checkpoints
├── logs/                                     # train.log & scalars.json
└── reports/                                  # Metrics JSON, confusion matrix PNG, error CSV
```

---

## Quick Start

### 1. Run Execution Status Experiments
```bash
./code/scripts/run_execution_status.sh
```

### 2. Run Response Category Experiments
```bash
./code/scripts/run_response_category.sh
```

### 3. Run All Experiments
```bash
./code/scripts/run_all.sh
```

### 4. Interactive Utterance Prediction
```bash
./code/scripts/predict.py \
  --model_dir code/models/execution_status/combined/best_model \
  --text "I haven't started yet"
```
