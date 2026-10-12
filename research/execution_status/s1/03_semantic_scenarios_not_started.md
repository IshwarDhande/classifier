# Execution Status Dataset — Stage 1 Semantic Scenarios: Not Started

## 1. Purpose

This document defines the Stage 1 semantic scenario inventory for the frozen Execution Status state:

> **Not Started**

The scenarios are construction artifacts used to ensure broad semantic coverage before linguistic expansion, boundary construction, and hard-negative generation.

The production label remains:

```yaml
execution_status: Not Started
```

The scenarios must represent cases in which the target task **has not begun**.

---

# 2. Stage 1 Construction Principle

A scenario is defined semantically before any final natural-language realization is written.

The construction process is:

```text
Semantic subtype
      ↓
Execution condition
      ↓
Scenario meaning
      ↓
Task-domain instantiation
      ↓
Initial natural-language anchors
      ↓
Later linguistic expansion
```

The scenario inventory must therefore avoid:

- keyword-based construction;
- paraphrase-only variation;
- premature minimal pairs;
- hard negatives;
- response-category assumptions;
- persuasion-barrier labels as execution states;
- scheduling/task-manager labels.

---

# 3. State Definition

## Not Started

The target task has **not begun**.

This includes semantically distinct situations such as:

- direct non-execution;
- future or deferred execution;
- conditional future execution;
- refusal without execution;
- reason-linked non-execution.

These are all mapped to the same production state because none provides evidence that execution has begun.

### Decision rule

```text
Completed?
    NO
     ↓
Execution started?
    NO
     ↓
Not Started
```

---

# 4. Working Scenario Target

The working Stage 1 target is:

| Item | Target |
|---|---:|
| Not Started subtypes | 5 |
| Scenarios per subtype | 3 |
| Total semantic scenarios | **15** |
| Initial anchors per scenario | 3 |
| Initial anchor capacity | **45** |

The 15 scenarios below form the **minimum working inventory** for Stage 1 construction.

The inventory should be expanded only if semantic coverage review identifies a genuine uncovered execution region. Additional scenarios must not be added merely to increase dataset size.

---

# 5. Scenario Metadata

Each scenario should carry the following construction metadata:

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

The final utterance generated from a scenario should additionally carry:

```yaml
utterance:
execution_status: Not Started
scenario_id:
anchor_type:
```

---

# 6. NS-01 — Direct Non-Execution

## Scenario NS-S01 — Task Not Yet Started

### Subtype

`NS-01 Direct Non-Execution`

### Scenario definition

The user explicitly states that the target task has not been started.

### Execution condition

```text
execution_started = false
execution_completed = false
```

### Core semantic meaning

No execution activity has occurred.

### Task-domain instantiations

- Medication: prescribed dose has not been taken.
- Hydration: planned water intake has not begun.
- Exercise: exercise session has not begun.
- Physiotherapy: therapy routine has not begun.

### Boundary risk

Primary boundary:

`Not Started ↔ In Progress`

The scenario must not contain evidence that even partial execution has begun.

### Example semantic realizations

- “I haven’t started the exercise yet.”
- “I haven’t taken the dose.”
- “I haven’t begun the routine.”

### Construction constraint

The wording must establish non-execution rather than merely lack of completion.

---

## Scenario NS-S02 — Task Remains Untouched

### Subtype

`NS-01 Direct Non-Execution`

### Scenario definition

The target task remains completely untouched at the current point in time.

### Execution condition

```text
execution_started = false
```

### Core semantic meaning

There has been no execution activity.

### Task-domain instantiations

- Medication: dose remains untaken.
- Hydration: no water has been consumed toward the target.
- Exercise: no exercise activity has been performed.
- Physiotherapy: no therapy activity has been performed.

### Boundary risk

`Not Started ↔ In Progress`

The scenario must distinguish “nothing has been done” from “some of it has been done.”

### Example semantic realizations

- “I haven’t done anything for the exercise yet.”
- “I haven’t taken any of it.”
- “I haven’t started the physiotherapy routine.”

### Construction constraint

Avoid language that implies a task component was already performed.

---

## Scenario NS-S03 — Current Non-Execution

### Subtype

`NS-01 Direct Non-Execution`

### Scenario definition

The user indicates that they are currently not performing the target task, without necessarily giving a future commitment or reason.

