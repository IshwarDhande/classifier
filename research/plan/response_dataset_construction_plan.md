# Response Category Dataset Construction Plan — V1

**Status:** Construction Plan — Ontology-Grounded Draft  
**Target:** Response Category Classification  
**Ontology:** Response Category Ontology V1.0  
**Categories:** `VP`, `P`, `I`, `N`, `VN`

---

## 1. Objective

The dataset will train a classifier to infer the user's **immediate behavioral appraisal of the agent's intervention** from conversational evidence.

The classifier must learn:

> **How did the user behaviorally react to the intervention?**

It must remain independent of sentiment, emotion, Dialogue Purpose, Persuasion Barrier, Execution Status, task completion, topic, and isolated keywords.

The Response Category ontology is:

| Label | Category | Core behavioral meaning |
|---|---|---|
| `VP` | Very Positive | Strong acceptance, appreciation, enthusiasm, high engagement |
| `P` | Positive | Acceptance, cooperation, willingness, low resistance |
| `I` | Indifferent | Neutral/non-committal engagement; insufficient evidence of acceptance or resistance |
| `N` | Negative | Reluctance, resistance, disagreement, mild reactance |
| `VN` | Very Negative | Strong rejection, hostility, high reactance, active disengagement |

The scale is ordinal:

```text
VN < N < I < P < VP
```

Response and task completion are explicitly separate constructs. A user can complete a task while reacting negatively, or fail to complete it while remaining indifferent.

---

# 2. Construction Architecture

The construction follows three major stages, with Stage 3 implemented in two chronological halves:

```text
STAGE 1 — Semantic Coverage
        ↓
STAGE 3A — Linguistic Expansion of Stage 1
        ↓
STAGE 2 — Boundary Quality
        ├── 2A Boundary Anchors
        ├── 2B Minimal Pairs
        └── 2C Hard Negatives
        ↓
STAGE 3B — Linguistic Expansion of Stage 2
        ├── Boundary Anchor Expansion
        ├── Hard-Negative Expansion
        └── Minimal-Pair Expansion
        ↓
Validation → Deduplication → Leakage Audit → Final Dataset
```

Stage 3 is deliberately **not one fixed paraphrasing operation**. Its expansion strategy may differ by category and resource.

---

# 3. Stage 1 — Semantic Coverage

## 3.1 Objective

Stage 1 establishes the semantic space of the five response states. Each category must be represented through multiple distinct behavioral situations rather than stereotypical phrases.

The construction hierarchy is:

```text
Response Category
        ↓
Semantic Subtype
        ↓
Semantic Scenario
        ↓
Linguistic Realization
```

The **semantic subtype layer is a construction-level organization layer**, not an additional classifier label. It is used to ensure that each Response Category is covered across substantively different behavioral regions.

The dataset must prevent shortcuts such as:

```text
"Thanks" → VP
"Okay"   → P
"Maybe"  → I
"Not now" → N
"No"     → VN
```

These forms must occur in varied contexts when naturally possible.

## 3.2 Semantic Subtype Catalogue

The number of semantic subtypes is **not fixed in advance**.

Planning range:

```text
5 Response Categories
        ↓
~3–6 Semantic Subtypes / Category
        ↓
~15–25 Semantic Scenarios / Category
        ↓
≈75–125 Semantic Scenarios Overall
```

These are planning ranges rather than ontology requirements. The final number of subtypes and scenarios must be determined by semantic coverage.

### Subtype Rules

Each subtype must:

1. represent a substantively distinct behavioral region;
2. remain fully within its parent Response Category;
3. help organize semantic coverage rather than introduce a new label;
4. prevent multiple scenarios from collapsing into one narrow behavioral pattern;
5. be sufficiently distinct from neighboring subtypes;
6. support meaningful scenario construction.

Do **not** impose an arbitrary equal number of subtypes across categories.

For example, a category may require four subtypes while another may require five or six if its behavioral space is more diverse.

### Subtype Derivation

Subtypes should be derived systematically:

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

The subtype catalogue must be reviewed and frozen before large-scale scenario construction.

## 3.3 Scenario Inventory

After the subtype catalogue is frozen, construct a semantic scenario inventory.

Target range:

```text
~15–25 semantic scenarios / category
≈75–125 semantic scenarios overall
```

A value near 20 scenarios/category may be used as a planning reference, but the final count should follow semantic coverage rather than a fixed quota.

