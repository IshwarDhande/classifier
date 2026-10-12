# Stage 2 — Execution Status Boundary Construction Plan

**Target:** Execution Status Dataset  
**Ontology:** Execution Status Ontology V1.0  
**Stage:** Stage 2 — Boundary Quality  
**Frozen states:** `Not Started`, `In Progress`, `Completed`

---

## 1. Purpose

Stage 2 constructs the decision-boundary resources required to teach the classifier why execution-related utterances belong to one Execution Status rather than another.

Stage 1 established broad execution-semantic coverage. Stage 3A expanded that frozen semantic space linguistically. Stage 2 now focuses specifically on distinctions between execution states, with primary emphasis on the two adjacent lifecycle boundaries.

```text
Stage 1 — Semantic Coverage
        ↓
Stage 3A — Linguistic Expansion
        ↓
Stage 2 — Boundary Quality
        ├── Stage 2A — Boundary Anchors
        ├── Stage 2B — Minimal Pairs
        └── Stage 2C — Hard Negatives
        ↓
Stage 3B — Boundary/Contrast/Distractor Expansion
```

---

## 2. Source Principles

The Execution Status ontology defines three mutually exclusive states:

```text
Not Started
In Progress
Completed
```

Their lifecycle is:

```text
Not Started → In Progress → Completed
```

Stage 2 therefore concentrates on:

- execution initiation;
- ongoing/partial execution;
- execution completion;
- remaining work;
- future intention versus actual execution;
- near completion versus completion;
- non-execution versus completed execution.

Stage 2 does **not** introduce new execution states.

It also follows the project allocation principle:

> **Humans define semantic boundaries, LLMs provide candidate linguistic realizations, and code performs deterministic auditing.**

---

## 3. Boundary Pair Matrix

Stage 2 uses all three possible pairwise boundaries.

The two adjacent lifecycle boundaries are Tier 1; the non-adjacent boundary is Tier 2.

| ID | Pair | Priority | Core boundary |
|---|---|---|---|
| `B01` | `Not Started ↔ In Progress` | Tier 1 | No execution has begun ↔ execution has begun but remains unfinished |
| `B02` | `In Progress ↔ Completed` | Tier 1 | Execution has begun but remains unfinished ↔ execution has finished |
| `B03` | `Not Started ↔ Completed` | Tier 2 | No execution ↔ finished execution |

See `stage_2_execution_status_boundary_pairs.md` for the complete diagnostic matrix.

---

## 4. Stage 2A — Boundary Anchors

### Objective

Create explicit semantic anchor examples that map the boundary region between two Execution Status states.

### Standard six-anchor structure

For each boundary pair, construct:

1. A Prototype
2. B Prototype
3. A-Leaning Boundary
4. B-Leaning Boundary
5. Implicit A
6. Implicit B

### Initial planning target

```text
3 boundary pairs × 6 anchors = 18 boundary anchors
```

### Construction rules

- A and B prototypes must clearly represent their respective execution states.
- Leaning examples should approach the boundary without crossing it.
- Implicit examples should demonstrate that state membership does not require canonical execution-status keywords.
- Adjacent boundaries receive the greatest semantic precision.
- The `Not Started ↔ Completed` boundary must represent a genuine execution contrast rather than merely exaggerated temporal wording.
- Each anchor receives pair-level lineage and a `closest_competing_state` value.

### Boundary-specific diagnostics

**B01 — Not Started ↔ In Progress**

- Has execution actually begun?
- Does the utterance merely express intention, preparation, or future action?
- Is there evidence of partial execution?
- Does a current activity actually concern the target task?

**B02 — In Progress ↔ Completed**

- Has execution finished?
- Is the task merely close to completion?
- Is there remaining work?
- Does the utterance report an ongoing or partial state?

**B03 — Not Started ↔ Completed**

- Is there actual evidence that the task was executed and finished?
- Is the statement merely future-oriented?
- Is non-execution being reported retrospectively?
- Is completion expressed indirectly?

### Output

```text
stage_2/
└── 2A_boundary_anchors/
    └── boundary_anchors_<pair-range>.md
```

---

## 5. Stage 2B — Minimal Pairs

### Objective

Construct paired utterances that keep the underlying task and conversational situation as constant as practical while changing the decisive execution-state evidence.

### Core principle

> **Change the execution state while holding the task situation stable.**

Preserve where practical:

- same target task;
- same intervention/reminder context;
- similar conversational position;
- comparable information content;
- comparable linguistic complexity.

