#!/usr/bin/env python3
"""
deep_audit_s2_ba.py
Detailed inspection of all 10 BA files in research/s2/ba/
"""

import os
import glob
import re

BA_DIR = "/home/eshwar/code/response/research/s2/ba"

def deep_audit():
    files = sorted(glob.glob(os.path.join(BA_DIR, "*.md")))
    
    for fpath in files:
        fname = os.path.basename(fpath)
        with open(fpath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            content = "".join(lines)
            
        print("=" * 80)
        print(f"FILE: {fname} ({len(lines)} lines)")
        print("=" * 80)
        
        # Check header 1
        h1 = [line.strip() for line in lines if line.startswith("# ")]
        print(f"H1: {h1}")
        
        # Check H2s
        h2 = [line.strip() for line in lines if line.startswith("## ")]
        print(f"H2 count: {len(h2)} -> {h2}")
        
        # Check H3s
        h3 = [line.strip() for line in lines if line.startswith("### ")]
        print(f"H3 count: {len(h3)} -> {h3}")
        
        # Find all anchors
        # In BA01: ### BA01-A01 — VP Prototype
        # In BA02+: ## BA02-A01 — P Prototype
        anchors = re.findall(r"(#{2,3})\s+(BA\d+-A\d+)\s+[—–-]\s+([^\n]+)", content)
        print(f"Anchors found ({len(anchors)}):")
        for lvl, aid, atype in anchors:
            print(f"  [{lvl}] {aid}: {atype}")
            
        # Extract each anchor's context, user utterance, and label
        # Notice BA01 vs BA02 format
        if fname == "BA01_vp_p.md":
            # BA01 format:
            # **Context:** ...
            # **User:** "..."
            # **Label:** `VP`
            blocks = re.findall(
                r"###\s+(BA\d+-A\d+)[^\n]*\n+\*\*Context:\*\*\s*(.+?)\n+\*\*User:\*\*\s*(.+?)\n+\*\*Label:\*\*\s*`?([A-Z]+)`?",
                content
            )
            print(f"  Parsed blocks: {len(blocks)}")
            for b in blocks:
                print(f"    {b[0]} | Label: {b[3]} | Context: {b[1][:40]}... | User: {b[2]}")
        else:
            # BA02+ format:
            # ## BA02-A01...
            # **Context:** \n Assistant: “...” \n **User:** \n “...” \n **Label:** `P`
            blocks = re.findall(
                r"##\s+(BA\d+-A\d+)[^\n]*\n+\*\*Context:\*\*\s*\n+([^\n]+)\n+\*\*User:\*\*\s*\n+([^\n]+)\n+\*\*Label:\*\*\s*`?([A-Z]+)`?",
                content
            )
            print(f"  Parsed blocks: {len(blocks)}")
            for b in blocks:
                print(f"    {b[0]} | Label: {b[3]} | Context: {b[1][:40]}... | User: {b[2]}")
                
        # Check if Label Key table exists
        has_table = "## Label Key" in content
        print(f"Has Label Key table: {has_table}")

if __name__ == "__main__":
    deep_audit()
