# Execution Status Dataset — Stage 1 Semantic Scenarios: Completed

## 1. Purpose

This document defines the Stage 1 semantic scenario inventory for the frozen Execution Status state:

> **Completed**

The scenarios represent situations in which execution of the target task **has finished**.

The production label remains:

```yaml
execution_status: Completed
```

The scenario inventory provides semantic coverage before linguistic expansion, boundary construction, and hard-negative generation.

---

# 2. Stage 1 Construction Principle

The central condition for every `Completed` scenario is:

```text
execution_started = true
execution_completed = true
```

The wording may differ substantially, but the underlying execution event must establish that the target task has finished.

The scenarios distinguish:

- direct completion;
- retrospective completion;
- indirect completion;
- multi-step completion;
- completion with additional commentary.

These distinctions are semantic construction regions, not additional production labels.

---

# 3. Working Scenario Target

The working Stage 1 target is:

| Item | Target |
|---|---:|
| Completed subtypes | 5 |
| Scenarios per subtype | 3 |
| Total semantic scenarios | **15** |
| Initial anchors per scenario | 3 |
| Initial anchor capacity | **45** |

The 15 scenarios below form the working semantic inventory.

The target is a construction planning number rather than a requirement to manufacture artificial distinctions.

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
execution_status: Completed
scenario_id:
anchor_type:
```

---

# 5. C-01 — Direct Completion

## Scenario C-S01 — Explicit Completion

### Subtype

`C-01 Direct Completion`

### Scenario definition

The user explicitly states that the target task has been completed.

### Execution condition

```text
execution_started = true
execution_completed = true
```

### Core semantic meaning

The target execution has finished.

### Task-domain instantiations

- Medication: dose has been taken.
- Hydration: target water intake has been consumed.
- Exercise: exercise session has been completed.
- Physiotherapy: therapy routine has been completed.

### Primary boundary

`In Progress ↔ Completed`

### Secondary boundary

`Not Started ↔ Completed`

### Example semantic realizations

- “I finished the exercise.”
- “I took the medicine.”
- “I completed the therapy routine.”

### Construction constraint

Completion must be asserted, not merely intended.

---

## Scenario C-S02 — Done / Finished State

### Subtype

`C-01 Direct Completion`

### Scenario definition

The user uses a concise completion expression that establishes that the target task is finished.

### Execution condition

```text
execution_started = true
execution_completed = true
```

### Core semantic meaning

The execution lifecycle has reached completion.

### Boundary risk

Short completion expressions must be interpreted with the target task established by context where necessary.

### Example semantic realizations

- “Done.”
- “Finished.”
- “All done with it.”

### Construction constraint

The target task must be recoverable from the immediate context when the utterance itself is short.

---

## Scenario C-S03 — Explicit Completion With Task Reference

### Subtype

`C-01 Direct Completion`

### Scenario definition

The user directly states completion while explicitly referring to the target task.

### Execution condition

```text
execution_started = true
execution_completed = true
```

### Core semantic meaning

The target task, rather than an unrelated activity, has finished.

### Example semantic realizations

- “I’ve finished my exercises.”
- “I’m done with the physiotherapy.”
- “I’ve taken the dose.”

### Construction constraint

The task reference must be semantically tied to the target task.

---

# 6. C-02 — Retrospective Completion

## Scenario C-S04 — Completed Earlier

### Subtype

`C-02 Retrospective Completion`

### Scenario definition

The user reports that the target task was completed earlier.

### Execution condition

```text
execution_started = true
execution_completed = true
```

### Core semantic meaning

Completion occurred before the current conversational moment.

### Primary boundary

`Not Started ↔ Completed`

### Example semantic realizations

- “I already did it.”
- “I took it earlier.”
- “I finished the exercise this morning.”

### Construction constraint

The past reference must indicate actual completion, not merely a past intention.

---

## Scenario C-S05 — Earlier Completion With Temporal Reference

### Subtype

`C-02 Retrospective Completion`

### Scenario definition

The user gives a temporal reference to a completed execution event.

### Execution condition

```text
execution_started = true
execution_completed = true
```

### Core semantic meaning

The target task is complete despite the execution occurring earlier.

### Example semantic realizations

- “I did it before breakfast.”
- “I completed the routine a while ago.”
- “I took the medicine earlier today.”

### Construction constraint

The temporal expression must locate a completed execution event rather than a planned one.

---

## Scenario C-S06 — Retrospective Completion After Reminder

### Subtype

`C-02 Retrospective Completion`

### Scenario definition

In conversational context, the user indicates that the target task was already completed before the current reminder or dialogue turn.

### Execution condition

```text
execution_started = true
execution_completed = true
```

### Core semantic meaning

The reminder does not imply that the task is currently unexecuted; the user reports prior completion.

### Example semantic realizations

- “I already took it.”
- “I did that earlier.”
- “That’s already finished.”

### Construction constraint

The response must establish prior completion rather than simply acknowledge the reminder.

---

# 7. C-03 — Indirect Completion

## Scenario C-S07 — Completion Through Result State

### Subtype

`C-03 Indirect Completion`

### Scenario definition

The user does not necessarily use an explicit completion verb but describes a resulting state that establishes that the target task has finished.

### Execution condition

```text
execution_started = true
execution_completed = true
```

### Core semantic meaning

The described result is sufficient evidence that execution is complete.

### Primary boundary

`In Progress ↔ Completed`

### Example semantic realizations

- “The bottle is empty now.”
- “There’s nothing left to drink.”
- “All the exercises are done.”

### Construction constraint

The result state must provide sufficient evidence of completion without requiring speculative inference.

---

## Scenario C-S08 — Completion Through Exhausted Required Quantity

### Subtype

`C-03 Indirect Completion`

### Scenario definition

The user indicates that the required quantity or target amount has been fully consumed or performed.

### Execution condition

```text
execution_started = true
execution_completed = true
```

### Core semantic meaning

The execution target has been fully reached.

### Example semantic realizations

- “I finished the whole bottle.”
- “I completed all the required movement.”
- “I got through the full exercise.”

### Construction constraint

The utterance must indicate the entire required target, not only a portion.

---

## Scenario C-S09 — Completion Through Consequential State

### Subtype

`C-03 Indirect Completion`

### Scenario definition

The user describes a state that logically follows from the completed execution and establishes that no target execution remains.

### Execution condition

```text
execution_started = true
execution_completed = true
```

### Core semantic meaning

The target task has ended even without a canonical completion verb.

### Example semantic realizations

- “There’s nothing left for me to do on the routine.”
- “The entire dose is taken.”
- “The session is over.”

### Construction constraint

The completion inference must be grounded in the utterance and immediate context, not broad external assumptions.

---

# 8. C-04 — Multi-Step Completion

## Scenario C-S10 — All Required Steps Completed

### Subtype

`C-04 Multi-Step Completion`

### Scenario definition

The target task consists of multiple required steps, and the user establishes that all steps are complete.

### Execution condition

```text
execution_started = true
execution_completed = true
```

with:

```text
completed_steps = total_required_steps
```

### Core semantic meaning

The complete multi-step execution sequence has finished.

### Primary boundary

`In Progress ↔ Completed`

### Example semantic realizations

- “I finished all the exercises.”
- “I completed every part of the routine.”
- “I did all the steps.”

### Construction constraint

All required steps must be complete.

---

## Scenario C-S11 — Final Step Completed

### Subtype

`C-04 Multi-Step Completion`

### Scenario definition

The user indicates that the final remaining step of a multi-step task has been completed.

### Execution condition

```text
execution_started = true
execution_completed = true
```

### Core semantic meaning

Completion occurs because the last required component has been finished.

### Example semantic realizations

- “I just finished the last set.”
- “The final exercise is done.”
- “I completed the last part of the routine.”

### Construction constraint

The utterance should establish that no required execution step remains.

---

## Scenario C-S12 — Multi-Step Completion With Full-Sequence Reference

### Subtype

`C-04 Multi-Step Completion`

### Scenario definition

The user refers to completion of the entire execution sequence rather than a single component.

### Execution condition

```text
execution_started = true
execution_completed = true
```

### Core semantic meaning

The complete target sequence has been executed.

### Example semantic realizations

- “I’ve gone through the whole routine.”
- “I finished the entire exercise session.”
- “I completed all of it.”

### Construction constraint

Do not use if the utterance only establishes completion of one component.

---

# 9. C-05 — Completion With Additional Commentary

## Scenario C-S13 — Completion Plus Reaction

### Subtype

`C-05 Completion with Additional Commentary`

### Scenario definition

The user explicitly establishes completion and then adds a reaction, evaluation, or observation.

### Execution condition

```text
execution_started = true
execution_completed = true
```

### Core semantic meaning

Completion is the execution signal; the additional reaction is secondary.

### Primary boundary

`In Progress ↔ Completed`

### Example semantic realizations

- “I finished the exercises; they were tiring.”
- “I’m done with the routine, and that was harder than expected.”
- “I took the medicine, and now I’m going to rest.”

### Construction constraint

The commentary must not introduce uncertainty about completion.

---

## Scenario C-S14 — Completion Plus Context

### Subtype

`C-05 Completion with Additional Commentary`

### Scenario definition

The user reports completion while adding contextual information about when, where, or under what circumstances it occurred.

### Execution condition

```text
execution_started = true
execution_completed = true
```

### Core semantic meaning

The contextual information accompanies a completed execution event.

### Example semantic realizations

- “I finished the exercise before breakfast.”
- “I took the medicine at home and I’m done now.”
- “I completed the routine earlier, so I’m free now.”

### Construction constraint

Context must support completion rather than merely describing a plan.

---

## Scenario C-S15 — Completion Plus Follow-Up Action

### Subtype

`C-05 Completion with Additional Commentary`

### Scenario definition

The user establishes completion and then describes what they will do afterward.

### Execution condition

```text
execution_started = true
execution_completed = true
```

### Core semantic meaning

The target task is complete; the follow-up action is a separate future event.

### Example semantic realizations

- “I finished the exercises; now I’ll take a break.”
- “I took the dose, and I’ll have breakfast now.”
- “I completed the therapy, so I’m going to rest.”

### Construction constraint

The future follow-up action must not be confused with the completion status of the target task.

---

# 10. Scenario Coverage Matrix

| Scenario | Subtype | Core semantic region | Primary boundary |
|---|---|---|---|
| C-S01 | C-01 | Explicit completion | IP ↔ C |
| C-S02 | C-01 | Done / finished expression | IP ↔ C |
| C-S03 | C-01 | Explicit task completion | IP ↔ C |
| C-S04 | C-02 | Completed earlier | NS ↔ C |
| C-S05 | C-02 | Temporal retrospective completion | NS ↔ C |
| C-S06 | C-02 | Completion before current reminder | NS ↔ C |
| C-S07 | C-03 | Result-state completion | IP ↔ C |
| C-S08 | C-03 | Full required quantity | IP ↔ C |
| C-S09 | C-03 | Consequential completion state | IP ↔ C |
| C-S10 | C-04 | All steps complete | IP ↔ C |
| C-S11 | C-04 | Final step complete | IP ↔ C |
| C-S12 | C-04 | Full sequence complete | IP ↔ C |
| C-S13 | C-05 | Completion + reaction | IP ↔ C |
| C-S14 | C-05 | Completion + context | IP ↔ C |
| C-S15 | C-05 | Completion + follow-up | IP ↔ C |

---

# 11. Task-Domain Coverage

The semantic scenarios should be instantiated across the frozen task domains:

1. Medication
2. Hydration
3. Exercise
4. Physiotherapy

The task domain must remain independent of the completion subtype.

Examples:

| Semantic region | Possible domains |
|---|---|
| Direct completion | Medication, hydration, exercise, physiotherapy |
| Retrospective completion | Medication, hydration, exercise, physiotherapy |
| Indirect completion | Hydration, medication, exercise |
| Multi-step completion | Exercise, physiotherapy, medication |
| Completion + commentary | Medication, hydration, exercise, physiotherapy |

The final anchors should rotate task domains so that domain-specific vocabulary does not become a shortcut for `Completed`.

---

# 12. Critical Semantic Distinctions

## 12.1 Future intention vs completed execution

```text
“I’ll take it tonight.”
→ Not Started

