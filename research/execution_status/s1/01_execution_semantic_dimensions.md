# Execution Status — Execution Semantic Dimensions

## 1. Purpose

This document defines the semantic dimensions used for **Stage 1 — Semantic Coverage** of the Execution Status dataset.

The purpose is to expose the classifier to a broad range of execution situations rather than allowing the three labels to collapse around isolated temporal or status keywords.

The classifier must learn:

> **What is the current execution state of the target task?**

The frozen labels are:

```text
Not Started
In Progress
Completed
```

with lifecycle:

```text
Not Started → In Progress → Completed
```

The dimensions in this document are **construction dimensions**, not additional classifier labels.

---

## 2. Construction Hierarchy

```text
Frozen Execution Status
        ↓
Execution Semantic Dimensions
        ↓
Semantic Subtypes
        ↓
Semantic Scenarios
        ↓
Natural-Language Realizations
```

The dimensions define the semantic regions that the subtype catalogue and scenario inventory must cover.

They do not determine a fixed number of subtypes or scenarios.

---

## 3. Core Semantic Principle

Execution Status should primarily depend on:

1. whether execution has begun;
2. how much of the task has been executed;
3. whether work remains;
4. whether execution has finished.

It must not reduce to rules such as:

```text
"will"       → Not Started
"now"        → In Progress
"already"    → Completed
"done"       → Completed
"almost"     → In Progress
```

These expressions may be useful linguistic evidence, but the underlying execution situation determines the label.

---

# 4. Primary Execution Dimensions

## 4.1 Execution Initiation

**Definition:** Whether actual execution of the target task has begun.

Relevant regions:

```text
Not Begun
Begun
```

This is the primary semantic distinction between:

```text
Not Started
```

and:

```text
In Progress / Completed
```

Coverage should include:

- explicit non-execution;
- future intention without execution;
- planned but uninitiated action;
- conditional intention;
- current non-execution;
- explicit execution initiation;
- indirect evidence of initiation.

**Boundary:** Not Started ↔ In Progress

Central question:

> Has the target task actually begun?

---

## 4.2 Current Execution Activity

**Definition:** Whether the user is currently engaged in execution.

Relevant regions:

```text
No current execution
Active execution
Temporarily interrupted execution
```

`In Progress` should not be represented only through present-progressive wording. Active execution may be expressed indirectly.

A temporary pause remains `In Progress` when execution has already begun and the task remains unfinished.

---

## 4.3 Amount of Task Completed

**Definition:** How much of the target task has actually been executed.

Relevant regions:

```text
0% completed
Some portion completed
Most completed
100% completed
```

Conceptual mapping:

```text
0% completed
→ Not Started

Some / most completed but unfinished
→ In Progress

100% completed
→ Completed
```

Near-complete execution remains `In Progress` until execution actually finishes.

---

## 4.4 Remaining Work

**Definition:** Whether unfinished work remains.

Relevant regions:

```text
Entire task remains
Some work remains
Small amount remains
No work remains
```

Interpretation:

```text
Work remains + execution not begun
→ Not Started

Work remains + execution begun
→ In Progress

No work remains + execution finished
→ Completed
```

This dimension is especially important for the In Progress ↔ Completed boundary.

---

## 4.5 Partial Execution

**Definition:** Execution has begun but only part of the target task has been completed.

Examples of semantic situations:

- some repetitions completed;
- some exercises completed;
- part of a multi-step task completed;
- several components completed with work remaining;
- first part completed while later work remains.

Target state:

```text
In Progress
```

Core rule:

```text
Execution has begun
+
Execution is incomplete
=
In Progress
```

---

## 4.6 Multi-Step Execution

**Definition:** The target task contains multiple execution steps or components.

Relevant regions:

```text
No step started
Some steps completed
Current step underway
Most steps completed
All steps completed
```

Mapping:

```text
No step started
→ Not Started

One or more steps started but not all completed
→ In Progress

All required steps completed
→ Completed
```

This prevents completion of one component from being mistaken for completion of the target task.

---

## 4.7 Temporary Interruption

**Definition:** Execution has begun but is temporarily paused before completion.

Relevant situations:

- user started and paused;
- user was interrupted while executing;
- user reports completed work plus remaining work;
- user intends to resume after a pause.

Target:

```text
In Progress
```

