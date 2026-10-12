# Stage 3A — Standard Variant Specification

**Purpose:** Define the standard linguistic variants to be generated from validated Stage-1 Execution Status anchors.

---

## 1. Definition

A **Stage-3A variant** is a new natural-language realization of an existing validated Stage-1 semantic scenario.

Formally:

```text
Variant = Linguistic Transformation
          of a Frozen Execution Scenario
```

A variant is **not** a new scenario.

---

## 2. What Must Stay the Same

For every variant derived from a parent anchor:

```text
Execution Status       SAME
Semantic Subtype       SAME
Semantic Scenario      SAME
Execution Condition    SAME
Target Task            SAME
Current Execution State SAME
Relevant Context       SAME
```

These are semantic invariants.

---

## 3. What May Change

The following may change:

```text
Word choice
Sentence structure
Length
Conversational style
Degree of explicitness
Discourse structure
Pragmatic formulation
Conversational markers
Natural hesitation
Self-correction
Question/statement framing
```

Changes are valid only when they preserve the semantic invariants.

---

## 4. Standard Variant Types

### V01 — Lexical Reformulation (`LEX`)

Same execution meaning with different vocabulary.

**Parent:**

> “I haven’t started it.”

**Variant:**

> “I haven’t gotten to it yet.”

---

### V02 — Syntactic Reformulation (`SYN`)

Same execution meaning with different grammatical structure.

**Parent:**

> “I’m doing the exercises now.”

**Variant:**

> “The exercises are what I’m working on right now.”

---

### V03 — Conversational Naturalization (`NAT`)

Convert canonical wording into natural dialogue.

**Parent:**

> “I have completed the task.”

**Variant:**

> “Yeah, I got it done.”

---

### V04 — Explicitness Variation (`EXP`)

Express the same execution state more or less directly.

**Explicit:**

> “I’m currently doing it.”

**Less explicit:**

> “That’s what I’m working on right now.”

The less explicit version is valid only if the parent context still supports the same execution interpretation.

---

### V05 — Length Variation (`LEN`)

Create short, medium, and longer natural forms.

**Short:**

> “Not yet.”

**Medium:**

> “Not yet, I haven’t started.”

**Long:**

> “Not yet, I haven’t started the exercise because I haven’t had a chance today.”

Length must not correlate systematically with execution status.

---

### V06 — Discourse-Structure Variation (`DSC`)

Reorganize clauses while preserving the same execution state.

**Parent:**

> “I’ve started it, and I still have some left.”

**Variant:**

> “I still have some left, but I’ve already started.”

The transformation is valid only if the same execution state remains clear.

---

### V07 — Pragmatic Reformulation (`PRG`)

Use a different natural pragmatic route to report the same execution state.

Examples:

```text
Current-activity report
Remaining-work report
Completion report
Result-based report
Retrospective report
Response after clarification
Response after reminder
```

The pragmatic form may vary only when the underlying execution state remains unchanged.

---

### V08 — Conversational Marker Variation (`CMK`)

Change natural dialogue markers.

Examples:

```text
“Yeah, I’m doing it now.”
“Okay, I’m doing it now.”
“Well, I’m doing it now.”
“Right, I’m doing it now.”
```

Markers must never become deterministic execution-status indicators.

---

### V09 — Hesitation / Self-Correction (`HES`)

Introduce natural hesitation or self-correction where compatible with the parent scenario.

**Parent:**

> “I’m doing it now.”

**Variant:**

> “Yeah, I’m... I’m doing it now.”

A self-correction may also be used when the final corrected execution state is unambiguous:

> “I thought I hadn’t done it, but I already finished it.”

The final semantic interpretation must remain consistent with the parent scenario.

---

### V10 — Question / Statement Framing (`QST`)

Use question-like or statement-like response forms when the same execution state remains clear.

**Example:**

> “I finished it. What else is left?”

Question framing must not introduce a new execution state.

---

## 5. Standard Variant Generation Rules

### Rule 1 — Preserve Parent Meaning

Every variant must be interpretable as another realization of the exact parent scenario.

### Rule 2 — One Primary Variation Type

Assign one primary `variation_type` to each candidate.

### Rule 3 — Naturalness First

Variants must sound like genuine user language, not generated paraphrase lists.

### Rule 4 — No Mechanical Synonym Replacement

Do not produce:

```text
finished → done → completed → over
```

without changing the broader linguistic realization.

### Rule 5 — No Execution-State Keyword Dependence

Avoid constructing a state through repeated lexical markers.

### Rule 6 — Preserve Execution Semantics

Do not accidentally change:

```text
Not Started → In Progress
In Progress → Completed
Not Started → Completed
```

through the transformation.

### Rule 7 — Preserve Contextual Conditions

If the parent scenario requires a condition, delay, prior explanation, multi-step structure, or interaction history, the variant must preserve that condition.

### Rule 8 — Avoid Unnecessary Context

Do not add dialogue history merely to make the sentence longer.

### Rule 9 — Avoid Other Ontology Signals

Do not make variants depend primarily on:

- persuasion barrier;
- dialogue purpose;
- response category;
- motivation;
- sentiment;
- deadline;
- scheduling status;
- task-manager state.

### Rule 10 — Preserve Lineage

Every variant must point to its parent scenario and anchor.

---

## 6. State-Specific Standard Variant Coverage

Stage 3A uses standard variation types for each Execution Status. The exact transformation must still be rejected if it changes the semantic scenario or produces unnatural language.

| Execution Status | Standard Variant Types | Rationale |
|---|---|---|
| `Not Started` | `LEX`, `NAT`, `EXP`, `PRG`, `CMK`, `QST` | Supports natural non-execution, future/deferred action, refusal, inability, and conditional action without collapsing into a small set of “not yet” patterns. |
| `In Progress` | `LEX`, `SYN`, `NAT`, `EXP`, `LEN`, `DSC` | Supports ongoing, partial, multi-step, remaining-work, interruption, and near-completion expressions. |
| `Completed` | `LEX`, `SYN`, `NAT`, `EXP`, `PRG`, `DSC` | Supports direct, retrospective, indirect, multi-step, result-based, and conversational completion. |

These six types define standard production coverage for each state. A specific transformation must still be rejected if it changes the execution state or creates an unnatural utterance.

---

## 7. Examples by Execution Status

### Not Started

Parent:

> “I haven’t started it yet.”

Possible variants:

```text
“I still haven’t gotten to it.”
“Not yet, I haven’t begun.”
“I haven’t done it so far.”
“I’ll get to it later.”
“I haven’t had a chance to start.”
```

All remain Not Started only when execution has not begun.

---

### In Progress

Parent:

> “I’m doing it now.”

Possible variants:

```text
“I’m working on it right now.”
“I’ve started, and I’m still doing it.”
“Yeah, I’m in the middle of it.”
“I’ve got part of it done already.”
“I’m still working through it.”
```

They remain In Progress when execution has begun but has not finished.

---

### Completed

Parent:

> “I finished it earlier.”

Possible variants:

```text
“I got it done earlier.”
“That’s already taken care of.”
“I completed it a while ago.”
“I did it earlier, so it’s done.”
“Yeah, I’ve already taken care of that.”
```

They remain Completed when execution has actually finished.

---

## 8. Variant Metadata

Every variant should contain:

```text
example_id
scenario_id
parent_id
lineage_id
execution_status
semantic_subtype
variation_type
utterance
context
target_task
source
```

Recommended optional audit fields:

```text
secondary_variation_type
generation_model
generation_prompt_version
duplicate_group_id
shortcut_flags
validation_status
annotator_1_label
annotator_2_label
adjudicated_label
ambiguity_flag
```

---

## 9. Parent–Variant Lineage

The lineage structure should be:

```text
Execution Status
   ↓
Semantic Subtype
   ↓
Semantic Scenario
   ↓
Initial Anchor
   ↓
Stage-3A Variant
```

Example:

```text
In Progress
└── IP-02 Partial Execution
    └── IP-02-S03 Remaining Work
        └── IP-02-S03-A1
            ├── V01 LEX
            ├── V03 NAT
            ├── V04 EXP
            └── V06 DSC
```

All descendants remain in the same leakage group.

---

## 10. Acceptance Test

A Stage-3A candidate is accepted only if all are true:

```text
[✓] Same semantic scenario
[✓] Same Execution Status
[✓] Same execution condition
[✓] Same target task
[✓] Natural language
[✓] Genuine linguistic variation
[✓] No deterministic lexical shortcut
[✓] Not a near-duplicate
[✓] Lineage preserved
```

If any semantic invariant fails:

```text
REJECT
```

If only the wording changes while the execution meaning remains identical:

```text
ACCEPT
```

---

## 11. Final Standard

The standard Stage-3A transformation is:

```text
ONE FROZEN SEMANTIC SCENARIO
          ↓
      MULTIPLE NATURAL
      LINGUISTIC FORMS
          ↓
 SAME EXECUTION STATE
```

The objective is not to maximize the number of paraphrases.

The objective is:

> **Maximize useful linguistic diversity while preserving execution-semantic identity.**
