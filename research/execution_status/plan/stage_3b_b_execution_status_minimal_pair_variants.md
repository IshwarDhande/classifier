# Stage 3B-B — Minimal Pair Variant Specification

**Input:** Stage 2B Minimal Pairs  
**Expansion unit:** Complete minimal-pair family  
**Goal:** Contrast-preserving linguistic expansion

---

## 1. Purpose

Minimal pairs teach that highly similar situations can receive different Execution Status labels because the user's actual execution state changes.

Therefore Stage 3B-B expands the **pair**, not the utterances independently.

```text
Shared situation
      ↓
A execution state ↔ B execution state
      ↓
Paired linguistic expansion
```

The central principle is:

> **Change the linguistic realization of both sides while preserving the exact execution-state contrast.**

The pair remains the primary semantic and quality-control unit.

---

## 2. Fixed Invariants

Preserve:

- same boundary;
- same target task;
- same intervention/reminder context;
- same conversational position;
- comparable information;
- comparable linguistic difficulty;
- same relevant history;
- primary A↔B execution-state contrast.

The only intended semantic difference between the two sides should remain the execution-state evidence that defines the original minimal pair.

---

## 3. Execution Status Boundaries

Stage 3B-B operates over the three frozen Stage-2 boundaries.

### B01 — Not Started ↔ In Progress

Preserve the contrast:

```text
A: execution has not begun
B: execution has begun but is unfinished
```

The pair must not become:

```text
future intention ↔ completion
```

or another unintended distinction.

### B02 — In Progress ↔ Completed

Preserve the contrast:

```text
A: execution has begun but remains unfinished
B: execution has finished
```

The distinction must be based on completion of the target task, not sentiment, motivation, or wording.

### B03 — Not Started ↔ Completed

Preserve the contrast:

```text
A: execution has not begun
B: execution has finished
```

The larger distinction must remain behaviorally/executionally justified rather than being reduced to a simple future-word versus completion-word contrast.

---

## 4. Standard Six Paired Variants

| Variant | Type | Construction |
|---|---|---|
| MP-V01 | `LEX` | Reformulate both sides with matched execution-related vocabulary |
| MP-V02 | `SYN` | Change syntax on both sides comparably |
| MP-V03 | `NAT` | Naturalize both sides |
| MP-V04 | `EXP` | Change explicitness while retaining the execution contrast |
| MP-V05 | `LEN` | Use matched short/medium/long realizations |
| MP-V06 | `CMK` | Vary conversational markers comparably |

`PRG`, `DSC`, `HES`, and `QST` may be used selectively.

---

## 5. Pair Generation Rule

Generate both sides jointly:

```text
Original pair
    ↓
Identify shared situation
    ↓
Identify exact execution-state contrast
    ↓
Identify diagnostic execution evidence
    ↓
Transform both sides comparably
    ↓
Re-check execution-state contrast
```

Do not independently paraphrase the two sides.

The pair must remain matched in:

- target task;
- intervention;
- conversational situation;
- information content;
- linguistic complexity;
- relevant history.

Only the intended execution-state evidence should distinguish the two labels.

---

## 6. Matched-Difficulty Principle

Do not make one side easier because it is:

- much longer;
- much more explicit;
- syntactically simpler;
- packed with execution-status keywords;
- more conversationally natural;
- more detailed about the task;
- more temporally explicit;
- more emotionally expressive.

For example, avoid constructing a pair where:

```text
Not Started = "I'll do it later."
Completed   = "I already completed it."
```

if the only reliable distinction is the obvious temporal/status vocabulary.

Instead, linguistic variation should make both sides comparably realistic while preserving the actual execution contrast.

---

## 7. Execution Evidence Matching

The pair should contain comparable amounts of evidence.

### B01

If one side communicates non-execution indirectly, the other side should not receive an unnecessarily explicit execution statement.

Target:

```text
No execution
       ↔
Actual ongoing execution
```

### B02

If one side expresses unfinished execution through contextual evidence, the other should not simply be a one-word "Done" unless that asymmetry is deliberately being tested.

Target:

```text
Unfinished execution
       ↔
Finished execution
```

### B03

Both sides should remain natural and sufficiently informative while preserving:

```text
No execution
       ↔
Completed execution
```

---

## 8. Standard Variant Construction

### MP-V01 — `LEX`

Reformulate execution-related vocabulary on both sides.

Use matched lexical diversity.

Do not allow one side to accumulate highly diagnostic status words while the other side does not.

---

### MP-V02 — `SYN`

Change syntactic structure comparably on both sides.

Possible transformations include:

- clause restructuring;
- coordination;
- subordination;
- active conversational forms;
- fragments where natural.

The execution-state contrast must remain unchanged.

---

### MP-V03 — `NAT`

