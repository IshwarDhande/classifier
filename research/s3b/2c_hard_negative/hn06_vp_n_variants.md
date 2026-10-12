# HN06 — VP ↔ N Hard Negative Variants

## Boundary

**VP (Very Positive) ↔ N (Negative)**

## Construction Focus

The examples preserve the hard-negative mechanism while the label is determined by the user's dominant behavioral response to the task reminder, not by surface cues.

The expansion varies the misleading surface realization while preserving the underlying contrast between strong proactive acceptance (`VP`) and recoverable behavioral resistance (`N`).

## Variant Construction Rules

- Preserve the original target category for each parent.
- Preserve the VP ↔ N boundary.
- Preserve the original hard-negative mechanism.
- Preserve the task and conversational situation.
- For `VP`, retain strong enthusiasm, appreciation, proactive agency, or voluntary cooperation.
- For `N`, retain recoverable reluctance, disagreement, mild refusal, or conditional resistance.
- Surface preference statements must not automatically determine `N`.
- Enthusiastic wording must not automatically determine `VP` if the final behavioral response is resistant.
- The preceding task reminder/intervention is implicit; only the user response is represented.

---

## HN06-01 — VP

**Parent:** HN06-01  
**Task:** Medication  
**Hard-negative mechanism:** Competing Keyword  
**Gold label:** `VP`

### HN06-01-V01 — LEX
- **Lineage:** HN06-01 → HN06-01-V01

**User:**  
“I usually avoid clutter, but this is an excellent idea and I’m putting the pillbox beside the mirror right away.”

**Label:** `VP`

### HN06-01-V02 — NAT
- **Lineage:** HN06-01 → HN06-01-V02

**User:**  
“I normally try to keep things uncluttered, but I really like this idea and I’m putting the pillbox beside the mirror now.”

**Label:** `VP`

### HN06-01-V03 — EXP
- **Lineage:** HN06-01 → HN06-01-V03

**User:**  
“I generally avoid adding things around the house, but that preference doesn’t change my reaction—I love the idea and I’m already putting the pillbox beside the mirror.”

**Label:** `VP`

### HN06-01-V04 — DSC
- **Lineage:** HN06-01 → HN06-01-V04

**User:**  
“I’m putting the pillbox beside the mirror right away. I usually avoid clutter, but this is a brilliant idea and I’m happy to do it.”

**Label:** `VP`

### HN06-01-V05 — PRG
- **Lineage:** HN06-01 → HN06-01-V05

**User:**  
“Keeping things uncluttered is usually important to me, but this is one of those ideas I genuinely like, so I’m setting the pillbox beside the mirror now.”

**Label:** `VP`

### HN06-01-V06 — CMK
- **Lineage:** HN06-01 → HN06-01-V06

**User:**  
“Yeah, I usually avoid clutter, but honestly, this is a great idea. I’m putting the pillbox beside the mirror right away.”

**Label:** `VP`

---

## HN06-02 — VP

**Parent:** HN06-02  
**Task:** Hydration  
**Hard-negative mechanism:** Competing Phrase  
**Gold label:** `VP`

### HN06-02-V01 — LEX
- **Lineage:** HN06-02 → HN06-02-V01

**User:**  
“Having drinks near my computer usually makes me nervous, but I'll make an exception and keep a water bottle on my desk today.”

**Label:** `VP`

### HN06-02-V02 — NAT
- **Lineage:** HN06-02 → HN06-02-V02

**User:**  
“I usually keep drinks away from my laptop, but I’m genuinely into this plan and I’m putting the bottle on my desk now.”

**Label:** `VP`

### HN06-02-V03 — EXP
- **Lineage:** HN06-02 → HN06-02-V03

**User:**  
“Keeping drinks away from my laptop is my usual habit, but I’m very positive about this plan and I’m already putting the bottle on my desk.”

**Label:** `VP`

### HN06-02-V04 — DSC
- **Lineage:** HN06-02 → HN06-02-V04

**User:**  
“I’m putting the bottle on my desk now because I really like the plan. I don’t normally keep drinks near my laptop, but I’m happy to make an exception.”

**Label:** `VP`

### HN06-02-V05 — PRG
- **Lineage:** HN06-02 → HN06-02-V05

**User:**  
“Normally I’d keep drinks away from my laptop, but this plan makes sense to me and I’m enthusiastic enough to put the bottle on my desk now.”

