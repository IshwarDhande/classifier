# Execution Status Dataset — Stage 1 Initial Anchors: In Progress

## 1. Purpose

This document defines the initial semantic anchors for all **15 In Progress scenarios**.

The anchors are the first natural-language realizations of the Stage 1 semantic scenario inventory. They establish the semantic center of each scenario before later linguistic expansion.

Production label:

```yaml
execution_status: In Progress
```

The three anchors for every scenario must preserve the same underlying execution meaning.

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
execution_completed: false
execution_status: In Progress
```

The following must not be introduced as completion evidence:

- explicit completion;
- full-task completion;
- all required steps finished;
- retrospective completion;
- result state that entails completion.

The defining question remains:

> Has execution actually begun, while the target task is still unfinished?

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
execution_status: In Progress
```

Anchor lineage:

```text
In Progress
    ↓
Subtype
    ↓
Scenario
    ↓
Anchor
```

---

# 5. IP-S01 — Explicit Current Execution

### Subtype
`IP-01 Direct Ongoing Execution`

### Scenario meaning

The user explicitly indicates that the target task is currently being performed.

### Anchor A — Explicit Prototype

> I’m doing the exercise right now.

### Anchor B — Natural Prototype

> I’m exercising at the moment.

### Anchor C — Contextual / Less-Explicit Prototype

> I’m in the middle of the exercise.

### Domain

Exercise

### Invariant

Execution has begun and the task is not yet complete.

---

# 6. IP-S02 — Active Performance

### Subtype
`IP-01 Direct Ongoing Execution`

### Scenario meaning

The user describes active performance of the target task without relying on a canonical “in progress” phrase.

### Anchor A — Explicit Prototype

> I’m drinking the water now.

### Anchor B — Natural Prototype

> I’m having the water right now.

### Anchor C — Contextual / Less-Explicit Prototype

> I’m working through my water target now.

### Domain

Hydration

### Invariant

The described activity is actual execution, not preparation or future intention.

---

# 7. IP-S03 — Current Execution With Context

### Subtype
`IP-01 Direct Ongoing Execution`

### Scenario meaning

Immediate conversational context establishes that the user has already started the target task and is still executing it.

### Anchor A — Explicit Prototype

> Yes, I’ve started the physiotherapy and I’m still doing it.

### Anchor B — Natural Prototype

> I’ve started already; I’m working through it now.

### Anchor C — Contextual / Less-Explicit Prototype

> I’m on it now.

### Domain

Physiotherapy

### Invariant

The context establishes actual initiation and unfinished execution.

---

# 8. IP-S04 — Partially Completed Task

### Subtype
`IP-02 Partial Execution`

### Scenario meaning

The user has completed part of the task while some execution remains.

### Anchor A — Explicit Prototype

> I’ve done part of the exercise, but I’m not finished.

### Anchor B — Natural Prototype

> I’ve started the exercises; there’s still some left.

### Anchor C — Contextual / Less-Explicit Prototype

> I’m partway through the exercise.

### Domain

Exercise

### Invariant

A non-zero portion is complete, but the full target remains unfinished.

---

# 9. IP-S05 — Partial Quantity / Portion

### Subtype
`IP-02 Partial Execution`

### Scenario meaning

A measurable portion of the target has been executed while some required amount remains.

### Anchor A — Explicit Prototype

> I’ve drunk half the bottle, but I still have some left.

### Anchor B — Natural Prototype

> I’m halfway through the water.

### Anchor C — Contextual / Less-Explicit Prototype

> There’s still some of the bottle left for me to drink.

### Domain

Hydration

### Invariant

The target quantity is only partially completed.

---

# 10. IP-S06 — Started but Not Finished

### Subtype
`IP-02 Partial Execution`

### Scenario meaning

The user explicitly establishes that execution started but has not finished.

### Anchor A — Explicit Prototype

> I started the medicine routine, but I haven’t finished it.

### Anchor B — Natural Prototype

