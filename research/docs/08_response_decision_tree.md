# Semantic Ontology Specification
# 06_RESPONSE_DECISION_TREE

**Document Status:** Draft v1.0 (Proposed Stable)  
**Ontology Component:** User Response Classification  
**Applies To:** `VN`, `N`, `I`, `P`, `VP`

---

# 1. Purpose

This document defines a deterministic decision procedure for mapping natural language user responses to the simulator's ordinal behavioral response variable.

The objective is to maximize annotation consistency, reduce ambiguity, and provide a reproducible protocol for manual annotation, simulator implementation, and future LLM-based classifiers.

---

# 2. Fundamental Principle

The response categories represent **latent behavioral states**, not lexical patterns.

Classification precedence:

1. Observed behavioral commitment
2. Behavioral resistance
3. Communicative intention
4. Pragmatic meaning
5. Surface wording

Keyword matching alone must never determine the final label.

---

# 3. Ordinal Response Scale

```text
VN  <  N  <  I  <  P  <  VP
```

Moving right indicates:

- greater acceptance
- lower resistance
- higher engagement
- stronger receptiveness

---

# 4. Primary Decision Tree

```text
START
│
├── Is there clear behavioral acceptance?
│       │
│       ├── YES
│       │      │
│       │      ├── Strong enthusiasm / appreciation / proactive engagement?
│       │      │          │
│       │      │          ├── YES → VP
│       │      │          └── NO  → P
│       │
│       └── NO
│
├── Is there behavioral resistance?
│       │
│       ├── YES
│       │      │
│       │      ├── Hostility / explicit rejection / strong reactance?
│       │      │          │
│       │      │          ├── YES → VN
│       │      │          └── NO  → N
│       │
│       └── NO
│
└── I
```

---

# 5. Secondary Tie-Breaking Rules

Apply these rules when multiple categories appear plausible.

## Rule 1 — Behavior Dominates Emotion

Example:

> "I'm annoyed, but I'll do it."

Behavioral commitment dominates.

→ **P**

---

## Rule 2 — Rejection Dominates Gratitude

Example:

> "Thanks, but I'm not doing it."

Behavioral rejection dominates.

→ **N** or **VN** depending on hostility.

---

## Rule 3 — Hostility Escalates

Any explicit hostility toward the agent or intervention moves the label toward **VN**.

---

## Rule 4 — Enthusiasm Escalates

Acceptance combined with appreciation and proactive engagement moves the label toward **VP**.

---

## Rule 5 — Lack of Evidence Defaults to Neutral

When neither acceptance nor resistance is supported by sufficient evidence:

→ **I**

---

# 6. Category Boundary Summary

| Boundary | Distinguishing Feature |
|----------|------------------------|
| VP vs P | Enthusiasm and appreciation |
| P vs I | Behavioral commitment |
| I vs N | Behavioral resistance |
| N vs VN | Hostility and strong reactance |

---

# 7. Handling Difficult Cases

## Mixed Intent

Determine the dominant behavioral state.

Example:

> "I'll do it, but stop reminding me."

Commitment exists with mild irritation.

→ Generally **P**.

---

## Contradictory Statements

Behavior outweighs wording.

Example:

> "I appreciate it but I refuse."

→ **N** or **VN**.

---

## Sarcasm

Interpret using dialogue history and pragmatic intent.

Never classify solely from literal wording.

---

## Silence

Silence is not acceptance.

If no behavioral evidence exists and a label is required:

→ **I**

---

## Uncertainty

Example:

> "Maybe."

Use surrounding dialogue.

Without commitment:

→ **I**

With avoidance:

→ **N**

---

# 8. Multi-turn Decision Policy

The current simulator labels the **current response**.

Previous turns may be used only to interpret ambiguity, not to replace the current behavioral evidence.

Example:

Turn 1:
> "No."

Turn 2:
> "Okay, I'll do it."

Current label:

→ **P**

not **N**.

---

# 9. Annotation Checklist

Before assigning a label, annotators should answer:

1. Was the recommendation accepted?
2. Was it rejected?
3. Is there behavioral commitment?
4. Is there resistance?
5. Is hostility present?
6. Is appreciation present?
7. Is enthusiasm present?

---

# 10. Category Selection Matrix

| Acceptance | Resistance | Enthusiasm | Hostility | Label |
|-----------:|-----------:|-----------:|-----------:|:------|
| High | Low | High | None | VP |
| High | Low | Low–Moderate | None | P |
| Low | Low | Low | None | I |
| Low | Moderate | None | Low | N |
| None | High | None | High | VN |

---

# 11. Implementation Notes

For simulator implementation:

- Perform behavioral inference before category assignment.
- Preserve the ordinal semantics of the five response classes.
- Do not classify using sentiment alone.
- Use dialogue context only for ambiguity resolution.

---

# 12. Notes for Future LLM Classifier

The classifier should estimate latent variables such as:

- behavioral commitment
- resistance
- appreciation
- reactance
- engagement

The predicted response category should be derived from these inferred variables rather than directly from lexical features.

---

# Current Category

**Cross-Category Response Decision Tree**

---

# Decisions Locked

- Behavior has higher priority than wording.
- Acceptance and resistance are the primary branching variables.
- Enthusiasm separates P from VP.
- Hostility separates N from VN.
- Neutral evidence defaults to I.




