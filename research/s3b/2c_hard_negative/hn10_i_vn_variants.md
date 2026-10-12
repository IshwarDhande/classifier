# HN10 — I ↔ VN Hard Negative Variants

## Boundary

**I (Indifferent) ↔ VN (Very Negative)**

## Construction Focus

The examples contain surface cues that mimic either neutral ambivalence or hostile confrontation, but the true intended label is determined by whether the user's communicative stance remains genuinely open and uncommitted (`I`) or explicitly terminates the interaction and rejects the domain topic (`VN`).

The expansion preserves the original hard-negative mechanisms while varying the misleading surface realization. The decisive evidence remains openness/deferral versus explicit interaction or topic rejection.

## Variant Construction Rules

- Preserve the original target category for each parent.
- Preserve the I ↔ VN boundary.
- Preserve the original hard-negative mechanism.
- Preserve the task and conversational situation.
- For `I`, retain genuine openness, consideration, uncertainty, or postponement without active rejection of the interaction.
- For `VN`, retain explicit interaction termination, strong topic rejection, autonomy shutdown, or active disengagement.
- Negative-sounding wording must not automatically determine `VN` when the user remains genuinely open.
- Neutral or tentative wording must not automatically determine `I` when the user explicitly ends the interaction or rejects the topic.
- The preceding task reminder/intervention is implicit; only the user response is represented.

---

## HN10-01 — I

**Parent:** HN10-01  
**Task:** Medication  
**Hard-negative mechanism:** Competing Keyword  
**Gold label:** `I`

### HN10-01-V01 — LEX
- **Lineage:** HN10-01 → HN10-01-V01

**User:**  
“Don't act like that's my only choice; it could work, but I'll make up my own mind.”

**Label:** `I`

### HN10-01-V02 — NAT
- **Lineage:** HN10-01 → HN10-01-V02

**User:**  
“Don’t assume that’s my only choice. It could work, but I’m still deciding whether I want to keep the medication there.”

**Label:** `I`

### HN10-01-V03 — EXP
- **Lineage:** HN10-01 → HN10-01-V03

**User:**  
“I disagree with treating that as the only option, but I haven’t rejected it—I’m still considering whether I want to keep the medication there.”

**Label:** `I`

### HN10-01-V04 — DSC
- **Lineage:** HN10-01 → HN10-01-V04

**User:**  
“I’m still considering whether I want to keep the medication there. Stop assuming that’s the only option, but I haven’t decided against it.”

**Label:** `I`

### HN10-01-V05 — PRG
- **Lineage:** HN10-01 → HN10-01-V05

**User:**  
“Calling it the only option is what I object to; the actual choice is still open, and I’m considering whether to keep the medication there.”

**Label:** `I`

### HN10-01-V06 — CMK
- **Lineage:** HN10-01 → HN10-01-V06

**User:**  
“No, don’t assume that’s the only option. It might work, though—I’m still thinking about whether I want the medication there.”

**Label:** `I`

---

## HN10-02 — I

**Parent:** HN10-02  
**Task:** Hydration  
**Hard-negative mechanism:** Competing Phrase  
**Gold label:** `I`

### HN10-02-V01 — LEX
- **Lineage:** HN10-02 → HN10-02-V01

**User:**  
“I’m tired of hearing people give hydration advice, but a bottle on the desk is still a possibility; I’ll decide later.”

**Label:** `I`

### HN10-02-V02 — NAT
- **Lineage:** HN10-02 → HN10-02-V02

**User:**  
“I’m getting tired of all the hydration advice, but I haven’t ruled out keeping a bottle on the desk. I’ll see later.”

**Label:** `I`

### HN10-02-V03 — EXP
- **Lineage:** HN10-02 → HN10-02-V03

**User:**  
“I’m frustrated by how much hydration advice I hear, but that doesn’t mean I’ve rejected the bottle idea—I’m still considering it and will decide later.”

**Label:** `I`

### HN10-02-V04 — DSC
- **Lineage:** HN10-02 → HN10-02-V04

**User:**  
“A bottle on the desk is still a possibility. I’m tired of hearing hydration advice, but I haven’t decided whether I want to do that yet.”

**Label:** `I`

### HN10-02-V05 — PRG
- **Lineage:** HN10-02 → HN10-02-V05

