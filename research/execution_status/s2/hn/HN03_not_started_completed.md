# Stage 2C — Hard Negatives
## HN03: Not Started ↔ Completed

### 1. Boundary Definition

**Boundary ID:** B03  
**State A:** Not Started  
**State B:** Completed

This hard-negative resource targets the boundary between **no execution having begun** and **execution having finished**.

The purpose is to construct utterances containing plausible competing surface cues that could cause a classifier to rely on shortcuts rather than on actual execution evidence.

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

For B03, the decisive question remains:

> **Is there evidence that the target task has been executed to completion, or has execution not begun?**

The following surface cues must not override the actual execution evidence:

- future-oriented wording;
- preparation language;
- temporal expressions;
- conversational framing;
- statements about what should happen;
- reasons for non-execution;
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

#### HN03-01 — Competing Temporal Cue

**Hard-Negative Type:** Competing temporal cue  
**Target Task:** Medication  
**Execution Status:** Not Started

> I was meant to take the medication earlier, but I haven't started it.

**Misleading cue:** “earlier” creates an expectation that execution should already have occurred.

**Decisive evidence:** “I haven't started it” establishes that execution has not begun.

---

#### HN03-02 — Competing Execution-Status Phrase

**Hard-Negative Type:** Competing execution-status phrase  
**Target Task:** Exercise  
**Execution Status:** Completed

> I didn't finish the last exercise separately, but I completed the full exercise routine.

**Misleading cue:** “didn't finish” can suggest non-completion.

**Decisive evidence:** “I completed the full exercise routine” establishes that the target task is finished.

---

#### HN03-03 — Misleading Opening Clause

**Hard-Negative Type:** Misleading opening clause  
**Target Task:** Physiotherapy  
**Execution Status:** Completed

> I'm ready for another session, but I already completed today's physiotherapy routine.

**Misleading cue:** “I'm ready for another session” can be interpreted as indicating that the current task has not been completed.

**Decisive evidence:** “I already completed today's physiotherapy routine” establishes completion of the target task.

---

#### HN03-04 — Self-Correction

**Hard-Negative Type:** Self-correction  
**Target Task:** Hydration  
**Execution Status:** Completed

> I haven't had the water yet—sorry, I mean the second bottle; I already finished the one for this task.

**Misleading cue:** The initial statement suggests no execution.

**Decisive evidence:** The correction identifies the relevant target and establishes that its execution is complete.

---

#### HN03-05 — Multiple Competing Cues

**Hard-Negative Type:** Multiple competing cues  
**Target Task:** Exercise  
**Execution Status:** Not Started

> I was supposed to exercise earlier, got the mat ready, and even planned the first set, but I haven't actually done any of it.

**Misleading cues:** temporal expectation, preparation, and planning all resemble task engagement.

**Decisive evidence:** “I haven't actually done any of it” establishes absence of execution.

---

#### HN03-06 — Strong Conversational Distractor

**Hard-Negative Type:** Strong conversational distractor  
**Target Task:** Physiotherapy  
**Execution Status:** Completed

> I need to rest after all that effort, and I'm already thinking about tomorrow's routine; today's physiotherapy routine is completely done.

**Misleading cues:** physical effort and discussion of a future routine can distract from the current execution state.

**Decisive evidence:** “today's physiotherapy routine is completely done” establishes completed execution.

### 4. Production Records

