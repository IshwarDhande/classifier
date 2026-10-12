# Execution Status Dataset Construction Plan — V1

**Status:** Construction Plan  
**Target:** Execution Status Classification Dataset  
**Ontology:** Execution Status Ontology V1.0 (Frozen)  
**Execution States:** `Not Started`, `In Progress`, `Completed`

---

# 1. Objective

The dataset will train a classifier to infer the **current execution state of the target task** from the user's latest response to an agent intervention.

The classifier must answer:

> **Based on the user's response, has execution of the target task not started, started but not finished, or finished?**

The classifier must model **execution state only**.

It must remain independent of:

- future intention;
- motivation;
- reason for non-execution;
- scheduling;
- deadlines;
- missed/overdue status;
- persuasion barrier;
- dialogue purpose;
- response category;
- topic or task identity.

The frozen ontology contains exactly three mutually exclusive states:

| Label | Execution Status | Core Meaning |
|---|---|---|
| `NS` | Not Started | Execution has not begun |
| `IP` | In Progress | Execution has begun but is unfinished |
| `C` | Completed | Execution has finished |

The execution lifecycle is:

```text
Not Started → In Progress → Completed
```

The classifier should learn the **execution state communicated by the user**, not the complete task lifecycle.

---

# 2. Frozen Semantic Scope

## 2.1 Classified Object

The classified object is:

> **The current execution state of the target task as communicated by the user's response.**

The agent's preceding intervention is implicit in the production representation.

Conceptually:

```text
Agent prompts/reminds user to perform target task
                    ↓
              User response
                    ↓
          Execution Status
```

## 2.2 Execution States

### `NS` — Not Started

Execution of the target task has **not yet begun**.

This includes pending, delayed, postponed, future, currently unexecuted, forgotten, conditional, uncertain, or refused execution. The reason does not create a separate execution state.

### `IP` — In Progress

Execution has **already begun** but is not yet complete.

This includes current, partial, halfway, nearly finished, multi-step, or temporarily paused execution when the task has genuinely started.

### `C` — Completed

Execution of the target task has **finished**.

This includes explicit completion and retrospective reports that the task has already been performed.

---

# 3. Orthogonality Principles

Execution Status must remain separate from the other Dialogue Interpreter dimensions.

| Dimension | Question |
|---|---|
| Response Category | How did the user react to the intervention? |
| Dialogue Purpose | What conversational function is the user performing? |
| Persuasion Barrier | Why is adherence/execution difficult? |
| Execution Status | What is the current execution state? |

Examples:

```text
"I'll do it tonight."
→ Execution Status = Not Started
→ Dialogue Purpose may be Commitment
```

```text
"I'm busy right now."
→ Execution Status = Not Started
→ Persuasion Barrier may be TimeConstraint
```

```text
"I'm taking it now."
→ Execution Status = In Progress
```

```text
"I already took it."
→ Execution Status = Completed
```

The dataset must contain such cross-ontology combinations so that execution status cannot be learned from another ontology as a shortcut.

---

# 4. Construction Architecture

The dataset follows the established research-grade construction methodology, adapted to the three-state execution ontology.

```text
FROZEN EXECUTION STATUS ONTOLOGY
            ↓
STAGE 1 — SEMANTIC COVERAGE
            ↓
Validated Execution Scenarios
            ↓
STAGE 3A — LINGUISTIC EXPANSION
            ↓
Expanded Natural-Language Resource
            ↓
STAGE 2 — BOUNDARY QUALITY
    ├── 2A Boundary Anchors
    ├── 2B Minimal Pairs
    └── 2C Hard Negatives
            ↓
STAGE 3B — BOUNDARY / CONTRAST / DISTRACTOR EXPANSION
            ↓
Final Validation
            ↓
Deduplication + Shortcut Audit
            ↓
Leakage Audit
            ↓
70/15/15 Group Split
            ↓
Diagnostic Challenge Set
            ↓
FINAL EXECUTION STATUS DATASET
```

---

# 5. Critical Difference from Response Category Construction

Execution Status is **not an ordinal behavioral-appraisal problem**.

