# Stage 1 — Response Category Dataset Construction Plan

**Status:** Construction Plan  
**Target:** Response Category Dataset  
**Ontology:** Response Category Ontology V1.0  
**Stage:** Stage 1 — Semantic Coverage

---

# 1. Objective

Stage 1 establishes the **semantic coverage** of the Response Category dataset.

The objective is to expose the classifier to a broad range of behavioral situations that can produce each Response Category, rather than allowing categories to collapse around a small set of lexical or stylistic patterns.

The classifier should learn:

> **How is the user behaviorally reacting to the intervention?**

and not:

- isolated keywords;
- sentiment polarity;
- emotion;
- dialogue purpose;
- persuasion barrier;
- execution status;
- task completion;
- topic;
- superficial sentence structure.

The five Response Categories are:

```text
VP — Very Positive
P  — Positive
I  — Indifferent
N  — Negative
VN — Very Negative
```

The ontology is ordinal:

```text
VN < N < I < P < VP
```

Stage 1 is concerned with covering the **behavioral semantic space** represented by these five categories. Decision-boundary construction is deferred to Stage 2.

---

# 2. Construction Principle

Stage 1 reuses the established semantic-coverage methodology from the Dialogue Purpose dataset, but does **not** blindly copy its ontology structure.

Response Category is an **ordinal behavioral-appraisal classification problem**. Therefore, Stage 1 must organize examples around behavioral meaning and response intensity.

A **semantic subtype layer** is introduced between the frozen Response Category labels and individual scenarios. This provides an intermediate level of semantic organization without turning construction metadata into additional classifier labels.

The construction hierarchy is:

```text
Response Category
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
VP | P | I | N | VN
```

---

# 3. Stage 1 Construction Target

The initial planning target is:

```text
5 Response Categories
        ↓
~3–6 Semantic Subtypes / Category
        ↓
~15–25 Semantic Scenarios / Category
        ↓
≈75–125 Semantic Scenarios Overall
```

These are **planning ranges, not ontology requirements**.

The exact number of semantic subtypes and scenarios must be determined after semantic analysis. Some categories may require more semantic regions than others, and some subtypes may require more scenarios than others.

The key requirement is **semantic completeness and diversity**, not numerical symmetry.

---

# 4. Stage 1 Construction Pipeline

```text
Response Category Ontology
        ↓
Behavioral Semantic Coverage Matrix
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

1. **Behavioral Semantic Coverage Matrix**
2. **Semantic Scenario Inventory**
3. **Initial Semantic Anchor Realizations**

The coverage matrix is an intermediate planning artifact used to ensure that scenario construction does not overrepresent easy or stereotypical realizations.

---

# 5. Behavioral Semantic Coverage Matrix

Before generating scenarios, define the behavioral regions that need representation within each category.

The matrix should organize coverage around the semantic properties established by the Response Category ontology.

## 5.1 Semantic Subtype Layer

Semantic subtypes are introduced to provide a structured middle layer between the five frozen Response Categories and individual scenarios.

A subtype should represent a **meaningfully distinct behavioral region** within a category.

For example:

```text
P — Positive
│
├── Ordinary Acceptance
├── Cooperative Commitment
├── Qualified Acceptance
└── Delayed Genuine Acceptance
```

The example is illustrative. The final subtype catalogue must be derived from the Response Category semantic space and reviewed before scenario generation.

### Subtype rules

1. **No fixed subtype count**

   Do not require exactly four subtypes, or any other predetermined number, for every category.

2. **Variable number is allowed**

   A category may contain fewer or more subtypes depending on the structure of its behavioral semantic space.

3. **Subtypes must be substantively distinct**

   A subtype should represent a meaningful behavioral region, not a superficial wording difference.

4. **Subtypes are not classifier labels**

   The classifier continues to predict only:

   ```text
   VP | P | I | N | VN
   ```

5. **Subtypes control coverage**

   Their purpose is to ensure that scenario generation covers the category systematically rather than concentrating on a few stereotypical expressions.

6. **Subtypes must remain within the frozen category**

   A subtype must not introduce a new behavioral state that belongs to a neighboring Response Category.

## 5.2 Subtype Derivation Process

Subtype construction should follow:

```text
Frozen Response Category
        ↓
Behavioral Dimensions
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

## 5.3 Core Behavioral Dimensions

Relevant dimensions include:

## 5.1 Core Behavioral Dimensions

