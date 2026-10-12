# Stage 3A — Linguistic Expansion Construction Plan

**Target:** Response Category Dataset  
**Ontology:** Response Category Ontology V1.0  
**Stage:** Stage 3A — Linguistic Expansion of Stage 1  
**Input:** Frozen Stage-1 semantic scenarios and validated initial anchors  
**Output:** Linguistically diverse Stage-3A realizations

---

## 1. Objective

Stage 3A expands the frozen Stage-1 semantic space into a broader set of natural-language realizations.

The central objective is:

> **Same Response Category + same semantic scenario → diverse linguistic realizations.**

Stage 3A must increase linguistic diversity without changing the underlying behavioral meaning.

The classifier should therefore encounter multiple ways of expressing the same behavioral reaction rather than learning a fixed sentence pattern for each semantic scenario.

---

## 2. Position in the Construction Pipeline

```text
Frozen Response Category Ontology
        ↓
Frozen Semantic Subtype Catalogue
        ↓
Frozen Semantic Scenarios
        ↓
Validated Initial Anchors
        ↓
STAGE 3A
Linguistic Expansion
        ↓
Candidate Variants
        ↓
Variant Validation
        ↓
Deduplication + Shortcut Audit
        ↓
Validated Stage-3A Resource
        ↓
STAGE 2 — Boundary Quality
```

Stage 3A must not introduce new semantic scenarios. New semantic situations belong to Stage 1.

---

## 3. Input Resources

Stage 3A operates only on validated Stage-1 resources:

```text
response_category
semantic_subtype
scenario_id
scenario_description
behavioral_core
intervention_context
initial_anchor
```

Every generated variant must retain its parent lineage.

---

## 4. Semantic Invariants

The following must remain unchanged across all variants derived from one scenario:

1. Response Category
2. Semantic Subtype
3. Semantic Scenario
4. Behavioral Core
5. Intervention Target
6. Dominant Behavioral Appraisal
7. Relevant Conversational Situation

Conceptually:

```text
Parent Scenario
        ↓
 ┌──────┼──────┐
 V1     V2     V3 ...
 │       │      │
 Same semantic meaning
 Different linguistic realization
```

A variant is invalid if the linguistic change creates a different behavioral state.

---

## 5. Linguistic Variation Space

Stage 3A should use controlled variation dimensions rather than unrestricted paraphrasing.

### 5.1 Lexical Variation

Change wording while preserving behavioral meaning.

Examples:

```text
"I'll do that."
"I can do that."
"That works for me."
"I can go with that."
```

The exact choice remains valid only when the underlying scenario is unchanged.

### 5.2 Syntactic Variation

Vary grammatical structure.

Examples:

```text
"I'll do it."
"That is something I can do."
"I can follow that."
"That plan works for me."
```

### 5.3 Conversational Naturalization

Transform formal or canonical wording into ordinary dialogue.

Examples:

```text
Canonical:
"I am willing to follow the recommendation."

Natural:
"Yeah, I can go with that."
```

### 5.4 Explicitness Variation

Vary how directly the behavioral appraisal is expressed.

```text
Explicit:
"I'll do it."

Less explicit:
"That should work for me."
```

The less explicit form must still support the same semantic interpretation.

### 5.5 Sentence-Length Variation

Use short, medium, and longer natural realizations.

```text
Short:
"Sure."

Medium:
"Sure, I can do that."

Long:
"Sure, I can work that into my routine this week."
```

Length must never become a category shortcut.

### 5.6 Discourse-Structure Variation

Vary placement of the behavioral response within a natural utterance.

Examples:

```text
"Yeah, I'll do that."
"I think that works for me, so I'll give it a try."
"That makes sense. I'll go ahead with it."
```

### 5.7 Pragmatic Reformulation

Express the same behavioral state through naturally different pragmatic forms.

Examples include:

- direct statement;
- agreement;
- preference;
- implication;
- conversational acknowledgement;
- response after clarification;
- response after consideration.

### 5.8 Conversational Marker Variation

Natural dialogue markers may vary:

```text
"Okay..."
"Yeah..."
"Right..."
"Well, sure..."
"Honestly, I can do that."
```

Markers must not determine the category independently.

### 5.9 Hesitation and Self-Correction

Use only when compatible with the parent scenario.

Examples:

```text
"Yeah, I think I can do that."
"Well, I was unsure, but I can give it a try."
```

Hesitation must not accidentally convert P to I or N, or VN to N.

### 5.10 Question/Statement Framing

A response may use a question or statement form when the parent scenario supports it.

Examples:

```text
"Sure, what time should I start?"
"Okay, should I begin with that one?"
```

This should be used selectively because question framing can change communicative purpose without necessarily changing Response Category.

---

## 6. Standard Variant Taxonomy

Every Stage-3A variant should be assigned one primary `variation_type`.

The standard taxonomy is:

