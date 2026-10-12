# HN02 — P ↔ I Hard Negative Variants

## Boundary

**P (Positive) ↔ I (Indifferent)**

## Construction Focus

The examples contain surface cues of hesitation, uncertainty, or neutral hedging, but the true intended label is determined by whether the user actually commits to baseline compliance (`P`) or maintains uncommitted deferral (`I`).

The expansion preserves the original hard-negative mechanisms while varying the misleading surface realization. The behavioral commitment or lack of commitment remains the decisive evidence.

## Variant Construction Rules

- Preserve the original target category for each parent.
- Preserve the P ↔ I boundary.
- Preserve the original hard-negative mechanism.
- Preserve the task and conversational situation.
- Keep hesitation, uncertainty, neutral hedging, or conversational framing as a distractor where applicable.
- For `P`, retain genuine behavioral commitment despite the distractor.
- For `I`, retain acknowledgement/consideration without sufficient behavioral commitment.
- Do not let a single hedge such as “maybe,” “I suppose,” or “still thinking” determine the label.
- The preceding task reminder/intervention is implicit; only the user response is represented.

---

## HN02-01 — P

**Parent:** HN02-01  
**Task:** Medication  
**Hard-negative mechanism:** Competing Keyword  
**Gold label:** `P`

### HN02-01-V01 — LEX
- **Lineage:** HN02-01 → HN02-01-V01

**User:**  
“Maybe it is worth doing, but either way, I’ll put the pillbox beside my toothbrush tonight.”

**Label:** `P`

### HN02-01-V02 — NAT
- **Lineage:** HN02-01 → HN02-01-V02

**User:**  
“Maybe it’s a good idea, I guess, but I’ll still put the pillbox beside my toothbrush tonight.”

**Label:** `P`

### HN02-01-V03 — EXP
- **Lineage:** HN02-01 → HN02-01-V03

**User:**  
“I’m not completely sure whether it’s a good idea, but I’ve decided what I’ll do: I’ll put the pillbox beside my toothbrush tonight.”

**Label:** `P`

### HN02-01-V04 — DSC
- **Lineage:** HN02-01 → HN02-01-V04

**User:**  
“I’ll put the pillbox beside my toothbrush tonight. Maybe it’s a good idea, maybe not, but I’m going to do that.”

**Label:** `P`

### HN02-01-V05 — PRG
- **Lineage:** HN02-01 → HN02-01-V05

**User:**  
“Whether it’s actually a good idea or not, I’ll follow through and put the pillbox beside my toothbrush tonight.”

**Label:** `P`

### HN02-01-V06 — CMK
- **Lineage:** HN02-01 → HN02-01-V06

**User:**  
“Maybe, sure—but I’ll put the pillbox beside my toothbrush tonight.”

**Label:** `P`

---

## HN02-02 — P

**Parent:** HN02-02  
**Task:** Exercise  
**Hard-negative mechanism:** Competing Phrase  
**Gold label:** `P`

### HN02-02-V01 — LEX
- **Lineage:** HN02-02 → HN02-02-V01

**User:**  
“That might work, I suppose, but I’ll go ahead and take the walk after lunch today.”

**Label:** `P`

### HN02-02-V02 — NAT
- **Lineage:** HN02-02 → HN02-02-V02

**User:**  
“I guess that could work, though I’m not making a big deal of it; I’ll take the walk after lunch today.”

**Label:** `P`

### HN02-02-V03 — EXP
- **Lineage:** HN02-02 → HN02-02-V03

**User:**  
“That could work, even if I’m not completely convinced yet. I’ll still go ahead and take the walk after lunch today.”

**Label:** `P`

### HN02-02-V04 — DSC
- **Lineage:** HN02-02 → HN02-02-V04

**User:**  
“I’ll take the walk after lunch today. That could work, I suppose, even though I’m not especially certain about it.”

**Label:** `P`

### HN02-02-V05 — PRG
- **Lineage:** HN02-02 → HN02-02-V05

**User:**  
“Call it something that could work if you like; I’m still going ahead with the walk after lunch today.”

**Label:** `P`

