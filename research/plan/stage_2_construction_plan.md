# Stage 2 — Response Category Boundary Construction Plan

**Target:** Response Category Dataset
**Ontology:** Response Category Ontology V1.0
**Stage:** Stage 2 — Boundary Quality
**Frozen categories:** `VP`, `P`, `I`, `N`, `VN`

## 1. Purpose

Stage 2 constructs the decision-boundary resources required to teach the classifier why behaviorally similar responses belong to one Response Category rather than another.

Stage 1 established broad behavioral semantic coverage. Stage 3A expanded that frozen semantic space linguistically. Stage 2 now focuses specifically on distinctions between categories, with particular emphasis on the ordinal neighboring boundaries.

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

## 2. Source Principles

The Stage-1 and master construction plans establish that Response Category is an ordinal behavioral-appraisal problem rather than a sentiment or emotion classification problem. The five labels remain:

```text
VN < N < I < P < VP
```

Stage 2 therefore concentrates on behavioral acceptance, commitment, resistance, enthusiasm, rejection, reactance, and disengagement rather than lexical polarity.

Stage 2 also follows the project allocation principle: humans define semantic boundaries, LLMs provide candidate linguistic realizations, and code performs deterministic auditing.

## 3. Boundary Pair Matrix

Stage 2 uses all ten possible pairwise boundaries. The four adjacent boundaries are Tier 1; the six non-adjacent boundaries are Tier 2.

| ID | Pair | Priority | Core boundary |
|---|---|---|---|
| `B01` | `VP ↔ P` | Tier 1 | Enthusiastic/high-engagement acceptance ↔ ordinary cooperative acceptance |
| `B02` | `P ↔ I` | Tier 1 | Behavioral acceptance/commitment ↔ uncertainty or non-commitment |
| `B03` | `I ↔ N` | Tier 1 | Neutral/non-committal response ↔ behavioral resistance |
| `B04` | `N ↔ VN` | Tier 1 | Recoverable resistance ↔ strong rejection/reactance/disengagement |
| `B05` | `VP ↔ I` | Tier 2 | Strong positive engagement ↔ insufficient behavioral commitment |
| `B06` | `VP ↔ N` | Tier 2 | Strong positive acceptance ↔ behavioral resistance |
| `B07` | `VP ↔ VN` | Tier 2 | Strong positive engagement ↔ strong rejection/reactance |
| `B08` | `P ↔ N` | Tier 2 | Ordinary cooperation ↔ meaningful resistance |
| `B09` | `P ↔ VN` | Tier 2 | Ordinary cooperation ↔ strong rejection/reactance |
| `B10` | `I ↔ VN` | Tier 2 | Insufficient behavioral evidence ↔ strong rejection/reactance |

See `stage_2_boundary_pairs.md` for the complete diagnostic matrix.

## 4. Stage 2A — Boundary Anchors

### Objective

Create explicit semantic anchor examples that map the boundary region between two Response Categories.

### Standard six-anchor structure

For each selected boundary pair, construct:

1. A Prototype
2. B Prototype
3. A-Leaning Boundary
4. B-Leaning Boundary
5. Implicit A
6. Implicit B

### Initial planning target

```text
10 boundary pairs × 6 anchors = 60 boundary anchors
```

### Construction rules

- A and B prototypes must clearly represent their respective behavioral states.
- Leaning examples should approach the boundary without crossing it.
- Implicit examples should demonstrate that category membership does not require category keywords.
- Adjacent boundaries receive the greatest semantic precision.
- Non-adjacent examples must still represent genuine behavioral contrasts rather than exaggerated lexical polarity.
- Each anchor receives pair-level lineage and a `closest_competing_category` value.

### Boundary-specific diagnostics

- **VP↔P:** Is strong enthusiasm/appreciation/high engagement present, or is the response simply cooperative?
- **P↔I:** Is there actual behavioral acceptance/commitment, or only acknowledgement/uncertainty?
- **I↔N:** Is there genuine behavioral resistance, or merely uncertainty/non-commitment?
- **N↔VN:** Does resistance remain recoverable, or does it become strong rejection, hostility, high reactance, or disengagement?
- **Non-adjacent pairs:** Does the evidence genuinely locate the response toward one endpoint rather than relying on sentiment or intensity words?

### Output

```text
stage_2/
└── 2A_boundary_anchors/
    └── boundary_anchors_<pair-range>.md
```

## 5. Stage 2B — Minimal Pairs

### Objective

Construct paired utterances that keep the underlying conversational situation as constant as practical while changing the dominant behavioral response category.

### Core principle

> Change the behavioral appraisal while holding the situation stable.

Preserve where practical:

- same intervention;
- same task context;
- similar conversational position;
- comparable information content;
- comparable linguistic complexity.

The pair, not the individual utterance, is the primary QC unit.

### Initial planning target

```text
10 boundary pairs × 6 minimal-pair instances
= 60 minimal pairs
= 120 utterances
```

### Construction rules

- Generate both sides jointly.
- Keep the scenario and intervention constant wherever possible.
- Change primarily the behavioral reaction.
- Avoid changing multiple semantic variables simultaneously.
- Do not rely on a single lexical edit if that creates an artificial distinction.
- For adjacent boundaries, make the behavioral transition precise.
- For non-adjacent boundaries, maintain a plausible shared situation while making the larger response-state contrast explicit.

### Example pattern

```text
P:  Okay, I’ll do it.
I:  I’ll think about it.

N:  I’d rather not.
VN: Leave me alone. I’m not doing this.
```

