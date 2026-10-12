# HN09 — P ↔ VN Hard Negative Variants

## Boundary

**P (Positive) ↔ VN (Very Negative)**

## Construction Focus

The examples preserve the hard-negative mechanism while the label is determined by the user's dominant behavioral response to the task reminder, not by surface cues.

The expansion varies misleading lexical, pragmatic, and conversational cues while preserving the underlying contrast between ordinary cooperation/commitment (`P`) and strong rejection, opposition, or active disengagement (`VN`).

## Variant Construction Rules

- Preserve the original target category for each parent.
- Preserve the P ↔ VN boundary.
- Preserve the original hard-negative mechanism.
- Preserve the task and conversational situation.
- For `P`, retain ordinary acceptance, cooperation, or behavioral commitment without strong enthusiasm.
- For `VN`, retain strong rejection, explicit opposition, autonomy shutdown, or active disengagement.
- Surface dislike or mild complaint must not automatically determine VN when the user still commits to the task.
- Politeness or initial agreement must not automatically determine P when the final behavioral response strongly rejects the interaction or topic.
- The preceding task reminder/intervention is implicit; only the user response is represented.

---

## HN09-01 — P

**Parent:** HN09-01  
**Task:** Medication  
**Hard-negative mechanism:** Competing Keyword  
**Gold label:** `P`

### HN09-01-V01 — LEX
- **Lineage:** HN09-01 → HN09-01-V01

**User:**  
“Normally I hate having pills anywhere near my sleep space, but fine, I'll place them next to the clock.”

**Label:** `P`

### HN09-01-V02 — NAT
- **Lineage:** HN09-01 → HN09-01-V02

**User:**  
“I’m not really a fan of keeping pills by the bed, but okay, I’ll put the pillbox beside the clock.”

**Label:** `P`

### HN09-01-V03 — EXP
- **Lineage:** HN09-01 → HN09-01-V03

**User:**  
“I don’t particularly like having pills beside my bed, but I’m still willing to put the pillbox beside the clock.”

**Label:** `P`

### HN09-01-V04 — DSC
- **Lineage:** HN09-01 → HN09-01-V04

**User:**  
“I’ll put the pillbox beside the clock. I’ve never liked keeping pills by my bed, but I’m okay with doing it this way.”

**Label:** `P`

### HN09-01-V05 — PRG
- **Lineage:** HN09-01 → HN09-01-V05

**User:**  
“Keeping pills by the bed isn’t my preference, but that doesn’t stop me from following through—I’ll put the pillbox beside the clock.”

**Label:** `P`

### HN09-01-V06 — CMK
- **Lineage:** HN09-01 → HN09-01-V06

**User:**  
“Yeah, I don’t like keeping pills by my bed, but alright, I’ll put the pillbox beside the clock.”

**Label:** `P`

---

## HN09-02 — P

**Parent:** HN09-02  
**Task:** Hydration  
**Hard-negative mechanism:** Competing Phrase  
**Gold label:** `P`

### HN09-02-V01 — LEX
- **Lineage:** HN09-02 → HN09-02-V01

**User:**  
“I absolutely detest having a cluttered workspace, however I will keep a bottle of water there.”

**Label:** `P`

### HN09-02-V02 — NAT
- **Lineage:** HN09-02 → HN09-02-V02

**User:**  
“I’m not a fan of clutter on my desk, but sure, I’ll keep a water bottle there today.”

**Label:** `P`

### HN09-02-V03 — EXP
- **Lineage:** HN09-02 → HN09-02-V03

**User:**  
“Having extra things on my desk bothers me, but I’m willing to keep a water bottle there today.”

**Label:** `P`

### HN09-02-V04 — DSC
- **Lineage:** HN09-02 → HN09-02-V04

**User:**  
“I’ll keep the water bottle on my desk today. I really dislike desk clutter, but I’m fine making that exception.”

**Label:** `P`

### HN09-02-V05 — PRG
- **Lineage:** HN09-02 → HN09-02-V05

**User:**  
“Desk clutter isn’t something I normally like, but I can live with it for this—I’ll keep the water bottle there today.”

**Label:** `P`

### HN09-02-V06 — CMK
- **Lineage:** HN09-02 → HN09-02-V06

