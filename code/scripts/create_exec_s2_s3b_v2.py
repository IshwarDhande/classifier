import glob, os, yaml, re, csv

OUT_DIR = '/home/eshwar/code/response/code/data/execution_status'
S2_DIR = '/home/eshwar/code/response/research/execution_status/s2'
S3B_DIR = '/home/eshwar/code/response/research/execution_status/s3b'

status_map = {
    'Not Started': 2,
    'In Progress': 1,
    'Completed': 0
}

def get_split(family_id):
    m = re.search(r'\d+', family_id)
    if m:
        num = int(m.group())
        mod = num % 5
        if mod in [1, 2, 3]: return 'train'
        if mod == 4: return 'validation'
        return 'test'
    return 'train'

def process_file(f, stage):
    records = []
    fname = os.path.basename(f)
    if "audit_report" in f: return []
    
    with open(f, 'r') as fp: content = fp.read()
    
    boundary_id = ""
    m_b = re.search(r'(B0[1-3])', content)
    if m_b: boundary_id = m_b.group(1)
    
    subtype = ""
    if "ba" in f or "boundary_anchor" in f: subtype = "boundary_anchor"
    elif "mp" in f or "minimal_pair" in f: subtype = "minimal_pair"
    elif "hn" in f or "hard_negative" in f: subtype = "hard_negative"
    
    def add_rec(utt, st, meta=None):
        if not utt or not st: return
        if meta is None: meta = {}
        # Avoid duplicate exact same utt
        for r in records:
            if r['utterance'] == utt: return
            
        r = {
            'utterance_id': meta.get('example_id', ''),
            'utterance': utt,
            'execution_status': st,
            'status_no': status_map.get(st, ''),
            'stage': stage,
            'split': get_split(meta.get('lineage_id', fname)),
            'task_or_scenario_id': meta.get('lineage_id', ''),
            'target_task': meta.get('target_task', ''),
            'semantic_subtype': subtype,
            'parent_id': meta.get('parent_id', ''),
            'lineage': meta.get('lineage_id', ''),
            'variation_type': meta.get('variation_type', ''),
            'boundary_id': boundary_id,
            'hard_negative_mechanism': '',
            'context': meta.get('context', ''),
            'source_file': fname,
            'validation_status': meta.get('validation_status', 'candidate'),
            'ambiguity_flag': str(meta.get('ambiguity_flag', 'false'))
        }
        records.append(r)

    # 1. YAML blocks
    yaml_blocks = re.findall(r'```yaml\n(.*?)\n```', content, re.DOTALL)
    for b in yaml_blocks:
        try:
            parsed = yaml.safe_load(b)
            if 'utterance' in parsed:
                add_rec(parsed['utterance'], parsed.get('execution_status'), parsed)
        except: pass
        
    # 2. Markdown lists (- **Utterance:** "...")
    # Usually these are preceded by - **Execution Status:** `...`
    blocks = re.split(r'\*\*BA\d+-\d+-V\d+.*?\*\*', content)
    for b in blocks[1:]:
        st_match = re.search(r'-\s*\*\*Execution Status:\*\*\s*`(.*?)`', b)
        utt_match = re.search(r'-\s*\*\*Utterance:\*\*\s*[“"]([^”"\n]+)[”"]', b)
        if st_match and utt_match:
            add_rec(utt_match.group(1), st_match.group(1))

    # 3. Stage 2 style blocks (**State:** \n > "..." or "...")
    s2_matches = re.finditer(r'\*\*(Not Started|In Progress|Completed):\*\*\s*\n(?:>\s*)?[“"]?([^”"\n]+)[”"]?', content)
    for m in s2_matches:
        add_rec(m.group(2).strip(), m.group(1))
        
    # 4. List format (- **State:** "...")
    lf_matches = re.finditer(r'-\s*\*\*(Not Started|In Progress|Completed):\*\*\s*[“"]([^”"\n]+)[”"]', content)
    for m in lf_matches:
        add_rec(m.group(2), m.group(1))
        
    # 5. Blockquotes (> "...") - these are tricky because there's no state attached directly.
    # Actually, in HN01, it is grouped under **Parent state:** Not Started
    # Let's split by "Parent state:"
    ps_blocks = re.split(r'\*\*Parent state:\*\*\s*(Not Started|In Progress|Completed)', content)
    for i in range(1, len(ps_blocks), 2):
        st = ps_blocks[i]
        b = ps_blocks[i+1]
        bq_matches = re.finditer(r'>\s*[“"]([^”"\n]+)[”"]', b)
        for m in bq_matches:
            add_rec(m.group(1), st)
            
    # For Stage 2 BA Tables
    for line in content.split('\n'):
        if line.strip().startswith('|') and 'BA0' in line:
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 6:
                st = parts[4].replace('`','')
                if st in status_map:
                    add_rec(parts[5], st)

    return records

s2_files = sorted(glob.glob(f'{S2_DIR}/**/*.md', recursive=True))
s3b_files = sorted(glob.glob(f'{S3B_DIR}/**/*.md', recursive=True))

s2_records = []
for f in s2_files: s2_records.extend(process_file(f, '2'))
s3b_records = []
for f in s3b_files: s3b_records.extend(process_file(f, '3B'))

columns = [
    'utterance_id', 'utterance', 'execution_status', 'status_no', 'stage', 'split',
    'task_or_scenario_id', 'parent_id', 'lineage', 'variation_type', 'boundary_id',
    'hard_negative_mechanism', 'target_task', 'semantic_subtype', 'context', 'source_file',
    'validation_status', 'ambiguity_flag'
]

with open(f'{OUT_DIR}/dataset_2/stage_2_dataset.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()
    for row in s2_records: writer.writerow({k: row.get(k, '') for k in columns})

with open(f'{OUT_DIR}/dataset_3b/stage_3b_dataset.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()
    for row in s3b_records: writer.writerow({k: row.get(k, '') for k in columns})

print(f"Generated {len(s2_records)} Stage 2 records and {len(s3b_records)} Stage 3B records.")
