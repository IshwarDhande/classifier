# Stage 3B — Construction Plan

**Target:** Response Category Dataset  
**Ontology:** Response Category Ontology V1.0  
**Stage:** Stage 3B — Linguistic Expansion of Stage 2

## 1. Objective

Stage 3B expands the boundary-focused resources created in Stage 2 without weakening the distinctions they were designed to teach.

```text
2A Boundary Anchors → Boundary-Preserving Expansion
2B Minimal Pairs    → Contrast-Preserving Expansion
2C Hard Negatives  → Distractor-Preserving Expansion
```

The objective is:

> **Increase linguistic diversity while preserving the exact diagnostic property that makes each Stage-2 example useful.**

Stage 3B must not create new ontology categories, boundaries, or semantic scenarios.

## 2. Core Invariants

### 2A Boundary Anchors
Preserve target category, competing category, boundary, anchor role, semantic position, behavioral evidence, intervention, and conversational situation.

### 2B Minimal Pairs
Preserve A/B categories, shared intervention, task context, conversational position, comparable information, comparable complexity, and the primary behavioral contrast.

### 2C Hard Negatives
Preserve target category, hard-negative mechanism, competing cue, dominant behavioral interpretation, intervention context, and distractor-target relationship.

## 3. Expansion Principle

```text
2A → vary linguistic realization of boundary evidence
2B → vary both sides while preserving contrast
2C → vary distractor realization while preserving target behavior
```

This is controlled linguistic expansion, not ordinary paraphrasing.

## 4. Expansion Unit

```text
2A: Boundary → Anchor → Variants
2B: Boundary → Minimal-Pair Family → Paired Variants
2C: Boundary → Hard-Negative Example → Variants
```

The parent family remains the leakage group.

## 5. Quantity

No blind final quota is imposed. A working generation target of **6 candidates per parent** may be used.

Planning maximum:

```text
2A: 60 × 6 = 360 candidates
2B: 60 pairs × 6 = 360 paired families = 720 utterances
2C: 60 × 6 = 360 candidates

Potential candidates = 1,440 utterances
```

Final size depends on semantic validation, deduplication, shortcut audits, and error analysis.

## 6. Standard Variation Dimensions

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

Track-specific use is defined in the separate specifications.

## 7. Generation Protocol

1. Read the complete parent.
2. Identify the semantic invariant.
3. Select a suitable variation type.
4. Generate natural conversational language.
5. Verify boundary/contrast/distractor preservation.
6. Audit lexical and structural shortcuts.
7. Remove exact and near duplicates.
8. Preserve complete lineage.

## 8. Quality Control

### Semantic
- Same target behavioral meaning.
- Same boundary or contrast.
- Same intervention.
- No ontology drift.

### Linguistic
- Natural.
- Diverse.
- Non-template-like.
- No mechanical synonym replacement.

### Shortcut
No single keyword, negation pattern, punctuation pattern, sentence length, gratitude cue, commitment verb, refusal verb, or sentiment cue should determine the label.

### Leakage
All descendants of one Stage-2 family remain in the same future split.

## 9. Lineage

Recommended fields:

```text
example_id
parent_id
lineage_id
boundary_id
resource_type
response_category
closest_competing_category
variation_type
context
utterance
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

## 10. Human–LLM–Code Allocation

| Activity | Human | LLM | Code |
|---|:---:|:---:|:---:|
| Define invariants | ✓ | Assist | |
| Select variants | ✓ | Assist | |
| Generate candidates | | ✓ | |
| Semantic validation | ✓ | Assist | |
| Pair consistency | ✓ | ✓ | |
| Duplicate detection | | | ✓ |
| Statistical/shortcut audit | ✓ | Assist | ✓ |
| Lineage validation | | | ✓ |
| Final adjudication | ✓ | | |

## 11. Final Acceptance Test

```text
[✓] Parent lineage preserved
[✓] Target category preserved
[✓] Boundary/contrast preserved
[✓] Behavioral evidence preserved
[✓] Intervention preserved
[✓] Natural language
[✓] Genuine linguistic variation
[✓] No deterministic lexical shortcut
[✓] No near-duplicate
[✓] No ontology leakage
```

If a critical semantic invariant fails: **REJECT**.

## 12. Output Structure

```text
03b_linguistic_expansion/
├── 2a_boundary_anchor/
├── 2b_minimal_pair/
└── 2c_hard_negative/
```

Each track remains independently auditable.

## 13. Completion Criteria

Stage 3B is complete when every validated Stage-2 family has been considered, appropriate variants have been generated, semantic invariants preserved, candidates validated, duplicates removed, shortcuts audited, lineage frozen, and difficult cases human-adjudicated.

> **Stage 3B maximizes linguistic robustness of Stage-2 decision-boundary resources without changing what those resources are designed to teach.**
