# Execution Status SRCC Data Pipeline Process

Here is a step-by-step summary of the entire data pipeline executed for the Execution Status SRCC dataset:

1. **Cleaned Filenames**
   We removed the `srcc_` prefix from all the markdown files in the `research/execution_status/srcc` directory. This cleaned up the file names (e.g., `01_srcc_ns_1word.md` became `01_ns_1word.md`), while intentionally skipping the master `.md` file so it wouldn't be corrupted.

2. **Aggregated the Unified Corpus** 
   We read through all the individual markdown files, parsed the tabular data, and extracted the data rows containing the ID, Expression, and Category. We then compiled this into a single CSV file: `code/data/execution_status/srcc/execution_status_srcc_unified_corpus.csv`.

3. **Standardized Column Headers**
   We updated the headers in the unified CSV to align with the project's naming conventions. The columns are now `ID`, `utterance`, and `execution_status`. 

4. **Expanded Category Labels**
   We mapped the short-form category acronyms found in the `execution_status` column to their full, snake_case names (`NS` -> `not_started`, `IP` -> `in_progress`, `C` -> `completed`).

5. **Applied Leakage-Safe Stratified Splitting**
   Following the principles in `generalized_dataset_methodology.md`, we split the unified corpus into `train.csv`, `val.csv`, and `test.csv` files. To prevent semantic leakage, we used the base scenario ID (the numeric suffix `01` through `20`) as the grouping key.
   - **Train (70%)**: Scenarios `01` to `14` (all variants)
   - **Validation (15%)**: Scenarios `15` to `17` (all variants)
   - **Test (15%)**: Scenarios `18` to `20` (all variants)
   
6. **Shuffled & Sequenced the Splits**
   Finally, in each of the three new split CSVs, we randomly shuffled the rows so the data wasn't ordered by category or length. We then renamed the first column from `ID` to `serial_id` and assigned fresh, sequential zero-padded numeric IDs (e.g., `001`, `002`, `003`...) to every row.