Response Category contains five intensity-oriented states:

```text
VN < N < I < P < VP
```

Execution Status contains three lifecycle states:

```text
NS → IP → C
```

Therefore:

- lifecycle boundaries receive priority;
- execution evidence has priority over attitude or sentiment;
- future intention does not imply execution;
- reasons for non-execution do not define execution status;
- refusal does not create a new execution category;
- scheduling information is excluded from the ontology.

The core semantic question is:

> **Has execution begun? If yes, has it finished?**

---

# 6. Stage 1 — Semantic Coverage

## 6.1 Objective

Stage 1 establishes the semantic situations that each execution state must cover.

The dataset must not collapse into stereotypical forms such as:

```text
"I haven't done it." → NS
"I'm doing it."      → IP
"I did it."          → C
```

Stage 1 should answer:

> **What distinct execution situations can produce each execution state?**

---

# 7. Execution Semantic Dimensions

Important construction dimensions include:

### Not Started

- explicit non-execution;
- future intention;
- delayed action;
- postponed action;
- current inability to act;
- temporary unavailability;
- forgetting;
- low motivation;
- uncertainty;
- refusal without execution;
- conditional future action;
- planned but uninitiated action.

### In Progress

- immediate ongoing execution;
- partial execution;
- halfway execution;
- execution with remaining work;
- temporary interruption during execution;
- current physical performance;
- multi-step execution;
- active execution after a prompt;
- execution nearly finished but not complete.

### Completed

- explicit completion;
- recent completion;
- earlier completion;
- completion reported indirectly;
- completed multi-step task;
- completed task with additional commentary;
- completed task despite negative reaction;
- completion followed by additional information.

These are **construction dimensions**, not classifier labels.

---

# 8. Stage-1 Semantic Subtypes

A semantic subtype layer may organize coverage within each state. The classifier still predicts only:

```text
NS | IP | C
```

A candidate construction structure is:

```text
NS — Not Started
├── Explicit Non-Execution
├── Future / Deferred Action
├── Current Non-Execution
├── Conditional Future Action
├── Refusal Without Execution
└── Reason-Linked Non-Execution

IP — In Progress
├── Direct Ongoing Execution
├── Partial Execution
├── Near Completion
├── Multi-Step Execution
└── Temporarily Interrupted Execution

C — Completed
├── Direct Completion
├── Retrospective Completion
├── Indirect Completion
├── Multi-Step Completion
└── Completion with Additional Commentary
```

These are candidate construction regions. They must be reviewed and frozen before large-scale scenario generation.

---

# 9. Scenario Inventory

## 9.1 Planning Target

A reasonable initial planning range is:

```text
3 states
× approximately 12–20 semantic scenarios/state
≈ 36–60 semantic scenarios overall
```

A working target near:

```text
15 scenarios/state
≈ 45 semantic scenarios
```

may be used for planning.

This is a planning range, not a fixed quota. The final number should follow semantic coverage.

## 9.2 Scenario Definition

Each scenario must represent a **distinct execution situation**, not merely a paraphrase.

Recommended metadata:

```text
scenario_id
execution_status
semantic_subtype
scenario_description
execution_condition
target_task
conversational_position
difficulty_level
explicitness
closest_competing_status
```

The construction hierarchy is:

```text
Execution Situation
        ↓
Execution State
        ↓
Natural-Language Realization
```

---

# 10. Stage-1 Scenario Design Principles

## 10.1 Distinct Semantic Situations

Do not create several scenarios that differ only lexically.

For example:

```text
"I haven't done it."
"I haven't started it."
"I didn't do it yet."
```

may be linguistic variants of one underlying situation rather than three independent scenarios.

## 10.2 Execution Evidence Must Be Central

Every scenario must contain evidence relevant to execution.

Do not let labels depend primarily on:

- emotion;
- politeness;
- motivation;
- reason;
- sentiment;
- conversational purpose.

## 10.3 Task Domain Diversity

Use the project's controlled task domains:

- medication;
- hydration;
- exercise;
- physiotherapy.

Every state should occur across multiple domains. Task identity must not become a shortcut.