These are construction patterns; final production examples must be generated and validated from the frozen boundary definitions.

### Output

```text
stage_2/
└── 2B_minimal_pairs/
    └── minimal_pairs_<pair-range>.md
```

## 6. Stage 2C — Hard Negatives

### Objective

Break superficial cues that could allow a classifier to predict Response Category without understanding behavioral appraisal.

Core principle:

> Surface polarity or response cue is not equivalent to Response Category.

### Hard-negative mechanisms

1. Competing keyword
2. Competing phrase
3. Misleading opening clause
4. Self-correction
5. Multiple competing cues
6. Strong conversational distractor

### Response-specific hard-negative patterns

- gratitude or appreciation wording with behavioral resistance;
- negative wording with genuine cooperation;
- commitment/future language without sufficient acceptance;
- acceptance wording combined with meaningful resistance;
- positive emotion unrelated to the intervention;
- conventional politeness without strong positive appraisal;
- sarcasm or pragmatic reversal where context supports the interpretation;
- emotionally strong language whose dominant behavioral response belongs elsewhere.

### Initial planning target

```text
10 boundary pairs × 6 hard-negative candidates
= 60 hard-negative candidates
```

### Construction rules

- Preserve the target behavioral category.
- Introduce a genuine competing surface cue.
- Do not make the distractor so artificial that the example becomes unnatural.
- Context must be sufficient when pragmatic interpretation is required.
- The dominant behavioral response must remain recoverable by a careful annotator.
- Hard negatives must not simply become boundary examples or minimal pairs.

### Output

```text
stage_2/
└── 2C_hard_negatives/
    └── hard_negatives_<pair-range>.md
```

## 7. Stage 2 Shared Semantic Invariants

All three resources must preserve:

- Response Category as the only classifier target;
- behavioral interpretation toward the intervention;
- the frozen ordinal ontology;
- relevant conversational context;
- orthogonality from Dialogue Purpose;
- orthogonality from Persuasion Barrier;
- orthogonality from Execution Status;
- orthogonality from task completion;
- independence from emotion and sentiment alone;
- resistance to isolated keyword shortcuts.

Decision hierarchy:

```text
Behavioral Commitment
        ↓
Behavioral Resistance
        ↓
Communicative Intention
        ↓
Pragmatic Meaning
        ↓
Surface Wording
```

## 8. Stage 2 Metadata and Lineage

Every Stage-2 example should retain:

```text
example_id
pair_id
parent_id
lineage_id
category
stage
resource_type
context
utterance
response_category
closest_competing_category
variation_type
hard_negative_type
source
validation_status
ambiguity_flag
```

For minimal pairs, both sides must share a common `pair_id` while retaining distinct example IDs.

Boundary anchors and hard negatives must preserve their originating boundary family.

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

## 10. Quality Control

### Boundary QC

- all four adjacent boundaries receive high-quality coverage;
- all six non-adjacent boundaries are represented;
- each anchor has a clear dominant category;
- neighboring-category confusion is intentional and diagnostically meaningful;
- boundary position is not determined by sentiment alone.

### Minimal-Pair QC

- shared situation is preserved;
- intervention is preserved;
- contextual position is comparable;
- behavioral contrast is clear;
- both sides are natural;
- the contrast survives lexical normalization.

### Hard-Negative QC

- competing cue is genuine;
- target behavior remains dominant;
- example is natural and contextually interpretable;
- distractor does not accidentally change the gold category;
- hard-negative mechanism is recorded.

### Orthogonality QC

Labels must not be deterministically recoverable from:

- emotion;
- sentiment polarity;
- topic;
- task completion;
- execution status;
- persuasion barrier;
- dialogue purpose;
- isolated keywords;
- punctuation or sentence length.

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

## 12. Deduplication and Leakage Control

Remove:

- exact duplicates;
- trivial lexical duplicates;
- redundant boundary examples;
- minimal pairs that differ only superficially without changing behavioral meaning;
- hard negatives whose distractor is not genuinely distinct.

Leakage grouping must preserve:

- boundary family;
- minimal-pair family;
- hard-negative family;
- all later Stage-3B descendants.

Do not split paired or family-linked examples across future train/validation/test groups.

## 13. Stage 2 Completion Criteria

Stage 2 is complete only when:

1. All ten boundary pairs are defined and reviewed.
2. Adjacent boundaries receive primary semantic scrutiny.
3. 60 boundary-anchor candidates have been constructed or the target has been adjusted by documented semantic review.
4. 60 minimal-pair families have been constructed or the target has been adjusted by documented semantic review.
5. 60 hard-negative candidates have been constructed or the target has been adjusted by documented semantic review.
6. Boundary, pair, and distractor semantics have been human-validated.
7. Duplicate and near-duplicate checks are complete.
8. Orthogonality and shortcut audits are complete.
9. Lineage is frozen.
10. Stage-2 resources are ready for Stage 3B expansion.

## 14. Construction Order

```text
1. Freeze 10 boundary pairs
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

## 15. Final Principle

> **Stage 2 should make the classifier learn where behavioral response states differ, not merely how positive or negative the wording sounds.**

The three resources serve complementary purposes:

```text
2A Boundary Anchors
→ map the semantic decision region

2B Minimal Pairs
→ isolate the behavioral distinction

2C Hard Negatives
→ defeat superficial lexical and sentiment shortcuts
```

Together they transform the Stage-1 semantic coverage into a boundary-aware training resource while preserving the frozen Response Category ontology.