# Execution Status Differentiation Guide
**Version:** 1.0

---

# Purpose

This document explains the semantic differences between the three **Execution Status** categories used within the Dialogue Interpreter.

Unlike the ontology specification, which formally defines each execution state, this guide focuses on helping annotators, model developers, and downstream system designers consistently distinguish between the categories.

The guiding question is:

> **"Based on the user's latest utterance, what is the current execution state of the target task?"**

Importantly, the ontology captures **execution state only**. It intentionally ignores:

- user motivation,
- reasons for non-execution,
- future intentions,
- scheduling,
- deadlines,
- missed tasks,
- temporal reasoning.

Those concepts are represented elsewhere in the architecture.

---

# Decision Tree

```
                    User Utterance
                           │
          Has the user completed the task?
                           │
                ┌──────────┴──────────┐
                │                     │
               YES                   NO
                │                     │
                ▼                     ▼
          Completed         Has execution started?
                                     │
                          ┌──────────┴──────────┐
                          │                     │
                         YES                   NO
                          │                     │
                          ▼                     ▼
                    In Progress         Not Started
```

---

# Comparison Overview

| Execution Status | Meaning | Typical Indicators |
|-----------------|---------|-------------------|
| **Not Started** | Execution has not yet begun | Pending, delayed, postponed, future intention |
| **In Progress** | Execution has begun but is unfinished | Currently performing task |
| **Completed** | Execution has finished | Done, completed, finished |

---

# Key Principle

Execution Status answers only one question:

> **Has execution started, and if so, has it finished?**

Everything else belongs elsewhere.

| Information | Ontology |
|-------------|----------|
| Why isn't the task done? | Persuasion Barrier |
| Is the user rejecting? | Dialogue Purpose |
| How positive is the response? | Response Category |
| Has execution started or finished? | Execution Status |

---

# 1. Not Started vs In Progress

## Not Started

Execution has **not begun**.

Examples

> I haven't done it yet.

> I'll do it tonight.

> I'm busy right now.

> Maybe later.

> I forgot.

Execution Status

```
Not Started
```

---

## In Progress

Execution has already begun.

Examples

> I'm taking it now.

> I'm exercising right now.

> I'm working on it.

> Give me a minute.

Execution Status

```
In Progress
```

---

## Side-by-Side

| User Utterance | Execution Status |
|---------------|------------------|
| I'll take it after dinner. | Not Started |
| I'm taking it now. | In Progress |
| I'll start after work. | Not Started |
| I'm halfway through my workout. | In Progress |
| I'll do it in five minutes. | Not Started |
| I'm doing it at the moment. | In Progress |

---

# 2. In Progress vs Completed

## In Progress

Execution is ongoing.

Examples

> I'm taking it now.

> I'm still exercising.

> I'm almost finished.

Execution Status

```
In Progress
```

---

## Completed

Execution has finished.

Examples

> Done.

> I already took it.

> Finished.

> I completed it.

Execution Status

```
Completed
```

---

## Side-by-Side

| User Utterance | Execution Status |
|---------------|------------------|
| I'm taking it now. | In Progress |
| I already took it. | Completed |
| I'm still working on it. | In Progress |
| I finished it. | Completed |
| Almost done. | In Progress |
| Done! | Completed |

---

# 3. Not Started vs Completed

## Not Started

Execution has never begun.

Examples

> I haven't done it.

> Not yet.

> I'll do it later.

Execution Status

```
Not Started
```

---

## Completed

Execution has finished.

Examples

> Already done.

> Completed.

> Finished earlier.

Execution Status

```
Completed
```

---

# Relationship with Dialogue Purpose

One of the most important design principles is that **Execution Status and Dialogue Purpose are independent semantic dimensions.**

---

## Example 1

User

> I'll do it tonight.

Execution Status

```
Not Started
```

Dialogue Purpose

```
Commitment
```

Future intention is captured by **Commitment**, not Execution Status.

---

## Example 2

User

> I'm busy right now.

Execution Status

```
Not Started
```

Dialogue Purpose

```
Information
```

The user explains their situation.

---

## Example 3

User

> I'm not doing it.

Execution Status

```
Not Started
```

