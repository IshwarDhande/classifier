import os
import csv

ROOT_DIR = '/home/eshwar/code/response'
DATA_DIR = os.path.join(ROOT_DIR, 'code/data/response_dataset')
OUT_DIR = os.path.join(DATA_DIR, 'combined')
os.makedirs(OUT_DIR, exist_ok=True)

UNIFIED_FIELDNAMES = [
    'utterance_id', 'utterance', 'response_category', 'category_no',
    'stage', 'split', 'task_or_scenario_id', 'parent_id', 'lineage',
    'variation_type', 'boundary_id', 'hard_negative_mechanism', 'source_file'
]

CAT_MAP = {
    'VP': ('very_positive', 4),
    'P': ('positive', 3),
    'I': ('indifferent', 2),
    'N': ('negative', 1),
    'VN': ('very_negative', 0),
    'VERY_POSITIVE': ('very_positive', 4),
    'POSITIVE': ('positive', 3),
    'INDIFFERENT': ('indifferent', 2),
    'NEGATIVE': ('negative', 1),
    'VERY_NEGATIVE': ('very_negative', 0)
}

def standardize_category(cat):
    c = cat.upper()
    if c in CAT_MAP:
        return CAT_MAP[c][0]
    return cat

def standardize_cat_no(cat):
    c = cat.upper()
    if c in CAT_MAP:
        return CAT_MAP[c][1]
    return -1

def read_csv(filepath):
    records = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)
    return records

def write_csv(filepath, records):
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=UNIFIED_FIELDNAMES, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for r in records:
            # only write unified fields
            row = {k: r.get(k, '') for k in UNIFIED_FIELDNAMES}
            writer.writerow(row)
    print(f"Written {len(records)} records to {filepath}")

def process_stage_1(records):
    # Already in unified schema format, just ensure completeness
    for r in records:
        r['response_category'] = standardize_category(r['response_category'])
    return records

def process_stage_3a(records):
    unified = []
    for r in records:
        u = {}
        u['utterance_id'] = r['utterance_id']
        u['utterance'] = r['utterance']
        u['response_category'] = standardize_category(r['response_category'])
        u['category_no'] = standardize_cat_no(r['response_category'])
        u['stage'] = '3A'
        u['split'] = r['split']
        u['task_or_scenario_id'] = r['scenario_id']
        u['parent_id'] = r['parent_anchor_id']
        u['lineage'] = r['lineage']
        u['variation_type'] = r['variation_type']
        u['boundary_id'] = ''
        u['hard_negative_mechanism'] = ''
        u['source_file'] = r['source_file']
        unified.append(u)
    return unified

def process_stage_2(records):
    unified = []
    for r in records:
        u = {}
        uid = r['utterance_id']
        u['utterance_id'] = uid
        u['utterance'] = r['utterance']
        u['response_category'] = standardize_category(r['response_category'])
        u['category_no'] = standardize_cat_no(r['response_category'])
        u['stage'] = '2'
        
        # S2 splitting by parent digit
        last_char = uid[-1]
        if last_char.isdigit():
            d = int(last_char)
            if d in [1, 2, 3, 4]:
                u['split'] = 'train'
            elif d == 5:
                u['split'] = 'validation'
            elif d == 6:
                u['split'] = 'test'
            else:
                u['split'] = 'train'
        else:
            u['split'] = 'train'
            
        u['task_or_scenario_id'] = r['task_domain']
        u['parent_id'] = ''
        u['lineage'] = ''
        u['variation_type'] = ''
        u['boundary_id'] = r['boundary_id']
        u['hard_negative_mechanism'] = ''
        u['source_file'] = r['source_file']
        unified.append(u)
    return unified

def process_stage_3b(records):
    unified = []
    for r in records:
        u = {}
        u['utterance_id'] = r['example_id']
        u['utterance'] = r['utterance']
        u['response_category'] = standardize_category(r['response_category'])
        u['category_no'] = standardize_cat_no(r['response_category'])
        u['stage'] = '3B'
        u['split'] = r['split']
        u['task_or_scenario_id'] = r['task_domain']
        u['parent_id'] = r['parent_id']
        u['lineage'] = r['lineage_id']
        u['variation_type'] = r['variation_type']
        u['boundary_id'] = r['boundary_id']
        u['hard_negative_mechanism'] = r['hard_negative_mechanism']
        # source_file wasn't saved in S3B previously! 
        # But we can leave blank if missing.
        u['source_file'] = r.get('source_file', '')
        unified.append(u)
    return unified

def main():
    print("Reading and standardizing datasets...")
    
    s1_raw = read_csv(os.path.join(DATA_DIR, 'dataset_1/stage_1_dataset.csv'))
    s1_clean = process_stage_1(s1_raw)
    
    s3a_raw = read_csv(os.path.join(DATA_DIR, 'dataset_3a/stage_3a_dataset.csv'))
    s3a_clean = process_stage_3a(s3a_raw)
    
    s2_raw = read_csv(os.path.join(DATA_DIR, 'dataset_2/stage_2_dataset.csv'))
    s2_clean = process_stage_2(s2_raw)
    
    s3b_raw = read_csv(os.path.join(DATA_DIR, 'dataset_3b/stage_3b_dataset.csv'))
    s3b_clean = process_stage_3b(s3b_raw)
    
    print("Combining datasets...")
    # 5. Stage 1 + Stage 3A
    s1_3a = s1_clean + s3a_clean
    write_csv(os.path.join(OUT_DIR, 'stage_1_and_3a_combined.csv'), s1_3a)
    
    # 6. Stage 2 + Stage 3B
    s2_3b = s2_clean + s3b_clean
    write_csv(os.path.join(OUT_DIR, 'stage_2_and_3b_combined.csv'), s2_3b)
    
    # 7. Complete Unified Corpus
    complete = s1_clean + s3a_clean + s2_clean + s3b_clean
    write_csv(os.path.join(OUT_DIR, 'complete_unified_corpus.csv'), complete)
    
    print("Successfully created unified combinations!")

if __name__ == '__main__':
    main()
