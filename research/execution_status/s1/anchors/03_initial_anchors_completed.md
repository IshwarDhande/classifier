# Execution Status Dataset — Stage 1 Initial Anchors: Completed

## 1. Purpose

This document defines the initial semantic anchors for all **15 Completed scenarios**.

The anchors are the first natural-language realizations of the Stage 1 semantic scenario inventory. They establish the semantic center of each scenario before later linguistic expansion.

Production label:

```yaml
execution_status: Completed
```

The three anchors for every scenario must preserve the same underlying completion meaning.

---

# 2. Anchor Construction Principle

Each semantic scenario receives exactly three initial anchors:

| Anchor | Purpose |
|---|---|
| A — Explicit Prototype | Direct, low-ambiguity realization |
| B — Natural Prototype | Natural conversational realization |
| C — Contextual / Less-Explicit Prototype | Less canonical realization that still preserves the scenario |

The three anchors are realizations of the same semantic scenario, not independent scenarios.

---

# 3. Global Semantic Invariant

Every anchor in this file must satisfy:

```yaml
execution_started: true
execution_completed: true
execution_status: Completed
```

The following must not weaken the completion evidence:

- future intention;
- partial execution;
- near completion;
- unfinished work;
- temporary interruption before completion.

The defining question remains:

> Has execution of the target task actually finished?

For every anchor in this file, the answer must be **Yes**.

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
execution_status: Completed
```

Anchor lineage:

```text
Completed
    ↓
Subtype
    ↓
Scenario
    ↓