**User:**  
“The repeated advice is getting tiring, but my position on the bottle itself is still open—I’ll decide later whether I want it on the desk.”

**Label:** `I`

### HN10-02-V06 — CMK
- **Lineage:** HN10-02 → HN10-02-V06

**User:**  
“Ugh, all this hydration advice is tiring, but maybe the bottle could work. I’ll see later.”

**Label:** `I`

---

## HN10-03 — I

**Parent:** HN10-03  
**Task:** Exercise  
**Hard-negative mechanism:** Misleading Opening Clause  
**Gold label:** `I`

### HN10-03-V01 — LEX
- **Lineage:** HN10-03 → HN10-03-V01

**User:**  
“Keep your exercise programs to yourself; a walk is a possibility, but I'll do it my way.”

**Label:** `I`

### HN10-03-V02 — NAT
- **Lineage:** HN10-03 → HN10-03-V02

**User:**  
“I’m not interested in joining a fitness program, but I might take a walk. I haven’t decided yet.”

**Label:** `I`

### HN10-03-V03 — EXP
- **Lineage:** HN10-03 → HN10-03-V03

**User:**  
“I don’t want to be included in a broader fitness program, but I haven’t rejected walking itself—I’m still considering whether to do it.”

**Label:** `I`

### HN10-03-V04 — DSC
- **Lineage:** HN10-03 → HN10-03-V04

**User:**  
“I haven’t decided whether to take the walk yet. Leave me out of your fitness programs; I’m only considering the walk as an option.”

**Label:** `I`

### HN10-03-V05 — PRG
- **Lineage:** HN10-03 → HN10-03-V05

**User:**  
“The fitness-program idea isn’t something I’m signing up for, but the walk remains undecided—I might do it, and I’ll decide later.”

**Label:** `I`

### HN10-03-V06 — CMK
- **Lineage:** HN10-03 → HN10-03-V06

**User:**  
“Look, leave me out of the fitness programs. But yeah, I might go for a walk—I just haven’t decided yet.”

**Label:** `I`

---

## HN10-04 — VN

**Parent:** HN10-04  
**Task:** Medication  
**Hard-negative mechanism:** Mid-Sentence Self-Correction  
**Gold label:** `VN`

### HN10-04-V01 — LEX
- **Lineage:** HN10-04 → HN10-04-V01

**User:**  
“I might consider taking the medication later—actually, absolutely not. Stop meddling with my medication and leave me alone.”

**Label:** `VN`

### HN10-04-V02 — NAT
- **Lineage:** HN10-04 → HN10-04-V02

**User:**  
“I was thinking I might take it later, but no, forget it. Stop interfering with my medication and leave me alone.”

**Label:** `VN`

### HN10-04-V03 — EXP
- **Lineage:** HN10-04 → HN10-04-V03

**User:**  
“I initially left open the possibility of taking the medication later, but I’m rejecting that now. Stop meddling with my medication; I don’t want this discussion anymore.”

**Label:** `VN`

### HN10-04-V04 — DSC
- **Lineage:** HN10-04 → HN10-04-V04

**User:**  
“Stop meddling with my medication and leave me alone. I said I might consider taking it later, but actually, absolutely not.”

**Label:** `VN`

### HN10-04-V05 — PRG
- **Lineage:** HN10-04 → HN10-04-V05

**User:**  
“The earlier possibility is withdrawn completely—I’m ending this discussion about my medication. Stop interfering and leave me alone.”

**Label:** `VN`

### HN10-04-V06 — CMK
- **Lineage:** HN10-04 → HN10-04-V06

**User:**  
“Maybe later—no, absolutely not. Stop meddling with my medication and just leave me alone.”

**Label:** `VN`

---

## HN10-05 — VN

**Parent:** HN10-05  
**Task:** Hydration  
**Hard-negative mechanism:** Multiple Competing Cues  
**Gold label:** `VN`

### HN10-05-V01 — LEX
- **Lineage:** HN10-05 → HN10-05-V01

**User:**  
“Maybe drinking more water helps people, maybe it doesn’t, but I don’t care. Stop lecturing me about hydration; I’m done discussing this.”

**Label:** `VN`

### HN10-05-V02 — NAT
- **Lineage:** HN10-05 → HN10-05-V02