Relevant dimensions include:

- strength of acceptance;
- strength of enthusiasm;
- appreciation;
- willingness to cooperate;
- behavioral commitment;
- uncertainty;
- non-commitment;
- hesitation;
- reluctance;
- disagreement;
- behavioral resistance;
- reactance;
- hostility;
- active disengagement;
- interaction termination;
- proactive engagement;
- conditional acceptance;
- conditional resistance;
- delayed acceptance;
- delayed action caused by resistance.

These dimensions are **construction dimensions**, not new labels.

## 5.4 Category-Oriented Coverage

### VP — Very Positive

Coverage should include behavioral situations involving:

- strong acceptance;
- enthusiasm;
- explicit appreciation;
- high engagement;
- proactive participation;
- voluntary cooperation;
- strong endorsement;
- positive engagement after clarification;
- positive response after personalization;
- active interest in continuing.

Core distinction:

```text
Ordinary acceptance → P
Strong enthusiasm / appreciation / high engagement → VP
```

### P — Positive

Coverage should include:

- ordinary acceptance;
- cooperative agreement;
- willingness to cooperate;
- behavioral commitment;
- straightforward compliance;
- polite acceptance;
- mild appreciation;
- implicit cooperation;
- delayed but genuine acceptance;
- qualified acceptance without meaningful resistance.

Core distinction:

```text
Acceptance + cooperation without strong enthusiasm → P
```

### I — Indifferent

Coverage should include:

- neutral acknowledgement;
- uncertainty;
- non-commitment;
- delayed decision;
- passive engagement;
- insufficient acceptance evidence;
- insufficient resistance evidence;
- clarification without behavioral acceptance;
- neutral response to persuasion;
- context-dependent neutrality.

Core distinction:

```text
No sufficiently strong evidence of acceptance
AND
No sufficiently strong evidence of resistance
→ I
```

I must not become a generic "weak positive" or "weak negative" class.

### N — Negative

Coverage should include:

- reluctance;
- mild refusal;
- disagreement;
- behavioral resistance;
- reduced willingness;
- mild reactance;
- conditional resistance;
- passive resistance;
- delayed action caused by resistance;
- recoverable resistance.

Core distinction:

```text
Behavioral resistance
without
strong rejection / hostility / active disengagement
→ N
```

### VN — Very Negative

Coverage should include:

- strong rejection;
- explicit opposition;
- strong reactance;
- hostility;
- active disengagement;
- interaction termination;
- rejection of future assistance;
- strong refusal;
- hostile resistance;
- breakdown of cooperation.

Core distinction:

```text
Strong rejection / hostility / high reactance / active disengagement
→ VN
```

VN should not be created simply by adding stronger negative vocabulary to an N scenario. The underlying behavioral situation must justify the stronger category.

---

# 6. Decision Hierarchy for Scenario Construction

The Response Category source material establishes that classification should prioritize behavioral evidence over surface form.

Stage 1 scenario construction and validation should therefore follow this hierarchy:

```text
Behavioral Commitment
        ↓
Behavioral Resistance
        ↓
Communicative Intention
        ↓
Pragmatic Meaning
        ↓
Surface Wording
```

This hierarchy is especially important when designing scenarios containing:

- gratitude;
- agreement words;
- commitment verbs;
- negative wording;
- politeness;
- uncertainty;
- emotional language;
- sarcasm;
- mixed acceptance and resistance.

The intended label must be justified by the **dominant behavioral response toward the intervention**, not by a lexical cue.

---

# 7. Scenario Inventory

## 7.1 Construction Target

The initial inventory should aim for approximately:

```text
~15–25 scenarios / category
≈75–125 scenarios overall
```

A working target near 20 scenarios/category is useful for planning, but it is not mandatory.

Scenario allocation should be performed **within semantic subtypes**, based on how much distinct behavioral coverage each subtype requires.

For example:

```text
Category
   ↓
Subtype A → 4 scenarios
Subtype B → 6 scenarios
Subtype C → 5 scenarios
Subtype D → 4 scenarios
≈19 scenarios
```

Another category may legitimately have a different subtype and scenario distribution.

The inventory must therefore be driven by behavioral coverage rather than filling an arbitrary numerical quota.

## 7.2 Scenario Construction Rule

Each scenario must represent a **distinct underlying behavioral situation**.

Five scenarios should not simply be five paraphrases of one situation.

