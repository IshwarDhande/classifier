# Stage 3B-C — Hard Negative Variant Specification

**Input:** Stage 2C Hard Negatives  
**Expansion unit:** Individual hard-negative example  
**Goal:** Distractor-preserving linguistic expansion

---

## 1. Purpose

Stage 2C tests whether the classifier can resist misleading surface cues that could suggest the wrong Execution Status. Stage 3B-C expands those cues while preserving the target execution state.

The central rule is:

> **Vary the distractor realization, not the Execution Status.**

A hard-negative variant must remain difficult for the same reason as its parent while preserving the actual execution evidence that supports the target state.

---

## 2. Fixed Invariants

Preserve:

- target Execution Status;
- boundary;
- hard-negative mechanism;
- dominant execution evidence;
- target task;
- intervention/reminder context;
- conversational situation;
- distractor-target relationship.

The misleading cue may change linguistically, but the semantic relationship between the distractor and the target execution evidence must remain.

---

## 3. Hard-Negative Mechanisms

Stage 2C hard negatives use execution-specific misleading mechanisms.

### HN01 — Competing Temporal Cue

Introduce or vary a temporal expression that could suggest another execution state.

Examples of potential cues include:

- later;
- now;
- already;
- tomorrow;
- earlier;
- just.

The temporal expression must not become the true execution evidence.

---

### HN02 — Competing Execution-Status Phrase

Use a phrase that superficially suggests another execution state.

Examples include references to:

- starting;
- finishing;
- being done;
- almost being done;
- having done something.

The phrase must remain contextually non-dominant when the target state differs.

---

### HN03 — Misleading Opening Clause

Begin with a clause that suggests one execution interpretation, followed by stronger evidence supporting the target state.

The opening cue may be reformulated or repositioned.

The final interpretation must remain determined by the dominant execution evidence.

---

### HN04 — Self-Correction

Vary an initial mistaken, incomplete, or misleading statement followed by a correction.

The corrected/final execution evidence must continue to support the target state.

The correction itself must not create genuine ambiguity.

---

### HN05 — Multiple Competing Cues

Vary the combination and order of multiple misleading cues.

The example may contain several expressions suggesting different execution states, but the target execution evidence must remain dominant.

---

### HN06 — Strong Conversational Distractor

Vary conversational material such as:

- prior interaction references;
- gratitude;
- frustration;
- apology;
- politeness;
- explanation;
- reminder discussion.

These may distract attention from the execution evidence but must not replace it.

---

## 4. Standard Six Variants

| Variant | Type | Purpose |
|---|---|---|
| HN-V01 | `LEX` | Change distractor vocabulary |
| HN-V02 | `NAT` | Naturalize distractor realization |
| HN-V03 | `EXP` | Change distractor/target explicitness |
| HN-V04 | `DSC` | Change discourse ordering |
| HN-V05 | `PRG` | Change pragmatic realization |
| HN-V06 | `CMK` | Change conversational markers |

`SYN`, `LEN`, `HES`, and `QST` may be used selectively.

---

## 5. Distractor Preservation

The intended structure is:

```text
Surface cue
     ↓
Potentially misleading
     ↓
BUT
     ↓
Actual execution evidence
     ↓
Target Execution Status
```

A variant is invalid if the distractor becomes the actual execution evidence.

The target state must remain recoverable from the complete utterance.

---

## 6. Execution-Specific Distractor Examples

### Not Started target

A misleading cue may suggest that execution has begun:

```text
"starting"
"now"
"already"
"just"
```

but the complete utterance must still establish that the target task has not actually begun.

Examples of mechanisms to vary:

- preparation mistaken for execution;
- intention mistaken for execution;
- discussion of starting mistaken for actual initiation;
- another task already completed;
- self-correction from apparent initiation to non-execution.

---

### In Progress target

A misleading cue may suggest either non-execution or completion.

Examples:

```text
"later"
"almost done"
"finished"
"done"
```

The complete utterance must still establish that target-task execution has begun but remains unfinished.

Particular care is required with:

```text
almost finished ≠ Completed
```

---

### Completed target

A misleading cue may suggest that the task remains unfinished.

Examples:

```text
"still"
"almost"
"working on it"
"just"
```

The complete utterance must nevertheless establish that the target task has actually finished.

Where multiple events are mentioned, completion must refer to the target task.

---

## 7. Standard Variant Construction

### HN-V01 — `LEX`

Change the misleading vocabulary while preserving the same competing implication.

The replacement distractor must be natural and semantically comparable.

Do not replace a distractor with a word that makes the target label deterministic.

---

### HN-V02 — `NAT`

Naturalize the distractor and surrounding utterance.

The hard negative should sound like ordinary user conversation rather than a deliberately constructed adversarial example.

---

### HN-V03 — `EXP`

Change the explicitness of the distractor or target evidence.

Possible forms include:

```text
Explicit distractor + implicit target
Implicit distractor + explicit target
Implicit distractor + implicit target
```

The target execution state must remain sufficiently recoverable.

---

### HN-V04 — `DSC`

Change the position or ordering of the distractor.

For example:

```text
Distractor → Target evidence
```

may become:

```text
Target evidence → Distractor
```

or:

```text
Distractor → additional context → Target evidence
```

The target execution evidence must remain dominant.

---

### HN-V05 — `PRG`

Change how the misleading cue is pragmatically presented.

Possible realizations include:

- clarification;
- explanation;
- correction;
- response to a reminder;
- conversational qualification;
- indirect reference.