Each scenario must represent a distinct behavioral situation, not merely a paraphrase of another scenario.

Each scenario should record at minimum:

```text
scenario_id
category
semantic_subtype
scenario_description
behavioral_core
relevant_intervention_context
closest_competing_category
```

Scenario allocation across subtypes may vary according to semantic richness.

## 3.4 Category-Specific Semantic Coverage

### VP — Very Positive

Cover distinct regions such as:

- enthusiastic acceptance;
- strong appreciation;
- proactive engagement;
- usefulness/motivation expressed toward the intervention;
- acceptance plus follow-up engagement;
- immediate or voluntary cooperation.

Boundary: acceptance alone is insufficient; appreciation, enthusiasm, or high engagement must support VP.

### P — Positive

Cover distinct regions such as:

- ordinary acceptance;
- cooperation;
- willingness to comply;
- genuine commitment;
- polite acceptance;
- mild appreciation;
- implicit cooperation;
- delayed but genuine acceptance.

Boundary: cooperative acceptance without the strong enthusiasm required for VP.

### I — Indifferent

Cover distinct regions such as:

- neutral acknowledgement;
- uncertainty;
- delayed decision;
- non-commitment;
- passive response;
- weak engagement;
- clarification without acceptance;
- insufficient evidence of future cooperation.

Boundary: neither clear acceptance nor clear rejection. Indifference is not disagreement.

### N — Negative

Cover distinct regions such as:

- reluctance;
- mild refusal;
- disagreement;
- behavioral resistance;
- mild annoyance;
- conditional resistance;
- passive resistance;
- reduced cooperation.

Boundary: resistance remains potentially recoverable and does not reach VN-level rejection/reactance.

### VN — Very Negative

Cover distinct regions such as:

- explicit rejection;
- strong resistance;
- hostility;
- high reactance;
- active disengagement;
- interaction termination;
- rejection of future assistance;
- strong opposition.

Boundary: strong rejection/reactance or active disengagement, rather than ordinary disagreement or reluctance.

## 3.5 Initial Semantic Anchors

Each validated semantic scenario initially receives three canonical realization types:

1. Direct
2. Indirect
3. Natural conversational

Planning target:

```text
~75–125 scenarios × 3 anchors
≈225–375 Stage-1 candidate examples
```

The exact number depends on the final semantic scenario inventory.

Anchors must instantiate the intended semantic scenario rather than merely paraphrase one another.

These remain candidates until validation.

## 3.6 Stage-1 Validation

Before Stage 3A begins, validate the semantic resources in the following order:

```text
Subtype Catalogue
        ↓
Scenario Inventory
        ↓
Initial Semantic Anchors
        ↓
Human Review
        ↓
Freeze Stage-1 Semantic Coverage
```

Validation must confirm:

- the subtype is semantically distinct and correctly assigned;
- each scenario expresses one dominant behavioral situation;
- the parent Response Category is correct;
- neighboring categories are not accidentally conflated;
- scenario descriptions are sufficiently distinct;
- anchors preserve the intended behavioral appraisal;
- coverage is not dominated by stereotypical lexical forms;
- semantic gaps and overrepresented regions are identified.

Stage 3A should begin only after the Stage-1 semantic space has been reviewed.

---

# 4. Stage 3A — Linguistic Expansion of Stage 1

Stage 3A begins only after Stage 1 semantic coverage has been reviewed and frozen.

## 4.1 Objective

> **Same Response Category + same semantic scenario → diverse linguistic realizations.**

Stage 3A expands the validated Stage-1 semantic resources without changing their underlying behavioral meaning.

Preserve:

- behavioral appraisal;
- Response Category;
- semantic subtype;
- semantic scenario;
- relevant intervention;
- intended interpretation.

The goal is linguistic diversity, not creation of new semantic scenarios.

## 4.2 Expansion Principle

Stage 3A is **not fixed to one universal variation template**.

Variation dimensions should be selected according to the semantic characteristics of each category and scenario.

Potential dimensions include:

- lexical variation;
- syntactic variation;
- conversational naturalization;
- explicit/implicit realization;
- sentence-length variation;
- discourse-structure variation;
- hesitation;
- self-correction;
- pragmatic reformulation;
- question/statement framing where semantically valid;
- natural variation in commitment, resistance, appreciation, or engagement expression.

Not every scenario requires every variation dimension.

### Category-Oriented Expansion