## 10.4 Conversational Position Diversity

Vary:

- immediately after a reminder;
- after clarification;
- after explanation;
- after a concern;
- after repeated prompting;
- after personalization;
- after a previous commitment;
- after partial progress.

Execution status must not correlate with one conversational position.

---

# 11. Stage-1 Category-Specific Coverage

## 11.1 Not Started

Cover:

- explicit non-execution;
- future intention;
- delayed execution;
- postponed execution;
- inability to start;
- temporary unavailability;
- forgetting;
- refusal;
- conditional future execution;
- uncertain future execution;
- reason-linked non-execution.

Critical rule:

```text
Future intention ≠ execution started
```

Therefore:

```text
"I'll do it tonight."
→ NS
```

## 11.2 In Progress

Cover:

- currently executing;
- partial completion;
- halfway through;
- nearly finished;
- multi-step execution;
- temporary pause during active execution;
- current physical performance;
- execution that began immediately before the response.

Critical rule:

```text
Execution started + not finished
→ IP
```

## 11.3 Completed

Cover:

- explicit completion;
- retrospective completion;
- earlier completion;
- indirect completion;
- completed multi-step task;
- completion plus additional information;
- completion with neutral or negative reaction.

Critical rule:

```text
Execution finished
→ C
```

Completion takes precedence over other commentary for the execution-status dimension.

---

# 12. Stage-1 Initial Anchors

After semantic scenarios are validated, create:

1. Direct realization
2. Indirect realization
3. Natural conversational realization

Planning target:

```text
~45 scenarios
× 3 anchors
≈ 135 Stage-1 candidates
```

### Direct

```text
"I haven't started it yet."
```

### Indirect

```text
"I'll get to it after I finish this."
```

### Natural Conversational

```text
"Yeah, give me a few minutes—I'm doing it now."
```

These are illustrative construction forms; final examples must come from validated scenarios.

---

# 13. Stage-1 Validation

Every candidate should be evaluated as:

```text
Scenario
+
Relevant Context
+
User Response
        ↓
Execution Interpretation
        ↓
NS / IP / C
```

Validation questions:

1. Has execution actually begun?
2. If execution has begun, is it finished?
3. Is the evidence about the target task?
4. Is the label independent of future intention?
5. Is the label independent of the reason for non-execution?
6. Is the label independent of sentiment/emotion?
7. Could the closest competing state reasonably be assigned?
8. Is the language natural?
9. Is the example semantically distinct?
10. Does task domain remain orthogonal to execution state?

---

# 14. Stage 3A — Linguistic Expansion of Stage 1

Stage 3A expands validated scenarios into diverse linguistic realizations.

Core principle:

> **Same execution scenario → diverse linguistic realizations → same execution state.**

Preserve:

- execution state;
- semantic scenario;
- execution condition;
- target task;
- relevant conversational situation.

Potential variation dimensions:

- lexical reformulation;
- syntactic reformulation;
- conversational naturalization;
- explicitness variation;
- sentence-length variation;
- discourse restructuring;
- pragmatic reformulation;
- conversational markers;
- hesitation;
- self-correction;
- question/statement framing where semantically valid.

Not every variation is appropriate for every scenario.

---

# 15. Execution-Specific Stage-3A Rules

## Not Started

Variants may express future action, postponement, current non-execution, conditionality, uncertainty, or explanation.

They must not imply that execution has begun.

```text
"I'll do it after work."
→ NS

"I've started it, but I'll finish after work."
→ IP
```

## In Progress

Variants must preserve evidence that execution has begun.

```text
"I'll start now."
→ NS

"I'm doing it now."
→ IP
```

The distinction between future initiation and current execution should be heavily represented.

## Completed

Variants must preserve evidence that execution has finished.

```text
"I'm almost done."
→ IP

"I'm done."
→ C
```

Completion must not be weakened into ongoing execution.

---

# 16. Stage 2 — Boundary Quality

There are two primary lifecycle boundaries:

```text
NS ↔ IP
IP ↔ C
```

A secondary contrast is:

```text
NS ↔ C
```

Thus:

```text
3 states → 3 pairwise contrasts
```

Adjacent lifecycle boundaries receive the strongest semantic emphasis.

---

# 17. Stage 2A — Boundary Anchors

For each boundary, construct:

1. A Prototype
2. B Prototype
3. A-Leaning Boundary
4. B-Leaning Boundary
5. Implicit A
6. Implicit B

Planning target:

```text
3 boundaries
× 6 anchors
= 18 boundary anchors
```

## 17.1 NS ↔ IP

Diagnostic question:

> **Has execution actually begun?**

```text
NS:
"I'll start in a few minutes."

IP:
"I'm doing it now."
```

## 17.2 IP ↔ C

Diagnostic question:

> **Has execution finished?**

```text
IP:
"I'm almost finished."

C:
"I've finished."
```

## 17.3 NS ↔ C

Diagnostic question:

> **Has the task remained unexecuted, or has execution already finished?**

This contrast tests future/non-execution against retrospective completion.

---

# 18. Stage 2B — Minimal Pairs

Generate both sides together while preserving the same task and conversational situation.

### NS ↔ IP

```text
NS:
"I'll start the exercises now."

IP:
"I'm doing the exercises now."
```

### IP ↔ C

```text
IP:
"I'm still doing the exercises."

C:
"I've finished the exercises."
```

### NS ↔ C

```text
NS:
"I haven't done the exercises yet."

C:
"I already did the exercises."
```

Preserve:

- same task;
- same conversational position;
- comparable wording complexity;
- comparable information content;
- same general situation.

Change primarily the execution state.

Planning target:

```text
3 boundaries
× 6 minimal-pair families
= 18 minimal pairs
= 36 utterances
```

---

# 19. Stage 2C — Hard Negatives

Core principle:

> **Surface wording associated with an execution state must not determine the execution label.**

Initial hard-negative mechanisms:

1. Competing Keyword
2. Competing Phrase
3. Misleading Opening Clause
4. Self-Correction
5. Multiple Competing Cues
6. Strong Conversational Distractor

Important patterns include:

- future wording with no execution;
- completion wording referring to something other than the target task;
- "almost" mistaken for completed;
- "starting" mistaken for in-progress;
- positive/negative reaction distracting from execution;
- barrier statements distracting from execution;
- mixed clauses with one dominant execution state.

Each hard negative must retain one clear gold execution state.

Planning target:

```text
3 boundaries
× 6 hard-negative families
= 18 hard-negative candidates
```

---

# 20. Execution-Specific Hard-Negative Principles

### Future intention must not imply In Progress

```text
"I'll start it right now."
→ NS
```

### Almost complete must not imply Completed

```text
"I'm nearly finished."
→ IP
```

### Completion plus negative reaction remains Completed

```text
"I hated doing it, but I finished it."
→ C
```

### Positive response with future action remains Not Started

```text
"Sure, I'll do it later."
→ NS
```

### Barrier plus current execution remains In Progress

```text
"I'm tired, but I'm doing the exercises now."
→ IP
```

These combinations prevent cross-ontology and lexical shortcuts.

---

# 21. Stage 3B — Expansion of Stage-2 Resources

Stage 3B contains:

```text
2A Boundary Anchors
        ↓
Boundary-Preserving Expansion

2B Minimal Pairs
        ↓
Contrast-Preserving Expansion

2C Hard Negatives
        ↓
Distractor-Preserving Expansion
```

## Boundary-Preserving

Preserve:

- target state;
- competing state;
- boundary;
- execution evidence;
- semantic position.

## Contrast-Preserving

Generate both sides together.

Preserve:

- shared task;
- shared conversational situation;
- comparable difficulty;
- execution-state contrast.

## Distractor-Preserving

Preserve:

- target state;
- hard-negative mechanism;
- competing execution cue;
- dominant execution evidence.

Core rule:

> **Vary the distractor realization, not the execution state.**

---

# 22. Shortcut Audit

Execution Status is particularly vulnerable to temporal and aspectual lexical shortcuts.

Audit:

```text
"already"     → not always Completed
"now"         → not always In Progress
"later"       → not always Not Started
"finished"    → inspect target-task scope
"starting"    → not automatically In Progress
"almost"      → not Completed
"will"        → not Started in every possible context
"done"        → verify what was done
```

Also audit:

- tense;
- aspect;
- temporal adverbs;
- completion verbs;
- progress verbs;
- future modals;
- sentence length;
- punctuation;
- task vocabulary;
- explicit time expressions.

The same surface forms should occur across states whenever naturally possible.

---

# 23. Cross-Ontology Shortcut Audit

Do not allow the classifier to infer execution state from:

### Dialogue Purpose

```text
Commitment → NS
Information → C
```

### Persuasion Barrier

```text
TimeConstraint → NS
Forgetfulness → NS
```

### Response Category

```text
Positive → C
Negative → NS
```

Instead include combinations such as:

```text
"Okay, I'll do it later."
→ P + NS

"No, I'm not doing it."
→ VN + NS

"I'm taking it now."
→ VP + IP

"Done."
→ VP + C
```

These are conceptual examples for construction and auditing.

---

# 24. Human–LLM–Code Allocation

The established project principle applies:

> **Humans define semantic space and decision boundaries; LLMs provide linguistic scale; code performs deterministic auditing.**

| Activity | Human | LLM | Code |
|---|:---:|:---:|:---:|
| Freeze ontology | ✓ | | |
| Define execution dimensions | ✓ | Assist | |
| Define semantic subtypes | ✓ | Assist | |
| Construct scenarios | ✓ | Assist | |
| Generate linguistic variants | | ✓ | |
| Generate boundary candidates | ✓ | ✓ | |
| Generate minimal pairs | ✓ | ✓ | |
| Generate hard negatives | ✓ | ✓ | |
| Schema validation | | | ✓ |
| Duplicate detection | | | ✓ |
| Shortcut audit | ✓ | Assist | ✓ |
| Coverage statistics | | | ✓ |
| Semantic validation | ✓ | Assist | |
| Difficult-case adjudication | ✓ | | |
| Final acceptance | ✓ | | ✓ |

LLM-generated examples remain candidates until validated.

---

# 25. Metadata and Lineage

Recommended schema:

```text
example_id
scenario_id
parent_id
lineage_id
execution_status
semantic_subtype
stage
resource_type
boundary_id
hard_negative_type
context
utterance
target_task
variation_type
source
validation_status
annotator_1_label
annotator_2_label
adjudicated_label
ambiguity_flag
split
```

Allowed ontology labels:

```text
NS
IP
C
```

Every variant must retain its parent lineage.

---

# 26. Leakage-Safe Split

Use:

```text
70% Train
15% Validation
15% Test
```

Split by semantic/lineage family, not by individual utterance.

Keep together:

- semantic scenarios;
- initial anchors;
- Stage-3A variants;
- boundary-anchor families;
- minimal-pair families;
- hard-negative families;
- Stage-3B descendants.

Both sides of a minimal pair must remain in the same split.

All variants of one hard-negative family must remain in the same split.

---

# 27. Diagnostic Challenge Set

Maintain a held-out challenge set focused on:

```text
NS ↔ IP
IP ↔ C
NS ↔ C
```

Include:

- future intention vs current execution;
- current execution vs near completion;
- near completion vs completion;
- non-execution vs completion;
- refusal vs completion;
- barrier statements;
- positive responses with NS;
- negative responses with NS;
- positive responses with IP;
- negative responses with IP;
- positive/negative reactions after completion;
- self-correction;
- ambiguous temporal wording;
- indirect execution evidence;
- multi-step tasks.

The challenge set should primarily support diagnostic evaluation.

---

# 28. Coverage Audit

Measure:

## Execution-state distribution

```text
NS
IP
C
```

## Semantic coverage

- scenarios per subtype;
- distinct execution conditions;
- underrepresented regions;
- overrepresented easy patterns.

## Task-domain coverage

```text
Medication
Hydration
Exercise
Physiotherapy
```

No task domain should correlate strongly with one execution state.

