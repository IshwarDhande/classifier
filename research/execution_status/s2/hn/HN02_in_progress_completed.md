# Stage 2C — Hard Negatives
## HN02: In Progress ↔ Completed

### 1. Boundary Definition

**Boundary ID:** B02  
**State A:** In Progress  
**State B:** Completed

This hard-negative resource targets the boundary between **execution that has begun but remains unfinished** and **execution that has finished**.

The purpose is to construct utterances containing plausible competing surface cues that could cause a classifier to rely on shortcuts rather than on the actual completion evidence.

The target state must remain determinable from the complete utterance.

### 2. Hard-Negative Construction Principle

A valid hard negative contains:

```text
Target execution state
        +
misleading competing surface cue
        +
sufficient completion evidence
        ↓
correct state remains recoverable
```

For B02, the decisive question remains:

> **Has execution finished?**

The following surface cues must not override the actual execution evidence:

- expressions such as “almost” or “nearly”;
- temporal expressions;
- conversational framing;
- statements about remaining or expected work;
- initial contradictory clauses;
- unrelated contextual information.

### 3. Hard-Negative Mechanisms

The six examples below cover the six Stage 2C hard-negative mechanisms:

1. Competing temporal cue
2. Competing execution-status phrase
3. Misleading opening clause
4. Self-correction
5. Multiple competing cues
6. Strong conversational distractor

---

#### HN02-01 — Competing Temporal Cue

**Hard-Negative Type:** Competing temporal cue  
**Target Task:** Medication  
**Execution Status:** Completed

> I took the medication earlier today, and it's completely finished.

**Misleading cue:** “earlier today” may draw attention toward temporal information rather than execution completion.

**Decisive evidence:** “it's completely finished” establishes completed execution.

---

#### HN02-02 — Competing Execution-Status Phrase

**Hard-Negative Type:** Competing execution-status phrase  
**Target Task:** Exercise  
**Execution Status:** In Progress

> I haven't finished the exercise routine yet; I'm still on the last exercise.

**Misleading cue:** “last exercise” may suggest that completion is imminent or already achieved.

**Decisive evidence:** “I haven't finished” and “I'm still on” establish unfinished execution.

---

#### HN02-03 — Misleading Opening Clause

**Hard-Negative Type:** Misleading opening clause  
**Target Task:** Physiotherapy  
**Execution Status:** Completed

> I'm still tired from the physiotherapy routine, but I finished the whole thing.

**Misleading cue:** “I'm still tired” can suggest that the activity is still ongoing.

**Decisive evidence:** “I finished the whole thing” establishes completed execution.

---

#### HN02-04 — Self-Correction

**Hard-Negative Type:** Self-correction  
**Target Task:** Hydration  
**Execution Status:** Completed

> I still have some water to drink—no, that's from another bottle; I finished the one for this task.

**Misleading cue:** The initial statement suggests remaining execution.

**Decisive evidence:** The self-correction clarifies that the target task's execution is complete.

---

#### HN02-05 — Multiple Competing Cues

**Hard-Negative Type:** Multiple competing cues  
**Target Task:** Exercise  
**Execution Status:** In Progress

> I did most of the exercises earlier, I'm almost there, but I still have one exercise left to complete.

**Misleading cues:** “did most,” “earlier,” and “almost there” all suggest substantial progress toward completion.

**Decisive evidence:** “I still have one exercise left” establishes that execution remains unfinished.

---

#### HN02-06 — Strong Conversational Distractor

**Hard-Negative Type:** Strong conversational distractor  
**Target Task:** Physiotherapy  
**Execution Status:** Completed

> My legs are tired and I need to rest now; I finished the entire physiotherapy routine.

**Misleading cue:** The focus on fatigue and the need to rest can distract from the execution state.

**Decisive evidence:** “I finished the entire physiotherapy routine” establishes completed execution.

### 4. Production Records

