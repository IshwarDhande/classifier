# Stage 1 — Execution Status Dataset Construction Plan

**Status:** Construction Plan  
**Target:** Execution Status Dataset  
**Ontology:** Execution Status Ontology V1.0  
**Stage:** Stage 1 — Semantic Coverage

---

# 1. Objective

Stage 1 establishes the **semantic coverage** of the Execution Status dataset.

The objective is to expose the classifier to a broad range of execution situations that can produce each Execution Status, rather than allowing categories to collapse around a small set of lexical or temporal patterns.

The classifier should learn:

> **What is the current execution state of the target task?**

and not:

- isolated temporal keywords;
- future intention alone;
- motivation;
- persuasion barrier;
- dialogue purpose;
- response sentiment;
- deadline status;
- scheduling status;
- task-manager state such as overdue or missed;
- superficial sentence structure.

The three Execution Status values are:

```text
Not Started
In Progress
Completed
```

The execution lifecycle is:

```text
Not Started → In Progress → Completed
```

Stage 1 is concerned with covering the **execution-semantic space** represented by these three states. Decision-boundary construction is deferred to Stage 2.

---

# 2. Construction Principle

Stage 1 reuses the established semantic-coverage methodology used for the Response Category dataset, but adapts it to the fundamentally different semantics of Execution Status.

Execution Status is a **task-execution lifecycle classification problem**, not an ordinal behavioral-appraisal problem.

Therefore, Stage 1 must organize examples around:

- whether execution has begun;
- what portion of the task has been executed;
- whether execution remains unfinished;
- whether execution has finished;
- how these states are naturally expressed in conversation.

A **semantic subtype layer** is introduced between the frozen Execution Status labels and individual scenarios. This provides an intermediate level of semantic organization without turning construction metadata into additional classifier labels.

The construction hierarchy is:

```text
Execution Status
        ↓
Semantic Subtype
        ↓
Semantic Scenario
        ↓
Natural-Language Realization
```

Semantic subtypes are **construction-level semantic regions**, not classifier labels. Their number is not fixed in advance and does not need to be equal across categories.

The classifier retains only:

```text
Not Started | In Progress | Completed
```

---

# 3. Stage 1 Construction Target

The initial planning target is:

```text
3 Execution States
        ↓
~4–6 Semantic Subtypes / State
        ↓
~12–20 Semantic Scenarios / State
        ↓
≈36–60 Semantic Scenarios Overall
```

These are **planning ranges, not ontology requirements**.

The exact number of semantic subtypes and scenarios must be determined after semantic analysis.

Some execution states may require more semantic regions than others, and some subtypes may require more scenarios than others.

The key requirement is **semantic completeness and diversity**, not numerical symmetry.

---

# 4. Stage 1 Construction Pipeline

```text
Execution Status Ontology
        ↓
Execution Semantic Coverage Matrix
        ↓
Semantic Subtype Catalogue
        ↓
Scenario Inventory
        ↓
Scenario Validation
        ↓
Initial Semantic Anchors
        ↓
Anchor Validation
        ↓
Stage-1 Semantic Coverage Dataset
        ↓
Stage 3A — Linguistic Expansion
```

Stage 1 therefore has three principal construction resources:

1. **Execution Semantic Coverage Matrix**
2. **Semantic Scenario Inventory**
3. **Initial Semantic Anchor Realizations**

The coverage matrix is an intermediate planning artifact used to ensure that scenario construction does not overrepresent easy or stereotypical realizations.

---

# 5. Execution Semantic Coverage Matrix

Before generating scenarios, define the execution regions that need representation within each state.

The matrix should organize coverage around the semantic properties established by the Execution Status ontology.

## 5.1 Semantic Subtype Layer

Semantic subtypes provide a structured middle layer between the three frozen Execution Status labels and individual scenarios.

A subtype should represent a **meaningfully distinct execution situation** within a state.

For example:

```text
In Progress
│
├── Direct Ongoing Execution
├── Partial Execution
├── Multi-Step Execution
└── Near Completion
```

The example is illustrative. The final subtype catalogue must be derived from the Execution Status semantic space and reviewed before scenario generation.

### Subtype rules

1. **No fixed subtype count**

   Do not require exactly four subtypes, or any other predetermined number, for every state.

2. **Variable number is allowed**

   A state may contain fewer or more subtypes depending on its execution-semantic space.

3. **Subtypes must be substantively distinct**

   A subtype should represent a meaningful execution situation, not a superficial wording difference.

4. **Subtypes are not classifier labels**

   The classifier continues to predict only:

   ```text
   Not Started | In Progress | Completed
   ```

5. **Subtypes control coverage**

   Their purpose is to ensure that scenario generation covers the state systematically rather than concentrating on a few stereotypical expressions.

6. **Subtypes must remain within the frozen state**

   A subtype must not introduce a new execution state that belongs to a neighboring Execution Status.

---

## 5.2 Subtype Derivation Process

Subtype construction should follow:

```text
Frozen Execution Status
        ↓
Execution Dimensions
        ↓
Candidate Semantic Regions
        ↓
Candidate Subtypes
        ↓
Human Semantic Review
        ↓
Frozen Stage-1 Subtype Catalogue
        ↓
Scenario Construction
```

The subtype catalogue should be frozen **before** large-scale scenario generation.

The catalogue is a Stage-1 construction artifact, not an extension of the ontology.

---

## 5.3 Core Execution Dimensions

Relevant construction dimensions include:

- whether execution has begun;
- current execution activity;
- amount of task completed;
- remaining work;
- partial execution;
- multi-step execution;
- temporary interruption;
- near completion;
- explicit completion;
- retrospective completion;
- indirect completion evidence;
- future/deferred action;
- conditional future action;
- current non-execution;
- refusal without execution;
- inability or unavailability without execution;
- forgetting without execution;
- reason-linked non-execution.

These dimensions are **construction dimensions**, not new labels.

---

# 6. State-Oriented Coverage

## 6.1 Not Started

Coverage should include execution situations involving:

- explicit non-execution;
- current non-execution;
- future action;
- deferred action;
- planned but uninitiated action;
- conditional future action;
- postponed action;
- inability or unavailability without execution;
- forgetting without execution;
- low motivation without execution;
- refusal without execution;
- uncertainty about starting;
- reason-linked non-execution.

Core distinction:

```text
Execution has NOT begun
→ Not Started
```

The presence of a future intention does not constitute execution.

For example:

```text
"I'll take it tonight."
→ Not Started
```

---

## 6.2 In Progress

Coverage should include execution situations involving:

- direct ongoing execution;
- current activity;
- partial execution;
- halfway execution;
- remaining work;
- multi-step execution;
- temporary interruption;
- active physical execution;
- execution of one component of a larger task;
- near completion;
- indirect evidence that execution is underway.

Core distinction:

```text
Execution HAS begun
AND
execution is NOT finished
→ In Progress
```

For example:

```text
"I'm taking it now."
→ In Progress
```

and:

```text
"I've done half of the exercises."
→ In Progress
```

Near completion must remain In Progress until execution has actually finished.

---

## 6.3 Completed

Coverage should include execution situations involving:

- direct completion;
- retrospective completion;
- recent completion;
- earlier completion;
- indirect completion evidence;
- multi-step completion;
- completion followed by commentary;
- completion followed by a result or consequence;
- conversational completion;
- completion expressed without the canonical word "done".

Core distinction:

```text
Execution HAS begun
AND
execution HAS finished
→ Completed
```

For example:

```text
"I already took it."
→ Completed
```

Completion must be supported by actual execution, not merely intention to complete.

---

# 7. Decision Hierarchy for Scenario Construction

Execution Status classification should prioritize actual execution evidence over surface wording.

Stage 1 scenario construction and validation should therefore follow this hierarchy:

```text
Execution Initiation
        ↓
Execution Progress
        ↓
Execution Completion
        ↓
Conversational / Pragmatic Evidence
        ↓
Surface Wording
```

The primary decision question is:

```text
Has execution started?
        |
        |-- NO → Not Started
        |
        |-- YES
              |
              |-- Finished → Completed
              |
              |-- Not Finished → In Progress
```

This hierarchy is especially important when designing scenarios containing:

- future intentions;
- temporal expressions;
- reasons for non-execution;
- refusal;
- forgetting;
- partial execution;
- near-completion statements;
- completion words;
- multi-step tasks;
- self-correction;
- indirect execution evidence.

The intended label must be justified by the **actual execution state**, not by a lexical cue.

---

# 8. Scenario Inventory

## 8.1 Construction Target

The initial inventory should aim for approximately:

```text
~12–20 scenarios / state
≈36–60 scenarios overall
```

A working target near 15 scenarios/state is useful for planning, but it is not mandatory.

Scenario allocation should be performed **within semantic subtypes**, based on how much distinct execution coverage each subtype requires.

For example:

```text
State
   ↓
Subtype A → 4 scenarios
Subtype B → 5 scenarios
Subtype C → 3 scenarios
Subtype D → 4 scenarios
≈16 scenarios
```

Another state may legitimately have a different subtype and scenario distribution.

The inventory must therefore be driven by execution-semantic coverage rather than filling an arbitrary numerical quota.

---

## 8.2 Scenario Construction Rule

Each scenario must represent a **distinct underlying execution situation**.

Five scenarios should not simply be five paraphrases of one situation.

A scenario should specify:

- the target task;
- the current execution state;
- the semantic subtype;
- the execution condition;
- relevant conversational context;
- relevant execution dimension;
- relevant boundary risk.

Conceptually:

```text
Execution Situation
        ↓
Expected Execution Status
        ↓
Natural User Response
```

Only after the scenarios are validated should large-scale linguistic realizations be constructed.

---

# 9. Scenario Design Principles

## 9.1 Distinct Semantic Situations

Scenarios within a state must represent different execution conditions.

Do not create several scenarios that differ only by wording.

For example, these are not sufficiently distinct scenarios merely because they use different words:

```text
"I haven't done it."
"I didn't do it."
"I haven't started."
```

If they all represent the same underlying execution situation, they should not be counted as separate semantic scenarios.

---

## 9.2 Execution Diversity

Vary the underlying execution conditions while preserving the state.

Examples include:

- current activity;
- amount completed;
- remaining work;
- number of completed steps;
- temporary interruption;
- near completion;
- future/deferred action;
- conditional action;
- inability;
- forgetting;
- refusal;
- retrospective reporting;
- indirect evidence;
- multi-step execution.

---

## 9.3 Conversational Position

Scenarios should occur at different points in an interaction:

- immediately after a reminder;
- after the user was asked whether they have started;
- after an explanation;
- after a clarification;
- after the user raises a concern;
- after the agent repeats the recommendation;
- after a previous intention;
- after a previous partial execution statement;
- after the user reports a result.

The same Execution Status should not always occur in the same conversational position.

---

## 9.4 Context Dependence

Some Execution Status decisions require conversational context.

Scenarios should therefore include context-dependent cases where appropriate, especially for:

- pronoun/reference expressions;
- indirect completion;
- multi-step tasks;
- self-correction;
- ambiguous temporal references;
- continuation of an earlier task discussion;
- statements where the target task is understood from dialogue history.

Context should be relevant rather than artificially lengthened.

---

# 10. Stage-1 Scenario Coverage by State

## 10.1 Not Started

Scenario inventory should represent:

- explicit non-execution;
- current non-execution;
- future intention;
- deferred action;
- conditional future action;
- planned but uninitiated action;
- postponed action;
- inability/unavailability;
- forgetting;
- low motivation;
- refusal;
- uncertainty about starting.