```text
VP → appreciation / enthusiasm / proactive engagement
P  → ordinary acceptance / cooperation / commitment
I  → uncertainty / acknowledgement / non-commitment
N  → reluctance / disagreement / resistance
VN → rejection / hostility / disengagement
```

These are expansion directions, not additional labels or fixed subtype definitions.

## 4.3 Resource-Level Expansion

Expansion should operate from validated Stage-1 scenario families:

```text
Scenario
   ↓
Validated Initial Anchors
   ↓
Category-appropriate linguistic variations
   ↓
Candidate realizations
   ↓
Human validation
```

Variants may differ substantially in wording while preserving the same semantic scenario.

For example, a commitment scenario may be realized through direct commitment, conversational commitment, implicit cooperation, or natural delayed wording, provided the underlying behavioral appraisal remains unchanged.

## 4.4 Candidate Generation Rules

LLM-generated variants must:

1. preserve the same semantic subtype;
2. preserve the same semantic scenario;
3. preserve the same Response Category;
4. remain natural in conversational context;
5. avoid introducing a stronger or weaker behavioral appraisal unless that change is explicitly intended;
6. avoid introducing a competing Response Category;
7. avoid relying on stereotypical category keywords;
8. avoid becoming duplicates of existing variants.

Every candidate must retain lineage to its Stage-1 parent:

```text
semantic_subtype
scenario_id
parent_id
lineage_id
variation_type
```

## 4.5 Stage-3A Validation

Each candidate is validated against its parent semantic scenario.

Reject candidates when:

- the behavioral category changes;
- the semantic scenario changes;
- another response state becomes dominant;
- the utterance becomes unnatural;
- the intervention target changes;
- the candidate introduces unintended sentiment/emotion as the main signal;
- the candidate is effectively a duplicate;
- the candidate creates a lexical shortcut.

The key test is:

> **If the wording changes but the semantic situation remains the same, would a careful annotator still assign the same Response Category?**

## 4.6 Stage-3A Coverage Audit

After expansion, audit:

- lexical diversity;
- syntactic diversity;
- sentence-length diversity;
- explicit/implicit diversity;
- conversational naturalness;
- variation across semantic subtypes;
- variation across semantic scenarios;
- representation of difficult pragmatic forms;
- shortcut resistance;
- preservation of category boundaries.

The audit should identify semantic regions that remain linguistically narrow and trigger targeted expansion rather than blindly applying the same number of variants everywhere.

## 4.7 Stage-3A Output Principle

Stage 3A should produce a **linguistically diverse realization layer over a frozen semantic Stage-1 space**:

```text
Frozen Semantic Subtype
        ↓
Frozen Semantic Scenario
        ↓
Initial Semantic Anchors
        ↓
Linguistic Expansion
        ↓
Validated Stage-3A Realizations
```

The number of Stage-3A variants is therefore **not fixed in advance**. Expansion should continue until each semantic region has sufficient linguistic diversity and shortcut resistance, subject to validation, deduplication, and leakage constraints.

# 5. Stage 2 — Boundary Quality

Stage 2 maps the decision boundaries between response states.

Central question:

> **Why is this response Category A rather than Category B?**

Because the ontology is ordinal, **adjacent boundaries receive highest priority**.

## 5.1 Primary Adjacent Boundaries

```text
VP ↔ P
P  ↔ I
I  ↔ N
N  ↔ VN
```

These represent the principal transitions on the behavioral scale.

## 5.2 Secondary Non-Adjacent Boundaries

The remaining six pairwise boundaries should also be represented where useful:

```text
VP ↔ I
VP ↔ N
VP ↔ VN
P  ↔ N
P  ↔ VN
I  ↔ VN
```

Thus there are:

```text
5 categories → 10 possible pairwise boundaries
```

Adjacent boundaries should receive the strongest semantic scrutiny; non-adjacent boundaries help prevent coarse polarity shortcuts.

---

# 6. Stage 2A — Boundary Anchors

For each selected confusion pair, use the established six-item boundary structure:

1. A Prototype
2. B Prototype
3. A-Leaning Boundary
4. B-Leaning Boundary
5. Implicit A
6. Implicit B

Initial full-matrix planning target:

```text
10 pairs × 6 anchors = 60 boundary anchors
```

These are candidate examples until human validation.

## 6.1 Response-Specific Boundary Diagnostics

### VP ↔ P
Is acceptance accompanied by strong appreciation, enthusiasm, or high engagement?

