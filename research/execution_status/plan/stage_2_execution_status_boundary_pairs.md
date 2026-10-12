# Stage 2 — Execution Status Boundary Pair Matrix

## Purpose

This matrix defines the three pairwise Execution Status boundaries used for Stage 2 boundary construction.

The two lifecycle-adjacent boundaries receive primary semantic priority. The non-adjacent `Not Started ↔ Completed` boundary provides broader contrast coverage and prevents the classifier from relying only on local progression cues.

## Frozen Execution Lifecycle

```text
Not Started → In Progress → Completed
```

## Boundary Pairs

| ID | Pair | Boundary class | Primary distinction | Diagnostic focus |
|---|---|---|---|---|
| `B01` | `Not Started ↔ In Progress` | Adjacent | No execution has begun ↔ execution has begun but remains unfinished | Not Started: intention/non-execution without actual initiation; In Progress: evidence that execution has started |
| `B02` | `In Progress ↔ Completed` | Adjacent | Execution has begun but remains unfinished ↔ execution has finished | In Progress: ongoing/partial/remaining work; Completed: finished execution |
| `B03` | `Not Started ↔ Completed` | Non-adjacent | No execution ↔ finished execution | Not Started: absence of execution; Completed: actual completed execution |

## Priority

### Tier 1 — Adjacent lifecycle boundaries

`B01 Not Started ↔ In Progress`, `B02 In Progress ↔ Completed`

These boundaries define the principal transitions of the execution lifecycle and receive the strongest semantic scrutiny.

### Tier 2 — Non-adjacent boundary

`B03 Not Started ↔ Completed`

This boundary is retained to ensure that the classifier can distinguish complete non-execution from completed execution without relying on a simple local progression cue.

## Construction Rule

Every boundary resource must answer:

> **What execution evidence establishes State A rather than State B?**

Boundary construction must prioritize actual execution evidence:

```text
Has execution started?
        ↓
If yes:
Has execution finished?
```

Planning, future intention, scheduling, deadline status, motivation, persuasion barrier, dialogue purpose, response sentiment, and task-manager states must not serve as hidden Execution Status proxies.

## Boundary-Specific Diagnostics

### B01 — Not Started ↔ In Progress

Ask:

> **Has the target task actually begun?**

Diagnostic distinction:

```text
Future intention / preparation / non-execution
                    ↔
Actual execution has begun
```

Critical cases include:

- “I’ll do it later.” → Not Started
- “I’m doing it now.” → In Progress
- “I’m getting ready to do it.” → Not Started
- “I’ve done the first part.” → In Progress
- “I’m about to start.” → Not Started unless execution has actually begun

### B02 — In Progress ↔ Completed

Ask:

> **Has the execution finished?**

Diagnostic distinction:

```text
Started but unfinished
        ↔
Finished execution
```

Critical cases include:

- “I’m almost done.” → In Progress
- “I finished it.” → Completed
- “I have one part left.” → In Progress
- “Everything is done.” → Completed
- “I’m still working on it.” → In Progress

### B03 — Not Started ↔ Completed

Ask:

> **Is there evidence of actual completed execution, or has execution not begun?**

Diagnostic distinction:

```text
No execution
    ↔
Finished execution
```

This boundary is especially important for:

- future intention vs retrospective completion;
- refusal vs completion;
- forgetting vs completion;
- inability vs completion;
- indirect non-execution vs indirect completion.

## Boundary Construction Principle

The boundary should be defined by the **minimum execution-semantic distinction** necessary to change the label.

```text
Not Started ↔ In Progress
        = execution initiation

In Progress ↔ Completed
        = execution completion

Not Started ↔ Completed
        = absence of execution ↔ finished execution
```

Temporal words may provide evidence, but they must not become the semantic definition of the boundary.

