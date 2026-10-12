# Stage 2A — Boundary Anchors
## BA02: In Progress ↔ Completed

### 1. Boundary Definition

**Boundary ID:** B02  
**State A:** In Progress  
**State B:** Completed

This boundary distinguishes execution that has **begun but remains unfinished** from execution that has **finished**.

The distinction is based on direct evidence of execution completion. Temporal expressions, plans, intentions, scheduling information, motivation, or reasons for execution/non-execution do not determine the boundary unless they provide explicit evidence about whether execution has finished.

### 2. Semantic Boundary

**Diagnostic question:**

> Has the execution of the target task finished?

- **In Progress:** execution has begun, but there is evidence that some execution remains.
- **Completed:** execution has finished, with no remaining execution required for the stated task.

The critical distinction is therefore:

```text
In Progress  → execution started + unfinished
Completed    → execution finished
```

### 3. Anchor Construction

The boundary is represented using six complementary anchor types:

1. **A Prototype** — clear In Progress example.
2. **B Prototype** — clear Completed example.
3. **A-Leaning Boundary** — near the completion boundary but still unfinished.
4. **B-Leaning Boundary** — near the completion boundary but clearly finished.
5. **Implicit A** — completion is not stated directly, but ongoing execution is inferable.
6. **Implicit B** — completion is not stated using a direct completion verb, but finished execution is inferable.

Anchors are constructed to expose the semantic distinction rather than relying on a fixed lexical marker.

### 4. Boundary Anchor Resources

#### BA02-01 — A Prototype

**Execution Status:** In Progress  
**Target Task:** Hydration  
**Anchor Type:** A Prototype

> I'm drinking the water now, and I still have some left.

**Diagnostic evidence:** Execution is explicitly underway and unfinished.

---

#### BA02-02 — B Prototype

**Execution Status:** Completed  
**Target Task:** Hydration  
**Anchor Type:** B Prototype

> I finished drinking the water.

**Diagnostic evidence:** The target execution is explicitly described as finished.

---

#### BA02-03 — A-Leaning Boundary

**Execution Status:** In Progress  
**Target Task:** Physiotherapy  
**Anchor Type:** A-Leaning Boundary

> I've done most of the physiotherapy exercises, but I still have one left.

**Diagnostic evidence:** Execution is substantially advanced, but the task remains unfinished.

---

#### BA02-04 — B-Leaning Boundary

**Execution Status:** Completed  
**Target Task:** Exercise  
**Anchor Type:** B-Leaning Boundary

> I just finished the last exercise.

**Diagnostic evidence:** The final execution step has been completed; the task is finished.

---

#### BA02-05 — Implicit A

**Execution Status:** In Progress  
**Target Task:** Medication  
**Anchor Type:** Implicit A

> I'm on the last few steps of taking it.

**Diagnostic evidence:** The utterance does not use an explicit completion statement, but ongoing execution and remaining steps establish that the task is unfinished.

---

#### BA02-06 — Implicit B

**Execution Status:** Completed  
**Target Task:** Physiotherapy  
**Anchor Type:** Implicit B

> That's the whole routine done for today.

**Diagnostic evidence:** Completion is conveyed through the finished scope of the routine rather than a simple completion verb.

### 5. Production Records

