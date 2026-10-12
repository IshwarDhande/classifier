# Stage 3B-A — Boundary Anchor Variant Specification

**Input:** Stage 2A Boundary Anchors  
**Expansion unit:** Individual boundary anchor  
**Goal:** Boundary-preserving linguistic expansion

---

## 1. Purpose

Stage 2A anchors teach where two Execution Status states meet. Stage 3B-A increases linguistic diversity while preserving the anchor's exact position and diagnostic execution evidence.

The central rule is:

> **Vary the linguistic realization, not the execution-state position.**

A variant must continue to represent the same side of the same Execution Status boundary for the same execution-related reason.

---

## 2. Fixed Invariants

Preserve:

- target Execution Status;
- closest competing Execution Status;
- boundary ID;
- anchor role;
- semantic position;
- execution evidence;
- target task;
- intervention/reminder context;
- conversational situation.

The execution-state distinction must remain unchanged.

For example, a **Not Started-Leaning Boundary** example must remain Not Started-leaning. It must not become a clear Not Started prototype or cross into In Progress.

Similarly:

- an In Progress-leaning example must remain unfinished execution;
- a Completed-leaning example must remain completed execution;
- an implicit example must remain inferable through execution evidence rather than becoming unnecessarily explicit.

---

## 3. Anchor Roles

| Role | Required property |
|---|---|
| Not Started Prototype | Clear evidence that target execution has not begun |
| In Progress Prototype | Clear evidence that target execution has begun but is unfinished |
| Completed Prototype | Clear evidence that target execution has finished |
| A-Leaning Boundary | Subtle but sufficient evidence for state A |
| B-Leaning Boundary | Subtle but sufficient evidence for state B |
| Implicit A | State A inferred through execution evidence/pragmatics |
| Implicit B | State B inferred through execution evidence/pragmatics |

The actual Stage 2 anchor role depends on the boundary.

### B01 — Not Started ↔ In Progress

```text
A = Not Started
B = In Progress
```

The boundary is:

> Has the target task actually begun?

### B02 — In Progress ↔ Completed

```text
A = In Progress
B = Completed
```

The boundary is:

> Has execution actually finished?

### B03 — Not Started ↔ Completed

```text
A = Not Started
B = Completed
```

The boundary is:

> Is there evidence of completed execution, or has execution not begun?

---

## 4. Standard Six Variants

| Variant | Type | Purpose |
|---|---|---|
| BA-V01 | `LEX` | Different execution-related vocabulary |
| BA-V02 | `SYN` | Different syntactic realization |
| BA-V03 | `NAT` | Natural conversational realization |
| BA-V04 | `EXP` | Explicit/implicit execution evidence variation |
| BA-V05 | `PRG` | Pragmatic reformulation |
| BA-V06 | `CMK` | Conversational-marker variation |

`LEN`, `DSC`, `HES`, and `QST` may be used selectively when they preserve the exact boundary position.

---

## 5. Boundary Rules

### B01 — Not Started ↔ In Progress

Highest precision is required around the initiation of actual execution.

Variants must distinguish:

```text
Not Started
    ↓
intention / preparation / discussion / non-execution
```

from:

```text
In Progress
    ↓
actual execution has begun
```

Do not allow words such as:

- "starting";
- "about to";
- "going to";
- "will";
- "getting ready"

to become deterministic evidence of In Progress.

Likewise, actual execution must not be weakened into mere intention.

---

### B02 — In Progress ↔ Completed

Highest precision is required around the endpoint of execution.

Variants must distinguish:

```text
In Progress
    ↓
execution has begun
but remains unfinished
```

from:

```text
Completed
    ↓
execution has finished
```

Expressions such as:

- "almost";
- "nearly";
- "just";
- "done";
- "finished"

must be interpreted in context rather than treated as deterministic keywords.

In particular:

> **Almost finished is still In Progress.**

---

### B03 — Not Started ↔ Completed

Variants must preserve the larger distinction between:

```text
No execution
```

and:

```text
Finished execution
```

without reducing the boundary to isolated future/completion words.

Particular care is required for:

- retrospective statements;
- indirect completion;
- refusal;
- forgetting;
- inability;
- conditional future action;
- completion of another task;
- references to an earlier or different event.

---

## 6. Boundary Position Preservation

A boundary anchor has a specific semantic position.

Conceptually:

```text
State A Prototype
       ↓
A-Leaning Boundary
       ↓
Boundary
       ↓
B-Leaning Boundary
       ↓
State B Prototype
```

Stage 3B-A must preserve the original position.

A variant must not:

- move an A-Leaning Boundary toward a clear A Prototype;
- move a B-Leaning Boundary toward a clear B Prototype;
- cross the boundary;
- remove the evidence that made the anchor diagnostic.

