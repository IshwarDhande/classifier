# Stage 2A — Boundary Anchors: B01 Not Started ↔ In Progress

## 1. Boundary Definition

**Boundary ID:** `B01`

**State pair:** `Not Started ↔ In Progress`

**Boundary class:** Adjacent lifecycle boundary

**Diagnostic question:**

> Has execution of the target task actually begun?

The boundary separates non-execution, preparation, or future action from actual execution that has begun but is not yet finished.

## 2. Semantic Boundary

| State | Boundary condition |
|---|---|
| Not Started | The target task has not begun, even if the user intends, prepares, delays, refuses, or plans to perform it. |
| In Progress | Execution of the target task has begun and remains unfinished. |

The minimum semantic distinction is **execution initiation**. Planning, preparation, future intention, and scheduling do not by themselves establish that execution has begun.

## 3. Anchor Construction

The boundary uses the six required anchor types:

1. A Prototype
2. B Prototype
3. A-Leaning Boundary
4. B-Leaning Boundary
5. Implicit A
6. Implicit B

## 4. Boundary Anchor Resources

| ID | Anchor Type | Task | Execution Status | Utterance |
|---|---|---|---|---|
| `BA01-01` | A Prototype | Medication | `Not Started` | I haven't started taking the medication yet. |
| `BA01-02` | B Prototype | Medication | `In Progress` | I'm taking the medication now. |
| `BA01-03` | A-Leaning Boundary | Exercise | `Not Started` | I'm getting ready to start the exercises, but I haven't begun them yet. |
| `BA01-04` | B-Leaning Boundary | Exercise | `In Progress` | I've started the first exercise, and I'm working through it now. |
| `BA01-05` | Implicit A | Hydration | `Not Started` | The bottle is still full; I'll deal with it after I finish this. |
| `BA01-06` | Implicit B | Physiotherapy | `In Progress` | I'm halfway through the routine and still have a few exercises left. |

## 5. Production Records

```yaml
example_id: BA01-01
pair_id: B01
parent_id: BA01-01
lineage_id: B01-01
execution_status: Not Started
semantic_subtype: boundary_anchor
stage: 2A
resource_type: boundary_anchor
boundary_id: B01
anchor_type: A Prototype
context: "Immediately after a medication reminder."
utterance: "I haven't started taking the medication yet."
target_task: Medication
closest_competing_state: In Progress
variation_type: boundary_semantic_realization
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA01-02
pair_id: B01
parent_id: BA01-02
lineage_id: B01-02
execution_status: In Progress
semantic_subtype: boundary_anchor
stage: 2A
resource_type: boundary_anchor
boundary_id: B01
anchor_type: B Prototype
context: "Immediately after a medication reminder."
utterance: "I'm taking the medication now."
target_task: Medication
closest_competing_state: Not Started
variation_type: boundary_semantic_realization
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA01-03
pair_id: B01
parent_id: BA01-03
lineage_id: B01-03
execution_status: Not Started
semantic_subtype: boundary_anchor
stage: 2A
resource_type: boundary_anchor
boundary_id: B01
anchor_type: A-Leaning Boundary
context: "The user is discussing beginning the exercise after a reminder."
utterance: "I'm getting ready to start the exercises, but I haven't begun them yet."
target_task: Exercise
closest_competing_state: In Progress
variation_type: boundary_semantic_realization
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA01-04
pair_id: B01
parent_id: BA01-04
lineage_id: B01-04
execution_status: In Progress
semantic_subtype: boundary_anchor
stage: 2A
resource_type: boundary_anchor
boundary_id: B01
anchor_type: B-Leaning Boundary
context: "The user responds while beginning the exercise."
utterance: "I've started the first exercise, and I'm working through it now."
target_task: Exercise
closest_competing_state: Not Started
variation_type: boundary_semantic_realization
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA01-05
pair_id: B01
parent_id: BA01-05
lineage_id: B01-05
execution_status: Not Started
semantic_subtype: boundary_anchor
stage: 2A
resource_type: boundary_anchor
boundary_id: B01
anchor_type: Implicit A
context: "The user responds to a hydration reminder."
utterance: "The bottle is still full; I'll deal with it after I finish this."
target_task: Hydration
closest_competing_state: In Progress
variation_type: boundary_semantic_realization
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA01-06
pair_id: B01
parent_id: BA01-06
lineage_id: B01-06
execution_status: In Progress
semantic_subtype: boundary_anchor
stage: 2A
resource_type: boundary_anchor
boundary_id: B01
anchor_type: Implicit B
context: "The user responds during a physiotherapy routine."
utterance: "I'm halfway through the routine and still have a few exercises left."
target_task: Physiotherapy
closest_competing_state: Not Started
variation_type: boundary_semantic_realization
source: constructed
validation_status: candidate
ambiguity_flag: false
```

## 6. Diagnostic Rationale

### BA01-01 — A Prototype

Execution of the target medication task has not begun.

### BA01-02 — B Prototype

Execution of the target medication task has begun and is currently ongoing.

### BA01-03 — A-Leaning Boundary

Preparation is occurring, but the target exercise itself has not started.

### BA01-04 — B-Leaning Boundary

Actual execution of the target exercise has begun, even though the task is not complete.

### BA01-05 — Implicit A

The target hydration task remains unexecuted; the statement expresses future action rather than current execution.

### BA01-06 — Implicit B

The target physiotherapy routine has clearly begun and remains unfinished.

## 7. Boundary Validation Criteria

A B01 anchor is acceptable only when the execution distinction is recoverable from the utterance and relevant context without relying on a single temporal or status keyword.

### Not Started anchors

- No actual execution of the target task has begun.
- Preparation must not be treated as execution.
- Future intention must not be treated as execution.
- The target task must remain the object of the execution judgment.

### In Progress anchors

- Actual execution of the target task has begun.
- The target task must remain unfinished.
- The evidence must concern the target task rather than preparation for it.
- Partial or ongoing execution is sufficient.

### General boundary requirements

- The two states must remain mutually exclusive.
- The examples must represent the B01 initiation boundary rather than the B02 completion boundary.
- Task identity must not determine the execution status.
- Reasons, motivation, sentiment, or conversational purpose must not determine the label.
- The examples must remain compatible with the frozen three-state lifecycle.

## 8. Boundary Invariant

```text
Preparation / intention / non-execution
                ↓
          Not Started
                │
                │ execution actually begins
                ▼
          In Progress
                │
                │ execution remains unfinished
                ▼
            Completed
```

For B01, only the transition from **no execution** to **actual execution begun** is relevant. Completion is outside this boundary.