```yaml
- example_id: HN02-01
  pair_id: HN02
  parent_id: null
  lineage_id: HN02-01
  execution_status: Completed
  semantic_subtype: hard_negative
  stage: 2C
  resource_type: hard_negative
  boundary_id: B02
  anchor_type: null
  context: "Medication execution has finished; the utterance contains a temporal cue."
  utterance: "I took the medication earlier today, and it's completely finished."
  target_task: medication
  closest_competing_state: In Progress
  variation_type: competing_temporal_cue
  hard_negative_type: competing_temporal_cue
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: HN02-02
  pair_id: HN02
  parent_id: null
  lineage_id: HN02-02
  execution_status: In Progress
  semantic_subtype: hard_negative
  stage: 2C
  resource_type: hard_negative
  boundary_id: B02
  anchor_type: null
  context: "Exercise execution has begun and remains unfinished."
  utterance: "I haven't finished the exercise routine yet; I'm still on the last exercise."
  target_task: exercise
  closest_competing_state: Completed
  variation_type: competing_execution_status_phrase
  hard_negative_type: competing_execution_status_phrase
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: HN02-03
  pair_id: HN02
  parent_id: null
  lineage_id: HN02-03
  execution_status: Completed
  semantic_subtype: hard_negative
  stage: 2C
  resource_type: hard_negative
  boundary_id: B02
  anchor_type: null
  context: "Physiotherapy execution has finished despite a misleading opening clause about the user's current physical state."
  utterance: "I'm still tired from the physiotherapy routine, but I finished the whole thing."
  target_task: physiotherapy
  closest_competing_state: In Progress
  variation_type: misleading_opening_clause
  hard_negative_type: misleading_opening_clause
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: HN02-04
  pair_id: HN02
  parent_id: null
  lineage_id: HN02-04
  execution_status: Completed
  semantic_subtype: hard_negative
  stage: 2C
  resource_type: hard_negative
  boundary_id: B02
  anchor_type: null
  context: "Hydration execution is complete; the utterance contains a self-correction about remaining water."
  utterance: "I still have some water to drink—no, that's from another bottle; I finished the one for this task."
  target_task: hydration
  closest_competing_state: In Progress
  variation_type: self_correction
  hard_negative_type: self_correction
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: HN02-05
  pair_id: HN02
  parent_id: null
  lineage_id: HN02-05
  execution_status: In Progress
  semantic_subtype: hard_negative
  stage: 2C
  resource_type: hard_negative
  boundary_id: B02
  anchor_type: null
  context: "Exercise execution is substantially advanced but one exercise remains."
  utterance: "I did most of the exercises earlier, I'm almost there, but I still have one exercise left to complete."
  target_task: exercise
  closest_competing_state: Completed
  variation_type: multiple_competing_cues
  hard_negative_type: multiple_competing_cues
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: HN02-06
  pair_id: HN02
  parent_id: null
  lineage_id: HN02-06
  execution_status: Completed
  semantic_subtype: hard_negative
  stage: 2C
  resource_type: hard_negative
  boundary_id: B02
  anchor_type: null
  context: "The physiotherapy routine has finished; the utterance contains a strong distractor about fatigue and subsequent rest."
  utterance: "My legs are tired and I need to rest now; I finished the entire physiotherapy routine."
  target_task: physiotherapy
  closest_competing_state: In Progress
  variation_type: strong_conversational_distractor
  hard_negative_type: strong_conversational_distractor
  source: constructed
  validation_status: candidate
  ambiguity_flag: false
```

### 5. Hard-Negative Diagnostic Rationale

| Example | Competing cue | Decisive execution evidence |
|---|---|---|
| HN02-01 | Temporal information | Target execution is explicitly finished |
| HN02-02 | Near-completion wording | Execution is explicitly still unfinished |
| HN02-03 | Current fatigue | The entire routine is explicitly finished |
| HN02-04 | Initial remaining-work statement | Self-correction establishes completion |
| HN02-05 | Extensive progress and “almost” | One exercise remains |
| HN02-06 | Fatigue and need for rest | Entire routine is explicitly finished |

The examples are designed so that completion cannot be reliably inferred from isolated lexical cues such as “last,” “earlier,” “tired,” or “almost.” The complete utterance must be interpreted.

### 6. Hard-Negative Validation Criteria

A candidate is valid only if:

1. The target task is identifiable.
2. The target execution status is semantically clear from the complete utterance.
3. A genuine competing cue is present.
4. The competing cue is plausible enough to create a classification challenge.
5. The competing cue does not actually change the execution state.
6. The decisive completion evidence remains present.
7. In Progress examples establish both begun execution and unfinished execution.
8. Completed examples establish finished execution.
9. Near-completion language is not treated as completion.
10. The example does not depend on motivation, persuasion barriers, dialogue purpose, or sentiment.
11. The example does not require external task-manager reasoning.
12. The utterance remains natural conversational language.
13. The hard negative does not become genuinely ambiguous.

### 7. Boundary Invariant

For HN02:

> **Competing surface cues must not override direct evidence about execution completion.**

The classifier must determine whether execution has finished. Progress level, temporal framing, physical state, conversational distractors, and other secondary cues must not override explicit evidence that the task is either still unfinished or fully completed.
