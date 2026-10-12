# HN09 — P ↔ VN Hard Negatives

## Boundary

**P ↔ VN**

### Construction focus

The examples preserve the hard-negative mechanism while the label is determined by the user's dominant behavioral response to the task reminder, not by surface cues.

---

## HN09-01 — Competing Keyword

**User:**  
“I’ve never liked keeping pills by my bed, but alright, I’ll put the pillbox beside the clock.”

**Label:** `P`

---

## HN09-02 — Competing Phrase

**User:**  
“I really dislike desk clutter, but okay, I’ll keep a water bottle there today.”

**Label:** `P`

---

## HN09-03 — Misleading Opening Clause

**User:**  
“I’m not planning to make this a big routine, but yes, I’ll take the fifteen-minute walk after dinner.”

**Label:** `P`

---

## HN09-04 — Mid-Sentence Self-Correction

**User:**  
“Sure, that sounds convenient—actually, no. Stop telling me how to organize my medication; I’m sick of these suggestions.”

**Label:** `VN`

---

## HN09-05 — Multiple Competing Cues

**User:**  
“I know you’re trying to help with hydration, but stop pushing drinking reminders; I don’t want to be micromanaged.”

**Label:** `VN`

---

## HN09-06 — Conversational Distractor

**User:**  
“Every time we talk you bring up physiotherapy. I’m done discussing it, so drop the subject.”

**Label:** `VN`

---

## Gold Labels

| ID | Label | Task | Distractor Pattern |
|---|---|---|---|
| HN09-01 | P | Medication | Competing Keyword |
| HN09-02 | P | Hydration | Competing Phrase |
| HN09-03 | P | Exercise | Misleading Opening Clause |
| HN09-04 | VN | Medication | Mid-Sentence Self-Correction |
| HN09-05 | VN | Hydration | Multiple Competing Cues |
| HN09-06 | VN | Physiotherapy | Conversational Distractor |