> I’ve begun the routine, but I still have more to do.

### Anchor C — Contextual / Less-Explicit Prototype

> I’m not done with the routine yet; I’ve already started.

### Domain

Medication

### Invariant

The utterance must establish both initiation and unfinished execution.

---

# 11. IP-S07 — Almost Finished

### Subtype
`IP-03 Near Completion`

### Scenario meaning

The task is nearly complete but some execution remains.

### Anchor A — Explicit Prototype

> I’m almost finished with the exercises.

### Anchor B — Natural Prototype

> I’m nearly done with the workout.

### Anchor C — Contextual / Less-Explicit Prototype

> I’ve got just a little of the exercise left.

### Domain

Exercise

### Invariant

Near completion is still `In Progress`.

---

# 12. IP-S08 — Final Remaining Step

### Subtype
`IP-03 Near Completion`

### Scenario meaning

Nearly all execution is complete, but one or a small number of final steps remain.

### Anchor A — Explicit Prototype

> I’ve got one exercise left.

### Anchor B — Natural Prototype

> I’m on the last set now.

### Anchor C — Contextual / Less-Explicit Prototype

> Just one more part of the routine remains.

### Domain

Exercise

### Invariant

The final required step has not yet been completed.

---

# 13. IP-S09 — Nearly Complete With Commentary

### Subtype
`IP-03 Near Completion`

### Scenario meaning

The user indicates near completion while adding contextual or evaluative commentary.

### Anchor A — Explicit Prototype

> I’m almost finished with the therapy, but it took a while.

### Anchor B — Natural Prototype

> I’m nearly through the routine; it’s been tiring.

### Anchor C — Contextual / Less-Explicit Prototype

> There’s only a little left, although this session has been long.

### Domain

Physiotherapy

### Invariant

The commentary must not change the unfinished execution state.

---

# 14. IP-S10 — Multiple Steps Partially Executed

### Subtype
`IP-04 Multi-Step Execution`

### Scenario meaning

The target consists of multiple required steps, some completed and some remaining.

### Anchor A — Explicit Prototype

> I’ve finished the first two exercises, but I still have one left.

### Anchor B — Natural Prototype

> I’ve done the first couple of sets and still have more to go.

### Anchor C — Contextual / Less-Explicit Prototype

> I’m partway through the routine; a few steps remain.

### Domain

Exercise

### Invariant

At least one required step remains.

---

# 15. IP-S11 — Sequential Execution Underway

### Subtype
`IP-04 Multi-Step Execution`

### Scenario meaning

The user is progressing through a sequence of required execution steps.

### Anchor A — Explicit Prototype

> I’m on the third step of the physiotherapy routine.

### Anchor B — Natural Prototype

> I’m working through the routine one step at a time.

### Anchor C — Contextual / Less-Explicit Prototype

> I’m in the middle of the therapy sequence.

### Domain

Physiotherapy

### Invariant

The sequence has started but has not reached its final required step.

---

# 16. IP-S12 — Multi-Step Execution With Remaining Work

### Subtype
`IP-04 Multi-Step Execution`

### Scenario meaning

The user identifies completed steps and explicitly indicates that additional required steps remain.

### Anchor A — Explicit Prototype

> I’ve done three sets, and two more are left.

### Anchor B — Natural Prototype

> I’ve got most of the routine done, but there’s still more to finish.

### Anchor C — Contextual / Less-Explicit Prototype

> I’m through the first few parts; the rest is still pending.

### Domain

Exercise

### Invariant

The sequence remains incomplete.

---

# 17. IP-S13 — Execution Paused After Starting

### Subtype
`IP-05 Temporarily Interrupted Execution`

### Scenario meaning

The user started the task and then temporarily paused before completion.

### Anchor A — Explicit Prototype

> I started the exercise, but I had to pause.

### Anchor B — Natural Prototype

> I was doing the exercise and stopped for a moment.

### Anchor C — Contextual / Less-Explicit Prototype

> I’m taking a short break in the middle of it.

