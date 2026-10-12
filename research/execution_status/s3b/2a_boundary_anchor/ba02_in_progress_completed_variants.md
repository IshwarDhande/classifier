# BA02 — In Progress ↔ Completed Boundary Anchor Variants

## Boundary

`B02 — In Progress ↔ Completed`

**Diagnostic:** Has execution of the target task actually finished?

Variants preserve the parent anchor's execution position while varying only its linguistic realization.

## Production Records

```yaml
example_id: BA02-01
pair_id: B02
parent_id: BA02-01
lineage_id: BA02-01
execution_status: In Progress
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: A Prototype
context: "The user is currently taking the target medication."
utterance: "The medication is being taken now, but I haven't finished the dose yet."
target_task: Medication
closest_competing_state: Completed
variation_type: LEX
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-02
pair_id: B02
parent_id: BA02-01
lineage_id: BA02-01
execution_status: In Progress
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: A Prototype
context: "The user is currently taking the target medication."
utterance: "I'm still taking the medication; the dose isn't finished yet."
target_task: Medication
closest_competing_state: Completed
variation_type: SYN
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-03
pair_id: B02
parent_id: BA02-01
lineage_id: BA02-01
execution_status: In Progress
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: A Prototype
context: "The user is currently taking the target medication."
utterance: "I'm in the middle of taking it—I haven't finished yet."
target_task: Medication
closest_competing_state: Completed
variation_type: NAT
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-04
pair_id: B02
parent_id: BA02-01
lineage_id: BA02-01
execution_status: In Progress
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: A Prototype
context: "The user is currently taking the target medication."
utterance: "I've started taking the medication, and there's still some left to take."
target_task: Medication
closest_competing_state: Completed
variation_type: EXP
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-05
pair_id: B02
parent_id: BA02-01
lineage_id: BA02-01
execution_status: In Progress
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: A Prototype
context: "The user is currently taking the target medication."
utterance: "I'm partway through the dose and will finish it shortly."
target_task: Medication
closest_competing_state: Completed
variation_type: PRG
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-06
pair_id: B02
parent_id: BA02-01
lineage_id: BA02-01
execution_status: In Progress
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: A Prototype
context: "The user is currently taking the target medication."
utterance: "I'm taking it now; give me a moment, I'm not finished yet."
target_task: Medication
closest_competing_state: Completed
variation_type: CMK
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-07
pair_id: B02
parent_id: BA02-02
lineage_id: BA02-02
execution_status: Completed
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: B Prototype
context: "The user reports the target medication after the dose has been fully taken."
utterance: "I finished taking the medication."
target_task: Medication
closest_competing_state: In Progress
variation_type: LEX
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-08
pair_id: B02
parent_id: BA02-02
lineage_id: BA02-02
execution_status: Completed
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: B Prototype
context: "The user reports the target medication after the dose has been fully taken."
utterance: "The medication has been taken in full."
target_task: Medication
closest_competing_state: In Progress
variation_type: SYN
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-09
pair_id: B02
parent_id: BA02-02
lineage_id: BA02-02
execution_status: Completed
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: B Prototype
context: "The user reports the target medication after the dose has been fully taken."
utterance: "That's done—I took the whole dose."
target_task: Medication
closest_competing_state: In Progress
variation_type: NAT
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-10
pair_id: B02
parent_id: BA02-02
lineage_id: BA02-02
execution_status: Completed
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: B Prototype
context: "The user reports the target medication after the dose has been fully taken."
utterance: "I took the medication completely, so there's nothing left to take."
target_task: Medication
closest_competing_state: In Progress
variation_type: EXP
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-11
pair_id: B02
parent_id: BA02-02
lineage_id: BA02-02
execution_status: Completed
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: B Prototype
context: "The user reports the target medication after the dose has been fully taken."
utterance: "I've finished the dose and am done with the medication for now."
target_task: Medication
closest_competing_state: In Progress
variation_type: PRG
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-12
pair_id: B02
parent_id: BA02-02
lineage_id: BA02-02
execution_status: Completed
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: B Prototype
context: "The user reports the target medication after the dose has been fully taken."
utterance: "Yep, I took it all already."
target_task: Medication
closest_competing_state: In Progress
variation_type: CMK
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-13
pair_id: B02
parent_id: BA02-03
lineage_id: BA02-03
execution_status: In Progress
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: A-Leaning Boundary
context: "The user is near the end of the exercise routine but has not completed it."
utterance: "I've started the exercises, but I still have the last few to do."
target_task: Exercise
closest_competing_state: Completed
variation_type: LEX
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-14
pair_id: B02
parent_id: BA02-03
lineage_id: BA02-03
execution_status: In Progress
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: A-Leaning Boundary
context: "The user is near the end of the exercise routine but has not completed it."
utterance: "The exercise routine is underway; I haven't worked through all of it yet."
target_task: Exercise
closest_competing_state: Completed
variation_type: SYN
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-15
pair_id: B02
parent_id: BA02-03
lineage_id: BA02-03
execution_status: In Progress
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: A-Leaning Boundary
context: "The user is near the end of the exercise routine but has not completed it."
utterance: "I'm on the final few exercises, so I'm not quite through the routine."
target_task: Exercise
closest_competing_state: Completed
variation_type: NAT
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-16
pair_id: B02
parent_id: BA02-03
lineage_id: BA02-03
execution_status: In Progress
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: A-Leaning Boundary
context: "The user is near the end of the exercise routine but has not completed it."
utterance: "I've already worked through most of the routine, with a small part still remaining."
target_task: Exercise
closest_competing_state: Completed
variation_type: EXP
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-17
pair_id: B02
parent_id: BA02-03
lineage_id: BA02-03
execution_status: In Progress
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: A-Leaning Boundary
context: "The user is near the end of the exercise routine but has not completed it."
utterance: "I'm wrapping up the last exercises, but they're not all done yet."
target_task: Exercise
closest_competing_state: Completed
variation_type: PRG
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-18
pair_id: B02
parent_id: BA02-03
lineage_id: BA02-03
execution_status: In Progress
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: A-Leaning Boundary
context: "The user is near the end of the exercise routine but has not completed it."
utterance: "I'm nearly through the routine—just a few exercises are still left."
target_task: Exercise
closest_competing_state: Completed
variation_type: CMK
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-19
pair_id: B02
parent_id: BA02-04
lineage_id: BA02-04
execution_status: Completed
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: B-Leaning Boundary
context: "The user reports the exercise routine after every exercise has been performed."
utterance: "I've worked through the entire exercise routine."
target_task: Exercise
closest_competing_state: In Progress
variation_type: LEX
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-20
pair_id: B02
parent_id: BA02-04
lineage_id: BA02-04
execution_status: Completed
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: B-Leaning Boundary
context: "The user reports the exercise routine after every exercise has been performed."
utterance: "All of the exercises have been completed."
target_task: Exercise
closest_competing_state: In Progress
variation_type: SYN
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-21
pair_id: B02
parent_id: BA02-04
lineage_id: BA02-04
execution_status: Completed
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: B-Leaning Boundary
context: "The user reports the exercise routine after every exercise has been performed."
utterance: "I'm through the whole routine now."
target_task: Exercise
closest_competing_state: In Progress
variation_type: NAT
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-22
pair_id: B02
parent_id: BA02-04
lineage_id: BA02-04
execution_status: Completed
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: B-Leaning Boundary
context: "The user reports the exercise routine after every exercise has been performed."
utterance: "I went through every exercise in the routine, with none remaining."
target_task: Exercise
closest_competing_state: In Progress
variation_type: EXP
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-23
pair_id: B02
parent_id: BA02-04
lineage_id: BA02-04
execution_status: Completed
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: B-Leaning Boundary
context: "The user reports the exercise routine after every exercise has been performed."
utterance: "The routine is wrapped up; I've done every exercise."
target_task: Exercise
closest_competing_state: In Progress
variation_type: PRG
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-24
pair_id: B02
parent_id: BA02-04
lineage_id: BA02-04
execution_status: Completed
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: B-Leaning Boundary
context: "The user reports the exercise routine after every exercise has been performed."
utterance: "That's the whole routine finished—I got through all of it."
target_task: Exercise
closest_competing_state: In Progress
variation_type: CMK
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-25
pair_id: B02
parent_id: BA02-05
lineage_id: BA02-05
execution_status: In Progress
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: Implicit A
context: "The user has already consumed part of the target hydration amount."
utterance: "I've had some water already, but I still need to drink the rest of this bottle."
target_task: Hydration
closest_competing_state: Completed
variation_type: LEX
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-26
pair_id: B02
parent_id: BA02-05
lineage_id: BA02-05
execution_status: In Progress
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: Implicit A
context: "The user has already consumed part of the target hydration amount."
utterance: "The bottle is partly emptied; I haven't finished drinking it yet."
target_task: Hydration
closest_competing_state: Completed
variation_type: SYN
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-27
pair_id: B02
parent_id: BA02-05
lineage_id: BA02-05
execution_status: In Progress
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: Implicit A
context: "The user has already consumed part of the target hydration amount."
utterance: "I've had some of it, and there's still quite a bit left."
target_task: Hydration
closest_competing_state: Completed
variation_type: NAT
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-28
pair_id: B02
parent_id: BA02-05
lineage_id: BA02-05
execution_status: In Progress
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: Implicit A
context: "The user has already consumed part of the target hydration amount."
utterance: "The water level has gone down, but there is still water left in the bottle."
target_task: Hydration
closest_competing_state: Completed
variation_type: EXP
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-29
pair_id: B02
parent_id: BA02-05
lineage_id: BA02-05
execution_status: In Progress
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: Implicit A
context: "The user has already consumed part of the target hydration amount."
utterance: "I'm partway through the bottle and will finish the remaining water next."
target_task: Hydration
closest_competing_state: Completed
variation_type: PRG
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-30
pair_id: B02
parent_id: BA02-05
lineage_id: BA02-05
execution_status: In Progress
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: Implicit A
context: "The user has already consumed part of the target hydration amount."
utterance: "I've already had some, but I'm not through the bottle yet."
target_task: Hydration
closest_competing_state: Completed
variation_type: CMK
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-31
pair_id: B02
parent_id: BA02-06
lineage_id: BA02-06
execution_status: Completed
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: Implicit B
context: "The user reports the physiotherapy routine after all required exercises have been performed."
utterance: "There are no exercises left in my physiotherapy routine."
target_task: Physiotherapy
closest_competing_state: In Progress
variation_type: LEX
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-32
pair_id: B02
parent_id: BA02-06
lineage_id: BA02-06
execution_status: Completed
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: Implicit B
context: "The user reports the physiotherapy routine after all required exercises have been performed."
utterance: "I've gone through the full physiotherapy routine; nothing remains."
target_task: Physiotherapy
closest_competing_state: In Progress
variation_type: SYN
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-33
pair_id: B02
parent_id: BA02-06
lineage_id: BA02-06
execution_status: Completed
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: Implicit B
context: "The user reports the physiotherapy routine after all required exercises have been performed."
utterance: "I'm through the whole physio routine now."
target_task: Physiotherapy
closest_competing_state: In Progress
variation_type: NAT
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-34
pair_id: B02
parent_id: BA02-06
lineage_id: BA02-06
execution_status: Completed
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: Implicit B
context: "The user reports the physiotherapy routine after all required exercises have been performed."
utterance: "I worked through every exercise in the routine, so there is nothing left to do."
target_task: Physiotherapy
closest_competing_state: In Progress
variation_type: EXP
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-35
pair_id: B02
parent_id: BA02-06
lineage_id: BA02-06
execution_status: Completed
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: Implicit B
context: "The user reports the physiotherapy routine after all required exercises have been performed."
utterance: "The routine is wrapped up—I completed all the exercises."
target_task: Physiotherapy
closest_competing_state: In Progress
variation_type: PRG
source: constructed
validation_status: candidate
ambiguity_flag: false
```

```yaml
example_id: BA02-36
pair_id: B02
parent_id: BA02-06
lineage_id: BA02-06
execution_status: Completed
semantic_subtype: boundary_anchor
stage: 3B-A
resource_type: boundary_anchor_variant
boundary_id: B02
anchor_type: Implicit B
context: "The user reports the physiotherapy routine after all required exercises have been performed."
utterance: "All done with the physio routine; I don't have any exercises left."
target_task: Physiotherapy
closest_competing_state: In Progress
variation_type: CMK
source: constructed
validation_status: candidate
ambiguity_flag: false
```

## Boundary Invariant

- **In Progress:** execution has begun and remains unfinished.
- **Completed:** execution has finished.
- Near-completion language remains In Progress when any required execution remains.
- Completion is established by completed execution, not merely by elapsed time, intention, or confidence.
- Variants must not introduce planning, scheduling, motivation, or barrier information as the basis for the label.