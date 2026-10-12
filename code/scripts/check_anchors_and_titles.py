import re, glob, os

S1_DIR = '/home/eshwar/code/response/research/s1'
S3A_DIR = '/home/eshwar/code/response/research/s3a'

def parse_s1_scenarios(cat):
    scen_files = {
        'I':  f'{S1_DIR}/05_semantic_scenarios_i.md',
        'N':  f'{S1_DIR}/06_semantic_scenarios_n.md',
        'VN': f'{S1_DIR}/07_semantic_scenarios_vn.md',
    }
    with open(scen_files[cat]) as f:
        content = f.read()
    matches = re.findall(r'^## ([A-Z0-9\-]+) — ([^\n]+)', content, re.MULTILINE)
    return {m[0]: m[1].strip() for m in matches}

def parse_s1_anchors(cat):
    anch_files = {
        'I':  f'{S1_DIR}/anchors/03_initial_anchors_i.md',
        'N':  f'{S1_DIR}/anchors/04_initial_anchors_n.md',
        'VN': f'{S1_DIR}/anchors/05_initial_anchors_vn.md',
    }
    with open(anch_files[cat]) as f:
        content = f.read()
    sections = re.split(r'\n## (?=[A-Z0-9\-]+ — )', content)
    anchs = {}
    for sec in sections[1:]:
        header = sec.split('\n')[0].strip()
        scen_id = header.split(' — ')[0].strip()
        direct = re.search(r'\*\*Direct:\*\*\s*\n[“"]([^”"\n]+)[”"]', sec)
        indirect = re.search(r'\*\*Indirect:\*\*\s*\n[“"]([^”"\n]+)[”"]', sec)
        natural = re.search(r'\*\*Natural Conversational:\*\*\s*\n[“"]([^”"\n]+)[”"]', sec)
        anchs[scen_id] = {
            'A1': direct.group(1).strip() if direct else None,
            'A2': indirect.group(1).strip() if indirect else None,
            'A3': natural.group(1).strip() if natural else None,
        }
    return anchs

for cat in ['I', 'N', 'VN']:
    s1_scens = parse_s1_scenarios(cat)
    s1_anchs = parse_s1_anchors(cat)
    for part in ['a', 'b']:
        fname = f'stage_3a_{cat.lower()}_{part}_s{"01_s10" if part=="a" else "11_s20"}_variants.md'
        fpath = os.path.join(S3A_DIR, fname)
        with open(fpath) as fp:
            text = fp.read()
        blocks = text.split('### ')[1:]
        print("\n" + "="*80)
        print(f"AUDITING: {fname}")
        print("="*80)
        anchor_dups = []
        title_mismatches = []
        for b in blocks:
            lines = [l.strip() for l in b.split('\n') if l.strip()]
            head = lines[0]
            scen_id = head.split(' — ')[0].strip()
            scen_title = head.split(' — ')[1].strip() if ' — ' in head else ''
            
            # check title against s1
            s1_t = s1_scens.get(scen_id, '')
            if s1_t and s1_t != scen_title and (scen_id, scen_title, s1_t) not in title_mismatches:
                title_mismatches.append((scen_id, scen_title, s1_t))
                
            v_text_m = re.search(r'Variant:\*{0,2}\s*([^\n]+)', b)
            v_text = v_text_m.group(1).strip() if v_text_m else ''
            
            v_type_m = re.search(r'Variation [Tt]ype:\*{0,2}\s*`?([A-Za-z0-9_]+)`?', b)
            v_type = v_type_m.group(1) if v_type_m else 'UNKNOWN'
            
            # check against anchors
            if scen_id in s1_anchs:
                for k, anch_val in s1_anchs[scen_id].items():
                    if anch_val and anch_val.lower().strip('.!') == v_text.lower().strip('.!'):
                        anchor_dups.append((scen_id, v_type, v_text, k, anch_val))
                        
        if title_mismatches:
            print(f"Scenario title mismatches against Stage 1 ({len(title_mismatches)}):")
            for tm in title_mismatches:
                print(f"  {tm[0]}: s3a='{tm[1]}' vs s1='{tm[2]}'")
        else:
            print("All scenario titles match Stage 1 perfectly!")
            
        if anchor_dups:
            print(f"CRITICAL: Duplicates against Stage 1 Anchors ({len(anchor_dups)}):")
            for ad in anchor_dups:
                print(f"  {ad[0]} ({ad[1]}): '{ad[2]}' matches Anchor {ad[3]}: '{ad[4]}'")
        else:
            print("Duplicates against Stage 1 Anchors: ZERO (all 60 variants are novel)")
