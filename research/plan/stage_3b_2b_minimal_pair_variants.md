# Stage 3B-B — Minimal Pair Variant Specification

**Input:** Stage 2B Minimal Pairs  
**Expansion unit:** Complete minimal-pair family  
**Goal:** Contrast-preserving linguistic expansion

## 1. Purpose

Minimal pairs teach that highly similar situations can receive different categories because the user's behavioral reaction changes.

Therefore Stage 3B-B expands the **pair**, not the utterances independently.

```text
Shared situation
      ↓
A response ↔ B response
      ↓
Paired linguistic expansion
```

## 2. Fixed Invariants

Preserve:

- same boundary;
- same intervention;
- same task context;
- same conversational position;
- comparable information;
- comparable linguistic difficulty;
- same relevant history;
- primary A↔B behavioral contrast.

## 3. Standard Six Paired Variants

| Variant | Type | Construction |
|---|---|---|
| MP-V01 | `LEX` | Reformulate both sides with matched vocabulary |
| MP-V02 | `SYN` | Change syntax on both sides comparably |
| MP-V03 | `NAT` | Naturalize both sides |
| MP-V04 | `EXP` | Change explicitness while retaining contrast |
| MP-V05 | `LEN` | Use matched short/medium/long realizations |
| MP-V06 | `CMK` | Vary conversational markers comparably |

`PRG`, `DSC`, `HES`, and `QST` may be used selectively.

## 4. Pair Generation Rule

Generate both sides jointly:

```text
Original pair
    ↓
Identify shared situation
    ↓
Identify exact behavioral contrast
    ↓
Transform both sides
    ↓
Re-check contrast
```

Do not independently paraphrase the two sides.

## 5. Matched-Difficulty Principle

Do not make one side easier because it is:

- much longer;
- much more emotional;
- much more explicit;
- much more polite;
- syntactically simpler;
- packed with category keywords.

## 6. Boundary-Specific Focus

- **VP ↔ P:** enthusiasm/engagement vs ordinary acceptance.
- **P ↔ I:** behavioral commitment vs non-commitment.
- **I ↔ N:** insufficient evidence vs actual resistance.
- **N ↔ VN:** recoverable resistance vs strong rejection/reactance.
- **Non-adjacent:** preserve the larger behavioral difference without sentiment-only contrast.

## 7. Forbidden Transformations

Reject if:

- only one side changes substantially;
- shared context changes;
- contrast disappears;
- one side crosses into a third category;
- lexical cues become deterministic;
- pair becomes merely positive-sentiment vs negative-sentiment.

## 8. Pair Acceptance Test

```text
[✓] Shared situation preserved
[✓] Intervention preserved
[✓] A category preserved
[✓] B category preserved
[✓] Behavioral contrast preserved
[✓] Comparable difficulty
[✓] No trivial lexical cue
[✓] Natural language
```

The pair is the primary QC unit.

## 9. Leakage

All descendants of one minimal-pair family remain together in every future split.
