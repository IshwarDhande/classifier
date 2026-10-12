# Execution Status Dataset — Semantic Subtype Catalogue

## 1. Purpose

This document defines the **semantic subtype layer** for the Execution Status dataset.

The subtype layer is a **construction artifact**, not an additional classifier label layer. Its purpose is to partition the frozen Execution Status semantic space into sufficiently distinct regions so that Stage 1 can construct balanced, semantically grounded execution scenarios before linguistic expansion and boundary construction.

The frozen output states remain:

- `Not Started`
- `In Progress`
- `Completed`

The subtype catalogue must never override these three states.

---

## 2. Construction Principle

Execution Status is determined by the user's **actual execution state of the target task**, not by:

- intention alone,
- scheduling,
- deadline information,
- reasons for non-execution,
- motivation,
- persuasion barriers,
- dialogue purpose,
- sentiment,
- response category,
- task-manager status.

The central decision hierarchy is:

1. **Has the task been completed?**
   - Yes → `Completed`
2. **If not, has execution begun?**
   - Yes → `In Progress`
3. **Otherwise**
   - `Not Started`

Subtypes exist to expose the semantic regions that must be represented during dataset construction. They are not intended to become additional production labels.

---

## 3. Working Construction Target

The current dataset construction plan uses a working target of:

| Execution state | Working subtype target |
|---|---:|
| Not Started | 5 |
| In Progress | 5 |
| Completed | 5 |
| **Total** | **15** |

This is a **planning target**, not an ontology constraint.

Subtype count must remain subordinate to semantic coverage. A subtype should exist only when it represents a meaningful and distinguishable execution region. Conversely, closely related regions may be grouped when separating them would create artificial distinctions.

The catalogue below therefore provides the current **15-subtype working inventory** while retaining coverage for the additional semantic regions identified in the Stage 1 construction plan.

---

# 4. Not Started — Subtype Catalogue

## NS-01 — Direct Non-Execution

### Definition

The target task has **not begun**, and the utterance directly indicates that the user is not currently executing it.

### Core semantic condition

`execution_started = false`

### Typical realization regions

- Explicit statement that the task has not been done.
- Statement that the user has not started.
- Statement that the task remains untouched.
- Current non-execution without a separate future commitment.

### Positive inclusion criteria

Include when:

- the target task has clearly not begun;
- no evidence of partial execution exists;
- no completion evidence exists.

### Exclusion criteria

Do not use when:

- execution has already begun → `In Progress`;
- the task is explicitly complete → `Completed`;
- the utterance only states a future intention without current execution evidence → NS-02;
- the user explicitly refuses → NS-04;
- the non-execution is primarily expressed through a reason/barrier → NS-05.

### Semantic examples

- “I haven’t started it.”
- “I haven’t done the exercise yet.”
- “I’m not doing it right now.”

---

## NS-02 — Future / Deferred Action

### Definition

The user has **not started execution** but refers to performing the task at a later point.

### Core semantic condition

`execution_started = false`

with a future/deferred temporal orientation.

### Typical realization regions

- Future intention.
- Deferred action.
- Later action.
- Postponed start.

### Positive inclusion criteria

Include when:

- execution has not begun;
- the utterance places execution in the future or later;
- the future statement does not itself provide evidence of current execution.

### Exclusion criteria

Do not use when:

- execution is already underway → `In Progress`;
- completion is reported → `Completed`;
- the statement is conditional rather than straightforwardly future → NS-03.

### Important distinction

Future intention does **not** constitute execution initiation.

For example:

> “I’ll take the medicine tonight.”

remains `Not Started`.

### Semantic examples

- “I’ll do it later.”
- “I’m going to start the exercises tonight.”
- “I’ll take the dose after dinner.”

---

## NS-03 — Conditional Future Action

### Definition

The user has **not started execution** and describes execution as dependent on a future condition.

### Core semantic condition

`execution_started = false`

with execution contingent on an explicit or implicit condition.

### Typical realization regions

- “If X happens, I’ll do Y.”
- “Once X is done, I’ll start.”
- “When I get home, I’ll exercise.”

### Positive inclusion criteria

Include when:

- the task has not begun;
- execution is presented as contingent on a condition;
- no current execution evidence exists.

