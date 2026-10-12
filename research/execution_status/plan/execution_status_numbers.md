# Execution Status Dataset — Construction Numbers and File Plan

## 1. Purpose

This document defines the planned file structure and construction quantities for the complete **Execution Status dataset research pipeline**.

The organization mirrors the existing Response Category research structure while adapting it to the frozen Execution Status ontology:

- **Not Started**
- **In Progress**
- **Completed**

The pipeline is organized into three major construction stages:

```text
Stage 1 — Semantic Coverage
        ↓
Stage 2 — Boundary Quality
        ↓
Stage 3 — Linguistic Robustness
        ├── Stage 3A — Linguistic Expansion
        └── Stage 3B — Boundary / Contrast / Distractor Expansion
```

The numbers below distinguish between:

1. **fixed planning targets**,
2. **working generation targets**, and
3. **non-quota coverage dimensions**.

This distinction is important because not every stage is designed around a blind final sample quota.

---

# 2. Final Research Directory

Only production construction files are included below.

```text
research/
├── files.md
│
├── s1/
│   ├── 01_execution_semantic_dimensions.md
│   ├── 02_semantic_subtype_catalogue.md
│   ├── 03_semantic_scenarios_not_started.md
│   ├── 04_semantic_scenarios_in_progress.md
│   ├── 05_semantic_scenarios_completed.md
│   └── anchors/
│       ├── 01_initial_anchors_not_started.md
│       ├── 02_initial_anchors_in_progress.md
│       └── 03_initial_anchors_completed.md
│
├── s2/
│   ├── ba/
│   │   ├── BA01_not_started_in_progress.md
│   │   ├── BA02_in_progress_completed.md
│   │   └── BA03_not_started_completed.md
│   ├── mp/
│   │   ├── MP01_not_started_in_progress.md
│   │   ├── MP02_in_progress_completed.md
│   │   └── MP03_not_started_completed.md
│   ├── hn/
│   │   ├── HN01_not_started_in_progress.md
│   │   ├── HN02_in_progress_completed.md
│   │   └── HN03_not_started_completed.md
│   └── stage_2_three_state_construction_plan.md
│
├── s3a/
│   ├── stage_3a_not_started_variants.md
│   ├── stage_3a_in_progress_variants.md
│   ├── stage_3a_completed_variants.md
│   └── stage_3a_standard_variants.md
│
└── s3b/
    ├── 2a_boundary_anchor/
    │   ├── ba01_not_started_in_progress_variants.md
    │   ├── ba02_in_progress_completed_variants.md
    │   └── ba03_not_started_completed_variants.md
    ├── 2b_minimal_pair/
    │   ├── mp01_not_started_in_progress_variants.md
    │   ├── mp02_in_progress_completed_variants.md
    │   └── mp03_not_started_completed_variants.md
    └── 2c_hard_negative/
        ├── hn01_not_started_in_progress_variants.md
        ├── hn02_in_progress_completed_variants.md
        └── hn03_not_started_completed_variants.md
```

No `quick_review.md`, audit report, fixes file, or implementation roadmap is part of this production file structure.

---

# 3. Frozen Ontology

The classifier target is fixed at three execution states:

| State | Meaning |
|---|---|
| Not Started | Target-task execution has not begun |
| In Progress | Target-task execution has begun but is unfinished |
| Completed | Target-task execution has finished |

The number of construction resources may grow across stages, but the number of ontology labels remains:

\[
N_{states}=3
\]

---

# 4. Stage 1 — Semantic Coverage

## 4.1 Stage 1 Objective

Stage 1 defines the semantic space before linguistic expansion or boundary construction.

The construction hierarchy is:

```text
Execution State
      ↓
Semantic Dimensions
      ↓
Semantic Subtypes
      ↓
Semantic Scenarios
      ↓
Initial Anchors
```

---

## 4.2 Stage 1 File Set

```text
s1/
├── 01_execution_semantic_dimensions.md
├── 02_semantic_subtype_catalogue.md
├── 03_semantic_scenarios_not_started.md
├── 04_semantic_scenarios_in_progress.md
├── 05_semantic_scenarios_completed.md
└── anchors/
    ├── 01_initial_anchors_not_started.md
    ├── 02_initial_anchors_in_progress.md
    └── 03_initial_anchors_completed.md
```