A scenario should specify:

- what intervention occurred;
- what behavioral state the user is in;
- why the response belongs to the target category;
- which semantic subtype it belongs to;
- relevant conversational position;
- relevant semantic coverage dimension.

Conceptually:

```text
Behavioral Situation
        ↓
Expected Response Category
        ↓
Natural User Response
```

Only after the scenarios are validated should linguistic realizations be constructed.

---

# 8. Scenario Design Principles

## 8.1 Distinct Semantic Situations

Scenarios within a category must represent different behavioral conditions.

Do not create several scenarios that differ only in wording.

## 8.2 Behavioral Diversity

Vary the underlying causes and manifestations of the response while preserving the category.

Examples include:

- strength;
- commitment;
- enthusiasm;
- uncertainty;
- resistance;
- appreciation;
- engagement;
- reactance;
- conditionality;
- delayed response;
- response after clarification;
- response after personalization;
- response after repeated persuasion.

## 8.3 Conversational Position

Scenarios should occur at different points in an interaction:

- immediately after a recommendation;
- after an explanation;
- after a clarification;
- after the user raises a concern;
- after the agent modifies the recommendation;
- after previous acceptance;
- after previous resistance;
- after repeated persuasion;
- after a reminder;
- after the agent acknowledges the user's concern.

The same Response Category should not always occur in the same conversational position.

## 8.4 Context Dependence

Some Response Category decisions require dialogue history.

Scenarios should therefore include context-dependent cases where appropriate, especially for:

- ambiguous agreement;
- conventional politeness;
- sarcasm;
- delayed compliance;
- mixed acceptance/resistance;
- repeated intervention;
- prior commitments or refusals.

Context should be relevant rather than artificially lengthened.

---

# 9. Stage-1 Scenario Coverage by Category

## 9.1 VP — Very Positive

Scenario inventory should represent:

- enthusiastic acceptance;
- strong appreciation;
- proactive engagement;
- willingness combined with enthusiasm;
- voluntary continuation;
- strong endorsement;
- appreciation after clarification;
- positive reaction after personalization;
- active interest;
- implicit but clearly enthusiastic cooperation.

The scenario must contain behavioral evidence stronger than ordinary acceptance.

## 9.2 P — Positive

Scenario inventory should represent:

- ordinary acceptance;
- cooperative agreement;
- willingness to follow;
- straightforward cooperation;
- polite acceptance;
- mild appreciation;
- acceptance without strong enthusiasm;
- implicit cooperation;
- acceptance after clarification;
- qualified acceptance.

The scenario should demonstrate positive/cooperative reaction without requiring VP-level enthusiasm.

## 9.3 I — Indifferent

Scenario inventory should represent:

- neutral acknowledgement;
- non-committal response;
- uncertainty;
- delayed decision;
- passive engagement;
- insufficient evidence of acceptance;
- insufficient evidence of resistance;
- clarification without behavioral acceptance;
- neutral response to persuasion;
- context-dependent neutrality.

The defining condition is insufficient behavioral evidence for either acceptance or resistance.

## 9.4 N — Negative

Scenario inventory should represent:

- reluctance;
- mild refusal;
- disagreement;
- behavioral resistance;
- conditional resistance;
- reduced willingness;
- mild reactance;
- delayed action caused by resistance;
- passive resistance;
- recoverable resistance.

The interaction should remain potentially recoverable and should not reach VN-level rejection or disengagement.

## 9.5 VN — Very Negative

Scenario inventory should represent:

- strong rejection;
- explicit opposition;
- strong reactance;
- hostility;
- active disengagement;
- interaction termination;
- rejection of future assistance;
- strong refusal;
- hostile resistance;
- breakdown of cooperation.

The underlying behavioral situation must justify VN; stronger negative vocabulary alone is insufficient.

---

# 10. Stage-1 Scenario Metadata

Each scenario should have stable metadata.

Recommended schema:

```text
scenario_id
response_category
semantic_subtype
scenario_description
behavioral_condition
intervention_context
behavioral_dimension
difficulty_level
explicitness
conversational_position
notes
validation_status
```

`behavioral_dimension` records the construction/coverage dimension represented by the scenario. It is not a classifier label.

---

# 11. Stage-1 Anchor Construction

After the semantic scenarios are finalized, construct initial natural-language realizations.

Each scenario should receive:

1. **Direct realization**
2. **Indirect realization**
3. **Natural conversational realization**

