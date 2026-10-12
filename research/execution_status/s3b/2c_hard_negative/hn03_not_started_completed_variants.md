# Stage 3B-C — Hard-Negative Variants: HN03 Not Started ↔ Completed

## Boundary

**Boundary ID:** `B03`  
**State A:** `Not Started`  
**State B:** `Completed`

### Construction Principle

Each variant preserves the parent hard-negative mechanism while changing the linguistic realization of the distractor and decisive execution evidence.

> **Vary the distractor realization, not the execution state.**

The six Stage-2 HN03 parents are retained as lineage families. Each parent receives six variants.

---

## HN03-01 — Competing Temporal Cue

**Parent state:** Not Started  
**Target:** Medication  
**Core diagnostic:** A temporal expectation does not mean execution has begun.

### Variant 01
> “I was meant to take the medication earlier, but I haven't started it.”

### Variant 02
> “I should have taken the medication by now, but I haven't begun.”

### Variant 03
> “The medication was due earlier, but I still haven't taken it.”

### Variant 04
> “I was supposed to take the dose earlier, but I haven't started the medication.”

### Variant 05
> “I expected to have taken it already, but the dose hasn't begun.”

### Variant 06
> “The medication was meant to be taken earlier, but I haven't actually taken it yet.”

**Decisive evidence:** Target execution has not begun.

---

## HN03-02 — Competing Execution-Status Phrase

**Parent state:** Completed  
**Target:** Exercise  
**Core diagnostic:** A statement about one component must not override explicit completion of the defined target routine.

### Variant 01
> “I didn't finish the last exercise separately, but I completed the full exercise routine.”

### Variant 02
> “The final exercise wasn't done on its own, but I completed the complete routine.”

### Variant 03
> “I didn't finish that last movement separately; the full exercise set is already complete.”

### Variant 04
> “That final exercise wasn't completed as a separate step, but I finished the entire routine.”

### Variant 05
> “I didn't do the last exercise by itself, but the full exercise routine was completed.”

### Variant 06
> “The last movement wasn't finished separately, but I completed the whole exercise set.”

**Decisive evidence:** The explicitly defined target routine is complete.

---

## HN03-03 — Misleading Opening Clause

**Parent state:** Completed  
**Target:** Physiotherapy  
**Core diagnostic:** Readiness for a future session does not imply that the current target task is incomplete.

### Variant 01
> “I'm ready for another session, but I already completed today's physiotherapy routine.”

### Variant 02
> “I'm ready to do physio again, but today's routine is already finished.”

### Variant 03
> “I could start another physiotherapy session now, although I already finished today's routine.”

### Variant 04
> “I'm prepared for the next physio session, but I completed the one for today.”

### Variant 05
> “I'm ready for another round of physiotherapy; today's exercises are already done.”

### Variant 06
> “I can do another session whenever needed, but I already completed today's physiotherapy routine.”

**Decisive evidence:** The current target session has already finished.

---

## HN03-04 — Self-Correction

**Parent state:** Completed  
**Target:** Hydration  
**Core diagnostic:** A corrected reference can distinguish the target water from another bottle or hydration instance.

### Variant 01
> “I haven't had the water yet—sorry, I mean the second bottle; I already finished the one for this task.”

### Variant 02
> “I haven't drunk that water—actually, that's the other bottle; I finished the one for this task.”

### Variant 03
> “I thought I hadn't had it yet, but I meant the other bottle; I already finished this task's water.”

### Variant 04
> “I still have water to drink—no, that's for later; I already finished the water assigned to this task.”

### Variant 05
> “I was thinking of the second bottle; the one for this task is already finished.”

### Variant 06
> “No, I haven't had the other bottle yet; I already finished the water for this task.”

**Decisive evidence:** The self-correction identifies the relevant target and establishes completed execution.

---

## HN03-05 — Multiple Competing Cues

**Parent state:** Not Started  
**Target:** Exercise  
**Core diagnostic:** Timing, preparation, and planning remain non-execution evidence.

### Variant 01
> “I was supposed to exercise earlier, got the mat ready, and even planned the first set, but I haven't actually done any of it.”

### Variant 02
> “I meant to start earlier, laid out the equipment, and planned the routine, but I haven't started the exercises.”

### Variant 03
> “I was going to exercise earlier, set everything up, and decided what to do first, but I haven't done the routine.”

### Variant 04
> “The mat is ready, I planned the first set, and I expected to begin earlier, but the exercises haven't started.”

### Variant 05
> “I prepared the space and intended to begin earlier, but I haven't actually done any exercises.”

### Variant 06
> “I got everything ready and planned the routine for earlier, but I still haven't started exercising.”

**Decisive evidence:** No actual exercise execution has begun.

---

## HN03-06 — Strong Conversational Distractor

**Parent state:** Completed  
**Target:** Physiotherapy  
**Core diagnostic:** Post-execution fatigue and future-task discussion must not obscure completion of the current task.

### Variant 01
> “I need to rest after all that effort, and I'm already thinking about tomorrow's routine; today's physiotherapy routine is completely done.”

### Variant 02
> “I'm ready to take it easy now, and I'm thinking about tomorrow's session, but today's physiotherapy routine is finished.”

### Variant 03
> “That routine wore me out, and I need to think about the next session; today's physiotherapy is already complete.”

### Variant 04
> “I need a break after all those exercises, and tomorrow's routine is on my mind; today's session is fully done.”

### Variant 05
> “I'm tired and already planning what I'll do tomorrow, but I've finished today's entire physiotherapy routine.”

### Variant 06
> “I need to recover now and prepare for the next session; the physiotherapy routine for today is completely finished.”

**Decisive evidence:** Today's target physiotherapy execution has finished.

---

## Variant-Level Validation Criteria

Every hard-negative candidate must satisfy:

1. The target task is identifiable.
2. The intended execution state is recoverable from the complete utterance.
3. The parent hard-negative mechanism remains present.
4. The competing cue is plausible but does not determine the execution state by itself.
5. `Not Started` examples contain no evidence that target execution has begun.
6. `Completed` examples contain evidence that target execution has finished.
7. Preparation is not treated as execution.
8. Future intention is not treated as execution.
9. Temporal expectation does not establish execution.
10. A statement about another component, instance, bottle, or future session must not override evidence about the explicitly defined target task.
11. Self-corrections resolve to the final supported execution state.
12. The examples do not depend on motivation, persuasion barriers, dialogue purpose, sentiment, or scheduling.
13. The examples remain natural conversational language.
14. No single lexical item should be sufficient to classify the state reliably.
15. The hard negative must not become genuinely ambiguous.

## Production Metadata

```yaml
boundary_id: B03
resource_type: hard_negative_variant
parent_families: 6
variants_per_family: 6
candidates: 36
states: [Not Started, Completed]
primary_diagnostic: no_execution_vs_finished_execution
lineage_unit: parent_hard_negative
target_tasks: [Medication, Hydration, Exercise, Physiotherapy]
```

## Boundary Invariant

> **Not Started = target execution has not begun.**  
> **Completed = target execution has finished.**

Competing temporal, preparatory, future-oriented, component-level, or conversational cues must not override direct evidence about whether the target task has actually been executed to completion.