### P ↔ I
Is there sufficient evidence of behavioral acceptance/cooperation?

### I ↔ N
Is there actual behavioral resistance rather than uncertainty or neutrality?

### N ↔ VN
Does resistance reach strong rejection, hostility, high reactance, or active disengagement?

### Non-adjacent boundaries
Does the behavioral evidence genuinely place the response toward one category rather than relying on positive/negative wording?

---

# 7. Stage 2B — Minimal Pairs

Minimal pairs hold the conversational situation as constant as practical while changing the primary behavioral response category.

Example:

```text
P: "Okay, I'll do it."
I: "I'll think about it."
```

Another boundary:

```text
N:  "I'd rather not."
VN: "Leave me alone. I'm not doing this."
```

The exact examples will be generated only after boundary definitions are validated.

## 7.1 Pair-Level Rules

Generate A and B together. Preserve where practical:

- same intervention;
- same task context;
- similar conversational position;
- comparable information content;
- comparable complexity.

Change primarily the behavioral appraisal.

The **pair**, not the individual utterance, is the unit of QC.

## 7.2 Planning Target

Initial target inherited from the established construction methodology:

```text
10 pairs × 6 minimal-pair variants
= 60 minimal pairs
= 120 utterances
```

This remains provisional.

---

# 8. Stage 2C — Hard Negatives

Hard negatives introduce cues associated with another Response Category while preserving the target behavioral response.

Core principle:

> **Surface polarity or response cue ≠ behavioral response category.**

Important Response-specific patterns include:

- gratitude/positive wording with resistance;
- negative wording with genuine cooperation;
- future/commitment language without sufficient acceptance;
- acceptance language combined with annoyance/resistance;
- positive emotion unrelated to the intervention;
- conventional politeness without strong positive appraisal;
- sarcasm or pragmatic reversal.

Initial hard-negative mechanisms:

1. Competing keyword
2. Competing phrase
3. Misleading opening clause
4. Self-correction
5. Multiple competing cues
6. Strong conversational distractor

These mechanisms remain subject to ontology-specific refinement.

Planning target:

```text
10 pairs × 6 hard negatives = 60 hard-negative candidates
```

---

# 9. Stage 3B — Linguistic Expansion of Stage 2

Stage 3B starts after Stage 2 has been completed and validated.

It contains three independent tracks:

```text
2A Boundary Anchors → Boundary-Preserving Expansion
2B Minimal Pairs    → Contrast-Preserving Expansion
2C Hard Negatives  → Distractor-Preserving Expansion
```

The number and exact variation types are **not fixed in advance**.

## 9.1 Boundary Anchor Expansion

Preserve:
- target category;
- competing category;
- boundary position;
- behavioral interpretation;
- diagnostic property.

Potential dimensions:
- lexical reformulation;
- syntactic reformulation;
- conversational naturalization;
- explicit/implicit conversion;
- length variation;
- pragmatic reformulation;
- context-preserving reformulation.

## 9.2 Hard-Negative Expansion

Preserve:
- target category;
- hard-negative mechanism;
- competing cue;
- dominant behavioral interpretation.

Core rule:

> **Vary the distractor realization, not the behavioral label.**

Different mechanisms may require different expansion strategies.

## 9.3 Minimal-Pair Expansion

Generate both sides together.

Preserve:
- shared situation;
- intervention;
- context;
- comparable difficulty;
- A↔B behavioral contrast.

Do not independently paraphrase the two sides if that weakens the contrast.

---

# 10. Orthogonality and Semantic Invariants

The Response Category must remain distinct from the other Dialogue Interpreter dimensions.

```text
Response Category  → How did the user react?
Dialogue Purpose   → What conversational function is being performed?
Persuasion Barrier → Why is adherence difficult?
Execution Status   → What is the task execution state?
```

The response dataset must not use these dimensions as hidden proxies.

## 10.1 Behavioral, Not Emotional

```text
Happy ≠ automatically VP
Angry ≠ automatically VN
```

Emotion may provide evidence, but the label concerns behavioral reaction toward the intervention.

## 10.2 Response ≠ Completion

```text
Completion = whether the task happened
Response   = how the user reacted
```

## 10.3 Response ≠ Dialogue Purpose

The same dialogue purpose may occur with different response categories.

## 10.4 Response ≠ Persuasion Barrier

A barrier and behavioral reaction are separate semantic dimensions.