Planning target:

```text
≈100 scenarios
× 3 anchors
≈300 Stage-1 candidate examples
```

These remain candidate examples until validation.

---

# 12. Anchor Type Definitions

## 12.1 Direct

The intended behavioral response is clearly expressed.

Example:

```text
P:
"Yes, I'll follow that."
```

## 12.2 Indirect

The behavioral response is conveyed pragmatically without relying on a category label.

Example:

```text
P:
"That sounds workable for me."
```

## 12.3 Natural Conversational

The response resembles ordinary spontaneous conversation.

Example:

```text
P:
"Yeah, I can give that a shot."
```

These examples are illustrative construction forms only. Final examples must be generated from validated scenarios.

---

# 13. Anchor Construction Rules

Each anchor must:

- realize the intended scenario;
- preserve the target Response Category;
- remain natural;
- avoid unnecessary category keywords;
- avoid sentiment-only shortcuts;
- avoid encoding execution status unless the scenario requires it;
- avoid introducing another primary behavioral response;
- remain distinguishable from neighboring categories;
- reflect the intended behavioral condition rather than merely its wording.

Anchors should not be intentionally adversarial at this stage.

Boundary engineering is handled in Stage 2.

---

# 14. What Stage 1 Should NOT Do

Stage 1 should not attempt to exhaustively solve decision-boundary problems.

Do not deliberately construct:

- minimal pairs;
- adversarial hard negatives;
- dense boundary clusters;
- misleading competing cues;
- extensive lexical distractors.

Those belong primarily to Stage 2.

Stage 1 should answer:

> **What behavioral situations does each Response Category need to cover?**

---

# 15. Human–LLM–Code Allocation

The established project principle applies:

> **Humans define semantic space; LLMs provide linguistic scale; code performs deterministic auditing.**

| Activity | Human | LLM | Code |
|---|:---:|:---:|:---:|
| Freeze category semantics | ✓ | | |
| Define behavioral coverage dimensions | ✓ | Assist | |
| Create scenario inventory | ✓ | Assist | |
| Generate anchor candidates | | ✓ | |
| Check schema | | | ✓ |
| Check category balance | | | ✓ |
| Detect duplicates | | | ✓ |
| Audit lexical shortcuts | ✓ | Assist | ✓ |
| Review ambiguous scenarios | ✓ | Assist | |
| Final semantic adjudication | ✓ | | |

LLM-generated scenarios and anchors remain **candidate data** until validated.

---

# 16. Validation Protocol

Every Stage-1 candidate should be evaluated as:

```text
Scenario
   +
Conversation Context
   +
Candidate Response
        ↓
Behavioral Interpretation
        ↓
Response Category
```

Validation should answer:

1. Does the candidate realize the intended scenario?
2. Is the intended behavioral reaction clear?
3. Is the category supported by behavioral evidence rather than isolated wording?
4. Could a neighboring category reasonably be assigned?
5. Does the candidate accidentally encode another project label?
6. Is the language natural?
7. Is the behavioral response directed toward the intervention?
8. If context is provided, does the candidate remain consistent with that context?

---

# 17. Stage-1 Quality-Control Checklist

## Semantic QC

- [ ] Correct Response Category
- [ ] Scenario is semantically distinct
- [ ] Behavioral condition is clear
- [ ] Exactly one primary Response Category
- [ ] No accidental ontology expansion
- [ ] Scenario represents a behavioral situation, not merely a sentence pattern

## Decision-Hierarchy QC

- [ ] Behavioral commitment considered
- [ ] Behavioral resistance considered
- [ ] Communicative intention does not override behavioral evidence
- [ ] Pragmatic interpretation considered where necessary
- [ ] Surface wording is not the primary basis of the label

## Orthogonality QC

- [ ] Not determined by emotion alone
- [ ] Not determined by sentiment alone
- [ ] Not determined by Dialogue Purpose
- [ ] Not determined by Persuasion Barrier
- [ ] Not determined by execution status
- [ ] Not determined by task completion

## Linguistic QC

- [ ] Natural wording
- [ ] Appropriate conversational form
- [ ] No unnecessary template repetition
- [ ] No obvious keyword shortcut
- [ ] Direct/indirect/natural realization is appropriate

## Coverage QC

