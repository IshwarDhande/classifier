# Execution Status Dataset — Stage 1 Semantic Scenarios: In Progress

## 1. Purpose

This document defines the Stage 1 semantic scenario inventory for the frozen Execution Status state:

> **In Progress**

The scenarios represent situations in which execution of the target task **has begun but has not yet finished**.

The production label remains:

```yaml
execution_status: In Progress
```

The scenario inventory is designed to provide semantic coverage before linguistic expansion, boundary construction, and hard-negative generation.

---

# 2. Stage 1 Construction Principle

The central condition for every `In Progress` scenario is:

```text
execution_started = true
execution_completed = false
```

The wording may vary substantially, but the underlying execution event must remain unchanged.

The scenarios must distinguish:

- active execution;
- partial execution;
- near completion;
- multi-step execution;
- temporarily interrupted execution.

They must not introduce additional production states for these distinctions.

---

# 3. Working Scenario Target

The working Stage 1 target is:

| Item | Target |
|---|---:|
| In Progress subtypes | 5 |
| Scenarios per subtype | 3 |
| Total semantic scenarios | **15** |
| Initial anchors per scenario | 3 |
| Initial anchor capacity | **45** |

The 15 scenarios below form the working semantic inventory.

The target is a construction planning number rather than a requirement to manufacture artificial semantic distinctions.

---

# 4. Scenario Metadata

Each scenario should carry:

```yaml
scenario_id:
state:
subtype_id:
scenario_name:
scenario_definition:
execution_condition:
target_task:
task_domain:
semantic_dimensions:
boundary_risk:
construction_notes:
```

Generated anchors should additionally retain:

```yaml
utterance:
execution_status: In Progress
scenario_id:
anchor_type:
```

---

# 5. IP-01 — Direct Ongoing Execution

## Scenario IP-S01 — Explicit Current Execution

### Subtype

`IP-01 Direct Ongoing Execution`

### Scenario definition

The user explicitly indicates that they are currently performing the target task.

### Execution condition

```text
execution_started = true
execution_completed = false
```

### Core semantic meaning

Execution is currently underway.

### Task-domain instantiations

- Medication: currently taking the dose.
- Hydration: currently drinking water.
- Exercise: currently exercising.
- Physiotherapy: currently performing the routine.

### Primary boundary

`Not Started ↔ In Progress`

### Secondary boundary

`In Progress ↔ Completed`

### Example semantic realizations

- “I’m taking it now.”
- “I’m doing the exercises.”
- “I’m doing the physiotherapy routine now.”

### Construction constraint

The utterance must provide actual execution evidence, not merely an intention to begin.

---

## Scenario IP-S02 — Active Performance

### Subtype

`IP-01 Direct Ongoing Execution`

### Scenario definition

The user describes an active execution event without necessarily using an explicit “doing” construction.

### Execution condition

```text
execution_started = true
execution_completed = false
```

### Core semantic meaning

The target task is actively being performed.

### Boundary risk

Natural conversational wording may omit explicit state markers.

### Example semantic realizations

- “I’m on the treadmill right now.”
- “I’m drinking the water.”
- “I’m doing the stretches.”

### Construction constraint

The activity must correspond to the target task rather than preparation for it.

---

## Scenario IP-S03 — Current Execution With Context

### Subtype

`IP-01 Direct Ongoing Execution`

### Scenario definition

The user establishes current execution through a short conversational context.

### Execution condition

```text
execution_started = true
execution_completed = false
```

### Core semantic meaning

The latest utterance, interpreted with the immediate context, establishes that execution is underway.

### Boundary risk

The dataset must distinguish contextual execution evidence from future intention.

### Example semantic realizations

- “Yes, I’m doing it now.”
- “I’ve started already.”
- “I’m in the middle of it.”

### Construction constraint

Context may clarify the execution event, but should not introduce unrelated reasoning.

---

# 6. IP-02 — Partial Execution

## Scenario IP-S04 — Partially Completed Task

### Subtype

`IP-02 Partial Execution`

### Scenario definition

The user has performed part of the target task, but the full task remains unfinished.

### Execution condition

```text
execution_started = true
execution_completed = false
```

with:

```text
completed_portion > 0
remaining_portion > 0
```

