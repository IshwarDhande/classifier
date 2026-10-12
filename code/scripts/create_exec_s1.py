import glob, os, re, csv

S1_DIR = '/home/eshwar/code/response/research/execution_status/s1/anchors'
OUT_DIR = '/home/eshwar/code/response/code/data/execution_status/dataset_1'
os.makedirs(OUT_DIR, exist_ok=True)

files = sorted(glob.glob(f'{S1_DIR}/*.md'))

records = []

status_map = {
    'not_started': ('Not Started', 2),
    'in_progress': ('In Progress', 1),
    'completed': ('Completed', 0)
}

for f in files:
    fname = os.path.basename(f)
    if 'not_started' in fname:
        status_label, status_no = status_map['not_started']
    elif 'in_progress' in fname:
        status_label, status_no = status_map['in_progress']
    elif 'completed' in fname:
        status_label, status_no = status_map['completed']
    else:
        continue
        
    with open(f, 'r') as fp:
        content = fp.read()
        
    # Split by scenario headers e.g. "# 5. NS-S01 — Task Not Yet Started"
    scenarios = re.finditer(r'# \d+\.\s+([A-Z]+-S\d+)\s+—\s+(.*?)\n(.*?)(?=\n# \d+\.\s+[A-Z]+-S\d+|$)', content, re.DOTALL)
    
    for match in scenarios:
        scenario_id = match.group(1).strip()
        scenario_name = match.group(2).strip()
        block = match.group(3)
        
        subtype_match = re.search(r'### Subtype\n`?(.*?)`?\n', block)
        subtype = subtype_match.group(1).strip() if subtype_match else ''
        
        domain_match = re.search(r'### Domain\n\n(.*?)\n', block)
        domain = domain_match.group(1).strip() if domain_match else ''
        
        context_match = re.search(r'### Scenario meaning\n\n(.*?)\n\n###', block, re.DOTALL)
        context = context_match.group(1).strip().replace('\n', ' ') if context_match else ''
        
        anchors = re.finditer(r'### Anchor ([A-C]) — (.*?)\n\n>\s*(.*?)\n', block)
        
        num_str = re.search(r'\d+', scenario_id).group()
        num = int(num_str)
        mod = num % 5
        if mod in [1, 2, 3]:
            split = 'train'
        elif mod == 4:
            split = 'validation'
        else:
            split = 'test'
            
        for a_match in anchors:
            anchor_letter = a_match.group(1)
            anchor_name = a_match.group(2)
            utterance = a_match.group(3).strip()
            
            utterance_id = f"{scenario_id}-A{1 if anchor_letter=='A' else 2 if anchor_letter=='B' else 3}"
            
            record = {
                'utterance_id': utterance_id,
                'utterance': utterance,
                'execution_status': status_label,
                'status_no': status_no,
                'stage': '1',
                'split': split,
                'task_or_scenario_id': scenario_id,
                'target_task': domain,
                'semantic_subtype': subtype,
                'parent_id': '',
                'lineage': '',
                'variation_type': '',
                'boundary_id': '',
                'hard_negative_mechanism': '',
                'source_file': fname,
                'validation_status': 'candidate',
                'ambiguity_flag': 'false'
            }
            records.append(record)

columns = [
    'utterance_id', 'utterance', 'execution_status', 'status_no', 'stage', 'split',
    'task_or_scenario_id', 'parent_id', 'lineage', 'variation_type', 'boundary_id',
    'hard_negative_mechanism', 'target_task', 'semantic_subtype', 'context', 'source_file',
    'validation_status', 'ambiguity_flag'
]

out_csv = os.path.join(OUT_DIR, 'stage_1_dataset.csv')
with open(out_csv, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    writer.writeheader()
    for row in records:
        writer.writerow({k: row.get(k, '') for k in columns})

print(f"Stage 1 compilation complete. Generated {len(records)} records in {out_csv}.")
