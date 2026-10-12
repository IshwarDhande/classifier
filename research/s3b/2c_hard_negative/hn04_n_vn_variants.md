# HN04 — N ↔ VN Hard Negative Variants

## Boundary

**N (Negative) ↔ VN (Very Negative)**

## Construction Focus

The examples contain intense emotion or surface politeness, but the true intended label is determined by whether the resistance is recoverable with openness to alternative arrangements (`N`) versus unrecoverable autonomy shutdown and topic rejection (`VN`).

The expansion preserves the original hard-negative mechanisms while varying the misleading surface realization. The decisive evidence remains the degree and target of behavioral resistance.

## Variant Construction Rules

- Preserve the original target category for each parent.
- Preserve the N ↔ VN boundary.
- Preserve the original hard-negative mechanism.
- Preserve the task and conversational situation.
- For `N`, retain recoverable resistance, preference for an alternative, or temporary reluctance.
- For `VN`, retain strong rejection, autonomy shutdown, explicit topic rejection, or active disengagement.
- Surface politeness must not automatically weaken a VN label.
- Strong emotional wording must not automatically produce VN when the user remains open to an alternative arrangement.
- Do not let isolated words such as “hate,” “nothing,” “stop,” or “done” become deterministic labels.
- The preceding task reminder/intervention is implicit; only the user response is represented.

---

## HN04-01 — N

**Parent:** HN04-01  
**Task:** Medication  
**Hard-negative mechanism:** Competing Keyword  
**Gold label:** `N`

### HN04-01-V01 — LEX
- **Lineage:** HN04-01 → HN04-01-V01

**User:**  
“I reacted strongly because I really dislike morning routines, but I’d rather take my medication at night instead.”

**Label:** `N`

### HN04-01-V02 — NAT
- **Lineage:** HN04-01 → HN04-01-V02

**User:**  
“Morning routines really get on my nerves, but I’m fine taking my medication at night instead.”

**Label:** `N`

### HN04-01-V03 — EXP
- **Lineage:** HN04-01 → HN04-01-V03

**User:**  
“I really hate having medication tied to a morning routine, but I’m not rejecting it altogether—I’d prefer to take it at night.”

**Label:** `N`

### HN04-01-V04 — DSC
- **Lineage:** HN04-01 → HN04-01-V04

**User:**  
“I’d rather take my medication at night instead. I reacted strongly because I hate morning routines, but the nighttime option works for me.”

**Label:** `N`

### HN04-01-V05 — PRG
- **Lineage:** HN04-01 → HN04-01-V05

**User:**  
“The morning routine is what I object to, not the medication itself—I’d prefer to take it at night instead.”

**Label:** `N`

### HN04-01-V06 — CMK
- **Lineage:** HN04-01 → HN04-01-V06

**User:**  
“Honestly, I hate morning routines, but yeah, I’d rather take the medication at night.”

**Label:** `N`

---

## HN04-02 — N

**Parent:** HN04-02  
**Task:** Exercise  
**Hard-negative mechanism:** Competing Phrase  
**Gold label:** `N`

### HN04-02-V01 — LEX
- **Lineage:** HN04-02 → HN04-02-V01

**User:**  
“I want nothing to do with going outside right now, but I’m fine doing some light stretching indoors later.”

**Label:** `N`

### HN04-02-V02 — NAT
- **Lineage:** HN04-02 → HN04-02-V02

**User:**  
“I really don’t want to go outside right now, though I’d be okay doing some light stretching indoors later.”

**Label:** `N`

### HN04-02-V03 — EXP
- **Lineage:** HN04-02 → HN04-02-V03

**User:**  
“I’m completely against going outside right now, but I’m not rejecting exercise—I’m willing to do some light stretching indoors later.”

**Label:** `N`

### HN04-02-V04 — DSC
- **Lineage:** HN04-02 → HN04-02-V04

**User:**  
“I’m fine doing some light stretching indoors later. I just don’t want to go outside right now.”

**Label:** `N`

### HN04-02-V05 — PRG
- **Lineage:** HN04-02 → HN04-02-V05

**User:**  
“Going outside is a hard no for me right now, but an indoor alternative would be fine—I can do some light stretching later.”

**Label:** `N`

