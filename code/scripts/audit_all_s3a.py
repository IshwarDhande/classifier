import re, glob, os
from collections import Counter

# Paths
S1_DIR = '/home/eshwar/code/response/research/s1'
S3A_DIR = '/home/eshwar/code/response/research/s3a'

CAT_SPECS = {
    'VP': ['LEX', 'NAT', 'EXP', 'PRG', 'CMK', 'QST'],
    'P':  ['LEX', 'SYN', 'NAT', 'EXP', 'LEN', 'CMK'],
    'I':  ['LEX', 'NAT', 'EXP', 'PRG', 'HES', 'QST'],
    'N':  ['LEX', 'SYN', 'NAT', 'EXP', 'PRG', 'CMK'],
    'VN': ['LEX', 'SYN', 'NAT', 'EXP', 'PRG', 'DSC'],
}

def parse_s1_scenarios():
    scen_files = {
        'VP': f'{S1_DIR}/03_semantic_scenarios_vp.md',
        'P':  f'{S1_DIR}/04_semantic_scenarios_p.md',
        'I':  f'{S1_DIR}/05_semantic_scenarios_i.md',
        'N':  f'{S1_DIR}/06_semantic_scenarios_n.md',
        'VN': f'{S1_DIR}/07_semantic_scenarios_vn.md',
    }
    scens = {}
    for cat, p in scen_files.items():
        with open(p) as f:
            content = f.read()
        matches = re.findall(r'^## ([A-Z0-9\-]+) — ([^\n]+)', content, re.MULTILINE)
        scens[cat] = {m[0]: m[1].strip() for m in matches}
    return scens

def parse_s1_anchors():
    anch_files = {
        'VP': f'{S1_DIR}/anchors/01_initial_anchors_vp.md',
        'P':  f'{S1_DIR}/anchors/02_initial_anchors_p.md',
        'I':  f'{S1_DIR}/anchors/03_initial_anchors_i.md',
        'N':  f'{S1_DIR}/anchors/04_initial_anchors_n.md',
        'VN': f'{S1_DIR}/anchors/05_initial_anchors_vn.md',
    }
    anchs = {}
    for cat, p in anch_files.items():
        with open(p) as f:
            content = f.read()
        sections = re.split(r'\n## (?=[A-Z0-9\-]+ — )', content)
        anchs[cat] = {}
        for sec in sections[1:]:
            header = sec.split('\n')[0].strip()
            scen_id = header.split(' — ')[0].strip()
            direct = re.search(r'\*\*Direct:\*\*\s*\n[“"]([^”"\n]+)[”"]', sec)
            indirect = re.search(r'\*\*Indirect:\*\*\s*\n[“"]([^”"\n]+)[”"]', sec)
            natural = re.search(r'\*\*Natural Conversational:\*\*\s*\n[“"]([^”"\n]+)[”"]', sec)
            anchs[cat][scen_id] = {
                'A1': direct.group(1).strip() if direct else None,
                'A2': indirect.group(1).strip() if indirect else None,
                'A3': natural.group(1).strip() if natural else None,
                'title': header.split(' — ')[1].strip() if ' — ' in header else ''
            }
    return anchs

s1_scenarios = parse_s1_scenarios()
s1_anchors = parse_s1_anchors()

files = sorted(glob.glob(f'{S3A_DIR}/*.md'))
variant_files = [f for f in files if 'audit_report' not in f and 'fixes.md' not in f]

print("="*80)
print(f"AUDITING {len(variant_files)} STAGE 3A VARIANT FILES")
print("="*80)

audit_results = {}

