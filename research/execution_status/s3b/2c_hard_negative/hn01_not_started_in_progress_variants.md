# Stage 3B-C — Hard-Negative Variants: HN01 Not Started ↔ In Progress

## Boundary

**Boundary ID:** `B01`  
**State A:** `Not Started`  
**State B:** `In Progress`

### Construction Principle

Each variant preserves the parent hard-negative mechanism while changing the linguistic realization of the distractor and execution evidence.

> **Vary the distractor realization, not the execution state.**

The six Stage-2 HN01 parents are retained as lineage families. Each parent receives six variants.

---

## HN01-01 — Competing Temporal Cue

**Parent state:** Not Started  
**Target:** Medication  
**Core diagnostic:** A temporal expectation does not mean execution has begun.

### Variant 01
> “I was meant to take the medication earlier, but I still haven't started it.”

### Variant 02
> “I should have taken the medication by now, but I haven't begun the dose.”

### Variant 03
> “It was supposed to be done earlier; I haven't actually taken the medication yet.”

### Variant 04
> “I was due to take it earlier, but the medication is still untouched.”

### Variant 05
> “I expected to have taken the medication already, but I haven't started taking it.”

### Variant 06
> “The dose was supposed to happen earlier, but I still haven't taken it.”

**Decisive evidence:** No execution has begun.

---

## HN01-02 — Competing Execution-Status Phrase

**Parent state:** In Progress  
**Target:** Exercise  
**Core diagnostic:** Incomplete wording must not be confused with absence of execution.

### Variant 01
> “I haven't finished the exercises yet because I'm still doing them.”

### Variant 02
> “The exercises aren't finished, but I'm working through them now.”

### Variant 03
> “I'm not done with the exercises yet; I've already started them.”

### Variant 04
> “I still have exercises left, and I'm doing them now.”

### Variant 05
> “The routine isn't complete yet because I'm still going through it.”

### Variant 06
> “I haven't completed the set, but I'm partway through the exercises.”

**Decisive evidence:** Execution has begun and remains unfinished.

---

## HN01-03 — Misleading Opening Clause

**Parent state:** Not Started  
**Target:** Physiotherapy  
**Core diagnostic:** Readiness or preparation does not constitute execution.

### Variant 01
> “I'm ready to do the physiotherapy routine, but I haven't started it yet.”

### Variant 02
> “Everything is ready for physio, though I haven't begun the routine.”

### Variant 03
> “I'm set up for the physiotherapy exercises, but I haven't actually started.”

### Variant 04
> “I've got everything ready for the routine; none of the exercises have begun.”

### Variant 05
> “I'm all set to start physiotherapy, but I haven't done any of it yet.”

### Variant 06
> “The routine is ready to go, but I haven't started working through it.”

**Decisive evidence:** Preparation is present, but execution has not begun.

---

## HN01-04 — Self-Correction

**Parent state:** In Progress  
**Target:** Hydration  
**Core diagnostic:** A later self-correction overrides an earlier mistaken or incomplete statement.

### Variant 01
> “I haven't started drinking it—actually, I have; I'm halfway through the bottle.”

### Variant 02
> “I was about to say I hadn't started, but I have; I'm already drinking it.”

### Variant 03
> “No, that's not right—I have started drinking the water, and there's still some left.”

### Variant 04
> “I thought I hadn't started, but I have; I'm partway through the bottle now.”

### Variant 05
> “I haven't started it—well, actually, I did; I'm still drinking the water.”

### Variant 06
> “At first I thought I hadn't begun, but I have; I'm not finished with the bottle yet.”

**Decisive evidence:** The corrected statement establishes that execution is underway and unfinished.

---

## HN01-05 — Multiple Competing Cues

**Parent state:** Not Started  
**Target:** Exercise  
**Core diagnostic:** Several execution-adjacent cues still do not establish begun execution.

### Variant 01
> “I was getting ready earlier, laid out the mat, and planned to start, but I still haven't begun the exercises.”

### Variant 02
> “I cleared some space, put the equipment out, and was ready earlier, but I haven't done the exercises.”

### Variant 03
> “The mat is out, my shoes are on, and I was preparing to start, but the exercises haven't begun.”

### Variant 04
> “I set everything up earlier and even got into position, but I haven't actually started the routine.”

### Variant 05
> “Everything is prepared, and I was going to start earlier, but I still haven't done any of the exercises.”

### Variant 06
> “I got the equipment ready and was about to begin, but I haven't started the exercise routine.”

**Decisive evidence:** Preparation, intention, and temporal cues do not establish actual execution.

---

## HN01-06 — Strong Conversational Distractor

**Parent state:** In Progress  
**Target:** Physiotherapy  
**Core diagnostic:** Duration, consequences, expectations, or surrounding conversation must not obscure active execution.

### Variant 01
> “The routine is taking longer than I expected, and I need to finish it before I can relax; I'm still working through the exercises.”

### Variant 02
> “This is taking up more time than I planned, and I still have things to do afterward; I'm continuing the physiotherapy routine now.”

### Variant 03
> “I thought I'd be finished by now, and I need to get on with the rest of my day, but I'm still doing the exercises.”

### Variant 04
> “It's been a longer routine than I expected, and I have somewhere to be later; I'm still going through the physiotherapy exercises.”

### Variant 05
> “I was hoping to be done already because I have other things to handle, but I'm still working through the routine.”

### Variant 06
> “The routine is taking longer than I wanted, and I need to move on afterward; I'm still in the middle of the exercises.”

**Decisive evidence:** Execution is currently underway and unfinished.

---

## Variant-Level Validation Criteria

Every hard-negative candidate must satisfy:

1. The target task is identifiable.
2. The intended execution state is recoverable from the complete utterance.
3. The parent hard-negative mechanism remains present.
4. The competing cue is plausible but does not determine the execution state by itself.
5. `Not Started` examples contain no actual target-task execution.
6. `In Progress` examples establish that execution has begun and remains unfinished.
7. Preparation, readiness, intention, and temporal expectation are not treated as execution.
8. Self-corrections resolve to the final supported execution state.
9. The examples do not depend on motivation, persuasion barriers, dialogue purpose, or sentiment.
10. The examples do not require scheduling or task-manager reasoning.
11. The examples remain natural conversational language.
12. No single lexical item should be sufficient to classify the state reliably.

## Production Metadata

```yaml
boundary_id: B01
resource_type: hard_negative_variant
parent_families: 6
variants_per_family: 6
candidates: 36
states: [Not Started, In Progress]
primary_diagnostic: execution_initiation
lineage_unit: parent_hard_negative
target_tasks: [Medication, Hydration, Exercise, Physiotherapy]
```

## Boundary Invariant

> **Not Started = execution has not begun.**  
> **In Progress = execution has begun but remains unfinished.**

Competing temporal, preparatory, conversational, or status-related cues must not override the actual execution evidence.