### Execution condition

```text
execution_started = false
```

### Core semantic meaning

The target task is not currently being executed.

### Task-domain instantiations

- Medication: currently not taking the dose.
- Hydration: currently not drinking.
- Exercise: currently not exercising.
- Physiotherapy: currently not performing the routine.

### Boundary risk

Potential confusion with `In Progress` when negative wording is weak or ambiguous.

### Example semantic realizations

- “I’m not doing it right now.”
- “I’m not taking it right now.”
- “I’m not exercising at the moment.”

### Construction constraint

The semantic interpretation must remain that execution has not begun for the target task.

---

# 7. NS-02 — Future / Deferred Action

## Scenario NS-S04 — Straightforward Future Action

### Subtype

`NS-02 Future / Deferred Action`

### Scenario definition

The user has not started execution and states that the task will be performed later.

### Execution condition

```text
execution_started = false
```

### Core semantic meaning

Future execution is intended, but current execution has not begun.

### Boundary risk

`Not Started ↔ In Progress`

### Example semantic realizations

- “I’ll do the exercise later.”
- “I’ll take the medicine tonight.”
- “I’ll do the physiotherapy routine later.”

### Construction constraint

Future intention must not be treated as execution initiation.

---

## Scenario NS-S05 — Deferred Start

### Subtype

`NS-02 Future / Deferred Action`

### Scenario definition

The user indicates that execution has not begun and that the start will occur at a later point.

### Execution condition

```text
execution_started = false
```

### Core semantic meaning

The start itself is deferred.

### Boundary risk

Distinguish from an ongoing task that is temporarily paused.

### Example semantic realizations

- “I haven’t started yet; I’ll do it after lunch.”
- “I’ll start the exercises this evening.”
- “I’ll take the dose when I get back.”

### Construction constraint

The utterance must not imply that execution already began before the deferral.

---

## Scenario NS-S06 — Later Completion Intention

### Subtype

`NS-02 Future / Deferred Action`

### Scenario definition

The user describes a future completion event while providing no evidence of current execution.

### Execution condition

```text
execution_started = false
execution_completed = false
```

### Core semantic meaning

The task remains unstarted despite a future-oriented commitment.

### Boundary risk

Future language can contain strong commitment cues while still being `Not Started`.

### Example semantic realizations

- “I’ll finish the routine tonight.”
- “I’m going to take the dose later.”
- “I’ll get the exercise done this evening.”

### Construction constraint

Do not infer current execution from confidence or strength of intention.

---

# 8. NS-03 — Conditional Future Action

## Scenario NS-S07 — Condition-Dependent Start

### Subtype

`NS-03 Conditional Future Action`

### Scenario definition

The user has not started execution and will begin only if a stated condition is satisfied.

### Execution condition

```text
execution_started = false
```

### Core semantic meaning

Execution is contingent on a future condition.

### Boundary risk

Distinguish conditional intention from current execution.

### Example semantic realizations

- “If I get time, I’ll exercise.”
- “If I’m free later, I’ll take the dose.”
- “If I get home early, I’ll do the therapy routine.”

### Construction constraint

The condition must not be interpreted as already satisfied.

---

## Scenario NS-S08 — Event-Triggered Future Start

### Subtype

`NS-03 Conditional Future Action`

### Scenario definition

Execution will begin after another event occurs.

### Execution condition

```text
execution_started = false
```

### Core semantic meaning

The target task remains unstarted until a future event occurs.

### Boundary risk

Distinguish “after X” as a future trigger from an execution sequence that has already begun.

### Example semantic realizations

- “Once I finish work, I’ll exercise.”
- “After dinner, I’ll take it.”
- “When I get home, I’ll do the physiotherapy.”

### Construction constraint

The triggering event must remain future or unresolved.

---

## Scenario NS-S09 — Conditional Availability

### Subtype

`NS-03 Conditional Future Action`

### Scenario definition

The user will execute the target task if the necessary opportunity or condition becomes available.

### Execution condition

```text
execution_started = false
```

### Core semantic meaning

No execution has started; future execution depends on availability.

### Boundary risk

May resemble reason-linked non-execution. The defining feature here is the explicit future conditional execution.

### Example semantic realizations