### Domain

Exercise

### Invariant

The interruption occurs after execution begins.

---

# 18. IP-S14 — Interrupted With Remaining Work

### Subtype
`IP-05 Temporarily Interrupted Execution`

### Scenario meaning

The user started execution, was interrupted, and still has unfinished work.

### Anchor A — Explicit Prototype

> I started the therapy, but I got interrupted before finishing.

### Anchor B — Natural Prototype

> I was doing the routine when something came up, and I still have some left.

### Anchor C — Contextual / Less-Explicit Prototype

> I had to stop halfway through, so I’m not finished yet.

### Domain

Physiotherapy

### Invariant

Execution has begun; interruption does not reset the state to `Not Started`.

---

# 19. IP-S15 — Resumable Interrupted Execution

### Subtype
`IP-05 Temporarily Interrupted Execution`

### Scenario meaning

The user began execution, temporarily stopped, and indicates that unfinished execution remains.

### Anchor A — Explicit Prototype

> I started the routine and paused; I still need to finish it.

### Anchor B — Natural Prototype

> I’ve begun it, but I’ll continue after this break.

### Anchor C — Contextual / Less-Explicit Prototype

> I’m halfway through and will pick it up again shortly.

### Domain

Physiotherapy

### Invariant

Future continuation does not erase the fact that execution has already begun.

---

# 20. Anchor Coverage Matrix

| Scenario | Subtype | Anchor A | Anchor B | Anchor C | Domain |
|---|---|---|---|---|---|
| IP-S01 | IP-01 | Explicit | Natural | Contextual | Exercise |
| IP-S02 | IP-01 | Explicit | Natural | Contextual | Hydration |
| IP-S03 | IP-01 | Explicit | Natural | Contextual | Physiotherapy |
| IP-S04 | IP-02 | Explicit | Natural | Contextual | Exercise |
| IP-S05 | IP-02 | Explicit | Natural | Contextual | Hydration |
| IP-S06 | IP-02 | Explicit | Natural | Contextual | Medication |
| IP-S07 | IP-03 | Explicit | Natural | Contextual | Exercise |
| IP-S08 | IP-03 | Explicit | Natural | Contextual | Exercise |
| IP-S09 | IP-03 | Explicit | Natural | Contextual | Physiotherapy |
| IP-S10 | IP-04 | Explicit | Natural | Contextual | Exercise |
| IP-S11 | IP-04 | Explicit | Natural | Contextual | Physiotherapy |
| IP-S12 | IP-04 | Explicit | Natural | Contextual | Exercise |
| IP-S13 | IP-05 | Explicit | Natural | Contextual | Exercise |
| IP-S14 | IP-05 | Explicit | Natural | Contextual | Physiotherapy |
| IP-S15 | IP-05 | Explicit | Natural | Contextual | Physiotherapy |

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
In Progress
```

### 21.2 Same scenario

The semantic subtype and scenario remain unchanged.

### 21.3 Execution has begun

Every anchor must provide sufficient evidence that actual execution occurred.

### 21.4 Completion has not occurred

Every anchor must preserve unfinished execution.

### 21.5 Controlled variation

Differences between A, B, and C should primarily concern realization style rather than execution semantics.

---

# 22. Anchor Type Definitions

## A — Explicit Prototype

Characteristics:

- direct;
- low ambiguity;
- strong evidence of execution initiation;
- explicit unfinished state where needed.

Purpose:

> Establish the semantic center of the scenario.

---

## B — Natural Prototype

Characteristics:

- conversational;
- less template-like;
- ordinary user phrasing;
- same execution semantics.

Purpose:

> Establish natural language variation without changing the scenario.

---

## C — Contextual / Less-Explicit Prototype

Characteristics:

- less canonical;
- may rely on immediate context;
- avoids repetitive state terminology;
- still semantically recoverable.

Purpose:

> Introduce modest semantic difficulty while remaining a Stage 1 prototype.

---

# 23. Lexical Shortcut Control

The anchors must not teach deterministic mappings such as:

```text
doing → In Progress
started → In Progress
almost → In Progress
left → In Progress
pause → In Progress
```

These expressions may occur in other execution states.

For example:

> “I’ll start the exercise later.”

contains “start” but is `Not Started`.

Likewise:

> “I finished the exercise after pausing.”

contains “pause” but is `Completed`.

The execution semantics, not individual words, determine the label.

---

# 24. Boundary Preservation

The initial anchors should remain close to the semantic center of their scenario.

## Not Started ↔ In Progress

Anchors must establish actual initiation.

For example:

```text
“I’ll do the exercise later.”
→ Not Started

