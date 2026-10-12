#!/usr/bin/env python3
"""
audit_s2_suite.py
Automated validation gate for Stage 2 (BA, MP, HN suites).
Verifies:
1. File inventory & anchor/pair counts
2. Dialogue turn syntax (Assistant: “...” and User: “...”)
3. Exact 4-task balance (Medication, Hydration, Exercise, Physiotherapy)
4. Class balance (VP, P, I, N, VN)
5. Zero duplicate user utterances across all files
"""

import os
import glob
import re
import argparse
import sys

BASE_DIR = "/home/eshwar/code/response/research/s2"

def detect_task(text):
    text_low = text.lower()
    if any(k in text_low for k in ['bottle', 'water', 'hydrat', 'sip', 'glass']):
        return 'Hydration'
    if any(k in text_low for k in ['medicat', 'pill', 'dose', 'tablet', 'tea']):
        return 'Medication'
    if 'physio' in text_low or 'mat' in text_low or 'movement' in text_low:
        return 'Physiotherapy'
    if any(k in text_low for k in ['walk', 'shoes', 'clothes', 'stretching', 'step goal', 'outside']):
        return 'Exercise'
    if any(k in text_low for k in ['routine', 'session', 'rehab']):
        return 'Physiotherapy'
    return 'UNKNOWN'

def audit_ba(verbose=True):
    files = sorted(glob.glob(os.path.join(BASE_DIR, "ba", "*.md")))
    if verbose:
        print(f"\nAUDITING STAGE 2A (BA) — {len(files)} files found")
        print("=" * 80)
        
    all_utterances = {}
    task_counts = {'Medication': 0, 'Hydration': 0, 'Exercise': 0, 'Physiotherapy': 0, 'UNKNOWN': 0}
    class_counts = {'VP': 0, 'P': 0, 'I': 0, 'N': 0, 'VN': 0}
    errors = []
    
    expected_matrix = {
        'BA01_vp_p.md': ['Medication', 'Hydration', 'Exercise'],
        'BA02_p_i.md': ['Physiotherapy', 'Medication', 'Hydration'],
        'BA03_i_n.md': ['Exercise', 'Physiotherapy', 'Medication'],
        'BA04_n_vn.md': ['Hydration', 'Exercise', 'Physiotherapy'],
        'BA05_vp_i.md': ['Medication', 'Hydration', 'Exercise'],
        'BA06_vp_n.md': ['Physiotherapy', 'Medication', 'Hydration'],
        'BA07_vp_vn.md': ['Exercise', 'Physiotherapy', 'Medication'],
        'BA08_p_n.md': ['Hydration', 'Exercise', 'Physiotherapy'],
        'BA09_p_vn.md': ['Medication', 'Hydration', 'Exercise'],
        'BA10_i_vn.md': ['Physiotherapy', 'Medication', 'Hydration']
    }
    
    for fpath in files:
        fname = os.path.basename(fpath)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        anchors = re.findall(
            r"##\s+(BA\d+-A\d+)\s+[—–-]\s+([^\n]+)\n+\*\*Context:\*\*\s*\n+([^\n]+)\n+\*\*User:\*\*\s*\n+([^\n]+)\n+\*\*Label:\*\*\s*`?([A-Z]+)`?",
            content
        )
        
        if len(anchors) != 6:
            errors.append(f"{fname}: Found {len(anchors)} anchors (expected 6)")
            
        file_tasks = []
        for aid, atype, ctx, usr, lbl in anchors:
            if not ctx.startswith("Assistant: “") or not ctx.endswith("”"):
                errors.append(f"{fname} {aid}: Context does not match 'Assistant: “...”'")
            if not usr.startswith("“") or not usr.endswith("”"):
                errors.append(f"{fname} {aid}: User utterance does not match '“...”'")
                
            task = detect_task(ctx)
            file_tasks.append(task)
            task_counts[task] = task_counts.get(task, 0) + 1
            class_counts[lbl] = class_counts.get(lbl, 0) + 1
            
            clean_usr = usr.strip('“"”').strip()
            if clean_usr in all_utterances:
                errors.append(f"Duplicate utterance across {fname} and {all_utterances[clean_usr]}: '{clean_usr}'")
            else:
                all_utterances[clean_usr] = f"{fname}:{aid}"
                
        if len(file_tasks) == 6:
            pair_tasks = [file_tasks[0], file_tasks[2], file_tasks[4]]
            exp_tasks = expected_matrix.get(fname, [])
            if pair_tasks != exp_tasks:
                errors.append(f"{fname} Task Mismatch: Got {pair_tasks}, Expected {exp_tasks}")
                
    if verbose:
        print(f"Total Anchors Audited: {len(all_utterances)}")
        print(f"Class Counts: {class_counts}")
        print(f"Task Counts: {task_counts}")
        if errors:
            print("\nERRORS DETECTED:")
            for e in errors:
                print(f"  [X] {e}")
        else:
            print("[PASS] All Stage 2A Boundary Anchors meet 100% of quality & balance criteria!")
            
    return len(errors) == 0, errors, all_utterances