### Exclusion criteria

Do not use when:

- execution has already started;
- completion is reported;
- the condition is merely a reason explaining non-execution without expressing conditional future execution → NS-05.

### Semantic examples

- “If I get some time, I’ll do the exercises.”
- “Once I get home, I’ll take the medicine.”
- “When I finish work, I’ll go for the walk.”

---

## NS-04 — Refusal Without Execution

### Definition

The user explicitly declines, rejects, or refuses the target task while **no execution has begun**.

### Core semantic condition

`execution_started = false`

with explicit refusal/rejection.

### Positive inclusion criteria

Include when:

- the target task has not begun;
- the user explicitly rejects, refuses, or declines execution.

### Exclusion criteria

Do not use when:

- the user has already started and then stops → `In Progress` at the current execution state if execution remains unfinished;
- the utterance merely gives a reason for not acting without explicit refusal → NS-05;
- the user says they will act later → NS-02.

### Important distinction

Refusal is not a separate production state.

A refusal remains `Not Started` because execution has not begun.

### Semantic examples

- “I’m not going to do it.”
- “No, I won’t take it.”
- “I don’t want to do the exercise.”

---

## NS-05 — Reason-Linked Non-Execution

### Definition

The user has **not started execution** and explains the non-execution through a reason, barrier, inability, unavailability, forgetting, low motivation, or similar condition.

### Core semantic condition

`execution_started = false`

with a reason or barrier associated with non-execution.

### Coverage regions

This subtype provides construction coverage for:

- being busy;
- lack of time;
- inability or unavailability;
- forgetting;
- low motivation;
- other reason-linked non-execution.

These reasons are **not themselves Execution Status labels**.

### Positive inclusion criteria

Include when:

- the task has not begun;
- the utterance provides a reason, barrier, or explanation for the non-execution.

### Exclusion criteria

Do not use when:

- execution has begun → `In Progress`;
- completion is reported → `Completed`;
- the utterance contains only a future intention without a reason → NS-02;
- the utterance is an explicit refusal without a substantive reason → NS-04.

### Important distinction

The reason may be relevant to the separate Persuasion Barrier ontology, but the Execution Status remains `Not Started`.

### Semantic examples

- “I’m too busy to do it right now.”
- “I forgot to take it.”
- “I couldn’t exercise because I wasn’t feeling up to it.”

---

# 5. In Progress — Subtype Catalogue

## IP-01 — Direct Ongoing Execution

### Definition

The user is **currently performing the target task**, and execution has begun but is not complete.

### Core semantic condition

`execution_started = true`

and `execution_completed = false`

### Typical realization regions

- Current action.
- Active performance.
- “Doing it now.”
- Ongoing execution.

### Positive inclusion criteria

Include when:

- there is direct evidence that execution has started;
- completion has not occurred.

### Exclusion criteria

Do not use when:

- the user merely intends to start → `Not Started`;
- the task is complete → `Completed`.

### Semantic examples

- “I’m taking it now.”
- “I’m doing the exercises.”
- “I’m drinking the water now.”

---

## IP-02 — Partial Execution

### Definition

The user has completed **part of the target task**, while some execution remains unfinished.

### Core semantic condition

`execution_started = true`

`execution_completed = false`

with explicit partial completion.

### Typical realization regions

- Some amount completed.
- Part of a multi-step task performed.
- Started but not finished.
- Partial quantity completed.

### Positive inclusion criteria

Include when:

- execution has clearly begun;
- only part of the task has been completed.

### Exclusion criteria

Do not use when:

- the task has not begun;
- all required execution is complete.

### Semantic examples

- “I’ve done half of the exercises.”
- “I took one part of the dose, but I’m not finished.”
- “I’ve started drinking it, but there’s still some left.”

---

## IP-03 — Near Completion

### Definition

Execution has begun and the task is **almost finished**, but completion has not yet occurred.

### Core semantic condition

`execution_started = true`

`execution_completed = false`

with little remaining execution.

### Positive inclusion criteria

Include when:

- execution is underway;
- the user explicitly indicates that completion is close;
- completion has not yet been reached.

### Exclusion criteria

Do not use when:

- the user says the task is finished → `Completed`;
- the user only plans to begin → `Not Started`.

### Critical boundary

“Almost done” remains `In Progress`.

### Semantic examples

- “I’m almost finished.”
- “Just one more set.”
- “I’m nearly done with it.”

---

## IP-04 — Multi-Step Execution

### Definition

The target task consists of multiple execution steps, and the user has begun the sequence but has not completed all required steps.

### Core semantic condition

`execution_started = true`

`execution_completed = false`

with multiple execution components.

### Positive inclusion criteria

Include when:

- at least one execution step has begun or been completed;
- at least one required execution step remains.

### Exclusion criteria

Do not use when:

- the user has only planned the sequence;
- every required step is complete.

### Semantic examples

- “I’ve done the first two exercises; I still have one left.”
- “I took the first part and still need to finish the rest.”
- “I’ve started the physiotherapy routine but haven’t completed all the steps.”

---

## IP-05 — Temporarily Interrupted Execution

### Definition

The user has **already begun execution**, but execution is temporarily paused or interrupted before completion.

### Core semantic condition

`execution_started = true`

`execution_completed = false`

with an interruption after initiation.

### Positive inclusion criteria

Include when:

- execution began;
- execution is unfinished;
- the user reports a pause, interruption, or temporary stop.

### Exclusion criteria

Do not use when:

- execution never began;
- the user completed the task before the interruption;
- the user merely intends to start later.

### Important distinction

An interruption after execution begins does not reset the execution state to `Not Started`.

### Semantic examples

- “I started the exercise but had to stop for a minute.”
- “I was taking it, but I paused.”
- “I began the routine and got interrupted.”

---

# 6. Completed — Subtype Catalogue

## C-01 — Direct Completion

### Definition

The user explicitly states that the target task has been completed.

### Core semantic condition

`execution_completed = true`

### Typical realization regions

- Direct completion statement.
- “Done.”
- “Finished.”
- “I completed it.”

### Positive inclusion criteria

Include when:

- completion is directly asserted;
- there is no semantic indication that the task remains unfinished.

### Exclusion criteria

Do not use when:

- execution is still underway;
- only intention is expressed;
- only part of the task is complete.

### Semantic examples

- “Done.”
- “I finished the exercise.”
- “I took the medicine.”

---

## C-02 — Retrospective Completion

### Definition

The user reports that the target task was completed **at an earlier point**.

### Core semantic condition

`execution_completed = true`

with retrospective temporal orientation.

### Positive inclusion criteria

Include when:

- the user looks back on a completed execution;
- completion is established by the utterance.

### Exclusion criteria

Do not use when:

- the utterance only describes future completion;
- execution is currently ongoing;
- completion is uncertain.

### Semantic examples

- “I already did it.”
- “I took it earlier.”
- “I finished the exercises this morning.”

---

## C-03 — Indirect Completion

### Definition

The user does not necessarily use an explicit completion verb, but the utterance provides sufficient evidence that the target task has finished.

### Core semantic condition

`execution_completed = true`

derived from the semantic content of the utterance rather than a direct completion expression.

### Positive inclusion criteria

Include when:

- the utterance entails that the target execution is complete;
- completion is not dependent on mere intention.

### Exclusion criteria

Do not use when:

- the evidence only indicates initiation or partial progress;
- the completion inference is speculative.

### Semantic examples

- “The whole bottle is empty.”
- “All five sets are done.”
- “There’s nothing left for me to take.”

### Construction caution

Indirect completion examples must be semantically unambiguous. Dataset construction must not rely on world knowledge that is unnecessary for interpreting the target execution state.

---

## C-04 — Multi-Step Completion

### Definition

The user indicates that **all required execution steps** of a multi-step task have been completed.

### Core semantic condition

`execution_completed = true`

with completion across multiple required components.

### Positive inclusion criteria

Include when:

- the task has multiple execution components;
- all relevant components are completed.

### Exclusion criteria

Do not use when:

- one or more required steps remain;
- only the first or some steps are completed.

### Semantic examples

- “I finished all the exercises.”
- “I completed every part of the routine.”
- “I’ve taken all the required doses for today.”

---

## C-05 — Completion with Additional Commentary

### Definition

