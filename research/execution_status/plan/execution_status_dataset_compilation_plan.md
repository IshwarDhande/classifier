# Dataset Compilation Plan — Execution Status

First we will save all Execution Status datasets in `code/data/execution_status`.

**Methodology Reference:** Use the project's generalized dataset methodology for the mathematical splitting rules, specifically Leakage-Safe Stratified Group Splitting, across all compiled datasets.

---

## Target Datasets to Compile

The Execution Status construction pipeline contains four primary stages:

1. **Stage 1**  
   *Target Name:* `stage_1_dataset.csv`

2. **Stage 3A**  
   *Target Name:* `stage_3a_dataset.csv`

3. **Stage 2**  
   *Target Name:* `stage_2_dataset.csv`

4. **Stage 3B**  
   *Target Name:* `stage_3b_dataset.csv`

In addition, compile the following combined resources:

5. **Stage 1 + Stage 3A**  
   *Target Name:* `stage_1_and_3a_combined.csv`

6. **Stage 2 + Stage 3B**  
   *Target Name:* `stage_2_and_3b_combined.csv`

7. **Stage 1 + Stage 3A + Stage 2 + Stage 3B**  
   *Target Name:* `complete_unified_corpus.csv`

The seven outputs provide stage-level resources as well as progressively unified corpora for training, analysis, and diagnostic evaluation.

---

## Pipeline Structure

```text
Stage 1
Semantic Coverage
    ↓
stage_1_dataset.csv
    ↓
Stage 3A
Linguistic Expansion
    ↓
stage_3a_dataset.csv
    ↓
Stage 2
Boundary Quality
    ├── 2A Boundary Anchors
    ├── 2B Minimal Pairs
    └── 2C Hard Negatives
    ↓
stage_2_dataset.csv
    ↓
Stage 3B
Boundary / Contrast / Distractor Expansion
    ├── 3B-A Boundary Anchor Variants
    ├── 3B-B Minimal Pair Variants
    └── 3B-C Hard Negative Variants
    ↓
stage_3b_dataset.csv
```

The combined corpora are constructed only after the individual stage datasets have passed their stage-specific validation.

---

## Unified Master Schema

All four stages must be normalized into a common schema before compilation.

| Column Name | Description | Source Stage Applicability |
| :--- | :--- | :--- |
| `utterance_id` | Unique identifier for the utterance. Maps to the stage-specific `example_id` where applicable. | All |
| `utterance` | Actual text of the user's conversational utterance. | All |
| `execution_status` | Ground-truth execution state: `not_started`, `in_progress`, or `completed`. | All |
| `status_no` | Numeric encoding of the frozen execution state. Recommended mapping: `2 = not_started`, `1 = in_progress`, `0 = completed`. | All |
| `stage` | Pipeline stage that generated the row: `1`, `2`, `3A`, or `3B`. | All |
| `split` | Dataset partition: `train`, `validation`, or `test`. | All |
| `task_or_scenario_id` | Semantic scenario or target task identifier. | All |
| `target_task` | Target behavioral task, restricted to the frozen task domains: medication, hydration, exercise, physiotherapy. | All |
| `semantic_subtype` | Stage-specific semantic subtype used during construction. | All |
| `parent_id` | Baseline/parent utterance from which the example was derived. | 3A, 3B |
| `lineage_id` | Complete derivation lineage for leakage-safe grouping. | 3A, 3B |
| `variation_type` | Linguistic transformation applied, e.g. `LEX`, `SYN`, `NAT`, `EXP`, `LEN`, `DSC`, `PRG`, `CMK`, `HES`, `QST`. | 3A, 3B |
| `boundary_id` | Execution-status boundary targeted, e.g. `B01`, `B02`, `B03`. | 2, 3B |
| `hard_negative_type` | Hard-negative mechanism used, e.g. competing temporal cue, competing execution-status phrase, misleading opening clause, self-correction, multiple competing cues, strong conversational distractor. | 2C, 3B-C |
| `closest_competing_state` | Closest competing Execution Status used during boundary construction. | 2, 3B |
| `resource_type` | Resource class such as scenario anchor, linguistic variant, boundary anchor, minimal-pair side, or hard negative. | All |
| `context` | Relevant conversational/intervention context required to interpret the utterance. | All |
| `source_file` | Original construction file from which the row was generated or parsed. | All |
| `validation_status` | Validation/adjudication status of the resource. | All |
| `ambiguity_flag` | Indicates whether the example requires additional review because of potential semantic ambiguity. | All |