### File-level quantities

| File | Construction Unit | Planned Quantity |
|---|---|---:|
| `01_execution_semantic_dimensions.md` | Semantic dimensions | Coverage framework; no fixed sample count |
| `02_semantic_subtype_catalogue.md` | Semantic subtypes | 15 |
| `03_semantic_scenarios_not_started.md` | Not Started scenarios | 15 |
| `04_semantic_scenarios_in_progress.md` | In Progress scenarios | 15 |
| `05_semantic_scenarios_completed.md` | Completed scenarios | 15 |
| `anchors/01_initial_anchors_not_started.md` | Not Started anchors | 45 |
| `anchors/02_initial_anchors_in_progress.md` | In Progress anchors | 45 |
| `anchors/03_initial_anchors_completed.md` | Completed anchors | 45 |

---

## 4.3 Semantic Subtypes

Working target:

\[
5\ subtypes/state
\]

\[
3\ states \times 5 = \boxed{15\ subtypes}
\]

| State | Subtypes |
|---|---:|
| Not Started | 5 |
| In Progress | 5 |
| Completed | 5 |
| **Total** | **15** |

These are construction artifacts, not classifier labels.

---

## 4.4 Semantic Scenarios

Working target:

\[
15\ scenarios/state
\]

\[
3 \times 15 = \boxed{45\ scenarios}
\]

| State | Scenarios |
|---|---:|
| Not Started | 15 |
| In Progress | 15 |
| Completed | 15 |
| **Total** | **45** |

With five subtypes per state:

\[
15/5=3\ scenarios/subtype
\]

Thus the working distribution is:

| State | Subtypes | Scenarios/Subtype | Scenarios |
|---|---:|---:|---:|
| Not Started | 5 | 3 | 15 |
| In Progress | 5 | 3 | 15 |
| Completed | 5 | 3 | 15 |
| **Total** | **15** | | **45** |

---

## 4.5 Initial Anchors

Each scenario receives three initial anchor realizations:

1. Direct
2. Indirect
3. Natural Conversational

Therefore:

\[
3\ anchors/scenario \times 45\ scenarios
=\boxed{135\ anchors}
\]

| State | Scenarios | Anchors/Scenario | Anchors |
|---|---:|---:|---:|
| Not Started | 15 | 3 | 45 |
| In Progress | 15 | 3 | 45 |
| Completed | 15 | 3 | 45 |
| **Total** | **45** | | **135** |

Anchor-type totals:

\[
45\ Direct + 45\ Indirect + 45\ Natural = \boxed{135}
\]

---

## 4.6 Stage 1 Total

Counting construction artifacts separately:

\[
15\ subtypes + 45\ scenarios + 135\ anchors
=\boxed{195}
\]

This **195 is not the final dataset size**. It is the number of Stage 1 semantic construction artifacts.

---

# 5. Stage 2 — Boundary Quality

## 5.1 Stage 2 Objective

Stage 2 converts the semantic space into explicit decision-boundary resources.

The frozen three-state ontology produces three pairwise state boundaries:

```text
B01 — Not Started ↔ In Progress
B02 — In Progress ↔ Completed
B03 — Not Started ↔ Completed
```

Priority:

- **Tier 1:** B01, B02 — adjacent lifecycle boundaries
- **Tier 2:** B03 — non-adjacent boundary

Therefore:

\[
N_{boundaries}=3
\]

---

# 6. Stage 2 File Set

```text
s2/
├── ba/
│   ├── BA01_not_started_in_progress.md
│   ├── BA02_in_progress_completed.md
│   └── BA03_not_started_completed.md
│
├── mp/
│   ├── MP01_not_started_in_progress.md
│   ├── MP02_in_progress_completed.md
│   └── MP03_not_started_completed.md
│
├── hn/
│   ├── HN01_not_started_in_progress.md
│   ├── HN02_in_progress_completed.md
│   └── HN03_not_started_completed.md
│
└── stage_2_three_state_construction_plan.md
```

---

# 7. Stage 2A — Boundary Anchors

Each boundary receives six boundary-anchor types:

1. A Prototype
2. B Prototype
3. A-Leaning Boundary
4. B-Leaning Boundary
5. Implicit A
6. Implicit B