provided:

```text
execution has begun
AND
target task remains unfinished
```

A purely future statement such as:

```text
"I'll start after lunch."
```

is not an interruption because execution has not begun.

---

## 4.8 Near Completion

**Definition:** Execution has progressed substantially but has not finished.

Relevant situations:

- almost finished;
- nearly done;
- final step remaining;
- most repetitions completed;
- small amount of work remaining.

Target:

```text
In Progress
```

Critical boundary:

```text
In Progress ↔ Completed
```

Words such as `almost` or `nearly` must not determine the label by themselves.

The semantic question is:

> Has execution actually finished?

---

## 4.9 Explicit Completion

**Definition:** The user explicitly indicates that execution of the target task has finished.

Relevant situations:

- task is finished;
- all required steps are complete;
- user explicitly reports completion;
- user says the task has been done.

Target:

```text
Completed
```

The completion evidence must refer to the target task rather than an unrelated task or subcomponent.

---

## 4.10 Retrospective Completion

**Definition:** The user reports that target-task execution was completed earlier.

Relevant situations:

- completed earlier today;
- completed before the conversation;
- completed previously;
- retrospective report of finished execution.

Target:

```text
Completed
```

The relevant question is whether execution has finished, not whether it is happening at the moment of the utterance.

---

## 4.11 Indirect Completion Evidence

**Definition:** Completion is established through a consequence, result, or contextual implication rather than a canonical completion word.

Relevant situations:

- reporting a result that presupposes completion;
- reporting a consequence of completed execution;
- answering a follow-up in a way that establishes completion;
- completion clear from dialogue context without saying `done` or `finished`.

Target:

```text
Completed
```

The dataset should not rely exclusively on:

```text
done
finished
completed
already
```

---

# 5. Non-Execution Dimensions

## 5.1 Future / Deferred Action

**Definition:** Execution will occur later, but has not begun.

Relevant situations:

- future intention;
- deferred action;
- postponed action;
- planned but uninitiated action.

Target:

```text
Not Started
```

Example:

```text
"I'll take it tonight."
→ Not Started
```

Future intention is not execution.

---

## 5.2 Conditional Future Action

**Definition:** Execution will occur only if a future condition is satisfied.

Examples:

```text
"I'll do it if I get time."
"I'll start once I get home."
"I can do it after I finish this."
```

Target, when execution has not begun:

```text
Not Started
```

This dimension prevents commitment or conditional planning from being interpreted as execution.

---

## 5.3 Current Non-Execution

**Definition:** The target task is not currently being executed and there is no evidence that execution has begun.

Relevant situations:

- user has not started;
- user is currently doing something else;
- user reports that the task is not being performed.

Target:

```text
Not Started
```

unless the utterance establishes that execution had already begun.

---

## 5.4 Refusal Without Execution

**Definition:** The user refuses to perform the target task without having begun execution.

Relevant situations:

- explicit refusal;
- unwillingness to start;
- rejection of the recommended action;
- statement that the user will not perform the task.

Target:

```text
Not Started
```

Refusal may simultaneously belong to another ontology, but Execution Status remains concerned with actual execution.

---

## 5.5 Inability or Unavailability Without Execution

**Definition:** The user cannot currently perform the target task and execution has not begun.

Relevant situations:

- lack of access;
- unavailable resources;
- current inability;
- circumstances preventing initiation.

Target:

```text
Not Started
```

The reason for non-execution may be represented by Persuasion Barrier, but it does not change Execution Status.

---

## 5.6 Forgetting Without Execution

**Definition:** The user reports forgetting to perform the target task and there is no evidence of execution.

Target:

```text
Not Started
```

Forgetting is a reason for non-execution, not a fourth Execution Status.

---

## 5.7 Reason-Linked Non-Execution

**Definition:** The user provides a reason explaining why the target task has not been performed.

Relevant reasons may include:

- being busy;
- lack of time;
- forgetting;
- inability;
- low motivation;
- refusal;
- lack of access;
- competing activity.

When there is no evidence that execution has begun:

```text
Reason-linked non-execution
→ Not Started
```

The classifier asks:

> Has the target task begun?

not:

> Why has the target task not begun?

---

# 6. Execution-State Coverage Matrix

