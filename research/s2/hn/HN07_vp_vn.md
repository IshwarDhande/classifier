# HN07 — VP ↔ VN Hard Negatives

## Boundary

**VP ↔ VN**

### Construction focus

The examples preserve the hard-negative mechanism while the label is determined by the user's dominant behavioral response to the task reminder, not by surface cues.

---

## HN07-01 — Competing Keyword

**User:**  
“I never expected to like this idea, but it’s fantastic and I’m putting the medication dispenser beside the coffee maker right now.”

**Label:** `VP`

---

## HN07-02 — Competing Phrase

**User:**  
“I absolutely dislike clutter around my workspace, but this idea is a game changer and I’m filling the bottle right now.”

**Label:** `VP`

---

## HN07-03 — Misleading Opening Clause

**User:**  
“Stop right there—that is actually a brilliant suggestion, and I’m putting on my shoes to take the walk now.”

**Label:** `VP`

---

## HN07-04 — Mid-Sentence Self-Correction

**User:**  
“I’ll organize my medication that way today—no, what am I saying? Stop telling me how to manage it; I’m completely fed up with these suggestions.”

**Label:** `VN`

---

## HN07-05 — Multiple Competing Cues

**User:**  
“I know you’re trying to help, but stop pushing me about getting ready for walks; leave me alone about it.”

**Label:** `VN`

---

## HN07-06 — Conversational Distractor

**User:**  
“We’ve had good conversations before, but I’m done discussing my physiotherapy. Drop the subject.”

**Label:** `VN`

---

## Gold Labels

| ID | Label | Task | Distractor Pattern |
|---|---|---|---|
| HN07-01 | VP | Medication | Competing Keyword |
| HN07-02 | VP | Hydration | Competing Phrase |
| HN07-03 | VP | Exercise | Misleading Opening Clause |
| HN07-04 | VN | Medication | Mid-Sentence Self-Correction |
| HN07-05 | VN | Exercise | Multiple Competing Cues |
| HN07-06 | VN | Physiotherapy | Conversational Distractor |