### Core semantic meaning

Some execution has occurred, but completion has not.

### Primary boundary

`Not Started ↔ In Progress`

### Secondary boundary

`In Progress ↔ Completed`

### Example semantic realizations

- “I’ve done part of the exercise.”
- “I’ve started drinking it, but there’s still some left.”
- “I’ve taken part of it, but I’m not finished.”

### Construction constraint

The utterance must establish both initiation and remaining work.

---

## Scenario IP-S05 — Partial Quantity / Portion

### Subtype

`IP-02 Partial Execution`

### Scenario definition

A measurable portion of the task has been executed while some required amount remains.

### Execution condition

```text
execution_started = true
execution_completed = false
```

### Core semantic meaning

The user has completed a non-zero portion but not the entire target.

### Boundary risk

Quantity language must not be mistaken for completion.

### Example semantic realizations

- “I drank half the bottle.”
- “I’ve finished two of the five sets.”
- “I’ve done the first part of the routine.”

### Construction constraint

The remaining requirement must remain semantically clear.

---

## Scenario IP-S06 — Started but Not Finished

### Subtype

`IP-02 Partial Execution`

### Scenario definition

The user explicitly reports that execution began but remains unfinished.

### Execution condition

```text
execution_started = true
execution_completed = false
```

### Core semantic meaning

The execution lifecycle has moved beyond initiation but has not reached completion.

### Example semantic realizations

- “I started it, but I haven’t finished.”
- “I’ve begun the exercise, but I still have more to do.”
- “I took the first part, but I’m not done yet.”

### Construction constraint

This scenario is a semantic center for the `Not Started ↔ In Progress` boundary.

---

# 7. IP-03 — Near Completion

## Scenario IP-S07 — Almost Finished

### Subtype

`IP-03 Near Completion`

### Scenario definition

The user has nearly completed the task but explicitly indicates that some execution remains.

### Execution condition

```text
execution_started = true
execution_completed = false
remaining_work > 0
```

### Core semantic meaning

Execution is close to completion but incomplete.

### Primary boundary

`In Progress ↔ Completed`

### Example semantic realizations

- “I’m almost done.”
- “I’m nearly finished.”
- “I only have a little left.”

### Construction constraint

“Almost” must not be converted into completion.

---

## Scenario IP-S08 — Final Remaining Step

### Subtype

`IP-03 Near Completion`

### Scenario definition

The user has completed nearly all execution and has one or a small number of final execution steps remaining.

### Execution condition

```text
execution_started = true
execution_completed = false
```

### Core semantic meaning

The execution state remains unfinished despite minimal remaining work.

### Example semantic realizations

- “I’ve just got one set left.”
- “I only need to finish the last part.”
- “One more step and I’m done.”

### Construction constraint

The final step must not already be completed.

---

## Scenario IP-S09 — Nearly Complete With Commentary

### Subtype

`IP-03 Near Completion`

### Scenario definition

The user indicates near completion while adding contextual or evaluative commentary.

### Execution condition

```text
execution_started = true
execution_completed = false
```

### Core semantic meaning

Near completion remains the execution signal despite additional content.

### Example semantic realizations

- “I’m almost finished; it took longer than I expected.”
- “Just one more exercise and I’m done.”
- “I’m nearly through the routine, but it’s tiring.”

### Construction constraint

Additional commentary must not change the execution state.

---

# 8. IP-04 — Multi-Step Execution

## Scenario IP-S10 — Multiple Steps Partially Executed

### Subtype

`IP-04 Multi-Step Execution`

### Scenario definition

The target task consists of multiple execution steps, some of which have been completed while others remain.

### Execution condition

```text
execution_started = true
execution_completed = false
```

with:

```text
completed_steps < total_required_steps
```

### Core semantic meaning

The execution sequence is underway but incomplete.

### Primary boundary

`In Progress ↔ Completed`

### Example semantic realizations

- “I finished the first two exercises and still have one left.”
- “I’ve completed the first part of the routine.”
- “I’ve taken the first dose but still have the next step.”

### Construction constraint

The remaining step(s) must be semantically required for completion.

---

## Scenario IP-S11 — Sequential Execution Underway

### Subtype

`IP-04 Multi-Step Execution`