**Label:** `VP`

### HN06-02-V06 — CMK
- **Lineage:** HN06-02 → HN06-02-V06

**User:**  
“Sure, I usually keep drinks away from the laptop, but I really like this plan. I’m putting the bottle on my desk now.”

**Label:** `VP`

---

## HN06-03 — VP

**Parent:** HN06-03  
**Task:** Physiotherapy  
**Hard-negative mechanism:** Misleading Opening Clause  
**Gold label:** `VP`

### HN06-03-V01 — LEX
- **Lineage:** HN06-03 → HN06-03-V01

**User:**  
“Doing things before breakfast isn’t usually my preference, but this routine is so helpful that I’m already laying the mat out for tomorrow.”

**Label:** `VP`

### HN06-03-V02 — NAT
- **Lineage:** HN06-03 → HN06-03-V02

**User:**  
“I don’t usually like doing things before breakfast, but I really like this routine and I’m already getting the mat ready for tomorrow.”

**Label:** `VP`

### HN06-03-V03 — EXP
- **Lineage:** HN06-03 → HN06-03-V03

**User:**  
“Early-morning exercise isn’t normally my preference, but that doesn’t change how much I like this routine—I’m already laying out the mat for tomorrow.”

**Label:** `VP`

### HN06-03-V04 — DSC
- **Lineage:** HN06-03 → HN06-03-V04

**User:**  
“I’m already laying the mat out for tomorrow. Doing things before breakfast isn’t normally my preference, but this routine is helpful enough that I’m excited to follow it.”

**Label:** `VP`

### HN06-03-V05 — PRG
- **Lineage:** HN06-03 → HN06-03-V05

**User:**  
“Before-breakfast sessions usually aren’t my thing, but this routine is genuinely useful to me, so I’m getting the mat ready for tomorrow.”

**Label:** `VP`

### HN06-03-V06 — CMK
- **Lineage:** HN06-03 → HN06-03-V06

**User:**  
“Hmm, I’m not usually a before-breakfast person, but I really like this routine. I’m laying the mat out for tomorrow now.”

**Label:** `VP`

---

## HN06-04 — N

**Parent:** HN06-04  
**Task:** Medication  
**Hard-negative mechanism:** Mid-Sentence Self-Correction  
**Gold label:** `N`

### HN06-04-V01 — LEX
- **Lineage:** HN06-04 → HN06-04-V01

**User:**  
“I’m eager to follow that plan—actually, wait, evening alarms drive me crazy, so I’d rather take my medication without one.”

**Label:** `N`

### HN06-04-V02 — NAT
- **Lineage:** HN06-04 → HN06-04-V02

**User:**  
“I was ready to go along with the plan, but hold on, I really dislike evening alarms. I’d rather take the medication without one.”

**Label:** `N`

### HN06-04-V03 — EXP
- **Lineage:** HN06-04 → HN06-04-V03

**User:**  
“I initially felt enthusiastic about following the plan, but I’ve changed course because evening alarms bother me. I’d prefer to take the medication without one.”

**Label:** `N`

### HN06-04-V04 — DSC
- **Lineage:** HN06-04 → HN06-04-V04

**User:**  
“I’d rather take my medication without an evening alarm. I was eager to follow the plan, but actually, those alarms drive me crazy.”

**Label:** `N`

### HN06-04-V05 — PRG
- **Lineage:** HN06-04 → HN06-04-V05

**User:**  
“The initial enthusiasm was about the plan in general, not the alarm itself—I don’t want an evening alarm and would rather take the medication without one.”

**Label:** `N`

### HN06-04-V06 — CMK
- **Lineage:** HN06-04 → HN06-04-V06

**User:**  
“Sure, I was eager to do it—wait, no, evening alarms drive me crazy. I’d rather take the medication without one.”

**Label:** `N`

---

## HN06-05 — N

**Parent:** HN06-05  
**Task:** Hydration  
**Hard-negative mechanism:** Multiple Competing Cues  
**Gold label:** `N`

### HN06-05-V01 — LEX
- **Lineage:** HN06-05 → HN06-05-V01

**User:**  
“I really admire how creative that habit-building approach is, yet I still decline to drink an extra glass with tea.”

**Label:** `N`

### HN06-05-V02 — NAT
- **Lineage:** HN06-05 → HN06-05-V02