The user explicitly establishes completion while adding additional information that is not itself the execution-status signal.

### Core semantic condition

`execution_completed = true`

with additional commentary.

### Typical additional content

- reaction after completion;
- evaluation of the task;
- contextual information;
- explanation;
- conversational follow-up.

### Positive inclusion criteria

Include when:

- completion is clearly established;
- additional commentary follows or accompanies the completion statement.

### Exclusion criteria

Do not use when:

- the additional commentary creates uncertainty about whether completion occurred;
- completion is only implied by future intention.

### Semantic examples

- “I finished the exercises, and they were tiring.”
- “Done with the medicine; I’m going to rest now.”
- “I completed the routine, although it took longer than expected.”

---

# 7. Cross-State Semantic Boundaries

The subtype catalogue must preserve the three principal Execution Status boundaries.

## B01 — Not Started ↔ In Progress

The decisive question is:

> Has execution actually begun?

Examples:

| Utterance | State |
|---|---|
| “I’ll start after lunch.” | Not Started |
| “I’m starting it now.” | In Progress |
| “I haven’t started yet.” | Not Started |
| “I’ve started, but I’m not finished.” | In Progress |

Future intention, preparation, or willingness must not be treated as execution unless the utterance provides evidence that execution has actually begun.

---

## B02 — In Progress ↔ Completed

The decisive question is:

> Is execution still unfinished?

Examples:

| Utterance | State |
|---|---|
| “I’m almost done.” | In Progress |
| “I’m on the last set.” | In Progress |
| “I finished the last set.” | Completed |
| “All done.” | Completed |

Near completion is still `In Progress`.

---

## B03 — Not Started ↔ Completed

The decisive question is:

> Is there evidence that execution occurred and finished?

Examples:

| Utterance | State |
|---|---|
| “I haven’t taken it.” | Not Started |
| “I’ll take it later.” | Not Started |
| “I already took it.” | Completed |
| “It’s done.” | Completed |

---

# 8. Subtype Orthogonality

The subtype system must not introduce additional production dimensions.

The following distinctions remain outside the Execution Status label space:

### Planning

Statements about plans, schedules, or intended future actions do not imply execution.

### Temporal status

“Late,” “overdue,” “missed,” “delayed,” and similar task-manager concepts are not Execution Status labels.

### Reasons and barriers

Busy, tired, forgetful, unmotivated, unavailable, or unable are reasons for the execution state, not replacement execution states.

### Dialogue purpose

A commitment, refusal, explanation, acknowledgement, or other dialogue purpose must not determine Execution Status independently of execution evidence.

### Response category

Positive or negative appraisal of the reminder must not determine whether execution has started or finished.

---

# 9. Task-Domain Coverage

Every subtype must be instantiated across the frozen task domains where the semantic construction is naturally applicable:

1. Medication
2. Hydration
3. Exercise
4. Physiotherapy

Task domain is a **content dimension**, not an Execution Status subtype.

The same execution semantics should be expressible across multiple domains to prevent the classifier from learning domain-specific shortcuts.

---

# 10. Conversational Context

Subtype construction should include both:

- semantically self-contained utterances;
- utterances whose execution state is clear in a short conversational context.

Context must not change the underlying Execution Status definition.

The target remains:

> What is the current execution state of the target task based on the user's latest utterance?

When context is used, the dataset must preserve the distinction between:

- execution evidence;
- intention;
- explanation;
- dialogue function.

---

# 11. Semantic Difficulty Within Each Subtype

Each subtype should eventually support multiple levels of linguistic and semantic difficulty.

### Level 1 — Explicit

Execution status is directly stated.

### Level 2 — Natural conversational

Execution status is expressed through ordinary conversational wording.

### Level 3 — Implicit

Execution status must be inferred from the described execution event.

### Level 4 — Distractor-rich

The utterance contains additional information that should not override the execution signal.

These difficulty levels are construction targets for later linguistic expansion and boundary resources. They should not create additional semantic subtypes.

---

# 12. Subtype Metadata

Each Stage 1 subtype should be documented using the following metadata:

```yaml
subtype_id:
state:
subtype_name:
definition:
core_execution_condition:
semantic_dimensions:
inclusion_criteria:
exclusion_criteria:
coverage_regions:
boundary_risks:
task_domains:
construction_notes:
```

