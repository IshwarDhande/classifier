# Stage 3B — Construction Plan

**Target:** Execution Status Dataset  
**Ontology:** Execution Status Ontology V1.0  
**Stage:** Stage 3B — Linguistic Expansion of Stage 2

---

## 1. Objective

Stage 3B expands the boundary-focused resources created in Stage 2 without weakening the execution-state distinctions they were designed to teach.

```text
2A Boundary Anchors → Boundary-Preserving Expansion
2B Minimal Pairs    → Contrast-Preserving Expansion
2C Hard Negatives  → Distractor-Preserving Expansion
```

The objective is:

> **Increase linguistic diversity while preserving the exact execution-state evidence that makes each Stage-2 example diagnostically useful.**

Stage 3B must not create new ontology states, new boundaries, or new execution semantics.

The frozen Execution Status ontology contains exactly:

```text
Not Started
In Progress
Completed
```

The three states form the execution lifecycle:

```text
Not Started → In Progress → Completed
```

Stage 3B expands how these distinctions are expressed linguistically; it does not redefine the lifecycle.

---

## 2. Core Invariants

### 2A Boundary Anchors

Preserve:

- target Execution Status;
- closest competing Execution Status;
- boundary ID;
- anchor role;
- semantic position;
- execution evidence;
- target task;
- relevant intervention/reminder context;
- conversational situation;
- execution interpretation.

For example, an **A-Leaning Boundary** example must remain on the same side of the same execution boundary. It must not become a clear prototype for either state.

### 2B Minimal Pairs

Preserve:

- A/B Execution Status;
- same target task;
- same intervention/reminder context;
- same conversational position;
- comparable information;
- comparable linguistic complexity;
- same relevant history;
- primary A↔B execution-state contrast.

The pair must continue to differ because of the user's execution evidence, not because one side contains an obvious status keyword.

### 2C Hard Negatives

Preserve:

- target Execution Status;
- hard-negative mechanism;
- competing cue;
- dominant execution interpretation;
- target task;
- intervention context;
- distractor–target relationship.

A hard negative must continue to contain a misleading surface cue while the actual execution evidence supports the target state.

---

## 3. Expansion Principle

```text
2A → vary linguistic realization of execution-boundary evidence
2B → vary both sides while preserving the execution-state contrast
2C → vary distractor realization while preserving the target execution state
```

This is **controlled linguistic expansion**, not ordinary paraphrasing.

The central rule is:

> **Vary how the execution state is expressed, not what the execution state is.**

Stage 3B must preserve the distinction between:

```text
No execution has begun
        ↓
Execution has begun but is unfinished
        ↓
Execution has finished
```

---

## 4. Expansion Unit

```text
2A: Boundary → Anchor → Variants
2B: Boundary → Minimal-Pair Family → Paired Variants
2C: Boundary → Hard-Negative Example → Variants
```

The parent family remains the leakage group.

A descendant must retain complete lineage to its Stage-2 parent.

---

## 5. Execution-State Boundaries

Stage 3B operates over the frozen Stage-2 boundaries:

| Boundary | States | Primary Diagnostic Question |
|---|---|---|
| B01 | Not Started ↔ In Progress | Has execution actually begun? |
| B02 | In Progress ↔ Completed | Has execution actually finished? |
| B03 | Not Started ↔ Completed | Is there evidence of completed execution, or has execution not begun? |

### B01 — Not Started ↔ In Progress

The key distinction is:

> Has the target task actually begun?

Variants must distinguish genuine execution initiation from:

- future intention;
- planning;
- preparation without execution;
- current non-execution;
- delay/postponement;
- inability or unavailability;
- forgetting;
- refusal;
- conditional future action.

Actual execution evidence must remain the reason for an In Progress label.

### B02 — In Progress ↔ Completed

The key distinction is:

> Has execution finished?

Variants must distinguish unfinished execution from:

- ongoing execution;
- partial execution;
- halfway completion;
- remaining work;
- temporary interruption;
- near completion.

Actual completion evidence must remain the reason for a Completed label.

### B03 — Not Started ↔ Completed

The key distinction is:

> Is there evidence of completed execution, or has execution not begun?

Variants must preserve the larger distinction while avoiding a simplistic:

```text
future = Not Started
finished = Completed
```

shortcut.

Particular attention should be given to:

- future intention vs retrospective completion;
- refusal vs completion;
- forgetting vs completion;
- inability vs completion;
- indirect non-execution vs indirect completion;
- completion of another task vs completion of the target task.

---

## 6. Quantity

No blind final quota is imposed.

A working generation target of **6 candidates per validated Stage-2 parent** may be used.

For the current Stage-2 working inventory:

```text
2A: 18 boundary anchors × 6 = 108 candidates
2B: 18 minimal-pair families × 6 = 108 paired families
    = 216 utterances
2C: 18 hard-negative examples × 6 = 108 candidates

Potential candidates:
108 + 216 + 108 = 432 utterances
```