**User:**  
“Maybe more water helps, maybe it doesn’t. Either way, I don’t care anymore—stop lecturing me about hydration. I’m done with the topic.”

**Label:** `VN`

### HN10-05-V03 — EXP
- **Lineage:** HN10-05 → HN10-05-V03

**User:**  
“I can see that drinking more water might help, but I’m rejecting the discussion itself. Stop lecturing me about hydration; I’m done talking about it.”

**Label:** `VN`

### HN10-05-V04 — DSC
- **Lineage:** HN10-05 → HN10-05-V04

**User:**  
“I’m done discussing hydration. Maybe more water helps and maybe it doesn’t, but I don’t care anymore, so stop lecturing me about it.”

**Label:** `VN`

### HN10-05-V05 — PRG
- **Lineage:** HN10-05 → HN10-05-V05

**User:**  
“Whether more water helps is no longer the issue—I’m ending this conversation about hydration. Stop lecturing me about it.”

**Label:** `VN`

### HN10-05-V06 — CMK
- **Lineage:** HN10-05 → HN10-05-V06

**User:**  
“Maybe it helps, maybe not. Honestly, I don’t care—stop lecturing me about hydration. I’m done discussing this.”

**Label:** `VN`

---

## HN10-06 — VN

**Parent:** HN10-06  
**Task:** Exercise  
**Hard-negative mechanism:** Conversational Distractor  
**Gold label:** `VN`

### HN10-06-V01 — LEX
- **Lineage:** HN10-06 → HN10-06-V01

**User:**  
“You bring up walking every single day. I’ve told you before to stop telling me what to wear or do; drop the subject.”

**Label:** `VN`

### HN10-06-V02 — NAT
- **Lineage:** HN10-06 → HN10-06-V02

**User:**  
“Every day you bring up walking again. I’ve already told you to stop telling me what to wear or do, so please drop it.”

**Label:** `VN`

### HN10-06-V03 — EXP
- **Lineage:** HN10-06 → HN10-06-V03

**User:**  
“I know walking has come up repeatedly, but I’m ending the discussion now. Stop telling me what to wear or do for it and drop the subject.”

**Label:** `VN`

### HN10-06-V04 — DSC
- **Lineage:** HN10-06 → HN10-06-V04

**User:**  
“Drop the subject. You bring up walking every single day, and I’ve already told you to stop telling me what to wear or do.”

**Label:** `VN`

### HN10-06-V05 — PRG
- **Lineage:** HN10-06 → HN10-06-V05

**User:**  
“The repeated walking discussion is not welcome—I’m ending it completely. Stop giving me instructions about what to wear or do and drop the subject.”

**Label:** `VN`

### HN10-06-V06 — CMK
- **Lineage:** HN10-06 → HN10-06-V06

**User:**  
“Again with the walking? No, I told you to stop telling me what to wear or do. Drop the subject.”

**Label:** `VN`

---

## Gold Labels

| ID | Variant | Label | Task | Distractor Pattern |
|---|---|---|---|---|
| HN10-01 | HN-V01–HN-V06 | I | Medication | Competing Keyword |
| HN10-02 | HN-V01–HN-V06 | I | Hydration | Competing Phrase |
| HN10-03 | HN-V01–HN-V06 | I | Exercise | Misleading Opening Clause |
| HN10-04 | HN-V01–HN-V06 | VN | Medication | Mid-Sentence Self-Correction |
| HN10-05 | HN-V01–HN-V06 | VN | Hydration | Multiple Competing Cues |
| HN10-06 | HN-V01–HN-V06 | VN | Exercise | Conversational Distractor |

## QC Checklist

- [x] Same target category within each parent family
- [x] Same hard-negative mechanism
- [x] Competing surface cue remains present
- [x] Target behavioral evidence remains dominant
- [x] I examples preserve genuine openness/consideration without active rejection
- [x] VN examples preserve explicit topic rejection or interaction termination
- [x] Negative-sounding wording does not automatically determine VN
- [x] Tentative wording does not automatically determine I
- [x] Self-correction preserves the final behavioral state
- [x] No reminder-configuration semantics
- [x] No sentiment-only labeling
- [x] No category drift across variants
- [x] Natural conversational wording
- [x] Parent-family lineage preserved for leakage-controlled splitting
