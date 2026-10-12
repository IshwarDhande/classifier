import os
import csv
import random
from collections import defaultdict

ROOT_DIR = '/home/eshwar/code/response'

def stratified_split(records, label_key, train_ratio=0.70, val_ratio=0.15, seed=42):
    random.seed(seed)
    by_class = defaultdict(list)
    for r in records:
        by_class[r[label_key]].append(r)
    
    train_records = []
    val_records = []
    test_records = []
    
    for cls, items in sorted(by_class.items()):
        shuffled = list(items)
        random.shuffle(shuffled)
        n = len(shuffled)
        n_train = int(round(n * train_ratio))
        n_val = int(round(n * val_ratio))
        
        # Ensure at least 1 in val and test if n is large enough
        if n >= 3 and n_val == 0:
            n_val = 1
        if n >= 3 and (n - n_train - n_val) == 0:
            n_train = n - 2
            n_val = 1
            
        train_records.extend(shuffled[:n_train])
        val_records.extend(shuffled[n_train:n_train + n_val])
        test_records.extend(shuffled[n_train + n_val:])
        
    return train_records, val_records, test_records

def load_csv(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def save_csv(filepath, records, fieldnames):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for idx, r in enumerate(records, start=1):
            row = dict(r)
            row['serial_id'] = f"{idx:04d}"
            writer.writerow({k: row[k] for k in fieldnames})
    print(f"Saved {len(records)} rows to {filepath}")

def build_response_combined():
    d2_dir = os.path.join(ROOT_DIR, 'code/data/response_dataset_training/dataset_2')
    srcc_file = os.path.join(ROOT_DIR, 'code/data/srcc/response_srcc_unified_corpus.csv')
    out_dir = os.path.join(ROOT_DIR, 'code/data/response_dataset_training/combined')
    
    d2_train = load_csv(os.path.join(d2_dir, 'train.csv'))
    d2_val = load_csv(os.path.join(d2_dir, 'val.csv'))
    d2_test = load_csv(os.path.join(d2_dir, 'test.csv'))
    
    srcc_raw = load_csv(srcc_file)
    srcc_clean = []
    for r in srcc_raw:
        srcc_clean.append({
            'utterance': r['utterance'].strip(),
            'response_category': r['response_category'].strip()
        })
        
    srcc_train, srcc_val, srcc_test = stratified_split(
        srcc_clean, label_key='response_category', train_ratio=0.70, val_ratio=0.15, seed=42
    )
    
    fieldnames = ['serial_id', 'utterance', 'response_category']
    save_csv(os.path.join(out_dir, 'train.csv'), d2_train + srcc_train, fieldnames)
    save_csv(os.path.join(out_dir, 'val.csv'), d2_val + srcc_val, fieldnames)
    save_csv(os.path.join(out_dir, 'test.csv'), d2_test + srcc_test, fieldnames)
    print("Response Category combined dataset created successfully.")

def build_execution_status_combined():
    d2_dir = os.path.join(ROOT_DIR, 'code/data/execution_status/execution_status_training/dataset_2')
    srcc_file = os.path.join(ROOT_DIR, 'code/data/execution_status/srcc/execution_status_srcc_unified_corpus.csv')
    out_dir = os.path.join(ROOT_DIR, 'code/data/execution_status/execution_status_training/combined')
    
    d2_train = load_csv(os.path.join(d2_dir, 'train.csv'))
    d2_val = load_csv(os.path.join(d2_dir, 'val.csv'))
    d2_test = load_csv(os.path.join(d2_dir, 'test.csv'))
    
    exec_label_map = {
        'not_started': 'Not Started',
        'in_progress': 'In Progress',
        'completed': 'Completed'
    }
    
    srcc_raw = load_csv(srcc_file)
    srcc_clean = []
    for r in srcc_raw:
        raw_label = r['execution_status'].strip()
        mapped_label = exec_label_map.get(raw_label.lower(), raw_label)
        srcc_clean.append({
            'utterance': r['utterance'].strip(),
            'execution_status': mapped_label
        })
        
    srcc_train, srcc_val, srcc_test = stratified_split(
        srcc_clean, label_key='execution_status', train_ratio=0.70, val_ratio=0.15, seed=42
    )
    
    fieldnames = ['serial_id', 'utterance', 'execution_status']
    save_csv(os.path.join(out_dir, 'train.csv'), d2_train + srcc_train, fieldnames)
    save_csv(os.path.join(out_dir, 'val.csv'), d2_val + srcc_val, fieldnames)
    save_csv(os.path.join(out_dir, 'test.csv'), d2_test + srcc_test, fieldnames)
    print("Execution Status combined dataset created successfully.")

if __name__ == '__main__':
    build_response_combined()
    build_execution_status_combined()