The scenario must establish that **execution has not begun**.

---

## 10.2 In Progress

Scenario inventory should represent:

- direct ongoing execution;
- partial execution;
- halfway execution;
- remaining work;
- multi-step execution;
- temporary interruption;
- active physical execution;
- one component of a larger task;
- near completion;
- indirect evidence of ongoing execution.

The scenario must establish that **execution has begun but has not finished**.

---

## 10.3 Completed

Scenario inventory should represent:

- direct completion;
- retrospective completion;
- recent completion;
- earlier completion;
- indirect completion;
- multi-step completion;
- completion plus commentary;
- completion plus consequence/result;
- conversational completion;
- completion without the canonical word "done".

The scenario must establish that **execution has finished**.

---

# 11. Stage-1 Scenario Metadata

Each scenario should have stable metadata.

Recommended schema:

```text
scenario_id
execution_status
semantic_subtype
scenario_description
execution_condition
target_task
execution_dimension
difficulty_level
explicitness
conversational_position
boundary_risk
notes
validation_status
```

`execution_dimension` records the construction/coverage dimension represented by the scenario. It is not a classifier label.

---

# 12. Stage-1 Anchor Construction

After the semantic scenarios are finalized, construct initial natural-language realizations.

Each scenario should receive:

1. **Direct realization**
2. **Indirect realization**
3. **Natural conversational realization**

Planning target:

```text
≈45 scenarios
× 3 anchors
≈135 Stage-1 candidate examples
```

The exact number depends on the final validated scenario inventory.

These remain candidate examples until validation.

---

# 13. Anchor Type Definitions

## 13.1 Direct

The execution state is clearly expressed.

Example:

```text
In Progress:
"I'm taking it now."
```

## 13.2 Indirect

The execution state is conveyed through contextual execution evidence rather than a canonical status word.

Example:

```text
In Progress:
"I've done the first few exercises; I still have two left."
```

## 13.3 Natural Conversational

The response resembles ordinary spontaneous conversation.

Example:

```text
Completed:
"Yeah, I got that done earlier."
```

These examples are illustrative construction forms only. Final examples must be generated from validated scenarios.

---

# 14. Anchor Construction Rules

Each anchor must:

- realize the intended execution scenario;
- preserve the target Execution Status;
- remain natural;
- avoid unnecessary status keywords;
- avoid temporal-word shortcuts;
- avoid introducing another primary semantic state;
- remain distinguishable from neighboring execution states;
- reflect actual execution rather than intention;
- preserve the target task;
- avoid relying on task-specific vocabulary to signal the label.

Anchors should not be intentionally adversarial at this stage.

Boundary engineering is handled in Stage 2.

---

# 15. What Stage 1 Should NOT Do

Stage 1 should not attempt to exhaustively solve execution-state decision boundaries.

Do not deliberately construct:

- minimal pairs;
- adversarial hard negatives;
- dense boundary clusters;
- misleading competing cues;
- extensive lexical distractors.

Those belong primarily to Stage 2.

Stage 1 should answer:

> **What execution situations does each Execution Status need to cover?**

---

# 16. Human–LLM–Code Allocation

The established project principle applies:

> **Humans define semantic space; LLMs provide linguistic scale; code performs deterministic auditing.**

| Activity | Human | LLM | Code |
|---|:---:|:---:|:---:|
| Freeze execution-state semantics | ✓ | | |
| Define execution coverage dimensions | ✓ | Assist | |
| Create subtype catalogue | ✓ | Assist | |
| Create scenario inventory | ✓ | Assist | |
| Generate anchor candidates | | ✓ | |
| Check schema | | | ✓ |
| Check state balance | | | ✓ |
| Detect duplicates | | | ✓ |
| Audit lexical shortcuts | ✓ | Assist | ✓ |
| Review ambiguous scenarios | ✓ | Assist | |
| Final semantic adjudication | ✓ | | |

LLM-generated scenarios and anchors remain **candidate data** until validated.

