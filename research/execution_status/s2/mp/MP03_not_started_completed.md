# Stage 2B — Minimal Pairs
## MP03: Not Started ↔ Completed

### 1. Boundary Definition

**Boundary ID:** B03  
**State A:** Not Started  
**State B:** Completed

This minimal-pair resource isolates the distinction between **no execution having begun** and **execution having finished**.

The paired utterances should preserve the same underlying task and practical situation as far as natural language permits. The decisive change is whether there is evidence of completed execution.

### 2. Minimal-Pair Construction Principle

A valid B03 minimal pair satisfies:

```text
Same task/context
        +
minimal semantic change
        ↓
execution evidence changes
        ↓
Not Started ↔ Completed
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

> **Not Started:** execution has not begun.  
> **Completed:** execution has finished.

### 3. Minimal-Pair Families

The following six families provide complementary realizations of the B03 boundary.

---

#### MP03-01 — Direct Non-Execution Versus Completion

**Target Task:** Medication

**Not Started:**
> I haven't started taking the medication yet.

**Completed:**
> I finished taking the medication.

**Decisive change:** explicit absence of execution versus explicit finished execution.

---

#### MP03-02 — Untouched Versus Finished

**Target Task:** Hydration

**Not Started:**
> I haven't touched the water yet.

**Completed:**
> I've finished the water.

**Decisive change:** the target has not been executed versus the target execution is complete.

---

#### MP03-03 — Preparation Versus Finished Execution

**Target Task:** Exercise

**Not Started:**
> The exercise mat is ready, but I haven't done the exercises.

**Completed:**
> The exercises are done, and the mat is put away.

**Decisive change:** preparation without execution versus completed execution followed by a post-execution action.

---

#### MP03-04 — Future Intention Versus Retrospective Completion

**Target Task:** Physiotherapy

**Not Started:**
> I'll do the physiotherapy routine later; I haven't started it.

**Completed:**
> I did the physiotherapy routine already.

**Decisive change:** future intention without execution versus retrospective evidence of finished execution.

---

#### MP03-05 — Indirect Non-Execution Versus Indirect Completion

**Target Task:** Medication

**Not Started:**
> The medication is still untouched.

**Completed:**
> The medication has been taken, and there's nothing left to take.

**Decisive change:** untouched state versus completed execution with no remaining task.

---

#### MP03-06 — Refusal/Non-Execution Versus Completion

**Target Task:** Exercise

**Not Started:**
> I didn't do the exercises.

**Completed:**
> I did all the exercises.

**Decisive change:** absence of execution versus complete execution.

### 4. Production Records

```yaml
- example_id: MP03-01-A
  pair_id: MP03-01
  parent_id: null
  lineage_id: MP03-01
  execution_status: Not Started
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B03
  anchor_type: null
  context: "Medication execution has not begun."
  utterance: "I haven't started taking the medication yet."
  target_task: medication
  closest_competing_state: Completed
  variation_type: direct_execution_evidence
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP03-01-B
  pair_id: MP03-01
  parent_id: null
  lineage_id: MP03-01
  execution_status: Completed
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B03
  anchor_type: null
  context: "Medication execution has finished."
  utterance: "I finished taking the medication."
  target_task: medication
  closest_competing_state: Not Started
  variation_type: direct_execution_evidence
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP03-02-A
  pair_id: MP03-02
  parent_id: null
  lineage_id: MP03-02
  execution_status: Not Started
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B03
  anchor_type: null
  context: "The hydration task has not begun."
  utterance: "I haven't touched the water yet."
  target_task: hydration
  closest_competing_state: Completed
  variation_type: untouched_vs_finished
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP03-02-B
  pair_id: MP03-02
  parent_id: null
  lineage_id: MP03-02
  execution_status: Completed
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B03
  anchor_type: null
  context: "The hydration task has finished."
  utterance: "I've finished the water."
  target_task: hydration
  closest_competing_state: Not Started
  variation_type: untouched_vs_finished
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP03-03-A
  pair_id: MP03-03
  parent_id: null
  lineage_id: MP03-03
  execution_status: Not Started
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B03
  anchor_type: null
  context: "Exercise preparation is complete but execution has not begun."
  utterance: "The exercise mat is ready, but I haven't done the exercises."
  target_task: exercise
  closest_competing_state: Completed
  variation_type: preparation_vs_completion
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP03-03-B
  pair_id: MP03-03
  parent_id: null
  lineage_id: MP03-03
  execution_status: Completed
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B03
  anchor_type: null
  context: "Exercise execution has finished and the equipment has been put away."
  utterance: "The exercises are done, and the mat is put away."
  target_task: exercise
  closest_competing_state: Not Started
  variation_type: preparation_vs_completion
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP03-04-A
  pair_id: MP03-04
  parent_id: null
  lineage_id: MP03-04
  execution_status: Not Started
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B03
  anchor_type: null
  context: "Physiotherapy execution has not begun; the user expresses future intention."
  utterance: "I'll do the physiotherapy routine later; I haven't started it."
  target_task: physiotherapy
  closest_competing_state: Completed
  variation_type: future_intention_vs_completion
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP03-04-B
  pair_id: MP03-04
  parent_id: null
  lineage_id: MP03-04
  execution_status: Completed
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B03
  anchor_type: null
  context: "Physiotherapy execution has already finished."
  utterance: "I did the physiotherapy routine already."
  target_task: physiotherapy
  closest_competing_state: Not Started
  variation_type: future_intention_vs_completion
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP03-05-A
  pair_id: MP03-05
  parent_id: null
  lineage_id: MP03-05
  execution_status: Not Started
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B03
  anchor_type: null
  context: "The medication has not been used."
  utterance: "The medication is still untouched."
  target_task: medication
  closest_competing_state: Completed
  variation_type: indirect_execution_evidence
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP03-05-B
  pair_id: MP03-05
  parent_id: null
  lineage_id: MP03-05
  execution_status: Completed
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B03
  anchor_type: null
  context: "The medication task has been fully executed."
  utterance: "The medication has been taken, and there's nothing left to take."
  target_task: medication
  closest_competing_state: Not Started
  variation_type: indirect_execution_evidence
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP03-06-A
  pair_id: MP03-06
  parent_id: null
  lineage_id: MP03-06
  execution_status: Not Started
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B03
  anchor_type: null
  context: "The exercise task was not executed."
  utterance: "I didn't do the exercises."
  target_task: exercise
  closest_competing_state: Completed
  variation_type: non_execution_vs_completion
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP03-06-B
  pair_id: MP03-06
  parent_id: null
  lineage_id: MP03-06
  execution_status: Completed
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B03
  anchor_type: null
  context: "The complete exercise task was executed."
  utterance: "I did all the exercises."
  target_task: exercise
  closest_competing_state: Not Started
  variation_type: non_execution_vs_completion
  source: constructed
  validation_status: candidate
  ambiguity_flag: false
