# SRCC — Short Reply Robustness Corpus for Execution Status

## 1. Purpose

The **Short Reply Robustness Corpus (SRCC)** for Execution Status is a dedicated dataset for improving classifier robustness on very short user replies that communicate whether a target task has not started, is currently being executed, or has been completed.

The corpus follows the same conservative strategy used for the Response Category SRCC: begin with a small, deployment-oriented collection of common short expressions before introducing contextual modeling, boundary engineering, or extensive linguistic variation.

> **Research question:** Can a small corpus of common 1–7 word execution-status replies improve classification robustness on short user replies?

---

## 2. Research Hypothesis

> **H1: A small deployment-oriented corpus of common 1–7 word replies, with stable Execution Status assignments, can improve classifier performance on short execution-status replies.**

The first experiment deliberately avoids additional model complexity and uses standalone user replies.

---

## 3. Frozen Execution Status Ontology

The corpus uses the existing three-state ontology:

| Category | Meaning |
|---|---|
| `NS` | Not Started |
| `IP` | In Progress |
| `C` | Completed |

Frozen lifecycle:

```text
Not Started → In Progress → Completed
```

### Not Started

The target task has **not actually begun**. This includes stable standalone expressions of non-execution, deferred action, future action, inability, forgetting, or refusal where no execution has begun.

### In Progress

The target task has **actually begun but is not finished**. This includes current execution, partial execution, remaining work, interruption, and near completion.

### Completed

The target task has **actually finished**. This includes direct, retrospective, indirect, or result-based completion reports.

No additional Execution Status category is introduced.

---

## 4. Core Construction Principle

This SRCC is a **standalone short-reply corpus**.

Each example consists only of the user's reply:

```text
User Reply
    ↓
SRCC
    ↓
Execution Status
```

The initial experiment includes:

- no agent message;
- no dialogue history;
- no conversational context;
- no task-specific scenario requirement.

The purpose is to test whether short standalone expressions provide useful execution-status signals.

---

## 5. Strict Execution-Status Mapping Principle

Each selected expression is assigned to **exactly one Execution Status** within SRCC.

An exact expression must never appear under multiple categories.

```text
"Not yet."       → NS
"Still working." → IP
"Done."          → C
```

The following is prohibited:

```text
"Done." → C
"Done." → IP
```

If an expression is too context-dependent or ambiguous to support a stable standalone assignment, **exclude it rather than assigning it to multiple categories**.

This is an experimental constraint. It does not claim that every short expression has one universally fixed meaning in unrestricted conversation.

---

## 6. Execution Evidence Rule

Execution Status represents the **actual execution state of the target task**, not merely the presence of a temporal or status-related word.

Potential shortcut words include:

```text
now
later
already
starting
started
almost
done
finished
completed
```

These words may occur naturally, but they must not become the sole design principle for category assignment.

The central distinction remains:

```text
Has execution started?
        ↓
NO  → Not Started
YES
 ↓
Has execution finished?
        ↓
YES → Completed
NO  → In Progress
```

---

## 7. Length Constraints

Every expression must contain between **1 and 7 words**.

| Length Band | Word Count |
|---|---:|
| `SR1` | 1 word |
| `SR2` | 2–3 words |
| `SR3` | 4–7 words |

No expression longer than seven words is included in the initial corpus.

---

## 8. Dataset Size

The initial target is:

```text
3 Execution Status categories
×
3 Length Bands
×
20 Expressions
=
180 Expressions
```

| Category | 1 word | 2–3 words | 4–7 words | Total |
|---|---:|---:|---:|---:|
| NS — Not Started | 20 | 20 | 20 | 60 |
| IP — In Progress | 20 | 20 | 20 | 60 |
| C — Completed | 20 | 20 | 20 | 60 |
| **Total** | **60** | **60** | **60** | **180** |

The corpus is balanced across Execution Status and length band.

---

## 9. Construction Philosophy

The initial SRCC deliberately uses **low lexical variety**.

Priorities are:

- common conversational expressions;
- short user replies;
- stable execution-status interpretation;
- natural language;
- deployment-like wording;
- direct and compact execution reports.

