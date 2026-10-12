# Stage 3A — Linguistic Expansion Construction Plan

**Target:** Execution Status Dataset  
**Ontology:** Execution Status Ontology V1.0  
**Stage:** Stage 3A — Linguistic Expansion of Stage 1  
**Input:** Frozen Stage-1 semantic scenarios and validated initial anchors  
**Output:** Linguistically diverse Stage-3A realizations

---

## 1. Objective

Stage 3A expands the frozen Stage-1 semantic space into a broader set of natural-language realizations.

The central objective is:

> **Same Execution Status + same semantic scenario → diverse linguistic realizations.**

Stage 3A must increase linguistic diversity without changing the underlying execution meaning.

The classifier should therefore encounter multiple ways of expressing the same execution state rather than learning a fixed sentence pattern for each semantic scenario.

The three frozen Execution Status labels remain:

```text
Not Started
In Progress
Completed
```

---

## 2. Position in the Construction Pipeline

```text
Frozen Execution Status Ontology
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
execution_status
semantic_subtype
scenario_id
scenario_description
execution_condition
target_task
execution_dimension
initial_anchor
```

Every generated variant must retain its parent lineage.

---

## 4. Semantic Invariants

The following must remain unchanged across all variants derived from one scenario:

1. Execution Status
2. Semantic Subtype
3. Semantic Scenario
4. Execution Condition
5. Target Task
6. Current Execution State
7. Relevant Conversational Situation

Conceptually:

```text
Parent Scenario
        ↓
   ┌────┼────┐
   V1   V2   V3 ...
    │    │    │
    └────┴────┘
 Same execution meaning
 Different linguistic realization
```

A variant is invalid if the linguistic change creates a different execution state.

---

## 5. Linguistic Variation Space

Stage 3A should use controlled variation dimensions rather than unrestricted paraphrasing.

### 5.1 Lexical Variation

Change wording while preserving execution meaning.

Examples:

```text
"I haven't started it."
"I haven't gotten to it yet."
"I still haven't done it."
```

These are valid only when they preserve the same underlying Not Started scenario.

### 5.2 Syntactic Variation

Vary grammatical structure.

Examples:

```text
"I'm doing it now."
"I'm currently working on it."
"That is what I'm working on right now."
```

### 5.3 Conversational Naturalization

Transform canonical wording into ordinary dialogue.

Example:

```text
Canonical:
"I have not completed the task."

Natural:
"I haven't finished it yet."
```

### 5.4 Explicitness Variation

Vary how directly the execution state is expressed.

```text
Explicit:
"I've finished the exercises."

Less explicit:
"That's all done."
```

The less explicit form must still support the same execution interpretation in context.

### 5.5 Sentence-Length Variation

Use short, medium, and longer natural realizations.

```text
Short:
"Not yet."

Medium:
"Not yet, I haven't started."

Long:
"Not yet, I haven't started the exercise because I haven't had a chance today."
```

Length must never become an execution-status shortcut.

### 5.6 Discourse-Structure Variation

Vary placement of execution evidence within an utterance.

Examples:

```text
"Yeah, I'm doing it now."
"I've started it, and I still have a little left."
"I finished it earlier, so there's nothing left to do."
```

### 5.7 Pragmatic Reformulation

Express the same execution state through naturally different pragmatic forms.

Examples include:

- direct status statement;
- current-activity report;
- remaining-work statement;
- retrospective report;
- result-based statement;
- response after clarification;
- response after a reminder.

### 5.8 Conversational Marker Variation

Natural dialogue markers may vary:

```text
"Yeah, I'm doing it now."
"Okay, I've finished it."
"Well, I haven't started yet."
"Right, that's already done."
```

Markers must not determine the execution status independently.

### 5.9 Hesitation and Self-Correction

Use only when compatible with the parent scenario.

Examples:

```text
"Yeah, I'm... I'm doing it now."
"I haven't started—actually, I just began."
"I thought I hadn't done it, but I already finished it."
```

Self-correction is especially important because the final execution state must be represented correctly rather than the first mistaken clause.

### 5.10 Question/Statement Framing

A response may use a question-like or statement form when the execution state remains clear.

Examples:

```text
"I'm doing it now, okay?"
"I finished it. What else is left?"
```

This should be used selectively because question framing can introduce another dialogue purpose without necessarily changing Execution Status.

---

## 6. Standard Variant Taxonomy

Every Stage-3A variant should be assigned one primary `variation_type`.

The standard taxonomy is:

| Code | Variation Type | Primary Change |
|---|---|---|
| `LEX` | Lexical Reformulation | Vocabulary |
| `SYN` | Syntactic Reformulation | Sentence structure |
| `NAT` | Conversational Naturalization | Formal → natural dialogue |
| `EXP` | Explicitness Shift | Explicit ↔ implicit execution expression |
| `LEN` | Length Variation | Short ↔ medium ↔ long |
| `DSC` | Discourse Structure | Clause/order/status placement |
| `PRG` | Pragmatic Reformulation | Different natural execution-reporting form |
| `CMK` | Conversational Marker Variation | Dialogue markers/fillers |
| `HES` | Hesitation/Self-Correction | Natural hesitation/correction |
| `QST` | Question/Statement Framing | Question ↔ statement where valid |

