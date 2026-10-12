# Stage 1 — Behavioral Semantic Dimensions

**File:** `01_behavioral_semantic_dimensions.md`  
**Stage:** Stage 1 — Semantic Coverage  
**Phase:** Phase 1 — Behavioral Semantic Dimensions  
**Ontology:** Response Category Ontology V1.0  
**Response Categories:** `VP`, `P`, `I`, `N`, `VN`

---

## 1. Purpose

This document defines the **behavioral semantic dimensions** that organize the semantic space of the five Response Categories.

The purpose is not to create classifier labels or semantic subtypes yet.

Instead, this phase answers:

> **What meaningful behavioral dimensions vary within each Response Category, and along which dimensions can semantically distinct response situations be constructed?**

These dimensions will be used in Phase 2 to derive the **Semantic Subtype Catalogue**, and in Phase 3 to construct the **Semantic Scenario Inventory**.

---

## 2. Frozen Response Category Semantics

The five Response Categories are:

| ID | Category | Core behavioral meaning |
|---|---|---|
| `VP` | Very Positive | Strong acceptance, appreciation, enthusiasm, high engagement |
| `P` | Positive | Acceptance, cooperation, willingness, low resistance |
| `I` | Indifferent | Neutral/non-committal engagement; insufficient evidence of acceptance or resistance |
| `N` | Negative | Reluctance, resistance, disagreement, mild reactance |
| `VN` | Very Negative | Strong rejection, hostility, high reactance, active disengagement |

The ordinal structure is:

```text
VN < N < I < P < VP
```

Response Category concerns the user's **immediate behavioral appraisal/reaction toward the intervention**.

It must remain distinct from:

- sentiment polarity;
- emotion;
- Dialogue Purpose;
- Persuasion Barrier;
- Execution Status;
- task completion;
- topic;
- personality;
- isolated lexical cues.

---

# 3. Cross-Category Behavioral Dimensions

The following dimensions provide the common semantic coordinate system for Stage 1.

These are **construction dimensions**, not labels.

## 3.1 Acceptance / Rejection Orientation

### Definition

The degree to which the user behaviorally accepts, tolerates, resists, or rejects the intervention.

### Semantic range

```text
Strong rejection
      ↓
Resistance / reluctance
      ↓
No clear acceptance or rejection
      ↓
Acceptance / cooperation
      ↓
Strong acceptance
```

### Relevance

This is the primary behavioral dimension underlying the ordinal response scale.

It helps distinguish:

- `VN` from `N`;
- `N` from `I`;
- `I` from `P`;
- `P` from `VP`.

---

## 3.2 Behavioral Commitment

### Definition

The degree to which the user's response provides evidence of willingness or intention to cooperate with the intervention.

### Possible regions

```text
No commitment
Weak / ambiguous commitment
Conditional commitment
Clear commitment
Strong / proactive commitment
```

### Relevance

Particularly important for:

- `I ↔ P`;
- `P` scenarios;
- distinguishing genuine acceptance from acknowledgement.

A statement can be positive in wording without providing behavioral commitment.

---

## 3.3 Resistance

### Definition

The degree to which the user behaviorally resists the intervention.

### Possible regions

```text
No observable resistance
Weak reluctance
Moderate resistance
Strong resistance
Active rejection / reactance
```

### Relevance

Particularly important for:

- `I ↔ N`;
- `N ↔ VN`.

Resistance must be interpreted behaviorally rather than inferred from negative emotion alone.

---

## 3.4 Engagement

### Definition

The degree to which the user actively engages with the intervention beyond merely acknowledging it.

### Possible regions

```text
Minimal engagement
Passive engagement
Ordinary engagement
Active engagement
Proactive engagement
```

### Relevance

Higher engagement can support `VP`, while weak or absent engagement may support `I`.

Engagement alone must not override stronger evidence of resistance or commitment.

---

## 3.5 Enthusiasm / Appreciation

### Definition

The degree to which the user expresses strong positive appraisal, appreciation, or enthusiasm toward the intervention.

### Possible regions

```text
Absent
Mild
Clear
Strong
Highly enthusiastic / appreciative
```

### Relevance

This is especially important for the:

```text
VP ↔ P
```

boundary.

Ordinary acceptance does not automatically become `VP`; stronger enthusiasm, appreciation, or high engagement is required.

---

## 3.6 Reactance / Opposition

### Definition

The degree to which the user actively pushes back against the intervention, the agent's persistence, or future interaction.

### Possible regions

```text
Absent
Mild pushback
Clear opposition
Strong reactance
Active interaction rejection
```

### Relevance

This is especially important for:

```text
N ↔ VN
```

and for scenarios involving:

- repeated reminders;
- requests to stop;
- rejection of future assistance;
- interaction termination.

---

## 3.7 Cooperation

### Definition

The degree to which the user demonstrates willingness to work with the intervention or agent.

### Possible regions

```text
Non-cooperation
Reluctant cooperation
Neutral / unclear cooperation
Ordinary cooperation
Proactive cooperation
```

### Relevance

Cooperation is central to distinguishing:

