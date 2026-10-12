# HN05 — VP ↔ I Hard Negative Variants

## Boundary

**VP (Very Positive) ↔ I (Indifferent)**

## Construction Focus

The examples contain surface cues that suggest either non-committal hesitation or eagerness, but the true intended label is determined by whether the user demonstrates active, proactive behavioral agency (`VP`) or uncommitted postponement (`I`).

The expansion preserves the original hard-negative mechanisms while varying the misleading surface realization. The decisive evidence remains proactive behavioral engagement versus insufficient behavioral commitment.

## Variant Construction Rules

- Preserve the original target category for each parent.
- Preserve the VP ↔ I boundary.
- Preserve the original hard-negative mechanism.
- Preserve the task and conversational situation.
- For `VP`, retain strong enthusiasm together with active/proactive behavioral agency.
- For `I`, retain consideration, uncertainty, or postponement without sufficient behavioral commitment.
- Do not let enthusiasm words alone determine `VP`.
- Do not let uncertainty words alone determine `I`.
- The preceding task reminder/intervention is implicit; only the user response is represented.

---

## HN05-01 — VP

**Parent:** HN05-01  
**Task:** Medication  
**Hard-negative mechanism:** Competing Keyword  
**Gold label:** `VP`

### HN05-01-V01 — LEX
- **Lineage:** HN05-01 → HN05-01-V01

**User:**  
“Maybe someone else would hesitate, but I’m delighted with this idea and I’m putting the medication beside my breakfast bowl right now.”

**Label:** `VP`

### HN05-01-V02 — NAT
- **Lineage:** HN05-01 → HN05-01-V02

**User:**  
“Some people might hesitate, but I’m genuinely excited about this and I’m setting the medication beside my breakfast bowl now.”

**Label:** `VP`

### HN05-01-V03 — EXP
- **Lineage:** HN05-01 → HN05-01-V03

**User:**  
“Maybe hesitation would make sense for someone else, but I’m genuinely excited about the idea and I’m already putting the medication beside my breakfast bowl.”

**Label:** `VP`

### HN05-01-V04 — DSC
- **Lineage:** HN05-01 → HN05-01-V04

**User:**  
“I’m setting the medication beside my breakfast bowl right now. Maybe someone else would hesitate, but I’m thrilled with the idea.”

**Label:** `VP`

### HN05-01-V05 — PRG
- **Lineage:** HN05-01 → HN05-01-V05

**User:**  
“Whether someone else might hesitate isn’t how I feel about it—I’m genuinely excited and I’m already setting the medication beside my breakfast bowl.”

**Label:** `VP`

### HN05-01-V06 — CMK
- **Lineage:** HN05-01 → HN05-01-V06

**User:**  
“Maybe, sure, someone else would hesitate—but I’m actually thrilled about it and I’m putting the medication beside my breakfast bowl now.”

**Label:** `VP`

---

## HN05-02 — VP

**Parent:** HN05-02  
**Task:** Exercise  
**Hard-negative mechanism:** Competing Phrase  
**Gold label:** `VP`

### HN05-02-V01 — LEX
- **Lineage:** HN05-02 → HN05-02-V01

**User:**  
“It’s one option among several, sure, but honestly I’m really excited about it and I’m lacing up my shoes now.”

**Label:** `VP`

### HN05-02-V02 — NAT
- **Lineage:** HN05-02 → HN05-02-V02

**User:**  
“It’s just one possibility, I know, but I’m genuinely excited about it and I’m already putting my shoes on.”

**Label:** `VP`

### HN05-02-V03 — EXP
- **Lineage:** HN05-02 → HN05-02-V03

**User:**  
“It may be one possibility among many, but that doesn’t capture my reaction—I’m very excited about it and I’m lacing up my shoes right now.”

**Label:** `VP`

### HN05-02-V04 — DSC
- **Lineage:** HN05-02 → HN05-02-V04

**User:**  
“I’m lacing up my shoes now because I’m genuinely excited to do it. It’s one possibility among many, sure, but I’m going ahead.”

**Label:** `VP`

### HN05-02-V05 — PRG
- **Lineage:** HN05-02 → HN05-02-V05

**User:**  
“Calling it just one possibility understates my response—I’m excited about it and I’m already getting ready to exercise.”

