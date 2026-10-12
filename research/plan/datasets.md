# Dataset Compilation Plan

First we will save datasets in `code/data/execution_status`.

**Methodology Reference:** Please refer to [`research/notes/generalized_dataset_methodology.md`](file:///home/eshwar/code/response/research/notes/generalized_dataset_methodology.md) for the mathematical splitting rules (Leakage-Safe Stratified Group Splitting) applied across these datasets.
## Target Datasets to Compile

Below is the list of datasets we need to build, along with their appropriate target names:

1. **Stage 1**  
   *Target Name:* `stage_1_dataset.csv`
2. **Stage 3A**  
   *Target Name:* `stage_3a_dataset.csv`
3. **Stage 2**  
   *Target Name:* `stage_2_dataset.csv`
4. **Stage 3B**  
   *Target Name:* `stage_3b_dataset.csv`
5. **Stage 1 + Stage 3A** (Combined)  
   *Target Name:* `stage_1_and_3a_combined.csv`
6. **Stage 2 + Stage 3B** (Combined)  
   *Target Name:* `stage_2_and_3b_combined.csv`
7. **Stage 1 + Stage 3A + Stage 2 + Stage 3B** (Full Unified Corpus)  
   *Target Name:* `complete_unified_corpus.csv`

---

## Existing Datasets Check

I have checked the `code/data/` folder. The following datasets **already exist** in the repository:

- **Stage 3A:** `code/data/response_dataset/dataset_3a/stage_3a_dataset.csv` (along with its train/val/test splits)
- **Stage 2:** `code/data/response_dataset/dataset_2/stage_2_dataset.csv` (and its individual track splits like `stage_2_ba.csv`, etc.)
- **Stage 3B:** `code/data/response_dataset/dataset_3b/stage_3b_dataset.csv` (along with its train/val/test splits)
- **Stage 1:** `code/data/response_dataset/dataset_1/stage_1_dataset.csv` (along with its train/val/test splits)

**Missing / To Be Generated:**
- Stage 1 standalone dataset (`stage_1_dataset.csv`)
- Combined Stage 1 + 3A dataset
- Combined Stage 2 + 3B dataset
- Full Unified Corpus (Stage 1 + 3A + 2 + 3B)

---

## Unified Master Schema

To successfully combine the datasets from different stages, we must standardize their columns into a single **Unified Master Schema**. Below is the target schema that all compilation and merge scripts will adopt:

| Column Name | Description | Source Stage Applicability |
| :--- | :--- | :--- |
| `utterance_id` | Unique identifier for the utterance (e.g., `VP-01-S01-V01`, `BA01-A01-V01`). Maps to `example_id` in S3B. | All |
| `utterance` | The actual text of the user's conversational response. | All |
| `response_category` | The ground-truth class label (`very_positive`, `positive`, `indifferent`, `negative`, `very_negative`). | All |
| `category_no` | Numeric encoding of the class (`4`, `3`, `2`, `1`, `0`). | All |
| `stage` | The pipeline stage that generated this row (`1`, `2`, `3A`, `3B`). | All |
| `split` | The dataset partition (`train`, `validation`, `test`) ensuring zero leakage. | All |
| `task_or_scenario_id` | The semantic scenario or task domain identifier (e.g., `VP-01-S01` or `Exercise`). | All |
| `parent_id` | The ID of the baseline/anchor utterance this variant was derived from. | 3A, 3B |
| `lineage` | The derivation path (e.g., `BA01-A01 → BA01-A01-V01`). | 3A, 3B |
| `variation_type` | The specific linguistic transformation applied (e.g., `LEX`, `SYN`, `CMK`). | 3A, 3B |
| `boundary_id` | The specific semantic boundary targeted (e.g., `BA01` for VP/P). | 2, 3B |
| `hard_negative_mechanism` | The distractor technique used (e.g., `Competing Keyword`). | 2 (HN), 3B (2C) |
| `source_file` | The original markdown file from which this data was parsed. | All |

*Note: Fields that are not applicable to a specific stage (e.g., `variation_type` for Stage 1 anchors) will be left blank (null) in the merged datasets.*

### Label Mapping Reference

When compiling the unified schema, ensure all `response_category` short-codes (VP, P, I, N, VN) are mapped to their standardized full-forms and correct `category_no`:

| Short Code (Legacy) | Standardized `response_category` | `category_no` |
| :--- | :--- | :--- |
| `VP` | `very_positive` | 4 |
| `P` | `positive` | 3 |
| `I` | `indifferent` | 2 |
| `N` | `negative` | 1 |
| `VN` | `very_negative` | 0 |
