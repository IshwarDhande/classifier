# Stage 3A — Execution Phases

## 1. Purpose

Stage 3A expands the validated Stage-1 semantic scenarios with additional linguistic realizations while preserving the underlying behavioral meaning.

The **semantic scenario is the unit of expansion**.

The three existing Stage-1 anchors — Direct, Indirect, and Natural Conversational — remain unchanged and remain part of the dataset. Stage 3A adds six new standard linguistic variants to each semantic scenario.

```text
Stage-1 Semantic Scenario
        │
        ├── Direct Anchor
        ├── Indirect Anchor
        ├── Natural Conversational Anchor
        │
        ├── Variant 1
        ├── Variant 2
        ├── Variant 3
        ├── Variant 4
        ├── Variant 5
        └── Variant 6
```

---

## 2. Quantitative Structure

The current Stage-1 corpus contains:

```text
5 Response Categories
× 20 scenarios/category
= 100 semantic scenarios
```

Each scenario already has:

```text
3 initial anchors/scenario
```

Therefore Stage 1 contains:

```text
100 scenarios × 3 anchors
= 300 initial anchor examples
```

Stage 3A adds:

```text
100 scenarios
× 6 new variants/scenario
= 600 new Stage-3A examples
```

The resulting corpus after Stage 3A is therefore:

```text
300 existing Stage-1 anchors
+ 600 new Stage-3A variants
= 900 examples
```

Thus:

> **Stage 3A target = 600 new variants, producing 900 total examples including the original anchors.**

The 600 figure is the planned generation target. Final accepted count may be lower after semantic-preservation, naturalness, duplication, and quality validation.

---

## 3. Execution Unit

Stage 3A will **not** be executed anchor-by-anchor.

The execution unit is:

```text
1 Semantic Scenario
        ↓
6 Stage-3A Variants
```

The three existing anchors provide the baseline linguistic realizations of the scenario. The six Stage-3A variants provide additional linguistic diversity.

The six variants are selected from the category-specific Stage-3A variant specification.

---

## 4. Phase Structure

Execution is divided into **10 phases**, with each phase containing 10 semantic scenarios.

```text
5 categories
× 2 phases/category
= 10 execution phases
```

Each phase contains:

```text
10 scenarios
× 6 new variants
= 60 new Stage-3A examples
```

Including the original anchors associated with those scenarios:

```text
10 scenarios × 3 anchors = 30 existing anchors
30 anchors + 60 new variants = 90 examples represented in the phase
```

### Phase summary

| Phase | Category | Scenarios | New Stage-3A Variants | Existing Anchors | Total Examples Represented |
|---|---|---:|---:|---:|---:|
| VP-A | VP | 10 | 60 | 30 | 90 |
| VP-B | VP | 10 | 60 | 30 | 90 |
| P-A | P | 10 | 60 | 30 | 90 |
| P-B | P | 10 | 60 | 30 | 90 |
| I-A | I | 10 | 60 | 30 | 90 |
| I-B | I | 10 | 60 | 30 | 90 |
| N-A | N | 10 | 60 | 30 | 90 |
| N-B | N | 10 | 60 | 30 | 90 |
| VN-A | VN | 10 | 60 | 30 | 90 |
| VN-B | VN | 10 | 60 | 30 | 90 |
| **Total** | **5 categories** | **100** | **600** | **300** | **900** |

---

## 5. Category-Level Phase Breakdown

### 5.1 VP — Very Positive

```text
VP-A
Scenarios 01–10
→ 10 × 6 = 60 new variants

VP-B
Scenarios 11–20
→ 10 × 6 = 60 new variants

VP total
20 × 6 = 120 new variants
```

### 5.2 P — Positive

```text
P-A
Scenarios 01–10
→ 10 × 6 = 60 new variants

P-B
Scenarios 11–20
→ 10 × 6 = 60 new variants

P total
20 × 6 = 120 new variants
```

### 5.3 I — Indifferent

```text
I-A
Scenarios 01–10
→ 10 × 6 = 60 new variants

I-B
Scenarios 11–20
→ 10 × 6 = 60 new variants

I total
20 × 6 = 120 new variants
```

### 5.4 N — Negative

```text
N-A
Scenarios 01–10
→ 10 × 6 = 60 new variants

N-B
Scenarios 11–20
→ 10 × 6 = 60 new variants

N total
20 × 6 = 120 new variants
```

### 5.5 VN — Very Negative

```text
VN-A
Scenarios 01–10
→ 10 × 6 = 60 new variants

VN-B
Scenarios 11–20
→ 10 × 6 = 60 new variants

VN total
20 × 6 = 120 new variants
```

---

## 6. Phase Execution Order

The recommended execution order is:

```text
VP-A
  ↓
VP-B
  ↓
P-A
  ↓
P-B
  ↓
I-A
  ↓
I-B
  ↓
N-A
  ↓
N-B
  ↓
VN-A
  ↓
VN-B
```

Each phase should be completed and validated before proceeding to the next phase.

---

## 7. Phase-Level Production Procedure

For each phase:

```text
Load 10 semantic scenarios
        ↓
Retain the 3 existing anchors for each scenario
        ↓
Generate 6 Stage-3A variants/scenario
        ↓
60 new candidate variants
        ↓
Semantic preservation check
        ↓
Linguistic naturalness check
        ↓
Variant-type compliance check
        ↓
Duplicate / near-duplicate check
        ↓
Category-specific shortcut check
        ↓
Accept / regenerate / reject
        ↓
Freeze phase output
```

The generation process must not modify the underlying Stage-1 semantic scenario or its three original anchors.

---

## 8. Phase-Level Quality Gate

Before moving from Phase X to Phase X+1, verify:

1. All 10 scenarios were processed.
2. Each scenario received six intended Stage-3A variant types.
3. The behavioral interpretation remains unchanged.
4. No variant introduces a new semantic scenario.
5. Variants are linguistically distinct from the existing anchors.
6. Variants are not merely superficial word substitutions where richer variation is expected.
7. No obvious lexical or formatting shortcut dominates the category.
8. No unacceptable duplication or near-duplication remains.
9. Rejected variants have been regenerated or explicitly excluded.
10. Scenario-to-variant lineage is preserved.

A phase is considered complete only after these checks pass.

---

## 9. Category-Level Quality Gate

After completing both phases of a category:

```text
Category
  ↓
20 scenarios
  ↓
120 new variants
  ↓
Category-level QC
```

Category-level QC should examine:

- coverage of the six designated variant types;
- linguistic diversity;
- consistency of behavioral meaning;
- category-specific semantic risks;
- repetition and template artifacts;
- lexical shortcut formation;
- balance across the four semantic subtypes.

Only after the category passes this gate should execution proceed to the next category.

---

## 10. Final Stage-3A Output

After all 10 phases:

```text
100 semantic scenarios
        ↓
300 existing Stage-1 anchors
        +
600 accepted Stage-3A variants
        ↓
900 total examples
```

The final Stage-3A corpus must preserve the lineage:

```text
Category
  ↓
Subtype
  ↓
Scenario
  ↓
Original Anchor / Stage-3A Variant
```

Stage 3A therefore increases **linguistic realization diversity**, not semantic scenario count.

---

## 11. Execution Principle

> **Execute Stage 3A at the scenario level, in 10-scenario batches, with category-level checkpoints. Keep the three Stage-1 anchors as permanent baseline examples and add six new linguistic variants per scenario.**

The resulting planning target is:

```text
100 scenarios
× 6 new variants
= 600 new Stage-3A variants

300 existing anchors
+ 600 new variants
= 900 total examples
```
