# HN01 — VP ↔ P Hard Negatives

## Boundary

**VP (Very Positive) ↔ P (Positive)**

### Construction focus

The examples contain surface cues that could suggest the competing category, but the true intended label is determined by the user's degree of behavioral engagement and proactive agency versus routine compliance.

---

## HN01-01 — Competing Keyword

**User:**
“Okay is enough to describe the idea, but I’m genuinely excited to set this bottle up right now and drink regularly.”

**Label:** `VP`

---

## HN01-02 — Competing Phrase

**User:**
“I’ll do it, though I wouldn’t call it a simple routine chore; I’m really looking forward to getting outside and starting today.”

**Label:** `VP`

---

## HN01-03 — Misleading Opening Clause

**User:**
“It’s nothing special at first glance, but I actually love this approach and I’m laying the mat out right now.”

**Label:** `VP`

---

## HN01-04 — Mid-Sentence Self-Correction

**User:**
“I was going to set up a whole tracking log for every glass—actually, never mind that, I’ll just drink the water after each meal.”

**Label:** `P`

---

## HN01-05 — Multiple Competing Cues

**User:**
“That sounds like a wonderful habit and I really appreciate the helpful thought, but simply put, yes, I’ll leave them by the door.”

**Label:** `P`

---

## HN01-06 — Conversational Distractor

**User:**
“You always come up with these ambitious habit changes, but for this one, sure, I’ll do the two short sessions today.”

**Label:** `P`

---

## Gold Labels

| ID | Label | Task | Distractor Pattern |
|---|---|---|---|
| HN01-01 | VP | Hydration | Competing Keyword |
| HN01-02 | VP | Exercise | Competing Phrase |
| HN01-03 | VP | Physiotherapy | Misleading Opening Clause |
| HN01-04 | P | Hydration | Mid-Sentence Self-Correction |
| HN01-05 | P | Exercise | Multiple Competing Cues |
| HN01-06 | P | Physiotherapy | Conversational Distractor |
