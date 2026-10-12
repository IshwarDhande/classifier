# HN03 — I ↔ N Hard Negative Variants

## Boundary

**I (Indifferent) ↔ N (Negative)**

## Construction Focus

The examples contain negative-sounding idioms or refusal-related cues, but the true intended label is determined by whether the user maintains uncommitted postponement (`I`) versus active behavioral resistance (`N`).

The expansion preserves the original hard-negative mechanisms while varying the misleading surface realization. The decisive evidence remains the user's behavioral commitment or resistance.

## Variant Construction Rules

- Preserve the original target category for each parent.
- Preserve the I ↔ N boundary.
- Preserve the original hard-negative mechanism.
- Preserve the task and conversational situation.
- Keep negative-sounding or refusal-related cues as distractors where applicable.
- For `I`, retain uncertainty, postponement, or insufficient behavioral commitment without active resistance.
- For `N`, retain observable reluctance, disagreement, mild refusal, or conditional resistance.
- Do not let isolated negative words or refusal-related expressions become deterministic labels.
- The preceding task reminder/intervention is implicit; only the user response is represented.

---

## HN03-01 — I

**Parent:** HN03-01  
**Task:** Medication  
**Hard-negative mechanism:** Competing Keyword  
**Gold label:** `I`

### HN03-01-V01 — LEX
- **Lineage:** HN03-01 → HN03-01-V01

**User:**  
“I’m not opposed to taking the medication, but I’m still deciding whether this timing works with my schedule.”

**Label:** `I`

### HN03-01-V02 — NAT
- **Lineage:** HN03-01 → HN03-01-V02

**User:**  
“I’m not really against taking it; I just haven’t decided whether this time fits my schedule.”

**Label:** `I`

### HN03-01-V03 — EXP
- **Lineage:** HN03-01 → HN03-01-V03

**User:**  
“I don’t have a problem with taking the medication itself, but I’m still weighing whether I can fit this timing into my schedule.”

**Label:** `I`

### HN03-01-V04 — DSC
- **Lineage:** HN03-01 → HN03-01-V04

**User:**  
“I’m still deciding whether this timing works with my schedule. I’m not against taking the medication, but I haven’t settled on it yet.”

**Label:** `I`

### HN03-01-V05 — PRG
- **Lineage:** HN03-01 → HN03-01-V05

**User:**  
“Whether I’m against it isn’t really the issue; I’m simply still deciding if this timing makes sense for my schedule.”

**Label:** `I`

### HN03-01-V06 — CMK
- **Lineage:** HN03-01 → HN03-01-V06

**User:**  
“No, I’m not against taking it or anything—I’m just still figuring out whether this timing works for me.”

**Label:** `I`

---

## HN03-02 — I

**Parent:** HN03-02  
**Task:** Exercise  
**Hard-negative mechanism:** Competing Phrase  
**Gold label:** `I`

### HN03-02-V01 — LEX
- **Lineage:** HN03-02 → HN03-02-V01

**User:**  
“I wouldn’t say I dislike walking, but I’m only weighing whether a walk after lunch fits my plans today.”

**Label:** `I`

### HN03-02-V02 — NAT
- **Lineage:** HN03-02 → HN03-02-V02

**User:**  
“It’s not that I dislike walking; I’m just trying to decide whether after lunch works for me today.”

**Label:** `I`

### HN03-02-V03 — EXP
- **Lineage:** HN03-02 → HN03-02-V03

**User:**  
“I don’t really have anything against walking, but I haven’t decided whether taking a walk after lunch fits into today’s plans.”

**Label:** `I`

### HN03-02-V04 — DSC
- **Lineage:** HN03-02 → HN03-02-V04

**User:**  
“I’m still weighing whether after lunch fits my plans today. I wouldn’t say I dislike walking; I just haven’t decided on the timing.”

**Label:** `I`

### HN03-02-V05 — PRG
- **Lineage:** HN03-02 → HN03-02-V05

**User:**  
“Disliking walking isn’t the issue—I’m simply considering whether after lunch is a workable time today.”

**Label:** `I`

### HN03-02-V06 — CMK
- **Lineage:** HN03-02 → HN03-02-V06