- [ ] All five categories represented
- [ ] Approximately balanced scenario count
- [ ] Behavioral dimensions sufficiently covered
- [ ] Explicit/implicit coverage balanced at corpus level
- [ ] Difficulty spectrum represented
- [ ] Different conversational positions represented
- [ ] Context-dependent cases represented where needed

---

# 18. Shortcut Audit

Before Stage 1 is frozen, perform a targeted shortcut audit.

Test whether category membership can be predicted using:

```text
"thanks"       → VP
"okay"         → P
"maybe"        → I
"not"          → N
"no"           → VN
"absolutely"   → VP
"I'll"         → P
```

These relationships must not become deterministic.

Additional shortcut dimensions:

- punctuation;
- sentence length;
- positive/negative sentiment;
- gratitude words;
- refusal words;
- commitment verbs;
- modal verbs;
- intensifiers;
- emojis or expressive markers.

The same surface forms should occur across categories whenever naturally possible.

---

# 19. Balance and Coverage Audit

After candidate generation, calculate:

### Category distribution

```text
VP
P
I
N
VN
```

### Semantic subtype distribution

Verify:

- subtype count by category;
- scenarios per subtype;
- whether each subtype has sufficient distinct coverage;
- whether any subtype is overrepresented merely because it is easier to generate.

The distribution does **not** need to be numerically equal.

### Scenario distribution

```text
~15–25 scenarios / category
≈75–125 scenarios overall
```

A target near 20/category may be used for planning, but semantic review takes precedence.

### Anchor distribution

```text
Direct
Indirect
Natural
```

### Behavioral dimensions

Verify that important dimensions such as:

- acceptance;
- enthusiasm;
- commitment;
- uncertainty;
- resistance;
- reactance;
- appreciation;
- disengagement

are represented where semantically appropriate.

### Explicitness

```text
Explicit
Implicit
```

### Difficulty

```text
Clear
Moderate
Difficult
```

### Conversational position

Verify that no category is systematically associated with one interaction position.

---

# 20. Deduplication

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

Two examples can represent the same category while still being useful if they represent genuinely different behavioral situations.

---

# 21. Leakage Prevention

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

# 22. Stage-1 Completion Criteria

Stage 1 is complete only when:

1. The five categories have validated semantic coverage.
2. The behavioral semantic coverage matrix is reviewed.
3. The candidate semantic subtype catalogue has been reviewed and frozen.
4. Each subtype represents a meaningful behavioral region within its parent category.
5. The scenario inventory is sufficiently diverse.
6. Approximately 15–25 scenarios/category have been constructed, unless semantic review justifies an adjustment.
7. Each validated scenario has three initial candidate anchors.
8. Category balance has been audited.
9. Subtype coverage and scenario allocation have been audited.
10. Behavioral-dimension coverage has been audited.
8. Explicit/implicit coverage has been audited.
9. Difficulty coverage has been audited.
10. Orthogonality with other project labels has been checked.
11. Decision-hierarchy compliance has been checked.
12. Shortcut audits have been performed.
13. Duplicate and near-duplicate scenarios have been removed.
14. Human validation/adjudication is complete.
15. Scenario lineage is frozen.

---

# 23. Stage-1 Output

The expected Stage-1 construction output is:

```text
01_semantic_coverage/
│
├── behavioral_semantic_coverage/
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
5 Response Categories
        ↓
Candidate / Frozen Semantic Subtype Catalogue
        ↓
Behavioral Semantic Coverage Matrix
        ↓
≈75–125 Distinct Behavioral Scenarios
        ↓
≈225–375 Initial Anchor Candidates
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

# 24. Final Principle

Stage 1 should answer one question:

> **Have we adequately represented the behavioral semantic space of each Response Category before attempting to engineer its decision boundaries?**

The construction sequence is therefore:

```text
Response Category
        ↓
Behavioral Semantic Space
        ↓
Semantic Subtype Catalogue
        ↓
Coverage Matrix
        ↓
Distinct Behavioral Scenarios
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

> **Stage 1 establishes what each Response Category means across diverse behavioral situations; it does not yet attempt to solve the boundary between neighboring categories.**

The five frozen Response Category labels remain the only classifier labels throughout this process. Semantic subtypes, behavioral dimensions, and scenario metadata are construction aids, not ontology expansion.

The central methodological rule is:

> **Use semantic subtypes to organize the space, but let the behavioral semantics determine how many subtypes and scenarios are needed. Do not impose an arbitrary fixed subtype count.**