def audit_mp(ba_utterances=None, verbose=True):
    files = sorted(glob.glob(os.path.join(BASE_DIR, "mp", "*.md")))
    if verbose:
        print(f"\nAUDITING STAGE 2B (MP) — {len(files)} files found")
        print("=" * 80)
        
    all_mp_utterances = {}
    task_counts = {'Medication': 0, 'Hydration': 0, 'Exercise': 0, 'Physiotherapy': 0, 'UNKNOWN': 0}
    class_counts = {'VP': 0, 'P': 0, 'I': 0, 'N': 0, 'VN': 0}
    errors = []
    
    pair_labels_map = {
        'MP01_vp_p.md': ('VP', 'P'),
        'MP02_p_i.md': ('P', 'I'),
        'MP03_i_n.md': ('I', 'N'),
        'MP04_n_vn.md': ('N', 'VN'),
        'MP05_vp_i.md': ('VP', 'I'),
        'MP06_vp_n.md': ('VP', 'N'),
        'MP07_vp_vn.md': ('VP', 'VN'),
        'MP08_p_n.md': ('P', 'N'),
        'MP09_p_vn.md': ('P', 'VN'),
        'MP10_i_vn.md': ('I', 'VN')
    }
    
    for fpath in files:
        fname = os.path.basename(fpath)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        c1, c2 = pair_labels_map[fname]
        
        pattern = rf"##\s+(MP\d+-\d+)\n+\*\*Context:\*\*\s*\n+([^\n]+)\n+\*\*{c1}:\*\*\s*\n+([^\n]+)\n+\*\*{c2}:\*\*\s*\n+([^\n]+)"
        pairs = re.findall(pattern, content)
        
        if len(pairs) != 6:
            errors.append(f"{fname}: Found {len(pairs)} pairs (expected 6)")
            
        for pid, ctx, utt1, utt2 in pairs:
            if not ctx.startswith("Assistant: “") or not ctx.endswith("”"):
                errors.append(f"{fname} {pid}: Context does not match 'Assistant: “...”'")
            if not utt1.startswith("“") or not utt1.endswith("”"):
                errors.append(f"{fname} {pid} {c1}: Utterance does not match '“...”'")
            if not utt2.startswith("“") or not utt2.endswith("”"):
                errors.append(f"{fname} {pid} {c2}: Utterance does not match '“...”'")
                
            task = detect_task(ctx)
            task_counts[task] = task_counts.get(task, 0) + 1
            class_counts[c1] = class_counts.get(c1, 0) + 1
            class_counts[c2] = class_counts.get(c2, 0) + 1
            
            for lbl, u in [(c1, utt1), (c2, utt2)]:
                clean_u = u.strip('“"”').strip()
                if clean_u in all_mp_utterances:
                    errors.append(f"Duplicate within MP across {fname} and {all_mp_utterances[clean_u]}: '{clean_u}'")
                else:
                    all_mp_utterances[clean_u] = f"{fname}:{pid}:{lbl}"
                if ba_utterances and clean_u in ba_utterances:
                    errors.append(f"Overlap between MP and BA ({fname}:{pid} vs {ba_utterances[clean_u]}): '{clean_u}'")
                    
    for t in ['Medication', 'Hydration', 'Exercise', 'Physiotherapy']:
        if task_counts.get(t, 0) != 15:
            errors.append(f"Task parity failure for {t}: Got {task_counts.get(t, 0)}, Expected exactly 15")
                
    if verbose:
        print(f"Total MP Pairs Audited: {sum(task_counts.values())} (120 turns)")
        print(f"Class Counts: {class_counts} (Target: 24 each)")
        print(f"Task Counts: {task_counts} (Target: 15 each)")
        if errors:
            print("\nERRORS DETECTED:")
            for e in errors:
                print(f"  [X] {e}")
        else:
            print("[PASS] All Stage 2B Minimal Pairs meet 100% of quality & parity criteria!")
            
    return len(errors) == 0, errors, all_mp_utterances

