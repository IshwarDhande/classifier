# Execution Status Dataset — Stage 1 Initial Anchors: Not Started

## 1. Purpose

This document defines the initial semantic anchors for all **15 Not Started scenarios**.

The anchors are the first natural-language realizations of the Stage 1 semantic scenario inventory. They establish the semantic center of each scenario before later linguistic expansion.

Production label:

```yaml
execution_status: Not Started
```

The three anchors for every scenario must preserve the same underlying execution meaning.

---

# 2. Anchor Construction Principle

Each semantic scenario receives exactly three initial anchors:

| Anchor | Purpose |
|---|---|
| A — Explicit Prototype | Direct, low-ambiguity realization of the scenario |
| B — Natural Prototype | Natural conversational realization |
| C — Contextual / Less-Explicit Prototype | Less canonical realization that still preserves the scenario semantics |

The three anchors are **not three different labels or scenarios**.

They are three realizations of the same semantic point.

---

# 3. Global Semantic Invariant

Every anchor in this file must satisfy:

```yaml
execution_started: false
execution_completed: false
execution_status: Not Started
```

The following must not be introduced as execution evidence:

- future intention;
- willingness;
- conditional intention;
- refusal;
- reason for non-execution;
- planning;
- scheduling;
- preparation alone.

The defining question remains:

> Has execution of the target task actually begun?

For this file, the answer must always be **No**.

---

# 4. Anchor Metadata

Recommended metadata:

```yaml
scenario_id:
subtype_id:
anchor_id:
anchor_type:
task_domain:
utterance:
execution_status: Not Started
```

Anchor lineage:

```text
Not Started
    ↓
Subtype
    ↓
Scenario
    ↓
Anchor
```

---

# 5. NS-S01 — Task Not Yet Started

### Subtype
`NS-01 Direct Non-Execution`

### Scenario meaning

The target task has not been started.

### Anchor A — Explicit Prototype

> I haven’t started the exercise yet.

### Anchor B — Natural Prototype

> I still haven’t begun the exercise.

### Anchor C — Contextual / Less-Explicit Prototype

> The exercise hasn’t been started on my side yet.

### Domain

Exercise

### Invariant

No execution activity has occurred.

---

# 6. NS-S02 — Task Remains Untouched

### Subtype
`NS-01 Direct Non-Execution`

### Scenario meaning

The target task remains completely untouched.

### Anchor A — Explicit Prototype

> I haven’t taken any of the medicine yet.

### Anchor B — Natural Prototype

> I haven’t done anything with the dose so far.

### Anchor C — Contextual / Less-Explicit Prototype

> The dose is still untouched.

### Domain

Medication

### Invariant

No portion of the target task has been executed.

---

# 7. NS-S03 — Current Non-Execution

### Subtype
`NS-01 Direct Non-Execution`

### Scenario meaning

The user is currently not performing the target task, with no future commitment or reason required.

### Anchor A — Explicit Prototype

> I’m not exercising right now.

### Anchor B — Natural Prototype

> I’m not doing the exercise at the moment.

### Anchor C — Contextual / Less-Explicit Prototype

> I’m not on the exercise yet.

### Domain

Exercise

### Invariant

The utterance must represent non-execution, not a temporary pause after execution began.

---

# 8. NS-S04 — Straightforward Future Action

### Subtype

`NS-02 Future / Deferred Action`

### Scenario meaning

The task has not begun; the user intends to perform it later.

### Anchor A — Explicit Prototype

> I’ll take the medicine later.

### Anchor B — Natural Prototype

> I’m going to take it tonight.

### Anchor C — Contextual / Less-Explicit Prototype

> I’ll get to the dose later.

### Domain

Medication

### Invariant

Future intention does not constitute execution.

---

# 9. NS-S05 — Deferred Start

### Subtype

`NS-02 Future / Deferred Action`

### Scenario meaning

The start of execution itself is deferred.

### Anchor A — Explicit Prototype

> I haven’t started the exercises yet; I’ll do them after lunch.

### Anchor B — Natural Prototype

> I’ll start the exercises this evening.