Anchor
```

---

# 5. C-S01 — Explicit Completion

### Subtype
`C-01 Direct Completion`

### Scenario meaning

The user explicitly states that the target task has been completed.

### Anchor A — Explicit Prototype

> I finished the exercise.

### Anchor B — Natural Prototype

> I’m done with the exercise.

### Anchor C — Contextual / Less-Explicit Prototype

> The exercise is finished.

### Domain

Exercise

### Invariant

The target execution has ended.

---

# 6. C-S02 — Done / Finished State

### Subtype
`C-01 Direct Completion`

### Scenario meaning

A concise completion expression establishes that the target task is finished.

### Anchor A — Explicit Prototype

> Done with the medicine.

### Anchor B — Natural Prototype

> All done.

### Anchor C — Contextual / Less-Explicit Prototype

> That’s finished now.

### Domain

Medication

### Invariant

For short anchors, the immediate conversational context must identify the target task.

---

# 7. C-S03 — Explicit Completion With Task Reference

### Subtype
`C-01 Direct Completion`

### Scenario meaning

The user directly establishes completion while explicitly referring to the target task.

### Anchor A — Explicit Prototype

> I’ve completed the physiotherapy routine.

### Anchor B — Natural Prototype

> I’m finished with the therapy.

### Anchor C — Contextual / Less-Explicit Prototype

> The whole therapy routine is done.

### Domain

Physiotherapy

### Invariant

The completed activity must be the target task.

---

# 8. C-S04 — Completed Earlier

### Subtype
`C-02 Retrospective Completion`

### Scenario meaning

The user reports that the target task was completed earlier.

### Anchor A — Explicit Prototype

> I already did the exercise.

### Anchor B — Natural Prototype

> I finished it earlier.

### Anchor C — Contextual / Less-Explicit Prototype

> That’s something I’ve already taken care of.

### Domain

Exercise

### Invariant

The temporal distance from the present does not change the completion state.

---

# 9. C-S05 — Earlier Completion With Temporal Reference

### Subtype
`C-02 Retrospective Completion`

### Scenario meaning

The user gives a temporal reference to a completed execution event.

### Anchor A — Explicit Prototype

> I took the medicine earlier today.

### Anchor B — Natural Prototype

> I did it before breakfast.

### Anchor C — Contextual / Less-Explicit Prototype

> The dose was taken earlier.

### Domain

Medication

### Invariant

The temporal expression must refer to completed execution, not planned execution.

---

# 10. C-S06 — Retrospective Completion After Reminder

### Subtype
`C-02 Retrospective Completion`

### Scenario meaning

In conversational context, the user indicates that the target task was already completed before the current reminder.

### Anchor A — Explicit Prototype

> I already took it.

### Anchor B — Natural Prototype

> That’s already done.

### Anchor C — Contextual / Less-Explicit Prototype

> You reminded me after I’d already finished it.

### Domain

Medication

### Invariant

The reminder context must not be interpreted as evidence that the task remains unfinished.

---

# 11. C-S07 — Completion Through Result State

### Subtype
`C-03 Indirect Completion`

### Scenario meaning

The user describes a resulting state that establishes completion without relying on a canonical completion verb.

### Anchor A — Explicit Prototype

> The water bottle is empty now.

### Anchor B — Natural Prototype

> There’s nothing left in the bottle.

### Anchor C — Contextual / Less-Explicit Prototype

> The whole bottle is gone.

### Domain

Hydration

### Invariant

The result state must establish that the intended target has been fully executed in the relevant context.

---

# 12. C-S08 — Completion Through Exhausted Required Quantity

### Subtype
`C-03 Indirect Completion`

### Scenario meaning

The required quantity or target amount has been fully consumed or performed.

### Anchor A — Explicit Prototype

> I finished the whole bottle of water.

### Anchor B — Natural Prototype

> I drank all of it.

### Anchor C — Contextual / Less-Explicit Prototype

> There’s none of the target amount left.

### Domain

Hydration

### Invariant

The entire required target is complete; a partial amount is insufficient.

---

# 13. C-S09 — Completion Through Consequential State

### Subtype
`C-03 Indirect Completion`

### Scenario meaning

The user describes a state that establishes that no target execution remains.

### Anchor A — Explicit Prototype

> There’s nothing left for me to do in the routine.

### Anchor B — Natural Prototype

> I’m through the whole routine now.

### Anchor C — Contextual / Less-Explicit Prototype

> The session is over.

### Domain

Physiotherapy

### Invariant

The consequential state must be sufficient evidence of completed execution.

---

# 14. C-S10 — All Required Steps Completed

### Subtype
`C-04 Multi-Step Completion`

### Scenario meaning

All required steps of a multi-step task have been completed.

### Anchor A — Explicit Prototype

> I finished all the exercises.

### Anchor B — Natural Prototype

> I got through the whole routine.

### Anchor C — Contextual / Less-Explicit Prototype

> Every step is done.

### Domain

Exercise

### Invariant

No required execution step remains.

---

# 15. C-S11 — Final Step Completed

### Subtype
`C-04 Multi-Step Completion`

### Scenario meaning

The final remaining step of a multi-step task has been completed.

### Anchor A — Explicit Prototype

> I just finished the last set.

### Anchor B — Natural Prototype

> The final exercise is done.

### Anchor C — Contextual / Less-Explicit Prototype

> That was the last step, and it’s finished.

### Domain

Exercise

### Invariant

The final step closes the execution sequence.

---

# 16. C-S12 — Multi-Step Completion With Full-Sequence Reference

### Subtype
`C-04 Multi-Step Completion`

### Scenario meaning

The user refers to completion of the entire execution sequence.

### Anchor A — Explicit Prototype

> I completed every part of the physiotherapy routine.

### Anchor B — Natural Prototype

> I went through the whole routine.

### Anchor C — Contextual / Less-Explicit Prototype

> I’ve finished all of it.

### Domain

Physiotherapy

### Invariant

The entire sequence, not just one component, has been completed.

---

# 17. C-S13 — Completion Plus Reaction

### Subtype
`C-05 Completion with Additional Commentary`

### Scenario meaning

The user explicitly establishes completion and adds a reaction or evaluation.

### Anchor A — Explicit Prototype

> I finished the exercises; they were tiring.

### Anchor B — Natural Prototype

> I’m done with the workout, and that was harder than expected.

### Anchor C — Contextual / Less-Explicit Prototype

> The exercise is finished, though it took a lot out of me.

### Domain

Exercise

### Invariant

The additional reaction does not alter the completed execution state.

---

# 18. C-S14 — Completion Plus Context

### Subtype
`C-05 Completion with Additional Commentary`

### Scenario meaning

The user reports completion while adding contextual information about when, where, or under what circumstances it occurred.

### Anchor A — Explicit Prototype

> I finished the exercise before breakfast.

### Anchor B — Natural Prototype

> I took the medicine at home, so that’s done.

### Anchor C — Contextual / Less-Explicit Prototype

> I completed the therapy earlier, while I was at home.

### Domain

Exercise / Medication / Physiotherapy

### Invariant

The contextual information accompanies an already completed execution event.

---

# 19. C-S15 — Completion Plus Follow-Up Action

### Subtype
`C-05 Completion with Additional Commentary`

### Scenario meaning

The user establishes completion and then describes a separate future follow-up action.

### Anchor A — Explicit Prototype

> I finished the exercises, and now I’ll take a break.

### Anchor B — Natural Prototype

> I’m done with the routine; I’m going to rest now.

### Anchor C — Contextual / Less-Explicit Prototype

> The therapy is finished, so I’ll relax for a while.

### Domain

Exercise / Physiotherapy

### Invariant

The future follow-up action must not obscure or replace the completed target task.

---

# 20. Anchor Coverage Matrix

| Scenario | Subtype | Anchor A | Anchor B | Anchor C | Domain |
|---|---|---|---|---|---|
| C-S01 | C-01 | Explicit | Natural | Contextual | Exercise |
| C-S02 | C-01 | Explicit | Natural | Contextual | Medication |
| C-S03 | C-01 | Explicit | Natural | Contextual | Physiotherapy |
| C-S04 | C-02 | Explicit | Natural | Contextual | Exercise |
| C-S05 | C-02 | Explicit | Natural | Contextual | Medication |
| C-S06 | C-02 | Explicit | Natural | Contextual | Medication |
| C-S07 | C-03 | Explicit | Natural | Contextual | Hydration |
| C-S08 | C-03 | Explicit | Natural | Contextual | Hydration |
| C-S09 | C-03 | Explicit | Natural | Contextual | Physiotherapy |
| C-S10 | C-04 | Explicit | Natural | Contextual | Exercise |
| C-S11 | C-04 | Explicit | Natural | Contextual | Exercise |
| C-S12 | C-04 | Explicit | Natural | Contextual | Physiotherapy |
| C-S13 | C-05 | Explicit | Natural | Contextual | Exercise |
| C-S14 | C-05 | Explicit | Natural | Contextual | Mixed |
| C-S15 | C-05 | Explicit | Natural | Contextual | Mixed |

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
Completed
```