Therefore:

\[
6\ boundary\ anchors/boundary
\]

\[
3\ boundaries \times 6
=\boxed{18\ boundary\ anchors}
\]

### Distribution

| Boundary | Pair | Anchors |
|---|---|---:|
| B01 | Not Started ↔ In Progress | 6 |
| B02 | In Progress ↔ Completed | 6 |
| B03 | Not Started ↔ Completed | 6 |
| **Total** | | **18** |

---

# 8. Stage 2B — Minimal Pairs

The construction target is six minimal-pair families per boundary.

\[
6\ pairs/boundary \times 3
=\boxed{18\ minimal\ pair\ families}
\]

Each pair contains two utterances:

\[
18\ families \times 2
=\boxed{36\ utterances}
\]

### Distribution

| Boundary | Pair Families | Utterances |
|---|---:|---:|
| B01 | 6 | 12 |
| B02 | 6 | 12 |
| B03 | 6 | 12 |
| **Total** | **18** | **36** |

The minimal-pair family, rather than the individual utterance, is the primary construction/QC unit.

---

# 9. Stage 2C — Hard Negatives

The Stage 2C working target is six hard-negative candidates per boundary.

\[
6\ HN/boundary \times 3
=\boxed{18\ hard\ negatives}
\]

The six mechanisms are:

1. Competing temporal cue
2. Competing execution-status phrase
3. Misleading opening clause
4. Self-correction
5. Multiple competing cues
6. Strong conversational distractor

### Distribution

| Boundary | Hard Negatives |
|---|---:|
| B01 | 6 |
| B02 | 6 |
| B03 | 6 |
| **Total** | **18** |

---

# 10. Stage 2 Total

Stage 2 contains:

\[
18\ boundary\ anchors
\]

\[
36\ minimal\ pair\ utterances
\]

\[
18\ hard\ negatives
\]

Therefore:

\[
18+36+18=\boxed{72\ utterance-level\ resources}
\]

The minimal-pair families themselves are additionally:

\[
\boxed{18\ pair\ families}
\]

Thus Stage 2 should be reported as:

```text
18 boundary anchors
18 minimal-pair families / 36 minimal-pair utterances
18 hard negatives
--------------------------------
72 utterance-level resources
```

---

# 11. Stage 3 — Linguistic Robustness

Stage 3 has two distinct components:

```text
Stage 3A — Standard linguistic expansion
Stage 3B — Boundary / contrast / distractor expansion
```

They must not be treated as one undifferentiated generation pool.

---

# 12. Stage 3A — Linguistic Expansion

## 12.1 Stage 3A File Set

```text
s3a/
├── stage_3a_not_started_variants.md
├── stage_3a_in_progress_variants.md
├── stage_3a_completed_variants.md
└── stage_3a_standard_variants.md
```

The three state files correspond to the three frozen execution states.

---

## 12.2 Standard Variant Dimensions

The Stage 3A standard taxonomy contains:

| ID | Variant |
|---|---|
| V01 | LEX — Lexical Reformulation |
| V02 | SYN — Syntactic Reformulation |
| V03 | NAT — Conversational Naturalization |
| V04 | EXP — Explicitness Variation |
| V05 | LEN — Length Variation |
| V06 | DSC — Discourse Structure |
| V07 | PRG — Pragmatic Reformulation |
| V08 | CMK — Conversational Marker Variation |
| V09 | HES — Hesitation / Self-Correction |
| V10 | QST — Question / Statement Framing |

\[
N_{variant\ types}=10
\]

However, Stage 3A does **not** impose a blind requirement that every scenario receive every variant type.

The construction plan explicitly treats the variants as **coverage dimensions**.

---

# 13. Stage 3A Quantity Rule

Stage 3A has **no fixed mandatory final sample count**.

The source construction plan requires expansion until scenarios have adequate:

- lexical diversity;
- syntactic diversity;
- conversational diversity;
- explicitness diversity;
- sentence-length diversity;
- indirectness diversity;
- shortcut resistance.

Therefore:

\[
N_{Stage3A,\ final}
\neq
fixed\ quota
\]

and should be determined by semantic and linguistic coverage.

### Planning capacity, not final quota