## 10.5 Response ≠ Execution Status

Current execution state must not substitute for behavioral appraisal.

---

# 11. Annotation Protocol

Use:

```text
Conversation Context
        +
Current User Utterance
        ↓
Behavioral appraisal toward intervention
        ↓
Exactly one Response Category
```

Annotators select exactly one:

```text
VP / P / I / N / VN
```

Also record:

```text
closest_competing_category
ambiguity_flag
```

For difficult examples, ask:

1. Is there behavioral acceptance?
2. Is there behavioral resistance?
3. Is there enthusiasm/appreciation?
4. Is there strong rejection/reactance?
5. Is the user simply uncertain/non-committal?
6. Is the evidence actually directed toward the intervention?

---

# 12. Category-Specific Diagnostic Rules

## VP
- acceptance;
- appreciation/enthusiasm;
- active engagement;
- no meaningful resistance.

## P
- acceptance;
- cooperation;
- low resistance;
- enthusiasm not strong enough for VP.

## I
- no clear acceptance;
- no clear rejection;
- weak/absent commitment;
- weak/absent resistance;
- future cooperation genuinely uncertain.

## N
- reluctance/resistance/disagreement;
- mild refusal or annoyance;
- interaction remains potentially recoverable;
- VN-level rejection absent.

## VN
- strong rejection;
- high reactance/hostility;
- active disengagement or interaction termination;
- minimal willingness to cooperate.

---

# 13. Human–LLM–Code Allocation

Use the established project principle:

> **Humans define semantic space and decision boundaries; LLMs provide linguistic scale; code performs deterministic auditing.**

| Activity | Human | LLM | Code |
|---|:---:|:---:|:---:|
| Freeze ontology | ✓ | | |
| Define semantics | ✓ | Assist | |
| Define scenarios | ✓ | Assist | |
| Generate candidates | | ✓ | |
| Generate boundary candidates | ✓ | ✓ | |
| Generate minimal pairs | ✓ | ✓ | |
| Generate hard negatives | ✓ | ✓ | |
| Validate difficult cases | ✓ | Assist | |
| Deduplication | | | ✓ |
| Balance/statistics | | | ✓ |
| Lineage tracking | | | ✓ |
| Leakage audit | | | ✓ |
| Final adjudication | ✓ | | |

LLM-generated examples remain candidates until validated.

---

# 14. Quality Control

## Semantic QC

- correct category;
- one primary behavioral outcome;
- valid intervention context;
- no accidental ontology expansion.

## Boundary QC

- adjacent ordinal boundaries clearly represented;
- non-adjacent boundaries represented where useful;
- minimal pairs remain contrastive;
- hard negatives contain genuine competing cues;
- ambiguous cases adjudicated.

## Linguistic QC

- lexical diversity;
- syntactic diversity;
- length diversity;
- explicit/implicit diversity;
- conversational naturalness.

## Orthogonality QC

Ensure labels are not determined by:

- emotion alone;
- sentiment polarity;
- topic;
- task completion;
- execution status;
- persuasion barrier;
- dialogue purpose;
- isolated keywords.

---

# 15. Shortcut Audit

Explicitly test and break shortcuts such as:

```text
"Thanks"     → not always VP
"Okay"       → not always P
"Sure"       → not always P
"Maybe"      → not always I
"No"         → not always N/VN
"Absolutely" → not always VP
"I'll"       → not always P
"not"        → not always N/VN
```

Also audit punctuation, negation, modal verbs, sentence length, gratitude terms, commitment verbs, refusal verbs, and sentiment polarity.

---

# 16. Context Requirements

Response interpretation may require conversational history.

Represent input as:

```text
X_t = [C_{t-k:t-1}, u_t]
```

where `C` is relevant dialogue history and `u_t` is the current user utterance.

Context is particularly important for:

- sarcasm;
- conventional politeness;
- ambiguous agreement;
- delayed compliance;
- mixed acceptance/resistance;
- prior commitments/refusals;
- repeated interventions.

Do not add irrelevant context merely to increase history length.

---

# 17. Master Schema and Lineage

Recommended schema:

```text
example_id
scenario_id
parent_id
lineage_id
category
stage
resource_type
context
utterance
response_category
closest_competing_category
variation_type
hard_negative_type
source
validation_status
annotator_1_label
annotator_2_label
adjudicated_label
ambiguity_flag
split
```