| Code | Variation Type | Primary Change |
|---|---|---|
| `LEX` | Lexical Reformulation | Vocabulary |
| `SYN` | Syntactic Reformulation | Sentence structure |
| `NAT` | Conversational Naturalization | Formal → natural dialogue |
| `EXP` | Explicitness Shift | Explicit ↔ implicit expression |
| `LEN` | Length Variation | Short ↔ medium ↔ long |
| `DSC` | Discourse Structure | Clause/order/response framing |
| `PRG` | Pragmatic Reformulation | Different natural pragmatic realization |
| `CMK` | Conversational Marker Variation | Dialogue markers/fillers |
| `HES` | Hesitation/Self-Correction | Natural hesitation where valid |
| `QST` | Question/Statement Framing | Question ↔ statement where valid |

A variant may contain secondary changes, but one primary variation type should be recorded for auditing.

---

## 7. Category-Specific Expansion Strategy

Stage 3A must not treat all five categories identically.

### VP — Very Positive

Prioritize:

- enthusiasm expression;
- appreciation wording;
- proactive engagement;
- voluntary cooperation;
- strong endorsement;
- natural positive conversational forms.

Avoid reducing VP to:

```text
"Absolutely"
"Definitely"
"Thanks"
```

alone.

The behavioral strength must remain evident.

### P — Positive

Prioritize:

- ordinary acceptance;
- cooperative commitment;
- practical willingness;
- qualified acceptance;
- delayed genuine acceptance;
- ordinary conversational agreement.

Avoid making every P example contain explicit commitment verbs.

### I — Indifferent

Prioritize:

- neutral acknowledgement;
- uncertainty;
- non-commitment;
- deferred decision;
- insufficient behavioral evidence;
- context-dependent neutral responses.

Avoid turning all I examples into explicit phrases such as:

```text
"I'm not sure."
"I don't know."
"Maybe."
```

### N — Negative

Prioritize:

- reluctance;
- mild refusal;
- disagreement;
- conditional resistance;
- temporary resistance;
- recoverable opposition.

Avoid making every N example contain:

```text
"no"
"not"
"don't"
```

### VN — Very Negative

Prioritize:

- strong rejection;
- strong opposition;
- hostile reactance;
- demands to stop intervention;
- active disengagement;
- interaction termination.

Avoid making every VN example rely on words such as:

```text
"stop"
"leave me alone"
"no"
```

The behavioral intensity must remain primary.

---

## 8. Generation Protocol

For each validated Stage-1 anchor:

### Step 1 — Read the Parent Scenario

Identify:

- semantic subtype;
- behavioral core;
- intervention;
- response intensity;
- contextual conditions.

### Step 2 — Select Variation Type

Choose a variation dimension that can change the wording without changing the semantic state.

### Step 3 — Generate Candidate

Produce a natural user utterance.

### Step 4 — Semantic Equivalence Check

Ask:

> Would a careful annotator assign the same Response Category and semantic scenario to this utterance in the same context?

### Step 5 — Shortcut Check

Verify that the candidate does not depend on a single keyword, punctuation pattern, sentence length, or sentiment cue.

### Step 6 — Naturalness Check

Remove unnatural, overly engineered, or template-like language.

### Step 7 — Deduplication

Compare against existing variants from the same and neighboring scenarios.

### Step 8 — Preserve Lineage

Store the candidate with its parent scenario and anchor identifiers.

---

## 9. Category-Specific Six-Variant Matrix

Stage 3A uses **six standard variant types per Response Category**. The six types are selected according to the linguistic properties of the category; there is no requirement that all categories use the same six types.

| Category | Six Standard Variant Types | Primary purpose |
|---|---|---|
| `VP` | `LEX`, `NAT`, `EXP`, `PRG`, `CMK`, `QST` | Vary enthusiasm, appreciation, engagement, and proactive cooperation without weakening VP intensity. |
| `P` | `LEX`, `SYN`, `NAT`, `EXP`, `LEN`, `CMK` | Vary ordinary acceptance, cooperation, and commitment while avoiding escalation into VP. |
| `I` | `LEX`, `NAT`, `EXP`, `PRG`, `HES`, `QST` | Vary uncertainty, acknowledgement, non-commitment, and insufficient evidence without creating resistance. |
| `N` | `LEX`, `SYN`, `NAT`, `EXP`, `PRG`, `CMK` | Vary reluctance, disagreement, mild refusal, and conditional resistance without reaching VN. |
| `VN` | `LEX`, `SYN`, `NAT`, `EXP`, `PRG`, `DSC` | Vary strong rejection, opposition, hostility, and disengagement while preserving high reactance. |

### 9.1 Variant Type Suitability

| Variant Type | VP | P | I | N | VN |
|---|---|---|---|---|---|
| `LEX` Lexical Reformulation | Core | Core | Core | Core | Core |
| `SYN` Syntactic Reformulation | Secondary | Core | — | Core | Core |
| `NAT` Conversational Naturalization | Core | Core | Core | Core | Core |
| `EXP` Explicitness Variation | Core | Core | Core | Core | Core |
| `LEN` Length Variation | — | Core | — | — | — |
| `DSC` Discourse-Structure Variation | — | — | — | — | Core |
| `PRG` Pragmatic Reformulation | Core | — | Core | Core | Core |
| `CMK` Conversational Marker Variation | Core | Core | — | Core | — |
| `HES` Hesitation / Self-Correction | — | — | Core | — | — |
| `QST` Question / Statement Framing | Core | — | Core | — | — |