## Linguistic coverage

- lexical diversity;
- syntactic diversity;
- sentence length;
- explicit/implicit realization;
- temporal-expression diversity;
- progress/completion vocabulary;
- conversational naturalness.

## Boundary coverage

```text
NS ↔ IP
IP ↔ C
NS ↔ C
```

## Shortcut exposure

Audit association with:

- temporal words;
- tense;
- aspect;
- completion verbs;
- progress verbs;
- future modals;
- task domain;
- Response Category;
- Dialogue Purpose;
- Persuasion Barrier.

---

# 29. Quality-Control Rules

Reject a candidate if:

- execution state is incorrect;
- execution evidence is absent;
- another ontology determines the label;
- future intention is mistaken for execution;
- near completion is labeled Completed;
- completion is weakened into In Progress;
- reason for non-execution determines the label;
- scheduling/deadline information determines the label;
- task domain acts as a shortcut;
- wording is unnatural;
- example is a near-duplicate;
- lexical cue alone determines the state;
- target task is ambiguous and context does not resolve it;
- candidate changes its parent semantic scenario;
- lineage is lost.

---

# 30. Annotation Protocol

Use:

```text
Relevant Conversation Context
+
Current User Utterance
        ↓
Target Task Execution Evidence
        ↓
Execution State
        ↓
NS / IP / C
```

Decision hierarchy:

```text
1. Is there explicit evidence of completion?
       ↓ YES → Completed

2. Otherwise, is there evidence that execution has begun?
       ↓ YES → In Progress

3. Otherwise
       ↓
   Not Started
```

The primary question is:

> **What has actually happened with execution of the target task?**

Do not replace execution evidence with intention, motivation, reason, sentiment, or conversational function.

---

# 31. Difficult-Case Rules

## Rule 1 — Future Intention

```text
"I'll do it tonight."
→ NS
```

## Rule 2 — Current Execution

```text
"I'm doing it now."
→ IP
```

## Rule 3 — Near Completion

```text
"I'm almost finished."
→ IP
```

## Rule 4 — Explicit Completion

```text
"I already finished."
→ C
```

## Rule 5 — Reason for Non-Execution

```text
"I'm busy."
→ NS
```

## Rule 6 — Refusal

```text
"I'm not doing it."
→ NS
```

Refusal is not an execution state.

## Rule 7 — Positive Response

```text
"Sure, I'll do it later."
→ NS
```

Positive response does not imply execution.

## Rule 8 — Negative Response During Execution

```text
"I don't like it, but I'm doing it now."
→ IP
```

## Rule 9 — Negative Response After Completion

```text
"I hated it, but I finished it."
→ C
```

## Rule 10 — Completion Takes Precedence

If the user explicitly reports that the target task is finished, assign:

```text
Completed
```

for Execution Status, regardless of additional commentary.

---

# 32. Construction Order

```text
1. Verify / freeze Execution Status ontology
        ↓
2. Define execution semantic dimensions
        ↓
3. Define candidate semantic subtypes
        ↓
4. Build semantic scenario inventory
        ↓
5. Validate / freeze scenarios
        ↓
6. Create initial anchors
        ↓
7. Validate Stage-1 anchors
        ↓
8. Stage 3A — linguistic expansion
        ↓
9. Stage 3A validation
        ↓
10. Stage 2A — boundary anchors
        ↓
11. Stage 2B — minimal pairs
        ↓
12. Stage 2C — hard negatives
        ↓
13. Stage 2 validation
        ↓
14. Stage 3B — boundary expansion
        ↓
15. Stage 3B — minimal-pair expansion
        ↓
16. Stage 3B — hard-negative expansion
        ↓
17. Final semantic QC
        ↓
18. Deduplication
        ↓
19. Shortcut audit
        ↓
20. Cross-ontology leakage audit
        ↓
21. Group-based 70/15/15 split
        ↓
22. Diagnostic challenge set
        ↓
23. Final dataset freeze
```

---

# 33. Initial Quantitative Targets

These are planning targets only.

## Stage 1