The pair, not the individual utterance, is the primary QC unit.

### Initial planning target

```text
3 boundary pairs × 6 minimal-pair instances
= 18 minimal pairs
= 36 utterances
```

### Construction rules

- Generate both sides jointly.
- Keep the task and surrounding situation constant wherever possible.
- Change primarily the execution-state evidence.
- Avoid changing multiple semantic variables simultaneously.
- Do not rely on a single lexical edit if that creates an artificial distinction.
- For adjacent boundaries, make the execution transition precise.
- For the non-adjacent boundary, maintain a plausible shared situation while making the larger execution contrast explicit.

### Example patterns

```text
Not Started:
"I'll do the exercise later."

In Progress:
"I'm doing the exercise now."
```

```text
In Progress:
"I've done most of the exercises; I still have two left."

Completed:
"I've done all the exercises; there are none left."
```

```text
Not Started:
"I haven't taken the medication yet."

Completed:
"I already took the medication."
```

These are construction patterns; final production examples must be generated and validated from the frozen boundary definitions.

### Output

```text
stage_2/
└── 2B_minimal_pairs/
    └── minimal_pairs_<pair-range>.md
```

---

## 6. Stage 2C — Hard Negatives

### Objective

Break superficial cues that could allow a classifier to predict Execution Status without understanding actual execution.

Core principle:

> **A temporal or status cue is not equivalent to an execution state.**

### Hard-negative mechanisms

1. Competing temporal cue
2. Competing execution-status phrase
3. Misleading opening clause
4. Self-correction
5. Multiple competing cues
6. Strong conversational distractor

### Execution-specific hard-negative patterns

- future language combined with current-task discussion;
- “already” or completion wording in a statement that is not actually about the target task;
- “starting” language where execution has not yet begun;
- “almost done” versus actual completion;
- reason/barrier statements that contain no execution;
- refusal statements followed by unrelated completion information;
- self-correction from one apparent state to another;
- multiple temporal expressions referring to different events;
- completion of one subtask while the target task remains unfinished;
- completion of a different task that is not the target task.

### Initial planning target

```text
3 boundary pairs × 6 hard-negative candidates
= 18 hard-negative candidates
```

### Construction rules

- Preserve the target Execution Status.
- Introduce a genuine competing surface cue.
- Do not make the distractor so artificial that the example becomes unnatural.
- Context must be sufficient when reference resolution is required.
- The actual execution state must remain recoverable by a careful annotator.
- Hard negatives must not simply become ordinary boundary examples or minimal pairs.
- The distractor must not change the target task.

### Output

```text
stage_2/
└── 2C_hard_negatives/
    └── hard_negatives_<pair-range>.md
```

---

## 7. Stage 2 Shared Semantic Invariants

All three resources must preserve:

- Execution Status as the only classifier target;
- actual execution evidence;
- the frozen three-state lifecycle;
- relevant conversational context;
- distinction between execution and intention;
- distinction between execution and planning;
- orthogonality from Dialogue Purpose;
- orthogonality from Persuasion Barrier;
- orthogonality from Response Category;
- orthogonality from deadline/scheduling status;
- orthogonality from task-manager derived states;
- independence from emotion and sentiment alone;
- resistance to isolated temporal/status keyword shortcuts.

### Decision hierarchy

```text
Has execution started?
        ↓
   NO → Not Started
        ↓
   YES
        ↓
Has execution finished?
        ↓
   YES → Completed
        ↓
   NO → In Progress
```

This hierarchy must govern all Stage-2 construction.

---

## 8. Stage 2 Metadata and Lineage

Every Stage-2 example should retain:

```text
example_id
pair_id
parent_id
lineage_id
execution_status
semantic_subtype
stage
resource_type
context
utterance
target_task
closest_competing_state
variation_type
hard_negative_type
source
validation_status
ambiguity_flag
```

For minimal pairs, both sides must share a common `pair_id` while retaining distinct example IDs.

Boundary anchors and hard negatives must preserve their originating boundary family.

---

## 9. Human–LLM–Code Allocation

| Activity | Human | LLM | Code |
|---|:---:|:---:|:---:|
| Define/freeze boundary semantics | ✓ | Assist | |
| Define diagnostic property | ✓ | Assist | |
| Generate boundary candidates | ✓ | ✓ | |
| Generate minimal pairs | ✓ | ✓ | |
| Generate hard negatives | ✓ | ✓ | |
| Validate difficult boundary cases | ✓ | Assist | |
| Exact/near duplicate detection | | | ✓ |
| Pair structure checks | | | ✓ |
| Lineage tracking | | | ✓ |
| Distribution/statistics | | | ✓ |
| Shortcut audits | ✓ | Assist | ✓ |
| Final adjudication | ✓ | | |