**Core** means part of the six standard types for that category. **Secondary** means potentially useful but not part of the standard six. **—** means it should generally not be used as a standard expansion type for that category because it can more easily introduce semantic drift or weakly represents the target behavioral region.

The six types are the **standard production coverage dimensions**. Individual scenarios may omit a type when the transformation would be unnatural or would alter the underlying semantic scenario.

---

## 10. Recommended Expansion Unit

The basic expansion unit is:

```text
Scenario
   ↓
Initial Anchors
   ↓
Variation Types
   ↓
Candidate Variants
```

Do not generate variants independently from the category label alone.

Bad:

```text
VP → generate 100 positive sentences
```

Correct:

```text
VP-03-S02
   ↓
validated semantic scenario
   ↓
its initial anchors
   ↓
linguistic variants preserving VP-03-S02
```

This preserves semantic control.

---

## 11. Variant Quantity

Stage 3A now defines **six standard variant types per Response Category**. These six types determine the intended linguistic coverage space. They do not require a blind one-variant-per-type quota for every scenario.

Therefore:

```text
5 categories
× 6 category-specific variant types
= 30 standard category-variant assignments
```

Within each assignment, generation may produce multiple candidates and retain only validated, non-redundant realizations. A transformation may also be skipped when it would sound unnatural or alter the semantic scenario.

Expansion should stop when the scenario has sufficient:

- lexical diversity;
- syntactic diversity;
- conversational diversity;
- explicitness diversity;
- sentence-length diversity;
- contextual robustness;
- shortcut resistance.

A scenario that remains linguistically narrow should receive additional targeted variants.

A scenario that already has adequate diversity should not receive unnecessary variants merely to satisfy a numerical quota.

---

## 12. Quality-Control Rules

Reject a candidate if:

- the Response Category changes;
- the semantic subtype changes;
- the semantic scenario changes;
- the behavioral intensity changes materially;
- the intervention target changes;
- another response state becomes dominant;
- the wording is unnatural;
- the candidate is a near-duplicate;
- a lexical shortcut determines the category;
- the candidate introduces an unrelated emotion or sentiment signal as the dominant cue;
- the candidate encodes another project dimension as a hidden proxy.

---

## 13. Human–LLM–Code Allocation

| Activity | Human | LLM | Code |
|---|:---:|:---:|:---:|
| Freeze semantic scenarios | ✓ | | |
| Select variation requirements | ✓ | Assist | |
| Generate linguistic variants | | ✓ | |
| Check schema | | | ✓ |
| Check lineage | | | ✓ |
| Detect duplicates | | | ✓ |
| Lexical/statistical audit | ✓ | Assist | ✓ |
| Semantic equivalence review | ✓ | Assist | |
| Difficult-case adjudication | ✓ | | |
| Final acceptance | ✓ | | |

The LLM provides linguistic scale; humans retain semantic authority.

---

## 14. Lineage and Leakage Control

Every variant must retain:

```text
category
semantic_subtype
scenario_id
parent_id
lineage_id
variation_type
```

All descendants of one semantic scenario must remain in the same future data split.

```text
Scenario S
   ├── Anchor A
   │     ├── Variant A1
   │     └── Variant A2
   ├── Anchor B
   │     └── Variant B1
   └── Anchor C
         └── Variant C1
```

The complete tree is one leakage group.

---

## 15. Stage-3A Validation

Validation should occur at three levels.

### Level 1 — Semantic Preservation

Does the variant still express the parent scenario?

### Level 2 — Category Preservation

Does the same Response Category remain the dominant behavioral appraisal?

### Level 3 — Linguistic Quality

Is the utterance natural, diverse, and non-template-like?

Only variants passing all three levels become validated Stage-3A data.

---

## 16. Stage-3A Coverage Audit

Measure:

```text
Lexical diversity
Syntactic diversity
Sentence-length distribution
Explicit/implicit distribution
Variation-type distribution
Subtype coverage
Scenario coverage
Conversational naturalness
Shortcut exposure
Duplicate rate
```

Also inspect whether categories are accidentally associated with:

- specific words;
- sentence length;
- punctuation;
- grammatical constructions;
- explicit commitment;
- negation;
- gratitude;
- intensifiers.

---

## 17. Final Stage-3A Output

The final Stage-3A resource should represent:

```text
Frozen Semantic Space
        ↓
Diverse Linguistic Realizations
        ↓
Validated Realization Layer
```

Stage 3A does not change the ontology, subtype catalogue, or semantic scenario inventory.

Its role is:

> **Increase linguistic coverage while preserving semantic identity.**
