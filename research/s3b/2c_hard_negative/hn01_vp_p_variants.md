# HN01 — VP ↔ P Hard Negative Variants

## Boundary

**VP (Very Positive) ↔ P (Positive)**

## Construction Focus

The examples contain surface cues that could suggest the competing category, but the true label is determined by the user's degree of behavioral engagement and proactive agency versus routine compliance.

The expansion preserves the original hard-negative mechanism: **Competing Keyword**. Across variants, the misleading surface cue changes while the dominant behavioral response remains the gold label.

## Variant Construction Rules

- Preserve the original target category for each parent.
- Preserve the competing VP/P boundary.
- Preserve the competing-keyword hard-negative mechanism.
- Preserve the task and conversational situation.
- Keep the misleading keyword present, but prevent it from becoming deterministic.
- Ensure behavioral evidence remains stronger than the isolated lexical cue.
- Do not turn VP examples into ordinary P acceptance, or P examples into VP-level enthusiasm.
- The preceding task reminder/intervention is implicit; only the user response is represented.

---

## HN01-01 — VP

**Parent:** HN01-01  
**Task:** Hydration  
**Hard-negative mechanism:** Competing Keyword  
**Gold label:** `VP`

### HN01-01-V01 — LEX
- **Lineage:** HN01-01 → HN01-01-V01

**User:**  
“Okay is enough to describe the idea, but I’m genuinely excited to put this bottle beside me and start drinking regularly.”

**Label:** `VP`

### HN01-01-V02 — NAT
- **Lineage:** HN01-01 → HN01-01-V02

**User:**  
“‘Okay’ is fair, but honestly I’m really excited to get this bottle ready and make regular drinking part of my day.”

**Label:** `VP`

### HN01-01-V03 — EXP
- **Lineage:** HN01-01 → HN01-01-V03

**User:**  
“Okay, I get the point, but I’m genuinely excited about this and I’m filling the bottle now so I can keep drinking throughout the day.”

**Label:** `VP`

### HN01-01-V04 — DSC
- **Lineage:** HN01-01 → HN01-01-V04

**User:**  
“I’m genuinely excited to start drinking regularly and get the bottle ready right now; ‘okay’ barely captures how motivated I feel about it.”

**Label:** `VP`

### HN01-01-V05 — PRG
- **Lineage:** HN01-01 → HN01-01-V05

**User:**  
“If ‘okay’ is all you hear, you’re missing the main point—I’m actually excited enough to get the bottle ready and start right away.”

**Label:** `VP`

### HN01-01-V06 — CMK
- **Lineage:** HN01-01 → HN01-01-V06

**User:**  
“Okay, sure—but I’m honestly excited about this. I’m getting the bottle ready now and I want to keep up the habit.”

**Label:** `VP`

---

## HN01-02 — VP

**Parent:** HN01-02  
**Task:** Exercise  
**Hard-negative mechanism:** Competing Keyword  
**Gold label:** `VP`

### HN01-02-V01 — LEX
- **Lineage:** HN01-02 → HN01-02-V01

**User:**  
“I’ll do it, although I wouldn’t call it just a simple chore; I’m really looking forward to getting outside and starting today.”

**Label:** `VP`

### HN01-02-V02 — NAT
- **Lineage:** HN01-02 → HN01-02-V02

**User:**  
“I’ll do it, even if ‘chore’ sounds a bit ordinary—I’m actually looking forward to getting outside and starting today.”

**Label:** `VP`

### HN01-02-V03 — EXP
- **Lineage:** HN01-02 → HN01-02-V03

**User:**  
“I’ll do it, but calling it a routine chore misses how I feel about it—I’m genuinely looking forward to getting outside and exercising today.”

**Label:** `VP`

### HN01-02-V04 — DSC
- **Lineage:** HN01-02 → HN01-02-V04

**User:**  
“I’m really looking forward to getting outside and starting today. I’ll do it, even though calling it a chore would make it sound too ordinary.”

**Label:** `VP`

### HN01-02-V05 — PRG
- **Lineage:** HN01-02 → HN01-02-V05