The pragmatic framing must not introduce a new target concept.

---

### HN-V06 — `CMK`

Vary conversational markers surrounding the distractor.

Examples include:

- "actually";
- "well";
- "yeah";
- "no";
- "okay";
- "right";
- hesitation markers.

Markers must not become the basis for the Execution Status label.

---

## 8. Controlled Distractor Strength

Where useful, variants may be organized as:

```text
HN-L1 → weak distractor
HN-L2 → moderate distractor
HN-L3 → strong distractor
```

The distractor should become progressively more misleading without becoming semantically decisive.

The intended relationship is:

```text
Weak distractor
      ↓
Moderate distractor
      ↓
Strong distractor
      ↓
BUT
      ↓
Target execution evidence remains dominant
```

The strongest valid distractor should challenge shortcut-based classification while remaining correctly annotatable by an expert.

---

## 9. Hard-Negative Boundary Focus

### B01 — Not Started ↔ In Progress

Hard negatives should challenge whether the target task has actually begun.

Important cases include:

- future intention described as if starting;
- preparation mistaken for execution;
- discussion of beginning mistaken for beginning;
- another task currently being performed;
- self-correction about whether execution started.

---

### B02 — In Progress ↔ Completed

Hard negatives should challenge whether execution has finished.

Important cases include:

- "almost done" vs actually done;
- one subtask completed while the target task remains unfinished;
- completion wording referring to another event;
- "finished" used in a non-target context;
- temporary interruption after execution began;
- self-correction around completion.

---

### B03 — Not Started ↔ Completed

Hard negatives should challenge whether there is evidence of actual completed execution.

Important cases include:

- completion of another task;
- retrospective reference to a different occurrence;
- refusal followed by unrelated completion;
- forgetting followed by unrelated completion;
- inability followed by another completed activity;
- misleading temporal references.

---

## 10. Forbidden Transformations

Reject if:

- distractor becomes dominant execution evidence;
- target Execution Status changes;
- boundary changes;
- hard-negative mechanism disappears;
- example becomes an ordinary prototype;
- competing cue becomes deterministic;
- target task changes;
- target execution evidence is removed;
- example becomes sentiment-only;
- example becomes primarily a Persuasion Barrier;
- example becomes primarily a Dialogue Purpose;
- example becomes primarily a Response Category;
- pragmatic reversal becomes genuinely ambiguous without required context;
- multiple cues make the example impossible to adjudicate consistently.

---

## 11. Acceptance Test

```text
[✓] Same target Execution Status
[✓] Same boundary
[✓] Same hard-negative mechanism
[✓] Competing cue still present
[✓] Target execution evidence remains dominant
[✓] Target task preserved
[✓] Natural language
[✓] No lexical shortcut
[✓] No category/state drift
[✓] No cross-ontology leakage
```

A candidate is accepted only if the misleading surface cue remains genuinely misleading while the correct execution interpretation remains recoverable.

---

## 12. Execution-State Dominance Test

For every hard-negative variant ask:

> **If the potentially misleading cue were ignored, would the remaining execution evidence support the target state?**

Then ask:

> **Does the complete utterance still support the same target state despite the distractor?**

If either answer is no, reject the candidate.

---

## 13. Distractor Strength Audit

Check whether the distractor has crossed the semantic boundary.

```text
Weak
  ↓
Moderate
  ↓
Strong
  ↓
INVALID
```

The final stage must not contain examples where expert annotators could reasonably assign the competing Execution Status solely because the distractor has become too strong.

Hardness must come from resisting a misleading cue, not from genuine annotation ambiguity.

---

## 14. Lexical Shortcut Audit

Audit common execution-status cues:

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

A hard negative should not be solvable by simply detecting or ignoring one keyword.

Where the same keyword appears in different states, its contextual meaning should remain important.

---

## 15. Cross-Ontology Audit

The hard negative must remain an Execution Status resource.

Do not allow:

- emotion;
- sentiment;
- motivation;
- refusal;
- persuasion barrier;
- dialogue purpose;
- response category;
- scheduling;
- deadline status;
- Task Manager operational status

to become the actual classification target.

These may occur naturally as distractors or context, but they must not determine the label.

---

## 16. Leakage

All variants derived from one hard-negative family remain one leakage group.

Retain:

```text
parent_id
lineage_id
boundary_id
hard_negative_type
competing_cue
```

for later evaluation and error analysis.

All descendants must remain together in future train/validation/test splits.

---

## 17. Recommended Metadata

Retain:

```text
example_id
parent_id
lineage_id
boundary_id
resource_type
execution_status
semantic_subtype
hard_negative_type
competing_cue
context
utterance
target_task
variation_type
source
validation_status
ambiguity_flag
```

The `hard_negative_type` should remain stable across descendants unless the variant is intentionally rejected and regenerated under a different mechanism.

---

## 18. Final Principle

> **Stage 3B-C increases linguistic diversity and distractor robustness while preserving the exact Execution Status supported by the underlying execution evidence.**

The objective is not to create arbitrary confusing examples.

It is to ensure that the classifier learns:

```text
Distractor
    ↓
resist surface cue
    ↓
identify actual execution evidence
    ↓
Execution Status
```

rather than:

```text
surface keyword
    ↓
Execution Status
```

The strongest valid hard negatives should therefore challenge lexical and discourse shortcuts while remaining semantically adjudicable under the frozen Execution Status ontology.
