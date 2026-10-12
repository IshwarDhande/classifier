import os
import re
import csv
import glob

# Paths
ROOT_DIR = '/home/eshwar/code/response'
S1_DIR = os.path.join(ROOT_DIR, 'research/s1/anchors')
OUT_DIR = os.path.join(ROOT_DIR, 'code/data/response_dataset/dataset_1')

os.makedirs(OUT_DIR, exist_ok=True)

CAT_MAP = {
    'VP': ('very_positive', 4),
    'P': ('positive', 3),
    'I': ('indifferent', 2),
    'N': ('negative', 1),
    'VN': ('very_negative', 0)
}

def parse_s1_files():
    all_records = []
    
    md_files = glob.glob(os.path.join(S1_DIR, '*.md'))
    
    for fpath in md_files:
        filename = os.path.basename(fpath)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Example filename: 01_initial_anchors_vp.md
        # Determine cat short code
        m_fname = re.search(r'initial_anchors_([a-z]+)\.md', filename)
        if not m_fname:
            continue
        cat_short = m_fname.group(1).upper()
        if cat_short not in CAT_MAP:
            continue
            
        full_cat, cat_no = CAT_MAP[cat_short]
        
        # Iterate over scenario blocks
        # e.g., ## VP-01-S01 — ...
        scenario_blocks = re.split(r'\n## (?=[A-Z]{1,2}-\d{2}-S\d{2})', '\n' + content)
        
        for sblock in scenario_blocks[1:]:
            s_lines = sblock.strip().split('\n')
            s_header = s_lines[0].strip()
            
            # Extract Scenario ID (e.g. VP-01-S01)
            m_sid = re.match(r'^([A-Z]{1,2}-\d{2}-S\d{2})', s_header)
            if not m_sid:
                continue
            scenario_id = m_sid.group(1)
            
            # Extract Direct
            m_direct = re.search(r'\*\*Direct:\*\*\s*\n[“"]?([^”"\n]+)[”"]?', sblock)
            if m_direct:
                all_records.append({
                    'utterance_id': f"{scenario_id}-A1",
                    'utterance': m_direct.group(1).strip(),
                    'response_category': full_cat,
                    'category_no': cat_no,
                    'stage': '1',
                    'task_or_scenario_id': scenario_id,
                    'source_file': filename
                })
                
            # Extract Indirect
            m_indirect = re.search(r'\*\*Indirect:\*\*\s*\n[“"]?([^”"\n]+)[”"]?', sblock)
            if m_indirect:
                all_records.append({
                    'utterance_id': f"{scenario_id}-A2",
                    'utterance': m_indirect.group(1).strip(),
                    'response_category': full_cat,
                    'category_no': cat_no,
                    'stage': '1',
                    'task_or_scenario_id': scenario_id,
                    'source_file': filename
                })
                
            # Extract Natural Conversational
            m_natural = re.search(r'\*\*Natural Conversational:\*\*\s*\n[“"]?([^”"\n]+)[”"]?', sblock)
            if m_natural:
                all_records.append({
                    'utterance_id': f"{scenario_id}-A3",
                    'utterance': m_natural.group(1).strip(),
                    'response_category': full_cat,
                    'category_no': cat_no,
                    'stage': '1',
                    'task_or_scenario_id': scenario_id,
                    'source_file': filename
                })
                
    return all_records

def assign_splits(records):
    # Leakage-safe scenario family split matching generalized_dataset_methodology.md
    for r in records:
        scen_id = r['task_or_scenario_id']
        parts = scen_id.split('-')
        st_num = int(parts[1]) # 01, 02, 03, 04
        scen_num = int(parts[2][1:]) # 1, 2, 3, 4, 5
        
        if st_num == 1:
            if scen_num in [1, 2, 3]:
                r['split'] = 'train'
            elif scen_num == 4:
                r['split'] = 'validation'
            elif scen_num == 5:
                r['split'] = 'test'
        elif st_num == 2:
            if scen_num in [1, 2, 3, 4]:
                r['split'] = 'train'
            elif scen_num == 5:
                r['split'] = 'validation'
        elif st_num == 3:
            if scen_num in [1, 2, 3, 4]:
                r['split'] = 'train'
            elif scen_num == 5:
                r['split'] = 'test'
        elif st_num == 4:
            if scen_num in [1, 2, 3]:
                r['split'] = 'train'
            elif scen_num == 4:
                r['split'] = 'validation'
            elif scen_num == 5:
                r['split'] = 'test'
        else:
            r['split'] = 'train' # fallback

def create_dataset():
    records = parse_s1_files()
    assign_splits(records)
    
    # Fill in unified schema fields with null/blank where not applicable
    for r in records:
        r.setdefault('parent_id', '')
        r.setdefault('lineage', '')
        r.setdefault('variation_type', '')
        r.setdefault('boundary_id', '')
        r.setdefault('hard_negative_mechanism', '')
    
    fieldnames = [
        'utterance_id',
        'utterance',
        'response_category',
        'category_no',
        'stage',
        'split',
        'task_or_scenario_id',
        'parent_id',
        'lineage',
        'variation_type',
        'boundary_id',
        'hard_negative_mechanism',
        'source_file'
    ]
    
    out_csv = os.path.join(OUT_DIR, 'stage_1_dataset.csv')
    with open(out_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for r in records:
            writer.writerow(r)
            
    print(f"Written primary dataset to {out_csv}")
    
    train_records = [r for r in records if r['split'] == 'train']
    val_records = [r for r in records if r['split'] == 'validation']
    test_records = [r for r in records if r['split'] == 'test']
    
    for split_name, split_data in [('train.csv', train_records), ('val.csv', val_records), ('test.csv', test_records)]:
        split_path = os.path.join(OUT_DIR, split_name)
        with open(split_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()
            for r in split_data:
                writer.writerow(r)
        print(f"Written {split_name} ({len(split_data)} rows) to {split_path}")
        
    print("\n" + "="*80)
    print("DATASET VERIFICATION & STATISTICAL AUDIT")
    print("="*80)
    print(f"Total Utterances: {len(records)}")
    
    split_counts = {}
    for r in records:
        split_counts[r['split']] = split_counts.get(r['split'], 0) + 1
        
    print("\nSplit Distribution:")
    for k, v in split_counts.items():
        print(f"  {k:<10}: {v} examples ({v/len(records)*100:.1f}%)")

if __name__ == '__main__':
    create_dataset()
