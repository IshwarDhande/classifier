# Stage 2B — Minimal Pairs
## MP01: Not Started ↔ In Progress

### 1. Boundary Definition

**Boundary ID:** B01  
**State A:** Not Started  
**State B:** In Progress

This minimal-pair resource isolates the transition from **no execution begun** to **execution begun but unfinished**.

The paired utterances should preserve the same underlying task and practical context as far as natural language permits. The decisive change is the evidence about whether task execution has actually started.

### 2. Minimal-Pair Construction Principle

A valid B01 minimal pair satisfies:

```text
Same task/context
        +
minimal semantic change
        ↓
execution-state evidence changes
        ↓
Not Started ↔ In Progress
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
> **In Progress:** execution has begun but is unfinished.

### 3. Minimal-Pair Families

The following six families provide complementary realizations of the B01 boundary.

---

#### MP01-01 — Direct Initiation Evidence

**Target Task:** Medication

**Not Started:**
> I haven't started taking the medication yet.

**In Progress:**
> I've started taking the medication, but I'm not finished yet.

**Decisive change:** explicit absence versus presence of execution initiation.

---

#### MP01-02 — Current Execution Evidence

**Target Task:** Hydration

**Not Started:**
> The water is still sitting there; I haven't started drinking it.

**In Progress:**
> I'm drinking the water now, and I haven't finished it.

**Decisive change:** untouched task versus active execution.

---

#### MP01-03 — Partial Execution Evidence

**Target Task:** Exercise

**Not Started:**
> I haven't done any of the exercises yet.

**In Progress:**
> I've done the first exercise and still have the others to do.

**Decisive change:** zero execution versus partial execution.

---

#### MP01-04 — Preparation Versus Execution

**Target Task:** Physiotherapy

**Not Started:**
> I've got the physiotherapy equipment ready, but I haven't begun.

**In Progress:**
> I've started the physiotherapy routine with the equipment, but I'm not done.

**Decisive change:** preparation without execution versus actual execution with remaining work.

---

#### MP01-05 — First-Step Boundary

**Target Task:** Medication

**Not Started:**
> I'm about to take the first step, but I haven't started yet.

**In Progress:**
> I've taken the first step, but there's more of the task left.

**Decisive change:** intended initiation versus actual initiation.

---

#### MP01-06 — Indirect Execution Evidence

**Target Task:** Physiotherapy

**Not Started:**
> The routine is still untouched.

**In Progress:**
> I'm halfway through the routine.

**Decisive change:** absence of execution evidence versus evidence of ongoing partial execution.

### 4. Production Records

```yaml
- example_id: MP01-01-A
  pair_id: MP01-01
  parent_id: null
  lineage_id: MP01-01
  execution_status: Not Started
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B01
  anchor_type: null
  context: "Medication execution has not begun."
  utterance: "I haven't started taking the medication yet."
  target_task: medication
  closest_competing_state: In Progress
  variation_type: execution_initiation
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP01-01-B
  pair_id: MP01-01
  parent_id: null
  lineage_id: MP01-01
  execution_status: In Progress
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B01
  anchor_type: null
  context: "Medication execution has begun but is unfinished."
  utterance: "I've started taking the medication, but I'm not finished yet."
  target_task: medication
  closest_competing_state: Not Started
  variation_type: execution_initiation
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP01-02-A
  pair_id: MP01-02
  parent_id: null
  lineage_id: MP01-02
  execution_status: Not Started
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B01
  anchor_type: null
  context: "The target hydration task has not begun."
  utterance: "The water is still sitting there; I haven't started drinking it."
  target_task: hydration
  closest_competing_state: In Progress
  variation_type: current_execution
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP01-02-B
  pair_id: MP01-02
  parent_id: null
  lineage_id: MP01-02
  execution_status: In Progress
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B01
  anchor_type: null
  context: "The target hydration task is underway but unfinished."
  utterance: "I'm drinking the water now, and I haven't finished it."
  target_task: hydration
  closest_competing_state: Not Started
  variation_type: current_execution
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP01-03-A
  pair_id: MP01-03
  parent_id: null
  lineage_id: MP01-03
  execution_status: Not Started
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B01
  anchor_type: null
  context: "No exercise execution has begun."
  utterance: "I haven't done any of the exercises yet."
  target_task: exercise
  closest_competing_state: In Progress
  variation_type: partial_execution
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP01-03-B
  pair_id: MP01-03
  parent_id: null
  lineage_id: MP01-03
  execution_status: In Progress
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B01
  anchor_type: null
  context: "Exercise execution has begun but remains unfinished."
  utterance: "I've done the first exercise and still have the others to do."
  target_task: exercise
  closest_competing_state: Not Started
  variation_type: partial_execution
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP01-04-A
  pair_id: MP01-04
  parent_id: null
  lineage_id: MP01-04
  execution_status: Not Started
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B01
  anchor_type: null
  context: "Physiotherapy equipment is prepared but execution has not begun."
  utterance: "I've got the physiotherapy equipment ready, but I haven't begun."
  target_task: physiotherapy
  closest_competing_state: In Progress
  variation_type: preparation_vs_execution
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP01-04-B
  pair_id: MP01-04
  parent_id: null
  lineage_id: MP01-04
  execution_status: In Progress
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B01
  anchor_type: null
  context: "Physiotherapy execution has begun but is unfinished."
  utterance: "I've started the physiotherapy routine with the equipment, but I'm not done."
  target_task: physiotherapy
  closest_competing_state: Not Started
  variation_type: preparation_vs_execution
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP01-05-A
  pair_id: MP01-05
  parent_id: null
  lineage_id: MP01-05
  execution_status: Not Started
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B01
  anchor_type: null
  context: "Medication execution is intended but has not begun."
  utterance: "I'm about to take the first step, but I haven't started yet."
  target_task: medication
  closest_competing_state: In Progress
  variation_type: first_step_boundary
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP01-05-B
  pair_id: MP01-05
  parent_id: null
  lineage_id: MP01-05
  execution_status: In Progress
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B01
  anchor_type: null
  context: "Medication execution has begun with a first completed step, but remains unfinished."
  utterance: "I've taken the first step, but there's more of the task left."
  target_task: medication
  closest_competing_state: Not Started
  variation_type: first_step_boundary
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP01-06-A
  pair_id: MP01-06
  parent_id: null
  lineage_id: MP01-06
  execution_status: Not Started
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B01
  anchor_type: null
  context: "The physiotherapy routine has not been initiated."
  utterance: "The routine is still untouched."
  target_task: physiotherapy
  closest_competing_state: In Progress
  variation_type: indirect_execution_evidence
  source: constructed
  validation_status: candidate
  ambiguity_flag: false