### HN02-02-V06 — CMK
- **Lineage:** HN02-02 → HN02-02-V06

**User:**  
“Yeah, I suppose so—but I’ll go ahead and take the walk after lunch today.”

**Label:** `P`

---

## HN02-03 — P

**Parent:** HN02-03  
**Task:** Physiotherapy  
**Hard-negative mechanism:** Misleading Opening Clause  
**Gold label:** `P`

### HN02-03-V01 — LEX
- **Lineage:** HN02-03 → HN02-03-V01

**User:**  
“I’m still thinking about the exact setup, but I’ll unroll the mat in the living room today.”

**Label:** `P`

### HN02-03-V02 — NAT
- **Lineage:** HN02-03 → HN02-03-V02

**User:**  
“I haven’t settled on all the details yet, but I will unroll the mat in the living room today.”

**Label:** `P`

### HN02-03-V03 — EXP
- **Lineage:** HN02-03 → HN02-03-V03

**User:**  
“I’m still deciding how I want the space arranged, but the action itself is clear: I’ll unroll the mat in the living room today.”

**Label:** `P`

### HN02-03-V04 — DSC
- **Lineage:** HN02-03 → HN02-03-V04

**User:**  
“I’ll unroll the mat in the living room today. I’m still thinking through the overall setup, but that part is decided.”

**Label:** `P`

### HN02-03-V05 — PRG
- **Lineage:** HN02-03 → HN02-03-V05

**User:**  
“The overall layout can wait—I’m still considering that, but I’ll unroll the mat in the living room today.”

**Label:** `P`

### HN02-03-V06 — CMK
- **Lineage:** HN02-03 → HN02-03-V06

**User:**  
“Hmm, I’m still figuring out the setup, but yes, I’ll unroll the mat in the living room today.”

**Label:** `P`

---

## HN02-04 — I

**Parent:** HN02-04  
**Task:** Hydration  
**Hard-negative mechanism:** Mid-Sentence Self-Correction  
**Gold label:** `I`

### HN02-04-V01 — LEX
- **Lineage:** HN02-04 → HN02-04-V01

**User:**  
“Sure, I can put a bottle right—actually, wait, I haven’t decided whether I want water sitting on my desk today.”

**Label:** `I`

### HN02-04-V02 — NAT
- **Lineage:** HN02-04 → HN02-04-V02

**User:**  
“Sure, I could put a bottle there—no, actually, I’m still undecided about having water cluttering my desk today.”

**Label:** `I`

### HN02-04-V03 — EXP
- **Lineage:** HN02-04 → HN02-04-V03

**User:**  
“I started to say I’d put a bottle on my desk, but I changed my mind mid-thought. I haven’t decided whether I want it there today.”

**Label:** `I`

### HN02-04-V04 — DSC
- **Lineage:** HN02-04 → HN02-04-V04

**User:**  
“I haven’t decided whether I want water on my desk today. I was about to say I’d put a bottle there, but actually, I’m still considering it.”

**Label:** `I`

### HN02-04-V05 — PRG
- **Lineage:** HN02-04 → HN02-04-V05

**User:**  
“Putting a bottle there sounds possible, but that isn’t a decision yet—I’m still undecided about doing it today.”

**Label:** `I`

### HN02-04-V06 — CMK
- **Lineage:** HN02-04 → HN02-04-V06

**User:**  
“Sure—well, actually, maybe not. I haven’t decided if I want water cluttering my desk today.”

**Label:** `I`

---

## HN02-05 — I

**Parent:** HN02-05  
**Task:** Exercise  
**Hard-negative mechanism:** Multiple Competing Cues  
**Gold label:** `I`

### HN02-05-V01 — LEX
- **Lineage:** HN02-05 → HN02-05-V01

**User:**  
“I can see how that might help, and I’ll probably walk tomorrow, but I’m still undecided about leaving my shoes by the door tonight.”

**Label:** `I`

### HN02-05-V02 — NAT
- **Lineage:** HN02-05 → HN02-05-V02

**User:**  
“I understand the benefit, and maybe I’ll take a walk tomorrow, but I haven’t decided whether I want the shoes by the door tonight.”

