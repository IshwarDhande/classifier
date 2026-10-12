import os
import re
import csv
import glob

# Paths
ROOT_DIR = '/home/eshwar/code/response'
S1_DIR = os.path.join(ROOT_DIR, 'research/s1')
S3A_DIR = os.path.join(ROOT_DIR, 'research/s3a')
OUT_DIR = os.path.join(ROOT_DIR, 'code/data/response_dataset/dataset_3a')

os.makedirs(OUT_DIR, exist_ok=True)

CATEGORY_NAMES = {
    'VP': 'Very Positive',
    'P': 'Positive',
    'I': 'Indifferent',
    'N': 'Negative',
    'VN': 'Very Negative'
}

ORDINAL_LABELS = {
    'VN': 0,
    'N': 1,
    'I': 2,
    'P': 3,
    'VP': 4
}

def parse_stage1_metadata():
    s1_files = {
        'VP': os.path.join(S1_DIR, '03_semantic_scenarios_vp.md'),
        'P': os.path.join(S1_DIR, '04_semantic_scenarios_p.md'),
        'I': os.path.join(S1_DIR, '05_semantic_scenarios_i.md'),
        'N': os.path.join(S1_DIR, '06_semantic_scenarios_n.md'),
        'VN': os.path.join(S1_DIR, '07_semantic_scenarios_vn.md'),
    }
    
    scenarios_meta = {}
    
    for cat, path in s1_files.items():
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
            
        sections = re.split(r'\n## (?=[A-Z0-9\-]+ — )', text)
        for sec in sections[1:]:
            lines = sec.strip().split('\n')
            header = lines[0].strip()
            parts = header.split(' — ')
            scen_id = parts[0].strip()
            scen_name = parts[1].strip() if len(parts) > 1 else ''
            
            scen_desc_m = re.search(r'\*\*Scenario:\*\*\s*([^\n]+(?:\n(?!\*\*)[^\n]+)*)', sec)
            beh_core_m = re.search(r'\*\*Behavioral core:\*\*\s*([^\n]+(?:\n(?!\*\*)[^\n]+)*)', sec)
            boundary_m = re.search(r'\*\*Boundary:\*\*\s*([^\n]+(?:\n(?!\*\*)[^\n]+)*)', sec)
            
            scen_desc = " ".join([l.strip() for l in scen_desc_m.group(1).split('\n') if l.strip()]) if scen_desc_m else ''
            beh_core = " ".join([l.strip() for l in beh_core_m.group(1).split('\n') if l.strip()]) if beh_core_m else ''
            boundary = " ".join([l.strip() for l in boundary_m.group(1).split('\n') if l.strip()]) if boundary_m else ''
            
            scenarios_meta[scen_id] = {
                'scenario_name': scen_name,
                'scenario_description': scen_desc,
                'behavioral_core': beh_core,
                'boundary': boundary
            }
            
    print(f"Loaded metadata for {len(scenarios_meta)} Stage 1 scenarios.")
    return scenarios_meta