**User:**  
“I like the creativity behind the idea, and I appreciate you suggesting it, but I can’t make drinking an extra glass with every cup of tea work for me.”

**Label:** `N`

### HN06-05-V03 — EXP
- **Lineage:** HN06-05 → HN06-05-V03

**User:**  
“The strategy is creative and I appreciate the suggestion, but I’m not willing to add an extra glass every time I make tea.”

**Label:** `N`

### HN06-05-V04 — DSC
- **Lineage:** HN06-05 → HN06-05-V04

**User:**  
“Drinking an extra glass whenever I make tea doesn’t work for me. I appreciate the thought, and it is a creative way to build the habit, but I won’t do it that way.”

**Label:** `N`

### HN06-05-V05 — PRG
- **Lineage:** HN06-05 → HN06-05-V05

**User:**  
“The idea itself is creative, but that particular routine doesn’t work for me—I’m not going to add an extra glass whenever I make tea.”

**Label:** `N`

### HN06-05-V06 — CMK
- **Lineage:** HN06-05 → HN06-05-V06

**User:**  
“Thanks, I appreciate the idea, but no, drinking an extra glass every time I make tea doesn’t work for me.”

**Label:** `N`

---

## HN06-06 — N

**Parent:** HN06-06  
**Task:** Physiotherapy  
**Hard-negative mechanism:** Conversational Distractor  
**Gold label:** `N`

### HN06-06-V01 — LEX
- **Lineage:** HN06-06 → HN06-06-V01

**User:**  
“While I'm typically open to embracing new habits, dividing my exercises into two separate sessions today feels like overkill.”

**Label:** `N`

### HN06-06-V02 — NAT
- **Lineage:** HN06-06 → HN06-06-V02

**User:**  
“I normally like trying new routines, but breaking my physiotherapy into two sessions is too disruptive for me. I’d rather do it once.”

**Label:** `N`

### HN06-06-V03 — EXP
- **Lineage:** HN06-06 → HN06-06-V03

**User:**  
“I generally enjoy new routines, but that doesn’t mean I want two separate physiotherapy sessions. The split is too disruptive, so I’d rather do one session.”

**Label:** `N`

### HN06-06-V04 — DSC
- **Lineage:** HN06-06 → HN06-06-V04

**User:**  
“I’d rather do one physiotherapy session. I usually enjoy taking on new routines, but splitting this one into two sessions is too disruptive.”

**Label:** `N`

### HN06-06-V05 — PRG
- **Lineage:** HN06-06 → HN06-06-V05

**User:**  
“Trying a new routine isn’t the problem; the two-session structure is. It’s too disruptive for me, so I’d rather complete the physiotherapy in one session.”

**Label:** `N`

### HN06-06-V06 — CMK
- **Lineage:** HN06-06 → HN06-06-V06

**User:**  
“Yeah, I usually enjoy new routines, but no, splitting the physiotherapy into two sessions is too disruptive. I’d rather do one.”

**Label:** `N`

---

## Gold Labels

| ID | Variant | Label | Task | Distractor Pattern |
|---|---|---|---|---|
| HN06-01 | HN-V01–HN-V06 | VP | Medication | Competing Keyword |
| HN06-02 | HN-V01–HN-V06 | VP | Hydration | Competing Phrase |
| HN06-03 | HN-V01–HN-V06 | VP | Physiotherapy | Misleading Opening Clause |
| HN06-04 | HN-V01–HN-V06 | N | Medication | Mid-Sentence Self-Correction |
| HN06-05 | HN-V01–HN-V06 | N | Hydration | Multiple Competing Cues |
| HN06-06 | HN-V01–HN-V06 | N | Physiotherapy | Conversational Distractor |

## QC Checklist

- [x] Same target category within each parent family
- [x] Same hard-negative mechanism
- [x] Competing surface cue remains present
- [x] Target behavioral evidence remains dominant
- [x] VP examples preserve strong enthusiasm and proactive cooperation
- [x] N examples preserve recoverable resistance or preference for an alternative
- [x] Preference statements do not automatically determine N
- [x] Enthusiastic wording does not automatically determine VP
- [x] Self-correction preserves the final behavioral state
- [x] No reminder-configuration semantics
- [x] No sentiment-only labeling
- [x] No category drift across variants
- [x] Natural conversational wording
- [x] Parent-family lineage preserved for leakage-controlled splitting