If all six state-specific standard variants were generated once for every Stage 1 initial anchor, the reference generation capacity would be:

\[
135\ anchors \times 6
=\boxed{810\ candidate\ variants}
\]

This **810 is only a planning/reference capacity**.

It must **not** be treated as a mandatory final Stage 3A dataset size.

Additional targeted variants may be generated for scenarios that remain linguistically narrow, while redundant variants should be rejected.

---

# 14. Stage 3A State-Specific Standard Coverage

The working state-specific standard variant sets are:

### Not Started

```text
LEX
NAT
EXP
PRG
CMK
QST
```

\[
6\ standard\ dimensions
\]

### In Progress

```text
LEX
SYN
NAT
EXP
LEN
DSC
```

\[
6\ standard\ dimensions
\]

### Completed

```text
LEX
SYN
NAT
EXP
PRG
DSC
```

\[
6\ standard\ dimensions
\]

Thus:

\[
6\ dimensions/state \times 3
=\boxed{18\ state\text{-}variant\ slots}
\]

Again, these are **coverage slots**, not a mandatory 18-example quota per scenario.

---

# 15. Stage 3B — Boundary / Contrast / Distractor Expansion

Stage 3B expands the validated Stage 2 resources.

The mapping is:

```text
Stage 2A Boundary Anchors
        ↓
Stage 3B-A Boundary-Preserving Variants

Stage 2B Minimal Pairs
        ↓
Stage 3B-B Contrast-Preserving Variants

Stage 2C Hard Negatives
        ↓
Stage 3B-C Distractor-Preserving Variants
```

---

# 16. Stage 3B File Set

```text
s3b/
├── 2a_boundary_anchor/
│   ├── ba01_not_started_in_progress_variants.md
│   ├── ba02_in_progress_completed_variants.md
│   └── ba03_not_started_completed_variants.md
│
├── 2b_minimal_pair/
│   ├── mp01_not_started_in_progress_variants.md
│   ├── mp02_in_progress_completed_variants.md
│   └── mp03_not_started_completed_variants.md
│
└── 2c_hard_negative/
    ├── hn01_not_started_in_progress_variants.md
    ├── hn02_in_progress_completed_variants.md
    └── hn03_not_started_completed_variants.md
```

---

# 17. Stage 3B-A — Boundary Anchor Variants

There are:

\[
18\ Stage2A\ parents
\]

The working target is:

\[
6\ candidates/parent
\]

Therefore:

\[
18 \times 6
=\boxed{108\ candidates}
\]

### Distribution

| Boundary | Stage 2A Parents | Variants/Parent | Candidates |
|---|---:|---:|---:|
| B01 | 6 | 6 | 36 |
| B02 | 6 | 6 | 36 |
| B03 | 6 | 6 | 36 |
| **Total** | **18** | **6** | **108** |

Standard Stage 3B-A variation set:

```text
LEX
SYN
NAT
EXP
PRG
CMK
```

---

# 18. Stage 3B-B — Minimal-Pair Variants

There are:

\[
18\ minimal\ pair\ families
\]

Each family contains two matched utterances.

The working target is six **paired variants per family**.

Therefore:

\[
18\ families \times 6
=\boxed{108\ paired\ variants}
\]

Because each paired variant contains two utterances:

\[
108 \times 2
=\boxed{216\ utterances}
\]

### Distribution

| Boundary | Pair Families | Paired Variants/Family | Variant Pairs | Utterances |
|---|---:|---:|---:|---:|
| B01 | 6 | 6 | 36 | 72 |
| B02 | 6 | 6 | 36 | 72 |
| B03 | 6 | 6 | 36 | 72 |
| **Total** | **18** | **6** | **108** | **216** |

Standard paired variant set:

```text
LEX
SYN
NAT
EXP
LEN
CMK
```

Both sides must be transformed jointly.

---

# 19. Stage 3B-C — Hard-Negative Variants

There are:

\[
18\ Stage2C\ parents
\]

The working target is:

\[
6\ variants/parent
\]

Therefore:

\[
18 \times 6
=\boxed{108\ candidates}
\]

### Distribution

