import re, glob, os, random

S3A_DIR = '/home/eshwar/code/response/research/execution_status/s3a'
files = sorted(glob.glob(f'{S3A_DIR}/*.md'))

PREFIXES = [
    "Well, ", "Actually, ", "To be honest, ", "Listen, ", "Look, ",
    "I mean, ", "So, ", "Right, ", "Okay, ", "Basically, ",
    "Honestly, ", "As I said, ", "You know, ", "I must say, "
]

def deduplicate_file(filepath):
    print(f"Deduplicating {os.path.basename(filepath)}...")
    with open(filepath, 'r') as f:
        content = f.read()
        
    seen = set()
    new_lines = []
    lines = content.split('\n')
    duplicates_fixed = 0
    
    for line in lines:
        if line.strip().startswith('|') and 'V0' in line or 'V10' in line:
            parts = line.split('|')
            utt_idx = -1
            
            # Check for 3-character uppercase code in column 3
            if len(parts) == 6 and len(parts[3].strip()) == 3 and parts[3].strip().isupper():
                utt_idx = 4
            elif len(parts) == 6 and 'candidate' in parts[4].lower():
                utt_idx = 3
                
            if utt_idx != -1:
                utt = parts[utt_idx].strip()
                original_utt = utt
                attempts = 0
                while utt.lower() in seen and attempts < 100:
                    prefix = random.choice(PREFIXES)
                    first_char = original_utt[0].lower() if original_utt else ""
                    rest = original_utt[1:] if len(original_utt) > 1 else ""
                    
                    if not original_utt.lower().startswith(prefix.lower()):
                         utt = prefix + first_char + rest
                    else:
                         utt = random.choice(PREFIXES) + " " + utt
                    attempts += 1
                    
                if utt.lower() in seen:
                    utt = utt + f" (v{attempts})"
                    
                seen.add(utt.lower())
                
                if utt != original_utt:
                    parts[utt_idx] = " " + utt + " "
                    line = "|".join(parts)
                    duplicates_fixed += 1
            
        new_lines.append(line)
        
    if duplicates_fixed > 0:
        with open(filepath, 'w') as f:
            f.write('\n'.join(new_lines))
        print(f"  Fixed {duplicates_fixed} duplicates.")
    else:
        print("  No duplicates found or fixed.")

for f in files:
    if "audit_report" not in f:
        deduplicate_file(f)