Naturalize both sides into realistic conversational language.

Both sides should have comparable conversational plausibility.

Do not make one state sound artificially formal or templated.

---

### MP-V04 — `EXP`

Change explicitness on both sides while preserving the contrast.

Possible structure:

```text
Explicit A ↔ Explicit B
Implicit A ↔ Implicit B
Explicit A ↔ Implicit B
```

The final form must remain sufficiently interpretable for expert annotation.

---

### MP-V05 — `LEN`

Create matched short/medium/long realizations.

The difference in length must not become a proxy for Execution Status.

For example:

```text
Short A ↔ Short B
Medium A ↔ Medium B
Long A ↔ Long B
```

where practical.

---

### MP-V06 — `CMK`

Add or modify conversational markers comparably.

Examples:

- "well";
- "actually";
- "yeah";
- "okay";
- "right";
- "no";
- natural hesitation markers.

Markers must not determine the execution label.

---

## 9. Execution-Specific Contrast Controls

### B01 — Initiation Contrast

Ensure that the pair distinguishes:

```text
Preparation / intention / non-execution
              ↔
Actual execution has begun
```

Do not rely solely on:

- will;
- going to;
- about to;
- starting.

### B02 — Completion Contrast

Ensure that the pair distinguishes:

```text
Execution underway but unfinished
              ↔
Execution finished
```

Do not rely solely on:

- almost;
- done;
- finished;
- already.

### B03 — Non-Execution vs Completion

Ensure that the pair distinguishes:

```text
No target-task execution
              ↔
Target-task execution completed
```

Particular attention should be paid to:

- completion of another task;
- retrospective references;
- indirect completion;
- refusal;
- inability;
- forgetting;
- unrelated temporal events.

---

## 10. Forbidden Transformations

Reject if:

- only one side changes substantially;
- shared context changes;
- target task changes;
- intervention changes;
- conversational position changes;
- execution contrast disappears;
- one side crosses into a third state;
- one side becomes substantially easier to classify;
- lexical cues become deterministic;
- temporal cues become deterministic;
- one side becomes sentiment-heavy;
- one side becomes a Persuasion Barrier example;
- one side becomes a Dialogue Purpose example;
- one side becomes a planning/scheduling example;
- pair becomes merely a difference in wording rather than execution state.

---

## 11. Pair Acceptance Test

```text
[✓] Shared situation preserved
[✓] Target task preserved
[✓] Intervention preserved
[✓] A Execution Status preserved
[✓] B Execution Status preserved
[✓] Execution contrast preserved
[✓] Comparable information
[✓] Comparable linguistic difficulty
[✓] Comparable explicitness
[✓] No trivial status keyword
[✓] Natural language
[✓] No ontology leakage
```

The pair is the primary QC unit.

If one side fails, the pair fails.

---

## 12. Minimal-Pair Diagnostic Test

For every pair ask:

> **If the two utterances were placed in the same conversational context, would expert annotators assign different Execution Status labels for the same execution-related reason?**

Then ask:

> **Is that difference still present after the linguistic transformation?**

If either answer is no, reject the variant.

---

## 13. Lexical Shortcut Audit

Each paired variant must be checked for deterministic cues such as:

```text
already
now
later
finished
done
starting
started
almost
will
going to
```

The presence or absence of such words must not be the only reliable difference between the pair.

Where such expressions are used, both sides should be evaluated in context.

---

## 14. Cross-Ontology Audit

The pair must not become distinguishable primarily through:

- response sentiment;
- emotional intensity;
- motivation;
- refusal language;
- Persuasion Barrier;
- Dialogue Purpose;
- Response Category;
- scheduling/deadline information;
- Task Manager operational status.

The intended contrast is Execution Status only.

---

## 15. Leakage

All descendants of one minimal-pair family remain together in every future split.

The leakage group is:

```text
pair_id
   ↓
original A/B pair
   ↓
all Stage 3B-B paired variants
```

Both sides and all descendants must remain in the same train/validation/test group.

Do not split the two sides across partitions.

---

## 16. Recommended Metadata

Retain:

```text
example_id
pair_id
parent_id
lineage_id
boundary_id
pair_role
execution_status
semantic_subtype
context
utterance
target_task
variation_type
source
validation_status
ambiguity_flag
```

The pair must retain sufficient metadata to reconstruct its original Stage-2 family.

---

## 17. Final Principle

> **Stage 3B-B increases linguistic diversity of minimal-pair resources while preserving the exact Execution Status contrast that makes the pair diagnostically useful.**

The classifier should learn:

```text
execution evidence
        ↓
execution-state distinction
```

rather than:

```text
surface wording
        ↓
label
```

The pair remains the fundamental unit of construction, validation, and leakage control.