| Boundary | Stage 2C Parents | Variants/Parent | Candidates |
|---|---:|---:|---:|
| B01 | 6 | 6 | 36 |
| B02 | 6 | 6 | 36 |
| B03 | 6 | 6 | 36 |
| **Total** | **18** | **6** | **108** |

Standard Stage 3B-C variant set:

```text
LEX
NAT
EXP
DSC
PRG
CMK
```

---

# 20. Stage 3B Total

Stage 3B-A:

\[
108\ candidates
\]

Stage 3B-B:

\[
216\ utterances
\]

Stage 3B-C:

\[
108\ candidates
\]

Therefore:

\[
108+216+108
=\boxed{432\ utterances}
\]

This is the current Stage 3B **working generation target**.

---

# 21. Complete Pipeline Numbers

## Stage 1

```text
15 semantic subtypes
45 semantic scenarios
135 initial anchors
```

## Stage 2

```text
18 boundary anchors
18 minimal-pair families
36 minimal-pair utterances
18 hard negatives
```

## Stage 3A

```text
No mandatory final quota
10 standard variant dimensions
6 state-specific standard dimensions/state

Reference planning capacity:
135 initial anchors × 6
= 810 candidate variants
```

## Stage 3B

```text
108 boundary-anchor variants
216 minimal-pair variant utterances
108 hard-negative variants

Total = 432 utterances
```

---

# 22. Stage-Wise Summary Table

| Stage | Resource | Quantity | Status of Number |
|---|---|---:|---|
| S1 | Semantic subtypes | 15 | Working target |
| S1 | Semantic scenarios | 45 | Working target |
| S1 | Initial anchors | 135 | Working target |
| S2A | Boundary anchors | 18 | Initial planning target |
| S2B | Minimal-pair families | 18 | Initial planning target |
| S2B | Minimal-pair utterances | 36 | Derived from 18 pairs |
| S2C | Hard negatives | 18 | Initial planning target |
| S3A | Standard variant dimensions | 10 | Fixed taxonomy |
| S3A | State-specific standard dimensions | 18 | Coverage slots |
| S3A | Reference candidate capacity | 810 | **Not a final quota** |
| S3B-A | Boundary-anchor variants | 108 | Working generation target |
| S3B-B | Minimal-pair variant pairs | 108 | Working generation target |
| S3B-B | Minimal-pair variant utterances | 216 | Derived |
| S3B-C | Hard-negative variants | 108 | Working generation target |
| S3B | Total utterance-level resources | 432 | Working generation target |

---

# 23. Mathematical Summary

Let:

\[
S=3
\]

be the number of execution states.

Let:

\[
U=5
\]

be the target number of semantic subtypes per state.

Let:

\[
C=15
\]

be the target number of semantic scenarios per state.

Let:

\[
A=3
\]

be the number of Stage 1 anchors per scenario.

Then:

### Stage 1

\[
N_{subtypes}=S\times U=3\times5=\boxed{15}
\]

\[
N_{scenarios}=S\times C=3\times15=\boxed{45}
\]

\[
N_{anchors}=45\times3=\boxed{135}
\]

---

For Stage 2, let:

\[
B=3
\]

be the number of state boundaries.

### Stage 2A

\[
N_{BA}=B\times6=3\times6=\boxed{18}
\]

### Stage 2B

\[
N_{MP,families}=B\times6=3\times6=\boxed{18}
\]

\[
N_{MP,utterances}=18\times2=\boxed{36}
\]

### Stage 2C

\[
N_{HN}=B\times6=3\times6=\boxed{18}
\]

Therefore:

\[
N_{S2,utterance-level}
=18+36+18
=\boxed{72}
\]

---

### Stage 3A reference capacity

Using six state-specific standard variants per Stage 1 anchor:

\[
N_{S3A,reference}=135\times6=\boxed{810}
\]

But:

\[
\boxed{810\neq mandatory\ final\ dataset\ size}
\]

because Stage 3A uses semantic/linguistic coverage rather than a blind quota.

---

### Stage 3B

For Stage 3B-A:

\[
18\times6=\boxed{108}
\]

For Stage 3B-B:

\[
18\ pair\ families\times6\ paired\ variants\times2
=\boxed{216\ utterances}
\]

For Stage 3B-C:

\[
18\times6=\boxed{108}
\]

Therefore:

\[
N_{S3B}=108+216+108=\boxed{432}
\]

---

# 24. Do Not Add Stage Totals Naively

The stage numbers should **not** be added together and interpreted as the number of unique final examples.

For example:

```text
Stage 1 anchors
        ↓
Stage 3A variants
```

and:

```text
Stage 2 resources
        ↓
Stage 3B variants
```

are lineage-based expansions.

Therefore, the same semantic lineage can appear in multiple stage-specific datasets.

The stage-specific totals represent **construction resources**, not mutually exclusive final samples.

---

# 25. Dataset Growth Model

The intended growth is:

```text
STAGE 1
45 semantic scenarios
        ↓
135 initial anchors
        ↓
STAGE 3A
linguistic expansion
        ↓
expanded scenario corpus


STAGE 2
18 boundary anchors
18 minimal-pair families / 36 utterances
18 hard negatives
        ↓
STAGE 3B
432 working target utterances
        ↓
boundary-robust corpus
```

The two branches are later combined during dataset compilation.

---

# 26. Important Counting Rules

## Rule 1 — Scenario ≠ utterance

One semantic scenario is an abstract execution situation.

It may have multiple natural-language realizations.

Therefore:

\[
1\ scenario \neq 1\ utterance
\]

---

## Rule 2 — Minimal pair ≠ single example

A minimal pair is a family containing two contrastive utterances.

Therefore:

\[
1\ minimal\ pair=2\ utterances
\]

---

## Rule 3 — Stage 3B paired variant ≠ single utterance

A Stage 3B-B paired variant transforms both sides jointly.

Therefore:

\[
1\ paired\ variant=2\ utterances
\]

---

## Rule 4 — Stage 3A has no blind quota

The six state-specific variant types are coverage dimensions.

They should not force six examples when a scenario already has adequate linguistic coverage.

---

## Rule 5 — Stage 3B numbers are working generation targets

The construction plan explicitly states that the six-candidate-per-parent target is a working generation target, not a mandatory final count.

Low-quality variants must be rejected.

---

# 27. Overall Construction Inventory

The complete planned inventory can therefore be summarized as:

```text
FROZEN ONTOLOGY
3 execution states
        │
        ▼
STAGE 1
15 semantic subtypes
45 semantic scenarios
135 initial anchors
        │
        ├───────────────────────┐
        │                       │
        ▼                       ▼
STAGE 3A                  STAGE 2
Linguistic Expansion      Boundary Quality
                          │
                          ├── 18 boundary anchors
                          ├── 18 pair families
                          │     └── 36 utterances
                          └── 18 hard negatives
                          │
                          ▼
                       STAGE 3B
                          │
                          ├── 108 BA variants
                          ├── 216 MP variant utterances
                          └── 108 HN variants
                          │
                          ▼
                       432 utterances
```

---

# 28. Final Working Numbers

The construction program should currently use the following numbers:

| Metric | Target |
|---|---:|
| Execution states | **3** |
| Semantic subtypes | **15** |
| Semantic scenarios | **45** |
| Stage 1 initial anchors | **135** |
| Stage 2 boundaries | **3** |
| Stage 2A boundary anchors | **18** |
| Stage 2B minimal-pair families | **18** |
| Stage 2B minimal-pair utterances | **36** |
| Stage 2C hard negatives | **18** |
| Stage 3A standard variant taxonomy | **10 types** |
| Stage 3A state-specific coverage dimensions | **18** |
| Stage 3A reference candidate capacity | **810** |
| Stage 3B-A variants | **108** |
| Stage 3B-B paired variants | **108 pairs / 216 utterances** |
| Stage 3B-C variants | **108** |
| Stage 3B working target | **432 utterances** |

---

# 29. Final Principle

The numerical targets exist to guarantee **semantic and boundary coverage**, not to reward volume.

The construction priority is:

\[
\boxed{
Semantic\ Coverage
>
Boundary\ Quality
>
Linguistic\ Diversity
>
Raw\ Quantity
}
\]

A target may be exceeded when additional examples add genuinely new semantic or linguistic coverage.

A target may be reduced when additional examples become redundant, ambiguous, low-quality, or shortcut-dependent.

The frozen ontology must remain unchanged throughout the entire construction process.
