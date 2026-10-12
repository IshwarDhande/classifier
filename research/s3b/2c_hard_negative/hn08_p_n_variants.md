# HN08 — P ↔ N Hard Negative Variants

## Boundary

**P (Positive) ↔ N (Negative)**

## Construction Focus

The examples preserve the hard-negative mechanism while the label is determined by the user's dominant behavioral response to the task reminder, not by surface cues.

The expansion varies misleading lexical, pragmatic, and conversational cues while preserving the underlying contrast between genuine cooperation/commitment (`P`) and recoverable reluctance or resistance (`N`).

## Variant Construction Rules

- Preserve the original target category for each parent.
- Preserve the P ↔ N boundary.
- Preserve the original hard-negative mechanism.
- Preserve the task and conversational situation.
- For `P`, retain genuine cooperation or behavioral commitment despite the distractor.
- For `N`, retain observable reluctance, disagreement, mild refusal, or conditional resistance.
- Surface dislike or reluctance must not automatically determine `N` when the user still commits to the task.
- Polite acceptance must not automatically determine `P` when the final behavioral response is resistant.
- The preceding task reminder/intervention is implicit; only the user response is represented.

---

## HN08-01 — P

**Parent:** HN08-01  
**Task:** Medication  
**Hard-negative mechanism:** Competing Keyword  
**Gold label:** `P`

### HN08-01-V01 — LEX
- **Lineage:** HN08-01 → HN08-01-V01

**User:**  
“I don’t like changing where I keep things, but fine, I’ll put my medication beside the breakfast plate.”

**Label:** `P`

### HN08-01-V02 — NAT
- **Lineage:** HN08-01 → HN08-01-V02

**User:**  
“I’m not a fan of changing where I keep things, but that’s okay—I’ll put the medication beside my breakfast plate.”

**Label:** `P`

### HN08-01-V03 — EXP
- **Lineage:** HN08-01 → HN08-01-V03

**User:**  
“Changing the usual spot isn’t really my preference, but I’ve decided to do it anyway and put the medication beside the breakfast plate.”

**Label:** `P`

### HN08-01-V04 — DSC
- **Lineage:** HN08-01 → HN08-01-V04

**User:**  
“I’ll put my medication beside the breakfast plate. I don’t really like changing where I keep things, but I’m fine doing it this way.”

**Label:** `P`

### HN08-01-V05 — PRG
- **Lineage:** HN08-01 → HN08-01-V05

**User:**  
“The change in location isn’t ideal for me, but that doesn’t stop me from following through—I’ll put the medication beside the breakfast plate.”

**Label:** `P`

### HN08-01-V06 — CMK
- **Lineage:** HN08-01 → HN08-01-V06

**User:**  
“Yeah, I dislike changing the usual spot, but okay, I’ll put the medication beside the breakfast plate.”

**Label:** `P`

---

## HN08-02 — P

**Parent:** HN08-02  
**Task:** Hydration  
**Hard-negative mechanism:** Competing Phrase  
**Gold label:** `P`

### HN08-02-V01 — LEX
- **Lineage:** HN08-02 → HN08-02-V01

**User:**  
“I don’t really feel like doing that, but sure, I’ll keep a water bottle on my desk today.”

**Label:** `P`

### HN08-02-V02 — NAT
- **Lineage:** HN08-02 → HN08-02-V02

**User:**  
“I’m not especially in the mood for it, but I’ll go ahead and keep a water bottle on my desk today.”

**Label:** `P`

### HN08-02-V03 — EXP
- **Lineage:** HN08-02 → HN08-02-V03

**User:**  
“I’m not particularly eager to do it, but I am willing to follow through and keep a water bottle on my desk today.”

**Label:** `P`

### HN08-02-V04 — DSC
- **Lineage:** HN08-02 → HN08-02-V04

**User:**  
“I’ll keep a water bottle on my desk today. I don’t really feel like doing it, but I’m willing to go ahead.”

**Label:** `P`

### HN08-02-V05 — PRG
- **Lineage:** HN08-02 → HN08-02-V05

**User:**  
“Not feeling like it doesn’t mean I’m refusing—I’ll still keep the water bottle on my desk today.”