For implicit anchors, the same inference must remain available through natural conversational context.

---

## 7. Standard Variant Construction

### BA-V01 — `LEX`

Change execution-related vocabulary while preserving:

- execution state;
- target task;
- boundary position;
- execution evidence.

Do not simply replace one status keyword with another.

---

### BA-V02 — `SYN`

Change syntactic structure while preserving the same execution interpretation.

Possible changes include:

- active/passive-like reformulation where natural;
- clause ordering;
- coordination;
- subordination;
- conversational fragments.

The syntactic transformation must not change whether execution has begun or finished.

---

### BA-V03 — `NAT`

Naturalize the utterance into realistic conversational language.

The result should sound like something a user would naturally say to a reminder agent.

Naturalization may introduce:

- conversational shorthand;
- ordinary phrasing;
- contractions;
- informal constructions.

It must not introduce a new execution state.

---

### BA-V04 — `EXP`

Vary the explicitness of execution evidence.

```text
Explicit execution evidence
        ↕
Indirect execution evidence
```

The same state must remain recoverable.

An implicit variant should not become genuinely ambiguous.

---

### BA-V05 — `PRG`

Change pragmatic realization while preserving the same execution evidence.

Examples of pragmatic framing include:

- direct report;
- response to a reminder;
- explanation;
- correction;
- brief conversational response;
- context-dependent implication.

The pragmatic framing must not replace execution status with a different construct such as motivation, refusal, or planning.

---

### BA-V06 — `CMK`

Vary conversational markers without changing the execution interpretation.

Examples include natural uses of:

- "well";
- "actually";
- "yeah";
- "no";
- "okay";
- "right";
- hesitation or discourse markers.

Markers must remain semantically non-diagnostic.

---

## 8. Execution-Specific Variation Controls

Stage 3B-A should deliberately vary the following:

### Initiation evidence

For B01, vary how actual execution begins:

```text
direct initiation
indirect initiation
current-action description
contextual evidence of action
```

while keeping the distinction from intention and preparation intact.

### Ongoing evidence

For B02, vary evidence that execution is underway but unfinished:

```text
currently performing
partially performed
remaining work
temporarily interrupted
nearly finished
```

### Completion evidence

For B02/B03, vary:

```text
explicit completion
retrospective completion
indirect completion
completion with commentary
```

while ensuring completion refers to the target task.

### Contextual references

Variants may refer to:

- the reminder;
- earlier conversation;
- current activity;
- a previous attempt;
- task progress.

Such references must not introduce scheduling or task-manager labels as the target.

---

## 9. Forbidden Transformations

Reject variants that:

- change the Execution Status;
- cross the intended boundary;
- intensify or weaken the anchor position;
- remove diagnostic execution evidence;
- add a new competing execution state;
- change the target task;
- convert execution into mere intention;
- convert unfinished execution into completion;
- convert completion into a statement about another task;
- rely on a single execution-status keyword;
- rely on sentiment or emotion;
- rely on Persuasion Barrier;
- rely on Dialogue Purpose;
- rely on Response Category;
- introduce scheduling/deadline semantics as the classifier target.

---

## 10. Acceptance Test

```text
[✓] Same boundary
[✓] Same anchor role
[✓] Same execution-state position
[✓] Same execution evidence
[✓] Same target task
[✓] Same Execution Status
[✓] Natural wording
[✓] Genuine linguistic variation
[✓] No lexical shortcut
[✓] No boundary drift
[✓] No cross-ontology leakage
```

Key question:

> **Would expert annotators place the original and variant on the same side of the same Execution Status boundary for the same execution-related reason?**

If the answer is no, reject the variant.

---

## 11. Execution Shortcut Audit

Every boundary-anchor variant should be checked for over-reliance on:

```text
already
now
later
tomorrow
finished
done
starting
started
almost
will
going to
```

These expressions may appear as part of natural language, but they must not independently determine the label.

The diagnostic signal must remain the user's actual execution state.

---

## 12. Leakage

All variants derived from one boundary anchor remain one leakage group.

Retain:

```text
parent_id
lineage_id
boundary_id
anchor_role
```

for later group-based dataset splitting.

An anchor and its linguistic descendants must never be distributed across different train/validation/test groups.

---

## 13. Final Principle

> **Stage 3B-A increases linguistic diversity around an Execution Status boundary without moving the example's semantic position.**

The objective is to make boundary recognition robust to linguistic variation while preserving the exact distinction:

```text
Not Started ↔ In Progress
In Progress ↔ Completed
Not Started ↔ Completed
```

The classifier should learn the underlying execution evidence, not the particular wording used to express it.