def audit_hn(ba_utterances=None, mp_utterances=None, verbose=True):
    files = sorted(glob.glob(os.path.join(BASE_DIR, "hn", "*.md")))
    if verbose:
        print(f"\nAUDITING STAGE 2C (HN) — {len(files)} files found")
        print("=" * 80)
        
    all_hn_utterances = {}
    task_counts = {'Medication': 0, 'Hydration': 0, 'Exercise': 0, 'Physiotherapy': 0, 'UNKNOWN': 0}
    class_counts = {'VP': 0, 'P': 0, 'I': 0, 'N': 0, 'VN': 0}
    errors = []
    
    if len(files) != 10:
        errors.append(f"Expected 10 HN files, found {len(files)}")
        
    for fpath in files:
        fname = os.path.basename(fpath)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        items = re.findall(
            r"##\s+(HN\d+-\d+)\s+[—–-]\s+([^\n]+)\n+\*\*Context:\*\*\s*\n+([^\n]+)\n+\*\*User:\*\*\s*\n+([^\n]+)\n+\*\*Label:\*\*\s*`?([A-Z]+)`?",
            content
        )
        
        if len(items) != 6:
            errors.append(f"{fname}: Found {len(items)} hard negative examples (expected 6)")
            
        for hid, hpattern, ctx, usr, lbl in items:
            if not ctx.startswith("Assistant: “") or not ctx.endswith("”"):
                errors.append(f"{fname} {hid}: Context does not match 'Assistant: “...”'")
            if not usr.startswith("“") or not usr.endswith("”"):
                errors.append(f"{fname} {hid}: User utterance does not match '“...”'")
                
            task = detect_task(ctx)
            task_counts[task] = task_counts.get(task, 0) + 1
            class_counts[lbl] = class_counts.get(lbl, 0) + 1
            
            clean_u = usr.strip('“"”').strip()
            if clean_u in all_hn_utterances:
                errors.append(f"Duplicate within HN across {fname} and {all_hn_utterances[clean_u]}: '{clean_u}'")
            else:
                all_hn_utterances[clean_u] = f"{fname}:{hid}:{lbl}"
                
            if ba_utterances and clean_u in ba_utterances:
                errors.append(f"Overlap between HN and BA ({fname}:{hid} vs {ba_utterances[clean_u]}): '{clean_u}'")
            if mp_utterances and clean_u in mp_utterances:
                errors.append(f"Overlap between HN and MP ({fname}:{hid} vs {mp_utterances[clean_u]}): '{clean_u}'")
                
    if len(files) == 10:
        for t in ['Medication', 'Hydration', 'Exercise', 'Physiotherapy']:
            if task_counts.get(t, 0) != 15:
                errors.append(f"HN Task parity failure for {t}: Got {task_counts.get(t, 0)}, Expected exactly 15")
        for c in ['VP', 'P', 'I', 'N', 'VN']:
            if class_counts.get(c, 0) != 12:
                errors.append(f"HN Class balance failure for {c}: Got {class_counts.get(c, 0)}, Expected exactly 12")
                
    if verbose:
        print(f"Total HN Examples Audited: {len(all_hn_utterances)}")
        print(f"Class Counts: {class_counts} (Target: 12 each)")
        print(f"Task Counts: {task_counts} (Target: 15 each)")
        if errors:
            print("\nERRORS DETECTED:")
            for e in errors:
                print(f"  [X] {e}")
        else:
            print("[PASS] All Stage 2C Hard Negatives meet 100% of quality & parity criteria!")
            
    return len(errors) == 0, errors

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ba", action="store_true", help="Audit Stage 2A BA files")
    parser.add_argument("--mp", action="store_true", help="Audit Stage 2B MP files")
    parser.add_argument("--hn", action="store_true", help="Audit Stage 2C HN files")
    parser.add_argument("--all", action="store_true", help="Audit all Stage 2 suites")
    args = parser.parse_args()
    
    run_all = args.all or not (args.ba or args.mp or args.hn)
    
    ba_ok, ba_err, ba_utts = audit_ba(verbose=args.ba or run_all)
    mp_ok, mp_err, mp_utts = (True, [], {})
    if args.mp or run_all:
        mp_ok, mp_err, mp_utts = audit_mp(ba_utterances=ba_utts, verbose=True)
    hn_ok, hn_err = (True, [])
    if args.hn or run_all:
        hn_ok, hn_err = audit_hn(ba_utterances=ba_utts, mp_utterances=mp_utts, verbose=True)
        
    if not (ba_ok and mp_ok and hn_ok):
        sys.exit(1)
