# Stage 2A — Boundary Anchors
## BA03: Not Started ↔ Completed

### 1. Boundary Definition

**Boundary ID:** B03  
**State A:** Not Started  
**State B:** Completed

This boundary distinguishes the **absence of begun execution** from **finished execution**.

The distinction is based on evidence of actual task execution. Planning, future intention, scheduling, motivation, reasons for non-execution, or other conversational information do not determine the boundary unless they establish that execution has or has not actually occurred.

### 2. Semantic Boundary

**Diagnostic question:**

> Is there evidence that the target task has been executed to completion?

- **Not Started:** there is no evidence that execution of the target task has begun.
- **Completed:** there is evidence that execution has finished.

The critical distinction is therefore:

```text
Not Started  → no execution begun
Completed    → execution finished
```

This is a non-adjacent boundary in the execution lifecycle. `In Progress` lies between the two states, but the B03 boundary remains important because conversational utterances can directly contrast non-execution with completed execution.

### 3. Anchor Construction

The boundary is represented using six complementary anchor types:

1. **A Prototype** — clear Not Started example.
2. **B Prototype** — clear Completed example.
3. **A-Leaning Boundary** — clearly non-executed but close to an execution-related boundary.
4. **B-Leaning Boundary** — clearly completed with little remaining uncertainty.
5. **Implicit A** — non-execution is inferable without a direct “not started” statement.
6. **Implicit B** — completion is inferable without a simple explicit completion verb.

Anchors are constructed around actual execution evidence rather than lexical oppositions.

### 4. Boundary Anchor Resources

#### BA03-01 — A Prototype

**Execution Status:** Not Started  
**Target Task:** Medication  
**Anchor Type:** A Prototype

> I haven't started taking the medication yet.

**Diagnostic evidence:** The utterance explicitly states that execution has not begun.

---

#### BA03-02 — B Prototype

**Execution Status:** Completed  
**Target Task:** Medication  
**Anchor Type:** B Prototype

> I finished taking the medication.

**Diagnostic evidence:** The target medication task is explicitly described as finished.

---

#### BA03-03 — A-Leaning Boundary

**Execution Status:** Not Started  
**Target Task:** Exercise  
**Anchor Type:** A-Leaning Boundary

> I have everything ready, but I haven't started the exercises.

**Diagnostic evidence:** Preparation is complete, but the actual execution has not begun.

---

#### BA03-04 — B-Leaning Boundary

**Execution Status:** Completed  
**Target Task:** Exercise  
**Anchor Type:** B-Leaning Boundary

> I completed the exercises and put everything away.

**Diagnostic evidence:** The exercise execution is explicitly finished, with a post-execution action providing additional completion evidence.

---

#### BA03-05 — Implicit A

**Execution Status:** Not Started  
**Target Task:** Hydration  
**Anchor Type:** Implicit A

> The bottle is still untouched.

**Diagnostic evidence:** The untouched state implies that the target hydration execution has not begun.

---

#### BA03-06 — Implicit B

**Execution Status:** Completed  
**Target Task:** Physiotherapy  
**Anchor Type:** Implicit B

> The whole routine is behind me now.

**Diagnostic evidence:** The utterance conveys that the complete routine has been carried out, without using a direct completion verb.

### 5. Production Records