“I already took it.”
→ Completed
```

Future intention provides no completion evidence.

---

## 12.2 Ongoing execution vs completion

```text
“I’m still doing the exercises.”
→ In Progress

“I finished the exercises.”
→ Completed
```

Completion requires that no required execution remains.

---

## 12.3 Near completion vs completion

```text
“I’m almost finished.”
→ In Progress

“I’m finished.”
→ Completed
```

The final portion matters.

---

## 12.4 Partial completion vs full completion

```text
“I did three of five sets.”
→ In Progress

“I did all five sets.”
→ Completed
```

The completed portion must cover the full target.

---

## 12.5 Interrupted execution vs completed execution

```text
“I started but had to stop.”
→ In Progress

“I finished before I stopped.”
→ Completed
```

An interruption does not itself establish completion.

---

## 12.6 Forgetting vs retrospective completion

```text
“I forgot to take it.”
→ Not Started

“I took it earlier.”
→ Completed
```

The relevant distinction is whether the task was actually executed.

---

# 13. Indirect Completion Construction Rules

Indirect completion is a high-value semantic region but must be constructed conservatively.

An indirect example should satisfy:

1. The utterance establishes a result or state that entails completion.
2. The inference does not depend on obscure world knowledge.
3. The target task is recoverable.
4. No unfinished component is implied.
5. The interpretation remains stable under ordinary conversational reading.

Avoid examples where completion requires guessing.

For example:

> “The bottle is empty.”

may establish completed hydration only when the task definition and context establish that the relevant target was to consume the bottle.

The dataset should not rely on assumptions that are unavailable to the classifier.

---

# 14. Completion With Additional Commentary

Additional commentary must not become the classification target.

For example:

> “I finished the exercises; they were exhausting.”

The execution signal is:

```text
finished the exercises
```

The additional sentiment/evaluation is not part of Execution Status.

Likewise:

> “I took the medicine, and now I’m going to sleep.”

The execution signal is:

```text
took the medicine
```

The future sleep action is a separate event.

This structure is useful for preventing the classifier from relying only on isolated completion phrases.

---

# 15. Lexical Shortcut Prevention

The dataset must not learn simplistic mappings such as:

- “done” → `Completed`;
- “finished” → `Completed`;
- “already” → `Completed`;
- “all” → `Completed`;
- “empty” → `Completed`.

These expressions can appear in semantically different contexts.

For example:

> “I’m not done yet.”

contains “done” but is `In Progress`.

Similarly:

> “I’ll finish it later.”

contains “finish” but is `Not Started` if execution has not begun.

Therefore the underlying execution semantics remain authoritative.

---

# 16. Conversational Context

Completed scenarios may use short conversational context to establish:

- the target task;
- what “done” refers to;
- the timing of prior completion;
- which sequence has been completed;
- the relationship between completion and follow-up commentary.

Context must not manufacture completion that is absent from the intended scenario.

For concise responses such as:

> “Done.”

the immediate context must clearly identify the target task.

---

# 17. Initial Anchor Construction

Each scenario should receive three initial anchors:

### Anchor A — Explicit Prototype

Directly states that the target task has been completed.

### Anchor B — Natural Prototype

Expresses completion using natural conversational language.

### Anchor C — Less Explicit / Contextual Prototype

Establishes completion through a less canonical expression while preserving sufficient semantic evidence.

All three must preserve:

```yaml
execution_started: true
execution_completed: true
execution_status: Completed
```

No anchor should intentionally cross into `Not Started` or `In Progress`.

---

# 18. Boundary-Oriented Scenario Distribution

The Completed inventory deliberately covers both boundaries involving completion.

## In Progress ↔ Completed

Primary emphasis:

- explicit completion;
- indirect completion;
- multi-step completion;
- completion with commentary.

Primary scenarios:

```text
C-S01
C-S02
C-S03
C-S07
C-S08
C-S09
C-S10
C-S11
C-S12
C-S13
C-S14
C-S15
```

## Not Started ↔ Completed

Primary emphasis:

- retrospective completion;
- direct completion;
- explicit distinction between completed execution and future intention.

Primary scenarios:

```text
C-S01
C-S04
C-S05
C-S06
```

The overlap is intentional because both boundaries must be represented from the Completed side.

---

# 19. Scenario Deduplication

Scenarios should not be separated merely because their wording differs.

For example:

- “I finished it.”
- “It’s done.”
- “I’m done with it.”

may represent the same semantic region and should normally be handled through linguistic variation.

A separate scenario is justified when the execution semantics differ, such as:

- direct completion;
- retrospective completion;
- indirect completion;
- multi-step completion;
- completion with additional commentary.

---

# 20. Scenario Leakage Prevention

Every generated utterance must retain its semantic lineage:

```text
Completed
    ↓