**User:**  
“If you take ‘chore’ as the important part, that’s not really my reaction—I’m looking forward to getting outside and starting.”

**Label:** `VP`

### HN01-02-V06 — CMK
- **Lineage:** HN01-02 → HN01-02-V06

**User:**  
“I’ll do it, sure, but honestly I’m looking forward to getting outside and getting started today.”

**Label:** `VP`

---

## HN01-03 — VP

**Parent:** HN01-03  
**Task:** Physiotherapy  
**Hard-negative mechanism:** Competing Keyword  
**Gold label:** `VP`

### HN01-03-V01 — LEX
- **Lineage:** HN01-03 → HN01-03-V01

**User:**  
“It may seem ordinary at first, but I actually love this approach and I’m laying out the exercise mat right now.”

**Label:** `VP`

### HN01-03-V02 — NAT
- **Lineage:** HN01-03 → HN01-03-V02

**User:**  
“‘Nothing special’ might be the first impression, but I genuinely love this approach and I’m getting the mat ready now.”

**Label:** `VP`

### HN01-03-V03 — EXP
- **Lineage:** HN01-03 → HN01-03-V03

**User:**  
“It looks ordinary on the surface, but I really like this approach and I’m already setting up the mat to begin.”

**Label:** `VP`

### HN01-03-V04 — DSC
- **Lineage:** HN01-03 → HN01-03-V04

**User:**  
“I actually love this approach and I’m laying out the mat right now, even if it might look like nothing special at first.”

**Label:** `VP`

### HN01-03-V05 — PRG
- **Lineage:** HN01-03 → HN01-03-V05

**User:**  
“Don’t let ‘ordinary’ be the takeaway—I really like this approach and I’m already getting the mat ready.”

**Label:** `VP`

### HN01-03-V06 — CMK
- **Lineage:** HN01-03 → HN01-03-V06

**User:**  
“Nothing special, maybe, but honestly I really like it. I’m laying out the mat and getting started now.”

**Label:** `VP`

---

## HN01-04 — P

**Parent:** HN01-04  
**Task:** Hydration  
**Hard-negative mechanism:** Competing Keyword with Self-Correction  
**Gold label:** `P`

### HN01-04-V01 — LEX
- **Lineage:** HN01-04 → HN01-04-V01

**User:**  
“I was going to set up a detailed tracking log for every glass—actually, forget that; I’ll drink the water after each meal.”

**Label:** `P`

### HN01-04-V02 — NAT
- **Lineage:** HN01-04 → HN01-04-V02

**User:**  
“I thought I’d need a whole tracking sheet for every glass, but never mind that—I’ll just drink water after each meal.”

**Label:** `P`

### HN01-04-V03 — EXP
- **Lineage:** HN01-04 → HN01-04-V03

**User:**  
“I was about to make a detailed log, but that’s unnecessary. I’ll keep it simple and drink the water after each meal.”

**Label:** `P`

### HN01-04-V04 — DSC
- **Lineage:** HN01-04 → HN01-04-V04

**User:**  
“I’ll just drink the water after each meal. I was going to make a tracking log for every glass, but actually, I don’t need to do that.”

**Label:** `P`

### HN01-04-V05 — PRG
- **Lineage:** HN01-04 → HN01-04-V05

**User:**  
“The tracking part sounded like too much, but that’s not what matters—I’ll keep it simple and drink water after each meal.”

**Label:** `P`

### HN01-04-V06 — CMK
- **Lineage:** HN01-04 → HN01-04-V06

**User:**  
“Right, I was thinking of tracking every glass—no, never mind. I’ll just have the water after each meal.”

**Label:** `P`

---

## HN01-05 — P

**Parent:** HN01-05  
**Task:** Exercise  
**Hard-negative mechanism:** Competing Keyword / Multiple Competing Cues  
**Gold label:** `P`

### HN01-05-V01 — LEX
- **Lineage:** HN01-05 → HN01-05-V01

**User:**  
“That sounds like a wonderful habit and I appreciate the helpful thought, but simply put, yes, I’ll leave my shoes by the door.”

**Label:** `P`

### HN01-05-V02 — NAT
- **Lineage:** HN01-05 → HN01-05-V02