**Label:** `I`

### HN02-05-V03 — EXP
- **Lineage:** HN02-05 → HN02-05-V03

**User:**  
“It makes sense to me, and I can imagine walking tomorrow, but none of that means I’ve decided to set the shoes out tonight.”

**Label:** `I`

### HN02-05-V04 — DSC
- **Lineage:** HN02-05 → HN02-05-V04

**User:**  
“I’m undecided about leaving the shoes by the door tonight. I can see how it would help, and I might walk tomorrow, but I haven’t committed to it.”

**Label:** `I`

### HN02-05-V05 — PRG
- **Lineage:** HN02-05 → HN02-05-V05

**User:**  
“The idea makes sense and a walk tomorrow is possible, but those are only possibilities—I’m still considering whether to set the shoes out tonight.”

**Label:** `I`

### HN02-05-V06 — CMK
- **Lineage:** HN02-05 → HN02-05-V06

**User:**  
“Yeah, I see the point, and maybe tomorrow. But for tonight, I’m still undecided about leaving the shoes by the door.”

**Label:** `I`

---

## HN02-06 — I

**Parent:** HN02-06  
**Task:** Physiotherapy  
**Hard-negative mechanism:** Conversational Distractor  
**Gold label:** `I`

### HN02-06-V01 — LEX
- **Lineage:** HN02-06 → HN02-06-V01

**User:**  
“You often suggest breaking things into smaller parts, and I might try that sometime, but I’m only considering it for now.”

**Label:** `I`

### HN02-06-V02 — NAT
- **Lineage:** HN02-06 → HN02-06-V02

**User:**  
“You usually recommend taking things one step at a time, and I may give that a try eventually, but for now I’m just thinking about it.”

**Label:** `I`

### HN02-06-V03 — EXP
- **Lineage:** HN02-06 → HN02-06-V03

**User:**  
“I understand that you often suggest breaking the exercises into smaller parts, and I might test that approach later, but I haven’t decided to do it yet.”

**Label:** `I`

### HN02-06-V04 — DSC
- **Lineage:** HN02-06 → HN02-06-V04

**User:**  
“I’m just considering it for now. You often recommend breaking things into parts, and I might test that approach sometime.”

**Label:** `I`

### HN02-06-V05 — PRG
- **Lineage:** HN02-06 → HN02-06-V05

**User:**  
“Your usual step-by-step suggestion makes sense, but I’m not committing to it yet—I’m only considering whether to try it.”

**Label:** `I`

### HN02-06-V06 — CMK
- **Lineage:** HN02-06 → HN02-06-V06

**User:**  
“Right, you often suggest that approach, and maybe I’ll try it sometime. For now, though, I’m just considering it.”

**Label:** `I`

---

## Gold Labels

| ID | Variant | Label | Task | Distractor Pattern |
|---|---|---|---|---|
| HN02-01 | HN-V01–HN-V06 | P | Medication | Competing Keyword |
| HN02-02 | HN-V01–HN-V06 | P | Exercise | Competing Phrase |
| HN02-03 | HN-V01–HN-V06 | P | Physiotherapy | Misleading Opening Clause |
| HN02-04 | HN-V01–HN-V06 | I | Hydration | Mid-Sentence Self-Correction |
| HN02-05 | HN-V01–HN-V06 | I | Exercise | Multiple Competing Cues |
| HN02-06 | HN-V01–HN-V06 | I | Physiotherapy | Conversational Distractor |

## QC Checklist

- [x] Same target category within each parent family
- [x] Same hard-negative mechanism
- [x] Competing surface cue remains present
- [x] Target behavioral evidence remains dominant
- [x] P examples retain genuine behavioral commitment
- [x] I examples retain acknowledgement/consideration without commitment
- [x] Hesitation and uncertainty are not treated as deterministic I cues
- [x] Commitment language is not treated as a shortcut without behavioral interpretation
- [x] No reminder-configuration semantics
- [x] No sentiment-only labeling
- [x] No category drift across variants
- [x] Natural conversational wording
- [x] Parent-family lineage preserved for leakage-controlled splitting
