<!--
FILE: research/simulator/semantic_ontology/understanding/response/RESPONSE_REFERENCE_VALUES.md
-->

# Response Understanding Ontology
# 
RESPONSE_REFERENCE_VALUES

**Document Status:** Reference v1.0  
**Ontology Component:** Dialogue Understanding  
**Purpose:** Central reference for all user response semantics used throughout the simulator.

---

# 1. Purpose

This document provides a single reference for every user response category used by the simulator.

It summarizes:

- semantic meaning;
- behavioral interpretation;
- latent appraisal interpretation;
- dialogue understanding meaning;
- downstream simulator effects.

This document should be treated as the canonical reference by:

- dialogue understanding
- response classification
- state transition implementation
- simulator development
- evaluation

---

# 2. Response Hierarchy

The simulator defines five ordered response categories.

```text
Very Positive
        │
        ▼
 Positive
        │
        ▼
Indifferent
        │
        ▼
 Negative
        │
        ▼
Very Negative
```

Mathematically,

$$
VN < N < I < P < VP
$$

These categories represent increasing favorability of the user's reaction toward the intervention.

---

# 3. Response Summary

| Response | Symbol | Behavioral Interpretation |
|-----------|--------|---------------------------|
| Very Positive | VP | Strong appreciation and highly favorable reaction |
| Positive | P | Accepts intervention positively |
| Indifferent | I | Neutral reaction with little affective response |
| Negative | N | Mild annoyance or dissatisfaction |
| Very Negative | VN | Strong rejection or highly unfavorable reaction |

---

# 4. Simulator Meaning

Responses describe

> **how the user reacted to the intervention.**

Responses do **not** directly represent:

- task completion;
- adherence;
- future compliance;
- reward.

They capture the immediate behavioral appraisal of the intervention itself.

---

# 5. Relationship to Task Completion

Task completion is

$$
Y_t\in\{0,1\}
$$

User response is

$$
R_t\in\{VN,N,I,P,VP\}
$$

These variables are intentionally independent.

Examples:

| Situation | Completion | Response |
|-----------|------------|----------|
| Task completed happily | 1 | VP |
| Task completed reluctantly | 1 | N |
| Task ignored without annoyance | 0 | I |
| Task rejected angrily | 0 | VN |

Therefore,

$$
Y_t \not\Rightarrow R_t
$$

and

$$
R_t \not\Rightarrow Y_t.
$$

---

# 6. Latent Appraisal Interpretation

Responses are generated from the latent appraisal score

$$
z
=
2Y
-
F
-
1.5X
-
0.5\hat{k}
$$

where

- \(Y\): task completion
- \(F\): fatigue
- \(X\): excess intervention
- \(\hat{k}\): normalized repetition count

Higher values of \(z\) increase the probability of positive responses.

Lower values increase the probability of negative responses.

---

# 7. Typical Appraisal Region

Although responses are sampled probabilistically, the latent appraisal generally follows:

| Latent Appraisal | Likely Response |
|-----------------:|----------------|
| Very High | VP |
| High | P |
| Near Zero | I |
| Low | N |
| Very Low | VN |

These are qualitative reference regions.

---

# 8. Response Generation Pipeline

```text
Action
    │
    ▼
Task Completion
    │
    ▼
Latent Appraisal
    │
    ▼
Ordinal Logistic Mapping
    │
    ▼
Response Distribution
    │
    ▼
Sampled Response
```

Dialogue Understanding predicts the observed response category.

The simulator then updates downstream latent variables.

---

# 9. Downstream Simulator Effects

The sampled response contributes to:

- fatigue dynamics;
- tolerance updates;
- future persuasion effectiveness;
- long-term interaction history.

Responses do **not** directly consume persuasion budget.

---

# 10. Dialogue Understanding Meaning

| Response | Dialogue Interpretation |
|-----------|------------------------|
| VP | Highly appreciative |
| P | Cooperative |
| I | Neutral |
| N | Mild dissatisfaction |
| VN | Strong dissatisfaction |

These are semantic interpretations only.

---

# 11. Evaluation Reference

Every classified response should preserve

✓ semantic meaning

✓ ordinal ordering

✓ behavioral interpretation

✓ consistency with dialogue context

✓ consistency with simulator formulation

---

# 12. Current Design Status

| Component | Status |
|-----------|--------|
| Five response categories | FROZEN |
| Ordered response semantics | FROZEN |
| Ordinal logistic mapping | FROZEN |
| Latent appraisal architecture | FROZEN |
| Initial coefficients | REFERENCE |
| Threshold values | REFERENCE |
| Behavioral interpretation | STABLE |

---

# 13. Important Distinctions

User response is different from

- task completion
- task success probability
- intervention intensity
- persuasion cost
- reward
- task criticality

These constructs intentionally remain independent.

---

# 14. Reference Summary

Whenever an implementation requires

- response semantics,
- response ordering,
- behavioral interpretation,
- simulator meaning,
- dialogue understanding labels,

this document should be used as the primary reference before consulting the individual response specifications.