**User:**  
“Honestly, I hate desk clutter, but okay, I’ll keep the water bottle there today.”

**Label:** `P`

---

## HN09-03 — P

**Parent:** HN09-03  
**Task:** Exercise  
**Hard-negative mechanism:** Misleading Opening Clause  
**Gold label:** `P`

### HN09-03-V01 — LEX
- **Lineage:** HN09-03 → HN09-03-V01

**User:**  
“I’m not planning to turn this into a major routine, but yes, I’ll take the fifteen-minute walk after dinner.”

**Label:** `P`

### HN09-03-V02 — NAT
- **Lineage:** HN09-03 → HN09-03-V02

**User:**  
“I’m not looking to make a big routine out of it, but yes, I’ll take the fifteen-minute walk after dinner.”

**Label:** `P`

### HN09-03-V03 — EXP
- **Lineage:** HN09-03 → HN09-03-V03

**User:**  
“I don’t intend to make this a major long-term routine, but I am willing to do the fifteen-minute walk after dinner.”

**Label:** `P`

### HN09-03-V04 — DSC
- **Lineage:** HN09-03 → HN09-03-V04

**User:**  
“Yes, I’ll take the fifteen-minute walk after dinner. I’m not planning to make it a big routine, but I’m happy to do this one.”

**Label:** `P`

### HN09-03-V05 — PRG
- **Lineage:** HN09-03 → HN09-03-V05

**User:**  
“Making it a major routine isn’t necessary for me; for today, though, I’ll take the fifteen-minute walk after dinner.”

**Label:** `P`

### HN09-03-V06 — CMK
- **Lineage:** HN09-03 → HN09-03-V06

**User:**  
“Sure, I’m not trying to make a huge routine out of this, but yes, I’ll take the fifteen-minute walk after dinner.”

**Label:** `P`

---

## HN09-04 — VN

**Parent:** HN09-04  
**Task:** Medication  
**Hard-negative mechanism:** Mid-Sentence Self-Correction  
**Gold label:** `VN`

### HN09-04-V01 — LEX
- **Lineage:** HN09-04 → HN09-04-V01

**User:**  
“Alright, that seems handy—wait, no it doesn't. Stop telling me how to organize my pills.”

**Label:** `VN`

### HN09-04-V02 — NAT
- **Lineage:** HN09-04 → HN09-04-V02

**User:**  
“Yeah, that sounds convenient—wait, no. I’m done with these suggestions about organizing my medication, so stop telling me how to manage it.”

**Label:** `VN`

### HN09-04-V03 — EXP
- **Lineage:** HN09-04 → HN09-04-V03

**User:**  
“I initially agreed that it sounded convenient, but I’m withdrawing that completely. Stop telling me how to organize my medication; I’m tired of these suggestions.”

**Label:** `VN`

### HN09-04-V04 — DSC
- **Lineage:** HN09-04 → HN09-04-V04

**User:**  
“Stop telling me how to organize my medication. I’m sick of these suggestions. I said it sounded convenient, but actually, no, I don’t want this anymore.”

**Label:** `VN`

### HN09-04-V05 — PRG
- **Lineage:** HN09-04 → HN09-04-V05

**User:**  
“The initial agreement doesn’t stand—I’m ending this discussion about how I organize my medication. Stop giving me these suggestions.”

**Label:** `VN`

### HN09-04-V06 — CMK
- **Lineage:** HN09-04 → HN09-04-V06

**User:**  
“Sure, sounds convenient—no, actually, stop. I’m sick of these medication suggestions, so leave it alone.”

**Label:** `VN`

---

## HN09-05 — VN

**Parent:** HN09-05  
**Task:** Hydration  
**Hard-negative mechanism:** Multiple Competing Cues  
**Gold label:** `VN`

### HN09-05-V01 — LEX
- **Lineage:** HN09-05 → HN09-05-V01

**User:**  
“I recognize your good intentions regarding my hydration, but please stop nagging me with these reminders.”

**Label:** `VN`

### HN09-05-V02 — NAT
- **Lineage:** HN09-05 → HN09-05-V02

**User:**  
“I understand you’re trying to help me stay hydrated, but stop pushing the drinking reminders. I don’t want to be micromanaged.”