- `P` from `I`;
- `VP` from `P`.

Cooperation should be interpreted from behavior and communicative meaning rather than politeness alone.

---

## 3.8 Temporal Commitment / Immediacy

### Definition

The temporal orientation of the user's behavioral response toward acting on the intervention.

### Possible regions

```text
No indicated action
Indefinite / unclear
Delayed consideration
Future commitment
Near-term commitment
Immediate / voluntary action
```

### Relevance

Temporal orientation can differentiate semantically distinct acceptance situations.

However, delayed action does not automatically imply `I` or `N`, and immediate action does not automatically imply `VP`.

The underlying behavioral appraisal remains primary.

---

## 3.9 Explicitness of Behavioral Signal

### Definition

How directly the user's behavioral reaction is expressed.

### Possible regions

```text
Highly implicit
Indirect
Conversationally implied
Explicit
Strongly explicit
```

### Relevance

The same behavioral situation may be realized explicitly or implicitly.

This dimension is particularly useful for:

- scenario construction;
- linguistic expansion;
- preventing lexical shortcuts.

Explicitness must not itself determine the Response Category.

---

## 3.10 Behavioral Evidence Strength

### Definition

How strongly the available conversational evidence supports a particular behavioral interpretation.

### Possible regions

```text
Very weak / insufficient
Weak
Moderate
Clear
Very strong
```

### Relevance

This dimension is critical for `I`.

`I` is not simply "neutral language." It often represents a case where the available behavioral evidence is insufficient to establish clear acceptance or resistance.

---

## 3.11 Politeness / Social Softening

### Definition

The degree to which social conventions soften or mask the user's underlying behavioral response.

### Possible regions

```text
Absent
Low
Moderate
Strong
Highly conventional / indirect
```

### Relevance

Politeness can coexist with different Response Categories.

Examples of possible patterns include:

```text
Polite + accepting
Polite + uncertain
Polite + resistant
Polite + strongly rejecting
```

Therefore politeness is a **semantic variation dimension**, not a category signal.

---

## 3.12 Mixed Acceptance–Resistance Structure

### Definition

Whether the utterance contains both acceptance/cooperation and resistance signals.

### Possible regions

```text
Pure acceptance
Mostly acceptance
Mixed
Mostly resistance
Pure resistance
```

### Relevance

Mixed responses are important because the ontology requires exactly one primary Response Category.

The dominant behavioral outcome must determine the category.

Examples from the ontology's decision logic include cases where:

- resistance is present but behavioral commitment dominates;
- appreciation is present but rejection dominates;
- cooperation is expressed alongside annoyance.

---

# 4. Category-Specific Behavioral Dimensions

The common dimensions above should be interpreted differently across the five categories.

---

## 4.1 VP — Very Positive

The semantic space of `VP` should emphasize:

### A. Strength of Acceptance

How strongly the user accepts the intervention.

```text
clear acceptance
→ strong acceptance
→ enthusiastic acceptance
```

### B. Enthusiasm

Degree of positive engagement beyond ordinary cooperation.

```text
ordinary
→ clearly enthusiastic
→ strongly enthusiastic
```

### C. Appreciation

Degree to which the intervention is explicitly valued or appreciated.

```text
none
→ mild appreciation
→ strong appreciation
```

### D. Proactive Engagement

Degree to which the user goes beyond minimal compliance.

```text
accepts
→ engages
→ voluntarily extends interaction
→ proactively seeks further engagement
```

### E. Immediate / Voluntary Cooperation

Degree to which cooperation is spontaneous, immediate, or voluntarily expressed.

### Core diagnostic relationship

```text
Acceptance + strong positive engagement
                ↓
               VP
```

Acceptance alone should remain available to `P`.

---

## 4.2 P — Positive

The semantic space of `P` should emphasize:

### A. Ordinary Acceptance

Straightforward acceptance without strong enthusiasm.

### B. Cooperation

Willingness to cooperate with the intervention.

### C. Behavioral Commitment

Evidence that the user genuinely intends to follow through.

### D. Qualified Acceptance

Acceptance that contains conditions or mild qualifications without becoming dominant resistance.

### E. Delayed Genuine Acceptance

Acceptance where action is postponed but willingness remains genuine.

### F. Low Resistance

Acceptance/cooperation remains behaviorally dominant despite minor hesitation or annoyance.

### Core diagnostic relationship

```text
Acceptance + cooperation + low resistance
                ↓
                P
```

The absence of strong enthusiasm keeps many genuine acceptance cases within `P` rather than `VP`.

---

## 4.3 I — Indifferent

The semantic space of `I` should emphasize:

### A. Neutral Acknowledgement

The user acknowledges the intervention without establishing acceptance or rejection.

### B. Uncertainty

The user's behavioral position remains unclear.

### C. Non-Commitment

The user does not provide sufficient evidence of willingness to cooperate.

### D. Delayed Decision

The user postpones a decision without clearly resisting.

### E. Weak Engagement

The user responds minimally without clear positive or negative behavioral direction.

### F. Clarification Without Acceptance

The user seeks or provides information without establishing cooperation.