| Semantic Dimension | Not Started | In Progress | Completed | Main Boundary |
|---|:---:|:---:|:---:|---|
| Execution initiation | ✓ | ✓ | ✓ | NS ↔ IP |
| Current execution activity | ✓ | ✓ | — | NS ↔ IP |
| Amount completed | 0% | Partial | 100% | IP ↔ C |
| Remaining work | Entire task | Some remains | None | IP ↔ C |
| Partial execution | — | ✓ | — | IP ↔ C |
| Multi-step execution | No step | Some steps | All steps | IP ↔ C |
| Temporary interruption | Possible* | ✓ | — | NS ↔ IP |
| Near completion | — | ✓ | — | IP ↔ C |
| Explicit completion | — | — | ✓ | IP ↔ C |
| Retrospective completion | — | — | ✓ | IP ↔ C |
| Indirect completion evidence | — | — | ✓ | IP ↔ C |
| Future/deferred action | ✓ | — | — | NS ↔ IP |
| Conditional future action | ✓ | — | — | NS ↔ IP |
| Current non-execution | ✓ | — | — | NS ↔ IP |
| Refusal without execution | ✓ | — | — | NS ↔ IP |
| Inability without execution | ✓ | — | — | NS ↔ IP |
| Forgetting without execution | ✓ | — | — | NS ↔ IP |
| Reason-linked non-execution | ✓ | — | — | NS ↔ IP |

`*` A temporary interruption is `In Progress` when execution has already begun. A future inability to begin remains `Not Started`.

---

# 7. Cross-Dimension Combinations

Dimensions should be combined to produce meaningful execution situations.

Examples:

```text
Partial Execution
+
Multi-Step Task
+
Remaining Work
→ In Progress
```

```text
Near Completion
+
One Step Remaining
→ In Progress
```

```text
Retrospective Report
+
All Steps Completed
→ Completed
```

```text
Future Intention
+
Conditional Action
+
No Execution Begun
→ Not Started
```

```text
Refusal
+
No Execution
→ Not Started
```

```text
Inability
+
No Execution
→ Not Started
```

These combinations provide semantic diversity without creating additional classifier labels.

---

# 8. Critical Boundary Dimensions

## B01 — Not Started ↔ In Progress

Prioritize:

- execution initiation;
- current activity;
- future/deferred action;
- conditional future action;
- current non-execution;
- refusal;
- inability;
- forgetting;
- reason-linked non-execution;
- temporary interruption.

Central question:

> **Has execution actually begun?**

---

## B02 — In Progress ↔ Completed

Prioritize:

- amount completed;
- remaining work;
- partial execution;
- multi-step execution;
- near completion;
- explicit completion;
- retrospective completion;
- indirect completion evidence.

Central question:

> **Has execution actually finished?**

---

## B03 — Not Started ↔ Completed

Prioritize:

- future intention vs retrospective completion;
- refusal vs completion;
- forgetting vs completion;
- inability vs completion;
- indirect non-execution vs indirect completion.

Central question:

> **Is there evidence of completed execution, or has execution not begun?**

---

# 9. Orthogonality Dimensions

Execution Status must remain independent of the other project ontologies.

## Dialogue Purpose

A user may ask, commit, report, refuse, or provide information. These are separate from execution state.

## Persuasion Barrier

A user may express:

```text
KnowledgeGap
LowConfidence
TimeConstraint
Forgetfulness
LowMotivation
RiskUnderestimation
SocialInfluence
```

A barrier can explain non-execution but does not itself determine Execution Status.

## Response Category

Behavioral appraisal toward an intervention is separate from task execution.

A positive or negative response can coexist with any execution state.

## Temporal / Scheduling Information

Statements about:

- later;
- tonight;
- tomorrow;
- deadlines;
- schedules;
- overdue;
- missed;

must not directly become Execution Status labels.

---

# 10. Lexical Shortcut Audit Dimensions

Important lexical regions include:

### Future / intention

```text
will
going to
plan to
later
tonight
tomorrow
```

### Current execution

```text
now
currently
doing
taking
working on
in the middle of
```

### Partial execution

```text
half
part
some
a few
first
remaining
```

### Near completion

```text
almost
nearly
just one left
about to finish
```

### Completion

```text
done
finished
completed
already did
got it done
```

These expressions must not become deterministic label indicators.

