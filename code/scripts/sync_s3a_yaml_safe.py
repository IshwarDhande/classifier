import glob, re

files = glob.glob('/home/eshwar/code/response/research/execution_status/s3a/*.md')

for f in files:
    if "audit_report" in f: continue
    with open(f, 'r') as fp:
        lines = fp.readlines()
        
    table_utts = {}
    current_scenario = None
    
    for line in lines:
        match = re.search(r'# \d+\.\s+([A-Z]+-S\d+)', line)
        if match:
            current_scenario = match.group(1)
            
        if line.strip().startswith('|') and 'V0' in line or 'V10' in line:
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 5 and len(parts[3]) == 3 and parts[3].isupper():
                anchor = parts[1]
                variant = parts[2]
                utt = parts[4]
                if current_scenario:
                    table_utts[(current_scenario, anchor, variant)] = utt

    with open(f, 'r') as fp:
        content = fp.read()

    def repl_yaml(match):
        yaml_content = match.group(1)
        scen_match = re.search(r'scenario_id:\s+([A-Z]+-S\d+)', yaml_content)
        anchor_match = re.search(r'anchor_id: .*?-(A[1-3])', yaml_content)
        variant_match = re.search(r'variant_id:\s+(V\d+)', yaml_content)
        
        if scen_match and anchor_match and variant_match:
            s = scen_match.group(1)
            a = anchor_match.group(1)
            v = variant_match.group(1)
            
            if (s, a, v) in table_utts:
                new_utt = table_utts[(s, a, v)]
                yaml_content = re.sub(r'utterance: ".*?"', f'utterance: "{new_utt}"', yaml_content)
                
        return f"```yaml\n{yaml_content}\n```"

    new_content = re.sub(r'```yaml\n(.*?)\n```', repl_yaml, content, flags=re.DOTALL)
    
    with open(f, 'w') as fp:
        fp.write(new_content)
        
print("Successfully synced YAML blocks using scenario-specific lookup.")
