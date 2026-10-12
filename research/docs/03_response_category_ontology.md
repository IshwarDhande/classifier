# Response Category Ontology
**Version:** 1.0 (Frozen)

---

# Executive Summary

This document specifies the **Response Category Ontology (RCO)**, the semantic representation used to model a user's immediate behavioral reaction to a persuasive intervention.

The Response Category Ontology is one of the four semantic dimensions within the **Dialogue Interpreter** and serves as the only semantic state directly shared between the reinforcement learning simulator and the production conversational AI system.

Unlike sentiment analysis or intent classification, the ontology represents the user's **latent behavioral appraisal** of the intervention, enabling the production system to estimate the same response variable used by the simulator.

Consequently, no semantic translation is required between simulation and deployment.

---

# 1. Motivation

## 1.1 Problem Statement

The reinforcement learning simulator models user reactions using an ordinal response variable

\[
R_t \in \{VN, N, I, P, VP\}
\]

During deployment, however, this variable is not directly observable.

Instead, the conversational agent receives only natural language user responses.

Therefore, a semantic ontology is required that enables the Dialogue Interpreter to infer the user's behavioral response from conversational evidence while preserving compatibility with the simulator.

---

## 1.2 Role in the Production Architecture

The Response Category Ontology bridges natural language understanding and reinforcement learning.

```
User Utterance
        │
        ▼
Structured Understanding Model
        │
        ▼
Response Category
        │
        ▼
RL State Update
```

Unlike the remaining semantic attributes, the Response Category is consumed directly by the reinforcement learning framework.

---

# 2. Design Objectives

The ontology is designed to satisfy the following objectives.

- Preserve complete compatibility with the validated simulator.
- Represent the user's behavioral appraisal of the intervention.
- Maintain an ordinal semantic structure.
- Remain independent of sentiment, emotion, and dialogue purposes.
- Provide a reproducible semantic target for supervised learning.

---

# 3. Formal Definition

## Definition

A **Response Category** represents the user's immediate behavioral appraisal of the conversational intervention, reflecting the degree of behavioral acceptance or resistance expressed toward the recommendation.

The Response Category captures **how the user reacted to the intervention**, rather than whether the requested task was completed.

---

## Mathematical Definition

For each conversational turn,

\[
R_t \in
\{
VN,\;
N,\;
I,\;
P,\;
VP
\}
\]

where

- **VN** – Very Negative
- **N** – Negative
- **I** – Indifferent
- **P** – Positive
- **VP** – Very Positive

These categories form an ordinal behavioral scale.

\[
VN < N < I < P < VP
\]

Increasing values correspond to increasingly favorable behavioral reactions toward the intervention.

---

# 4. Behavioral Interpretation

The ontology models the user's behavioral response to the intervention rather than lexical polarity or emotional expression.

| Response | Behavioral Interpretation |
|----------|----------------------------|
| VP | Strong acceptance with enthusiasm and appreciation |
| P | Acceptance and willingness to cooperate |
| I | Behavioral neutrality without commitment or resistance |
| N | Mild behavioral resistance or reluctance |
| VN | Strong rejection, hostility, or reactance |

The ontology therefore represents **behavioral orientation toward the intervention**, not emotional state.

---

# 5. Relationship to the Simulator

The Response Category Ontology is reused directly from the simulator.

```
Simulator

User Response
      │
      ▼
 VP ← P ← I → N → VN

==============================

Production

User Utterance
      │
      ▼
Structured Understanding Model
      │
      ▼
Response Category
```

The production system estimates the same latent behavioral variable used by the simulator.

No semantic conversion is performed.

---

# 6. Relationship to Other Semantic Dimensions

The Response Category is one of four orthogonal semantic dimensions within the Dialogue Interpreter.

| Semantic Dimension | Question Answered |
|--------------------|-------------------|
| Response Category | How did the user react to the intervention? |
| Dialogue Purpose | What conversational function is being performed? |
| Persuasion Barrier | Why is the user not adhering? |
| Execution Status | What is the current execution state of the task? |