Fields that are not applicable to a stage remain null.

---

## Frozen Label Mapping

The classifier target is the frozen three-state Execution Status ontology:

| Execution State | Standardized Label | `status_no` |
| :--- | :--- | :--- |
| Not Started | `not_started` | `2` |
| In Progress | `in_progress` | `1` |
| Completed | `completed` | `0` |

The ordering reflects the execution lifecycle:

```text
Not Started → In Progress → Completed
```

The numeric encoding is only a machine-readable representation. It must not be interpreted as an ordinal behavioral score.

---

## Stage-Specific Compilation

### Stage 1

Stage 1 contains:

- semantic scenarios;
- execution-state subtypes;
- direct anchors;
- indirect anchors;
- natural conversational anchors.

Stage 1 is the semantic coverage resource.

No Stage 1 example should receive a `parent_id` or `variation_type` unless such lineage actually exists.

---

### Stage 3A

Stage 3A contains linguistic variants derived from Stage 1 scenarios.

Each example must retain:

```text
parent_id
lineage_id
semantic_subtype
variation_type
execution_status
target_task
```

Stage 3A variants remain grouped with their Stage 1 semantic family for leakage-safe splitting.

---

### Stage 2

Stage 2 contains three boundary-quality resources:

```text
2A — Boundary Anchors
2B — Minimal Pairs
2C — Hard Negatives
```

The primary boundaries are:

```text
B01 — Not Started ↔ In Progress
B02 — In Progress ↔ Completed
B03 — Not Started ↔ Completed
```

Stage 2 examples must retain their boundary identity and, where relevant:

```text
pair_id
pair_role
hard_negative_type
closest_competing_state
```

---

### Stage 3B

Stage 3B contains:

```text
3B-A — Boundary Anchor Variants
3B-B — Minimal Pair Variants
3B-C — Hard Negative Variants
```

All descendants must retain complete Stage-2 lineage.

For example:

```text
Stage 2 parent
      ↓
Stage 3B variant
      ↓
same lineage group
```

The three tracks must remain independently auditable.

---

## Combined Datasets

### Stage 1 + Stage 3A

`stage_1_and_3a_combined.csv`

Purpose:

> Unified semantic-coverage and standard linguistic-expansion resource.

This corpus combines original semantic examples with their Stage 3A linguistic descendants.

Lineage must be preserved so that variants can be identified as belonging to the same semantic family.

---

### Stage 2 + Stage 3B

`stage_2_and_3b_combined.csv`

Purpose:

> Unified boundary-quality and robustness resource.

This corpus combines:

```text
Stage 2
    ↓
boundary anchors
minimal pairs
hard negatives

Stage 3B
    ↓
boundary-preserving variants
contrast-preserving variants
distractor-preserving variants
```

Stage 2 parents and all Stage 3B descendants remain identifiable through lineage.

---

### Complete Unified Corpus

`complete_unified_corpus.csv`

Contains:

```text
Stage 1
+
Stage 3A
+
Stage 2
+
Stage 3B
```

This is the complete Execution Status construction corpus.

It must preserve the provenance of every example so that researchers can later filter by:

- stage;
- boundary;
- semantic subtype;
- variation type;
- hard-negative mechanism;
- target task;
- lineage;
- split.

---

## Leakage-Safe Splitting

The final split must follow the project's generalized leakage-safe stratified group methodology.

The fundamental rule is:

> **Semantically related descendants must never be separated across train, validation, and test sets.**

Therefore:

```text
Stage 1 scenario
   +
Stage 3A descendants
```

remain within one leakage group.

Similarly:

```text
Stage 2 boundary family
   +
Stage 3B descendants
```

remain within one leakage group.

For minimal pairs:

```text
Pair A
Pair B
All Stage 3B descendants
```

must remain in the same group.

For hard negatives:

```text
Original hard negative
All distractor variants
```

must remain in the same group.

The target split remains:

```text
70% Train
15% Validation
15% Test
```

subject to the project's leakage-safe grouped splitting procedure.

---

## Compilation Order

Compilation should follow this order:

```text
1. Parse Stage 1
       ↓
2. Normalize Stage 1 schema
       ↓
3. Parse Stage 3A
       ↓
4. Normalize Stage 3A schema
       ↓
5. Parse Stage 2A / 2B / 2C
       ↓
6. Normalize Stage 2 schema
       ↓
7. Parse Stage 3B-A / 3B-B / 3B-C
       ↓
8. Normalize Stage 3B schema
       ↓
9. Validate identifiers and lineage
       ↓
10. Deduplicate
       ↓
11. Audit labels
       ↓
12. Audit target-task coverage
       ↓
13. Audit boundary coverage
       ↓
14. Audit hard-negative mechanisms
       ↓
15. Perform leakage-safe group split
       ↓
16. Generate seven final CSV resources
```

---

## Required Compilation Audits

Before writing the final datasets, verify:

### Schema Audit

```text
[✓] Required columns present
[✓] Column names standardized
[✓] Data types valid
[✓] Nulls only where expected
```

### Label Audit

```text
[✓] Only three execution states
[✓] No unknown labels
[✓] Correct state normalization
[✓] No accidental Response Category labels
```

### Target Task Audit

```text
[✓] Medication
[✓] Hydration
[✓] Exercise
[✓] Physiotherapy
```

No new target task should be introduced during compilation.

### Boundary Audit

```text
[✓] B01 — Not Started ↔ In Progress
[✓] B02 — In Progress ↔ Completed
[✓] B03 — Not Started ↔ Completed
```

### Lineage Audit

```text
[✓] Every Stage 3A example has valid ancestry
[✓] Every Stage 3B example has valid Stage 2 ancestry
[✓] Minimal-pair sides remain grouped
[✓] Hard-negative descendants remain grouped
```

### Shortcut Audit

Check for excessive dependence on:

```text
already
now
later
finished
done
starting
started
almost
will
going to
```

These expressions may occur naturally, but must not become deterministic class markers.

### Duplicate Audit

Remove:

- exact duplicates;
- accidental duplicate lineage entries;
- near-duplicate utterances where the intended linguistic variation has effectively disappeared.

---

## Output Directory

Recommended structure:

```text
code/data/execution_status_dataset/
│
├── dataset_1/
│   ├── stage_1_dataset.csv
│   ├── train.csv
│   ├── validation.csv
│   └── test.csv
│
├── dataset_3a/
│   ├── stage_3a_dataset.csv
│   ├── train.csv
│   ├── validation.csv
│   └── test.csv
│
├── dataset_2/
│   ├── stage_2_dataset.csv
│   ├── stage_2_ba.csv
│   ├── stage_2_mp.csv
│   ├── stage_2_hn.csv
│   ├── train.csv
│   ├── validation.csv
│   └── test.csv
│
├── dataset_3b/
│   ├── stage_3b_dataset.csv
│   ├── stage_3b_ba.csv
│   ├── stage_3b_mp.csv
│   ├── stage_3b_hn.csv
│   ├── train.csv
│   ├── validation.csv
│   └── test.csv
│
└── combined/
    ├── stage_1_and_3a_combined.csv
    ├── stage_2_and_3b_combined.csv
    └── complete_unified_corpus.csv
```

---

## Final Compilation Principle

> **Compile the Execution Status corpus as one lineage-aware dataset rather than as independent collections of utterances.**

The final corpus must preserve:

```text
Semantic meaning
      ↓
Execution Status
      ↓
Stage provenance
      ↓
Boundary / contrast / distractor information
      ↓
Linguistic variation
      ↓
Lineage
      ↓
Leakage-safe split
```

The compilation process must never alter the frozen semantic labels. Its role is to normalize, validate, preserve provenance, enforce leakage safety, and produce consistent CSV resources for training and evaluation.