Every linguistic variant must retain its parent/lineage relationship.

---

# 18. Leakage-Safe Split

Use the project standard:

```text
70% Train
15% Validation
15% Test
```

Split by semantic/lineage family rather than individual utterance.

Keep together:

- scenario families;
- Stage-1 anchors;
- Stage-3A variants;
- boundary-anchor families;
- minimal-pair families;
- hard-negative families;
- Stage-3B variants;
- closely related contextual variants.

---

# 19. Challenge Set

Maintain a held-out diagnostic challenge set containing:

- VP↔P boundaries;
- P↔I boundaries;
- I↔N boundaries;
- N↔VN boundaries;
- selected non-adjacent boundaries;
- hard negatives;
- mixed acceptance/resistance;
- conventional gratitude;
- sarcasm;
- uncertain commitment;
- delayed compliance;
- positive wording with negative behavioral appraisal;
- negative wording with positive behavioral appraisal;
- context-dependent cases.

Use primarily for diagnostic evaluation, not ordinary training.

---

# 20. Construction Order

```text
1. Verify / freeze Response Category semantics
        ↓
2. Stage 1 — Semantic Scenario Inventory
        ↓
3. Stage 1 — Initial Anchors
        ↓
4. Stage 1 Validation
        ↓
5. Stage 3A — Stage-1 Linguistic Expansion
        ↓
6. Stage 3A Validation
        ↓
7. Stage 2A — Boundary Anchors
        ↓
8. Stage 2B — Minimal Pairs
        ↓
9. Stage 2C — Hard Negatives
        ↓
10. Stage 2 Validation
        ↓
11. Stage 3B — Boundary Anchor Expansion
        ↓
12. Stage 3B — Hard-Negative Expansion
        ↓
13. Stage 3B — Minimal-Pair Expansion
        ↓
14. Final QC
        ↓
15. Deduplication
        ↓
16. Leakage Audit
        ↓
17. 70/15/15 Group Split
        ↓
18. Challenge Set
```

---

# 21. Initial Quantitative Targets

These are planning targets only.

### Stage 1

```text
5 categories
× 20 scenarios/category
= 100 semantic scenarios

100 scenarios
× 3 initial anchors
= 300 Stage-1 candidates
```

### Stage 2

```text
10 pairwise boundaries
× 6 boundary anchors
= 60 boundary anchors

10 pairwise boundaries
× 6 minimal-pair variants
= 60 minimal pairs
= 120 utterances

10 pairwise boundaries
× 6 hard negatives
= 60 hard-negative candidates
```

### Stage 3

```text
Stage 3A → expand Stage-1 semantic resources

Stage 3B → expand:
             • boundary anchors
             • hard negatives
             • minimal pairs
```

**No fixed Stage-3 expansion count is imposed at this stage.** The number and type of variants should depend on category difficulty, boundary density, linguistic coverage, duplication, and subsequent classifier error analysis.

---

# 22. Important Difference from Dialogue Purpose

The construction should reuse the **methodology**, not blindly copy the exact dataset behavior.

Dialogue Purpose is primarily a communicative-function classification problem.

Response Category is an **ordinal behavioral-appraisal classification problem**:

```text
Very Negative
      ↓
Negative
      ↓
Indifferent
      ↓
Positive
      ↓
Very Positive
```

Therefore the Response dataset must give particular attention to:

- intensity/degree;
- adjacent ordinal boundaries;
- behavioral acceptance versus resistance;
- enthusiasm versus ordinary acceptance;
- neutrality versus reluctance;
- mild resistance versus strong rejection;
- mixed responses and dominant behavioral outcome;
- pragmatic/contextual interpretation.

---

# 23. Final Construction Principle

The Response Category dataset should follow:

```text
Semantic Space
      ↓
Behavioral Category Coverage
      ↓
Stage-1 Linguistic Diversity
      ↓
Ordinal Decision Boundaries
      ↓
Boundary / Contrast / Distractor Diversity
      ↓
Stage-2 Linguistic Expansion
      ↓
Contextual + Pragmatic Robustness
      ↓
Robust Response Classification
```

> **First cover the behavioral semantic space, then map where neighboring response states differ, and finally expose the classifier to diverse linguistic and contextual realizations of those distinctions.**

The final gold dataset size and exact Stage-3 expansion matrices should be frozen only after candidate generation, validation, deduplication, leakage auditing, and initial classifier error analysis.