**Label:** `VP`

### HN05-02-V06 — CMK
- **Lineage:** HN05-02 → HN05-02-V06

**User:**  
“Sure, it’s one option—but honestly, I’m super excited about it. I’m putting my shoes on now.”

**Label:** `VP`

---

## HN05-03 — VP

**Parent:** HN05-03  
**Task:** Physiotherapy  
**Hard-negative mechanism:** Misleading Opening Clause  
**Gold label:** `VP`

### HN05-03-V01 — LEX
- **Lineage:** HN05-03 → HN05-03-V01

**User:**  
“I haven’t settled on the room layout, but I absolutely love the physiotherapy routine and I’m unrolling the mat right away.”

**Label:** `VP`

### HN05-03-V02 — NAT
- **Lineage:** HN05-03 → HN05-03-V02

**User:**  
“I’m still figuring out where everything should go, but I really love this physiotherapy routine and I’m getting the mat out now.”

**Label:** `VP`

### HN05-03-V03 — EXP
- **Lineage:** HN05-03 → HN05-03-V03

**User:**  
“The room setup is still undecided, but my reaction to the routine is clear—I absolutely love it and I’m already unrolling the mat.”

**Label:** `VP`

### HN05-03-V04 — DSC
- **Lineage:** HN05-03 → HN05-03-V04

**User:**  
“I absolutely love the physiotherapy routine and I’m unrolling the mat immediately. I haven’t decided on the room layout yet, but that doesn’t change my enthusiasm.”

**Label:** `VP`

### HN05-03-V05 — PRG
- **Lineage:** HN05-03 → HN05-03-V05

**User:**  
“The room layout can be figured out later; what matters is that I love this routine and I’m already getting the mat ready.”

**Label:** `VP`

### HN05-03-V06 — CMK
- **Lineage:** HN05-03 → HN05-03-V06

**User:**  
“Hmm, I’m still working out the room layout, but I absolutely love the routine. I’m unrolling the mat now.”

**Label:** `VP`

---

## HN05-04 — I

**Parent:** HN05-04  
**Task:** Medication  
**Hard-negative mechanism:** Mid-Sentence Self-Correction  
**Gold label:** `I`

### HN05-04-V01 — LEX
- **Lineage:** HN05-04 → HN05-04-V01

**User:**  
“I’ll take the evening medication right away tonight—actually, hold on, I haven’t decided whether that timing works for me.”

**Label:** `I`

### HN05-04-V02 — NAT
- **Lineage:** HN05-04 → HN05-04-V02

**User:**  
“I was about to say I’d take the evening medication tonight, but wait, I’m still not sure that timing works for me.”

**Label:** `I`

### HN05-04-V03 — EXP
- **Lineage:** HN05-04 → HN05-04-V03

**User:**  
“I started to commit to taking the medication tonight, but I need to correct that—I haven’t decided whether that time works for me yet.”

**Label:** `I`

### HN05-04-V04 — DSC
- **Lineage:** HN05-04 → HN05-04-V04

**User:**  
“I haven’t decided whether taking it at that time works for me. I was going to say I’d take the evening medication immediately, but actually, I’m still considering it.”

**Label:** `I`

### HN05-04-V05 — PRG
- **Lineage:** HN05-04 → HN05-04-V05

**User:**  
“The initial ‘I’ll take it tonight’ was premature—I’m still deciding whether that timing works for me.”

**Label:** `I`

### HN05-04-V06 — CMK
- **Lineage:** HN05-04 → HN05-04-V06

**User:**  
“Sure, I’ll take it tonight—wait, actually, maybe not. I haven’t decided if that timing works for me.”

**Label:** `I`

---

## HN05-05 — I

**Parent:** HN05-05  
**Task:** Hydration  
**Hard-negative mechanism:** Multiple Competing Cues  
**Gold label:** `I`

### HN05-05-V01 — LEX
- **Lineage:** HN05-05 → HN05-05-V01

**User:**  
“Your strategy makes a lot of sense in theory, though I'm still deciding if I'll actually keep a water bottle on my desk today.”

**Label:** `I`

### HN05-05-V02 — NAT
- **Lineage:** HN05-05 → HN05-05-V02

