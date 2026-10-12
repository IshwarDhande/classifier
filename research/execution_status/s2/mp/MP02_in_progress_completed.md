# Stage 2B — Minimal Pairs
## MP02: In Progress ↔ Completed

### 1. Boundary Definition

**Boundary ID:** B02  
**State A:** In Progress  
**State B:** Completed

This minimal-pair resource isolates the transition from **execution that has begun but remains unfinished** to **execution that has finished**.

The paired utterances should preserve the same underlying task and practical context as far as natural language permits. The decisive change is the evidence about whether execution is still ongoing or has finished.

### 2. Minimal-Pair Construction Principle

A valid B02 minimal pair satisfies:

```text
Same task/context
        +
minimal semantic change
        ↓
execution-completion evidence changes
        ↓
In Progress ↔ Completed
```

The pair must not rely on changing:

- task identity;
- persuasion barrier;
- motivation;
- dialogue purpose;
- sentiment;
- scheduling information;
- unrelated temporal details.

The decisive distinction is:

> **In Progress:** execution has begun but remains unfinished.  
> **Completed:** execution has finished.

### 3. Minimal-Pair Families

The following six families provide complementary realizations of the B02 boundary.

---

#### MP02-01 — Explicit Completion Evidence

**Target Task:** Medication

**In Progress:**
> I'm still taking the medication; I haven't finished yet.

**Completed:**
> I've finished taking the medication.

**Decisive change:** explicit unfinished execution versus explicit finished execution.

---

#### MP02-02 — Remaining Work Evidence

**Target Task:** Exercise

**In Progress:**
> I've done most of the exercises, but I still have one left.

**Completed:**
> I've done all the exercises; there isn't one left.

**Decisive change:** remaining execution versus no remaining execution.

---

#### MP02-03 — Ongoing Versus Finished Routine

**Target Task:** Physiotherapy

**In Progress:**
> I'm still working through the physiotherapy routine.

**Completed:**
> I've completed the physiotherapy routine.

**Decisive change:** ongoing routine versus finished routine.

---

#### MP02-04 — Final-Step Boundary

**Target Task:** Hydration

**In Progress:**
> I'm nearly finished with the water, but there's still some left.

**Completed:**
> I've finished the water; there's none left.

**Decisive change:** final portion remains versus final portion has been consumed.

---

#### MP02-05 — Partial Versus Complete Execution

**Target Task:** Exercise

**In Progress:**
> I've completed the first few exercises and still have the rest to do.

**Completed:**
> I've completed all of the exercises.

**Decisive change:** partial execution versus complete execution.

---

#### MP02-06 — Indirect Completion Evidence

**Target Task:** Physiotherapy

**In Progress:**
> I'm halfway through the routine and still have exercises left.

**Completed:**
> The whole routine is done, and I have nothing left to do.

**Decisive change:** unfinished scope versus finished scope.

### 4. Production Records