**Label:** `VN`

### HN09-05-V03 — EXP
- **Lineage:** HN09-05 → HN09-05-V03

**User:**  
“I appreciate the goal of helping with hydration, but I’m rejecting the reminder approach completely. Stop pushing drinking reminders; I don’t want this level of monitoring.”

**Label:** `VN`

### HN09-05-V04 — DSC
- **Lineage:** HN09-05 → HN09-05-V04

**User:**  
“I don’t want to be micromanaged about hydration. I know you’re trying to help, but stop pushing the drinking reminders.”

**Label:** `VN`

### HN09-05-V05 — PRG
- **Lineage:** HN09-05 → HN09-05-V05

**User:**  
“The hydration goal isn’t what I’m objecting to—I’m rejecting the repeated reminders and the feeling of being monitored. Stop pushing them.”

**Label:** `VN`

### HN09-05-V06 — CMK
- **Lineage:** HN09-05 → HN09-05-V06

**User:**  
“Thanks, I know you’re trying to help, but no—stop pushing the drinking reminders. I don’t want to be micromanaged.”

**Label:** `VN`

---

## HN09-06 — VN

**Parent:** HN09-06  
**Task:** Physiotherapy  
**Hard-negative mechanism:** Conversational Distractor  
**Gold label:** `VN`

### HN09-06-V01 — LEX
- **Lineage:** HN09-06 → HN09-06-V01

**User:**  
“Every time we talk you bring up physiotherapy. I’m completely done discussing it, so drop the subject.”

**Label:** `VN`

### HN09-06-V02 — NAT
- **Lineage:** HN09-06 → HN09-06-V02

**User:**  
“Whenever we talk, physiotherapy comes up again. I’m done discussing it, so please drop the subject.”

**Label:** `VN`

### HN09-06-V03 — EXP
- **Lineage:** HN09-06 → HN09-06-V03

**User:**  
“I know physiotherapy has come up in our previous conversations, but I’m ending that discussion now. I’m completely done with the topic, so stop bringing it up.”

**Label:** `VN`

### HN09-06-V04 — DSC
- **Lineage:** HN09-06 → HN09-06-V04

**User:**  
“Drop the subject. Every time we talk you bring up physiotherapy, and I’m completely done discussing it.”

**Label:** `VN`

### HN09-06-V05 — PRG
- **Lineage:** HN09-06 → HN09-06-V05

**User:**  
“The repeated discussion itself is the problem—I’m ending the physiotherapy topic completely. Please stop bringing it up.”

**Label:** `VN`

### HN09-06-V06 — CMK
- **Lineage:** HN09-06 → HN09-06-V06

**User:**  
“Again with the physiotherapy? No, I’m done discussing it. Drop the subject.”

**Label:** `VN`

---

## Gold Labels

| ID | Variant | Label | Task | Distractor Pattern |
|---|---|---|---|---|
| HN09-01 | HN-V01–HN-V06 | P | Medication | Competing Keyword |
| HN09-02 | HN-V01–HN-V06 | P | Hydration | Competing Phrase |
| HN09-03 | HN-V01–HN-V06 | P | Exercise | Misleading Opening Clause |
| HN09-04 | HN-V01–HN-V06 | VN | Medication | Mid-Sentence Self-Correction |
| HN09-05 | HN-V01–HN-V06 | VN | Hydration | Multiple Competing Cues |
| HN09-06 | HN-V01–HN-V06 | VN | Physiotherapy | Conversational Distractor |

## QC Checklist

- [x] Same target category within each parent family
- [x] Same hard-negative mechanism
- [x] Competing surface cue remains present
- [x] Target behavioral evidence remains dominant
- [x] P examples preserve ordinary cooperation/commitment
- [x] VN examples preserve strong rejection/disengagement
- [x] Mild dislike does not automatically determine VN
- [x] Initial politeness/agreement does not automatically determine P
- [x] Self-correction preserves the final behavioral state
- [x] No reminder-configuration semantics
- [x] No sentiment-only labeling
- [x] No category drift across variants
- [x] Natural conversational wording
- [x] Parent-family lineage preserved for leakage-controlled splitting