**User:**  
“It sounds great in theory, but I’m honestly still deciding whether I want a water bottle sitting on my desk today.”

**Label:** `I`

### HN05-05-V03 — EXP
- **Lineage:** HN05-05 → HN05-05-V03

**User:**  
“I can see why the strategy sounds fantastic, but that doesn’t mean I’ve decided to use it—I’m still considering whether I want the bottle on my desk today.”

**Label:** `I`

### HN05-05-V04 — DSC
- **Lineage:** HN05-05 → HN05-05-V04

**User:**  
“I’m still weighing whether I want a water bottle on my desk today. The strategy sounds fantastic on paper, but I haven’t decided to do it.”

**Label:** `I`

### HN05-05-V05 — PRG
- **Lineage:** HN05-05 → HN05-05-V05

**User:**  
“The idea may sound fantastic, but my current position is still undecided—I’m considering whether to keep a water bottle on my desk today.”

**Label:** `I`

### HN05-05-V06 — CMK
- **Lineage:** HN05-05 → HN05-05-V06

**User:**  
“Yeah, it sounds great, but honestly, I’m still thinking about whether I want the water bottle on my desk today.”

**Label:** `I`

---

## HN05-06 — I

**Parent:** HN05-06  
**Task:** Physiotherapy  
**Hard-negative mechanism:** Conversational Distractor  
**Gold label:** `I`

### HN05-06-V01 — LEX
- **Lineage:** HN05-06 → HN05-06-V01

**User:**  
“I appreciate your constant encouragement regarding my physical therapy, which is why I'm contemplating doing two sessions.”

**Label:** `I`

### HN05-06-V02 — NAT
- **Lineage:** HN05-06 → HN05-06-V02

**User:**  
“You’re always encouraging me to stay proactive with physiotherapy, and two sessions might be workable, but I want to think it over before I commit.”

**Label:** `I`

### HN05-06-V03 — EXP
- **Lineage:** HN05-06 → HN05-06-V03

**User:**  
“I know you usually encourage a proactive approach to physiotherapy, and I can see that two sessions could work, but I haven’t decided to commit yet.”

**Label:** `I`

### HN05-06-V04 — DSC
- **Lineage:** HN05-06 → HN05-06-V04

**User:**  
“I’m going to think about it before committing. You always encourage me to be proactive about physiotherapy, and two sessions could work.”

**Label:** `I`

### HN05-06-V05 — PRG
- **Lineage:** HN05-06 → HN05-06-V05

**User:**  
“Your encouragement to be proactive is noted, and two sessions are possible, but I’m still considering the idea rather than committing to it.”

**Label:** `I`

### HN05-06-V06 — CMK
- **Lineage:** HN05-06 → HN05-06-V06

**User:**  
“Right, you’re always telling me to be proactive, and maybe two sessions could work. I’m going to think about it before committing.”

**Label:** `I`

---

## Gold Labels

| ID | Variant | Label | Task | Distractor Pattern |
|---|---|---|---|---|
| HN05-01 | HN-V01–HN-V06 | VP | Medication | Competing Keyword |
| HN05-02 | HN-V01–HN-V06 | VP | Exercise | Competing Phrase |
| HN05-03 | HN-V01–HN-V06 | VP | Physiotherapy | Misleading Opening Clause |
| HN05-04 | HN-V01–HN-V06 | I | Medication | Mid-Sentence Self-Correction |
| HN05-05 | HN-V01–HN-V06 | I | Hydration | Multiple Competing Cues |
| HN05-06 | HN-V01–HN-V06 | I | Physiotherapy | Conversational Distractor |

## QC Checklist

- [x] Same target category within each parent family
- [x] Same hard-negative mechanism
- [x] Competing surface cue remains present
- [x] Target behavioral evidence remains dominant
- [x] VP examples preserve strong enthusiasm plus proactive behavioral agency
- [x] I examples preserve postponement/consideration without sufficient commitment
- [x] Enthusiasm words do not act as deterministic VP cues
- [x] Hesitation words do not act as deterministic I cues
- [x] Self-correction preserves the final behavioral state
- [x] No reminder-configuration semantics
- [x] No sentiment-only labeling
- [x] No category drift across variants
- [x] Natural conversational wording
- [x] Parent-family lineage preserved for leakage-controlled splitting
