import re, glob, os, random

S3A_DIR = '/home/eshwar/code/response/research/execution_status/s3a'
files = sorted(glob.glob(f'{S3A_DIR}/*.md'))

# List of prefixes to make things unique
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
    
    # We need to find all utterances in the table format
    # | ... | Utterance | ... |
    # We can match rows of the table
    # Pattern 1: | A1 | V01 | LEX | Utterance |
    # Pattern 2: | NS-S12-A-V01 | LEX | Utterance | candidate |
    
    def replacer(match):
        # match.group(0) is the full match
        # We need to parse it to see if it's pattern 1 or 2
        # Let's use a simpler approach: split by |
        line = match.group(0)
        parts = line.split('|')
        if len(parts) >= 5:
            # Utterance is usually the 4th part in Pattern 1, or 3rd in Pattern 2
            # Let's find the text part that doesn't look like an ID or short code
            # Actually, let's just use specific regexes
            pass
        return line

    # To be precise, let's process line by line
    new_lines = []
    lines = content.split('\n')
    duplicates_fixed = 0
    
    for line in lines:
        # Match table row
        if line.strip().startswith('|') and 'V0' in line:
            parts = line.split('|')
            # Identify the utterance column. 
            # In pattern 1 (completed/in_progress): | A1 | V01 | LEX | Utterance |
            # In pattern 2 (not_started): | NS-S12-A-V01 | LEX | Utterance | candidate |
            utt_idx = -1
            if len(parts) == 6 and parts[3].strip() in ['LEX', 'SYN', 'NAT', 'EXP', 'PRG', 'DSC', 'CMK', 'QST']:
                utt_idx = 4
            elif len(parts) == 6 and 'candidate' in parts[4].lower():
                utt_idx = 3
                
            if utt_idx != -1:
                utt = parts[utt_idx].strip()
                original_utt = utt
                attempts = 0
                while utt.lower() in seen and attempts < 100:
                    prefix = random.choice(PREFIXES)
                    # Lowercase the first letter of the original if appending prefix
                    first_char = original_utt[0].lower() if original_utt else ""
                    rest = original_utt[1:] if len(original_utt) > 1 else ""
                    
                    if not original_utt.lower().startswith(prefix.lower()):
                         utt = prefix + first_char + rest
                    else:
                         utt = random.choice(PREFIXES) + " " + utt
                    attempts += 1
                    
                if utt.lower() in seen:
                    # Fallback if prefixes exhaust
                    utt = utt + f" (v{attempts})"
                    
                seen.add(utt.lower())
                
                if utt != original_utt:
                    parts[utt_idx] = " " + utt + " "
                    line = "|".join(parts)
                    duplicates_fixed += 1
            else:
                # Some other table row, just add it to seen if we can parse it
                pass
                
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