```text
3 states
× ~15 scenarios/state
≈ 45 semantic scenarios

45 scenarios
× 3 initial anchors
≈ 135 Stage-1 candidates
```

## Stage 2A

```text
3 boundaries
× 6 boundary anchors
= 18 boundary anchors
```

## Stage 2B

```text
3 boundaries
× 6 minimal-pair families
= 18 minimal pairs
= 36 utterances
```

## Stage 2C

```text
3 boundaries
× 6 hard-negative families
= 18 hard-negative candidates
```

## Stage 3

No blind fixed expansion quota is imposed.

Expansion should depend on:

- semantic coverage;
- boundary difficulty;
- linguistic diversity;
- shortcut exposure;
- duplicate rate;
- classifier error analysis.

The final dataset size should be frozen only after validation and diagnostic analysis.

---

# 34. Stage Completion Criteria

## Stage 1 Complete When

- all three states have meaningful semantic coverage;
- semantic dimensions are reviewed;
- candidate subtypes are reviewed and frozen;
- scenarios are semantically distinct;
- task domains are distributed across states;
- initial anchors are generated and validated;
- future intention is not confused with execution;
- near completion is not confused with completion;
- reasons for non-execution do not become labels;
- cross-ontology shortcuts have been audited;
- lineage is frozen.

## Stage 2 Complete When

- NS↔IP is clearly represented;
- IP↔C is clearly represented;
- NS↔C is represented;
- minimal pairs preserve shared situations;
- hard negatives contain genuine distractors;
- difficult cases are adjudicated.

## Final Dataset Complete When

- semantic coverage is validated;
- linguistic diversity is sufficient;
- boundary coverage is sufficient;
- hard-negative robustness is validated;
- duplicates are removed;
- cross-ontology shortcuts are audited;
- leakage-safe splits are established;
- challenge set is frozen;
- final annotation is adjudicated.

---

# 35. Recommended Construction File Structure

```text
execution_status/
│
├── 00_ontology/
│   ├── execution_status_ontology.md
│   └── execution_status_differentiation.md
│
├── 01_semantic_coverage/
│   ├── semantic_dimensions/
│   ├── subtype_catalogue/
│   ├── scenario_inventory/
│   ├── stage_1_anchors/
│   ├── validation/
│   └── statistics/
│
├── 02_boundary/
│   ├── 2a_boundary_anchors/
│   ├── 2b_minimal_pairs/
│   ├── 2c_hard_negatives/
│   └── validation/
│
├── 03_linguistic_expansion/
│   ├── stage_3a/
│   ├── stage_3b_boundary/
│   ├── stage_3b_minimal_pairs/
│   └── stage_3b_hard_negatives/
│
├── 04_dataset/
│   ├── candidates/
│   ├── validated/
│   ├── train/
│   ├── validation/
│   └── test/
│
├── 05_quality/
│   ├── duplicate_audit/
│   ├── shortcut_audit/
│   ├── leakage_audit/
│   ├── coverage_audit/
│   └── challenge_set/
│
└── README.md
```

---

# 36. Final Construction Principle

The Execution Status dataset should follow:

```text
Frozen Execution Ontology
        ↓
Execution Semantic Space
        ↓
Distinct Execution Scenarios
        ↓
Natural-Language Realizations
        ↓
Linguistic Expansion
        ↓
Lifecycle Boundaries
        ↓
Minimal-Pair Contrast
        ↓
Hard-Negative Robustness
        ↓
Cross-Ontology Orthogonality
        ↓
Validation + Deduplication
        ↓
Leakage-Safe Dataset
        ↓
Diagnostic Evaluation
```

The central methodological principle is:

> **First represent the different ways execution state can occur, then teach the classifier where execution states differ, and finally expose it to diverse linguistic and distractor-rich realizations without changing the underlying execution state.**

The final classifier should learn one compact semantic distinction:

```text
Has execution started?
        │
        ├── NO → Not Started
        │
        └── YES
              │
              ├── FINISHED → Completed
              │
              └── NOT FINISHED → In Progress
```

Everything outside this execution lifecycle should remain represented by the appropriate ontology or downstream component.