A variant may contain secondary changes, but one primary variation type should be recorded for auditing.

---

## 7. State-Specific Expansion Strategy

Stage 3A must not treat all three states identically.

### Not Started

Prioritize variation in:

- non-execution statements;
- future/deferred action;
- current non-execution;
- conditional action;
- refusal;
- inability/unavailability;
- forgetting;
- reason-linked non-execution;
- natural references to not having begun.

Avoid making every Not Started example contain:

```text
"not yet"
"haven't started"
"will"
```

The execution state must remain clear without depending on these markers.

### In Progress

Prioritize variation in:

- current activity;
- partial execution;
- remaining work;
- halfway progress;
- multi-step execution;
- temporary interruption;
- near completion;
- indirect evidence of ongoing execution.

Avoid making every In Progress example contain:

```text
"now"
"currently"
"doing"
"started"
```

### Completed

Prioritize variation in:

- direct completion;
- retrospective reporting;
- recent completion;
- earlier completion;
- indirect completion;
- multi-step completion;
- completion plus result;
- completion plus commentary.

Avoid making every Completed example contain:

```text
"done"
"finished"
"already"
```

The actual execution state must remain primary.

---

## 8. Generation Protocol

For each validated Stage-1 anchor:

### Step 1 — Read the Parent Scenario

Identify:

- semantic subtype;
- execution condition;
- target task;
- current execution state;
- relevant contextual conditions;
- boundary risks.

### Step 2 — Select Variation Type

Choose a variation dimension that can change the wording without changing the execution state.

### Step 3 — Generate Candidate

Produce a natural user utterance.

### Step 4 — Semantic Equivalence Check

Ask:

> Would a careful annotator assign the same Execution Status and semantic scenario to this utterance in the same context?

### Step 5 — Execution-State Check

Verify:

```text
Not Started → execution has not begun
In Progress → execution has begun but is unfinished
Completed → execution has finished
```

### Step 6 — Shortcut Check

Verify that the candidate does not depend on a single temporal/status keyword, punctuation pattern, sentence length, or task name.

### Step 7 — Naturalness Check

Remove unnatural, overly engineered, or template-like language.

### Step 8 — Deduplication

Compare against existing variants from the same and neighboring scenarios.

### Step 9 — Preserve Lineage

Store the candidate with its parent scenario and anchor identifiers.

---

## 9. State-Specific Variant Coverage

Stage 3A should provide broad variation for each state while avoiding artificial symmetry.

| State | Priority Variation Areas |
|---|---|
| `Not Started` | future/deferred action, current non-execution, conditional action, refusal, inability, forgetting, natural non-execution reporting |
| `In Progress` | current activity, partial completion, remaining work, multi-step execution, interruption, near completion |
| `Completed` | direct completion, retrospective completion, indirect completion, result evidence, multi-step completion, completion commentary |

A transformation must be skipped when it would naturally move the utterance into a neighboring state.

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

Do not generate variants independently from the state label alone.

Bad:

```text
Completed → generate 100 completion sentences
```

Correct:

```text
Completed-03-S02
   ↓
validated semantic scenario
   ↓
its initial anchors
   ↓
linguistic variants preserving Completed-03-S02
```

This preserves semantic control.

---

## 11. Variant Quantity

Stage 3A defines standard variation types as **coverage dimensions**, not a blind one-variant-per-type quota for every scenario.

Generation should continue until each scenario has sufficient:

- lexical diversity;
- syntactic diversity;
- conversational diversity;
- explicitness diversity;
- sentence-length diversity;
- indirectness diversity;
- shortcut resistance.

A scenario that remains linguistically narrow should receive additional targeted variants.

A scenario that already has adequate diversity should not receive unnecessary variants merely to satisfy a numerical quota.

---

## 12. Quality-Control Rules

Reject a candidate if:

- the Execution Status changes;
- the semantic subtype changes;
- the semantic scenario changes;
- the execution condition changes;
- the target task changes;
- a neighboring execution state becomes dominant;
- future intention is incorrectly converted into execution;
- near completion is converted into completion;
- the wording is unnatural;
- the candidate is a near-duplicate;
- a temporal/status keyword determines the label;
- another project ontology becomes a hidden proxy.

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
execution_status
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

Does the variant still express the parent execution scenario?

### Level 2 — State Preservation

Does the same Execution Status remain the correct state?

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
Temporal/status cue exposure
Duplicate rate
```

Also inspect whether states are accidentally associated with:

- specific words;
- sentence length;
- punctuation;
- grammatical constructions;
- temporal expressions;
- completion words;
- progress verbs;
- future-intention verbs;
- negation;
- task vocabulary.

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

> **Increase linguistic coverage while preserving execution-state identity.**
