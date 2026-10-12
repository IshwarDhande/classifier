# Stage 3B-C — Hard-Negative Variants: HN02 In Progress ↔ Completed

## Boundary

**Boundary ID:** `B02`  
**State A:** `In Progress`  
**State B:** `Completed`

### Construction Principle

Each variant preserves the parent hard-negative mechanism while changing the linguistic realization of the distractor and the decisive completion evidence.

> **Vary the distractor realization, not the execution state.**

The six Stage-2 HN02 parents are retained as lineage families. Each parent receives six variants.

---

## HN02-01 — Competing Temporal Cue

**Parent state:** Completed  
**Target:** Medication  
**Core diagnostic:** Temporal information does not determine whether execution is finished.

### Variant 01
> “I took the medication earlier today, and it's completely finished.”

### Variant 02
> “I finished the medication this morning; it's all done now.”

### Variant 03
> “The dose was taken earlier, and I've completed it.”

### Variant 04
> “I already took the medication a while ago, and the dose is finished.”

### Variant 05
> “I took the medication before lunch, and there's nothing left to take.”

### Variant 06
> “The medication was taken earlier, and I've finished the full dose.”

**Decisive evidence:** The target medication execution has finished.

---

## HN02-02 — Competing Execution-Status Phrase

**Parent state:** In Progress  
**Target:** Exercise  
**Core diagnostic:** Near-completion or final-step language does not mean execution has finished.

### Variant 01
> “I haven't finished the exercise routine yet; I'm still on the last exercise.”

### Variant 02
> “I'm nearly done with the routine, but I'm still doing the final exercise.”

### Variant 03
> “I've reached the last exercise, and I haven't finished the routine yet.”

### Variant 04
> “There's only one exercise left, so I'm close to done, but I'm still working on it.”

### Variant 05
> “I'm at the end of the exercise routine, but I still have the final exercise to finish.”

### Variant 06
> “Most of the routine is complete, but I'm still doing the last exercise.”

**Decisive evidence:** Execution has begun and remains unfinished.

---

## HN02-03 — Misleading Opening Clause

**Parent state:** Completed  
**Target:** Physiotherapy  
**Core diagnostic:** A current physical state does not imply that the target execution is still ongoing.

### Variant 01
> “I'm still tired from the physiotherapy routine, but I finished the whole thing.”

### Variant 02
> “My legs are still sore from physio, but I completed the entire routine.”

### Variant 03
> “I still feel the effects of the physiotherapy, although the routine is already finished.”

### Variant 04
> “I'm still feeling tired after physio, but I completed all the exercises.”

### Variant 05
> “My body is still worn out from the routine, but I've finished the full session.”

### Variant 06
> “I still feel tired from doing the exercises, but the physiotherapy routine is done.”

**Decisive evidence:** The physiotherapy execution has finished; the physical after-effect is not ongoing execution.

---

## HN02-04 — Self-Correction

**Parent state:** Completed  
**Target:** Hydration  
**Core diagnostic:** A later correction can resolve an apparent remaining-work cue.

### Variant 01
> “I still have some water to drink—no, that's from another bottle; I finished the one for this task.”

### Variant 02
> “I thought I still had some water left, but that's a different bottle; I've finished the task bottle.”

### Variant 03
> “There's still water here—actually, that's for later; I already finished the water for this task.”

### Variant 04
> “I still have a bottle with water in it—wait, that's not the one I was supposed to drink; I finished mine.”

### Variant 05
> “I was about to say I had some left, but I checked the bottle and realized I had already finished the task amount.”

### Variant 06
> “I still have water beside me—no, that's separate; I finished the water I needed for this task.”

**Decisive evidence:** The correction establishes that the target hydration task is complete.

---

## HN02-05 — Multiple Competing Cues

**Parent state:** In Progress  
**Target:** Exercise  
**Core diagnostic:** Extensive progress, temporal wording, and near-completion language do not establish completion when work remains.

### Variant 01
> “I did most of the exercises earlier, I'm almost there, but I still have one exercise left to complete.”

### Variant 02
> “I've finished nearly the whole routine, and I started earlier, but there's still one exercise left.”

### Variant 03
> “Most of it is done and I'm close to the end, but I'm still working through the final exercise.”

### Variant 04
> “I got through almost everything earlier, but one exercise remains, so the routine isn't finished yet.”

### Variant 05
> “I'm nearly done after completing most of the exercises, but I still have the last one to do.”

### Variant 06
> “I completed almost the entire set earlier, but there's one exercise I haven't finished.”

**Decisive evidence:** At least one target exercise remains, so execution is unfinished.

---

## HN02-06 — Strong Conversational Distractor

**Parent state:** Completed  
**Target:** Physiotherapy  
**Core diagnostic:** Fatigue, recovery, and subsequent needs must not obscure explicit completion.

### Variant 01
> “My legs are tired and I need to rest now; I finished the entire physiotherapy routine.”

### Variant 02
> “I'm exhausted and need to sit down for a while, but I completed the full physiotherapy routine.”

### Variant 03
> “I need to rest after that session because my legs are tired; the whole routine is already done.”

### Variant 04
> “My legs are worn out, and I don't want to do anything else right now; I finished all the physiotherapy exercises.”

### Variant 05
> “I'm feeling the strain and need some recovery time, but I've completed the entire routine.”

### Variant 06
> “I need to take a break now because I'm tired; the physiotherapy session itself is finished.”

**Decisive evidence:** The entire physiotherapy execution has finished; the surrounding fatigue and recovery statements are post-execution context.

---

## Variant-Level Validation Criteria

Every hard-negative candidate must satisfy:

1. The target task is identifiable.
2. The intended execution state is recoverable from the complete utterance.
3. The parent hard-negative mechanism remains present.
4. The competing cue is plausible but does not determine the execution state by itself.
5. `In Progress` examples establish begun but unfinished execution.
6. `Completed` examples establish finished execution.
7. “Almost,” “nearly,” “last,” and similar progress cues do not count as completion when work remains.
8. Temporal expressions do not determine completion by themselves.
9. Physical after-effects do not imply that execution is still ongoing.
10. Self-corrections resolve to the final supported execution state.
11. The examples do not depend on motivation, persuasion barriers, dialogue purpose, sentiment, or scheduling.
12. The examples remain natural conversational language.
13. No single lexical item should be sufficient to classify the state reliably.
14. The hard negative must not become genuinely ambiguous.

## Production Metadata

```yaml
boundary_id: B02
resource_type: hard_negative_variant
parent_families: 6
variants_per_family: 6
candidates: 36
states: [In Progress, Completed]
primary_diagnostic: execution_completion
lineage_unit: parent_hard_negative
target_tasks: [Medication, Hydration, Exercise, Physiotherapy]
```

## Boundary Invariant

> **In Progress = execution has begun but remains unfinished.**  
> **Completed = execution has finished.**

Competing temporal, progress-related, conversational, physical-state, or contextual cues must not override direct evidence about whether the target execution has actually finished.
