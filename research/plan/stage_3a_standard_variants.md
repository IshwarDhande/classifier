# Stage 3A — Standard Variant Specification

**Purpose:** Define the standard linguistic variants to be generated from validated Stage-1 anchors.

---

## 1. Definition

A **Stage-3A variant** is a new natural-language realization of an existing validated Stage-1 semantic scenario.

Formally:

```text
Variant = Linguistic Transformation
          of a Frozen Semantic Scenario
```

A variant is **not** a new scenario.

---

## 2. What Must Stay the Same

For every variant derived from a parent anchor:

```text
Response Category      SAME
Semantic Subtype       SAME
Semantic Scenario      SAME
Behavioral Core        SAME
Intervention Target    SAME
Dominant Appraisal     SAME
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
Question/statement framing
```

Changes are valid only when they preserve the semantic invariants.

---

## 4. Standard Variant Types

### V01 — Lexical Reformulation (`LEX`)

Same meaning with different vocabulary.

**Parent:**
> “I’ll do that.”

**Variant:**
> “I can go ahead with that.”

---

### V02 — Syntactic Reformulation (`SYN`)

Same meaning with different grammatical structure.

**Parent:**
> “I’ll follow the recommendation.”

**Variant:**
> “That recommendation is something I can follow.”

---

### V03 — Conversational Naturalization (`NAT`)

Convert canonical wording into natural dialogue.

**Parent:**
> “I am willing to try this.”

**Variant:**
> “Yeah, I can give it a try.”

---

### V04 — Explicitness Variation (`EXP`)

Express the same behavioral state more or less directly.

**Explicit:**
> “I’m willing to do it.”

**Less explicit:**
> “That should work for me.”

The implicit version is valid only if the parent context still supports the same behavioral interpretation.

---

### V05 — Length Variation (`LEN`)

Create short, medium, and longer natural forms.

**Short:**
> “Sure.”

**Medium:**
> “Sure, I can do that.”

**Long:**
> “Sure, I can work that into my routine this week.”

Length must not correlate systematically with category.

---

### V06 — Discourse-Structure Variation (`DSC`)

Reorganize clauses while preserving the same response.

**Parent:**
> “I understand, and I’ll do it.”

**Variant:**
> “That makes sense. I’ll go ahead with it.”

---

### V07 — Pragmatic Reformulation (`PRG`)

Use a different natural pragmatic route to express the same behavioral appraisal.

Examples:

```text
Agreement
Preference
Willingness
Acknowledgement
Commitment
Consideration
Response after clarification
```

The pragmatic function may vary only when the underlying Response Category remains unchanged.

---

### V08 — Conversational Marker Variation (`CMK`)

Change natural dialogue markers.

Examples:

```text
“Okay, I can do that.”
“Yeah, I can do that.”
“Right, I can do that.”
“Well, sure, I can do that.”
```

Markers must never become deterministic category indicators.

---

### V09 — Hesitation / Self-Correction (`HES`)

Introduce natural hesitation or self-correction where compatible with the parent scenario.

**Parent:**
> “I’ll give it a try.”

**Variant:**
> “Well, yeah, I think I can give it a try.”

This variant type is especially useful for scenarios where hesitation is already compatible with the semantic state.

It must not change:

```text
P → I
P → N
N → VN
```

or any other category transition.

---

### V10 — Question / Statement Framing (`QST`)

Use question-like or statement-like response forms when the same behavioral appraisal remains clear.

**Example:**
> “Sure, should I start with that one?”

