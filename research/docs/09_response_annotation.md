# 6. Semantic State Annotation

This section provides semantic-state-specific annotation instructions.

Each semantic state should be annotated independently using its corresponding ontology as the primary reference.

Annotators should first consult the relevant ontology definition and then follow the annotation procedure described in this section.

---

# 6.1 Response Category

## Objective

The objective of Response Category annotation is to determine **how receptive the user's response is to the conversational intervention**.

Response Category captures the overall behavioral response expressed by the user and serves as the primary semantic interface between the Dialogue Interpreter and the Reinforcement Learning policy.

---

## Reference Ontology

The formal definitions, decision boundaries, and examples are specified in:

```
01_RESPONSE_CATEGORY_ONTOLOGY.md
```

This document should be considered the authoritative reference for all Response Category annotations.

---

## Annotation Question

For every user utterance, answer the following question:

> **How receptive is the user's response to the current conversational intervention?**

Do not consider:

- conversational structure,
- persuasion barriers,
- execution status,
- future intentions,

unless they influence the user's overall behavioral response.

---

## Annotation Procedure

For each user utterance:

### Step 1

Read the complete conversational context.

Understand the recommendation or persuasive intervention immediately preceding the user's response.

---

### Step 2

Read the user's entire response before attempting classification.

Avoid assigning labels based on isolated words or phrases.

---

### Step 3

Determine the user's overall behavioral response toward the intervention.

Assign exactly one Response Category according to the ontology.

---

### Step 4

Ignore semantic information belonging to other ontologies.

For example,

- questions belong to Dialogue Purpose,
- reasons belong to Persuasion Barrier,
- execution lifecycle belongs to Execution Status.

These should not influence Response Category unless they alter the user's overall receptiveness.

---

## Annotation Rules

### Rule 1 — One Label Only

Assign exactly one Response Category.

Multi-label annotation is not permitted.

---

### Rule 2 — Annotate Behavioral Response

Focus on the user's behavioral response toward the intervention rather than the wording of the response.

---

### Rule 3 — Consider the Entire Utterance

Do not classify using only the first sentence.

Always interpret the complete response before assigning a label.

---

### Rule 4 — Prefer Dominant Interpretation

If multiple behavioral signals are present, assign the category representing the dominant overall response.

---

### Rule 5 — Do Not Infer Missing Information

Annotate only the receptiveness expressed or strongly implied by the user.

Avoid speculative interpretation.

---

## Common Annotation Mistakes

### Incorrect

```
"I'm busy today."

↓

Response Category = Time Constraint
```

Correct

```
Response Category = N (or appropriate behavioral category)

Persuasion Barrier = Time Constraint
```

---

### Incorrect

```
"Why should I do this?"

↓

Response Category = Question
```

Correct

```
Response Category = Information-seeking behavioral response

Dialogue Purpose = Question
```

(Response Category and Dialogue Purpose are independent semantic states.)

---

### Incorrect

```
"I'll do it tonight."

↓

Execution Status = Planned
```

Response Category should be determined independently from Execution Status.

---

## Ambiguous Cases

When uncertainty exists between two adjacent Response Categories:

1. Follow the formal ontology definitions.
2. Choose the simpler interpretation requiring fewer assumptions.
3. Use the dominant behavioral response expressed by the user.

---

## Final Checklist

Before finalizing the annotation, verify:

- Exactly one Response Category has been assigned.
- The label reflects behavioral receptiveness.
- The decision follows the ontology definitions.
- The label was assigned independently of the remaining semantic states.