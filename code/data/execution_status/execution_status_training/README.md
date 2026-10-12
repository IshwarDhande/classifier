# Execution Status Training Datasets

This directory contains the final formatted training data splits (`dataset_1` and `dataset_2`) used for training Execution Status classifiers.

## Data Structure

Each dataset folder contains the following split files:
- `train.csv` (~70%)
- `val.csv` (~15%)
- `test.csv` (~15%)

Additionally, the original master CSV files used for generating these splits are also preserved within these folders for reference.

### Columns

The CSV files have been streamlined and formatted for training with the following columns:
- `serial_id`: A unique, incrementally generated 3-digit identifier for each utterance (e.g., `001`, `002`, `003`). This replaces the original verbose `utterance_id`.
- `utterance`: The natural language string representing the user's conversational input.
- `execution_status`: The target classification label (`Not Started`, `In Progress`, `Completed`).

## Split Methodology

The train/val/test splits were deterministically generated using a **Leakage-Safe Stratified Group Splitting** algorithm. This ensures that the classifier learns true communicative abstractions rather than exploiting surface-level shortcuts or memorizing specific scenarios.

1. **Group Splitting by Scenario (No Leakage):** 
   The grouping key used during splitting is the base `task_or_scenario_id`. All generated linguistic realizations (e.g., Lexical, Syntactic, Conversational variants) derived from the exact same base scenario are strictly mapped to the **same split**. This guarantees zero semantic leakage across the train, validation, and test boundaries.
   
2. **Stratified by Class & Subtype:**
   The splits maintain the target 70/15/15 ratios consistently across both the `execution_status` classes and the underlying `semantic_subtype`. This guarantees that every semantic difficulty tier or boundary type is adequately exposed during training, while the validation and test sets evaluate completely novel base scenarios within those same subtypes.