**User:**  
“Not really, I don’t dislike walking. I’m just thinking about whether after lunch fits my plans today.”

**Label:** `I`

---

## HN03-03 — I

**Parent:** HN03-03  
**Task:** Physiotherapy  
**Hard-negative mechanism:** Misleading Opening Clause  
**Gold label:** `I`

### HN03-03-V01 — LEX
- **Lineage:** HN03-03 → HN03-03-V01

**User:**  
“The hallway is a little narrow, but I haven’t ruled out doing the physiotherapy there; I’ll decide later.”

**Label:** `I`

### HN03-03-V02 — NAT
- **Lineage:** HN03-03 → HN03-03-V02

**User:**  
“The hallway is kind of tight, although I’m not ruling out doing the exercises there. I’ll figure it out later.”

**Label:** `I`

### HN03-03-V03 — EXP
- **Lineage:** HN03-03 → HN03-03-V03

**User:**  
“The narrow hallway could make the setup awkward, but I haven’t rejected the idea of doing physiotherapy there; I’ll decide later.”

**Label:** `I`

### HN03-03-V04 — DSC
- **Lineage:** HN03-03 → HN03-03-V04

**User:**  
“I haven’t ruled out doing the physiotherapy in the hallway. It is somewhat narrow, though, so I’ll decide later.”

**Label:** `I`

### HN03-03-V05 — PRG
- **Lineage:** HN03-03 → HN03-03-V05

**User:**  
“The hallway being narrow is a consideration, not a refusal—I’m still leaving the option open and will decide later.”

**Label:** `I`

### HN03-03-V06 — CMK
- **Lineage:** HN03-03 → HN03-03-V06

**User:**  
“Hmm, the hallway is pretty narrow, but I haven’t ruled it out. I’ll see later.”

**Label:** `I`

---

## HN03-04 — N

**Parent:** HN03-04  
**Task:** Hydration  
**Hard-negative mechanism:** Mid-Sentence Self-Correction  
**Gold label:** `N`

### HN03-04-V01 — LEX
- **Lineage:** HN03-04 → HN03-04-V01

**User:**  
“A bottle on the desk might be fine—actually, no, I’d rather keep my desk clear and get water from the kitchen.”

**Label:** `N`

### HN03-04-V02 — NAT
- **Lineage:** HN03-04 → HN03-04-V02

**User:**  
“I was thinking a bottle on the desk could work, but actually I’d rather keep the desk clear and get my water from the kitchen.”

**Label:** `N`

### HN03-04-V03 — EXP
- **Lineage:** HN03-04 → HN03-04-V03

**User:**  
“I initially considered putting a bottle on the desk, but I’ve decided against that because I’d rather keep the desk clear and get water from the kitchen.”

**Label:** `N`

### HN03-04-V04 — DSC
- **Lineage:** HN03-04 → HN03-04-V04

**User:**  
“I’d rather keep my desk clear and get water from the kitchen instead. A bottle on the desk might have worked, but no, I don’t want it there.”

**Label:** `N`

### HN03-04-V05 — PRG
- **Lineage:** HN03-04 → HN03-04-V05

**User:**  
“The desk option sounds possible at first, but it’s not what I want—I’d rather keep the desk clear and get water from the kitchen.”

**Label:** `N`

### HN03-04-V06 — CMK
- **Lineage:** HN03-04 → HN03-04-V06

**User:**  
“Sure, a bottle could go there—actually, no, I’d rather keep my desk clear and get water from the kitchen.”

**Label:** `N`

---

## HN03-05 — N

**Parent:** HN03-05  
**Task:** Exercise  
**Hard-negative mechanism:** Multiple Competing Cues  
**Gold label:** `N`

### HN03-05-V01 — LEX
- **Lineage:** HN03-05 → HN03-05-V01

**User:**  
“I realize having a routine is helpful and fitness matters to me, but I really don’t want to leave my walking shoes by the door today.”

**Label:** `N`

### HN03-05-V02 — NAT
- **Lineage:** HN03-05 → HN03-05-V02

**User:**  
“I understand that it’s a sensible routine, and I’m still considering my fitness, but I don’t want my walking shoes left by the door today.”

**Label:** `N`

