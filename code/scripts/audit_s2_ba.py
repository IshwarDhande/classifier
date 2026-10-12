#!/usr/bin/env python3
"""
audit_s2_ba.py
Inspect and audit all boundary anchor files in research/s2/ba/ using the standardized schema.
"""

import os
import re
import glob

BA_DIR = "/home/eshwar/code/response/research/s2/ba"

def audit_ba_files():
    files = sorted(glob.glob(os.path.join(BA_DIR, "*.md")))
    print(f"Auditing {len(files)} BA files in {BA_DIR}:\n")
    
    total_anchors = 0
    file_reports = []
    
    for fpath in files:
        fname = os.path.basename(fpath)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Parse title
        title_m = re.search(r"^#\s+(BA\d+)\s+[—–-]\s+([^\n]+)", content, re.MULTILINE)
        ba_id = title_m.group(1) if title_m else "UNKNOWN"
        ba_title = title_m.group(2) if title_m else "UNKNOWN"
        
        # Parse boundary definition
        boundary_m = re.search(r"## Boundary\s*\n+\*\*([^\n]+)\*\*", content)
        boundary_str = boundary_m.group(1).replace("**", "").strip() if boundary_m else "UNKNOWN"
        
        # Parse anchors (Level 2 header: ## BAxx-Axx — Type)
        # Context: Assistant: ...
        # User: ...
        # Label: `LBL`
        anchor_blocks = re.findall(
            r"##\s+(BA\d+-A\d+)\s+[—–-]\s+([^\n]+)\n+\*\*Context:\*\*\s*\n+([^\n]+)\n+\*\*User:\*\*\s*\n+([^\n]+)\n+\*\*Label:\*\*\s*`?([A-Z]+)`?",
            content
        )
        
        report = {
            "file": fname,
            "ba_id": ba_id,
            "title": ba_title,
            "boundary": boundary_str,
            "anchor_count": len(anchor_blocks),
            "anchors": [],
            "issues": []
        }
        
        if len(anchor_blocks) != 6:
            report["issues"].append(f"Expected 6 anchors, found {len(anchor_blocks)}")
            
        for a_id, a_type, ctx, usr, lbl in anchor_blocks:
            usr_clean = usr.strip().strip('"').strip('“').strip('”').strip()
            ctx_clean = ctx.strip().replace("Assistant: “", "").replace("Assistant: \"", "").rstrip('”"').strip()
            report["anchors"].append({
                "id": a_id,
                "type": a_type.strip(),
                "context": ctx_clean,
                "user": usr_clean,
                "label": lbl.strip()
            })
            total_anchors += 1
            
        file_reports.append(report)
        
    print(f"{'File':<16} | {'BA ID':<6} | {'Boundary':<25} | {'Anchors':<7} | {'Status'}")
    print("-" * 80)
    for r in file_reports:
        status_str = "; ".join(r["issues"]) if r["issues"] else "100% OK"
        print(f"{r['file']:<16} | {r['ba_id']:<6} | {r['boundary']:<25} | {r['anchor_count']:<7} | {status_str}")
        
    print(f"\nTotal BA Anchors extracted across 10 files: {total_anchors}")
    return file_reports

if __name__ == "__main__":
    audit_ba_files()