### Scenario definition

The user is progressing through a sequence of required execution steps.

### Execution condition

```text
execution_started = true
execution_completed = false
```

### Core semantic meaning

The task is being executed as a sequence, but the sequence has not ended.

### Example semantic realizations

- “I’m on the third exercise.”
- “I’m working through the routine.”
- “I’ve started the steps and I’m still going through them.”

### Construction constraint

The sequence must represent execution rather than planning.

---

## Scenario IP-S12 — Multi-Step Execution With Remaining Work

### Subtype

`IP-04 Multi-Step Execution`

### Scenario definition

The user explicitly identifies completed steps and remaining steps.

### Execution condition

```text
execution_started = true
execution_completed = false
```

### Core semantic meaning

Execution is demonstrably underway because at least one required step has occurred, while at least one remains.

### Example semantic realizations

- “I’ve done three sets; two more are left.”
- “I completed the first part and still need to do the rest.”
- “I’ve started the routine; there are still a few steps left.”

### Construction constraint

This scenario should be useful later for robust `In Progress ↔ Completed` boundary construction.

---

# 9. IP-05 — Temporarily Interrupted Execution

## Scenario IP-S13 — Execution Paused After Starting

### Subtype

`IP-05 Temporarily Interrupted Execution`

### Scenario definition

The user began executing the task and then temporarily paused before completion.

### Execution condition

```text
execution_started = true
execution_completed = false
```

with:

```text
interruption_after_start = true
```

### Core semantic meaning

Execution has entered the lifecycle and remains unfinished despite a temporary pause.

### Primary boundary

`Not Started ↔ In Progress`

### Secondary boundary

`In Progress ↔ Completed`

### Example semantic realizations

- “I started the exercise but paused.”
- “I was doing it, but I had to stop for a moment.”
- “I began the routine and took a short break.”

### Construction constraint

The pause must occur **after** execution begins.

---

## Scenario IP-S14 — Interrupted With Remaining Work

### Subtype

`IP-05 Temporarily Interrupted Execution`

### Scenario definition

The user started execution, was interrupted, and explicitly indicates that unfinished work remains.

### Execution condition

```text
execution_started = true
execution_completed = false
```

### Core semantic meaning

Execution remains in progress at the lifecycle level even though activity is temporarily paused.

### Example semantic realizations

- “I started the exercises but got interrupted; I still have some left.”
- “I was taking it when something came up, so I haven’t finished.”
- “I began the routine but had to stop before completing it.”

### Construction constraint

The interruption must not be interpreted as cancellation before execution.

---

## Scenario IP-S15 — Resumable Interrupted Execution

### Subtype

`IP-05 Temporarily Interrupted Execution`

### Scenario definition

The user began the target task, temporarily stopped, and indicates that execution remains unfinished and can continue.

### Execution condition

```text
execution_started = true
execution_completed = false
```

### Core semantic meaning

The execution lifecycle remains between initiation and completion.

### Example semantic realizations

- “I started it and will continue after this break.”
- “I’m halfway through; I’ll finish the rest in a bit.”
- “I paused the routine and still need to complete it.”

### Construction constraint

The future continuation must not obscure the fact that execution has already begun.

---

# 10. Scenario Coverage Matrix

| Scenario | Subtype | Core semantic region | Primary boundary |
|---|---|---|---|
| IP-S01 | IP-01 | Explicit current execution | NS ↔ IP |
| IP-S02 | IP-01 | Active performance | NS ↔ IP |
| IP-S03 | IP-01 | Contextual current execution | NS ↔ IP |
| IP-S04 | IP-02 | Partial task execution | NS ↔ IP |
| IP-S05 | IP-02 | Partial quantity/portion | NS ↔ IP |
| IP-S06 | IP-02 | Started but unfinished | NS ↔ IP |
| IP-S07 | IP-03 | Almost finished | IP ↔ C |
| IP-S08 | IP-03 | Final remaining step | IP ↔ C |
| IP-S09 | IP-03 | Near completion + commentary | IP ↔ C |
| IP-S10 | IP-04 | Multi-step partial execution | IP ↔ C |
| IP-S11 | IP-04 | Sequential execution | IP ↔ C |
| IP-S12 | IP-04 | Completed + remaining steps | IP ↔ C |
| IP-S13 | IP-05 | Paused after initiation | NS ↔ IP |
| IP-S14 | IP-05 | Interrupted + unfinished | NS ↔ IP |
| IP-S15 | IP-05 | Resumable interruption | NS ↔ IP |