**Label:** `P`

### HN08-02-V06 — CMK
- **Lineage:** HN08-02 → HN08-02-V06

**User:**  
“Honestly, I don’t feel like it, but sure, I’ll keep the bottle on my desk today.”

**Label:** `P`

---

## HN08-03 — P

**Parent:** HN08-03  
**Task:** Physiotherapy  
**Hard-negative mechanism:** Misleading Opening Clause  
**Gold label:** `P`

### HN08-03-V01 — LEX
- **Lineage:** HN08-03 → HN08-03-V01

**User:**  
“The living room is a little cramped, but I can make it work and do the physiotherapy exercises there.”

**Label:** `P`

### HN08-03-V02 — NAT
- **Lineage:** HN08-03 → HN08-03-V02

**User:**  
“The living room is kind of tight, but I can manage it and do the physiotherapy exercises there.”

**Label:** `P`

### HN08-03-V03 — EXP
- **Lineage:** HN08-03 → HN08-03-V03

**User:**  
“The limited space isn’t ideal, but it’s workable, and I’ll do the physiotherapy exercises there.”

**Label:** `P`

### HN08-03-V04 — DSC
- **Lineage:** HN08-03 → HN08-03-V04

**User:**  
“I can make it work and do the physiotherapy exercises in the living room. It’s a bit tight, but that’s manageable.”

**Label:** `P`

### HN08-03-V05 — PRG
- **Lineage:** HN08-03 → HN08-03-V05

**User:**  
“The space is not perfect, but that’s only a practical inconvenience—I can work with it and do the exercises there.”

**Label:** `P`

### HN08-03-V06 — CMK
- **Lineage:** HN08-03 → HN08-03-V06

**User:**  
“Hmm, the living room is pretty tight, but yeah, I can make it work and do the physiotherapy there.”

**Label:** `P`

---

## HN08-04 — N

**Parent:** HN08-04  
**Task:** Medication  
**Hard-negative mechanism:** Mid-Sentence Self-Correction  
**Gold label:** `N`

### HN08-04-V01 — LEX
- **Lineage:** HN08-04 → HN08-04-V01

**User:**  
“Sure, I can stick to that—wait, actually, taking medication in the evening is just too exhausting right now.”

**Label:** `N`

### HN08-04-V02 — NAT
- **Lineage:** HN08-04 → HN08-04-V02

**User:**  
“Sure, I’ll follow the schedule—wait, actually, evenings aren’t good for me. I’d rather take the medication at a time that works for me.”

**Label:** `N`

### HN08-04-V03 — EXP
- **Lineage:** HN08-04 → HN08-04-V03

**User:**  
“I initially agreed to follow that schedule, but I’ve changed my mind because evenings don’t work for me. I’d rather take the medication on my own schedule.”

**Label:** `N`

### HN08-04-V04 — DSC
- **Lineage:** HN08-04 → HN08-04-V04

**User:**  
“I’d rather take my medication on my own schedule. I said I’d follow the plan, but actually, evenings don’t work for me.”

**Label:** `N`

### HN08-04-V05 — PRG
- **Lineage:** HN08-04 → HN08-04-V05

**User:**  
“The initial agreement was too quick—what matters is that the evening schedule doesn’t work for me, so I’d rather use my own timing.”

**Label:** `N`

### HN08-04-V06 — CMK
- **Lineage:** HN08-04 → HN08-04-V06

**User:**  
“Okay, sure, I’ll do that—no, actually, evenings don’t work for me. I’d rather take the medication on my own schedule.”

**Label:** `N`

---

## HN08-05 — N

**Parent:** HN08-05  
**Task:** Hydration  
**Hard-negative mechanism:** Multiple Competing Cues  
**Gold label:** `N`

### HN08-05-V01 — LEX
- **Lineage:** HN08-05 → HN08-05-V01

**User:**  
“I totally get the reasoning behind your suggestion and value hydration, yet I prefer not to tie it to lunch.”

**Label:** `N`

### HN08-05-V02 — NAT
- **Lineage:** HN08-05 → HN08-05-V02

**User:**  
“I get why you’re suggesting it, and I definitely want to stay hydrated, but having the water tied to lunch doesn’t work for me, so I’ll skip that routine.”

