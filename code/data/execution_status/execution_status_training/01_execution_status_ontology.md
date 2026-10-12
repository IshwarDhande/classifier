# Execution Status Ontology
**Version:** 1.0 (Frozen)

---

# Executive Summary

This document specifies the **Execution Status Ontology (ESO)** used within the Dialogue Interpreter.

The ontology captures the current execution state of the target task as communicated by the user's latest utterance.

Unlike scheduling or task management systems, the ontology models only **task execution**. It intentionally excludes planning, deadlines, missed tasks, and temporal reasoning, which are handled by downstream system components such as the Task Manager.

The ontology consists of three mutually exclusive execution states:

- Not Started
- In Progress
- Completed

This minimal representation provides a clean interface between natural language interpretation and task management while avoiding semantic overlap with the Dialogue Purpose and Persuasion Barrier ontologies.

---

# 1. Motivation

## 1.1 Problem Statement

The conversational agent must determine the execution state of the target task from natural language responses.

For example,

> "I already took my medicine."

indicates that task execution has finished.

Similarly,

> "I'm taking it now."

indicates that execution is currently underway.

Rather than modelling the entire task lifecycle, the Dialogue Interpreter extracts only the execution state communicated by the user.

---

## 1.2 Role in the Production Architecture

The Execution Status Ontology provides the execution state required by downstream system components.

```
User Utterance
        │
        ▼
Dialogue Interpreter
        │
        ▼
Execution Status
        │
        ├────────► Task Manager
        ├────────► RL State Update
        └────────► Dialogue Composer
```

The ontology itself does not perform task management.

---

# 2. Design Objectives

The ontology is designed to satisfy the following objectives.

- Represent only execution state.
- Remain independent of scheduling.
- Avoid duplication with Dialogue Purpose.
- Avoid duplication with Persuasion Barrier.
- Provide a minimal and mutually exclusive state space.
- Support reproducible annotation.

---

# 3. Formal Definition

## Definition

**Execution Status** represents the current execution lifecycle of the target task as explicitly or implicitly communicated by the user's latest utterance.

The ontology describes whether task execution has:

- not yet started,
- is currently underway,
- or has been completed.

---

# 4. Execution States

## 4.1 Not Started

### Definition

The user indicates that execution of the target task has not yet begun.

This includes situations where the task is pending, delayed, postponed, or intentionally deferred.

---

### Typical Examples

> I haven't done it yet.

> I'll do it after work.

> I'm busy right now.

> I forgot today.

> Maybe later.

---

## 4.2 In Progress

### Definition

The user indicates that execution of the target task has begun but has not yet been completed.

---

### Typical Examples

> I'm taking it now.

> I'm exercising right now.

> I'm working on it.

> Give me a minute, I'm doing it.

---

## 4.3 Completed

### Definition

The user indicates that execution of the target task has been completed.

---

### Typical Examples

> I already took it.

> Done.

> I finished exercising.

> I completed it.

> I already did that.

---

# 5. State Transition

The ontology represents a simple execution lifecycle.

```
Not Started
       │
       ▼
 In Progress
       │
       ▼
 Completed
```

Backward transitions are not represented within the ontology.

---

# 6. Relationship to Other Semantic Dimensions

Execution Status is independent of the remaining semantic states.

| Semantic Dimension | Question Answered |
|--------------------|-------------------|
| Response Category | How did the user react? |
| Dialogue Purpose | What is the user trying to accomplish conversationally? |
| Persuasion Barrier | Why is the task not completed? |
| Execution Status | What is the current execution state of the task? |

Each semantic dimension answers a different question and should be predicted independently.

---

# 7. Boundary Cases

## Example 1

**User**

> I'll do it after dinner.

Execution Status

```
Not Started
```

Dialogue Purpose

```
Commitment
```

The ontology distinguishes execution from future intention.

---

## Example 2

**User**

> I'm busy because I'm in a meeting.

Execution Status

```
Not Started
```

Barrier

```
Time Constraint
```

The execution state remains independent of the reason for non-execution.

---

## Example 3

**User**

> I'm taking it now.

Execution Status

```
In Progress
```

---

## Example 4

**User**

> I already finished.

Execution Status

```
Completed
```

---

# 8. Not Represented

The ontology intentionally excludes the following concepts.

- Planned
- Scheduled
- Skipped
- Missed
- Expired
- Overdue
- Cancelled
- Failed

These are **derived operational states** computed by downstream components.

For example,

```
Execution Status

+

Task Schedule

+

Current Time

↓

Skipped
```

Such reasoning belongs to the Task Manager rather than the Dialogue Interpreter.

---

# 9. Annotation Rules

### Rule 1

Assign exactly one Execution Status to every user utterance.

---

### Rule 2

Classify based on the execution state communicated by the user rather than inferred scheduling information.

---

### Rule 3

Future intentions are classified as

```
Not Started
```

The intention itself is captured by the **Commitment Dialogue Purpose**.

---

### Rule 4

Reasons for non-execution are ignored during Execution Status annotation.

They are captured by the **Persuasion Barrier** ontology.

---

### Rule 5

If execution has begun but is unfinished,

```
In Progress
```

takes precedence.

---

### Rule 6

If execution is complete,

```
Completed
```

always takes precedence.

---

# 10. Design Principles Satisfied

| Principle | Satisfaction |
|-----------|--------------|
| One Primary Status | ✔ Exactly one execution state per utterance |
| Minimal | ✔ Three-state ontology |
| Orthogonal | ✔ Independent of Dialogue Purpose and Barrier |
| Actionable | ✔ Directly supports Task Manager decisions |
| Stable | ✔ Consistent across wording variations |
| Execution-Oriented | ✔ Models execution only |

---

# 11. Interface Specification

## Input

```
Conversation Context

+

Current User Utterance
```

---

## Output

```yaml
execution_status:

allowed_values:
  - Not Started
  - In Progress
  - Completed
```

---

# 12. Downstream Interfaces

### Primary Consumer

```
Task Manager
```

Responsibilities

- Maintain task lifecycle
- Derive skipped tasks
- Detect overdue tasks
- Update scheduler

---

### Secondary Consumers

#### RL State Update

Uses execution status to update the interaction state.

---

#### Dialogue Composer

Uses execution status to determine whether persuasion should continue, transition to reinforcement, or conclude the conversation.

---

# 13. Current Design Status

| Component | Status |
|-----------|--------|
| Ontology Name | FROZEN |
| Three Execution States | FROZEN |
| Interface | FROZEN |
| Annotation Rules | FROZEN |
| Downstream Consumers | FROZEN |

---

# Summary

The **Execution Status Ontology** provides a minimal, execution-oriented representation of the target task's lifecycle as communicated by the user. By restricting the ontology to three mutually exclusive execution states—**Not Started**, **In Progress**, and **Completed**—the design maintains clear separation of concerns, avoids duplication with other semantic dimensions, and delegates temporal reasoning and operational task management to downstream components. This results in a compact, interpretable, and production-ready ontology that aligns with the overall architecture of the conversational persuasion system.