“I’m doing the exercise now.”
→ In Progress
```

## In Progress ↔ Completed

Anchors must establish remaining work.

For example:

```text
“I’m almost finished.”
→ In Progress

“I’m finished.”
→ Completed
```

Boundary ambiguity should be deliberately introduced later during Stage 2, not accidentally introduced here.

---

# 25. Interruption Preservation

Temporary interruption requires special care.

Correct:

> “I started the exercise but paused.”

→ `In Progress`

Incorrect semantic construction:

> “I haven’t started the exercise because I’m busy.”

→ `Not Started`

The decisive feature is whether execution began before the interruption or reason occurred.

---

# 26. Partial Execution Preservation

Partial execution must contain evidence of both:

```text
completed portion > 0
remaining portion > 0
```

For example:

> “I’ve done three sets and have two left.”

is clearly `In Progress`.

An anchor that says only:

> “I did three sets.”

may be insufficient unless the task definition establishes that more remains.

Stage 1 anchors should therefore favor semantically clear partial-execution constructions.

---

# 27. Near-Completion Preservation

Near completion must never be converted into completion.

Correct:

> “One more set and I’m done.”

→ `In Progress`

Incorrect:

> “I finished the last set.”

→ `Completed`

The remaining work is the decisive semantic feature.

---

# 28. Context Handling

Short contextual anchors may depend on an immediately established target task.

For example:

```text
Agent: Have you started the exercise?
User: Yes, I’m halfway through.
```

The user state is:

```text
In Progress
```

Context should identify the task or execution reference, not manufacture execution evidence.

---

# 29. Task-Domain Distribution

The anchors use the four frozen task domains:

- Medication
- Hydration
- Exercise
- Physiotherapy

The same subtype should eventually appear across multiple domains.

Later linguistic expansion should increase domain rotation and reduce domain-specific lexical shortcuts.

---

# 30. Anchor Quality Rules

Each anchor should satisfy:

1. Natural conversational plausibility.
2. Clear target-task reference or recoverability.
3. Correct semantic subtype.
4. Correct production state.
5. Evidence that execution has begun.
6. Evidence that completion has not occurred.
7. No dependence on a single keyword.
8. No accidental future-only interpretation.
9. No accidental completion interpretation.
10. No unrelated dialogue-purpose or persuasion-barrier substitution.

---

# 31. Human–LLM–Code Allocation

## Human responsibility

Humans verify:

- execution genuinely began;
- completion genuinely has not occurred;
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

# 32. Stage 1 Anchor Completion Criteria

The In Progress anchor resource is complete when:

- all 15 scenarios have three anchors;
- total anchor count is 45;
- every anchor maps to `In Progress`;
- every anchor preserves its parent scenario;
- all five In Progress subtypes are represented;
- explicit, natural, and contextual prototypes are represented;
- every anchor establishes execution initiation;
- every anchor preserves unfinished execution;
- partial execution is not treated as completion;
- near completion is not treated as completion;
- interruption after initiation is not treated as `Not Started`;
- lexical shortcuts are not required to identify the state.

---

# 33. Output Summary

```text
State: In Progress

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

For every anchor in this file, execution has begun but the target task remains unfinished.

The invariant is:

```text
execution_started = true
execution_completed = false
        ↓
In Progress
```