### 21.2 Same scenario

The semantic subtype and scenario remain unchanged.

### 21.3 Execution has occurred

The target task must have actually been executed.

### 21.4 Execution is finished

No required target execution remains.

### 21.5 Controlled variation

Differences between A, B, and C should primarily concern realization style rather than completion semantics.

---

# 22. Anchor Type Definitions

## A — Explicit Prototype

Characteristics:

- direct;
- low ambiguity;
- explicit completion evidence;
- strong semantic center.

Purpose:

> Establish the completed state clearly.

---

## B — Natural Prototype

Characteristics:

- conversational;
- less template-like;
- ordinary user phrasing;
- same completion semantics.

Purpose:

> Establish natural language variation without changing the state.

---

## C — Contextual / Less-Explicit Prototype

Characteristics:

- less canonical;
- may rely on immediate context;
- avoids repetitive completion terminology;
- still semantically recoverable.

Purpose:

> Introduce modest semantic difficulty while remaining a Stage 1 prototype.

---

# 23. Lexical Shortcut Control

The anchors must not teach deterministic mappings such as:

```text
done → Completed
finished → Completed
already → Completed
empty → Completed
all → Completed
```

These words can occur in other execution states.

For example:

> “I’m not done yet.”

contains “done” but is `In Progress`.

Likewise:

> “I’ll finish it later.”

contains “finish” but can be `Not Started` when execution has not begun.

The execution semantics, not individual words, determine the label.

---

# 24. Indirect Completion Anchor Control