The same lexical families should occur across different semantic configurations whenever naturally possible.

---

# 11. Target-Task Dimension

The frozen target-task space is:

```text
Medication
Hydration
Exercise
Physiotherapy
```

Target task is contextual metadata, not an Execution Status label.

Stage 1 should represent execution states across all four domains.

The desired relationship is:

```text
Execution State × Target Task
```

rather than:

```text
Target Task → Execution Status
```

---

# 12. Conversational Context Dimension

Execution evidence may occur:

- directly in the current utterance;
- through reference to an earlier statement;
- through a consequence of execution;
- through a follow-up answer;
- through a correction;
- through a multi-step interaction.

Therefore Stage 1 should include both:

```text
Context-independent execution evidence
```

and:

```text
Context-dependent execution evidence
```

where context is genuinely required for interpretation.

Context should support interpretation rather than artificially increase sequence length.

---

# 13. Explicitness Dimension

Each state should contain a mixture of explicit and less explicit execution evidence.

### Explicit

```text
"I haven't started it."
```

### Indirect

```text
"I've done the first two and still have three left."
```

### Natural conversational

```text
"Yeah, I got that done earlier."
```

The goal is to prevent the classifier from learning that only explicit status statements are informative.

---

# 14. Difficulty Dimension

Scenario construction should cover:

### Clear

The execution state is directly supported.

### Moderate

The state requires combining multiple pieces of evidence.

### Difficult

The state requires distinguishing execution evidence from:

- intention;
- planning;
- temporal expressions;
- reasons;
- partial completion;
- indirect completion;
- multi-step context;
- conversational distractors.

Difficulty should arise from semantic interpretation, not unnatural wording.

---

# 15. Dimension-to-Scenario Mapping

Each future scenario should identify its primary execution dimension or dimension combination.

Recommended metadata:

```text
scenario_id
execution_status
semantic_subtype
scenario_description
execution_condition
target_task
execution_dimension
difficulty_level
explicitness
conversational_position
boundary_risk
notes
```

`execution_dimension` records the construction/coverage dimension represented by the scenario. It is not a classifier target.

---

# 16. Coverage Requirements Before Scenario Freeze

Before freezing the Stage 1 scenario inventory, verify meaningful coverage of:

```text
✓ Execution initiation
✓ Current execution activity
✓ Amount completed
✓ Remaining work
✓ Partial execution
✓ Multi-step execution
✓ Temporary interruption
✓ Near completion
✓ Explicit completion
✓ Retrospective completion
✓ Indirect completion evidence
✓ Future/deferred action
✓ Conditional future action
✓ Current non-execution
✓ Refusal without execution
✓ Inability/unavailability without execution
✓ Forgetting without execution
✓ Reason-linked non-execution
✓ Conversational context
✓ Explicitness variation
✓ Difficulty variation
✓ Four target-task domains
```

Not every dimension must occur equally often. The requirement is meaningful semantic representation.

---

# 17. What This File Does Not Define

This file does not freeze:

- the final semantic subtype catalogue;
- the exact number of subtypes;
- the exact number of scenarios per state;
- individual natural-language examples;
- boundary anchors;
- minimal pairs;
- hard negatives;
- Stage 3A variants;
- Stage 3B variants.

Those are constructed in subsequent resources.

---

# 18. Stage 1 Working Numbers

The current working construction plan is:

```text
Execution States
= 3

Semantic Subtypes
≈ 4–6 / state
Working target = 5 / state
Working target total = 15

Semantic Scenarios
≈ 12–20 / state
Working target = 15 / state
Working target total = 45

Initial Anchors
= 3 / scenario
Working target = 45 × 3
= 135
```

These are planning targets. Semantic completeness and diversity take precedence over numerical symmetry.

---

# 19. Final Principle

The execution semantic dimensions should make the dataset answer:

> **What has actually happened with the target task?**

rather than:

> **Which words suggest a particular status?**

The construction direction is:

```text
Execution Semantics
        ↓
Semantic Regions
        ↓
Distinct Scenarios
        ↓
Natural Language
```

not:

```text
Keywords
        ↓
Labels
```

The three frozen Execution Status values remain the only classifier labels:

```text
Not Started
In Progress
Completed
```

All dimensions in this document exist to ensure that these three states are represented across a broad and difficult execution-semantic space.