This is a controlled first experiment, not a replacement for the broader Execution Status corpus.

---

## 10. Category Construction

Each category receives 60 expressions:

```text
Execution Status
│
├── SR1 — 20 one-word expressions
├── SR2 — 20 two-to-three-word expressions
└── SR3 — 20 four-to-seven-word expressions
```

Repeated for:

```text
NS — Not Started
IP — In Progress
C  — Completed
```

---

## 11. Semantic Construction

### NS — Not Started

Focus on expressions indicating that actual execution has not begun:

- non-execution;
- deferred action;
- future action;
- inability to begin;
- forgetting;
- refusal/non-execution;
- preparation without execution.

The critical distinction is:

```text
intention / preparation / non-execution
                ↓
          Not Started
```

### IP — In Progress

Focus on expressions indicating that execution has begun but remains unfinished:

- current execution;
- ongoing activity;
- partial execution;
- remaining work;
- near completion;
- temporary interruption.

```text
execution started + execution unfinished
                  ↓
             In Progress
```

### C — Completed

Focus on expressions indicating that execution has actually finished:

- direct completion;
- finished execution;
- completed action;
- completed result;
- retrospective completion.

```text
execution started + execution finished
                  ↓
               Completed
```

These descriptions guide expression selection; they do not create additional labels.

---

## 12. Execution-State Boundary Awareness

The initial SRCC does not contain formal minimal-pair or hard-negative resources, but expression selection must respect the frozen boundaries.

### B01 — Not Started ↔ In Progress

> **Has actual execution begun?**

```text
"I'll do it later."  → Not Started
"I'm doing it now."  → In Progress
```

Preparation or intention does not by itself establish execution.

### B02 — In Progress ↔ Completed

> **Has execution actually finished?**

```text
"I'm almost done." → In Progress
"I finished it."   → Completed
```

Near completion remains In Progress.

### B03 — Not Started ↔ Completed

> **Is there evidence of completed execution, or has execution not begun?**

```text
"I haven't done it." → Not Started
"I already did it."  → Completed
```

Do not reduce this distinction to a simple future-word versus completion-word lookup.

---

## 13. File Generation Plan

The corpus contains **9 expression files plus this corpus-level specification**:

```text
SRCC/
│
├── srcc.md
│
├── NS/
│   ├── 01_srcc_ns_1word.md
│   ├── 02_srcc_ns_2_3word.md
│   └── 03_srcc_ns_4_7word.md
│
├── IP/
│   ├── 04_srcc_ip_1word.md
│   ├── 05_srcc_ip_2_3word.md
│   └── 06_srcc_ip_4_7word.md
│
└── C/
    ├── 07_srcc_c_1word.md
    ├── 08_srcc_c_2_3word.md
    └── 09_srcc_c_4_7word.md
```

Each expression file contains exactly **20 accepted expressions**.

---

## 14. Individual File Structure

Each construction file should be standalone and production-grade, with minimal metadata and the expression table as the main artifact.

Recommended structure:

```text
# SRCC — Not Started — 1 Word

## Fixed Category
NS — Not Started

## Length Constraint
1 word

## Target
20 expressions

## Strict Execution-Status Mapping
Every expression in this file is permanently mapped to NS.

## Expression Inventory

| ID | Expression | Category |
|---|---|---|
| ... | ... | NS |

## Validation
- [ ] Exactly 20 expressions
- [ ] Correct length band
- [ ] Every expression maps to NS
- [ ] No cross-category exact duplicate
- [ ] No context required
- [ ] Natural standalone reply
- [ ] No task-specific wording
```

No tracker should be embedded inside individual files.

---

## 15. Quality-Control Rules

Every expression must pass:

### QC-1 — Length

```text
1 ≤ word_count ≤ 7
```

and it must belong to its assigned band.

### QC-2 — Standalone usability

The expression must function as a standalone user reply.

### QC-3 — Fixed category

The expression must have exactly one SRCC Execution Status.

### QC-4 — No cross-category duplication

The same exact expression must not occur under multiple categories.

### QC-5 — Naturalness

The expression must sound like something a real user could naturally say.

