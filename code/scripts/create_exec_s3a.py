import glob, os, yaml, re, csv

S3A_DIR = '/home/eshwar/code/response/research/execution_status/s3a'
OUT_DIR = '/home/eshwar/code/response/code/data/execution_status/dataset_3a'
os.makedirs(OUT_DIR, exist_ok=True)

files = sorted(glob.glob(f'{S3A_DIR}/*.md'))

records = []

status_map = {
    'Not Started': 2,
    'In Progress': 1,
    'Completed': 0
}

for f in files:
    if "audit_report" in f: continue
    fname = os.path.basename(f)
        
    with open(f, 'r') as fp:
        content = fp.read()
        
    yaml_blocks = re.findall(r'```yaml\n(.*?)\n```', content, re.DOTALL)
    for b in yaml_blocks:
        try:
            parsed = yaml.safe_load(b)
            if 'utterance' not in parsed: continue
            
            scenario_id = str(parsed.get('scenario_id', ''))
            
            num_str = re.search(r'\d+', scenario_id)
            if not num_str: continue
            num = int(num_str.group())
            mod = num % 5
            
            if mod in [1, 2, 3]:
                split = 'train'
            elif mod == 4:
                split = 'validation'
            else:
                split = 'test'
                
            status_label = parsed.get('execution_status', '')
            status_no = status_map.get(status_label, '')
                
            record = {
                'utterance_id': parsed.get('example_id', ''),
                'utterance': parsed.get('utterance', ''),
                'execution_status': status_label,
                'status_no': status_no,
                'stage': '3A',
                'split': split,
                'task_or_scenario_id': scenario_id,
                'target_task': parsed.get('task_domain', ''),
                'semantic_subtype': parsed.get('subtype_id', ''),
                'parent_id': parsed.get('anchor_id', ''),
                'lineage': parsed.get('lineage_id', ''),
                'variation_type': parsed.get('variant_type', ''),
                'boundary_id': '',
                'hard_negative_mechanism': '',
                'context': '',
                'source_file': fname,
                'validation_status': parsed.get('validation_status', ''),
                'ambiguity_flag': 'false'
            }
            records.append(record)
        except Exception as e:
            pass

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