Dialogue Purpose

```
Refusal
```

Execution has not started, but the user is rejecting the recommendation.

---

## Example 4

User

> I already finished.

Execution Status

```
Completed
```

Dialogue Purpose

```
Information
```

The user is reporting completed execution.

---

# Relationship with Persuasion Barrier

Execution Status does **not** explain why execution has not occurred.

Examples

| User Utterance | Execution Status | Barrier |
|---------------|------------------|---------|
| I'm busy. | Not Started | Time Constraint |
| I forgot. | Not Started | Forgetfulness |
| I don't think it helps. | Not Started | Knowledge Gap |
| I'm not motivated today. | Not Started | Low Motivation |

Notice that different barriers can produce the same execution state.

---

# Relationship with Response Category

Execution Status is also independent of behavioral response.

| User Utterance | Response Category | Execution Status |
|---------------|------------------|------------------|
| Okay, I'll do it later. | P | Not Started |
| No, I'm not doing it. | VN | Not Started |
| I'm taking it now. | VP | In Progress |
| Done. | VP | Completed |

---

# Frequently Confused Examples

| User Utterance | Execution Status | Reason |
|---------------|------------------|--------|
| I'll do it tonight. | Not Started | Future intention, execution has not begun. |
| I'm busy. | Not Started | Explains current situation, execution has not started. |
| I'm almost done. | In Progress | Execution has started but is unfinished. |
| Give me a minute, I'm doing it. | In Progress | Current execution. |
| I already finished. | Completed | Execution has ended. |
| Done! | Completed | Explicit completion. |
| I'll start in five minutes. | Not Started | Planned future action. |
| I forgot today. | Not Started | Reports non-execution. |
| I skipped today's dose. | Not Started* | Execution Status only; Task Manager derives **Skipped**. |

---

# Derived States (Not Part of the Ontology)

The following are **not predicted** by the Structured Understanding Model.

Instead, they are computed by the Task Manager using Execution Status together with scheduling and temporal information.

```
Execution Status

+

Task Schedule

+

Current Time

↓

Derived State
```

Examples

| Derived State | Computed By |
|---------------|-------------|
| Skipped | Task Manager |
| Overdue | Task Manager |
| Expired | Task Manager |
| Missed | Task Manager |
| Delayed | Task Manager |

---

# Annotation Guidelines

## Rule 1

Ignore the user's reason for not performing the task.

Focus only on execution.

---

## Rule 2

Ignore future intentions.

Future intentions belong to the **Commitment Dialogue Purpose**.

---

## Rule 3

Ignore deadlines.

Whether the task is overdue is determined by the Task Manager.

---

## Rule 4

Ignore persuasion barriers.

Reasons such as:

- busy,
- forgot,
- not motivated,

do not change Execution Status.

---

## Rule 5

If execution has begun,

always assign

```
In Progress
```

unless the user explicitly states completion.

---

## Rule 6

If the user explicitly reports completion,

always assign

```
Completed
```

---

# Common Annotation Mistakes

❌ Incorrect

```
"I'll do it tonight."

↓

Execution Status = In Progress
```

Correct

```
Not Started
```

---

❌ Incorrect

```
"I skipped today's dose."

↓

Execution Status = Skipped
```

Correct

```
Not Started
```

(Task Manager later derives **Skipped**.)

---

❌ Incorrect

```
"I'm busy."

↓

Execution Status = Time Constraint
```

Correct

```
Execution Status = Not Started

Barrier = Time Constraint
```

---

❌ Incorrect

```
"I'm taking it now."

↓

Execution Status = Completed
```

Correct

```
In Progress
```

---

# Summary

The Execution Status Ontology models only the **execution lifecycle** of the target task.

| Execution Status | Meaning |
|------------------|---------|
| **Not Started** | Execution has not begun. |
| **In Progress** | Execution has started but is not complete. |
| **Completed** | Execution has finished. |

The ontology deliberately excludes planning, scheduling, deadlines, and missed tasks. These operational concepts are derived later by the **Task Manager**, ensuring that the Dialogue Interpreter remains minimal, orthogonal, and focused solely on extracting primitive semantic facts from natural language.