---

# 11. Task-Domain Coverage

The semantic scenarios should be instantiated across the frozen task domains:

1. Medication
2. Hydration
3. Exercise
4. Physiotherapy

The domain should vary independently from the execution subtype.

For example:

| Semantic region | Possible domains |
|---|---|
| Direct ongoing | Medication, hydration, exercise, physiotherapy |
| Partial execution | Medication, hydration, exercise, physiotherapy |
| Near completion | Medication, hydration, exercise, physiotherapy |
| Multi-step execution | Medication, exercise, physiotherapy |
| Temporary interruption | Hydration, exercise, physiotherapy |

The examples above are illustrative allocations. The final anchor set should rotate domains rather than repeatedly pairing one subtype with one task.

---

# 12. Critical Semantic Distinctions

## 12.1 Future intention vs ongoing execution

```text
“I’ll exercise later.”
→ Not Started

“I’m exercising now.”
→ In Progress
```

The first describes future action; the second establishes actual execution.

---

## 12.2 Preparation vs execution

Preparation must not automatically be treated as task execution.

For example:

> “I’m getting ready to exercise.”

may or may not constitute execution depending on the frozen task definition and context. Scenario construction should avoid such ambiguous cases unless they are intentionally reserved for later boundary analysis.

---

## 12.3 Partial execution vs completion

```text
“I’ve done three of five sets.”
→ In Progress

“I’ve done all five sets.”
→ Completed
```

The amount completed is not sufficient by itself; the relevant question is whether all required execution is finished.

---

## 12.4 Near completion vs completion

```text
“I’m almost done.”
→ In Progress

“I’m done.”
→ Completed
```

Near completion is explicitly retained as `In Progress`.

---

## 12.5 Interruption after initiation vs non-execution

```text
“I haven’t started because I was busy.”
→ Not Started

“I started, but I had to stop because I was busy.”
→ In Progress
```

The decisive feature is whether execution began.

---

## 12.6 Interrupted execution vs completed execution

```text
“I started but had to stop.”
→ In Progress

“I finished before stopping.”
→ Completed
```

An interruption does not imply completion.

---

# 13. Scenario Construction Constraints

Every In Progress scenario must satisfy:

### 13.1 Execution has begun

There must be evidence of actual task execution.

### 13.2 Completion has not occurred

The complete target task must remain unfinished.

### 13.3 Partial execution is sufficient

The task does not need to be near completion to qualify.

### 13.4 Near completion remains In Progress

Minimal remaining work does not change the label.

### 13.5 Interruption does not reset state

Once execution begins, a temporary pause remains within the `In Progress` semantic region until completion.

### 13.6 Future continuation does not change the current state

“I’ll finish later” can still be `In Progress` when the utterance establishes that execution already began.

### 13.7 Reasons remain orthogonal

Busy, tired, interrupted, distracted, or unavailable may explain why execution is incomplete, but they do not replace the execution state.

### 13.8 Planning is not execution

Planning future steps without evidence of execution remains `Not Started`.

---

# 14. Lexical Shortcut Prevention

The dataset must not learn simplistic mappings such as:

- “doing” → `In Progress`;
- “started” → `In Progress`;
- “almost” → `In Progress`;
- “left” → `In Progress`;
- “pause” → `In Progress`.

The same words can occur in different semantic contexts.

For example:

> “I’m going to start exercising later.”

contains “start” but is `Not Started`.

Similarly:

> “I finished the exercise after pausing.”

contains “pause” but is `Completed`.

The semantic execution condition is authoritative.

---

# 15. Conversational Context

Some scenarios should be expressible in short dialogue context.

Context may establish:

- which task is being discussed;
- whether an action has already begun;
- whether a remaining step exists;
- whether an interruption occurred after initiation.

However, context must not be used to manufacture execution evidence that is absent from the intended semantic scenario.

The target remains the user's current execution state.

---

# 16. Initial Anchor Construction