**Label:** `N`

### HN08-05-V03 — EXP
- **Lineage:** HN08-05 → HN08-05-V03

**User:**  
“I agree that staying hydrated matters, and I understand the reasoning, but I’m not going to connect the water to lunch. I’ll skip that arrangement.”

**Label:** `N`

### HN08-05-V04 — DSC
- **Lineage:** HN08-05 → HN08-05-V04

**User:**  
“I’ll skip that arrangement. I do want to stay hydrated, and I understand why you suggest it, but tying the water to lunch doesn’t suit me.”

**Label:** `N`

### HN08-05-V05 — PRG
- **Lineage:** HN08-05 → HN08-05-V05

**User:**  
“The hydration goal itself is fine, but this particular routine isn’t—I’m not going to tie drinking water to lunch.”

**Label:** `N`

### HN08-05-V06 — CMK
- **Lineage:** HN08-05 → HN08-05-V06

**User:**  
“Yeah, I know why you suggest it, and I want to stay hydrated, but no, tying the water to lunch doesn’t suit me. I’ll skip that.”

**Label:** `N`

---

## HN08-06 — N

**Parent:** HN08-06  
**Task:** Exercise  
**Hard-negative mechanism:** Conversational Distractor  
**Gold label:** `N`

### HN08-06-V01 — LEX
- **Lineage:** HN08-06 → HN08-06-V01

**User:**  
“I usually enjoy getting outside, but today the walk doesn’t work for me; I’d rather stay in.”

**Label:** `N`

### HN08-06-V02 — NAT
- **Lineage:** HN08-06 → HN08-06-V02

**User:**  
“I normally like going outside, but today I don’t want to take the walk. I’d rather stay indoors.”

**Label:** `N`

### HN08-06-V03 — EXP
- **Lineage:** HN08-06 → HN08-06-V03

**User:**  
“I generally enjoy being outside, but that doesn’t mean today’s walk works for me. I’d rather stay in today.”

**Label:** `N`

### HN08-06-V04 — DSC
- **Lineage:** HN08-06 → HN08-06-V04

**User:**  
“I’d rather stay in today. I usually enjoy getting outside, but the walk doesn’t work for me right now.”

**Label:** `N`

### HN08-06-V05 — PRG
- **Lineage:** HN08-06 → HN08-06-V05

**User:**  
“Enjoying outdoor activity generally isn’t the issue; today’s walk simply doesn’t suit me, so I’d rather stay in.”

**Label:** `N`

### HN08-06-V06 — CMK
- **Lineage:** HN08-06 → HN08-06-V06

**User:**  
“Sure, I usually enjoy getting outside, but no, today the walk doesn’t work for me. I’d rather stay in.”

**Label:** `N`

---

## Gold Labels

| ID | Variant | Label | Task | Distractor Pattern |
|---|---|---|---|---|
| HN08-01 | HN-V01–HN-V06 | P | Medication | Competing Keyword |
| HN08-02 | HN-V01–HN-V06 | P | Hydration | Competing Phrase |
| HN08-03 | HN-V01–HN-V06 | P | Physiotherapy | Misleading Opening Clause |
| HN08-04 | HN-V01–HN-V06 | N | Medication | Mid-Sentence Self-Correction |
| HN08-05 | HN-V01–HN-V06 | N | Hydration | Multiple Competing Cues |
| HN08-06 | HN-V01–HN-V06 | N | Exercise | Conversational Distractor |

## QC Checklist

- [x] Same target category within each parent family
- [x] Same hard-negative mechanism
- [x] Competing surface cue remains present
- [x] Target behavioral evidence remains dominant
- [x] P examples preserve genuine cooperation/commitment
- [x] N examples preserve recoverable reluctance/resistance
- [x] Surface dislike or reluctance does not automatically determine N
- [x] Polite acceptance does not automatically determine P
- [x] Self-correction preserves the final behavioral state
- [x] No reminder-configuration semantics
- [x] No sentiment-only labeling
- [x] No category drift across variants
- [x] Natural conversational wording
- [x] Parent-family lineage preserved for leakage-controlled splitting