Each semantic dimension captures a distinct aspect of the user's response and should be predicted independently.

---

# 7. Ontology Structure

```
Very Positive (VP)
        │
        ▼
 Positive (P)
        │
        ▼
Indifferent (I)
        │
        ▼
 Negative (N)
        │
        ▼
Very Negative (VN)
```

This ordering represents increasing behavioral acceptance from bottom to top.

---

# 8. Semantic Characteristics

The ontology captures behavioral evidence rather than surface wording.

Classification should prioritize:

1. Behavioral commitment
2. Behavioral resistance
3. Enthusiasm
4. Hostility
5. Pragmatic interpretation
6. Surface lexical content

Natural language realization alone is insufficient for determining the response category.

---

# 9. Scope

The ontology represents:

- acceptance
- cooperation
- resistance
- appreciation
- hostility
- behavioral engagement

These constructs are interpreted with respect to the conversational intervention.

---

# 10. Out of Scope

The Response Category does **not** represent:

- sentiment
- emotion
- personality
- persuasion barrier
- dialogue purpose
- task completion
- task success
- reward
- future adherence
- user preference

These constructs are modeled by separate components within the production architecture.

---

# 11. Relationship to Task Completion

Task completion and Response Category are intentionally independent.

Let

\[
Y_t \in \{0,1\}
\]

denote task completion.

Then

\[
Y_t \not\Rightarrow R_t
\]

Similarly,

\[
R_t \not\Rightarrow Y_t
\]

Examples

| Situation | Completion | Response |
|-----------|------------|----------|
| Completes task enthusiastically | Yes | VP |
| Completes task reluctantly | Yes | N |
| Ignores recommendation | No | I |
| Rejects recommendation angrily | No | VN |

Behavioral reaction and task completion therefore represent different latent variables.

---

# 12. Downstream Consumer

The primary consumer of the Response Category is the reinforcement learning framework.

```
User Utterance
        │
        ▼
Structured Understanding Model
        │
        ▼
Response Category
        │
        ▼
RL State Update
```

The Response Category updates the estimated interaction state while preserving compatibility with the simulator formulation.

---

# 13. Design Principles

The ontology follows the following principles.

### Principle 1 — Behavioral Interpretation

The ontology models behavioral response rather than lexical sentiment.

---

### Principle 2 — Ordinal Semantics

The five categories represent ordered behavioral states rather than independent classes.

---

### Principle 3 — Simulator Compatibility

The production ontology must preserve the semantics of the simulator without modification.

---

### Principle 4 — Orthogonality

Response Category is independent of the remaining semantic dimensions.

---

### Principle 5 — Context-Aware Interpretation

Dialogue context may resolve ambiguity, but the category should always describe the current user response.

---

# 14. Quality Criteria

A valid Response Category Ontology should satisfy the following properties.

- Behavioral interpretability
- Ordinal consistency
- Simulator compatibility
- Mutual exclusivity
- Annotation reproducibility
- Context sensitivity
- Independence from other semantic attributes

---

# 15. Interface Specification

## Input

```
Conversation Context

+

Current User Utterance
```

---

## Output

```yaml
response_category:

allowed_values:
  - VP
  - P
  - I
  - N
  - VN
```

---

# 16. Current Design Status

| Component | Status |
|-----------|--------|
| Five response categories | FROZEN |
| Ordinal semantics | FROZEN |
| Behavioral interpretation | FROZEN |
| Simulator compatibility | FROZEN |
| Production interface | FROZEN |

---

# Summary

The Response Category Ontology provides a structured semantic representation of the user's immediate behavioral appraisal of a conversational intervention. By preserving the simulator's validated ordinal response variable without modification, the ontology establishes a direct semantic bridge between natural language understanding and reinforcement learning. This shared representation enables consistent behavior modeling across both simulation and real-world deployment while maintaining architectural simplicity and semantic integrity.