```yaml
- example_id: BA03-01
  pair_id: B03
  parent_id: null
  lineage_id: BA03-01
  execution_status: Not Started
  semantic_subtype: boundary_anchor
  stage: 2A
  resource_type: boundary_anchor
  boundary_id: B03
  anchor_type: A Prototype
  context: "The target medication task has not begun."
  utterance: "I haven't started taking the medication yet."
  target_task: medication
  closest_competing_state: Completed
  variation_type: execution_completion_boundary
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: BA03-02
  pair_id: B03
  parent_id: null
  lineage_id: BA03-02
  execution_status: Completed
  semantic_subtype: boundary_anchor
  stage: 2A
  resource_type: boundary_anchor
  boundary_id: B03
  anchor_type: B Prototype
  context: "The target medication task has finished."
  utterance: "I finished taking the medication."
  target_task: medication
  closest_competing_state: Not Started
  variation_type: execution_completion_boundary
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: BA03-03
  pair_id: B03
  parent_id: null
  lineage_id: BA03-03
  execution_status: Not Started
  semantic_subtype: boundary_anchor
  stage: 2A
  resource_type: boundary_anchor
  boundary_id: B03
  anchor_type: A-Leaning Boundary
  context: "An exercise task has been prepared but execution has not begun."
  utterance: "I have everything ready, but I haven't started the exercises."
  target_task: exercise
  closest_competing_state: Completed
  variation_type: execution_completion_boundary
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: BA03-04
  pair_id: B03
  parent_id: null
  lineage_id: BA03-04
  execution_status: Completed
  semantic_subtype: boundary_anchor
  stage: 2A
  resource_type: boundary_anchor
  boundary_id: B03
  anchor_type: B-Leaning Boundary
  context: "An exercise task has been fully executed and followed by a post-execution action."
  utterance: "I completed the exercises and put everything away."
  target_task: exercise
  closest_competing_state: Not Started
  variation_type: execution_completion_boundary
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: BA03-05
  pair_id: B03
  parent_id: null
  lineage_id: BA03-05
  execution_status: Not Started
  semantic_subtype: boundary_anchor
  stage: 2A
  resource_type: boundary_anchor
  boundary_id: B03
  anchor_type: Implicit A
  context: "The target hydration task has not been initiated."
  utterance: "The bottle is still untouched."
  target_task: hydration
  closest_competing_state: Completed
  variation_type: execution_completion_boundary
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: BA03-06
  pair_id: B03
  parent_id: null
  lineage_id: BA03-06
  execution_status: Completed
  semantic_subtype: boundary_anchor
  stage: 2A
  resource_type: boundary_anchor
  boundary_id: B03
  anchor_type: Implicit B
  context: "The complete physiotherapy routine has already been carried out."
  utterance: "The whole routine is behind me now."
  target_task: physiotherapy
  closest_competing_state: Not Started
  variation_type: execution_completion_boundary
  source: constructed
  validation_status: candidate
  ambiguity_flag: false
```

### 6. Diagnostic Rationale

The six anchors collectively cover the core non-execution versus completed-execution distinction:

| Anchor | State | Primary execution evidence |
|---|---|---|
| BA03-01 | Not Started | Explicitly states that execution has not begun |
| BA03-02 | Completed | Explicitly states that execution has finished |
| BA03-03 | Not Started | Preparation exists, but execution has not begun |
| BA03-04 | Completed | Completed execution is supported by the subsequent post-execution action |
| BA03-05 | Not Started | Untouched task object implies no execution |
| BA03-06 | Completed | Finished scope of the routine is implied |

The boundary must not be determined from future-oriented language, scheduling information, or reasons for non-execution. Likewise, completion must be grounded in evidence that the target execution actually finished.

### 7. Boundary Validation Criteria

A candidate is valid only if:

1. The target task is identifiable.
2. The Not Started example contains no evidence that execution has begun.
3. The Completed example contains evidence that execution has finished.
4. Preparation is not treated as execution.
5. Future intention is not treated as execution.
6. Reasons for non-execution do not determine the label.
7. The distinction does not depend on motivation, persuasion barriers, dialogue purpose, or sentiment.
8. The example does not require external task-manager reasoning.
9. The utterance remains natural conversational language.
10. The closest competing state is semantically plausible but incorrect.

### 8. Boundary Invariant

For B03, the invariant is:

> **Not Started = no execution has begun. Completed = execution has finished.**

The presence of preparation, intention, scheduling, or discussion about the task must not be mistaken for execution. Completed status requires evidence that the target task itself has been carried out to completion.