Subtype
    ↓
Scenario
    ↓
Anchor
    ↓
Variant
```

Descendants of the same semantic scenario must remain identifiable for later group-based splitting.

A paraphrase of a completion scenario is not an independent semantic scenario.

---

# 21. Human–LLM–Code Allocation

## Human

Humans determine:

- whether completion genuinely occurred;
- whether all required execution is finished;
- whether an indirect result actually entails completion;
- whether the scenario is semantically distinct;
- whether the boundary is correctly represented.

## LLM

LLMs may assist with:

- natural conversational realization;
- paraphrasing;
- indirect completion wording;
- contextual variation;
- commentary-bearing utterances.

LLMs must preserve the predefined completion semantics.

## Code

Code should verify:

- metadata completeness;
- state/subtype consistency;
- scenario identifiers;
- anchor counts;
- duplicates;
- lineage;
- later split grouping.

---

# 22. Stage 1 Completion Criteria for Completed

The scenario inventory is ready for anchor construction when:

- all five Completed subtypes are represented;
- all 15 working scenarios have explicit semantic definitions;
- every scenario establishes completed execution;
- direct completion is covered;
- retrospective completion is covered;
- indirect completion is covered conservatively;
- multi-step completion is covered;
- completion with additional commentary is covered;
- the `In Progress ↔ Completed` boundary is represented;
- the `Not Started ↔ Completed` boundary is represented;
- task domains are distributed across scenarios;
- scenarios do not depend on completion keywords;
- future intentions are not treated as completion;
- partial or near completion is not treated as completion;
- interrupted execution is not treated as completion unless completion occurred before interruption;
- no scenario creates an additional production label.

---

# 23. Stage 1 Output

This file defines:

```text
5 working subtypes
15 semantic scenarios
3 initial anchors per scenario
45 initial anchor slots
```

The next construction resource is:

```text
s1/anchors/03_initial_anchors_completed.md
```

That file should realize these 15 semantic scenarios into three initial anchors per scenario while preserving the completion invariants.

---

# 24. Final Principle

**A Completed scenario is valid only when the target task has actually finished.**

Direct statements, retrospective reports, indirect result states, full multi-step execution, and completion with additional commentary may differ linguistically and structurally, but they belong to the same production state whenever the target execution is complete.

The Stage 1 objective is therefore:

> **Construct a semantically complete inventory of completed execution situations before introducing broad linguistic variation.**
