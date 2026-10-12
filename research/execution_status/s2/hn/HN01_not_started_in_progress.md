# Stage 2C — Hard Negatives
## HN01: Not Started ↔ In Progress

### 1. Boundary Definition

**Boundary ID:** B01  
**State A:** Not Started  
**State B:** In Progress

This hard-negative resource targets the boundary between **no execution having begun** and **execution having begun but remaining unfinished**.

The purpose is to construct utterances containing a plausible competing surface cue that could cause a classifier to rely on a shortcut rather than on the actual execution evidence.

The target state must remain determinable from the complete utterance.

### 2. Hard-Negative Construction Principle

A valid hard negative contains:

```text
Target execution state
        +
misleading competing surface cue
        +
sufficient execution evidence
        ↓
correct state remains recoverable
```

For B01, the decisive question remains:

> **Has execution actually begun?**

The following surface cues must not override the execution evidence:

- future-oriented wording;
- preparation language;
- temporal expressions;
- conversational framing;
- statements about what will happen next;
- indirect contextual information.

### 3. Hard-Negative Mechanisms

The six examples below cover the six Stage 2C hard-negative mechanisms:

1. Competing temporal cue
2. Competing execution-status phrase
3. Misleading opening clause
4. Self-correction
5. Multiple competing cues
6. Strong conversational distractor

---

#### HN01-01 — Competing Temporal Cue

**Hard-Negative Type:** Competing temporal cue  
**Target Task:** Medication  
**Execution Status:** Not Started

> I was supposed to take the medication earlier, but I still haven't started taking it.

**Misleading cue:** “earlier” may suggest that execution should already have occurred.

**Decisive evidence:** “I still haven't started taking it” establishes that execution has not begun.

---

#### HN01-02 — Competing Execution-Status Phrase

**Hard-Negative Type:** Competing execution-status phrase  
**Target Task:** Exercise  
**Execution Status:** In Progress

> I haven't finished the exercises yet because I'm still doing them.

**Misleading cue:** “haven't finished” can be incorrectly associated with Not Started.

**Decisive evidence:** “I'm still doing them” establishes that execution has begun and remains unfinished.

---

#### HN01-03 — Misleading Opening Clause

**Hard-Negative Type:** Misleading opening clause  
**Target Task:** Physiotherapy  
**Execution Status:** Not Started

> I'm ready to do the physiotherapy routine, but I haven't started it yet.

**Misleading cue:** “I'm ready to do” can resemble active execution.

**Decisive evidence:** “I haven't started it yet” establishes no begun execution.

---

#### HN01-04 — Self-Correction

**Hard-Negative Type:** Self-correction  
**Target Task:** Hydration  
**Execution Status:** In Progress

> I haven't started drinking it—actually, I have; I'm halfway through the bottle.

**Misleading cue:** The initial “I haven't started” statement points toward Not Started.

**Decisive evidence:** The self-correction establishes that execution has begun and is currently unfinished.

---

#### HN01-05 — Multiple Competing Cues

**Hard-Negative Type:** Multiple competing cues  
**Target Task:** Exercise  
**Execution Status:** Not Started

> I was getting ready earlier and even laid out the mat, but I still haven't begun the exercises.

**Misleading cues:** “earlier,” “getting ready,” and “laid out the mat” all provide execution-adjacent information.

**Decisive evidence:** “I still haven't begun the exercises” establishes that execution has not started.

---

#### HN01-06 — Strong Conversational Distractor

**Hard-Negative Type:** Strong conversational distractor  
**Target Task:** Physiotherapy  
**Execution Status:** In Progress

> The routine is taking longer than I expected, and I need to get through it before I can relax; I'm still working through the exercises.

**Misleading cue:** The statement focuses strongly on duration and what must happen afterward.

**Decisive evidence:** “I'm still working through the exercises” establishes that execution has begun and remains unfinished.

### 4. Production Records