For individual scenarios, subtype membership should be retained as construction metadata while the final classifier-facing state remains one of:

```yaml
execution_status:
  - Not Started
  - In Progress
  - Completed
```

---

# 13. Catalogue Summary

| ID | State | Subtype |
|---|---|---|
| NS-01 | Not Started | Direct Non-Execution |
| NS-02 | Not Started | Future / Deferred Action |
| NS-03 | Not Started | Conditional Future Action |
| NS-04 | Not Started | Refusal Without Execution |
| NS-05 | Not Started | Reason-Linked Non-Execution |
| IP-01 | In Progress | Direct Ongoing Execution |
| IP-02 | In Progress | Partial Execution |
| IP-03 | In Progress | Near Completion |
| IP-04 | In Progress | Multi-Step Execution |
| IP-05 | In Progress | Temporarily Interrupted Execution |
| C-01 | Completed | Direct Completion |
| C-02 | Completed | Retrospective Completion |
| C-03 | Completed | Indirect Completion |
| C-04 | Completed | Multi-Step Completion |
| C-05 | Completed | Completion with Additional Commentary |

**Total working subtype inventory: 15**

---

# 14. Relationship to Stage 1 Scenario Construction

The subtype catalogue is the bridge between the semantic dimensions and the Stage 1 scenario inventory:

```text
Frozen Execution Status Ontology
            ↓
Execution Semantic Dimensions
            ↓
Semantic Subtype Catalogue
            ↓
Subtype × Task Domain Coverage
            ↓
Execution Scenarios
            ↓
Initial Anchors
```

Each Stage 1 scenario should be assigned:

- one execution state;
- one primary semantic subtype;
- one or more execution dimensions;
- one task domain;
- sufficient context to establish the intended execution state.

Scenarios should be constructed from the semantic subtype definition rather than from lexical examples.

---

# 15. Construction Rules

1. **Do not construct subtypes from keywords.**
   - “started,” “done,” “later,” etc. are lexical realizations, not subtype definitions.

2. **Do not use reasons as states.**
   - Busy, forgetting, low motivation, or inability remain reasons for `Not Started` when execution has not begun.

3. **Do not use intention as execution.**
   - Future commitments remain `Not Started`.

4. **Do not collapse partial execution into completion.**
   - Any unfinished execution remains `In Progress`.

5. **Do not reset interrupted execution to Not Started.**
   - Once execution has begun, a temporary interruption remains within `In Progress` until completion.

6. **Do not infer completion from willingness.**
   - “I will finish it” is not completion.

7. **Do not infer execution from preparation alone.**
   - Preparation should only count as execution when the task definition itself makes the preparation an execution step.

8. **Do not create artificial subtype distinctions.**
   - Subtypes must correspond to meaningful semantic regions.

9. **Do not force equal subtype counts if semantic validation later shows otherwise.**
   - The 5-per-state inventory is a working construction target.

10. **Keep the production ontology frozen.**
    - Final classifier output remains exactly:
      `Not Started`, `In Progress`, `Completed`.

---

# 16. Completion Criteria for the Subtype Catalogue

The subtype catalogue is ready for Stage 1 scenario construction when:

- all three frozen execution states are represented;
- all major execution dimensions identified in the semantic-dimensions document are covered;
- the Not Started subtype layer covers direct non-execution, future/deferred action, conditional action, refusal, and reason-linked non-execution;
- the In Progress subtype layer covers ongoing, partial, near-complete, multi-step, and interrupted execution;
- the Completed subtype layer covers direct, retrospective, indirect, multi-step, and commentary-bearing completion;
- every subtype has a clear execution condition;
- inclusion and exclusion criteria are explicit;
- major cross-state boundaries are represented;
- subtype definitions do not depend on lexical cues;
- subtypes remain construction artifacts rather than production labels;
- the frozen three-state ontology is preserved.

---

## Final Principle

**The subtype catalogue defines the semantic regions from which scenarios are constructed; it does not expand the Execution Status ontology.**

The final classifier still answers one question:

> **What is the current execution state of the target task?**

with exactly one of:

`Not Started` · `In Progress` · `Completed`
