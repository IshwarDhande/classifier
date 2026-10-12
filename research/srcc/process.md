# SRCC Data Pipeline Process

Here is a step-by-step summary of the entire data pipeline executed for the SRCC dataset:

1. **Cleaned Filenames**
   We removed the `srcc_` prefix from all the markdown files in the `research/srcc` directory. This cleaned up the file names (e.g., `01_srcc_vp_1word.md` became `01_vp_1word.md`), while intentionally skipping `srcc.md` so it wouldn't be corrupted into a `.md` file.

2. **Aggregated the Unified Corpus** 
   We read through all the individual markdown files, parsed the tabular data, and extracted the data rows containing the ID, Expression, and Category. We then compiled this into a single CSV file: `code/data/srcc/response_srcc.csv`.

3. **Renamed the Corpus File**
   We renamed the aggregated file to `response_srcc_unified_corpus.csv` to better reflect its purpose as the master dataset.

4. **Standardized Column Headers**
   We updated the headers in the unified CSV to align with the project's naming conventions. We changed `Expression` to `utterance` and `Category` to `response_category`. 

5. **Expanded Category Labels**
   We mapped the short-form category acronyms found in the `response_category` column to their full, snake_case names (`VP` -> `very_positive`, `P` -> `positive`, `I` -> `indifferent`, `N` -> `negative`, `VN` -> `very_negative`), matching the exact styling found in the reference `test.csv` file.

6. **Applied Leakage-Safe Stratified Splitting**
   Following the principles in `generalized_dataset_methodology.md`, we split the unified corpus into `train.csv`, `val.csv`, and `test.csv` files. To prevent semantic leakage, we used the base scenario ID (the numeric suffix `001` through `020`) as the grouping key.
   - **Train (70%)**: Scenarios `001` to `014` (all variants)
   - **Validation (15%)**: Scenarios `015` to `017` (all variants)
   - **Test (15%)**: Scenarios `018` to `020` (all variants)
   
7. **Shuffled & Sequenced the Splits**
   Finally, in each of the three new split CSVs, we randomly shuffled the rows so the data wasn't ordered by category or length. We then renamed the first column from `ID` to `serial_id` and assigned fresh, sequential zero-padded numeric IDs (e.g., `001`, `002`, `003`...) to every row.