---

# 17. Validation Protocol

Every Stage-1 candidate should be evaluated as:

```text
Scenario
   +
Conversation Context
   +
Candidate Response
        ↓
Execution Interpretation
        ↓
Execution Status
```

Validation should answer:

1. Has execution actually begun?
2. If execution has begun, is it finished?
3. Does the candidate realize the intended scenario?
4. Is the execution state supported by execution evidence rather than isolated wording?
5. Could a neighboring state reasonably be assigned?
6. Does the candidate accidentally encode another project label?
7. Is the language natural?
8. Is the target task identifiable?
9. If context is provided, does the candidate remain consistent with that context?
10. Does the candidate distinguish execution from intention, planning, or scheduling?

---

# 18. Stage-1 Quality-Control Checklist

## Semantic QC

- [ ] Correct Execution Status
- [ ] Scenario is semantically distinct
- [ ] Execution condition is clear
- [ ] Exactly one primary Execution Status
- [ ] No accidental ontology expansion
- [ ] Scenario represents an execution situation, not merely a sentence pattern

## Decision-Hierarchy QC

- [ ] Execution initiation considered
- [ ] Execution progress considered
- [ ] Completion considered
- [ ] Intention does not override execution evidence
- [ ] Planning/scheduling does not override execution evidence
- [ ] Surface wording is not the primary basis of the label

## Orthogonality QC

- [ ] Not determined by Dialogue Purpose
- [ ] Not determined by Persuasion Barrier
- [ ] Not determined by Response Category
- [ ] Not determined by motivation alone
- [ ] Not determined by sentiment
- [ ] Not determined by deadline status
- [ ] Not determined by task-manager state

## Linguistic QC

- [ ] Natural wording
- [ ] Appropriate conversational form
- [ ] No unnecessary template repetition
- [ ] No obvious temporal/status keyword shortcut
- [ ] Direct/indirect/natural realization is appropriate

## Coverage QC

- [ ] All three states represented
- [ ] Approximately balanced scenario count
- [ ] Execution dimensions sufficiently covered
- [ ] Explicit/implicit coverage balanced at corpus level
- [ ] Difficulty spectrum represented
- [ ] Different conversational positions represented
- [ ] Context-dependent cases represented where needed
- [ ] All four target task domains represented

---

# 19. Shortcut Audit

Before Stage 1 is frozen, perform a targeted shortcut audit.

Test whether state membership can be predicted using:

```text
"already"   → Completed
"now"       → In Progress
"later"     → Not Started
"finished"  → Completed
"starting"  → In Progress
"almost"    → In Progress
"will"      → Not Started
"done"      → Completed
```

These relationships must not become deterministic.

Additional shortcut dimensions:

- punctuation;
- sentence length;
- temporal expressions;
- completion words;
- progress verbs;
- future-intention verbs;
- modal verbs;
- task names;
- tense/aspect alone;
- discourse position.

The same surface forms should occur across states whenever naturally possible.

---

# 20. Balance and Coverage Audit

After candidate generation, calculate:

## Execution Status distribution

```text
Not Started
In Progress
Completed
```

## Semantic subtype distribution

Verify:

- subtype count by state;
- scenarios per subtype;
- whether each subtype has sufficient distinct coverage;
- whether any subtype is overrepresented merely because it is easier to generate.

The distribution does **not** need to be numerically equal.

## Scenario distribution

```text
~12–20 scenarios / state
≈36–60 scenarios overall
```

A target near 15/state may be used for planning, but semantic review takes precedence.

## Anchor distribution

```text
Direct
Indirect
Natural
```

## Execution dimensions

Verify that important dimensions such as:

- initiation;
- ongoing execution;
- partial execution;
- remaining work;
- multi-step execution;
- near completion;
- completion;
- future/deferred action;
- refusal;
- forgetting;
- inability;
- indirect execution evidence

are represented where semantically appropriate.

## Explicitness

```text
Explicit
Implicit
```