- “If I have enough time, I’ll do it.”
- “If I can get a break, I’ll exercise.”
- “If I’m able to later, I’ll take it.”

### Construction constraint

The utterance should preserve conditional future execution as the primary semantic structure.

---

# 9. NS-04 — Refusal Without Execution

## Scenario NS-S10 — Direct Refusal

### Subtype

`NS-04 Refusal Without Execution`

### Scenario definition

The user explicitly refuses to perform the target task and has not started it.

### Execution condition

```text
execution_started = false
```

### Core semantic meaning

The task has not begun because the user declines execution.

### Boundary risk

Refusal is not a separate execution state.

### Example semantic realizations

- “No, I’m not going to do it.”
- “I won’t take it.”
- “I’m not doing the exercise.”

### Construction constraint

The refusal must not contain evidence that execution has already begun.

---

## Scenario NS-S11 — Rejection of the Task

### Subtype

`NS-04 Refusal Without Execution`

### Scenario definition

The user rejects the proposed task or declines to carry it out.

### Execution condition

```text
execution_started = false
```

### Core semantic meaning

No execution has occurred.

### Boundary risk

Distinguish rejection from a temporary pause after execution.

### Example semantic realizations

- “I’m skipping the exercise.”
- “I’m not going to take that dose.”
- “I don’t want to do the routine.”

### Construction constraint

“Skipping” here refers to non-execution; the dataset must not turn the task-manager-derived status `Skipped` into an Execution Status label.

---

## Scenario NS-S12 — Refusal Without Explicit Reason

### Subtype

`NS-04 Refusal Without Execution`

### Scenario definition

The user clearly declines the task without providing a reason.

### Execution condition

```text
execution_started = false
```

### Core semantic meaning

The task remains unstarted.

### Boundary risk

Distinguish refusal from neutral current non-execution.

### Example semantic realizations

- “No, I won’t.”
- “I’m not doing that.”
- “I’ll pass on it.”

### Construction constraint

The utterance should communicate refusal rather than merely absence of action.

---

# 10. NS-05 — Reason-Linked Non-Execution

## Scenario NS-S13 — Non-Execution Due to Time Constraint

### Subtype

`NS-05 Reason-Linked Non-Execution`

### Scenario definition

The user has not started the task and gives lack of time or busyness as the reason.

### Execution condition

```text
execution_started = false
```

### Core semantic meaning

Non-execution is current; the stated reason explains it.

### Boundary risk

The reason must not become the execution label.

### Example semantic realizations

- “I haven’t exercised because I’m too busy.”
- “I haven’t taken it because I’ve been occupied.”
- “I haven’t done the therapy because I haven’t had time.”

### Construction constraint

This scenario can overlap with the Persuasion Barrier ontology, but the Execution Status remains `Not Started`.

---

## Scenario NS-S14 — Non-Execution Due to Forgetting

### Subtype

`NS-05 Reason-Linked Non-Execution`

### Scenario definition

The user has not started the task and explains that they forgot or failed to remember it.

### Execution condition

```text
execution_started = false
```

### Core semantic meaning

The task remains unexecuted; forgetting is the explanation.

### Boundary risk

Distinguish forgetting from retrospective completion.

### Example semantic realizations

- “I forgot to take the medicine.”
- “I forgot to do the exercises.”
- “I completely forgot about the therapy routine.”

### Construction constraint

The utterance must not imply that the task was actually completed earlier.

---

## Scenario NS-S15 — Non-Execution Due to Inability / Unavailability

### Subtype

`NS-05 Reason-Linked Non-Execution`

### Scenario definition

The user has not begun the task because they were unable, unavailable, or otherwise prevented from executing it.

### Execution condition

```text
execution_started = false
```

### Core semantic meaning

The task remains unstarted; inability or unavailability explains the state.

### Boundary risk

Distinguish inability before initiation from interruption after initiation.

### Example semantic realizations

- “I couldn’t do the exercise because I wasn’t able to.”
- “I haven’t taken it because I couldn’t get to it.”
- “I couldn’t start the therapy routine today.”

### Construction constraint

If the utterance establishes that execution began before the problem occurred, it belongs to `In Progress`, not this scenario.

---

# 11. Scenario Coverage Matrix