### QC-6 — No task dependence

Avoid expressions requiring knowledge of a particular task to determine the execution state.

### QC-7 — Execution evidence

The assigned state must reflect execution semantics rather than sentiment, motivation, or topic.

### QC-8 — No artificial keyword engineering

Do not manufacture expressions merely to associate isolated words with categories.

### QC-9 — Exact quota

Every category × length-band file must contain exactly 20 accepted expressions.

### QC-10 — No punctuation shortcut

Punctuation must not be used as the primary distinction between categories.

---

## 16. Cross-Category Lexical Audit

Before freezing SRCC, perform a global audit across all nine expression files.

Check:

```text
Exact duplicate
      ↓
Cross-category conflict?
      ↓
YES → REJECT / REPLACE
NO  → ACCEPT
```

Punctuation variants should not be used merely to inflate the inventory.

For example, these should be treated as the same lexical item for audit purposes:

```text
"Done."
"Done!"
```

if the only difference is punctuation.

---

## 17. Execution-State Shortcut Audit

Inspect whether category membership can be predicted from a small set of isolated words.

Potential cues include:

```text
not
yet
later
now
starting
started
working
almost
done
finished
completed
already
```

These may occur naturally, but SRCC should not become a simple dictionary:

```text
keyword → category
```

The intended signal is the short expression's execution meaning.

---

## 18. Orthogonality

Execution Status must remain distinct from the other project ontologies.

The SRCC label must not be determined primarily by:

- Response Category;
- Dialogue Purpose;
- Persuasion Barrier;
- emotion;
- sentiment;
- motivation;
- deadline status;
- scheduling status;
- task-manager operational status.

For example, positive emotion does not imply Completed, and refusal does not automatically imply Not Started. The target remains the user's **actual execution state**.

---

## 19. Construction Order

```text
Phase 1
Core short-expression inventory
        ↓
Phase 2
Assign each expression to one fixed Execution Status
        ↓
Phase 3
Separate expressions by length band
        ↓
Phase 4
Fill 20 expressions per category × length band
        ↓
Phase 5
Cross-category exact-duplicate audit
        ↓
Phase 6
Execution-semantic review
        ↓
Phase 7
Shortcut / lexical audit
        ↓
Phase 8
Human quality review
        ↓
Phase 9
SRCC freeze
```

---

## 20. Experimental Boundary

The initial Execution Status SRCC intentionally does **not** include:

- conversational context;
- agent intervention;
- dialogue history;
- task-specific scenarios;
- minimal-pair construction;
- hard-negative construction;
- extensive paraphrase expansion;
- new Execution Status categories;
- architecture changes.

These can be investigated later if the initial strategy is insufficient.

---

## 21. Initial Target

```text
                     SRCC
                       │
             ┌─────────┼─────────┐
             │         │         │
            SR1       SR2       SR3
          1 word    2–3 words  4–7 words
             │         │         │
             └─────────┼─────────┘
                       │
                3 categories
                × 20 expressions
                       │
                   180 total
```

Distribution:

```text
NS → 60
IP → 60
C  → 60
```

---

## 22. Success Criterion

The primary objective is to determine whether SRCC improves Execution Status classification specifically on short user replies.

Evaluation should compare:

```text
Existing Classifier
        vs.
Existing Classifier + Execution Status SRCC
```

Report performance separately for:

- 1-word replies;
- 2–3-word replies;
- 4–7-word replies;
- overall short replies;
- each Execution Status category.

Also inspect the three principal confusions:

```text
NS ↔ IP
IP ↔ C
NS ↔ C
```

The existing Execution Status ontology and classifier architecture should remain unchanged so that observed improvement can be attributed primarily to the short-reply training intervention.

---

## Final Principle

> **Keep the first Execution Status SRCC deliberately simple: common short replies, no context, stable standalone mappings, balanced length bands, and a small 180-expression corpus.**

The experiment should establish whether this simple intervention improves robustness before introducing context-aware, boundary-aware, or hard-negative solutions.

Most importantly:

> **The classifier should learn the user's actual execution state, not merely memorize words such as “done,” “now,” “later,” or “started.”**
