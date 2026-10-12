# HN04 — N ↔ VN Hard Negatives

## Boundary

**N (Negative) ↔ VN (Very Negative)**

### Construction focus

The examples contain intense emotion or surface politeness, but the true intended label is determined by whether the resistance is recoverable with openness to alternative arrangements (N) versus unrecoverable autonomy shutdown and topic rejection (VN).

---

## HN04-01 — Competing Keyword

**User:**
“I reacted strongly because I hate morning routines, but I just prefer taking my medication at night instead.”

**Label:** `N`

---

## HN04-02 — Competing Phrase

**User:**
“I want nothing to do with going outside right now, though I’m fine doing some light stretching indoors later.”

**Label:** `N`

---

## HN04-03 — Misleading Opening Clause

**User:**
“Stop telling me what to do with my mat; I’m just not in the mood for physiotherapy right now, let’s talk later.”

**Label:** `N`

---

## HN04-04 — Mid-Sentence Self-Correction

**User:**
“I might look for a bottle later—actually, you know what, forget it. Stop monitoring my water intake, I’m completely sick of this topic.”

**Label:** `VN`

---

## HN04-05 — Multiple Competing Cues

**User:**
“I appreciate you think you’re being helpful, but seriously, leave me alone about exercise shoes and don’t bring this up again.”

**Label:** `VN`

---

## HN04-06 — Conversational Distractor

**User:**
“Every single day it’s another rehab suggestion. I am completely done discussing physiotherapy with you, so drop it.”

**Label:** `VN`

---

## Gold Labels

| ID | Label | Task | Distractor Pattern |
|---|---|---|---|
| HN04-01 | N | Medication | Competing Keyword |
| HN04-02 | N | Exercise | Competing Phrase |
| HN04-03 | N | Physiotherapy | Misleading Opening Clause |
| HN04-04 | VN | Hydration | Mid-Sentence Self-Correction |
| HN04-05 | VN | Exercise | Multiple Competing Cues |
| HN04-06 | VN | Physiotherapy | Conversational Distractor |
