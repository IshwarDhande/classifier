import glob, os, yaml, re, csv

OUT_DIR = '/home/eshwar/code/response/code/data/execution_status'
S2_DIR = '/home/eshwar/code/response/research/execution_status/s2'
S3B_DIR = '/home/eshwar/code/response/research/execution_status/s3b'
os.makedirs(f"{OUT_DIR}/dataset_2", exist_ok=True)
os.makedirs(f"{OUT_DIR}/dataset_3b", exist_ok=True)

status_map = {
    'Not Started': 2,
    'In Progress': 1,
    'Completed': 0
}

def get_split(family_id):
    m = re.search(r'\d+', family_id.split('-')[-1])
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
    
    # 1. YAML BLOCKS
    yaml_blocks = re.findall(r'```yaml\n(.*?)\n```', content, re.DOTALL)
    for b in yaml_blocks:
        try:
            parsed = yaml.safe_load(b)
            if 'utterance' not in parsed: continue
            
            status = parsed.get('execution_status', '')
            family_id = str(parsed.get('lineage_id', parsed.get('parent_id', '')))
            
            record = {
                'utterance_id': parsed.get('example_id', ''),
                'utterance': parsed.get('utterance', ''),
                'execution_status': status,
                'status_no': status_map.get(status, ''),
                'stage': stage,
                'split': get_split(family_id),
                'task_or_scenario_id': family_id,
                'target_task': parsed.get('target_task', ''),
                'semantic_subtype': subtype,
                'parent_id': parsed.get('parent_id', ''),
                'lineage': parsed.get('lineage_id', ''),
                'variation_type': parsed.get('variation_type', ''),
                'boundary_id': boundary_id,
                'hard_negative_mechanism': '',
                'context': parsed.get('context', ''),
                'source_file': fname,
                'validation_status': parsed.get('validation_status', ''),
                'ambiguity_flag': str(parsed.get('ambiguity_flag', 'false'))
            }
            records.append(record)
        except Exception as e:
            pass

    # 2. Markdown Tables
    lines = content.split('\n')
    for line in lines:
        if line.strip().startswith('|') and len(line.split('|')) >= 5:
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 6 and parts[1].startswith(('BA', 'MP', 'HN')):
                ex_id = parts[1]
                status = parts[4] if parts[4] in status_map else parts[3]
                if status not in status_map: continue
                utt = parts[5] if parts[4] in status_map else parts[4]
                if "candidate" in utt or "Variant" in utt:
                    utt = parts[3]
                    status = parts[2]
                if status not in status_map:
                    # check if status is in parts[3]
                    if parts[3] in status_map:
                        status = parts[3]
                        utt = parts[4]
                        
                # It's tricky to parse markdown tables generally, let's look for explicit "candidate"
                if "candidate" in line:
                    utt = parts[3] if len(parts) > 3 else ""
                    # Actually if stage 3B, it's mostly yaml. 
                    # Stage 2 BA has a table: | ID | Anchor Type | Task | Execution Status | Utterance |
                    if "BA01-" in ex_id or "BA02-" in ex_id or "BA03-" in ex_id:
                        status = parts[4] if parts[4].replace('`','') in status_map else ""
                        status = status.replace('`','')
                        utt = parts[5]
                        
                family_id = ex_id
                
                if status in status_map:
                    record = {
                        'utterance_id': ex_id,
                        'utterance': utt,
                        'execution_status': status,
                        'status_no': status_map.get(status, ''),
                        'stage': stage,
                        'split': get_split(family_id),
                        'task_or_scenario_id': family_id,
                        'target_task': '',
                        'semantic_subtype': subtype,
                        'parent_id': '',
                        'lineage': family_id,
                        'variation_type': '',
                        'boundary_id': boundary_id,
                        'hard_negative_mechanism': '',
                        'context': '',
                        'source_file': fname,
                        'validation_status': 'candidate',
                        'ambiguity_flag': 'false'
                    }
                    records.append(record)
                    
    # 3. Blockquotes Format (**State:** \n > "utt")
    # For MP and HN files
    blocks = re.split(r'#{3,4} (?:MP|HN)\d+-\d+', content)
    for block in blocks[1:]:
        # block corresponds to a family
        # We try to extract domain and utterances
        dom_match = re.search(r'\*\*Target(?: Task)?:\*\*\s*(.*?)\n', block)
        domain = dom_match.group(1).strip() if dom_match else ''
        
        # Look for **Not Started:** \n > I haven't started...
        states = re.finditer(r'\*\*(Not Started|In Progress|Completed):\*\*\s*\n>\s*(.*?)\n', block)
        for s_match in states:
            status = s_match.group(1)
            utt = s_match.group(2).strip()
            
            record = {
                'utterance_id': '',
                'utterance': utt,
                'execution_status': status,
                'status_no': status_map.get(status, ''),
                'stage': stage,
                'split': get_split(fname), # default to fname split if no family id
                'task_or_scenario_id': '',
                'target_task': domain,
                'semantic_subtype': subtype,
                'parent_id': '',
                'lineage': '',
                'variation_type': '',
                'boundary_id': boundary_id,
                'hard_negative_mechanism': '',
                'context': '',
                'source_file': fname,
                'validation_status': 'candidate',
                'ambiguity_flag': 'false'
            }
            records.append(record)
            
    # 4. Stage 3B Variant Blocks Format
    # ### Variant 01 \n - **State:** "utt" \n - **State2:** "utt2"
    var_blocks = re.split(r'#{3} Variant \d+', content)
    for v_block in var_blocks[1:]:
        v_states = re.finditer(r'-\s*\*\*(Not Started|In Progress|Completed):\*\*\s*[“"](.*?)[”"]', v_block)
        for s_match in v_states:
            status = s_match.group(1)
            utt = s_match.group(2).strip()
            
            record = {
                'utterance_id': '',
                'utterance': utt,
                'execution_status': status,
                'status_no': status_map.get(status, ''),
                'stage': stage,
                'split': get_split(fname),
                'task_or_scenario_id': '',
                'target_task': '',
                'semantic_subtype': subtype,
                'parent_id': '',
                'lineage': '',
                'variation_type': '',
                'boundary_id': boundary_id,
                'hard_negative_mechanism': '',
                'context': '',
                'source_file': fname,
                'validation_status': 'candidate',
                'ambiguity_flag': 'false'
            }
            records.append(record)

    return records

s2_files = sorted(glob.glob(f'{S2_DIR}/**/*.md', recursive=True))
s3b_files = sorted(glob.glob(f'{S3B_DIR}/**/*.md', recursive=True))

s2_records = []
for f in s2_files: s2_records.extend(process_file(f, '2'))
s3b_records = []
for f in s3b_files: s3b_records.extend(process_file(f, '3B'))

# Remove duplicates if any (due to overlapping regex approaches)
def deduplicate_records(records):
    seen = set()
    deduped = []
    for r in records:
        key = (r['utterance'].lower(), r['execution_status'], r['source_file'])
        if key not in seen:
            seen.add(key)
            deduped.append(r)
    return deduped

s2_records = deduplicate_records(s2_records)
s3b_records = deduplicate_records(s3b_records)

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