### Anchor C — Contextual / Less-Explicit Prototype

> I’ll get started on the routine when I’m back.

### Domain

Exercise

### Invariant

The task must not have already begun.

---

# 10. NS-S06 — Later Completion Intention

### Subtype
`NS-02 Future / Deferred Action`

### Scenario meaning

The user describes future completion without evidence of current execution.

### Anchor A — Explicit Prototype

> I haven’t started it; I’ll finish the routine tonight.

### Anchor B — Natural Prototype

> I’m going to get the physiotherapy done later.

### Anchor C — Contextual / Less-Explicit Prototype

> The routine is something I’ll take care of this evening.

### Domain

Physiotherapy

### Invariant

Strong intention remains `Not Started` when execution has not begun.

---

# 11. NS-S07 — Condition-Dependent Start

### Subtype
`NS-03 Conditional Future Action`

### Scenario meaning

Execution will begin only if a future condition is satisfied.

### Anchor A — Explicit Prototype

> If I get enough time, I’ll do the exercise.

### Anchor B — Natural Prototype

> I’ll exercise if I get a free hour.

### Anchor C — Contextual / Less-Explicit Prototype

> The exercise will happen if I can get some time later.

### Domain

Exercise

### Invariant

The condition has not been satisfied and execution has not begun.

---

# 12. NS-S08 — Event-Triggered Future Start

### Subtype
`NS-03 Conditional Future Action`

### Scenario meaning

Execution will begin after another future event.

### Anchor A — Explicit Prototype

> I’ll take the medicine after dinner.

### Anchor B — Natural Prototype

> Once I finish dinner, I’ll take it.

### Anchor C — Contextual / Less-Explicit Prototype

> The dose comes after I’m done eating.

### Domain

Medication

### Invariant

The triggering event remains future; current execution has not begun.

---

# 13. NS-S09 — Conditional Availability

### Subtype
`NS-03 Conditional Future Action`

### Scenario meaning

Execution depends on future availability or opportunity.

### Anchor A — Explicit Prototype

> If I have enough time, I’ll do the physiotherapy.

### Anchor B — Natural Prototype

> I’ll do the routine if I get a break later.

### Anchor C — Contextual / Less-Explicit Prototype

> I can get to the therapy if I’m free this evening.

### Domain

Physiotherapy

### Invariant

Conditional future execution must not be confused with current execution.

---

# 14. NS-S10 — Direct Refusal

### Subtype
`NS-04 Refusal Without Execution`

### Scenario meaning

The user explicitly refuses the target task without having started it.

### Anchor A — Explicit Prototype

> I’m not going to do the exercise.

### Anchor B — Natural Prototype

> No, I’m not doing it.

### Anchor C — Contextual / Less-Explicit Prototype

> I’ll pass on the exercise today.

### Domain

Exercise

### Invariant

The refusal must not imply that execution already occurred.

---

# 15. NS-S11 — Rejection of the Task

### Subtype
`NS-04 Refusal Without Execution`

### Scenario meaning

The user rejects or declines the target task.

### Anchor A — Explicit Prototype

> I’m not going to take the medicine.

### Anchor B — Natural Prototype

> I don’t want to do the routine.

### Anchor C — Contextual / Less-Explicit Prototype

> I’m skipping the therapy today.

### Domain

Physiotherapy

### Invariant

“Skipping” is treated here as non-execution, not as a Task Manager state.

---

# 16. NS-S12 — Refusal Without Explicit Reason

### Subtype
`NS-04 Refusal Without Execution`

### Scenario meaning

The user clearly refuses without giving a reason.

### Anchor A — Explicit Prototype

> No, I won’t do it.

### Anchor B — Natural Prototype

> I’m not doing that.

### Anchor C — Contextual / Less-Explicit Prototype

> I’ll pass.

### Domain

Hydration

### Invariant

The target task must be recoverable from the immediate context for very short anchors.

---

# 17. NS-S13 — Non-Execution Due to Time Constraint

### Subtype
`NS-05 Reason-Linked Non-Execution`

### Scenario meaning

