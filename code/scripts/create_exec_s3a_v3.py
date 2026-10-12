import glob, os, re, csv

S3A_DIR = '/home/eshwar/code/response/research/execution_status/s3a'
OUT_DIR = '/home/eshwar/code/response/code/data/execution_status/dataset_3a'
os.makedirs(OUT_DIR, exist_ok=True)

files = sorted(glob.glob(f'{S3A_DIR}/*.md'))

records = []

status_map = {
    'not_started': ('Not Started', 2),
    'in_progress': ('In Progress', 1),
    'completed': ('Completed', 0)
}

for f in files:
    if "audit_report" in f: continue
    fname = os.path.basename(f)
    
    status_key = 'not_started' if 'not_started' in fname else 'in_progress' if 'in_progress' in fname else 'completed' if 'completed' in fname else None
    if not status_key: continue
    status_label, status_no = status_map[status_key]
        
    with open(f, 'r') as fp:
        lines = fp.readlines()
        
    current_scenario = None
    current_domain = ""
    current_subtype = ""
    
    for i, line in enumerate(lines):
        scen_match = re.search(r'#+\s+([A-Z]+-S\d+)', line)
        if scen_match:
            current_scenario = scen_match.group(1)
            
        # Try finding Domain
        # Sometimes it's "**Domain:** Exercise" or "**Task domain:** Exercise"
        dom_match = re.search(r'\*\*(?:Task\s*)?[dD]omain:\*\*\s*(.*?)$', line)
        if dom_match:
            current_domain = dom_match.group(1).strip()
            
        # Try finding Subtype
        sub_match = re.search(r'\*\*Subtype:\*\*\s*`?(.*?)`?$', line)
        if sub_match:
            current_subtype = sub_match.group(1).strip()
            
        if line.strip().startswith('|') and ('V0' in line or 'V10' in line):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 5:
                # Meta tables have "Code | Variant type", skip them
                if "Construction role" in line or "Variant type" in line:
                    continue
                    
                if not current_scenario:
                    m2 = re.search(r'^([A-Z]+-S\d+)', parts[1])
                    if m2: current_scenario = m2.group(1)
                    
                if not current_scenario:
                    continue
                    
                if len(parts[1]) == 2 and parts[1].startswith('A'):
                    anchor = parts[1]
                    variant = parts[2]
                    var_type = parts[3]
                    utt = parts[4]
                    example_id = f"{current_scenario}-{anchor}-{variant}"
                else:
                    example_id = parts[1]
                    var_type = parts[2]
                    utt = parts[3]
                    m = re.search(r'-(A[1-3]?)-(V\d+)', example_id)
                    anchor = m.group(1) if m else ''
                    variant = m.group(2) if m else ''
                
                num_str = re.search(r'\d+', current_scenario)
                if not num_str: continue
                num = int(num_str.group())
                mod = num % 5
                
                if mod in [1, 2, 3]: split = 'train'
                elif mod == 4: split = 'validation'
                else: split = 'test'
                
                record = {
                    'utterance_id': example_id,
                    'utterance': utt,
                    'execution_status': status_label,
                    'status_no': status_no,
                    'stage': '3A',
                    'split': split,
                    'task_or_scenario_id': current_scenario,
                    'target_task': current_domain,
                    'semantic_subtype': current_subtype,
                    'parent_id': f"{current_scenario}-{anchor}",
                    'lineage': current_scenario,
                    'variation_type': var_type,
                    'boundary_id': '',
                    'hard_negative_mechanism': '',
                    'context': '',
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

out_csv = os.path.join(OUT_DIR, 'stage_3a_dataset.csv')
with open(out_csv, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    writer.writeheader()
    for row in records:
        writer.writerow({k: row.get(k, '') for k in columns})

print(f"Stage 3A compilation complete. Generated {len(records)} records in {out_csv}.")