**User:**  
“I really appreciate the suggestion, and it does sound like a great habit, but yes, I’ll keep my shoes by the door and do the session.”

**Label:** `P`

### HN01-05-V03 — EXP
- **Lineage:** HN01-05 → HN01-05-V03

**User:**  
“It sounds wonderful and I’m grateful for the suggestion, but my response is simply yes—I’ll leave the shoes by the door and do it.”

**Label:** `P`

### HN01-05-V04 — DSC
- **Lineage:** HN01-05 → HN01-05-V04

**User:**  
“Yes, I’ll leave my shoes by the door and do the session. It does sound like a good habit, and I appreciate the suggestion.”

**Label:** `P`

### HN01-05-V05 — PRG
- **Lineage:** HN01-05 → HN01-05-V05

**User:**  
“You can call it a wonderful habit if you want; either way, yes, I’ll leave the shoes by the door and follow through.”

**Label:** `P`

### HN01-05-V06 — CMK
- **Lineage:** HN01-05 → HN01-05-V06

**User:**  
“Thanks, that sounds great. But yes, I’ll leave the shoes by the door and get the session done.”

**Label:** `P`

---

## HN01-06 — P

**Parent:** HN01-06  
**Task:** Physiotherapy  
**Hard-negative mechanism:** Competing Keyword / Conversational Distractor  
**Gold label:** `P`

### HN01-06-V01 — LEX
- **Lineage:** HN01-06 → HN01-06-V01

**User:**  
“You frequently suggest ambitious routine shifts, but in this specific instance, sure, I’ll split the exercises into two sessions today.”

**Label:** `P`

### HN01-06-V02 — NAT
- **Lineage:** HN01-06 → HN01-06-V02

**User:**  
“You do tend to suggest some pretty ambitious changes, but this one is manageable; I’ll do the two short sessions today.”

**Label:** `P`

### HN01-06-V03 — EXP
- **Lineage:** HN01-06 → HN01-06-V03

**User:**  
“Even if your suggestions can sound ambitious, this one is clear enough—I’ll do the two short physiotherapy sessions today.”

**Label:** `P`

### HN01-06-V04 — DSC
- **Lineage:** HN01-06 → HN01-06-V04

**User:**  
“I’ll do the two short sessions today. You always suggest ambitious changes, but this one is fine.”

**Label:** `P`

### HN01-06-V05 — PRG
- **Lineage:** HN01-06 → HN01-06-V05

**User:**  
“Call it another ambitious habit change if you like, but for this one I’ll do the two short sessions today.”

**Label:** `P`

### HN01-06-V06 — CMK
- **Lineage:** HN01-06 → HN01-06-V06

**User:**  
“Yeah, you’re always pushing ambitious habit changes, but sure, I’ll do the two short sessions today.”

**Label:** `P`

---

## Gold Labels

| ID | Variant | Label | Task | Distractor Pattern |
|---|---|---|---|---|
| HN01-01 | HN-V01–HN-V06 | VP | Hydration | Competing Keyword |
| HN01-02 | HN-V01–HN-V06 | VP | Exercise | Competing Keyword |
| HN01-03 | HN-V01–HN-V06 | VP | Physiotherapy | Competing Keyword |
| HN01-04 | HN-V01–HN-V06 | P | Hydration | Competing Keyword + Self-Correction |
| HN01-05 | HN-V01–HN-V06 | P | Exercise | Competing Keyword + Multiple Cues |
| HN01-06 | HN-V01–HN-V06 | P | Physiotherapy | Competing Keyword + Conversational Distractor |

## QC Checklist

- [x] Same target category within each parent family
- [x] Same hard-negative mechanism
- [x] Competing surface cue remains present
- [x] Target behavioral evidence remains dominant
- [x] VP examples preserve strong enthusiasm/proactive engagement
- [x] P examples preserve ordinary cooperation without VP-level enthusiasm
- [x] No reminder-configuration semantics
- [x] No sentiment-only labeling
- [x] No single keyword acts as a deterministic label
- [x] No category drift across variants
- [x] Natural conversational wording
- [x] Parent-family lineage preserved for later leakage-controlled splitting
