# HN05 — VP ↔ I Hard Negatives

## Boundary

**VP (Very Positive) ↔ I (Indifferent)**

### Construction focus

The examples contain surface cues that suggest either non-committal hesitation or eagerness, but the true intended label is determined by whether the user demonstrates active, proactive behavioral agency (VP) or uncommitted postponement (I).

---

## HN05-01 — Competing Keyword

**User:**
“Maybe someone else would hesitate, but I’m thrilled with this idea and I’m setting the medication beside my breakfast bowl right now.”

**Label:** `VP`

---

## HN05-02 — Competing Phrase

**User:**
“It’s one possibility among many, sure, but honestly I’m super excited about it and I’m lacing up my shoes now.”

**Label:** `VP`

---

## HN05-03 — Misleading Opening Clause

**User:**
“I haven’t really decided on the room layout, but I absolutely love the physiotherapy routine and I’m unrolling the mat immediately.”

**Label:** `VP`

---

## HN05-04 — Mid-Sentence Self-Correction

**User:**
“I’ll take the evening medication immediately tonight—actually, hold on, I haven’t decided whether taking it at that time works for me.”

**Label:** `I`

---

## HN05-05 — Multiple Competing Cues

**User:**
“That sounds like a fantastic strategy on paper, but realistically I’m still weighing whether I want a water bottle on my desk today.”

**Label:** `I`

---

## HN05-06 — Conversational Distractor

**User:**
“You always encourage me to be proactive about physiotherapy, and two sessions could work, but I’m going to think about it before committing.”

**Label:** `I`

---

## Gold Labels

| ID | Label | Task | Distractor Pattern |
|---|---|---|---|
| HN05-01 | VP | Medication | Competing Keyword |
| HN05-02 | VP | Exercise | Competing Phrase |
| HN05-03 | VP | Physiotherapy | Misleading Opening Clause |
| HN05-04 | I | Medication | Mid-Sentence Self-Correction |
| HN05-05 | I | Hydration | Multiple Competing Cues |
| HN05-06 | I | Physiotherapy | Conversational Distractor |
