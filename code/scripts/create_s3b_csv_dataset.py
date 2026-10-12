import os
import re
import csv
import glob

# Paths
ROOT_DIR = '/home/eshwar/code/response'
S3B_DIR = os.path.join(ROOT_DIR, 'research/s3b')
OUT_DIR = os.path.join(ROOT_DIR, 'code/data/response_dataset/dataset_3b')

os.makedirs(OUT_DIR, exist_ok=True)

def parse_s3b_files():
    all_records = []
    
    # Process all markdown files in the subdirectories
    md_files = []
    for root, dirs, files in os.walk(S3B_DIR):
        for f in files:
            if f.endswith('.md'):
                md_files.append(os.path.join(root, f))
                
    for fpath in md_files:
        filename = os.path.basename(fpath)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Determine track
        if filename.startswith('ba'):
            track = '2A'
        elif filename.startswith('mp'):
            track = '2B'
        elif filename.startswith('hn'):
            track = '2C'
        else:
            continue # skip audit report etc
            
        # Extract boundary from filename e.g. ba01_vp_p_variants.md -> VP, P
        m_fname = re.match(r'[a-z]+\d+_([a-z]+)_([a-z]+)', filename)
        if m_fname:
            cat1 = m_fname.group(1).upper()
            cat2 = m_fname.group(2).upper()
            boundary_cats = {cat1, cat2}
        else:
            boundary_cats = set()
            
        # Iterate over parent blocks
        # e.g., ## BA01-A01 — ... or ## MP01-01 or ## HN01-01
        parent_blocks = re.split(r'\n## (?=[A-Z0-9\-]+)', '\n' + content)
        
        for pblock in parent_blocks[1:]:
            p_lines = pblock.strip().split('\n')
            p_header = p_lines[0].strip()
            
            # Extract Parent ID
            m_pid = re.match(r'^([A-Z0-9\-]+)', p_header)
            if not m_pid:
                continue
            parent_id = m_pid.group(1)
            
            boundary_id = parent_id.split('-')[0] # e.g. BA01, MP01, HN01
            
            # Extract Task Domain
            m_task = re.search(r'\*\*Task:\*\*\s*(.+)', pblock)
            task_domain = m_task.group(1).strip() if m_task else ""
            
            # Extract Hard-negative mechanism (only in 2C, but we'll try)
            m_hn = re.search(r'\*\*Hard-negative mechanism:\*\*\s*(.+)', pblock)
            hn_mech = m_hn.group(1).strip() if m_hn else ""
            
            # Now find all variants inside this parent block
            vblocks = re.findall(
                r'###\s+([A-Z0-9\-]+-V\d+)\s+[—–-]\s+([A-Za-z]+)\n+(.*?)(?=\n###\s+[A-Z0-9\-]+-V\d+|\Z)',
                pblock,
                re.S
            )
            
            for vtag, vtype, vbody in vblocks:
                # Extract Lineage
                m_lin = re.search(r'-\s*\*\*Lineage:\*\*\s*(.+)', vbody)
                lineage_id = m_lin.group(1).split('→')[-1].strip() if m_lin else vtag
                
                # Extract Utterances
                sides = re.findall(r'\*\*([A-Z]+):\*\*\s*[“"]?([^”"\n]+)[”"]?', vbody)
                if not sides and "**User:**" in vbody:
                    # Single utterance case (Track 2A, Track 2C)
                    m_utt = re.search(r'\*\*User:\*\*\s*\n*[“"]?([^”"\n]+)[”"]?', vbody)
                    utt = m_utt.group(1).strip() if m_utt else ""
                    
                    m_lbl = re.search(r'\*\*Label:\*\*\s*`?([A-Z]+)`?', vbody)
                    label = m_lbl.group(1).strip() if m_lbl else ""
                    
                    sides = [(label, utt)]
                    
                for cat, utt in sides:
                    competing = list(boundary_cats - {cat})
                    closest_comp = competing[0] if competing else ""
                    
                    example_id = vtag if len(sides) == 1 else f"{vtag}-{cat}"
                    
                    all_records.append({
                        'example_id': example_id,
                        'parent_id': parent_id,
                        'lineage_id': lineage_id,
                        'boundary_id': boundary_id,
                        'track': track,
                        'response_category': cat,
                        'closest_competing_category': closest_comp,
                        'variation_type': vtype,
                        'hard_negative_mechanism': hn_mech,
                        'task_domain': task_domain,
                        'utterance': utt
                    })
                    
    return all_records

def assign_splits(records):
    for r in records:
        pid = r['parent_id'] # e.g. BA01-A01 or MP01-01
        last_digit = int(pid[-1])
        
        if last_digit in [1, 2, 3, 4]:
            r['split'] = 'train'
        elif last_digit == 5:
            r['split'] = 'validation'
        elif last_digit == 6:
            r['split'] = 'test'
        else:
            r['split'] = 'train' # fallback

def create_dataset():
    records = parse_s3b_files()
    assign_splits(records)
    
    fieldnames = [
        'example_id',
        'parent_id',
        'lineage_id',
        'boundary_id',
        'track',
        'response_category',
        'closest_competing_category',
        'variation_type',
        'hard_negative_mechanism',
        'task_domain',
        'utterance',
        'split'
    ]
    
    out_csv = os.path.join(OUT_DIR, 'stage_3b_dataset.csv')
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
    
    track_counts = {}
    split_counts = {}
    for r in records:
        track_counts[r['track']] = track_counts.get(r['track'], 0) + 1
        split_counts[r['split']] = split_counts.get(r['split'], 0) + 1
        
    print("\nTrack Distribution:")
    for k, v in sorted(track_counts.items()):
        print(f"  Track {k}: {v} utterances")
        
    print("\nSplit Distribution:")
    for k, v in split_counts.items():
        print(f"  {k:<10}: {v} examples ({v/len(records)*100:.1f}%)")

if __name__ == '__main__':
    create_dataset()