```

### 5. Pair-Level Diagnostic Rationale

| Pair | Not Started evidence | Completed evidence |
|---|---|---|
| MP03-01 | Execution explicitly has not begun | Execution explicitly finished |
| MP03-02 | Target remains untouched | Target execution is finished |
| MP03-03 | Preparation exists without execution | Execution is finished |
| MP03-04 | Future intention without execution | Retrospective completed execution |
| MP03-05 | Untouched target | Completed execution and no remaining task |
| MP03-06 | No execution occurred | Complete execution occurred |

The pairs deliberately include cases where planning, preparation, future intention, or indirect object-state evidence could otherwise be mistaken for execution.

### 6. Minimal-Pair Validation Criteria

A pair is valid only if:

1. Both utterances refer to the same target task.
2. Both utterances represent the same broad practical situation where natural.
3. The Not Started member contains no evidence of begun execution.
4. The Completed member contains evidence that execution has finished.
5. Preparation is not treated as execution.
6. Future intention is not treated as execution.
7. A refusal or non-execution statement remains Not Started when no execution occurred.
8. Indirect evidence still clearly determines the execution state.
9. The distinction does not depend on motivation, persuasion barriers, dialogue purpose, or sentiment.
10. The example does not require external scheduling or task-manager reasoning.
11. The pair remains natural conversational language.
12. The pair does not create a systematic lexical shortcut across the dataset.

### 7. Boundary Invariant

For MP03:

> **Change only the evidence distinguishing no begun execution from finished execution.**

The Not Started member must establish absence of begun execution. The Completed member must establish finished execution. Preparation, intention, scheduling, or discussion about the task must not be mistaken for execution.