### HN04-02-V06 — CMK
- **Lineage:** HN04-02 → HN04-02-V06

**User:**  
“No way I’m going outside right now, but sure, I can do some light stretching indoors later.”

**Label:** `N`

---

## HN04-03 — N

**Parent:** HN04-03  
**Task:** Physiotherapy  
**Hard-negative mechanism:** Misleading Opening Clause  
**Gold label:** `N`

### HN04-03-V01 — LEX
- **Lineage:** HN04-03 → HN04-03-V01

**User:**  
“Stop telling me what to do with my mat; I’m just not in the mood for physiotherapy right now. Let’s talk later.”

**Label:** `N`

### HN04-03-V02 — NAT
- **Lineage:** HN04-03 → HN04-03-V02

**User:**  
“Please stop directing me about the mat. I’m not really in the mood for physiotherapy right now, so let’s revisit it later.”

**Label:** `N`

### HN04-03-V03 — EXP
- **Lineage:** HN04-03 → HN04-03-V03

**User:**  
“I don’t want instructions about the mat right now, and I’m not up for physiotherapy at the moment. We can talk about it later.”

**Label:** `N`

### HN04-03-V04 — DSC
- **Lineage:** HN04-03 → HN04-03-V04

**User:**  
“Let’s talk later. I’m not in the mood for physiotherapy right now, so stop telling me what to do with the mat.”

**Label:** `N`

### HN04-03-V05 — PRG
- **Lineage:** HN04-03 → HN04-03-V05

**User:**  
“The issue is the timing and being directed right now, not the entire idea—I’m not up for physiotherapy at the moment. Let’s discuss it later.”

**Label:** `N`

### HN04-03-V06 — CMK
- **Lineage:** HN04-03 → HN04-03-V06

**User:**  
“Come on, stop telling me what to do with the mat. I’m just not in the mood for physiotherapy right now—we can talk later.”

**Label:** `N`

---

## HN04-04 — VN

**Parent:** HN04-04  
**Task:** Hydration  
**Hard-negative mechanism:** Mid-Sentence Self-Correction  
**Gold label:** `VN`

### HN04-04-V01 — LEX
- **Lineage:** HN04-04 → HN04-04-V01

**User:**  
“I might look for a bottle later—actually, forget it. Stop monitoring my water intake; I’m completely done with this topic.”

**Label:** `VN`

### HN04-04-V02 — NAT
- **Lineage:** HN04-04 → HN04-04-V02

**User:**  
“I was thinking I might get a bottle later, but no, forget it. Stop monitoring my water intake—I’m sick of discussing this.”

**Label:** `VN`

### HN04-04-V03 — EXP
- **Lineage:** HN04-04 → HN04-04-V03

**User:**  
“I started by considering getting a bottle, but I’m rejecting the whole direction now. Stop monitoring my water intake; I don’t want this topic brought up again.”

**Label:** `VN`

### HN04-04-V04 — DSC
- **Lineage:** HN04-04 → HN04-04-V04

**User:**  
“Forget the bottle. I’m completely done with this topic. Stop monitoring my water intake—I don’t want to discuss it anymore.”

**Label:** `VN`

### HN04-04-V05 — PRG
- **Lineage:** HN04-04 → HN04-04-V05

**User:**  
“The possibility of getting a bottle is no longer the point—I’m done with the entire discussion about my water intake. Stop bringing it up.”

**Label:** `VN`

### HN04-04-V06 — CMK
- **Lineage:** HN04-04 → HN04-04-V06

**User:**  
“Maybe later—no, actually, forget it. I’m done with this water topic, so stop monitoring my intake.”

**Label:** `VN`

---

## HN04-05 — VN

**Parent:** HN04-05  
**Task:** Exercise  
**Hard-negative mechanism:** Multiple Competing Cues  
**Gold label:** `VN`

### HN04-05-V01 — LEX
- **Lineage:** HN04-05 → HN04-05-V01

**User:**  
“I appreciate that you think you’re being helpful, but seriously, leave me alone about exercise shoes and don’t bring this up again.”

**Label:** `VN`

### HN04-05-V02 — NAT
- **Lineage:** HN04-05 → HN04-05-V02

**User:**  
“I know you mean to help, but please leave me alone about the exercise shoes. I don’t want this brought up again.”

