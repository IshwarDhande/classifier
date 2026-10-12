import glob, re

files = glob.glob('/home/eshwar/code/response/research/execution_status/s3a/*.md')

for f in files:
    if "audit_report" in f: continue
    with open(f, 'r') as fp:
        content = fp.read()
        
    # Split by scenario block
    blocks = re.split(r'\n# \d+\.\s+', content)
    
    new_blocks = [blocks[0]] # Header
    
    for i in range(1, len(blocks)):
        block = blocks[i]
        
        # Extract table utterances for THIS scenario
        table_utts = {}
        for line in block.split('\n'):
            if line.strip().startswith('|') and 'V0' in line or 'V10' in line:
                parts = [p.strip() for p in line.split('|')]
                if len(parts) == 6 and len(parts[3]) == 3 and parts[3].isupper():
                    anchor = parts[1]
                    variant = parts[2]
                    utt = parts[4]
                    table_utts[(anchor, variant)] = utt
                    
        # Replace yaml in THIS scenario
        def repl_yaml(match):
            yaml_content = match.group(1)
            anchor_match = re.search(r'anchor_id: .*?-(A[1-3])', yaml_content)
            variant_match = re.search(r'variant_id: (V\d+)', yaml_content)
            if anchor_match and variant_match:
                a = anchor_match.group(1)
                v = variant_match.group(1)
                if (a, v) in table_utts:
                    new_utt = table_utts[(a, v)]
                    # Use a stricter regex to only replace the utterance line
                    yaml_content = re.sub(r'utterance: ".*?"', f'utterance: "{new_utt}"', yaml_content)
            return f"```yaml\n{yaml_content}\n```"
            
        new_block = re.sub(r'```yaml\n(.*?)\n```', repl_yaml, block, flags=re.DOTALL)
        new_blocks.append(new_block)
        
    new_content = ""
    for i, b in enumerate(new_blocks):
        if i == 0:
            new_content += b
        else:
            new_content += "\n# " + str(i+4) + ". " + b # roughly reconstruct, but wait! The split removed the '# 5. ' part
            # It's better to use finditer and replace in place.