The task has not begun because the user is busy or lacks time.

### Anchor A — Explicit Prototype

> I haven’t exercised because I’m too busy.

### Anchor B — Natural Prototype

> I haven’t had time to do the exercises.

### Anchor C — Contextual / Less-Explicit Prototype

> The exercise hasn’t happened; my schedule has been packed.

### Domain

Exercise

### Invariant

The reason explains non-execution; it does not replace the execution status.

---

# 18. NS-S14 — Non-Execution Due to Forgetting

### Subtype
`NS-05 Reason-Linked Non-Execution`

### Scenario meaning

The target task has not been executed because the user forgot.

### Anchor A — Explicit Prototype

> I forgot to take the medicine.

### Anchor B — Natural Prototype

> I completely forgot about the dose.

### Anchor C — Contextual / Less-Explicit Prototype

> The medicine never got taken because I forgot.

### Domain

Medication

### Invariant

Forgetting must not imply that the task was completed earlier.

---

# 19. NS-S15 — Non-Execution Due to Inability / Unavailability

### Subtype
`NS-05 Reason-Linked Non-Execution`

### Scenario meaning

The task has not begun because the user was unable or unavailable to execute it.

### Anchor A — Explicit Prototype

> I couldn’t start the physiotherapy today.

### Anchor B — Natural Prototype

> I wasn’t able to do the routine.

### Anchor C — Contextual / Less-Explicit Prototype

> I never got to the therapy because I couldn’t.

### Domain

Physiotherapy

### Invariant

The scenario must not imply that execution began before the inability occurred.

---

# 20. Anchor Coverage Matrix

| Scenario | Subtype | Anchor A | Anchor B | Anchor C | Domain |
|---|---|---|---|---|---|
| NS-S01 | NS-01 | Explicit | Natural | Contextual | Exercise |
| NS-S02 | NS-01 | Explicit | Natural | Contextual | Medication |
| NS-S03 | NS-01 | Explicit | Natural | Contextual | Exercise |
| NS-S04 | NS-02 | Explicit | Natural | Contextual | Medication |
| NS-S05 | NS-02 | Explicit | Natural | Contextual | Exercise |
| NS-S06 | NS-02 | Explicit | Natural | Contextual | Physiotherapy |
| NS-S07 | NS-03 | Explicit | Natural | Contextual | Exercise |
| NS-S08 | NS-03 | Explicit | Natural | Contextual | Medication |
| NS-S09 | NS-03 | Explicit | Natural | Contextual | Physiotherapy |
| NS-S10 | NS-04 | Explicit | Natural | Contextual | Exercise |
| NS-S11 | NS-04 | Explicit | Natural | Contextual | Physiotherapy |
| NS-S12 | NS-04 | Explicit | Natural | Contextual | Hydration |
| NS-S13 | NS-05 | Explicit | Natural | Contextual | Exercise |
| NS-S14 | NS-05 | Explicit | Natural | Contextual | Medication |
| NS-S15 | NS-05 | Explicit | Natural | Contextual | Physiotherapy |

Total:

```text
15 scenarios
× 3 anchors
= 45 initial anchors
```

---

# 21. Anchor-Level Semantic Invariants

Every three-anchor family must preserve:

### 21.1 Same execution state

All anchors map to:

```text
Not Started
```

### 21.2 Same scenario

The semantic subtype and scenario remain unchanged.

### 21.3 No execution initiation

No anchor may accidentally introduce:

- starting;
- partial completion;
- active performance;
- near completion.

### 21.4 No completion

No anchor may imply that the task has already finished.

### 21.5 Controlled variation

Differences between A, B, and C should primarily concern realization style, not execution semantics.

---

# 22. Anchor Type Definitions

## A — Explicit Prototype

Characteristics:

- direct;
- low ambiguity;
- minimal inference;
- strong semantic center.

Typical construction:

```text
subject + explicit execution-state expression + task
```

The wording should make the intended `Not Started` interpretation easy to verify.

---

## B — Natural Prototype

Characteristics:

- conversational;
- less template-like;
- ordinary user language;
- same semantic state.

