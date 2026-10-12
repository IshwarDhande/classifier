import re, glob, os

files = {
    'VP-A': '/home/eshwar/code/response/research/s3a/stage_3a_vp_a_s01_s10_variants.md',
    'VP-B': '/home/eshwar/code/response/research/s3a/stage_3a_vp_b_s11_s20_variants.md',
    'P-A': '/home/eshwar/code/response/research/s3a/stage_3a_p_a_s01_s10_variants.md',
    'P-B': '/home/eshwar/code/response/research/s3a/stage_3a_p_b_s11_s20_variants.md',
}

def extract_utterances(path):
    with open(path) as f:
        text = f.read()
    # Find all utterances
    utts = []
    # format 1
    m1 = re.findall(r'###\s+([A-Z0-9\-]+)\s*—\s*`?([A-Z]{3})`?.*?-\s*\*\*Utterance:\*\*\s*[“"]?([^”"\n]+)[”"]?', text, re.DOTALL)
    if m1:
        for item in m1:
            utts.append({'id': item[0], 'type': item[1], 'text': item[2].strip().strip('“').strip('”').strip('"')})
    else:
        # format 2
        blocks = text.split('### ')[1:]
        for i, b in enumerate(blocks):
            lines = [l.strip() for l in b.split('\n') if l.strip()]
            head = lines[0]
            scen_id = head.split(' — ')[0].strip()
            v_type = re.search(r'Variation type:\s*`?([A-Z]{3})`?', b)
            var_t = v_type.group(1) if v_type else 'UNK'
            v_text = re.search(r'Variant:\s*([^\n]+)', b)
            ut = v_text.group(1).strip() if v_text else ''
            utts.append({'id': f"{scen_id}-V{i%6+1:02d}", 'type': var_t, 'text': ut.strip('“').strip('”').strip('"')})
    return utts

all_data = {}
for k, p in files.items():
    all_data[k] = extract_utterances(p)
    print(f"{k}: extracted {len(all_data[k])} utterances")

# Check VP files for under-intensity (sounding like P or I)
# VP should demonstrate strong acceptance, appreciation, enthusiasm, proactive engagement, or strong voluntary cooperation.
# Weak utterances in VP:
print("\n" + "="*60)
print("VP UTTERANCES REQUIRING SCRUTINY (Potential under-intensity / leak into P or I):")
print("="*60)
for k in ['VP-A', 'VP-B']:
    for u in all_data[k]:
        txt = u['text']
        # Suspiciously flat or neutral or ordinary phrases:
        # e.g. "I can go ahead with that", "that makes sense to me", "I understand", "works for me" without positive boost
        flat_markers = [
            "i can go ahead with that",
            "makes sense to me",
            "i understand",
            "that's fine",
            "that is fine",
            "should i go ahead",
            "i can do that"
        ]
        # check if it lacks enthusiasm/appreciation words
        high_pos = ["appreciate", "thank", "grateful", "eager", "keen", "excited", "love", "fantastic", "great", "excellent", "glad", "happy", "definitely", "absolutely", "completely on board", "fully on board", "really helps", "what else", "next step", "build on", "routine", "consistently", "ahead"]
        
        has_flat = any(fm in txt.lower() for fm in flat_markers)
        has_boost = any(hp in txt.lower() for hp in high_pos)
        
        if has_flat and not has_boost:
            print(f"[{k}] {u['id']} ({u['type']}): \"{txt}\"")

# Check P files for over-intensity (sounding like VP) or non-commitment (sounding like I)
print("\n" + "="*60)
print("P UTTERANCES REQUIRING SCRUTINY:")
print("="*60)
for k in ['P-A', 'P-B']:
    for u in all_data[k]:
        txt = u['text']
        # Suspiciously enthusiastic (leaking into VP):
        over_pos = ["love", "excited", "fantastic", "amazing", "thrilled", "wonderful", "extremely", "keen", "genuinely happy", "super"]
        # Check if it lacks acceptance or sounds purely like neutral acknowledgement (I):
        pure_ack = ["that makes sense", "i understand", "i see", "i hear you"]
        
        has_over = any(op in txt.lower() for op in over_pos)
        # Check if text is just an acknowledgement without willingness/acceptance:
        is_ack = any(txt.lower().strip('.!') == pa for pa in pure_ack)
        
        if has_over:
            print(f"[{k}] Potential VP leak -> {u['id']} ({u['type']}): \"{txt}\"")
        if is_ack:
            print(f"[{k}] Potential I leak (pure acknowledgement) -> {u['id']} ({u['type']}): \"{txt}\"")