| Scenario | Subtype | Core semantic region | Primary boundary |
|---|---|---|---|
| NS-S01 | NS-01 | Explicit non-start | NS ↔ IP |
| NS-S02 | NS-01 | Untouched task | NS ↔ IP |
| NS-S03 | NS-01 | Current non-execution | NS ↔ IP |
| NS-S04 | NS-02 | Future action | NS ↔ IP |
| NS-S05 | NS-02 | Deferred start | NS ↔ IP |
| NS-S06 | NS-02 | Future completion intention | NS ↔ IP |
| NS-S07 | NS-03 | Conditional start | NS ↔ IP |
| NS-S08 | NS-03 | Event-triggered start | NS ↔ IP |
| NS-S09 | NS-03 | Conditional availability | NS ↔ IP |
| NS-S10 | NS-04 | Direct refusal | NS ↔ IP |
| NS-S11 | NS-04 | Task rejection | NS ↔ IP |
| NS-S12 | NS-04 | Refusal without reason | NS ↔ IP |
| NS-S13 | NS-05 | Time/busyness reason | NS ↔ IP |
| NS-S14 | NS-05 | Forgetting reason | NS ↔ Completed / IP |
| NS-S15 | NS-05 | Inability/unavailability | NS ↔ IP |

---

# 12. Task-Domain Allocation

The 15 semantic scenarios should not be instantiated using only one task domain.

A balanced working allocation can use:

| Scenario group | Medication | Hydration | Exercise | Physiotherapy |
|---|---:|---:|---:|---:|
| NS-01 | ✓ | ✓ | ✓ | ✓ |
| NS-02 | ✓ | ✓ | ✓ | ✓ |
| NS-03 | ✓ | ✓ | ✓ | ✓ |
| NS-04 | ✓ | ✓ | ✓ | ✓ |
| NS-05 | ✓ | ✓ | ✓ | ✓ |

The scenario itself defines the semantic region. Domain allocation should be rotated across scenarios and anchors so that:

- no subtype is tied to one domain;
- no lexical expression becomes domain-specific;
- no task domain predicts the execution state.

---

# 13. Initial Anchor Construction

Each semantic scenario should receive **three initial anchors**.

The anchors are not intended to be final linguistic diversity. They establish the semantic meaning of the scenario before Stage 3A expansion.

## Anchor A — Explicit Prototype

A direct, low-ambiguity realization of the scenario.

Purpose:

- establish the semantic center;
- make the intended execution state obvious;
- provide a stable reference example.

## Anchor B — Natural Prototype

A natural conversational realization preserving the same scenario meaning.

Purpose:

- move away from rigid template language;
- test that the scenario remains understandable in ordinary conversation.

## Anchor C — Implicit / Contextual Prototype

A less explicit realization that still preserves the scenario's execution semantics.

Purpose:

- begin semantic robustness;
- avoid making the dataset dependent on direct state words.

### Anchor invariant

All three anchors must map to:

```yaml
execution_status: Not Started
```

while preserving the same underlying scenario.

---

# 14. Example Anchor Intent

For scenario `NS-S04 — Straightforward Future Action`:

### Anchor A — Explicit Prototype

Semantic intent:

> The user has not started the exercise and says they will do it later.

### Anchor B — Natural Prototype

Semantic intent:

> The user naturally says they will exercise later.

### Anchor C — Less Explicit Prototype

Semantic intent:

> The user indicates that exercise will happen later, with no evidence of current execution.

The exact final utterances should be produced during anchor construction, not copied mechanically from this document.

---

# 15. Scenario Construction Constraints

Every Not Started scenario must satisfy all of the following:

### 15.1 No execution evidence

The utterance must not imply that execution has begun.

### 15.2 No completion evidence

The utterance must not imply that the target task has already been completed.

### 15.3 Future intention is still Not Started

Statements about future execution remain `Not Started`.

### 15.4 Reasons do not change execution status

A reason for non-execution does not itself create a new execution state.

### 15.5 Refusal remains Not Started

A refusal without execution remains `Not Started`.

### 15.6 Interruption is different

If execution has already begun and then stops temporarily, the example belongs to `In Progress`.

### 15.7 No task-manager semantics

Do not construct scenarios whose defining label is:

- overdue;
- missed;
- expired;
- delayed;
- skipped as an operational scheduler state.