- example_id: MP01-06-B
  pair_id: MP01-06
  parent_id: null
  lineage_id: MP01-06
  execution_status: In Progress
  semantic_subtype: minimal_pair
  stage: 2B
  resource_type: minimal_pair
  boundary_id: B01
  anchor_type: null
  context: "The physiotherapy routine is partially complete and remains unfinished."
  utterance: "I'm halfway through the routine."
  target_task: physiotherapy
  closest_competing_state: Not Started
  variation_type: indirect_execution_evidence
  source: constructed
  validation_status: candidate
  ambiguity_flag: false
```

### 5. Pair-Level Diagnostic Rationale

| Pair | Not Started evidence | In Progress evidence |
|---|---|---|
| MP01-01 | Execution has not begun | Execution has begun and remains unfinished |
| MP01-02 | Target remains untouched | Active execution is occurring |
| MP01-03 | No exercise has been performed | At least one exercise has been performed |
| MP01-04 | Equipment preparation only | Actual physiotherapy execution has begun |
| MP01-05 | Initiation is only anticipated | A first execution step has occurred |
| MP01-06 | No execution is implied | Partial execution is implied |

Each pair changes the execution evidence while preserving the target task and the underlying decision boundary.

### 6. Minimal-Pair Validation Criteria

A pair is valid only if:

1. Both utterances refer to the same target task.
2. Both utterances represent the same broad practical situation where natural.
3. The labels differ only because of execution-state evidence.
4. The Not Started member contains no evidence that execution has begun.
5. The In Progress member contains evidence that execution has begun.
6. The In Progress member does not imply completion.
7. Preparation is not treated as execution.
8. Future intention or imminent action is not treated as execution.
9. The distinction does not depend on persuasion barriers, motivation, dialogue purpose, or sentiment.
10. The pair remains natural conversational language.
11. Neither member requires external scheduling or task-manager reasoning.
12. The pair does not create a lexical shortcut that makes the state distinction trivial across the dataset.

### 7. Boundary Invariant

For MP01:

> **Change only the evidence of execution initiation.**

The Not Started member must establish that execution has not begun. The In Progress member must establish that execution has begun while remaining unfinished. No other semantic dimension should be responsible for the label change.