for f in variant_files:
    fname = os.path.basename(f)
    # Determine category
    m_cat = re.search(r'stage_3a_([a-z]+)_[ab]_', fname)
    raw_cat = m_cat.group(1).upper() if m_cat else 'UNKNOWN'
    
    with open(f) as fp:
        raw = fp.read()
        
    res = {
        'filename': fname,
        'category': raw_cat,
        'schema': 'UNKNOWN',
        'records': [],
        'errors': [],
        'warnings': []
    }
    
    # Pattern 1: Standard Schema
    # ## [SCENARIO]
    # ### [ID] — `[TYPE]`
    # - **Parent Anchor:** `[ANCHOR]`
    # - **Variation Type:** `[TYPE]`
    # - **Lineage:** ...
    # - **Utterance:** “...”
    pattern1 = re.compile(
        r'###\s+([A-Z0-9\-]+)(?:-V\d+)?\s*—\s*`?([A-Z]{3})`?'
        r'.*?'
        r'-\s*\*\*Parent [Aa]nchor:\*\*\s*`?([A-Z0-9\-]+)`?'
        r'.*?'
        r'-\s*\*\*Variation [Tt]ype:\*\*\s*`?([A-Z]{3})`?'
        r'.*?'
        r'-\s*\*\*Lineage:\*\*\s*([^\n]+)'
        r'.*?'
        r'-\s*\*\*Utterance:\*\*\s*[“"]?([^”"\n]+)[”"]?',
        re.DOTALL
    )
    
    # Pattern 2: Alternate Schema (repeated scenario header)
    pattern2 = re.compile(
        r'###\s+([A-Z0-9\-]+)\s*—\s*([^\n]+)\n+'
        r'-\s*\*\*Subtype:\*\*\s*`?([A-Z0-9\-]+)`?\n+'
        r'-\s*\*\*Parent [Aa]nchor:\*\*\s*`?([A-Z0-9\-]+)`?\n+'
        r'-\s*\*\*Variation [Tt]ype:\*\*\s*`?([A-Z]{3})`?\n+'
        r'-\s*\*\*Variant:\*\*\s*([^\n]+)',
        re.MULTILINE
    )
    
    matches1 = pattern1.findall(raw)
    matches2 = pattern2.findall(raw)
    
    if len(matches1) == 60:
        res['schema'] = 'STANDARD'
        for m in matches1:
            res['records'].append({
                'id': m[0],
                'var_type': m[3],
                'parent_anchor': m[2],
                'lineage': m[4].strip(),
                'utterance': m[5].strip().strip('“').strip('”').strip('"')
            })
    elif len(matches2) == 60:
        res['schema'] = 'ALTERNATE (NON-STANDARD)'
        res['errors'].append("Uses non-standard schema: missing level-2 scenario headers, variant IDs (e.g. -V01), and lineage fields.")
        for i, m in enumerate(matches2):
            res['records'].append({
                'id': f"{m[0]}-V{i%6+1:02d}",
                'scenario_id': m[0],
                'var_type': m[4],
                'parent_anchor': m[3],
                'lineage': None,
                'utterance': m[5].strip().strip('“').strip('”').strip('"')
            })
    else:
        res['schema'] = f'INCOMPLETE/MIXED (P1: {len(matches1)}, P2: {len(matches2)})'
        res['errors'].append(f"Unexpected record match count: P1={len(matches1)}, P2={len(matches2)}")
        
    # Check scenario count
    scen_counts = {}
    for r in res['records']:
        scen = "-".join(r['id'].split('-')[:3])
        scen_counts[scen] = scen_counts.get(scen, 0) + 1
    
    if len(scen_counts) != 10:
        res['errors'].append(f"Scenario count is {len(scen_counts)}, expected 10.")
    for s, c in scen_counts.items():
        if c != 6:
            res['errors'].append(f"Scenario {s} has {c} variants, expected 6.")
            
    # Check expected variation sequence
    exp_seq = CAT_SPECS.get(raw_cat, [])
    for s in sorted(scen_counts.keys()):
        s_recs = [r for r in res['records'] if "-".join(r['id'].split('-')[:3]) == s]
        act_seq = [r['var_type'] for r in s_recs]
        if act_seq != exp_seq:
            res['errors'].append(f"Sequence mismatch in {s}: {act_seq} != {exp_seq}")
            
    # Check parent anchor distribution
    # In standard schema, anchors should rotate among A1, A2, A3
    for s in sorted(scen_counts.keys()):
        s_recs = [r for r in res['records'] if "-".join(r['id'].split('-')[:3]) == s]
        p_anchs = [r['parent_anchor'] for r in s_recs]
        if len(set(p_anchs)) == 1:
            res['warnings'].append(f"All 6 variants in {s} cite single anchor '{p_anchs[0]}' (no parent diversity).")
        if any('A01' in pa for pa in p_anchs):
            res['errors'].append(f"Anchor ID notation in {s} uses 'A01' instead of standard 'A1'/'A2'/'A3'.")
            
    # Check internal duplicate utterances
    utts = [r['utterance'] for r in res['records']]
    dup_utts = [u for u in utts if utts.count(u) > 1]
    if dup_utts:
        res['errors'].append(f"Internal duplicate utterances found: {set(dup_utts)}")
        
    # Check duplicates against Stage 1 Anchors
    cat_anchors = s1_anchors.get(raw_cat, {})
    for r in res['records']:
        s_id = "-".join(r['id'].split('-')[:3])
        if s_id in cat_anchors:
            for k in ['A1', 'A2', 'A3']:
                anch_val = cat_anchors[s_id].get(k)
                if anch_val and anch_val.lower().strip('.!') == r['utterance'].lower().strip('.!'):
                    res['errors'].append(f"Variant {r['id']} is identical to Stage-1 Anchor {s_id}-{k}: '{anch_val}'")
                    
    audit_results[fname] = res

# Print Report
print("\n" + "#"*80)
print("AUDIT SUMMARY TABLE")
print("#"*80)
print(f"{'Filename':<35} | {'Schema':<12} | {'Records':<7} | {'Errors':<6} | {'Warnings':<8}")
print("-" * 80)
for fn, r in audit_results.items():
    print(f"{fn:<35} | {r['schema'][:12]:<12} | {len(r['records']):<7} | {len(r['errors']):<6} | {len(r['warnings']):<8}")

print("\n" + "#"*80)
print("DETAILED ERROR & WARNING LOG")
print("#"*80)
for fn, r in audit_results.items():
    if r['errors'] or r['warnings']:
        print(f"\n>>> {fn} (Category: {r['category']}, Schema: {r['schema']})")
        if r['errors']:
            print("  ERRORS:")
            # print up to 5
            for e in r['errors'][:8]:
                print(f"    - {e}")
            if len(r['errors']) > 8:
                print(f"    ... and {len(r['errors']) - 8} more errors")
        if r['warnings']:
            print("  WARNINGS:")
            for w in r['warnings'][:5]:
                print(f"    - {w}")
            if len(r['warnings']) > 5:
                print(f"    ... and {len(r['warnings']) - 5} more warnings")
    else:
        print(f"\n>>> {fn}: 100% CLEAN (Zero errors, zero warnings)")
