# HN02 — P ↔ I Hard Negatives

## Boundary

**P (Positive) ↔ I (Indifferent)**

### Construction focus

The examples contain surface cues of hesitation, uncertainty, or neutral hedging, but the true intended label is determined by whether the user actually commits to baseline compliance (P) or maintains uncommitted deferral (I).

---

## HN02-01 — Competing Keyword

**User:**
“Maybe it is a good idea, but regardless of that, I’ll put the pillbox beside my toothbrush tonight.”

**Label:** `P`

---

## HN02-02 — Competing Phrase

**User:**
“That could work, I suppose, so I’ll go ahead and take the walk after lunch today.”

**Label:** `P`

---

## HN02-03 — Misleading Opening Clause

**User:**
“I’m still thinking about the overall layout, but I will unroll the mat in the living room today.”

**Label:** `P`

---

## HN02-04 — Mid-Sentence Self-Correction

**User:**
“Sure, I can put a bottle right—wait, actually, I haven’t decided if I want water cluttering my desk today.”

**Label:** `I`

---

## HN02-05 — Multiple Competing Cues

**User:**
“I can see how that helps, and I’ll probably walk tomorrow, but I’m undecided whether I want shoes lying by the door tonight.”

**Label:** `I`

---

## HN02-06 — Conversational Distractor

**User:**
“You often recommend breaking things into parts, and I might test that out sometime, but I’m just considering it for now.”

**Label:** `I`

---

## Gold Labels

| ID | Label | Task | Distractor Pattern |
|---|---|---|---|
| HN02-01 | P | Medication | Competing Keyword |
| HN02-02 | P | Exercise | Competing Phrase |
| HN02-03 | P | Physiotherapy | Misleading Opening Clause |
| HN02-04 | I | Hydration | Mid-Sentence Self-Correction |
| HN02-05 | I | Exercise | Multiple Competing Cues |
| HN02-06 | I | Physiotherapy | Conversational Distractor |