The anchor should sound like something a user could naturally say during interaction with a reminder agent.

---

## C — Contextual / Less-Explicit Prototype

Characteristics:

- less canonical;
- may rely on immediate context;
- avoids overuse of explicit state terminology;
- still semantically recoverable.

This anchor should introduce modest semantic difficulty without becoming a Stage 2 hard negative.

---

# 23. Lexical Shortcut Control

The anchors intentionally vary wording so that the dataset does not reduce to simple lexical rules.

The following must not be treated as deterministic labels:

```text
haven’t
later
will
if
won’t
forgot
couldn’t
```

For example:

> “I haven’t finished yet.”

would not automatically be `Not Started`; if the context establishes prior execution, it can be `In Progress`.

Likewise:

> “I’ll finish it later.”

is `Not Started` only when the target task has not already begun.

---

# 24. Boundary Preservation

The initial anchors should sit around the semantic center of their scenario, not deliberately cross a neighboring state.

Important boundaries:

### Not Started ↔ In Progress

Do not introduce:

- partial execution;
- current performance;
- execution already underway.

### Not Started ↔ Completed

Do not introduce:

- retrospective completion;
- result states that entail completion;
- full execution.

Boundary ambiguity will be deliberately constructed later in Stage 2.

---

# 25. Context Handling

Short contextual anchors may rely on a previously established target task.

For example:

```text
Agent: Did you take your medicine?
User: I’ll take it after dinner.
```

The user's execution state remains:

```text
Not Started
```

Context should clarify the target task, not alter the execution semantics.

---

# 26. Task-Domain Distribution

The current initial anchors use the four frozen task domains:

- Medication
- Hydration
- Exercise
- Physiotherapy

Domain rotation is intentionally imperfect at this first anchor stage because the semantic scenario remains the primary construction unit.

Later expansion should broaden domain realization and prevent domain-specific lexical shortcuts.

---

# 27. Anchor Quality Rules

Each anchor should satisfy:

1. Natural conversational plausibility.
2. Clear target-task reference or recoverability.
3. Correct semantic subtype.
4. Correct production state.
5. No unintended execution evidence.
6. No unintended completion evidence.
7. No dependence on a single keyword.
8. No unnecessary external knowledge.
9. No accidental dialogue-purpose substitution.
10. No accidental persuasion-barrier relabeling.

---

# 28. Human–LLM–Code Allocation

## Human responsibility

Humans verify:

- semantic correctness;
- state correctness;
- subtype correctness;
- scenario fidelity;
- boundary safety.

## LLM responsibility

LLMs may produce:

- natural wording;
- paraphrases;
- contextual variants;
- conversational realizations.

The LLM must preserve the scenario definition.

## Code responsibility

Code should validate:

- 15 scenario IDs;
- 3 anchors per scenario;
- unique anchor IDs;
- required metadata;
- state consistency;
- duplicate detection;
- lineage preservation.

---

# 29. Stage 1 Anchor Completion Criteria

The Not Started anchor resource is complete when:

- all 15 scenarios have three anchors;
- total anchor count is 45;
- every anchor maps to `Not Started`;
- every anchor preserves its parent scenario;
- all five Not Started subtypes are represented;
- explicit, natural, and contextual prototypes are represented;
- no anchor implies execution has begun;
- no anchor implies completion;
- future intention remains distinct from current execution;
- refusal remains non-execution;
- reason-linked non-execution remains non-execution;
- lexical shortcuts are not required to identify the state.

---

# 30. Output Summary

```text
State: Not Started

Subtypes: 5
Scenarios: 15
Anchors per scenario: 3
Initial anchors: 45

Anchor types:
A — Explicit Prototype
B — Natural Prototype
C — Contextual / Less-Explicit Prototype
```

---

# 31. Final Principle

**The purpose of an initial anchor is to establish the semantic center of a scenario, not to maximize linguistic diversity.**

For every anchor in this file, the target task remains unstarted.

The language may change, but the execution invariant does not:

```text
execution_started = false
execution_completed = false
        ↓
Not Started
```