Each scenario should receive three initial anchors:

### Anchor A — Explicit Prototype

Directly expresses that execution is underway and unfinished.

### Anchor B — Natural Prototype

Expresses the same execution state using natural conversational language.

### Anchor C — Less Explicit / Contextual Prototype

Requires modest semantic interpretation while preserving a clear execution state.

All three must preserve:

```yaml
execution_started: true
execution_completed: false
execution_status: In Progress
```

No anchor should intentionally cross into `Not Started` or `Completed`.

---

# 17. Boundary-Oriented Scenario Distribution

The 15 scenarios deliberately cover both major boundaries involving `In Progress`.

### Not Started ↔ In Progress

Emphasis:

- actual initiation;
- partial execution;
- interruption after initiation.

Primary scenarios:

```text
IP-S01
IP-S02
IP-S03
IP-S04
IP-S05
IP-S06
IP-S13
IP-S14
IP-S15
```

### In Progress ↔ Completed

Emphasis:

- remaining work;
- near completion;
- incomplete multi-step execution;
- interruption before completion.

Primary scenarios:

```text
IP-S07
IP-S08
IP-S09
IP-S10
IP-S11
IP-S12
IP-S14
IP-S15
```

The overlap is intentional because both boundaries must be represented from the In Progress side.

---

# 18. Scenario Deduplication

Scenarios should not be separated merely because the wording differs.

For example:

- “I’m doing it now.”
- “I’m currently doing it.”
- “I’m in the middle of it.”

represent the same semantic region and should normally be handled as linguistic variation of a common scenario.

A separate scenario is justified when the execution semantics change, such as:

- direct ongoing execution;
- partial execution;
- near completion;
- multi-step execution;
- interrupted execution.

---

# 19. Scenario Leakage Prevention

Every utterance generated later must retain its semantic lineage:

```text
In Progress
    ↓
Subtype
    ↓
Scenario
    ↓
Anchor
    ↓
Variant
```

Descendants of the same semantic scenario must be identifiable for later group-based dataset splitting.

A linguistic paraphrase of an In Progress scenario must not be treated as an independent semantic scenario.

---

# 20. Human–LLM–Code Allocation

## Human

Humans determine:

- whether execution genuinely began;
- whether completion genuinely has not occurred;
- whether the scenario is semantically distinct;
- whether a boundary is correctly represented.

## LLM

LLMs may assist with:

- natural conversational realizations;
- paraphrasing;
- linguistic diversity;
- contextually varied expressions.

LLMs must preserve the predefined execution semantics.

## Code

Code should verify:

- metadata completeness;
- subtype/state consistency;
- scenario identifiers;
- anchor counts;
- duplicates;
- lineage;
- later split grouping.

---

# 21. Stage 1 Completion Criteria for In Progress

The scenario inventory is ready for anchor construction when:

- all five In Progress subtypes are represented;
- all 15 working scenarios have explicit semantic definitions;
- every scenario satisfies `execution_started = true`;
- every scenario satisfies `execution_completed = false`;
- direct ongoing execution is covered;
- partial execution is covered;
- near completion is covered;
- multi-step execution is covered;
- temporary interruption after initiation is covered;
- the `Not Started ↔ In Progress` boundary is represented;
- the `In Progress ↔ Completed` boundary is represented;
- task domains are distributed across scenarios;
- scenarios do not depend on lexical shortcuts;
- preparation and intention are not incorrectly treated as execution;
- no scenario creates an additional production label.

---

# 22. Stage 1 Output

This file defines:

```text
5 working subtypes
15 semantic scenarios
3 initial anchors per scenario
45 initial anchor slots
```

The next construction resource is:

```text
s1/anchors/02_initial_anchors_in_progress.md
```

That file should realize these 15 semantic scenarios into three initial anchors per scenario while preserving the execution invariants.

---

# 23. Final Principle

**An In Progress scenario is valid only when execution has begun and completion has not yet occurred.**

The amount completed, remaining work, number of steps, temporary interruption, and degree of completion may differ substantially, but these distinctions remain within the same production state whenever the task is unfinished.

The Stage 1 objective is therefore:

> **Construct a semantically complete inventory of unfinished execution situations before introducing broad linguistic variation.**