```yaml
- example_id: MP02-01-A
  pair_id: MP02-01
  parent_id: null
  lineage_id: MP02-01
  execution_status: In Progress
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B02
  anchor_type: null
  context: "Medication execution has begun but remains unfinished."
  utterance: "I'm still taking the medication; I haven't finished yet."
  target_task: medication
  closest_competing_state: Completed
  variation_type: explicit_completion
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP02-01-B
  pair_id: MP02-01
  parent_id: null
  lineage_id: MP02-01
  execution_status: Completed
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B02
  anchor_type: null
  context: "Medication execution has finished."
  utterance: "I've finished taking the medication."
  target_task: medication
  closest_competing_state: In Progress
  variation_type: explicit_completion
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP02-02-A
  pair_id: MP02-02
  parent_id: null
  lineage_id: MP02-02
  execution_status: In Progress
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B02
  anchor_type: null
  context: "Exercise execution is substantially complete but one exercise remains."
  utterance: "I've done most of the exercises, but I still have one left."
  target_task: exercise
  closest_competing_state: Completed
  variation_type: remaining_work
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP02-02-B
  pair_id: MP02-02
  parent_id: null
  lineage_id: MP02-02
  execution_status: Completed
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B02
  anchor_type: null
  context: "All exercise execution is finished."
  utterance: "I've done all the exercises; there isn't one left."
  target_task: exercise
  closest_competing_state: In Progress
  variation_type: remaining_work
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP02-03-A
  pair_id: MP02-03
  parent_id: null
  lineage_id: MP02-03
  execution_status: In Progress
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B02
  anchor_type: null
  context: "The physiotherapy routine is underway but unfinished."
  utterance: "I'm still working through the physiotherapy routine."
  target_task: physiotherapy
  closest_competing_state: Completed
  variation_type: ongoing_vs_finished
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP02-03-B
  pair_id: MP02-03
  parent_id: null
  lineage_id: MP02-03
  execution_status: Completed
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B02
  anchor_type: null
  context: "The physiotherapy routine has been fully executed."
  utterance: "I've completed the physiotherapy routine."
  target_task: physiotherapy
  closest_competing_state: In Progress
  variation_type: ongoing_vs_finished
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP02-04-A
  pair_id: MP02-04
  parent_id: null
  lineage_id: MP02-04
  execution_status: In Progress
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B02
  anchor_type: null
  context: "Hydration execution is almost complete but some water remains."
  utterance: "I'm nearly finished with the water, but there's still some left."
  target_task: hydration
  closest_competing_state: Completed
  variation_type: final_step_boundary
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP02-04-B
  pair_id: MP02-04
  parent_id: null
  lineage_id: MP02-04
  execution_status: Completed
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B02
  anchor_type: null
  context: "Hydration execution has reached completion."
  utterance: "I've finished the water; there's none left."
  target_task: hydration
  closest_competing_state: In Progress
  variation_type: final_step_boundary
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP02-05-A
  pair_id: MP02-05
  parent_id: null
  lineage_id: MP02-05
  execution_status: In Progress
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B02
  anchor_type: null
  context: "Only part of the exercise set has been completed."
  utterance: "I've completed the first few exercises and still have the rest to do."
  target_task: exercise
  closest_competing_state: Completed
  variation_type: partial_vs_complete
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP02-05-B
  pair_id: MP02-05
  parent_id: null
  lineage_id: MP02-05
  execution_status: Completed
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B02
  anchor_type: null
  context: "The complete exercise set has been executed."
  utterance: "I've completed all of the exercises."
  target_task: exercise
  closest_competing_state: In Progress
  variation_type: partial_vs_complete
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP02-06-A
  pair_id: MP02-06
  parent_id: null
  lineage_id: MP02-06
  execution_status: In Progress
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B02
  anchor_type: null
  context: "The physiotherapy routine is partially complete and remains unfinished."
  utterance: "I'm halfway through the routine and still have exercises left."
  target_task: physiotherapy
  closest_competing_state: Completed
  variation_type: indirect_completion_evidence
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP02-06-B
  pair_id: MP02-06
  parent_id: null
  lineage_id: MP02-06
  execution_status: Completed
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B02
  anchor_type: null
  context: "The entire physiotherapy routine has been executed."
  utterance: "The whole routine is done, and I have nothing left to do."
  target_task: physiotherapy
  closest_competing_state: In Progress
  variation_type: indirect_completion_evidence
  source: constructed
  validation_status: candidate
  ambiguity_flag: false
```

### 5. Pair-Level Diagnostic Rationale

| Pair | In Progress evidence | Completed evidence |
|---|---|---|
| MP02-01 | Execution is ongoing | Execution is explicitly finished |
| MP02-02 | Some execution remains | No execution remains |
| MP02-03 | Routine is still underway | Routine is finished |
| MP02-04 | Final portion remains | Final portion has been consumed |
| MP02-05 | Only part of the task is complete | Entire task is complete |
| MP02-06 | Remaining exercises are explicit | Finished scope and absence of remaining work are explicit |

Each pair changes the execution-completion evidence while preserving the target task and the underlying practical situation as closely as natural language allows.

### 6. Minimal-Pair Validation Criteria

A pair is valid only if:

1. Both utterances refer to the same target task.
2. Both utterances represent the same broad practical situation where natural.
3. The labels differ because of execution-completion evidence.
4. The In Progress member establishes that execution has begun.
5. The In Progress member establishes that execution remains unfinished.
6. The Completed member establishes that execution has finished.
7. “Almost finished” is not treated as Completed.
8. Partial execution is not treated as Completed.
9. The distinction does not depend on motivation, persuasion barriers, dialogue purpose, or sentiment.
10. The example does not require external scheduling or task-manager reasoning.
11. The pair remains natural conversational language.
12. The pair does not create a systematic lexical shortcut across the dataset.

### 7. Boundary Invariant

For MP02:

> **Change only the evidence of execution completion.**

The In Progress member must establish that execution has started and remains unfinished. The Completed member must establish that execution has finished. The semantic label must not be determined by scheduling, intention, motivation, or unrelated temporal information.