```yaml
- example_id: BA02-01
  pair_id: B02
  parent_id: null
  lineage_id: BA02-01
  execution_status: In Progress
  semantic_subtype: boundary_anchor
  stage: 2A
  resource_type: boundary_anchor
  boundary_id: B02
  anchor_type: A Prototype
  context: "Execution of a hydration task is underway and remains unfinished."
  utterance: "I'm drinking the water now, and I still have some left."
  target_task: hydration
  closest_competing_state: Completed
  variation_type: execution_completion_boundary
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: BA02-02
  pair_id: B02
  parent_id: null
  lineage_id: BA02-02
  execution_status: Completed
  semantic_subtype: boundary_anchor
  stage: 2A
  resource_type: boundary_anchor
  boundary_id: B02
  anchor_type: B Prototype
  context: "Execution of a hydration task has finished."
  utterance: "I finished drinking the water."
  target_task: hydration
  closest_competing_state: In Progress
  variation_type: execution_completion_boundary
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: BA02-03
  pair_id: B02
  parent_id: null
  lineage_id: BA02-03
  execution_status: In Progress
  semantic_subtype: boundary_anchor
  stage: 2A
  resource_type: boundary_anchor
  boundary_id: B02
  anchor_type: A-Leaning Boundary
  context: "Execution of a physiotherapy routine is nearly complete but one exercise remains."
  utterance: "I've done most of the physiotherapy exercises, but I still have one left."
  target_task: physiotherapy
  closest_competing_state: Completed
  variation_type: execution_completion_boundary
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: BA02-04
  pair_id: B02
  parent_id: null
  lineage_id: BA02-04
  execution_status: Completed
  semantic_subtype: boundary_anchor
  stage: 2A
  resource_type: boundary_anchor
  boundary_id: B02
  anchor_type: B-Leaning Boundary
  context: "Execution of an exercise routine has reached its final step and finished."
  utterance: "I just finished the last exercise."
  target_task: exercise
  closest_competing_state: In Progress
  variation_type: execution_completion_boundary
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: BA02-05
  pair_id: B02
  parent_id: null
  lineage_id: BA02-05
  execution_status: In Progress
  semantic_subtype: boundary_anchor
  stage: 2A
  resource_type: boundary_anchor
  boundary_id: B02
  anchor_type: Implicit A
  context: "Medication execution is underway and has remaining steps."
  utterance: "I'm on the last few steps of taking it."
  target_task: medication
  closest_competing_state: Completed
  variation_type: execution_completion_boundary
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: BA02-06
  pair_id: B02
  parent_id: null
  lineage_id: BA02-06
  execution_status: Completed
  semantic_subtype: boundary_anchor
  stage: 2A
  resource_type: boundary_anchor
  boundary_id: B02
  anchor_type: Implicit B
  context: "The complete physiotherapy routine has been carried out."
  utterance: "That's the whole routine done for today."
  target_task: physiotherapy
  closest_competing_state: In Progress
  variation_type: execution_completion_boundary
  source: constructed
  validation_status: candidate
  ambiguity_flag: false
```

### 6. Diagnostic Rationale

The six anchors collectively cover the central completion distinction:

| Anchor | State | Primary execution evidence |
|---|---|---|
| BA02-01 | In Progress | Execution is occurring and some remains |
| BA02-02 | Completed | Execution is explicitly finished |
| BA02-03 | In Progress | Most execution is complete, but one part remains |
| BA02-04 | Completed | Final execution step has finished |
| BA02-05 | In Progress | Remaining execution steps are implied |
| BA02-06 | Completed | Finished scope of the task is implied |

The boundary must not be decided from expressions such as “now,” “today,” “last,” or “just” in isolation. The decisive evidence is whether the target execution is unfinished or finished.

### 7. Boundary Validation Criteria

A candidate is valid only if:

1. The target task is identifiable.
2. Execution has clearly begun for an In Progress example.
3. An In Progress example contains evidence that execution remains unfinished.
4. A Completed example contains evidence that execution has finished.
5. The distinction does not depend solely on scheduling or temporal language.
6. The distinction does not depend on motivation, persuasion barriers, dialogue purpose, or sentiment.
7. The example does not require external task-manager reasoning.
8. The utterance remains natural conversational language.
9. The target label can be determined from the utterance itself.
10. The closest competing state is genuinely plausible but semantically incorrect.

### 8. Boundary Invariant

For B02, the invariant is:

> **In Progress = execution has started but is not finished. Completed = execution has finished.**

No amount of planning, future intention, scheduling information, motivation, or contextual urgency should override direct evidence about execution completion.