Such states may later be derived by the Task Manager from Execution Status plus temporal information.

---

# 16. Scenario-Level Boundary Sensitivity

The Not Started inventory must deliberately contain examples that sit near the transition into `In Progress`.

Important contrast regions include:

### Future intention vs actual initiation

```text
“I’ll start the exercise later.”
        ↓
Not Started

“I’m starting the exercise now.”
        ↓
In Progress
```

### No execution vs partial execution

```text
“I haven’t done the exercise.”
        ↓
Not Started

“I’ve done part of the exercise.”
        ↓
In Progress
```

### Reason-linked non-execution vs interrupted execution

```text
“I couldn’t start the exercise.”
        ↓
Not Started

“I started the exercise but had to stop.”
        ↓
In Progress
```

### Forgetting vs retrospective completion

```text
“I forgot to take the medicine.”
        ↓
Not Started

“I took the medicine earlier.”
        ↓
Completed
```

These are semantic boundary regions. They are not yet Stage 2 minimal-pair resources.

---

# 17. Lexical Shortcut Prevention

Scenario construction must not rely on a fixed vocabulary such as:

- “haven’t” → Not Started;
- “later” → Not Started;
- “won’t” → Not Started;
- “forgot” → Not Started.

The same lexical items may appear in different semantic contexts during later boundary and hard-negative construction.

For example:

> “I haven’t finished yet.”

is not automatically `Not Started`; if the context establishes that execution began, the correct state is `In Progress`.

Therefore the semantic condition—not the presence of a word—controls the label.

---

# 18. Scenario Deduplication

Two scenarios should not be retained as separate semantic scenarios merely because their wording differs.

A new scenario is justified only when it introduces a distinct execution meaning, such as:

- direct non-execution;
- future/deferred action;
- conditional action;
- refusal;
- reason-linked non-execution.

Paraphrases belong to anchor or later linguistic expansion stages.

---

# 19. Scenario Leakage Prevention

Scenario lineage must be retained.

Each generated utterance should be traceable to:

```text
state
  ↓
subtype
  ↓
scenario
  ↓
anchor
  ↓
linguistic variant
```

The same semantic scenario should not be independently regenerated under another subtype simply because its wording differs.

For later train/test/validation splitting, descendants of the same semantic lineage should be grouped to prevent semantic leakage.

---

# 20. Stage 1 Human–LLM–Code Allocation

## Human responsibility

Humans determine:

- whether a semantic scenario is valid;
- whether it belongs to `Not Started`;
- whether it is genuinely distinct from another scenario;
- whether its boundary is correctly identified.

## LLM responsibility

LLMs may assist with:

- natural-language realization;
- paraphrase generation;
- linguistic diversity;
- alternative conversational phrasing.

LLMs must not independently redefine the execution ontology.

## Code responsibility

Code should verify:

- metadata completeness;
- state/subtype consistency;
- scenario IDs;
- anchor counts;
- duplicate detection;
- lineage fields;
- later split integrity.

---

# 21. Stage 1 Completion Criteria for Not Started

The Not Started scenario inventory is ready for anchor construction when:

- all five working subtypes are represented;
- all 15 working scenarios have clear semantic definitions;
- every scenario has an explicit execution condition;
- future intention is separated from actual execution;
- conditional future action is represented;
- refusal is represented without turning it into a new production state;
- reason-linked non-execution is represented;
- forgetting and inability/unavailability are covered;
- task-domain coverage is distributed across medication, hydration, exercise, and physiotherapy;
- major `Not Started ↔ In Progress` boundary regions are represented;
- no scenario depends on lexical shortcuts;
- no scenario duplicates another semantic region;
- all scenarios remain compatible with the frozen three-state ontology.

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
s1/anchors/01_initial_anchors_not_started.md
```

That file should realize the 15 semantic scenarios into three initial anchors per scenario while preserving the semantic invariants defined here.

---

# 23. Final Principle

**A Not Started scenario is valid only when the target task has not begun.**

Future intention, conditional intention, refusal, forgetting, busyness, inability, and other explanations may produce different linguistic forms and different conversational meanings, but they remain `Not Started` whenever there is no evidence that task execution has begun.

The Stage 1 objective is therefore:

> **Construct a semantically complete inventory of non-execution situations before introducing linguistic variation.**
