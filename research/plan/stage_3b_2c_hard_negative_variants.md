# Stage 3B-C — Hard Negative Variant Specification

**Input:** Stage 2C Hard Negatives  
**Expansion unit:** Individual hard-negative example  
**Goal:** Distractor-preserving linguistic expansion

## 1. Purpose

Stage 2C tests whether the classifier can resist misleading surface cues. Stage 3B-C expands those cues while preserving the target behavioral category.

> **Vary the distractor realization, not the behavioral label.**

## 2. Fixed Invariants

Preserve:

- target Response Category;
- boundary;
- hard-negative mechanism;
- dominant behavioral reaction;
- intervention;
- conversational situation;
- distractor-target relationship.

## 3. Mechanism-Specific Expansion

### HN01 — Competing Keyword
Change the misleading keyword while preserving the dominant behavior.

### HN02 — Competing Phrase
Replace the misleading phrase with another natural distractor carrying the same competing implication.

### HN03 — Misleading Opening Clause
Reformulate or reposition the opening cue while keeping later behavioral evidence dominant.

### HN04 — Self-Correction
Vary the initial mistaken interpretation and correction while preserving the final behavioral state.

### HN05 — Multiple Competing Cues
Vary the combination/order of distractors without allowing them to become the true behavioral label.

### HN06 — Strong Conversational Distractor
Vary prior interaction references, politeness, frustration, gratitude, or conversational framing while preserving current behavior.

## 4. Standard Six Variants

| Variant | Type | Purpose |
|---|---|---|
| HN-V01 | `LEX` | Change distractor vocabulary |
| HN-V02 | `NAT` | Naturalize distractor |
| HN-V03 | `EXP` | Change distractor/target explicitness |
| HN-V04 | `DSC` | Change discourse ordering |
| HN-V05 | `PRG` | Change pragmatic realization |
| HN-V06 | `CMK` | Change conversational markers |

`SYN`, `LEN`, `HES`, and `QST` may be used selectively.

## 5. Distractor Preservation

The intended structure is:

```text
Surface cue
     ↓
Potentially misleading
     ↓
BUT
     ↓
Not the dominant behavioral evidence
```

A variant is invalid if the distractor becomes the actual behavioral response.

## 6. Controlled Distractor Strength

Where useful, variants may be organized as:

```text
HN-L1 → weak distractor
HN-L2 → moderate distractor
HN-L3 → strong distractor
```

The distractor must never become strong enough to legitimately change the target category.

## 7. Forbidden Transformations

Reject if:

- distractor becomes dominant behavioral evidence;
- target category changes;
- hard-negative mechanism disappears;
- example becomes an ordinary prototype;
- competing cue becomes deterministic;
- example becomes sentiment-only;
- pragmatic reversal becomes ambiguous without required context.

## 8. Acceptance Test

```text
[✓] Same target category
[✓] Same hard-negative mechanism
[✓] Competing cue still present
[✓] Target behavioral evidence remains dominant
[✓] Natural language
[✓] No lexical shortcut
[✓] No category drift
```

## 9. Leakage

All variants derived from one hard-negative family remain one leakage group. Retain `hard_negative_type` for later evaluation and error analysis.
