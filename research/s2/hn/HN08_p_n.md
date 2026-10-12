# HN08 — P ↔ N Hard Negatives

## Boundary

**P ↔ N**

### Construction focus

The examples preserve the hard-negative mechanism while the label is determined by the user's dominant behavioral response to the task reminder, not by surface cues.

---

## HN08-01 — Competing Keyword

**User:**  
“I dislike changing where I keep things, but fine, I’ll put my medication beside the breakfast plate.”

**Label:** `P`

---

## HN08-02 — Competing Phrase

**User:**  
“I don’t really feel like doing that, though sure, I’ll keep a water bottle on my desk today.”

**Label:** `P`

---

## HN08-03 — Misleading Opening Clause

**User:**  
“The living room is a bit tight, but I can make it work and do the physiotherapy exercises there.”

**Label:** `P`

---

## HN08-04 — Mid-Sentence Self-Correction

**User:**  
“Okay, I’ll follow that schedule—actually, no, evenings don’t work for me; I’d rather take my medication on my own schedule.”

**Label:** `N`

---

## HN08-05 — Multiple Competing Cues

**User:**  
“I understand why you suggest it and I do want to stay hydrated, but tying the water to lunch doesn’t suit me, so I’ll skip that.”

**Label:** `N`

---

## HN08-06 — Conversational Distractor

**User:**  
“I usually appreciate getting outside, but today the walk doesn’t work for me; I’d rather stay in.”

**Label:** `N`

---

## Gold Labels

| ID | Label | Task | Distractor Pattern |
|---|---|---|---|
| HN08-01 | P | Medication | Competing Keyword |
| HN08-02 | P | Hydration | Competing Phrase |
| HN08-03 | P | Physiotherapy | Misleading Opening Clause |
| HN08-04 | N | Medication | Mid-Sentence Self-Correction |
| HN08-05 | N | Hydration | Multiple Competing Cues |
| HN08-06 | N | Exercise | Conversational Distractor |