Indirect completion requires additional caution.

An indirect anchor is valid only when:

1. the described result establishes completion;
2. the target task is identifiable;
3. no required execution remains;
4. the inference does not require obscure external knowledge;
5. the immediate conversational context supports the interpretation.

For example:

> “The bottle is empty now.”

can represent `Completed` for a hydration task when the target is established as consuming that bottle.

The same sentence should not be used without sufficient task context if multiple interpretations remain possible.

---

# 25. Boundary Preservation

The initial anchors should remain close to the semantic center of their scenario.

## In Progress ↔ Completed

Anchors must establish full completion.

For example:

```text
“I’m almost finished.”
→ In Progress

“I’m finished.”
→ Completed
```

## Not Started ↔ Completed

Anchors must establish that execution actually occurred.

For example:

```text
“I’ll take it later.”
→ Not Started

“I already took it.”
→ Completed
```

Boundary ambiguity should be deliberately constructed later during Stage 2, not accidentally introduced here.

---

# 26. Multi-Step Completion Preservation

Multi-step completion anchors must establish:

```text
completed_steps = total_required_steps
```

For example:

> “I finished all five sets.”

clearly establishes completion.

By contrast:

> “I finished three sets.”

does not establish completion if five are required.

The full execution target is the semantic reference.

---

# 27. Commentary Preservation

Additional commentary must not become the classification target.

For example:

> “I finished the exercises; they were exhausting.”

The execution signal is:

```text
finished the exercises
```

The evaluation is separate.

Likewise:

> “I finished the exercises, and now I’ll rest.”

The future rest action is separate from the completed exercise task.

---

# 28. Context Handling

Short contextual anchors may depend on an immediately established target task.

For example:

```text
Agent: Did you take your medicine?
User: Yes, I already took it.
```

The user's execution state is:

```text
Completed
```

Context should identify the target task, not manufacture completion evidence.

---

# 29. Task-Domain Distribution

The anchors use the four frozen task domains:

- Medication
- Hydration
- Exercise
- Physiotherapy

The same completion subtype should eventually appear across multiple domains.

Later linguistic expansion should broaden domain rotation and reduce domain-specific lexical shortcuts.

---

# 30. Anchor Quality Rules

Each anchor should satisfy:

1. Natural conversational plausibility.
2. Clear target-task reference or recoverability.
3. Correct semantic subtype.
4. Correct production state.
5. Evidence that execution occurred.
6. Evidence that execution finished.
7. No dependence on a single completion keyword.
8. No accidental future-only interpretation.
9. No accidental partial-execution interpretation.
10. No unrelated dialogue-purpose or persuasion-barrier substitution.

---

# 31. Human–LLM–Code Allocation

## Human responsibility

Humans verify:

- execution genuinely occurred;
- completion genuinely occurred;
- subtype correctness;
- scenario fidelity;
- boundary safety;
- indirect completion validity.

## LLM responsibility

LLMs may produce:

- natural wording;
- paraphrases;
- contextual variants;
- indirect completion realizations;
- commentary-bearing utterances.

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

# 32. Stage 1 Anchor Completion Criteria

The Completed anchor resource is complete when:

- all 15 scenarios have three anchors;
- total anchor count is 45;
- every anchor maps to `Completed`;
- every anchor preserves its parent scenario;
- all five Completed subtypes are represented;
- explicit, natural, and contextual prototypes are represented;
- every anchor establishes actual execution;
- every anchor establishes completed execution;
- partial execution is not treated as completion;
- near completion is not treated as completion;
- future intention is not treated as completion;
- retrospective completion is preserved;
- indirect completion remains sufficiently grounded;
- multi-step completion means all required steps are complete;
- commentary does not change the state;
- lexical shortcuts are not required to identify the state.

---

# 33. Output Summary

```text
State: Completed

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

# 34. Final Principle

**The purpose of an initial anchor is to establish the semantic center of a scenario, not to maximize linguistic diversity.**

For every anchor in this file, the target execution has actually occurred and has finished.

The invariant is:

```text
execution_started = true
execution_completed = true
        ↓
Completed
```