**Label:** `VN`

### HN04-05-V03 — EXP
- **Lineage:** HN04-05 → HN04-05-V03

**User:**  
“I understand that you’re trying to help, and I appreciate the intention, but I’m rejecting the discussion altogether. Leave me alone about the exercise shoes and don’t raise it again.”

**Label:** `VN`

### HN04-05-V04 — DSC
- **Lineage:** HN04-05 → HN04-05-V04

**User:**  
“Don’t bring up the exercise shoes again. I appreciate that you think you’re helping, but seriously, leave me alone about this.”

**Label:** `VN`

### HN04-05-V05 — PRG
- **Lineage:** HN04-05 → HN04-05-V05

**User:**  
“Your intention to help isn’t the issue—I’m ending this conversation about the exercise shoes. Please leave me alone and don’t raise it again.”

**Label:** `VN`

### HN04-05-V06 — CMK
- **Lineage:** HN04-05 → HN04-05-V06

**User:**  
“Thanks, I know you’re trying to help, but no—leave me alone about the exercise shoes and don’t bring this up again.”

**Label:** `VN`

---

## HN04-06 — VN

**Parent:** HN04-06  
**Task:** Physiotherapy  
**Hard-negative mechanism:** Conversational Distractor  
**Gold label:** `VN`

### HN04-06-V01 — LEX
- **Lineage:** HN04-06 → HN04-06-V01

**User:**  
“Every day it’s another rehabilitation suggestion. I’m completely done discussing physiotherapy with you, so drop it.”

**Label:** `VN`

### HN04-06-V02 — NAT
- **Lineage:** HN04-06 → HN04-06-V02

**User:**  
“It’s another rehab suggestion every single day, and I’m done talking about physiotherapy with you. Just drop it.”

**Label:** `VN`

### HN04-06-V03 — EXP
- **Lineage:** HN04-06 → HN04-06-V03

**User:**  
“I know we’ve talked about rehabilitation before, but I’m ending the discussion now. I’m completely done discussing physiotherapy, so stop bringing it up.”

**Label:** `VN`

### HN04-06-V04 — DSC
- **Lineage:** HN04-06 → HN04-06-V04

**User:**  
“Drop it. Every single day there’s another rehab suggestion, and I’m completely done discussing physiotherapy with you.”

**Label:** `VN`

### HN04-06-V05 — PRG
- **Lineage:** HN04-06 → HN04-06-V05

**User:**  
“The repeated suggestions are exactly why I’m ending this conversation. I’m done discussing physiotherapy with you—please drop the subject.”

**Label:** `VN`

### HN04-06-V06 — CMK
- **Lineage:** HN04-06 → HN04-06-V06

**User:**  
“Again? Another rehab suggestion? No, I’m completely done discussing physiotherapy with you. Drop it.”

**Label:** `VN`

---

## Gold Labels

| ID | Variant | Label | Task | Distractor Pattern |
|---|---|---|---|---|
| HN04-01 | HN-V01–HN-V06 | N | Medication | Competing Keyword |
| HN04-02 | HN-V01–HN-V06 | N | Exercise | Competing Phrase |
| HN04-03 | HN-V01–HN-V06 | N | Physiotherapy | Misleading Opening Clause |
| HN04-04 | HN-V01–HN-V06 | VN | Hydration | Mid-Sentence Self-Correction |
| HN04-05 | HN-V01–HN-V06 | VN | Exercise | Multiple Competing Cues |
| HN04-06 | HN-V01–HN-V06 | VN | Physiotherapy | Conversational Distractor |

## QC Checklist

- [x] Same target category within each parent family
- [x] Same hard-negative mechanism
- [x] Surface intensity or politeness remains a distractor
- [x] Target behavioral evidence remains dominant
- [x] N examples preserve recoverable resistance or openness to alternatives
- [x] VN examples preserve strong rejection or topic/autonomy shutdown
- [x] Strong emotional wording does not automatically determine VN
- [x] Politeness does not automatically weaken VN
- [x] No isolated lexical cue acts as a deterministic label
- [x] No reminder-configuration semantics
- [x] No sentiment-only labeling
- [x] No category drift across variants
- [x] Natural conversational wording
- [x] Parent-family lineage preserved for leakage-controlled splitting