LLM-generated examples remain candidate data until human validation.

---

## 10. Quality Control

### Boundary QC

- all three boundaries receive high-quality coverage;
- both adjacent boundaries receive highest semantic scrutiny;
- each anchor has a clear dominant execution state;
- neighboring-state confusion is intentional and diagnostically meaningful;
- boundary position is not determined by a single temporal word;
- “almost,” “already,” “now,” “later,” and similar cues do not become deterministic labels.

### Minimal-Pair QC

- shared task situation is preserved;
- intervention/reminder context is preserved where relevant;
- contextual position is comparable;
- execution-state contrast is clear;
- both sides are natural;
- the contrast survives lexical normalization;
- the decisive difference is execution semantics rather than unrelated information.

### Hard-Negative QC

- competing cue is genuine;
- target execution state remains dominant;
- example is natural and contextually interpretable;
- distractor does not accidentally change the gold state;
- hard-negative mechanism is recorded;
- target task remains stable.

### Orthogonality QC

Labels must not be deterministically recoverable from:

- emotion;
- sentiment polarity;
- topic;
- task completion language alone when it refers to another task;
- persuasion barrier;
- dialogue purpose;
- response category;
- isolated temporal keywords;
- punctuation;
- sentence length;
- future intention alone.

---

## 11. Stage 2 Validation Sequence

```text
Boundary Pair Definitions
        ↓
2A Boundary Anchors
        ↓
Human Boundary Review
        ↓
2B Minimal Pairs
        ↓
Pair-Level Review
        ↓
2C Hard Negatives
        ↓
Hard-Negative Review
        ↓
Global Stage-2 QC
```

Stage 3B must not begin until the Stage-2 resources are semantically validated.

---

## 12. Deduplication and Leakage Control

Remove:

- exact duplicates;
- trivial lexical duplicates;
- redundant boundary examples;
- minimal pairs that differ only superficially without changing execution meaning;
- hard negatives whose distractor is not genuinely distinct;
- examples that duplicate Stage-1 scenarios without adding boundary value.

Leakage grouping must preserve:

- boundary family;
- minimal-pair family;
- hard-negative family;
- all later Stage-3B descendants.

Do not split paired or family-linked examples across future train/validation/test groups.

---

## 13. Stage 2 Completion Criteria

Stage 2 is complete only when:

1. All three boundary pairs are defined and reviewed.
2. Adjacent lifecycle boundaries receive primary semantic scrutiny.
3. 18 boundary-anchor candidates have been constructed or the target has been adjusted by documented semantic review.
4. 18 minimal-pair families have been constructed or the target has been adjusted by documented semantic review.
5. 18 hard-negative candidates have been constructed or the target has been adjusted by documented semantic review.
6. Boundary, pair, and distractor semantics have been human-validated.
7. Duplicate and near-duplicate checks are complete.
8. Orthogonality and shortcut audits are complete.
9. Lineage is frozen.
10. Stage-2 resources are ready for Stage 3B expansion.

---

## 14. Construction Order

```text
1. Freeze 3 boundary pairs
        ↓
2. Define diagnostic property for each pair
        ↓
3. Stage 2A — Boundary Anchors
        ↓
4. Validate boundary anchors
        ↓
5. Stage 2B — Minimal Pairs
        ↓
6. Validate minimal-pair families
        ↓
7. Stage 2C — Hard Negatives
        ↓
8. Validate hard-negative candidates
        ↓
9. Global Stage-2 QC
        ↓
10. Deduplication
        ↓
11. Leakage audit
        ↓
12. Freeze Stage 2
        ↓
13. Stage 3B
```

---

## 15. Final Principle

> **Stage 2 should make the classifier learn where execution states differ, not merely which temporal or status words tend to occur with each state.**

The three resources serve complementary purposes:

```text
2A Boundary Anchors
→ map the semantic decision region

2B Minimal Pairs
→ isolate the execution-state distinction

2C Hard Negatives
→ defeat superficial temporal, lexical, and conversational shortcuts
```

Together they transform the Stage-1 semantic coverage into a boundary-aware training resource while preserving the frozen Execution Status ontology.