These are generation targets, not mandatory final counts.

Final dataset size depends on:

- semantic validation;
- boundary preservation;
- execution-state correctness;
- deduplication;
- shortcut audits;
- leakage audits;
- error analysis;
- human adjudication.

Low-quality variants must be rejected rather than retained merely to satisfy a quota.

---

## 7. Standard Variation Dimensions

The standard variation dimensions are:

- `LEX` — lexical reformulation
- `SYN` — syntactic reformulation
- `NAT` — conversational naturalization
- `EXP` — explicitness variation
- `LEN` — length variation
- `DSC` — discourse structure
- `PRG` — pragmatic reformulation
- `CMK` — conversational-marker variation
- `HES` — hesitation/self-correction
- `QST` — question/statement framing

Track-specific use is defined in the separate Stage 3B specifications.

Variation must not introduce a new execution scenario.

---

## 8. Execution-Specific Linguistic Variation

Stage 3B should deliberately vary how users communicate execution status.

Useful dimensions include:

### Lexical variation

Vary verbs and expressions describing:

- beginning;
- ongoing activity;
- partial execution;
- completion;
- stopping;
- remaining work.

### Syntactic variation

Vary:

- simple statements;
- compound statements;
- subordinate clauses;
- coordinated actions;
- conversational fragments;
- natural question/answer forms.

### Explicitness variation

Move between:

```text
Explicit execution evidence
        ↕
Indirect execution evidence
```

without changing the underlying state.

### Discourse variation

Change where execution evidence appears:

```text
opening → middle → closing
```

while preserving the same interpretation.

### Pragmatic variation

Express the same state through:

- direct report;
- contextual implication;
- response to a reminder;
- correction;
- explanation;
- conversational shorthand.

### Conversational-marker variation

Vary:

- "yeah";
- "okay";
- "actually";
- "well";
- "right";
- "no";
- "yes";
- hesitation markers.

These markers must not determine the execution label.

---

## 9. Execution-Specific Shortcut Resistance

Stage 3B must explicitly protect against lexical shortcuts involving status-related words.

Potential cues include:

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

These expressions may appear across different semantic contexts.

For example:

- a future expression does not by itself define the state;
- "now" does not automatically prove execution has begun;
- "almost" does not mean Completed;
- "done" must refer to the target task;
- "already" may refer to another event;
- "starting" may describe an intention rather than actual execution.

The classifier must learn **execution evidence**, not isolated status vocabulary.

---

## 10. Generation Protocol

For every Stage-2 parent:

1. Read the complete parent example and metadata.
2. Identify the exact execution-state invariant.
3. Identify the boundary, contrast, or hard-negative mechanism.
4. Select an appropriate variation type.
5. Generate natural conversational language.
6. Verify execution-state preservation.
7. Verify target-task preservation.
8. Verify boundary/contrast/distractor preservation.
9. Audit temporal and execution-status lexical shortcuts.
10. Remove exact and near duplicates.
11. Preserve complete lineage.
12. Submit difficult cases for human adjudication.

For minimal pairs, both sides must be transformed jointly.

For hard negatives, the distractor must remain present without becoming the dominant execution evidence.

---

## 11. Quality Control

### Semantic QC

Every variant must satisfy:

- same target Execution Status;
- same boundary or contrast;
- same execution evidence;
- same target task;
- same relevant intervention context;
- no ontology drift.

### Linguistic QC

Variants must be:

- natural;
- diverse;
- conversationally plausible;
- non-template-like;
- free from mechanical synonym replacement.

### Execution Evidence QC

Check that:

- actual execution is distinguishable from intention;
- unfinished execution is distinguishable from completion;
- target-task execution is distinguishable from unrelated actions;
- indirect evidence remains interpretable;
- multi-step execution is handled correctly.

### Shortcut QC

No single:

- temporal word;
- completion word;
- initiation word;
- negation pattern;
- punctuation pattern;
- sentence length;
- discourse marker;
- politeness marker;
- sentiment cue

should deterministically determine the label.

### Cross-Ontology QC

Execution Status must not be inferred from:

- Dialogue Purpose;
- Persuasion Barrier;
- Response Category;
- motivation;
- sentiment;
- emotion;
- scheduling/deadline status;
- Task Manager operational states.

---

## 12. Boundary-Preservation Requirements

### 2A

A boundary-anchor variant must remain at the same semantic position.

```text
Not Started prototype
Not Started-leaning boundary
        ↕
In Progress-leaning boundary
In Progress prototype
```

and similarly for:

```text
In Progress ↔ Completed
Not Started ↔ Completed
```

A variant must not become more or less diagnostic simply because of linguistic rewriting.

### 2B

The two sides must continue to differ for the same execution reason.

For example:

```text
Same task
Same context
Same intervention
        ↓
Execution has begun
        vs
Execution has not begun
```

