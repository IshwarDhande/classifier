# HN10 — I ↔ VN Hard Negatives

## Boundary

**I (Indifferent) ↔ VN (Very Negative)**

### Construction focus

The examples contain surface cues that mimic either neutral ambivalence or hostile confrontation, but the true intended label is determined by whether the user's communicative stance remains genuinely open and uncommitted (I) or explicitly terminates the interaction and rejects the domain topic (VN).

---

## HN10-01 — Competing Keyword

**User:**
“Stop assuming that’s the only option; it might work, but I’m still considering whether I want to keep the medication there.”

**Label:** `I`

---

## HN10-02 — Competing Phrase

**User:**
“I’m sick of hearing people give hydration advice, but a bottle on the desk is a possibility; I’ll see later.”

**Label:** `I`

---

## HN10-03 — Misleading Opening Clause

**User:**
“Leave me out of your fitness programs; going for a walk is something I might do, but I haven’t decided yet.”

**Label:** `I`

---

## HN10-04 — Mid-Sentence Self-Correction

**User:**
“I might consider taking the medication later—actually, you know what, absolutely not. Stop meddling with my medication and leave me alone.”

**Label:** `VN`

---

## HN10-05 — Multiple Competing Cues

**User:**
“Maybe drinking more water helps people, maybe it doesn’t, but I don’t care. Stop lecturing me about hydration, I am done discussing this.”

**Label:** `VN`

---

## HN10-06 — Conversational Distractor

**User:**
“You bring up walking every single day. I told you before to stop telling me what to wear or do; drop the subject.”

**Label:** `VN`

---

## Gold Labels

| ID | Label | Task | Distractor Pattern |
|---|---|---|---|
| HN10-01 | I | Medication | Competing Keyword |
| HN10-02 | I | Hydration | Competing Phrase |
| HN10-03 | I | Exercise | Misleading Opening Clause |
| HN10-04 | VN | Medication | Mid-Sentence Self-Correction |
| HN10-05 | VN | Hydration | Multiple Competing Cues |
| HN10-06 | VN | Exercise | Conversational Distractor |