## Difficulty

```text
Clear
Moderate
Difficult
```

## Conversational position

Verify that no state is systematically associated with one interaction position.

---

# 21. Deduplication

Stage 1 should remove:

- exact duplicates;
- trivial lexical duplicates;
- near-identical scenarios;
- scenarios differing only by superficial wording;
- anchors that are effectively the same realization.

Important distinction:

```text
Semantic similarity
≠
Duplicate
```

Two examples can represent the same state while still being useful if they represent genuinely different execution situations.

---

# 22. Leakage Prevention

Stage 1 lineage must be preserved before any future split.

The basic grouping unit should be:

```text
scenario_id
```

All three initial anchors derived from the same scenario should remain in the same future split.

Later Stage-3A variants derived from those anchors must also remain with the same scenario lineage.

Therefore:

```text
Scenario
   ├── Anchor A
   ├── Anchor B
   ├── Anchor C
   └── Stage-3A descendants
```

must be treated as one leakage group.

---

# 23. Stage-1 Completion Criteria

Stage 1 is complete only when:

1. The three execution states have validated semantic coverage.
2. The execution semantic coverage matrix is reviewed.
3. The candidate semantic subtype catalogue has been reviewed and frozen.
4. Each subtype represents a meaningful execution region within its parent state.
5. The scenario inventory is sufficiently diverse.
6. Approximately 12–20 scenarios/state have been constructed, unless semantic review justifies an adjustment.
7. Each validated scenario has three initial candidate anchors.
8. State balance has been audited.
9. Subtype coverage and scenario allocation have been audited.
10. Execution-dimension coverage has been audited.
11. Explicit/implicit coverage has been audited.
12. Difficulty coverage has been audited.
13. Orthogonality with other project labels has been checked.
14. Decision-hierarchy compliance has been checked.
15. Shortcut audits have been performed.
16. Duplicate and near-duplicate scenarios have been removed.
17. Human validation/adjudication is complete.
18. Scenario lineage is frozen.

---

# 24. Stage-1 Output

The expected Stage-1 construction output is:

```text
01_semantic_coverage/
│
├── execution_semantic_coverage/
│   ├── coverage_matrix
│   └── coverage_review
│
├── scenario_inventory
│   ├── scenario_inventory
│   └── scenario_definitions
│
├── stage_1_anchors
│
├── validation
│
└── statistics
```

Conceptually:

```text
3 Execution States
        ↓
Candidate / Frozen Semantic Subtype Catalogue
        ↓
Execution Semantic Coverage Matrix
        ↓
≈36–60 Distinct Execution Scenarios
        ↓
≈108–180 Initial Anchor Candidates
        ↓
QC + Human Validation
        ↓
Validated Stage-1 Semantic Resource
```

The validated Stage-1 resource then becomes the input to:

```text
Stage 3A
Stage-1 Linguistic Expansion
```

---

# 25. Final Principle

Stage 1 should answer one question:

> **Have we adequately represented the execution-semantic space of each Execution Status before attempting to engineer its decision boundaries?**

The construction sequence is therefore:

```text
Execution Status
        ↓
Execution Semantic Space
        ↓
Semantic Subtype Catalogue
        ↓
Coverage Matrix
        ↓
Distinct Execution Scenarios
        ↓
Direct / Indirect / Natural Realizations
        ↓
Semantic Validation
        ↓
Stage-1 Dataset
        ↓
Stage 3A Linguistic Expansion
```

The central rule is:

> **Stage 1 establishes what each Execution Status means across diverse execution situations; it does not yet attempt to solve the boundary between neighboring states.**

The three frozen Execution Status values remain the only classifier labels throughout this process. Semantic subtypes, execution dimensions, and scenario metadata are construction aids, not ontology expansion.

The central methodological rule is:

> **Use semantic subtypes to organize the execution space, but let execution semantics determine how many subtypes and scenarios are needed. Do not impose an arbitrary fixed subtype count.**