The question must not introduce a different dominant response category.

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
good → nice → fine → great → excellent
```

without changing the broader linguistic realization.

### Rule 5 — No Category Keyword Dependence

Avoid constructing a category through repeated lexical markers.

### Rule 6 — Preserve Behavioral Intensity

Do not accidentally strengthen or weaken the appraisal.

Examples:

```text
Ordinary acceptance → strong enthusiasm
```

is not a valid P variant.

```text
Reluctance → explicit hostility
```

is not a valid N variant.

### Rule 7 — Preserve Contextual Conditions

If the parent scenario requires a condition, delay, prior explanation, or interaction history, the variant must preserve that condition.

### Rule 8 — Avoid Unnecessary Context

Do not add dialogue history merely to make the sentence longer.

### Rule 9 — Avoid Other Ontology Signals

Do not make variants depend on:

- task completion;
- execution status;
- persuasion barrier;
- dialogue purpose;
- emotion;
- topic.

### Rule 10 — Preserve Lineage

Every variant must point to its parent scenario.

---

## 6. Category-Specific Six-Variant Standard

Stage 3A uses six standard variant types for each Response Category. The six are deliberately category-specific because the linguistic realization of enthusiasm, ordinary acceptance, uncertainty, resistance, and strong rejection is not identical.

| Category | Six Standard Variant Types | Rationale |
|---|---|---|
| `VP` | `LEX`, `NAT`, `EXP`, `PRG`, `CMK`, `QST` | Supports variation in enthusiasm, appreciation, proactive engagement, and voluntary cooperation. `QST` is useful for proactive follow-up questions. |
| `P` | `LEX`, `SYN`, `NAT`, `EXP`, `LEN`, `CMK` | Supports ordinary acceptance and commitment across concise, expanded, syntactically varied, and naturally conversational forms. |
| `I` | `LEX`, `NAT`, `EXP`, `PRG`, `HES`, `QST` | Supports uncertainty, acknowledgement, non-commitment, and clarification without forcing acceptance or resistance. |
| `N` | `LEX`, `SYN`, `NAT`, `EXP`, `PRG`, `CMK` | Supports reluctance, disagreement, mild refusal, and conditional resistance while preserving recoverability. |
| `VN` | `LEX`, `SYN`, `NAT`, `EXP`, `PRG`, `DSC` | Supports strong rejection, opposition, hostility, and active disengagement, including discourse-level closure. |

These six types define the standard production coverage for each category. A specific transformation must still be rejected if it changes the semantic scenario or creates an unnatural utterance.

---

## 7. Examples by Response Category

### VP

Parent:

> “Thanks, that really helped.”

Possible variants:

```text
“Thank you, that was really useful.”
“I really appreciate that. It helped a lot.”
“Thanks, that cleared things up for me.”
“Honestly, that was exactly what I needed.”
```

All remain VP only when strong appreciation remains the dominant behavioral appraisal.

---

### P

Parent:

> “Yeah, I can do that.”

Possible variants:

```text
“Sure, I can do that.”
“Okay, that works for me.”
“I can go ahead with that.”
“Yeah, I’ll take care of it.”
```

The variants remain P when they express ordinary cooperation rather than strong enthusiasm.

---

### I

Parent:

> “I’m not sure yet.”

Possible variants:

```text
“I haven’t decided yet.”
“I’ll have to think about it.”
“I’m still considering it.”
“I don’t know yet.”
“Let me think about that.”
```

They remain I only when they express uncertainty/non-commitment without behavioral resistance.

---

### N

Parent:

> “I’d rather not do that.”

Possible variants:

```text
“I don’t really want to do that.”
“I’d prefer another option.”
“That’s not something I’m comfortable doing.”
“I don’t think I want to go with that.”
“I’d rather take a different approach.”
```

They remain N when resistance is meaningful but still potentially recoverable.

---

### VN

Parent:

> “No. I’m not doing that.”

Possible variants:

```text
“I’m completely refusing that.”
“I’m not going along with this.”
“No, absolutely not.”
“I’ve made my decision. I’m not doing it.”
“That’s not happening.”
```

They remain VN only when strong rejection remains the dominant behavioral response.

---

## 8. Variant Metadata

Every variant should contain:

```text
example_id
scenario_id
parent_id
lineage_id
category
semantic_subtype
variation_type
utterance
context
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
Category
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
P
└── P-02 Cooperative Commitment
    └── P-02-S03 Specific Commitment
        └── P-02-S03-A1
            ├── V01 LEX
            ├── V03 NAT
            ├── V04 EXP
            └── V05 LEN
```

All descendants remain in the same leakage group.

---

## 10. Acceptance Test

A Stage-3A candidate is accepted only if all are true:

```text
[✓] Same semantic scenario
[✓] Same Response Category
[✓] Same behavioral core
[✓] Same intervention target
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

If only the wording changes while the behavioral meaning remains identical:

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
 SAME BEHAVIORAL APPRAISAL
```

The objective is not to maximize the number of paraphrases.

The objective is:

> **Maximize useful linguistic diversity while preserving semantic identity.**
