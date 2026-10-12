import glob, re

files = glob.glob('/home/eshwar/code/response/research/execution_status/s3a/*.md')

for f in files:
    with open(f, 'r') as fp:
        content = fp.read()
        
    # Extract table utterances
    table_utts = {}
    for line in content.split('\n'):
        if line.strip().startswith('|') and 'V0' in line or 'V10' in line:
            parts = [p.strip() for p in line.split('|')]
            if len(parts) == 6 and len(parts[3]) == 3 and parts[3].isupper():
                # | A1 | V01 | LEX | utterance |
                anchor = parts[1]
                variant = parts[2]
                utt = parts[4]
                table_utts[(anchor, variant)] = utt
            elif len(parts) == 6 and 'candidate' in parts[4].lower():
                # Older format or candidate
                pass
                
    # Now find yaml blocks and update utterance
    def repl_yaml(match):
        block = match.group(1)
        anchor_match = re.search(r'anchor_id: .*?-(A[1-3])', block)
        variant_match = re.search(r'variant_id: (V\d+)', block)
        if anchor_match and variant_match:
            a = anchor_match.group(1)
            v = variant_match.group(1)
            if (a, v) in table_utts:
                new_utt = table_utts[(a, v)]
                block = re.sub(r'utterance: ".*?"', f'utterance: "{new_utt}"', block)
        return f"```yaml\n{block}\n```"
        
    new_content = re.sub(r'```yaml\n(.*?)\n```', repl_yaml, content, flags=re.DOTALL)
    
    with open(f, 'w') as fp:
        fp.write(new_content)
        
print("Synced YAML blocks with modified tables.")
