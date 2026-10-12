# HN06 — VP ↔ N Hard Negatives

## Boundary

**VP ↔ N**

### Construction focus

The examples preserve the hard-negative mechanism while the label is determined by the user's dominant behavioral response to the task reminder, not by surface cues.

---

## HN06-01 — Competing Keyword

**User:**  
“I usually avoid clutter, but this is a brilliant idea and I’m putting the pillbox beside the mirror right away.”

**Label:** `VP`

---

## HN06-02 — Competing Phrase

**User:**  
“I don’t normally keep drinks near my laptop, but I really like this plan and I’m putting the bottle on my desk now.”

**Label:** `VP`

---

## HN06-03 — Misleading Opening Clause

**User:**  
“Doing things before breakfast isn’t my preference, but this routine is so helpful that I’m already laying the mat out for tomorrow.”

**Label:** `VP`

---

## HN06-04 — Mid-Sentence Self-Correction

**User:**  
“I’m eager to follow that plan—actually, wait, evening alarms drive me crazy; I’d rather take my medication without one.”

**Label:** `N`

---

## HN06-05 — Multiple Competing Cues

**User:**  
“That’s a creative way to build the habit, and I appreciate the thought, but drinking an extra glass whenever I make tea doesn’t work for me.”

**Label:** `N`

---

## HN06-06 — Conversational Distractor

**User:**  
“I usually enjoy taking on new routines, but splitting my physiotherapy into two sessions is too disruptive; I’d rather do one session.”

**Label:** `N`

---

## Gold Labels

| ID | Label | Task | Distractor Pattern |
|---|---|---|---|
| HN06-01 | VP | Medication | Competing Keyword |
| HN06-02 | VP | Hydration | Competing Phrase |
| HN06-03 | VP | Physiotherapy | Misleading Opening Clause |
| HN06-04 | N | Medication | Mid-Sentence Self-Correction |
| HN06-05 | N | Hydration | Multiple Competing Cues |
| HN06-06 | N | Physiotherapy | Conversational Distractor |