or:

```text
Same task
Same context
Same intervention
        ↓
Execution unfinished
        vs
Execution finished
```

### 2C

The competing cue must remain present but non-dominant.

```text
Surface cue
     ↓
Potentially misleading
     ↓
BUT
     ↓
Actual execution evidence
     ↓
Target Execution Status
```

---

## 13. Human–LLM–Code Allocation

| Activity | Human | LLM | Code |
|---|:---:|:---:|:---:|
| Define execution invariants | ✓ | Assist | |
| Select variation types | ✓ | Assist | |
| Generate candidates | | ✓ | |
| Validate execution semantics | ✓ | Assist | |
| Boundary consistency | ✓ | ✓ | |
| Minimal-pair consistency | ✓ | ✓ | |
| Hard-negative consistency | ✓ | ✓ | |
| Duplicate detection | | | ✓ |
| Statistical/shortcut audit | ✓ | Assist | ✓ |
| Lineage validation | | | ✓ |
| Final adjudication | ✓ | | |

Human judgment remains authoritative for semantic validity.

LLMs provide linguistic scale and candidate generation.

Code performs deterministic audits and lineage checks.

---

## 14. Lineage

Recommended fields:

```text
example_id
parent_id
lineage_id
boundary_id
resource_type
execution_status
semantic_subtype
context
utterance
target_task
variation_type
source
validation_status
ambiguity_flag
```

Minimal pairs additionally retain:

```text
pair_id
side
pair_role
```

Hard negatives additionally retain:

```text
hard_negative_type
competing_cue
```

All descendants of a single Stage-2 family remain one leakage group.

---

## 15. Leakage Prevention

Stage 3B must not create train/test leakage through linguistic descendants.

The following must remain together:

```text
Stage-2 parent
    ├── Variant 1
    ├── Variant 2
    ├── Variant 3
    ├── Variant 4
    ├── Variant 5
    └── Variant 6
```

For minimal pairs:

```text
Pair family
    ├── A variants
    └── B variants
```

For hard negatives:

```text
Hard-negative family
    ├── distractor variant 1
    ├── distractor variant 2
    └── ...
```

The parent lineage must therefore be retained through the eventual 70/15/15 group split.

---

## 16. Forbidden Transformations

Reject a Stage 3B candidate if it:

- changes the Execution Status;
- crosses the intended boundary;
- removes the diagnostic execution evidence;
- introduces a new semantic scenario;
- changes the target task;
- changes the hard-negative mechanism;
- makes a distractor the dominant evidence;
- creates a trivial lexical shortcut;
- becomes sentiment-only;
- becomes planning-only;
- becomes a Dialogue Purpose example;
- becomes a Persuasion Barrier example;
- refers to a different task while appearing to describe the target task;
- becomes ambiguous without required context.

---

## 17. Final Acceptance Test

```text
[✓] Parent lineage preserved
[✓] Target Execution Status preserved
[✓] Boundary/contrast preserved
[✓] Execution evidence preserved
[✓] Target task preserved
[✓] Intervention/context preserved
[✓] Natural language
[✓] Genuine linguistic variation
[✓] No deterministic temporal/status keyword shortcut
[✓] No ontology leakage
[✓] No exact duplicate
[✓] No near duplicate
[✓] No execution-state drift
```

If a critical execution-semantic invariant fails:

> **REJECT**

---

## 18. Output Structure

```text
03b_linguistic_expansion/
├── 2a_boundary_anchor/
├── 2b_minimal_pair/
└── 2c_hard_negative/
```

Each track remains independently auditable.

The three tracks must retain their Stage-2 parent IDs and complete lineage.

---

## 19. Completion Criteria

Stage 3B is complete when:

- every validated Stage-2 family has been considered;
- appropriate linguistic variants have been generated;
- execution-state invariants are preserved;
- boundary and contrast distinctions remain intact;
- hard-negative distractors remain non-dominant;
- target-task identity is preserved;
- duplicates and near duplicates are removed;
- lexical and structural shortcuts are audited;
- cross-ontology leakage is audited;
- lineage is frozen;
- difficult cases are human-adjudicated.

The final resource must be suitable for downstream group-based dataset splitting and diagnostic evaluation.

---

## 20. Final Principle

> **Stage 3B maximizes linguistic robustness of Stage-2 execution-state decision-boundary resources without changing what those resources are designed to teach.**

The purpose is not to create more examples merely for quantity.

The purpose is to ensure that the classifier learns:

```text
execution evidence
      ↓
execution state
```

rather than:

```text
keyword
      ↓
execution state
```

or:

```text
emotion / intention / barrier / dialogue purpose
      ↓
execution state
```

The final Stage 3B resource should therefore make the frozen Execution Status ontology harder to solve through shortcuts while remaining semantically faithful to the original Stage-2 decision boundaries.
