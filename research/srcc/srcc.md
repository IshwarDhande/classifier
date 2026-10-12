# SRCC — Short Reply Robustness Corpus

## 1. Purpose

The **Short Reply Robustness Corpus (SRCC)** is a dedicated dataset for improving the deployed Response Category classifier's performance on very short user replies.

The corpus is motivated by findings from the user study showing that real users frequently respond using very short utterances, often consisting of a single word and generally no more than 6–7 words.

The initial SRCC experiment deliberately uses a **simple and conservative construction strategy**.

The objective is not to model every possible contextual interpretation of short replies. Instead, the first experiment tests whether a small, controlled vocabulary of common short expressions with stable Response Category assignments can improve classification robustness.

---

# 2. Research Hypothesis

The initial experiment tests:

> **H1: A small deployment-oriented corpus of common 1–7 word replies, with strict lexical-to-category mappings, can improve Response Category classification performance on short user replies.**

The experiment intentionally avoids introducing additional model complexity, contextual information, or extensive linguistic variation.

---

# 3. Response Category Ontology

SRCC uses the existing frozen Response Category ontology:

| Category | Meaning |
|---|---|
| `VP` | Very Positive |
| `P` | Positive |
| `I` | Indifferent |
| `N` | Negative |
| `VN` | Very Negative |

No new response category is introduced for this experiment.

In particular, **Uncertain** is not added as a sixth category.

---

# 4. Core Construction Principle

SRCC is a **standalone short-reply corpus**.

Each example consists only of the user reply.

No agent message or conversational context is included.

```text
User Reply
    ↓
SRCC
    ↓
Response Category
```

The corpus therefore specifically tests whether short lexical expressions alone can provide useful classification signals.

---

# 5. Strict Lexical Mapping Principle

This is the central constraint of the initial SRCC experiment.

## 5.1 Fixed lexical-to-category mapping

Each selected short expression is assigned to **exactly one Response Category**.

Once an expression is assigned to a category, that expression must not appear under another category anywhere in SRCC.

For example:

```text
"Okay." → P
"Fine." → P
"Sure." → P
"Yes." → P

"Maybe." → I

"No." → N

"Never." → VN
```

The following is explicitly prohibited:

```text
"Okay." → P
"Okay." → I

"Fine." → P
"Fine." → N
```

---

## 5.2 No artificial lexical ambiguity

The corpus must **not deliberately reuse the same expression across categories** in order to create lexical diversity or contextual variation.

This would undermine the controlled experiment by introducing label noise.

The objective is to test a simple strategy:

> **Can stable mappings between common short expressions and Response Categories improve short-reply classification?**

---

## 5.3 Ambiguous expressions

If an expression is inherently too ambiguous to support a stable category assignment under the standalone setting, it should be **excluded rather than assigned to multiple categories**.

Therefore:

```text
Allowed:
"Okay." → P

Not allowed:
"Okay." → P / I
```

This rule is experimental and does not claim that expressions such as “okay” have universally fixed meanings in natural conversation.

It simply establishes a controlled condition for the first SRCC experiment.

---

# 6. Length Constraints

Every SRCC expression must contain between **1 and 7 words**.

Three length bands are used:

| Length Band | Word Count |
|---|---:|
| `SR1` | 1 word |
| `SR2` | 2–3 words |
| `SR3` | 4–7 words |

No example longer than seven words is included in the initial corpus.

---

# 7. Dataset Size

The initial target is:

```text
5 Response Categories
×
3 Length Bands
×
20 Expressions
=
300 Expressions
```

| Category | 1 word | 2–3 words | 4–7 words | Total |
|---|---:|---:|---:|---:|
| VP | 20 | 20 | 20 | 60 |
| P | 20 | 20 | 20 | 60 |
| I | 20 | 20 | 20 | 60 |
| N | 20 | 20 | 20 | 60 |
| VN | 20 | 20 | 20 | 60 |
| **Total** | **100** | **100** | **100** | **300** |

The initial corpus is therefore **balanced across both Response Category and length band**.

---

# 8. Construction Philosophy

SRCC intentionally uses **low lexical variety**.

The purpose is not to produce a large paraphrase corpus.

Instead, construction should focus on:

- common conversational expressions
- simple wording
- short replies
- stable lexical assignments
- natural language
- high-frequency deployment-like expressions

The corpus should answer a narrow experimental question before more sophisticated approaches are introduced.

---

# 9. Category Construction

Each category receives 60 expressions:

```text
Category
│
├── SR1 — 20 one-word expressions
├── SR2 — 20 two-to-three-word expressions
└── SR3 — 20 four-to-seven-word expressions
```

This structure is repeated for:

```text
VP
P
I
N
VN
```

---

# 10. Semantic Construction

Although SRCC uses strict lexical mapping, expressions should still be selected according to the behavioral meaning of the assigned Response Category.

### VP — Very Positive

Focus on:

- strong acceptance
- enthusiasm
- strong appreciation
- eager willingness

### P — Positive

Focus on:

- ordinary acceptance
- cooperation
- willingness
- mild agreement

