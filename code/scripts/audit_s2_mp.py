#!/usr/bin/env python3
"""
audit_s2_mp.py
Inspect and audit all minimal pair files in research/s2/mp/
"""

import os
import glob
import re

MP_DIR = "/home/eshwar/code/response/research/s2/mp"

def audit_mp_files():
    files = sorted(glob.glob(os.path.join(MP_DIR, "*.md")))
    print(f"Auditing {len(files)} MP files in {MP_DIR}:\n")
    
    for fpath in files:
        fname = os.path.basename(fpath)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        title_m = re.search(r"^#\s+(MP\d+)\s+[—–-]\s+([^\n]+)", content, re.MULTILINE)
        mp_id = title_m.group(1) if title_m else "UNKNOWN"
        mp_title = title_m.group(2) if title_m else "UNKNOWN"
        
        # Check context format:
        # Does it use dialogue "Assistant: “..." or narrative "The assistant suggests..."?
        contexts = re.findall(r"\*\*Context:\*\*\s*(.+?)(?=\n+\*\*[A-Z]+:|\Z)", content, re.DOTALL)
        narrative_ctx = [c for c in contexts if "The assistant" in c]
        dialogue_ctx = [c for c in contexts if "Assistant:" in c]
        
        # Check pair count (## MPxx-yy)
        pairs = re.findall(r"##\s+(MP\d+-\d+)", content)
        
        # Check if table exists
        has_table = "## Gold Labels" in content or "## Label Key" in content
        
        print(f"FILE: {fname:<15} | Pairs: {len(pairs)} | Dialogue Ctx: {len(dialogue_ctx)} | Narrative Ctx: {len(narrative_ctx)} | Has Table: {has_table}")

if __name__ == "__main__":
    audit_mp_files()