```yaml
- example_id: HN01-01
  pair_id: HN01
  parent_id: null
  lineage_id: HN01-01
  execution_status: Not Started
  semantic_subtype: hard_negative
  stage: 2C
  resource_type: hard_negative
  boundary_id: B01
  anchor_type: null
  context: "Medication execution has not begun despite a temporal cue suggesting it should have occurred earlier."
  utterance: "I was supposed to take the medication earlier, but I still haven't started taking it."
  target_task: medication
  closest_competing_state: In Progress
  variation_type: competing_temporal_cue
  hard_negative_type: competing_temporal_cue
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: HN01-02
  pair_id: HN01
  parent_id: null
  lineage_id: HN01-02
  execution_status: In Progress
  semantic_subtype: hard_negative
  stage: 2C
  resource_type: hard_negative
  boundary_id: B01
  anchor_type: null
  context: "Exercise execution is underway but unfinished."
  utterance: "I haven't finished the exercises yet because I'm still doing them."
  target_task: exercise
  closest_competing_state: Not Started
  variation_type: competing_execution_status_phrase
  hard_negative_type: competing_execution_status_phrase
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: HN01-03
  pair_id: HN01
  parent_id: null
  lineage_id: HN01-03
  execution_status: Not Started
  semantic_subtype: hard_negative
  stage: 2C
  resource_type: hard_negative
  boundary_id: B01
  anchor_type: null
  context: "Physiotherapy preparation is complete but execution has not begun."
  utterance: "I'm ready to do the physiotherapy routine, but I haven't started it yet."
  target_task: physiotherapy
  closest_competing_state: In Progress
  variation_type: misleading_opening_clause
  hard_negative_type: misleading_opening_clause
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: HN01-04
  pair_id: HN01
  parent_id: null
  lineage_id: HN01-04
  execution_status: In Progress
  semantic_subtype: hard_negative
  stage: 2C
  resource_type: hard_negative
  boundary_id: B01
  anchor_type: null
  context: "Hydration execution has begun and is halfway complete; the utterance contains a self-correction."
  utterance: "I haven't started drinking it—actually, I have; I'm halfway through the bottle."
  target_task: hydration
  closest_competing_state: Not Started
  variation_type: self_correction
  hard_negative_type: self_correction
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: HN01-05
  pair_id: HN01
  parent_id: null
  lineage_id: HN01-05
  execution_status: Not Started
  semantic_subtype: hard_negative
  stage: 2C
  resource_type: hard_negative
  boundary_id: B01
  anchor_type: null
  context: "Exercise preparation occurred earlier, but actual execution has not begun."
  utterance: "I was getting ready earlier and even laid out the mat, but I still haven't begun the exercises."
  target_task: exercise
  closest_competing_state: In Progress
  variation_type: multiple_competing_cues
  hard_negative_type: multiple_competing_cues
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: HN01-06
  pair_id: HN01
  parent_id: null
  lineage_id: HN01-06
  execution_status: In Progress
  semantic_subtype: hard_negative
  stage: 2C
  resource_type: hard_negative
  boundary_id: B01
  anchor_type: null
  context: "Physiotherapy execution is underway but remains unfinished, while the utterance contains a strong distractor about duration and a subsequent obligation."
  utterance: "The routine is taking longer than I expected, and I need to get through it before I can relax; I'm still working through the exercises."
  target_task: physiotherapy
  closest_competing_state: Not Started
  variation_type: strong_conversational_distractor
  hard_negative_type: strong_conversational_distractor
  source: constructed
  validation_status: candidate
  ambiguity_flag: false
```

### 5. Hard-Negative Diagnostic Rationale

| Example | Competing cue | Decisive execution evidence |
|---|---|---|
| HN01-01 | Temporal expectation | Execution has not started |
| HN01-02 | “Haven't finished” | Execution is currently occurring |
| HN01-03 | Readiness/preparation | Execution has not started |
| HN01-04 | Initial contradictory statement | Self-correction establishes active execution |
| HN01-05 | Preparation plus temporal cue | Actual exercise execution has not begun |
| HN01-06 | Duration and post-task distractor | Execution is currently underway |

The examples are designed so that a classifier cannot reliably determine the state from a single lexical or surface cue. The complete utterance must be interpreted to identify the decisive execution evidence.

### 6. Hard-Negative Validation Criteria

A candidate is valid only if:

1. The target task is identifiable.
2. The target execution status is semantically clear after considering the complete utterance.
3. A genuine competing cue is present.
4. The competing cue is plausible enough to create a classification challenge.
5. The competing cue does not actually change the execution state.
6. The decisive execution evidence remains present.
7. The Not Started examples contain no actual execution evidence.
8. The In Progress examples contain evidence that execution has begun and remains unfinished.
9. The example does not depend on motivation, persuasion barriers, dialogue purpose, or sentiment.
10. The example does not require external task-manager reasoning.
11. The utterance remains natural conversational language.
12. The hard negative does not become ambiguous merely because the distractor is present.

### 7. Boundary Invariant

For HN01:

> **Competing surface cues must not override direct evidence about execution initiation.**

The classifier must identify whether execution has actually begun. Preparation, temporal expectations, incomplete-status wording, conversational framing, and other distractors are secondary unless they directly establish the execution state.
