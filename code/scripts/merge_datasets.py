import csv, os

OUT_DIR = '/home/eshwar/code/response/code/data/execution_status'

cols = [
    'utterance_id', 'utterance', 'execution_status', 'status_no', 'stage', 'split',
    'task_or_scenario_id', 'parent_id', 'lineage', 'variation_type', 'boundary_id',
    'hard_negative_mechanism', 'target_task', 'semantic_subtype', 'context', 'source_file',
    'validation_status', 'ambiguity_flag'
]

def merge(files, outfile):
    records = []
    for f in files:
        with open(f, 'r') as fp:
            reader = csv.DictReader(fp)
            records.extend(list(reader))
    with open(outfile, 'w', newline='') as fp:
        writer = csv.DictWriter(fp, fieldnames=cols)
        writer.writeheader()
        writer.writerows(records)
    return records

r_1_3a = merge([
    f"{OUT_DIR}/dataset_1/stage_1_dataset.csv",
    f"{OUT_DIR}/dataset_3a/stage_3a_dataset.csv"
], f"{OUT_DIR}/stage_1_and_3a_combined.csv")

r_2_3b = merge([
    f"{OUT_DIR}/dataset_2/stage_2_dataset.csv",
    f"{OUT_DIR}/dataset_3b/stage_3b_dataset.csv"
], f"{OUT_DIR}/stage_2_and_3b_combined.csv")

r_all = merge([
    f"{OUT_DIR}/stage_1_and_3a_combined.csv",
    f"{OUT_DIR}/stage_2_and_3b_combined.csv"
], f"{OUT_DIR}/complete_unified_corpus.csv")

print(f"Merged successfully. Total unified records: {len(r_all)}")
print(f"Stage 1 & 3A: {len(r_1_3a)}")
print(f"Stage 2 & 3B: {len(r_2_3b)}")