### I — Indifferent

Focus on:

- neutral acknowledgment
- non-commitment
- uncertainty
- low engagement

### N — Negative

Focus on:

- reluctance
- mild refusal
- resistance
- disagreement

### VN — Very Negative

Focus on:

- strong refusal
- strong rejection
- hostility
- active disengagement

These semantic descriptions guide expression selection; they do not create additional labels.

---

# 11. File Generation Plan

The corpus will contain **15 construction files**.

```text
SRCC/
│
├── srcc.md
│
├── VP/
│   ├── 01_srcc_vp_1word.md
│   ├── 02_srcc_vp_2_3word.md
│   └── 03_srcc_vp_4_7word.md
│
├── P/
│   ├── 01_srcc_p_1word.md
│   ├── 02_srcc_p_2_3word.md
│   └── 03_srcc_p_4_7word.md
│
├── I/
│   ├── 01_srcc_i_1word.md
│   ├── 02_srcc_i_2_3word.md
│   └── 03_srcc_i_4_7word.md
│
├── N/
│   ├── 01_srcc_n_1word.md
│   ├── 02_srcc_n_2_3word.md
│   └── 03_srcc_n_4_7word.md
│
└── VN/
    ├── 01_srcc_vn_1word.md
    ├── 02_srcc_vn_2_3word.md
    └── 03_srcc_vn_4_7word.md
```

Each file contains exactly **20 candidate expressions** for its category and length band.

---

# 12. Individual File Structure

Each construction file should follow a consistent format.

Example:

```text
# SRCC — Positive — 1 Word

## Fixed Category

P — Positive

## Length Constraint

1 word

## Target

20 expressions

## Strict Lexical Mapping

Every expression in this file is permanently mapped to P.

An expression appearing in this file must not appear
under VP, I, N, or VN elsewhere in SRCC.

## Expression Inventory

1. Okay.
2. Sure.
3. Yes.
...
20. ...

## Validation

- [ ] Exactly 20 expressions
- [ ] Every expression is one word
- [ ] Every expression maps to P
- [ ] No expression is assigned to another category
- [ ] No context is required
- [ ] Natural standalone reply
- [ ] No task-specific wording
```

The same structure should be used for all 15 files.

---

# 13. Quality-Control Rules

Every expression must pass the following checks.

### QC-1 — Length

```text
1 ≤ word_count ≤ 7
```

and must belong to the assigned length band.

### QC-2 — Standalone usability

The expression must function as a standalone user reply.

### QC-3 — Fixed category

The expression must have exactly one SRCC category.

### QC-4 — No cross-category duplication

The same lexical expression must not occur under multiple categories.

### QC-5 — Naturalness

The expression must sound like something a real user could naturally say.

### QC-6 — No task dependence

Avoid task-specific expressions that require contextual information to interpret.

### QC-7 — No artificial lexical engineering

Do not manufacture unnatural expressions merely to fill the quota.

### QC-8 — Exact quota

Every category × length-band file must contain exactly 20 accepted expressions.

---

# 14. Construction Order

The dataset should be constructed systematically:

```text
Phase 1
Core expression inventory
        ↓
Phase 2
Assign each expression to one fixed category
        ↓
Phase 3
Separate expressions by length band
        ↓
Phase 4
Fill 20 expressions per category × length band
        ↓
Phase 5
Cross-category lexical duplication audit
        ↓
Phase 6
Human quality review
        ↓
Phase 7
SRCC freeze
```

---

# 15. Experimental Boundary

The initial SRCC experiment intentionally does **not** include:

- conversational context
- agent intervention
- dialogue history
- extensive paraphrasing
- contextual disambiguation
- hard-negative construction
- minimal-pair construction
- additional Response Categories
- an uncertainty class
- architecture changes

These can be investigated later if the initial strategy fails.

---

# 16. Final Initial Target

The frozen initial target is:

```text
                 SRCC
                  │
       ┌──────────┼──────────┐
       │          │          │
      SR1        SR2        SR3
    1 word     2–3 words   4–7 words
       │          │          │
       └──────────┼──────────┘
                  │
        5 categories each
        × 20 expressions
                  │
             300 total
```

The initial experiment therefore evaluates a **small, balanced, standalone, strictly lexically mapped corpus**.

If this strategy demonstrates meaningful improvement on short-reply classification, subsequent experiments can progressively introduce additional complexity.

---

# 17. Success Criterion

The primary objective is to determine whether SRCC improves classification performance specifically on short replies.

Evaluation should compare:

```text
Existing Classifier
        vs.
Existing Classifier + SRCC
```

with performance reported separately for:

- 1-word replies
- 2–3-word replies
- 4–7-word replies
- overall short replies

The experiment should preserve the existing Response Category ontology and classifier architecture so that any improvement can be attributed primarily to the short-reply training strategy.

---

## Final Principle

> **Keep the first experiment deliberately simple: common short expressions, no context, fixed lexical-to-category mapping, balanced length bands, and only 300 examples.**

The purpose is to establish whether this simple intervention works before introducing more sophisticated solutions.