### G. Insufficient Behavioral Evidence

The available response does not support a stronger acceptance or resistance interpretation.

### Core diagnostic relationship

```text
No clear acceptance
        +
No clear resistance
        +
Insufficient behavioral evidence
                ↓
                I
```

`I` must not become a generic label for all ambiguous or short utterances. Context should be used where available.

---

## 4.4 N — Negative

The semantic space of `N` should emphasize:

### A. Reluctance

The user shows reduced willingness without strong rejection.

### B. Mild Refusal

The user declines or resists in a recoverable manner.

### C. Disagreement

The user disagrees with the intervention without strong reactance.

### D. Behavioral Resistance

The user pushes against the intervention.

### E. Conditional Resistance

The user resists under current conditions while leaving room for cooperation.

### F. Passive Resistance

Resistance is expressed indirectly or without active confrontation.

### G. Reduced Cooperation

The user's willingness to cooperate is meaningfully reduced.

### Core diagnostic relationship

```text
Behavioral resistance
        +
Recoverable interaction
        +
No strong hostility / reactance
                ↓
                N
```

---

## 4.5 VN — Very Negative

The semantic space of `VN` should emphasize:

### A. Strong Rejection

Explicit and strong refusal of the intervention.

### B. Strong Opposition

Active opposition to the recommendation or intervention.

### C. Hostility

Strongly negative interactional response directed toward the intervention or agent.

### D. High Reactance

Strong pushback against being persuaded, reminded, or influenced.

### E. Active Disengagement

The user attempts to terminate or withdraw from the interaction.

### F. Rejection of Future Assistance

The user explicitly rejects continued intervention or assistance.

### G. Interaction Termination

The response indicates a strong desire to end the interaction.

### Core diagnostic relationship

```text
Strong rejection / reactance
        +
High resistance or disengagement
                ↓
               VN
```

---

# 5. Boundary-Critical Dimensions

Not every dimension contributes equally to every decision boundary.

The following dimensions should receive priority during scenario construction.

| Boundary | Primary dimensions |
|---|---|
| `VP ↔ P` | Enthusiasm, appreciation, engagement, strength of acceptance |
| `P ↔ I` | Behavioral commitment, cooperation, acceptance, evidence strength |
| `I ↔ N` | Resistance, reluctance, disagreement, evidence strength |
| `N ↔ VN` | Reactance, opposition, hostility, disengagement, rejection strength |

The central principle is:

> **Boundary distinctions must be expressed through behavioral evidence, not merely positive or negative wording.**

---

# 6. Orthogonality Requirements

The behavioral dimensions must not collapse into other Dialogue Interpreter dimensions.

## 6.1 Response Category ≠ Emotion

```text
Happy ≠ automatically VP
Angry ≠ automatically VN
```

Emotion may contribute evidence, but the target is the behavioral reaction toward the intervention.

## 6.2 Response Category ≠ Dialogue Purpose

A user can perform the same dialogue purpose with different behavioral reactions.

## 6.3 Response Category ≠ Persuasion Barrier

The reason a user struggles with adherence is distinct from how the user reacts to the intervention.

## 6.4 Response Category ≠ Execution Status

Whether the task has been completed is distinct from the user's immediate reaction.

## 6.5 Response Category ≠ Task Completion

A user may:

- react positively but fail to complete the task;
- react negatively but later complete the task.

Therefore completion must not be used as a semantic shortcut.

---

# 7. Construction Rules for Phase 2

Phase 2 should use these dimensions to derive semantic subtypes.

### Rule 1 — Dimensions are not labels

Do not turn dimensions directly into classifier categories.

### Rule 2 — Subtypes must represent semantic regions

A subtype should correspond to a coherent combination of behavioral properties.

### Rule 3 — Multiple dimensions may define one subtype

For example, a meaningful semantic region may involve:

```text
acceptance
+
commitment
+
low resistance
```

rather than one isolated dimension.

### Rule 4 — Dimensions may overlap

The same dimension can contribute to multiple subtypes.

### Rule 5 — Category boundaries must remain visible

Subtype construction must preserve the distinction between:

```text
VP ↔ P
P  ↔ I
I  ↔ N
N  ↔ VN
```

### Rule 6 — Do not force equal subtype counts

The semantic richness of each category determines the number of subtypes.

### Rule 7 — Avoid lexical definitions

A subtype must never be defined by words such as:

```text
"thanks"
"okay"
"no"
"maybe"
"absolutely"
```

Those are possible realizations, not semantic definitions.

### Rule 8 — Behavior dominates surface form

Subtype definitions must be expressed in behavioral terms.

---

# 8. Phase-1 Output

This document provides the behavioral dimensions that will be used for Phase 2.

Phase 1 does **not** freeze:

- semantic subtype names;
- subtype counts;
- semantic scenarios;
- linguistic realizations.

Those decisions belong to subsequent phases.

The next step is:

```text
Phase 1 — Behavioral Semantic Dimensions
                ↓
        HUMAN REVIEW / FREEZE
                ↓
Phase 2 — Semantic Subtype Catalogue
```

---