def parse_stage3a_files():
    variant_files = [
        'stage_3a_vp_a_s01_s10_variants.md',
        'stage_3a_vp_b_s11_s20_variants.md',
        'stage_3a_p_a_s01_s10_variants.md',
        'stage_3a_p_b_s11_s20_variants.md',
        'stage_3a_i_a_s01_s10_variants.md',
        'stage_3a_i_b_s11_s20_variants.md',
        'stage_3a_n_a_s01_s10_variants.md',
        'stage_3a_n_b_s11_s20_variants.md',
        'stage_3a_vn_a_s01_s10_variants.md',
        'stage_3a_vn_b_s11_s20_variants.md'
    ]
    
    record_pattern = re.compile(
        r'###\s+([A-Z0-9\-]+-V\d+)\s*—\s*`?([A-Z]{3})`?'
        r'.*?'
        r'-\s*\*\*Parent [Aa]nchor:\*\*\s*`?([A-Z0-9\-]+)`?'
        r'.*?'
        r'-\s*\*\*Variation [Tt]ype:\*\*\s*`?([A-Z]{3})`?'
        r'.*?'
        r'-\s*\*\*Lineage:\*\*\s*([^\n]+)'
        r'.*?'
        r'-\s*\*\*Utterance:\*\*\s*[“"]?([^”"\n]+)[”"]?',
        re.DOTALL
    )
    
    all_records = []
    
    for fname in variant_files:
        fpath = os.path.join(S3A_DIR, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        m_cat = re.search(r'stage_3a_([a-z]+)_[ab]_', fname)
        cat = m_cat.group(1).upper()
        
        matches = record_pattern.findall(content)
        if len(matches) != 60:
            raise ValueError(f"File {fname} yielded {len(matches)} matches, expected 60!")
            
        for m in matches:
            ex_id = m[0].strip()
            # scenario_id: VP-01-S01 from VP-01-S01-V01
            parts = ex_id.split('-')
            scen_id = "-".join(parts[:3])
            subtype = "-".join(parts[:2])
            
            p_anchor = m[2].strip().replace('`', '').strip()
            var_type = m[3].strip().replace('`', '').strip()
            lineage = m[4].strip().replace('`', '').strip()
            utt = m[5].strip().strip('“').strip('”').strip('"').strip()
            
            all_records.append({
                'utterance_id': ex_id,
                'scenario_id': scen_id,
                'semantic_subtype': subtype,
                'label': CATEGORY_NAMES[cat],
                'response_category': cat,
                'category_no': ORDINAL_LABELS[cat],
                'parent_anchor_id': p_anchor,
                'variation_type': var_type,
                'lineage': lineage,
                'utterance': utt,
                'stage': '3A',
                'source_file': fname
            })
            
    print(f"Extracted {len(all_records)} variants across all 10 files.")
    return all_records

def assign_splits(records):
    # Leakage-safe scenario family split matching generalized_dataset_methodology.md Section 2.2:
    # 70% Train (14 scenarios per class = 420 variants total)
    # 15% Validation (3 scenarios per class = 90 variants total)
    # 15% Test (3 scenarios per class = 90 variants total)
    #
    # Subtype Allocation Matrix (Per Class):
    # Subtype 1 (S01-S05): S01, S02, S03 (Train) | S04 (Val) | S05 (Test)
    # Subtype 2 (S01-S05): S01, S02, S03, S04 (Train) | S05 (Val) | — (Test: 0)
    # Subtype 3 (S01-S05): S01, S02, S03, S04 (Train) | — (Val: 0) | S05 (Test)
    # Subtype 4 (S01-S05): S01, S02, S03 (Train) | S04 (Val) | S05 (Test)
    
    for r in records:
        scen_id = r['scenario_id']
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
            raise ValueError(f"Unexpected subtype number {st_num} in {scen_id}")

def create_dataset():
    s1_meta = parse_stage1_metadata()
    records = parse_stage3a_files()
    assign_splits(records)
    
    # Merge metadata
    for r in records:
        sid = r['scenario_id']
        meta = s1_meta.get(sid, {})
        r['scenario_name'] = meta.get('scenario_name', '')
        r['scenario_description'] = meta.get('scenario_description', '')
        r['behavioral_core'] = meta.get('behavioral_core', '')
        r['boundary'] = meta.get('boundary', '')
        
    # Schema columns: First five are utterance_id, utterance, label, response_category, category_no
    fieldnames = [
        'utterance_id',
        'utterance',
        'label',
        'response_category',
        'category_no',
        'scenario_id',
        'scenario_name',
        'semantic_subtype',
        'variation_type',
        'parent_anchor_id',
        'lineage',
        'behavioral_core',
        'scenario_description',
        'boundary',
        'stage',
        'split',
        'source_file'
    ]
    
    out_csv = os.path.join(OUT_DIR, 'stage_3a_dataset.csv')
    with open(out_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for r in records:
            writer.writerow(r)
            
    print(f"Written primary dataset to {out_csv}")
    
    # Also export individual split files matching methodology Section 5:
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
    

    
    # Print Verification & Statistics
    print("\n" + "="*80)
    print("DATASET VERIFICATION & STATISTICAL AUDIT")
    print("="*80)
    print(f"Total Rows: {len(records)}")
    print(f"Columns: {len(fieldnames)}")
    
    # Category distribution
    cat_counts = {}
    split_counts = {}
    cat_split_counts = {}
    
    for r in records:
        c = r['response_category']
        s = r['split']
        cat_counts[c] = cat_counts.get(c, 0) + 1
        split_counts[s] = split_counts.get(s, 0) + 1
        key = (c, s)
        cat_split_counts[key] = cat_split_counts.get(key, 0) + 1
        
    print("\nClass Distribution:")
    for c in ['VP', 'P', 'I', 'N', 'VN']:
        print(f"  {c:<4} ({CATEGORY_NAMES[c]:<14}): {cat_counts.get(c, 0)} examples ({cat_counts.get(c, 0)/len(records)*100:.1f}%)")
        
    print("\nSplit Distribution:")
    for s in ['train', 'validation', 'test']:
        print(f"  {s:<12}: {split_counts.get(s, 0)} examples ({split_counts.get(s, 0)/len(records)*100:.1f}%)")
        
    print("\nCategory x Split Matrix:")
    print(f"{'Category':<6} | {'Train':<7} | {'Val':<7} | {'Test':<7} | {'Total':<7}")
    print("-" * 40)
    for c in ['VP', 'P', 'I', 'N', 'VN']:
        tr = cat_split_counts.get((c, 'train'), 0)
        va = cat_split_counts.get((c, 'validation'), 0)
        te = cat_split_counts.get((c, 'test'), 0)
        tot = tr + va + te
        print(f"{c:<6} | {tr:<7} | {va:<7} | {te:<7} | {tot:<7}")

if __name__ == '__main__':
    create_dataset()