### HN03-05-V03 — EXP
- **Lineage:** HN03-05 → HN03-05-V03

**User:**  
“I can see why the routine makes sense, and I’m thinking about staying active, but I’m not willing to leave my walking shoes by the door today.”

**Label:** `N`

### HN03-05-V04 — DSC
- **Lineage:** HN03-05 → HN03-05-V04

**User:**  
“I really don’t want to leave my walking shoes by the door today. I know the routine is sensible, and I’m still thinking about fitness overall, but that setup isn’t for me.”

**Label:** `N`

### HN03-05-V05 — PRG
- **Lineage:** HN03-05 → HN03-05-V05

**User:**  
“The routine itself may be sensible, but that doesn’t change my response—I don’t want to leave the walking shoes by the door today.”

**Label:** `N`

### HN03-05-V06 — CMK
- **Lineage:** HN03-05 → HN03-05-V06

**User:**  
“Yeah, I know it makes sense, and I’m thinking about fitness. But honestly, I don’t want the walking shoes by the door today.”

**Label:** `N`

---

## HN03-06 — N

**Parent:** HN03-06  
**Task:** Physiotherapy  
**Hard-negative mechanism:** Conversational Distractor  
**Gold label:** `N`

### HN03-06-V01 — LEX
- **Lineage:** HN03-06 → HN03-06-V01

**User:**  
“We’ve discussed splitting sessions before, but having two separate interruptions doesn’t work for me; I’d rather do my physiotherapy all at once.”

**Label:** `N`

### HN03-06-V02 — NAT
- **Lineage:** HN03-06 → HN03-06-V02

**User:**  
“We’ve talked about breaking the sessions up before, but I don’t like having two separate interruptions. I’d rather do the physiotherapy in one go.”

**Label:** `N`

### HN03-06-V03 — EXP
- **Lineage:** HN03-06 → HN03-06-V03

**User:**  
“I remember our earlier discussion about splitting the sessions, but I don’t want two separate interruptions; I’d prefer to complete the physiotherapy all at once.”

**Label:** `N`

### HN03-06-V04 — DSC
- **Lineage:** HN03-06 → HN03-06-V04

**User:**  
“I’d rather do my physiotherapy all at once. We’ve discussed breaking sessions up before, but two separate interruptions don’t suit me.”

**Label:** `N`

### HN03-06-V05 — PRG
- **Lineage:** HN03-06 → HN03-06-V05

**User:**  
“Even though we’ve discussed splitting the sessions before, I’m not agreeing to two interruptions—I’d rather complete the physiotherapy in one session.”

**Label:** `N`

### HN03-06-V06 — CMK
- **Lineage:** HN03-06 → HN03-06-V06

**User:**  
“Right, we’ve talked about breaking it up before, but no, two separate interruptions don’t suit me. I’d rather do it all at once.”

**Label:** `N`

---

## Gold Labels

| ID | Variant | Label | Task | Distractor Pattern |
|---|---|---|---|---|
| HN03-01 | HN-V01–HN-V06 | I | Medication | Competing Keyword |
| HN03-02 | HN-V01–HN-V06 | I | Exercise | Competing Phrase |
| HN03-03 | HN-V01–HN-V06 | I | Physiotherapy | Misleading Opening Clause |
| HN03-04 | HN-V01–HN-V06 | N | Hydration | Mid-Sentence Self-Correction |
| HN03-05 | HN-V01–HN-V06 | N | Exercise | Multiple Competing Cues |
| HN03-06 | HN-V01–HN-V06 | N | Physiotherapy | Conversational Distractor |

## QC Checklist

- [x] Same target category within each parent family
- [x] Same hard-negative mechanism
- [x] Negative/refusal-related surface cue remains present
- [x] Target behavioral evidence remains dominant
- [x] I examples preserve postponement/uncertainty without active resistance
- [x] N examples preserve observable behavioral resistance
- [x] Negative words do not act as deterministic N cues
- [x] Contextual/pragmatic interpretation remains necessary
- [x] No reminder-configuration semantics
- [x] No sentiment-only labeling
- [x] No category drift across variants
- [x] Natural conversational wording
- [x] Parent-family lineage preserved for leakage-controlled splitting
