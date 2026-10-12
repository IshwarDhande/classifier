# HN03 — I ↔ N Hard Negatives

## Boundary

**I (Indifferent) ↔ N (Negative)**

### Construction focus

The examples contain negative-sounding idioms or refusal-related cues, but the true intended label is determined by whether the user maintains uncommitted postponement (I) versus active behavioral resistance (N).

---

## HN03-01 — Competing Keyword

**User:**
“I’m not against taking the medication, but I’m still deciding whether this timing makes sense for my schedule.”

**Label:** `I`

---

## HN03-02 — Competing Phrase

**User:**
“I wouldn’t say I dislike walking, but I’m just weighing whether after lunch fits into my plans today.”

**Label:** `I`

---

## HN03-03 — Misleading Opening Clause

**User:**
“The hallway is somewhat narrow, though I haven’t ruled out doing the physiotherapy there; I’ll see later.”

**Label:** `I`

---

## HN03-04 — Mid-Sentence Self-Correction

**User:**
“A bottle on the desk might be fine—no, actually, I’d rather keep my desk clear and grab water from the kitchen instead.”

**Label:** `N`

---

## HN03-05 — Multiple Competing Cues

**User:**
“I know it’s a sensible routine and I’m still thinking about fitness overall, but I really don’t want to leave my walking shoes by the door today.”

**Label:** `N`

---

## HN03-06 — Conversational Distractor

**User:**
“We’ve discussed breaking sessions up before, but having two separate interruptions doesn’t suit me; I’d rather do my physiotherapy all at once.”

**Label:** `N`

---

## Gold Labels

| ID | Label | Task | Distractor Pattern |
|---|---|---|---|
| HN03-01 | I | Medication | Competing Keyword |
| HN03-02 | I | Exercise | Competing Phrase |
| HN03-03 | I | Physiotherapy | Misleading Opening Clause |
| HN03-04 | N | Hydration | Mid-Sentence Self-Correction |
| HN03-05 | N | Exercise | Multiple Competing Cues |
| HN03-06 | N | Physiotherapy | Conversational Distractor |