```yaml
- example_id: HN03-01
  pair_id: HN03
  parent_id: null
  lineage_id: HN03-01
  execution_status: Not Started
  semantic_subtype: hard_negative
  stage: 2C
  resource_type: hard_negative
  boundary_id: B03
  anchor_type: null
  context: "Medication execution has not begun despite a temporal cue suggesting it should have occurred earlier."
  utterance: "I was meant to take the medication earlier, but I haven't started it."
  target_task: medication
  closest_competing_state: Completed
  variation_type: competing_temporal_cue
  hard_negative_type: competing_temporal_cue
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: HN03-02
  pair_id: HN03
  parent_id: null
  lineage_id: HN03-02
  execution_status: Completed
  semantic_subtype: hard_negative
  stage: 2C
  resource_type: hard_negative
  boundary_id: B03
  anchor_type: null
  context: "The complete exercise routine has been executed despite a phrase describing one component as unfinished."
  utterance: "I didn't finish the last exercise separately, but I completed the full exercise routine."
  target_task: exercise
  closest_competing_state: Not Started
  variation_type: competing_execution_status_phrase
  hard_negative_type: competing_execution_status_phrase
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: HN03-03
  pair_id: HN03
  parent_id: null
  lineage_id: HN03-03
  execution_status: Completed
  semantic_subtype: hard_negative
  stage: 2C
  resource_type: hard_negative
  boundary_id: B03
  anchor_type: null
  context: "Today's physiotherapy routine has finished despite an opening statement about readiness for a future session."
  utterance: "I'm ready for another session, but I already completed today's physiotherapy routine."
  target_task: physiotherapy
  closest_competing_state: Not Started
  variation_type: misleading_opening_clause
  hard_negative_type: misleading_opening_clause
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: HN03-04
  pair_id: HN03
  parent_id: null
  lineage_id: HN03-04
  execution_status: Completed
  semantic_subtype: hard_negative
  stage: 2C
  resource_type: hard_negative
  boundary_id: B03
  anchor_type: null
  context: "The target hydration task is complete; a self-correction distinguishes it from another bottle."
  utterance: "I haven't had the water yet—sorry, I mean the second bottle; I already finished the one for this task."
  target_task: hydration
  closest_competing_state: Not Started
  variation_type: self_correction
  hard_negative_type: self_correction
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: HN03-05
  pair_id: HN03
  parent_id: null
  lineage_id: HN03-05
  execution_status: Not Started
  semantic_subtype: hard_negative
  stage: 2C
  resource_type: hard_negative
  boundary_id: B03
  anchor_type: null
  context: "Exercise preparation and planning occurred, but no actual execution occurred."
  utterance: "I was supposed to exercise earlier, got the mat ready, and even planned the first set, but I haven't actually done any of it."
  target_task: exercise
  closest_competing_state: Completed
  variation_type: multiple_competing_cues
  hard_negative_type: multiple_competing_cues
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: HN03-06
  pair_id: HN03
  parent_id: null
  lineage_id: HN03-06
  execution_status: Completed
  semantic_subtype: hard_negative
  stage: 2C
  resource_type: hard_negative
  boundary_id: B03
  anchor_type: null
  context: "Today's physiotherapy routine is complete despite distractors about fatigue and a future routine."
  utterance: "I need to rest after all that effort, and I'm already thinking about tomorrow's routine; today's physiotherapy routine is completely done."
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
| HN03-01 | Temporal expectation | Execution has not started |
| HN03-02 | Non-completion of one component | Complete target routine is explicitly finished |
| HN03-03 | Future-session readiness | Today's target routine is explicitly complete |
| HN03-04 | Initial non-execution statement | Self-correction establishes completed target execution |
| HN03-05 | Timing, preparation, and planning | No actual execution occurred |
| HN03-06 | Fatigue and future-task discussion | Today's target routine is explicitly complete |

The examples are designed to prevent classification from relying on preparation, intention, temporal cues, isolated non-completion phrases, or unrelated conversational content.

### 6. Hard-Negative Validation Criteria

A candidate is valid only if:

1. The target task is identifiable.
2. The target execution status is semantically clear from the complete utterance.
3. A genuine competing cue is present.
4. The competing cue is plausible enough to create a classification challenge.
5. The competing cue does not actually change the target execution state.
6. The decisive execution evidence remains present.
7. Not Started examples contain no evidence of begun execution.
8. Completed examples contain evidence that the target execution has finished.
9. Preparation is not treated as execution.
10. Future intention is not treated as execution.
11. A statement about one component must not override completion evidence for the explicitly defined target task.
12. The example does not depend on motivation, persuasion barriers, dialogue purpose, or sentiment.
13. The example does not require external task-manager reasoning.
14. The utterance remains natural conversational language.
15. The hard negative does not become genuinely ambiguous.

### 7. Boundary Invariant

For HN03:

> **Competing surface cues must not override direct evidence distinguishing no begun execution from finished execution.**

The classifier must identify whether the target task has actually been executed to completion. Preparation, intention, temporal expectations, future tasks, partial component statements, and conversational distractors must not be mistaken for the target execution state.
