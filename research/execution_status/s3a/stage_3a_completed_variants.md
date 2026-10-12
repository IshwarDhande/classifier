# Execution Status Dataset — Stage 3A Linguistic Expansion: Completed

## 1. Scope

This resource contains Stage 3A linguistic expansions for the frozen `Completed` execution status. Each variant is a new natural-language realization of an existing Stage 1 semantic scenario and preserves the scenario's completion semantics.

```yaml
execution_status: Completed
execution_started: true
execution_completed: true
```

Stage 3A does not introduce new semantic scenarios. The target-task domain, semantic subtype, execution condition, and underlying scenario remain fixed within each lineage.

## 2. Semantic Invariants

Every variant in this resource must preserve all of the following:

- execution has occurred;
- the target task has reached completion;
- the assigned semantic subtype remains unchanged;
- the assigned scenario remains unchanged;
- the target task remains within the frozen task-domain space;
- linguistic variation does not alter the execution status;
- additional commentary, timing information, or contextual detail must not reverse the completion state.

## 3. Standard Variant Types

| Code | Variant type | Construction role |
|---|---|---|
| V01 | LEX | Lexical variation |
| V02 | SYN | Syntactic variation |
| V03 | NAT | Natural conversational phrasing |
| V04 | EXP | Explicit semantic realization |
| V05 | PRG | Pragmatic/discourse variation |
| V06 | DSC | Discourse/contextual variation |

These six variant types constitute the standard Stage 3A expansion set for `Completed` scenarios.

## 4. Production Record Schema

```yaml
example_id:
lineage_id:
scenario_id:
subtype_id:
anchor_id:
variant_id:
variant_type:
task_domain:
utterance:
execution_status: Completed
validation_status: candidate
```

`validation_status: candidate` identifies a Stage 3A construction artifact awaiting dataset validation; it is not an execution-status label.

## 5. Linguistic Construction Rules

1. Do not create a new execution scenario during paraphrasing.
2. Preserve evidence that the target task has actually been completed.
3. Do not weaken completion into ongoing or partial execution.
4. Do not introduce an unfinished remainder.
5. Do not rely on a single completion keyword as the sole semantic signal.
6. Retrospective wording must still establish that completion occurred.
7. Indirect completion variants must provide evidence that supports completed execution rather than merely preparation.
8. Multi-step completion variants must indicate that all required steps have been completed.
9. Additional commentary may describe circumstances, feelings, timing, or consequences, but must not negate completion.
10. Do not introduce persuasion barriers, response categories, dialogue purposes, scheduling status, or task-manager states as replacement semantics.

---

## C-S01 — C-01 Direct Completion

### Scenario

The user explicitly states that the required medication task has been completed.

### Target task domain

Medication

### Stage 1 anchors

- **A1:** I took my medication.
- **A2:** I’ve finished taking my medicine.
- **A3:** The medication is done.

### Semantic invariant

The target task has been executed and is complete.

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I took my medication. |
| A1 | V02 | SYN | My medication has been taken. |
| A1 | V03 | NAT | I’ve taken it already. |
| A1 | V04 | EXP | I’ve completed the medication task; I took the medicine. |
| A1 | V05 | PRG | The medication is finished for this task. |
| A1 | V06 | DSC | That’s done—I’ve taken my medicine. |
| A2 | V01 | LEX | I took the medicine. |
| A2 | V02 | SYN | To be honest, my medication has been taken. |
| A2 | V03 | NAT | Basically, i’ve taken it already. |
| A2 | V04 | EXP | Actually, i’ve completed the medication task; I took the medicine. |
| A2 | V05 | PRG | Right, the medication is finished for this task. |
| A2 | V06 | DSC | That’s done—I’ve taken the medication. |
| A3 | V01 | LEX | You know, i took my medication. |
| A3 | V02 | SYN | Okay, my medication has been taken. |
| A3 | V03 | NAT | Actually, i’ve taken it already. |
| A3 | V04 | EXP | I’ve completed my dose task; I took my dose. |
| A3 | V05 | PRG | Listen, the medication is finished for this task. |
| A3 | V06 | DSC | Right, that’s done—I’ve taken my medicine. |

### Production records

```yaml
example_id: C3A-01-A1-V01
lineage_id: C-S01-A1
scenario_id: C-S01
subtype_id: C-01
anchor_id: C-S01-A1
variant_id: V01
variant_type: LEX
task_domain: Medication
utterance: "I took my medication."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-01-A1-V02
lineage_id: C-S01-A1
scenario_id: C-S01
subtype_id: C-01
anchor_id: C-S01-A1
variant_id: V02
variant_type: SYN
task_domain: Medication
utterance: "My medication has been taken."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-01-A1-V03
lineage_id: C-S01-A1
scenario_id: C-S01
subtype_id: C-01
anchor_id: C-S01-A1
variant_id: V03
variant_type: NAT
task_domain: Medication
utterance: "I’ve taken it already."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-01-A1-V04
lineage_id: C-S01-A1
scenario_id: C-S01
subtype_id: C-01
anchor_id: C-S01-A1
variant_id: V04
variant_type: EXP
task_domain: Medication
utterance: "I’ve completed the medication task; I took the medicine."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-01-A1-V05
lineage_id: C-S01-A1
scenario_id: C-S01
subtype_id: C-01
anchor_id: C-S01-A1
variant_id: V05
variant_type: PRG
task_domain: Medication
utterance: "The medication is finished for this task."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-01-A1-V06
lineage_id: C-S01-A1
scenario_id: C-S01
subtype_id: C-01
anchor_id: C-S01-A1
variant_id: V06
variant_type: DSC
task_domain: Medication
utterance: "That’s done—I’ve taken my medicine."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-01-A2-V01
lineage_id: C-S01-A2
scenario_id: C-S01
subtype_id: C-01
anchor_id: C-S01-A2
variant_id: V01
variant_type: LEX
task_domain: Medication
utterance: "I took the medicine."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-01-A2-V02
lineage_id: C-S01-A2
scenario_id: C-S01
subtype_id: C-01
anchor_id: C-S01-A2
variant_id: V02
variant_type: SYN
task_domain: Medication
utterance: "To be honest, my medication has been taken."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-01-A2-V03
lineage_id: C-S01-A2
scenario_id: C-S01
subtype_id: C-01
anchor_id: C-S01-A2
variant_id: V03
variant_type: NAT
task_domain: Medication
utterance: "Basically, i’ve taken it already."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-01-A2-V04
lineage_id: C-S01-A2
scenario_id: C-S01
subtype_id: C-01
anchor_id: C-S01-A2
variant_id: V04
variant_type: EXP
task_domain: Medication
utterance: "Actually, i’ve completed the medication task; I took the medicine."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-01-A2-V05
lineage_id: C-S01-A2
scenario_id: C-S01
subtype_id: C-01
anchor_id: C-S01-A2
variant_id: V05
variant_type: PRG
task_domain: Medication
utterance: "Right, the medication is finished for this task."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-01-A2-V06
lineage_id: C-S01-A2
scenario_id: C-S01
subtype_id: C-01
anchor_id: C-S01-A2
variant_id: V06
variant_type: DSC
task_domain: Medication
utterance: "That’s done—I’ve taken the medication."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-01-A3-V01
lineage_id: C-S01-A3
scenario_id: C-S01
subtype_id: C-01
anchor_id: C-S01-A3
variant_id: V01
variant_type: LEX
task_domain: Medication
utterance: "You know, i took my medication."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-01-A3-V02
lineage_id: C-S01-A3
scenario_id: C-S01
subtype_id: C-01
anchor_id: C-S01-A3
variant_id: V02
variant_type: SYN
task_domain: Medication
utterance: "Okay, my medication has been taken."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-01-A3-V03
lineage_id: C-S01-A3
scenario_id: C-S01
subtype_id: C-01
anchor_id: C-S01-A3
variant_id: V03
variant_type: NAT
task_domain: Medication
utterance: "Actually, i’ve taken it already."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-01-A3-V04
lineage_id: C-S01-A3
scenario_id: C-S01
subtype_id: C-01
anchor_id: C-S01-A3
variant_id: V04
variant_type: EXP
task_domain: Medication
utterance: "I’ve completed my dose task; I took my dose."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-01-A3-V05
lineage_id: C-S01-A3
scenario_id: C-S01
subtype_id: C-01
anchor_id: C-S01-A3
variant_id: V05
variant_type: PRG
task_domain: Medication
utterance: "Listen, the medication is finished for this task."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-01-A3-V06
lineage_id: C-S01-A3
scenario_id: C-S01
subtype_id: C-01
anchor_id: C-S01-A3
variant_id: V06
variant_type: DSC
task_domain: Medication
utterance: "Right, that’s done—I’ve taken my medicine."
execution_status: Completed
validation_status: candidate
```

## C-S02 — C-01 Direct Completion

### Scenario

The user explicitly states that the required hydration task has been completed.

### Target task domain

Hydration

### Stage 1 anchors

- **A1:** I drank the water.
- **A2:** I’ve finished my water.
- **A3:** The water is done.

### Semantic invariant

The target task has been executed and is complete.

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I drank the water. |
| A1 | V02 | SYN | The water has been finished. |
| A1 | V03 | NAT | I’ve had the water already. |
| A1 | V04 | EXP | I’ve completed the hydration task and finished the water. |
| A1 | V05 | PRG | My water intake for this task is finished. |
| A1 | V06 | DSC | That’s done—I’ve finished the water. |
| A2 | V01 | LEX | I drank the bottle. |
| A2 | V02 | SYN | As I said, the water has been finished. |
| A2 | V03 | NAT | I’ve had the bottle already. |
| A2 | V04 | EXP | I’ve completed the hydration task and finished the bottle. |
| A2 | V05 | PRG | The bottle intake for this task is finished. |
| A2 | V06 | DSC | That’s done—I’ve finished the bottle. |
| A3 | V01 | LEX | I drank the required water. |
| A3 | V02 | SYN | Look, the water has been finished. |
| A3 | V03 | NAT | I’ve had the required water already. |
| A3 | V04 | EXP | I’ve completed the hydration task and finished the required water. |
| A3 | V05 | PRG | Look, my water intake for this task is finished. |
| A3 | V06 | DSC | That’s done—I’ve finished the required water. |

### Production records

```yaml
example_id: C3A-02-A1-V01
lineage_id: C-S02-A1
scenario_id: C-S02
subtype_id: C-01
anchor_id: C-S02-A1
variant_id: V01
variant_type: LEX
task_domain: Hydration
utterance: "I drank the water."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-02-A1-V02
lineage_id: C-S02-A1
scenario_id: C-S02
subtype_id: C-01
anchor_id: C-S02-A1
variant_id: V02
variant_type: SYN
task_domain: Hydration
utterance: "The water has been finished."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-02-A1-V03
lineage_id: C-S02-A1
scenario_id: C-S02
subtype_id: C-01
anchor_id: C-S02-A1
variant_id: V03
variant_type: NAT
task_domain: Hydration
utterance: "I’ve had the water already."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-02-A1-V04
lineage_id: C-S02-A1
scenario_id: C-S02
subtype_id: C-01
anchor_id: C-S02-A1
variant_id: V04
variant_type: EXP
task_domain: Hydration
utterance: "I’ve completed the hydration task and finished the water."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-02-A1-V05
lineage_id: C-S02-A1
scenario_id: C-S02
subtype_id: C-01
anchor_id: C-S02-A1
variant_id: V05
variant_type: PRG
task_domain: Hydration
utterance: "My water intake for this task is finished."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-02-A1-V06
lineage_id: C-S02-A1
scenario_id: C-S02
subtype_id: C-01
anchor_id: C-S02-A1
variant_id: V06
variant_type: DSC
task_domain: Hydration
utterance: "That’s done—I’ve finished the water."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-02-A2-V01
lineage_id: C-S02-A2
scenario_id: C-S02
subtype_id: C-01
anchor_id: C-S02-A2
variant_id: V01
variant_type: LEX
task_domain: Hydration
utterance: "I drank the bottle."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-02-A2-V02
lineage_id: C-S02-A2
scenario_id: C-S02
subtype_id: C-01
anchor_id: C-S02-A2
variant_id: V02
variant_type: SYN
task_domain: Hydration
utterance: "As I said, the water has been finished."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-02-A2-V03
lineage_id: C-S02-A2
scenario_id: C-S02
subtype_id: C-01
anchor_id: C-S02-A2
variant_id: V03
variant_type: NAT
task_domain: Hydration
utterance: "I’ve had the bottle already."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-02-A2-V04
lineage_id: C-S02-A2
scenario_id: C-S02
subtype_id: C-01
anchor_id: C-S02-A2
variant_id: V04
variant_type: EXP
task_domain: Hydration
utterance: "I’ve completed the hydration task and finished the bottle."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-02-A2-V05
lineage_id: C-S02-A2
scenario_id: C-S02
subtype_id: C-01
anchor_id: C-S02-A2
variant_id: V05
variant_type: PRG
task_domain: Hydration
utterance: "The bottle intake for this task is finished."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-02-A2-V06
lineage_id: C-S02-A2
scenario_id: C-S02
subtype_id: C-01
anchor_id: C-S02-A2
variant_id: V06
variant_type: DSC
task_domain: Hydration
utterance: "That’s done—I’ve finished the bottle."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-02-A3-V01
lineage_id: C-S02-A3
scenario_id: C-S02
subtype_id: C-01
anchor_id: C-S02-A3
variant_id: V01
variant_type: LEX
task_domain: Hydration
utterance: "I drank the required water."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-02-A3-V02
lineage_id: C-S02-A3
scenario_id: C-S02
subtype_id: C-01
anchor_id: C-S02-A3
variant_id: V02
variant_type: SYN
task_domain: Hydration
utterance: "Look, the water has been finished."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-02-A3-V03
lineage_id: C-S02-A3
scenario_id: C-S02
subtype_id: C-01
anchor_id: C-S02-A3
variant_id: V03
variant_type: NAT
task_domain: Hydration
utterance: "I’ve had the required water already."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-02-A3-V04
lineage_id: C-S02-A3
scenario_id: C-S02
subtype_id: C-01
anchor_id: C-S02-A3
variant_id: V04
variant_type: EXP
task_domain: Hydration
utterance: "I’ve completed the hydration task and finished the required water."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-02-A3-V05
lineage_id: C-S02-A3
scenario_id: C-S02
subtype_id: C-01
anchor_id: C-S02-A3
variant_id: V05
variant_type: PRG
task_domain: Hydration
utterance: "Look, my water intake for this task is finished."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-02-A3-V06
lineage_id: C-S02-A3
scenario_id: C-S02
subtype_id: C-01
anchor_id: C-S02-A3
variant_id: V06
variant_type: DSC
task_domain: Hydration
utterance: "That’s done—I’ve finished the required water."
execution_status: Completed
validation_status: candidate
```

## C-S03 — C-01 Direct Completion

### Scenario

The user explicitly states that the required exercise task has been completed.

### Target task domain

Exercise

### Stage 1 anchors

- **A1:** I finished the exercise.
- **A2:** I completed my workout.
- **A3:** The exercise is done.

### Semantic invariant

The target task has been executed and is complete.

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I finished the exercise. |
| A1 | V02 | SYN | My workout has been completed. |
| A1 | V03 | NAT | I’m done with the workout. |
| A1 | V04 | EXP | I’ve completed the exercise task from start to finish. |
| A1 | V05 | PRG | The workout is finished now. |
| A1 | V06 | DSC | That’s done—I’ve completed my exercise. |
| A2 | V01 | LEX | I finished the routine. |
| A2 | V02 | SYN | I must say, my workout has been completed. |
| A2 | V03 | NAT | I must say, i’m done with the workout. |
| A2 | V04 | EXP | So, i’ve completed the exercise task from start to finish. |
| A2 | V05 | PRG | Listen, the workout is finished now. |
| A2 | V06 | DSC | You know, that’s done—I’ve completed my exercise. |
| A3 | V01 | LEX | I finished the exercise routine. |
| A3 | V02 | SYN | Actually, my workout has been completed. |
| A3 | V03 | NAT | I’m done with the exercise routine. |
| A3 | V04 | EXP | I’ve completed the exercise routine task from start to finish. |
| A3 | V05 | PRG | Right, the workout is finished now. |
| A3 | V06 | DSC | Right, that’s done—I’ve completed my exercise. |

### Production records

```yaml
example_id: C3A-03-A1-V01
lineage_id: C-S03-A1
scenario_id: C-S03
subtype_id: C-01
anchor_id: C-S03-A1
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "I finished the exercise."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-03-A1-V02
lineage_id: C-S03-A1
scenario_id: C-S03
subtype_id: C-01
anchor_id: C-S03-A1
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "My workout has been completed."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-03-A1-V03
lineage_id: C-S03-A1
scenario_id: C-S03
subtype_id: C-01
anchor_id: C-S03-A1
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "I’m done with the workout."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-03-A1-V04
lineage_id: C-S03-A1
scenario_id: C-S03
subtype_id: C-01
anchor_id: C-S03-A1
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "I’ve completed the exercise task from start to finish."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-03-A1-V05
lineage_id: C-S03-A1
scenario_id: C-S03
subtype_id: C-01
anchor_id: C-S03-A1
variant_id: V05
variant_type: PRG
task_domain: Exercise
utterance: "The workout is finished now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-03-A1-V06
lineage_id: C-S03-A1
scenario_id: C-S03
subtype_id: C-01
anchor_id: C-S03-A1
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "That’s done—I’ve completed my exercise."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-03-A2-V01
lineage_id: C-S03-A2
scenario_id: C-S03
subtype_id: C-01
anchor_id: C-S03-A2
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "I finished the routine."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-03-A2-V02
lineage_id: C-S03-A2
scenario_id: C-S03
subtype_id: C-01
anchor_id: C-S03-A2
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "I must say, my workout has been completed."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-03-A2-V03
lineage_id: C-S03-A2
scenario_id: C-S03
subtype_id: C-01
anchor_id: C-S03-A2
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "I must say, i’m done with the workout."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-03-A2-V04
lineage_id: C-S03-A2
scenario_id: C-S03
subtype_id: C-01
anchor_id: C-S03-A2
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "So, i’ve completed the exercise task from start to finish."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-03-A2-V05
lineage_id: C-S03-A2
scenario_id: C-S03
subtype_id: C-01
anchor_id: C-S03-A2
variant_id: V05
variant_type: PRG
task_domain: Exercise
utterance: "Listen, the workout is finished now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-03-A2-V06
lineage_id: C-S03-A2
scenario_id: C-S03
subtype_id: C-01
anchor_id: C-S03-A2
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "You know, that’s done—I’ve completed my exercise."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-03-A3-V01
lineage_id: C-S03-A3
scenario_id: C-S03
subtype_id: C-01
anchor_id: C-S03-A3
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "I finished the exercise routine."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-03-A3-V02
lineage_id: C-S03-A3
scenario_id: C-S03
subtype_id: C-01
anchor_id: C-S03-A3
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "Actually, my workout has been completed."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-03-A3-V03
lineage_id: C-S03-A3
scenario_id: C-S03
subtype_id: C-01
anchor_id: C-S03-A3
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "I’m done with the exercise routine."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-03-A3-V04
lineage_id: C-S03-A3
scenario_id: C-S03
subtype_id: C-01
anchor_id: C-S03-A3
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "I’ve completed the exercise routine task from start to finish."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-03-A3-V05
lineage_id: C-S03-A3
scenario_id: C-S03
subtype_id: C-01
anchor_id: C-S03-A3
variant_id: V05
variant_type: PRG
task_domain: Exercise
utterance: "Right, the workout is finished now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-03-A3-V06
lineage_id: C-S03-A3
scenario_id: C-S03
subtype_id: C-01
anchor_id: C-S03-A3
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "Right, that’s done—I’ve completed my exercise."
execution_status: Completed
validation_status: candidate
```

## C-S04 — C-01 Direct Completion

### Scenario

The user explicitly states that the required physiotherapy task has been completed.

### Target task domain

Physiotherapy

### Stage 1 anchors

- **A1:** I finished my physiotherapy.
- **A2:** I completed the physio routine.
- **A3:** The therapy session is done.

### Semantic invariant

The target task has been executed and is complete.

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I finished my physiotherapy. |
| A1 | V02 | SYN | The physio routine has been completed. |
| A1 | V03 | NAT | I’m done with the physio. |
| A1 | V04 | EXP | I’ve completed the entire physiotherapy task. |
| A1 | V05 | PRG | The therapy session is finished. |
| A1 | V06 | DSC | That’s done—I’ve completed the physio routine. |
| A2 | V01 | LEX | Actually, i finished my physiotherapy. |
| A2 | V02 | SYN | Right, the physio routine has been completed. |
| A2 | V03 | NAT | I’m done with the therapy. |
| A2 | V04 | EXP | You know, i’ve completed the entire physiotherapy task. |
| A2 | V05 | PRG | I must say, the therapy session is finished. |
| A2 | V06 | DSC | That’s done—I’ve completed the therapy routine. |
| A3 | V01 | LEX | Right, i finished my physiotherapy. |
| A3 | V02 | SYN | Okay, the physio routine has been completed. |
| A3 | V03 | NAT | I’m done with the therapy session. |
| A3 | V04 | EXP | Okay, i’ve completed the entire physiotherapy task. |
| A3 | V05 | PRG | As I said, the therapy session is finished. |
| A3 | V06 | DSC | That’s done—I’ve completed the therapy session routine. |

### Production records

```yaml
example_id: C3A-04-A1-V01
lineage_id: C-S04-A1
scenario_id: C-S04
subtype_id: C-01
anchor_id: C-S04-A1
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "I finished my physiotherapy."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-04-A1-V02
lineage_id: C-S04-A1
scenario_id: C-S04
subtype_id: C-01
anchor_id: C-S04-A1
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "The physio routine has been completed."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-04-A1-V03
lineage_id: C-S04-A1
scenario_id: C-S04
subtype_id: C-01
anchor_id: C-S04-A1
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "I’m done with the physio."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-04-A1-V04
lineage_id: C-S04-A1
scenario_id: C-S04
subtype_id: C-01
anchor_id: C-S04-A1
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "I’ve completed the entire physiotherapy task."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-04-A1-V05
lineage_id: C-S04-A1
scenario_id: C-S04
subtype_id: C-01
anchor_id: C-S04-A1
variant_id: V05
variant_type: PRG
task_domain: Physiotherapy
utterance: "The therapy session is finished."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-04-A1-V06
lineage_id: C-S04-A1
scenario_id: C-S04
subtype_id: C-01
anchor_id: C-S04-A1
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "That’s done—I’ve completed the physio routine."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-04-A2-V01
lineage_id: C-S04-A2
scenario_id: C-S04
subtype_id: C-01
anchor_id: C-S04-A2
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "Actually, i finished my physiotherapy."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-04-A2-V02
lineage_id: C-S04-A2
scenario_id: C-S04
subtype_id: C-01
anchor_id: C-S04-A2
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "Right, the physio routine has been completed."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-04-A2-V03
lineage_id: C-S04-A2
scenario_id: C-S04
subtype_id: C-01
anchor_id: C-S04-A2
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "I’m done with the therapy."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-04-A2-V04
lineage_id: C-S04-A2
scenario_id: C-S04
subtype_id: C-01
anchor_id: C-S04-A2
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "You know, i’ve completed the entire physiotherapy task."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-04-A2-V05
lineage_id: C-S04-A2
scenario_id: C-S04
subtype_id: C-01
anchor_id: C-S04-A2
variant_id: V05
variant_type: PRG
task_domain: Physiotherapy
utterance: "I must say, the therapy session is finished."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-04-A2-V06
lineage_id: C-S04-A2
scenario_id: C-S04
subtype_id: C-01
anchor_id: C-S04-A2
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "That’s done—I’ve completed the therapy routine."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-04-A3-V01
lineage_id: C-S04-A3
scenario_id: C-S04
subtype_id: C-01
anchor_id: C-S04-A3
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "Right, i finished my physiotherapy."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-04-A3-V02
lineage_id: C-S04-A3
scenario_id: C-S04
subtype_id: C-01
anchor_id: C-S04-A3
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "Okay, the physio routine has been completed."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-04-A3-V03
lineage_id: C-S04-A3
scenario_id: C-S04
subtype_id: C-01
anchor_id: C-S04-A3
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "I’m done with the therapy session."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-04-A3-V04
lineage_id: C-S04-A3
scenario_id: C-S04
subtype_id: C-01
anchor_id: C-S04-A3
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "Okay, i’ve completed the entire physiotherapy task."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-04-A3-V05
lineage_id: C-S04-A3
scenario_id: C-S04
subtype_id: C-01
anchor_id: C-S04-A3
variant_id: V05
variant_type: PRG
task_domain: Physiotherapy
utterance: "As I said, the therapy session is finished."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-04-A3-V06
lineage_id: C-S04-A3
scenario_id: C-S04
subtype_id: C-01
anchor_id: C-S04-A3
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "That’s done—I’ve completed the therapy session routine."
execution_status: Completed
validation_status: candidate
```

## C-S05 — C-02 Retrospective Completion

### Scenario

The user refers back to an earlier completed medication task and makes completion explicit.

### Target task domain

Medication

### Stage 1 anchors

- **A1:** I already took the medication.
- **A2:** I took my medicine earlier.
- **A3:** I’d finished the medication before you reminded me.

### Semantic invariant

The target task has been executed and is complete.

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I already took the medication. |
| A1 | V02 | SYN | The medication was already taken earlier. |
| A1 | V03 | NAT | I took it a little while ago. |
| A1 | V04 | EXP | I completed the medication task earlier, before this reminder. |
| A1 | V05 | PRG | That medication task was finished earlier today. |
| A1 | V06 | DSC | You don’t need to remind me—I already took it. |
| A2 | V01 | LEX | So, i already took the medication. |
| A2 | V02 | SYN | Right, the medication was already taken earlier. |
| A2 | V03 | NAT | Listen, i took it a little while ago. |
| A2 | V04 | EXP | I mean, i completed the medication task earlier, before this reminder. |
| A2 | V05 | PRG | I mean, that medication task was finished earlier today. |
| A2 | V06 | DSC | Listen, you don’t need to remind me—I already took it. |
| A3 | V01 | LEX | I already took my dose. |
| A3 | V02 | SYN | Well, the medication was already taken earlier. |
| A3 | V03 | NAT | Look, i took it a little while ago. |
| A3 | V04 | EXP | I completed my dose task earlier, before this reminder. |
| A3 | V05 | PRG | I must say, that medication task was finished earlier today. |
| A3 | V06 | DSC | You know, you don’t need to remind me—I already took it. |

### Production records

```yaml
example_id: C3A-05-A1-V01
lineage_id: C-S05-A1
scenario_id: C-S05
subtype_id: C-02
anchor_id: C-S05-A1
variant_id: V01
variant_type: LEX
task_domain: Medication
utterance: "I already took the medication."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-05-A1-V02
lineage_id: C-S05-A1
scenario_id: C-S05
subtype_id: C-02
anchor_id: C-S05-A1
variant_id: V02
variant_type: SYN
task_domain: Medication
utterance: "The medication was already taken earlier."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-05-A1-V03
lineage_id: C-S05-A1
scenario_id: C-S05
subtype_id: C-02
anchor_id: C-S05-A1
variant_id: V03
variant_type: NAT
task_domain: Medication
utterance: "I took it a little while ago."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-05-A1-V04
lineage_id: C-S05-A1
scenario_id: C-S05
subtype_id: C-02
anchor_id: C-S05-A1
variant_id: V04
variant_type: EXP
task_domain: Medication
utterance: "I completed the medication task earlier, before this reminder."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-05-A1-V05
lineage_id: C-S05-A1
scenario_id: C-S05
subtype_id: C-02
anchor_id: C-S05-A1
variant_id: V05
variant_type: PRG
task_domain: Medication
utterance: "That medication task was finished earlier today."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-05-A1-V06
lineage_id: C-S05-A1
scenario_id: C-S05
subtype_id: C-02
anchor_id: C-S05-A1
variant_id: V06
variant_type: DSC
task_domain: Medication
utterance: "You don’t need to remind me—I already took it."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-05-A2-V01
lineage_id: C-S05-A2
scenario_id: C-S05
subtype_id: C-02
anchor_id: C-S05-A2
variant_id: V01
variant_type: LEX
task_domain: Medication
utterance: "So, i already took the medication."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-05-A2-V02
lineage_id: C-S05-A2
scenario_id: C-S05
subtype_id: C-02
anchor_id: C-S05-A2
variant_id: V02
variant_type: SYN
task_domain: Medication
utterance: "Right, the medication was already taken earlier."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-05-A2-V03
lineage_id: C-S05-A2
scenario_id: C-S05
subtype_id: C-02
anchor_id: C-S05-A2
variant_id: V03
variant_type: NAT
task_domain: Medication
utterance: "Listen, i took it a little while ago."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-05-A2-V04
lineage_id: C-S05-A2
scenario_id: C-S05
subtype_id: C-02
anchor_id: C-S05-A2
variant_id: V04
variant_type: EXP
task_domain: Medication
utterance: "I mean, i completed the medication task earlier, before this reminder."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-05-A2-V05
lineage_id: C-S05-A2
scenario_id: C-S05
subtype_id: C-02
anchor_id: C-S05-A2
variant_id: V05
variant_type: PRG
task_domain: Medication
utterance: "I mean, that medication task was finished earlier today."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-05-A2-V06
lineage_id: C-S05-A2
scenario_id: C-S05
subtype_id: C-02
anchor_id: C-S05-A2
variant_id: V06
variant_type: DSC
task_domain: Medication
utterance: "Listen, you don’t need to remind me—I already took it."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-05-A3-V01
lineage_id: C-S05-A3
scenario_id: C-S05
subtype_id: C-02
anchor_id: C-S05-A3
variant_id: V01
variant_type: LEX
task_domain: Medication
utterance: "I already took my dose."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-05-A3-V02
lineage_id: C-S05-A3
scenario_id: C-S05
subtype_id: C-02
anchor_id: C-S05-A3
variant_id: V02
variant_type: SYN
task_domain: Medication
utterance: "Well, the medication was already taken earlier."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-05-A3-V03
lineage_id: C-S05-A3
scenario_id: C-S05
subtype_id: C-02
anchor_id: C-S05-A3
variant_id: V03
variant_type: NAT
task_domain: Medication
utterance: "Look, i took it a little while ago."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-05-A3-V04
lineage_id: C-S05-A3
scenario_id: C-S05
subtype_id: C-02
anchor_id: C-S05-A3
variant_id: V04
variant_type: EXP
task_domain: Medication
utterance: "I completed my dose task earlier, before this reminder."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-05-A3-V05
lineage_id: C-S05-A3
scenario_id: C-S05
subtype_id: C-02
anchor_id: C-S05-A3
variant_id: V05
variant_type: PRG
task_domain: Medication
utterance: "I must say, that medication task was finished earlier today."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-05-A3-V06
lineage_id: C-S05-A3
scenario_id: C-S05
subtype_id: C-02
anchor_id: C-S05-A3
variant_id: V06
variant_type: DSC
task_domain: Medication
utterance: "You know, you don’t need to remind me—I already took it."
execution_status: Completed
validation_status: candidate
```

## C-S06 — C-02 Retrospective Completion

### Scenario

The user retrospectively reports that the hydration task was already completed.

### Target task domain

Hydration

### Stage 1 anchors

- **A1:** I already drank the water.
- **A2:** I finished my water earlier.
- **A3:** I had the water before this reminder.

### Semantic invariant

The target task has been executed and is complete.

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I already drank the water. |
| A1 | V02 | SYN | The water was already finished earlier. |
| A1 | V03 | NAT | I had it earlier. |
| A1 | V04 | EXP | I completed the hydration task earlier, before you reminded me. |
| A1 | V05 | PRG | The required water was finished earlier today. |
| A1 | V06 | DSC | That reminder came after I’d already finished my water. |
| A2 | V01 | LEX | I already drank the bottle. |
| A2 | V02 | SYN | So, the water was already finished earlier. |
| A2 | V03 | NAT | Look, i had it earlier. |
| A2 | V04 | EXP | Actually, i completed the hydration task earlier, before you reminded me. |
| A2 | V05 | PRG | I must say, the required water was finished earlier today. |
| A2 | V06 | DSC | Honestly, that reminder came after I’d already finished my water. |
| A3 | V01 | LEX | I already drank the required water. |
| A3 | V02 | SYN | Actually, the water was already finished earlier. |
| A3 | V03 | NAT | So, i had it earlier. |
| A3 | V04 | EXP | Well, i completed the hydration task earlier, before you reminded me. |
| A3 | V05 | PRG | Listen, the required water was finished earlier today. |
| A3 | V06 | DSC | I mean, that reminder came after I’d already finished my water. |

### Production records

```yaml
example_id: C3A-06-A1-V01
lineage_id: C-S06-A1
scenario_id: C-S06
subtype_id: C-02
anchor_id: C-S06-A1
variant_id: V01
variant_type: LEX
task_domain: Hydration
utterance: "I already drank the water."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-06-A1-V02
lineage_id: C-S06-A1
scenario_id: C-S06
subtype_id: C-02
anchor_id: C-S06-A1
variant_id: V02
variant_type: SYN
task_domain: Hydration
utterance: "The water was already finished earlier."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-06-A1-V03
lineage_id: C-S06-A1
scenario_id: C-S06
subtype_id: C-02
anchor_id: C-S06-A1
variant_id: V03
variant_type: NAT
task_domain: Hydration
utterance: "I had it earlier."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-06-A1-V04
lineage_id: C-S06-A1
scenario_id: C-S06
subtype_id: C-02
anchor_id: C-S06-A1
variant_id: V04
variant_type: EXP
task_domain: Hydration
utterance: "I completed the hydration task earlier, before you reminded me."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-06-A1-V05
lineage_id: C-S06-A1
scenario_id: C-S06
subtype_id: C-02
anchor_id: C-S06-A1
variant_id: V05
variant_type: PRG
task_domain: Hydration
utterance: "The required water was finished earlier today."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-06-A1-V06
lineage_id: C-S06-A1
scenario_id: C-S06
subtype_id: C-02
anchor_id: C-S06-A1
variant_id: V06
variant_type: DSC
task_domain: Hydration
utterance: "That reminder came after I’d already finished my water."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-06-A2-V01
lineage_id: C-S06-A2
scenario_id: C-S06
subtype_id: C-02
anchor_id: C-S06-A2
variant_id: V01
variant_type: LEX
task_domain: Hydration
utterance: "I already drank the bottle."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-06-A2-V02
lineage_id: C-S06-A2
scenario_id: C-S06
subtype_id: C-02
anchor_id: C-S06-A2
variant_id: V02
variant_type: SYN
task_domain: Hydration
utterance: "So, the water was already finished earlier."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-06-A2-V03
lineage_id: C-S06-A2
scenario_id: C-S06
subtype_id: C-02
anchor_id: C-S06-A2
variant_id: V03
variant_type: NAT
task_domain: Hydration
utterance: "Look, i had it earlier."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-06-A2-V04
lineage_id: C-S06-A2
scenario_id: C-S06
subtype_id: C-02
anchor_id: C-S06-A2
variant_id: V04
variant_type: EXP
task_domain: Hydration
utterance: "Actually, i completed the hydration task earlier, before you reminded me."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-06-A2-V05
lineage_id: C-S06-A2
scenario_id: C-S06
subtype_id: C-02
anchor_id: C-S06-A2
variant_id: V05
variant_type: PRG
task_domain: Hydration
utterance: "I must say, the required water was finished earlier today."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-06-A2-V06
lineage_id: C-S06-A2
scenario_id: C-S06
subtype_id: C-02
anchor_id: C-S06-A2
variant_id: V06
variant_type: DSC
task_domain: Hydration
utterance: "Honestly, that reminder came after I’d already finished my water."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-06-A3-V01
lineage_id: C-S06-A3
scenario_id: C-S06
subtype_id: C-02
anchor_id: C-S06-A3
variant_id: V01
variant_type: LEX
task_domain: Hydration
utterance: "I already drank the required water."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-06-A3-V02
lineage_id: C-S06-A3
scenario_id: C-S06
subtype_id: C-02
anchor_id: C-S06-A3
variant_id: V02
variant_type: SYN
task_domain: Hydration
utterance: "Actually, the water was already finished earlier."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-06-A3-V03
lineage_id: C-S06-A3
scenario_id: C-S06
subtype_id: C-02
anchor_id: C-S06-A3
variant_id: V03
variant_type: NAT
task_domain: Hydration
utterance: "So, i had it earlier."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-06-A3-V04
lineage_id: C-S06-A3
scenario_id: C-S06
subtype_id: C-02
anchor_id: C-S06-A3
variant_id: V04
variant_type: EXP
task_domain: Hydration
utterance: "Well, i completed the hydration task earlier, before you reminded me."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-06-A3-V05
lineage_id: C-S06-A3
scenario_id: C-S06
subtype_id: C-02
anchor_id: C-S06-A3
variant_id: V05
variant_type: PRG
task_domain: Hydration
utterance: "Listen, the required water was finished earlier today."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-06-A3-V06
lineage_id: C-S06-A3
scenario_id: C-S06
subtype_id: C-02
anchor_id: C-S06-A3
variant_id: V06
variant_type: DSC
task_domain: Hydration
utterance: "I mean, that reminder came after I’d already finished my water."
execution_status: Completed
validation_status: candidate
```

## C-S07 — C-02 Retrospective Completion

### Scenario

The user retrospectively reports that the exercise task was already completed.

### Target task domain

Exercise

### Stage 1 anchors

- **A1:** I already did my workout.
- **A2:** I finished exercising earlier.
- **A3:** I completed the workout before the reminder.

### Semantic invariant

The target task has been executed and is complete.

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I already did my workout. |
| A1 | V02 | SYN | The workout was completed earlier. |
| A1 | V03 | NAT | I got my exercise done earlier. |
| A1 | V04 | EXP | I completed the exercise task before this reminder. |
| A1 | V05 | PRG | The workout was finished earlier today. |
| A1 | V06 | DSC | The reminder came after I’d already done the workout. |
| A2 | V01 | LEX | Honestly, i already did my workout. |
| A2 | V02 | SYN | Well, the workout was completed earlier. |
| A2 | V03 | NAT | Look, i got my exercise done earlier. |
| A2 | V04 | EXP | As I said, i completed the exercise task before this reminder. |
| A2 | V05 | PRG | I mean, the workout was finished earlier today. |
| A2 | V06 | DSC | Okay, the reminder came after I’d already done the workout. |
| A3 | V01 | LEX | Okay, i already did my workout. |
| A3 | V02 | SYN | As I said, the workout was completed earlier. |
| A3 | V03 | NAT | I mean, i got my exercise done earlier. |
| A3 | V04 | EXP | I completed the exercise routine task before this reminder. |
| A3 | V05 | PRG | I must say, the workout was finished earlier today. |
| A3 | V06 | DSC | The reminder came after I’d already done the exercise routine. |

### Production records

```yaml
example_id: C3A-07-A1-V01
lineage_id: C-S07-A1
scenario_id: C-S07
subtype_id: C-02
anchor_id: C-S07-A1
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "I already did my workout."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-07-A1-V02
lineage_id: C-S07-A1
scenario_id: C-S07
subtype_id: C-02
anchor_id: C-S07-A1
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "The workout was completed earlier."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-07-A1-V03
lineage_id: C-S07-A1
scenario_id: C-S07
subtype_id: C-02
anchor_id: C-S07-A1
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "I got my exercise done earlier."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-07-A1-V04
lineage_id: C-S07-A1
scenario_id: C-S07
subtype_id: C-02
anchor_id: C-S07-A1
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "I completed the exercise task before this reminder."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-07-A1-V05
lineage_id: C-S07-A1
scenario_id: C-S07
subtype_id: C-02
anchor_id: C-S07-A1
variant_id: V05
variant_type: PRG
task_domain: Exercise
utterance: "The workout was finished earlier today."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-07-A1-V06
lineage_id: C-S07-A1
scenario_id: C-S07
subtype_id: C-02
anchor_id: C-S07-A1
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "The reminder came after I’d already done the workout."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-07-A2-V01
lineage_id: C-S07-A2
scenario_id: C-S07
subtype_id: C-02
anchor_id: C-S07-A2
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "Honestly, i already did my workout."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-07-A2-V02
lineage_id: C-S07-A2
scenario_id: C-S07
subtype_id: C-02
anchor_id: C-S07-A2
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "Well, the workout was completed earlier."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-07-A2-V03
lineage_id: C-S07-A2
scenario_id: C-S07
subtype_id: C-02
anchor_id: C-S07-A2
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "Look, i got my exercise done earlier."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-07-A2-V04
lineage_id: C-S07-A2
scenario_id: C-S07
subtype_id: C-02
anchor_id: C-S07-A2
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "As I said, i completed the exercise task before this reminder."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-07-A2-V05
lineage_id: C-S07-A2
scenario_id: C-S07
subtype_id: C-02
anchor_id: C-S07-A2
variant_id: V05
variant_type: PRG
task_domain: Exercise
utterance: "I mean, the workout was finished earlier today."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-07-A2-V06
lineage_id: C-S07-A2
scenario_id: C-S07
subtype_id: C-02
anchor_id: C-S07-A2
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "Okay, the reminder came after I’d already done the workout."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-07-A3-V01
lineage_id: C-S07-A3
scenario_id: C-S07
subtype_id: C-02
anchor_id: C-S07-A3
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "Okay, i already did my workout."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-07-A3-V02
lineage_id: C-S07-A3
scenario_id: C-S07
subtype_id: C-02
anchor_id: C-S07-A3
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "As I said, the workout was completed earlier."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-07-A3-V03
lineage_id: C-S07-A3
scenario_id: C-S07
subtype_id: C-02
anchor_id: C-S07-A3
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "I mean, i got my exercise done earlier."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-07-A3-V04
lineage_id: C-S07-A3
scenario_id: C-S07
subtype_id: C-02
anchor_id: C-S07-A3
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "I completed the exercise routine task before this reminder."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-07-A3-V05
lineage_id: C-S07-A3
scenario_id: C-S07
subtype_id: C-02
anchor_id: C-S07-A3
variant_id: V05
variant_type: PRG
task_domain: Exercise
utterance: "I must say, the workout was finished earlier today."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-07-A3-V06
lineage_id: C-S07-A3
scenario_id: C-S07
subtype_id: C-02
anchor_id: C-S07-A3
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "The reminder came after I’d already done the exercise routine."
execution_status: Completed
validation_status: candidate
```

## C-S08 — C-02 Retrospective Completion

### Scenario

The user retrospectively reports that the physiotherapy task was already completed.

### Target task domain

Physiotherapy

### Stage 1 anchors

- **A1:** I already did my physio.
- **A2:** I finished the therapy earlier.
- **A3:** I completed the routine before you reminded me.

### Semantic invariant

The target task has been executed and is complete.

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I already did my physio. |
| A1 | V02 | SYN | The therapy routine was completed earlier. |
| A1 | V03 | NAT | I got the physio done earlier. |
| A1 | V04 | EXP | I completed the physiotherapy task before this reminder. |
| A1 | V05 | PRG | The therapy session was finished earlier today. |
| A1 | V06 | DSC | You reminded me after I’d already completed the routine. |
| A2 | V01 | LEX | Honestly, i already did my physio. |
| A2 | V02 | SYN | To be honest, the therapy routine was completed earlier. |
| A2 | V03 | NAT | I got the therapy done earlier. |
| A2 | V04 | EXP | I completed the therapytherapy task before this reminder. |
| A2 | V05 | PRG | You know, the therapy session was finished earlier today. |
| A2 | V06 | DSC | You reminded me after I’d already completed the therapy routine. |
| A3 | V01 | LEX | Well, i already did my physio. |
| A3 | V02 | SYN | So, the therapy routine was completed earlier. |
| A3 | V03 | NAT | I got the therapy session done earlier. |
| A3 | V04 | EXP | I completed the therapy sessiontherapy task before this reminder. |
| A3 | V05 | PRG | Look, the therapy session was finished earlier today. |
| A3 | V06 | DSC | Honestly, you reminded me after I’d already completed the therapy routine. |

### Production records

```yaml
example_id: C3A-08-A1-V01
lineage_id: C-S08-A1
scenario_id: C-S08
subtype_id: C-02
anchor_id: C-S08-A1
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "I already did my physio."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-08-A1-V02
lineage_id: C-S08-A1
scenario_id: C-S08
subtype_id: C-02
anchor_id: C-S08-A1
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "The therapy routine was completed earlier."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-08-A1-V03
lineage_id: C-S08-A1
scenario_id: C-S08
subtype_id: C-02
anchor_id: C-S08-A1
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "I got the physio done earlier."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-08-A1-V04
lineage_id: C-S08-A1
scenario_id: C-S08
subtype_id: C-02
anchor_id: C-S08-A1
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "I completed the physiotherapy task before this reminder."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-08-A1-V05
lineage_id: C-S08-A1
scenario_id: C-S08
subtype_id: C-02
anchor_id: C-S08-A1
variant_id: V05
variant_type: PRG
task_domain: Physiotherapy
utterance: "The therapy session was finished earlier today."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-08-A1-V06
lineage_id: C-S08-A1
scenario_id: C-S08
subtype_id: C-02
anchor_id: C-S08-A1
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "You reminded me after I’d already completed the routine."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-08-A2-V01
lineage_id: C-S08-A2
scenario_id: C-S08
subtype_id: C-02
anchor_id: C-S08-A2
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "Honestly, i already did my physio."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-08-A2-V02
lineage_id: C-S08-A2
scenario_id: C-S08
subtype_id: C-02
anchor_id: C-S08-A2
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "To be honest, the therapy routine was completed earlier."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-08-A2-V03
lineage_id: C-S08-A2
scenario_id: C-S08
subtype_id: C-02
anchor_id: C-S08-A2
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "I got the therapy done earlier."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-08-A2-V04
lineage_id: C-S08-A2
scenario_id: C-S08
subtype_id: C-02
anchor_id: C-S08-A2
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "I completed the therapytherapy task before this reminder."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-08-A2-V05
lineage_id: C-S08-A2
scenario_id: C-S08
subtype_id: C-02
anchor_id: C-S08-A2
variant_id: V05
variant_type: PRG
task_domain: Physiotherapy
utterance: "You know, the therapy session was finished earlier today."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-08-A2-V06
lineage_id: C-S08-A2
scenario_id: C-S08
subtype_id: C-02
anchor_id: C-S08-A2
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "You reminded me after I’d already completed the therapy routine."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-08-A3-V01
lineage_id: C-S08-A3
scenario_id: C-S08
subtype_id: C-02
anchor_id: C-S08-A3
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "Well, i already did my physio."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-08-A3-V02
lineage_id: C-S08-A3
scenario_id: C-S08
subtype_id: C-02
anchor_id: C-S08-A3
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "So, the therapy routine was completed earlier."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-08-A3-V03
lineage_id: C-S08-A3
scenario_id: C-S08
subtype_id: C-02
anchor_id: C-S08-A3
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "I got the therapy session done earlier."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-08-A3-V04
lineage_id: C-S08-A3
scenario_id: C-S08
subtype_id: C-02
anchor_id: C-S08-A3
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "I completed the therapy sessiontherapy task before this reminder."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-08-A3-V05
lineage_id: C-S08-A3
scenario_id: C-S08
subtype_id: C-02
anchor_id: C-S08-A3
variant_id: V05
variant_type: PRG
task_domain: Physiotherapy
utterance: "Look, the therapy session was finished earlier today."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-08-A3-V06
lineage_id: C-S08-A3
scenario_id: C-S08
subtype_id: C-02
anchor_id: C-S08-A3
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "Honestly, you reminded me after I’d already completed the therapy routine."
execution_status: Completed
validation_status: candidate
```

## C-S09 — C-03 Indirect Completion

### Scenario

The user provides evidence that necessarily indicates the medication task has already been completed without using a direct completion verb.

### Target task domain

Medication

### Stage 1 anchors

- **A1:** The pill bottle is back in the cabinet.
- **A2:** There are no tablets left in today’s compartment.
- **A3:** I’ve put the medicine away.

### Semantic invariant

The target task has been executed and is complete.

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | The medicine is back in its cabinet. |
| A1 | V02 | SYN | Today’s medication compartment is empty. |
| A1 | V03 | NAT | The pills are put away now. |
| A1 | V04 | EXP | The medication has been taken, as shown by the empty dose compartment. |
| A1 | V05 | PRG | Everything is put away after today’s dose. |
| A1 | V06 | DSC | The bottle is already back in the cabinet, so today’s dose is finished. |
| A2 | V01 | LEX | I must say, the medicine is back in its cabinet. |
| A2 | V02 | SYN | Honestly, today’s medication compartment is empty. |
| A2 | V03 | NAT | So, the pills are put away now. |
| A2 | V04 | EXP | Listen, the medication has been taken, as shown by the empty dose compartment. |
| A2 | V05 | PRG | Right, everything is put away after today’s dose. |
| A2 | V06 | DSC | Listen, the bottle is already back in the cabinet, so today’s dose is finished. |
| A3 | V01 | LEX | Look, the medicine is back in its cabinet. |
| A3 | V02 | SYN | As I said, today’s medication compartment is empty. |
| A3 | V03 | NAT | Right, the pills are put away now. |
| A3 | V04 | EXP | So, the medication has been taken, as shown by the empty dose compartment. |
| A3 | V05 | PRG | Basically, everything is put away after today’s dose. |
| A3 | V06 | DSC | Right, the bottle is already back in the cabinet, so today’s dose is finished. |

### Production records

```yaml
example_id: C3A-09-A1-V01
lineage_id: C-S09-A1
scenario_id: C-S09
subtype_id: C-03
anchor_id: C-S09-A1
variant_id: V01
variant_type: LEX
task_domain: Medication
utterance: "The medicine is back in its cabinet."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-09-A1-V02
lineage_id: C-S09-A1
scenario_id: C-S09
subtype_id: C-03
anchor_id: C-S09-A1
variant_id: V02
variant_type: SYN
task_domain: Medication
utterance: "Today’s medication compartment is empty."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-09-A1-V03
lineage_id: C-S09-A1
scenario_id: C-S09
subtype_id: C-03
anchor_id: C-S09-A1
variant_id: V03
variant_type: NAT
task_domain: Medication
utterance: "The pills are put away now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-09-A1-V04
lineage_id: C-S09-A1
scenario_id: C-S09
subtype_id: C-03
anchor_id: C-S09-A1
variant_id: V04
variant_type: EXP
task_domain: Medication
utterance: "The medication has been taken, as shown by the empty dose compartment."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-09-A1-V05
lineage_id: C-S09-A1
scenario_id: C-S09
subtype_id: C-03
anchor_id: C-S09-A1
variant_id: V05
variant_type: PRG
task_domain: Medication
utterance: "Everything is put away after today’s dose."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-09-A1-V06
lineage_id: C-S09-A1
scenario_id: C-S09
subtype_id: C-03
anchor_id: C-S09-A1
variant_id: V06
variant_type: DSC
task_domain: Medication
utterance: "The bottle is already back in the cabinet, so today’s dose is finished."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-09-A2-V01
lineage_id: C-S09-A2
scenario_id: C-S09
subtype_id: C-03
anchor_id: C-S09-A2
variant_id: V01
variant_type: LEX
task_domain: Medication
utterance: "I must say, the medicine is back in its cabinet."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-09-A2-V02
lineage_id: C-S09-A2
scenario_id: C-S09
subtype_id: C-03
anchor_id: C-S09-A2
variant_id: V02
variant_type: SYN
task_domain: Medication
utterance: "Honestly, today’s medication compartment is empty."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-09-A2-V03
lineage_id: C-S09-A2
scenario_id: C-S09
subtype_id: C-03
anchor_id: C-S09-A2
variant_id: V03
variant_type: NAT
task_domain: Medication
utterance: "So, the pills are put away now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-09-A2-V04
lineage_id: C-S09-A2
scenario_id: C-S09
subtype_id: C-03
anchor_id: C-S09-A2
variant_id: V04
variant_type: EXP
task_domain: Medication
utterance: "Listen, the medication has been taken, as shown by the empty dose compartment."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-09-A2-V05
lineage_id: C-S09-A2
scenario_id: C-S09
subtype_id: C-03
anchor_id: C-S09-A2
variant_id: V05
variant_type: PRG
task_domain: Medication
utterance: "Right, everything is put away after today’s dose."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-09-A2-V06
lineage_id: C-S09-A2
scenario_id: C-S09
subtype_id: C-03
anchor_id: C-S09-A2
variant_id: V06
variant_type: DSC
task_domain: Medication
utterance: "Listen, the bottle is already back in the cabinet, so today’s dose is finished."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-09-A3-V01
lineage_id: C-S09-A3
scenario_id: C-S09
subtype_id: C-03
anchor_id: C-S09-A3
variant_id: V01
variant_type: LEX
task_domain: Medication
utterance: "Look, the medicine is back in its cabinet."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-09-A3-V02
lineage_id: C-S09-A3
scenario_id: C-S09
subtype_id: C-03
anchor_id: C-S09-A3
variant_id: V02
variant_type: SYN
task_domain: Medication
utterance: "As I said, today’s medication compartment is empty."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-09-A3-V03
lineage_id: C-S09-A3
scenario_id: C-S09
subtype_id: C-03
anchor_id: C-S09-A3
variant_id: V03
variant_type: NAT
task_domain: Medication
utterance: "Right, the pills are put away now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-09-A3-V04
lineage_id: C-S09-A3
scenario_id: C-S09
subtype_id: C-03
anchor_id: C-S09-A3
variant_id: V04
variant_type: EXP
task_domain: Medication
utterance: "So, the medication has been taken, as shown by the empty dose compartment."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-09-A3-V05
lineage_id: C-S09-A3
scenario_id: C-S09
subtype_id: C-03
anchor_id: C-S09-A3
variant_id: V05
variant_type: PRG
task_domain: Medication
utterance: "Basically, everything is put away after today’s dose."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-09-A3-V06
lineage_id: C-S09-A3
scenario_id: C-S09
subtype_id: C-03
anchor_id: C-S09-A3
variant_id: V06
variant_type: DSC
task_domain: Medication
utterance: "Right, the bottle is already back in the cabinet, so today’s dose is finished."
execution_status: Completed
validation_status: candidate
```

## C-S10 — C-03 Indirect Completion

### Scenario

The user provides contextual evidence that indicates the hydration task has been completed.

### Target task domain

Hydration

### Stage 1 anchors

- **A1:** The bottle is empty now.
- **A2:** I put the empty bottle on the counter.
- **A3:** There’s no water left in the bottle.

### Semantic invariant

The target task has been executed and is complete.

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | The bottle is empty now. |
| A1 | V02 | SYN | There is no water left in the bottle. |
| A1 | V03 | NAT | I’ve emptied the bottle. |
| A1 | V04 | EXP | The hydration task is complete; the required bottle is empty. |
| A1 | V05 | PRG | The bottle is finished and empty now. |
| A1 | V06 | DSC | There’s nothing left in the bottle, so I’m finished with it. |
| A2 | V01 | LEX | Well, the bottle is empty now. |
| A2 | V02 | SYN | Okay, there is no water left in the bottle. |
| A2 | V03 | NAT | Listen, i’ve emptied the bottle. |
| A2 | V04 | EXP | I mean, the hydration task is complete; the required bottle is empty. |
| A2 | V05 | PRG | I must say, the bottle is finished and empty now. |
| A2 | V06 | DSC | Okay, there’s nothing left in the bottle, so I’m finished with it. |
| A3 | V01 | LEX | Listen, the bottle is empty now. |
| A3 | V02 | SYN | Basically, there is no water left in the bottle. |
| A3 | V03 | NAT | Honestly, i’ve emptied the bottle. |
| A3 | V04 | EXP | Basically, the hydration task is complete; the required bottle is empty. |
| A3 | V05 | PRG | I mean, the bottle is finished and empty now. |
| A3 | V06 | DSC | You know, there’s nothing left in the bottle, so I’m finished with it. |

### Production records

```yaml
example_id: C3A-10-A1-V01
lineage_id: C-S10-A1
scenario_id: C-S10
subtype_id: C-03
anchor_id: C-S10-A1
variant_id: V01
variant_type: LEX
task_domain: Hydration
utterance: "The bottle is empty now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-10-A1-V02
lineage_id: C-S10-A1
scenario_id: C-S10
subtype_id: C-03
anchor_id: C-S10-A1
variant_id: V02
variant_type: SYN
task_domain: Hydration
utterance: "There is no water left in the bottle."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-10-A1-V03
lineage_id: C-S10-A1
scenario_id: C-S10
subtype_id: C-03
anchor_id: C-S10-A1
variant_id: V03
variant_type: NAT
task_domain: Hydration
utterance: "I’ve emptied the bottle."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-10-A1-V04
lineage_id: C-S10-A1
scenario_id: C-S10
subtype_id: C-03
anchor_id: C-S10-A1
variant_id: V04
variant_type: EXP
task_domain: Hydration
utterance: "The hydration task is complete; the required bottle is empty."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-10-A1-V05
lineage_id: C-S10-A1
scenario_id: C-S10
subtype_id: C-03
anchor_id: C-S10-A1
variant_id: V05
variant_type: PRG
task_domain: Hydration
utterance: "The bottle is finished and empty now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-10-A1-V06
lineage_id: C-S10-A1
scenario_id: C-S10
subtype_id: C-03
anchor_id: C-S10-A1
variant_id: V06
variant_type: DSC
task_domain: Hydration
utterance: "There’s nothing left in the bottle, so I’m finished with it."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-10-A2-V01
lineage_id: C-S10-A2
scenario_id: C-S10
subtype_id: C-03
anchor_id: C-S10-A2
variant_id: V01
variant_type: LEX
task_domain: Hydration
utterance: "Well, the bottle is empty now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-10-A2-V02
lineage_id: C-S10-A2
scenario_id: C-S10
subtype_id: C-03
anchor_id: C-S10-A2
variant_id: V02
variant_type: SYN
task_domain: Hydration
utterance: "Okay, there is no water left in the bottle."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-10-A2-V03
lineage_id: C-S10-A2
scenario_id: C-S10
subtype_id: C-03
anchor_id: C-S10-A2
variant_id: V03
variant_type: NAT
task_domain: Hydration
utterance: "Listen, i’ve emptied the bottle."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-10-A2-V04
lineage_id: C-S10-A2
scenario_id: C-S10
subtype_id: C-03
anchor_id: C-S10-A2
variant_id: V04
variant_type: EXP
task_domain: Hydration
utterance: "I mean, the hydration task is complete; the required bottle is empty."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-10-A2-V05
lineage_id: C-S10-A2
scenario_id: C-S10
subtype_id: C-03
anchor_id: C-S10-A2
variant_id: V05
variant_type: PRG
task_domain: Hydration
utterance: "I must say, the bottle is finished and empty now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-10-A2-V06
lineage_id: C-S10-A2
scenario_id: C-S10
subtype_id: C-03
anchor_id: C-S10-A2
variant_id: V06
variant_type: DSC
task_domain: Hydration
utterance: "Okay, there’s nothing left in the bottle, so I’m finished with it."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-10-A3-V01
lineage_id: C-S10-A3
scenario_id: C-S10
subtype_id: C-03
anchor_id: C-S10-A3
variant_id: V01
variant_type: LEX
task_domain: Hydration
utterance: "Listen, the bottle is empty now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-10-A3-V02
lineage_id: C-S10-A3
scenario_id: C-S10
subtype_id: C-03
anchor_id: C-S10-A3
variant_id: V02
variant_type: SYN
task_domain: Hydration
utterance: "Basically, there is no water left in the bottle."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-10-A3-V03
lineage_id: C-S10-A3
scenario_id: C-S10
subtype_id: C-03
anchor_id: C-S10-A3
variant_id: V03
variant_type: NAT
task_domain: Hydration
utterance: "Honestly, i’ve emptied the bottle."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-10-A3-V04
lineage_id: C-S10-A3
scenario_id: C-S10
subtype_id: C-03
anchor_id: C-S10-A3
variant_id: V04
variant_type: EXP
task_domain: Hydration
utterance: "Basically, the hydration task is complete; the required bottle is empty."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-10-A3-V05
lineage_id: C-S10-A3
scenario_id: C-S10
subtype_id: C-03
anchor_id: C-S10-A3
variant_id: V05
variant_type: PRG
task_domain: Hydration
utterance: "I mean, the bottle is finished and empty now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-10-A3-V06
lineage_id: C-S10-A3
scenario_id: C-S10
subtype_id: C-03
anchor_id: C-S10-A3
variant_id: V06
variant_type: DSC
task_domain: Hydration
utterance: "You know, there’s nothing left in the bottle, so I’m finished with it."
execution_status: Completed
validation_status: candidate
```

## C-S11 — C-03 Indirect Completion

### Scenario

The user provides contextual evidence that indicates the exercise task has been completed.

### Target task domain

Exercise

### Stage 1 anchors

- **A1:** I’ve put the exercise equipment away.
- **A2:** The workout mat is rolled up and stored.
- **A3:** I’m back in my regular clothes after the workout.

### Semantic invariant

The target task has been executed and is complete.

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I’ve put the exercise equipment away. |
| A1 | V02 | SYN | The workout mat has been rolled up and stored. |
| A1 | V03 | NAT | The gear is all put away now. |
| A1 | V04 | EXP | The exercise is complete; I’ve finished the routine and stored the equipment. |
| A1 | V05 | PRG | The workout setup is packed away now. |
| A1 | V06 | DSC | The equipment is already stored, so the workout is finished. |
| A2 | V01 | LEX | I’ve put the routine equipment away. |
| A2 | V02 | SYN | I mean, the workout mat has been rolled up and stored. |
| A2 | V03 | NAT | I must say, the gear is all put away now. |
| A2 | V04 | EXP | Well, the exercise is complete; I’ve finished the routine and stored the equipment. |
| A2 | V05 | PRG | I mean, the workout setup is packed away now. |
| A2 | V06 | DSC | Look, the equipment is already stored, so the workout is finished. |
| A3 | V01 | LEX | I’ve put the exercise routine equipment away. |
| A3 | V02 | SYN | Well, the workout mat has been rolled up and stored. |
| A3 | V03 | NAT | As I said, the gear is all put away now. |
| A3 | V04 | EXP | Look, the exercise is complete; I’ve finished the routine and stored the equipment. |
| A3 | V05 | PRG | Honestly, the workout setup is packed away now. |
| A3 | V06 | DSC | The equipment is already stored, so the exercise routine is finished. |

### Production records

```yaml
example_id: C3A-11-A1-V01
lineage_id: C-S11-A1
scenario_id: C-S11
subtype_id: C-03
anchor_id: C-S11-A1
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "I’ve put the exercise equipment away."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-11-A1-V02
lineage_id: C-S11-A1
scenario_id: C-S11
subtype_id: C-03
anchor_id: C-S11-A1
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "The workout mat has been rolled up and stored."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-11-A1-V03
lineage_id: C-S11-A1
scenario_id: C-S11
subtype_id: C-03
anchor_id: C-S11-A1
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "The gear is all put away now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-11-A1-V04
lineage_id: C-S11-A1
scenario_id: C-S11
subtype_id: C-03
anchor_id: C-S11-A1
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "The exercise is complete; I’ve finished the routine and stored the equipment."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-11-A1-V05
lineage_id: C-S11-A1
scenario_id: C-S11
subtype_id: C-03
anchor_id: C-S11-A1
variant_id: V05
variant_type: PRG
task_domain: Exercise
utterance: "The workout setup is packed away now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-11-A1-V06
lineage_id: C-S11-A1
scenario_id: C-S11
subtype_id: C-03
anchor_id: C-S11-A1
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "The equipment is already stored, so the workout is finished."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-11-A2-V01
lineage_id: C-S11-A2
scenario_id: C-S11
subtype_id: C-03
anchor_id: C-S11-A2
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "I’ve put the routine equipment away."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-11-A2-V02
lineage_id: C-S11-A2
scenario_id: C-S11
subtype_id: C-03
anchor_id: C-S11-A2
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "I mean, the workout mat has been rolled up and stored."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-11-A2-V03
lineage_id: C-S11-A2
scenario_id: C-S11
subtype_id: C-03
anchor_id: C-S11-A2
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "I must say, the gear is all put away now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-11-A2-V04
lineage_id: C-S11-A2
scenario_id: C-S11
subtype_id: C-03
anchor_id: C-S11-A2
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "Well, the exercise is complete; I’ve finished the routine and stored the equipment."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-11-A2-V05
lineage_id: C-S11-A2
scenario_id: C-S11
subtype_id: C-03
anchor_id: C-S11-A2
variant_id: V05
variant_type: PRG
task_domain: Exercise
utterance: "I mean, the workout setup is packed away now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-11-A2-V06
lineage_id: C-S11-A2
scenario_id: C-S11
subtype_id: C-03
anchor_id: C-S11-A2
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "Look, the equipment is already stored, so the workout is finished."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-11-A3-V01
lineage_id: C-S11-A3
scenario_id: C-S11
subtype_id: C-03
anchor_id: C-S11-A3
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "I’ve put the exercise routine equipment away."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-11-A3-V02
lineage_id: C-S11-A3
scenario_id: C-S11
subtype_id: C-03
anchor_id: C-S11-A3
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "Well, the workout mat has been rolled up and stored."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-11-A3-V03
lineage_id: C-S11-A3
scenario_id: C-S11
subtype_id: C-03
anchor_id: C-S11-A3
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "As I said, the gear is all put away now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-11-A3-V04
lineage_id: C-S11-A3
scenario_id: C-S11
subtype_id: C-03
anchor_id: C-S11-A3
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "Look, the exercise is complete; I’ve finished the routine and stored the equipment."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-11-A3-V05
lineage_id: C-S11-A3
scenario_id: C-S11
subtype_id: C-03
anchor_id: C-S11-A3
variant_id: V05
variant_type: PRG
task_domain: Exercise
utterance: "Honestly, the workout setup is packed away now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-11-A3-V06
lineage_id: C-S11-A3
scenario_id: C-S11
subtype_id: C-03
anchor_id: C-S11-A3
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "The equipment is already stored, so the exercise routine is finished."
execution_status: Completed
validation_status: candidate
```

## C-S12 — C-04 Multi-Step Completion

### Scenario

The user indicates that all required steps of a multi-step physiotherapy routine have been completed.

### Target task domain

Physiotherapy

### Stage 1 anchors

- **A1:** I finished all the exercises in the physio routine.
- **A2:** I completed every step of the therapy sequence.
- **A3:** All the physiotherapy exercises are done.

### Semantic invariant

The target task has been executed and is complete.

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I finished all the exercises in the physio routine. |
| A1 | V02 | SYN | Every step of the therapy sequence has been completed. |
| A1 | V03 | NAT | I’ve worked through the whole physio routine. |
| A1 | V04 | EXP | I completed every required physiotherapy step, so the routine is finished. |
| A1 | V05 | PRG | The entire therapy sequence is finished now. |
| A1 | V06 | DSC | I’ve gone through all the physio exercises; there’s nothing left in the routine. |
| A2 | V01 | LEX | I finished all the exercises in the therapy routine. |
| A2 | V02 | SYN | So, every step of the therapy sequence has been completed. |
| A2 | V03 | NAT | Listen, i’ve worked through the whole physio routine. |
| A2 | V04 | EXP | I completed every required physiotherapy step, so the therapy routine is finished. |
| A2 | V05 | PRG | Basically, the entire therapy sequence is finished now. |
| A2 | V06 | DSC | I’ve gone through all the therapy exercises; there’s nothing left in the therapy routine. |
| A3 | V01 | LEX | I finished all the exercises in the therapy session routine. |
| A3 | V02 | SYN | Look, every step of the therapy sequence has been completed. |
| A3 | V03 | NAT | Look, i’ve worked through the whole physio routine. |
| A3 | V04 | EXP | You know, i completed every required physiotherapy step, so the therapy routine is finished. |
| A3 | V05 | PRG | Right, the entire therapy sequence is finished now. |
| A3 | V06 | DSC | I’ve gone through all the therapy session exercises; there’s nothing left in the therapy routine. |

### Production records

```yaml
example_id: C3A-12-A1-V01
lineage_id: C-S12-A1
scenario_id: C-S12
subtype_id: C-04
anchor_id: C-S12-A1
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "I finished all the exercises in the physio routine."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-12-A1-V02
lineage_id: C-S12-A1
scenario_id: C-S12
subtype_id: C-04
anchor_id: C-S12-A1
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "Every step of the therapy sequence has been completed."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-12-A1-V03
lineage_id: C-S12-A1
scenario_id: C-S12
subtype_id: C-04
anchor_id: C-S12-A1
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "I’ve worked through the whole physio routine."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-12-A1-V04
lineage_id: C-S12-A1
scenario_id: C-S12
subtype_id: C-04
anchor_id: C-S12-A1
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "I completed every required physiotherapy step, so the routine is finished."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-12-A1-V05
lineage_id: C-S12-A1
scenario_id: C-S12
subtype_id: C-04
anchor_id: C-S12-A1
variant_id: V05
variant_type: PRG
task_domain: Physiotherapy
utterance: "The entire therapy sequence is finished now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-12-A1-V06
lineage_id: C-S12-A1
scenario_id: C-S12
subtype_id: C-04
anchor_id: C-S12-A1
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "I’ve gone through all the physio exercises; there’s nothing left in the routine."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-12-A2-V01
lineage_id: C-S12-A2
scenario_id: C-S12
subtype_id: C-04
anchor_id: C-S12-A2
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "I finished all the exercises in the therapy routine."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-12-A2-V02
lineage_id: C-S12-A2
scenario_id: C-S12
subtype_id: C-04
anchor_id: C-S12-A2
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "So, every step of the therapy sequence has been completed."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-12-A2-V03
lineage_id: C-S12-A2
scenario_id: C-S12
subtype_id: C-04
anchor_id: C-S12-A2
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "Listen, i’ve worked through the whole physio routine."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-12-A2-V04
lineage_id: C-S12-A2
scenario_id: C-S12
subtype_id: C-04
anchor_id: C-S12-A2
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "I completed every required physiotherapy step, so the therapy routine is finished."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-12-A2-V05
lineage_id: C-S12-A2
scenario_id: C-S12
subtype_id: C-04
anchor_id: C-S12-A2
variant_id: V05
variant_type: PRG
task_domain: Physiotherapy
utterance: "Basically, the entire therapy sequence is finished now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-12-A2-V06
lineage_id: C-S12-A2
scenario_id: C-S12
subtype_id: C-04
anchor_id: C-S12-A2
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "I’ve gone through all the therapy exercises; there’s nothing left in the therapy routine."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-12-A3-V01
lineage_id: C-S12-A3
scenario_id: C-S12
subtype_id: C-04
anchor_id: C-S12-A3
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "I finished all the exercises in the therapy session routine."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-12-A3-V02
lineage_id: C-S12-A3
scenario_id: C-S12
subtype_id: C-04
anchor_id: C-S12-A3
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "Look, every step of the therapy sequence has been completed."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-12-A3-V03
lineage_id: C-S12-A3
scenario_id: C-S12
subtype_id: C-04
anchor_id: C-S12-A3
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "Look, i’ve worked through the whole physio routine."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-12-A3-V04
lineage_id: C-S12-A3
scenario_id: C-S12
subtype_id: C-04
anchor_id: C-S12-A3
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "You know, i completed every required physiotherapy step, so the therapy routine is finished."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-12-A3-V05
lineage_id: C-S12-A3
scenario_id: C-S12
subtype_id: C-04
anchor_id: C-S12-A3
variant_id: V05
variant_type: PRG
task_domain: Physiotherapy
utterance: "Right, the entire therapy sequence is finished now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-12-A3-V06
lineage_id: C-S12-A3
scenario_id: C-S12
subtype_id: C-04
anchor_id: C-S12-A3
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "I’ve gone through all the therapy session exercises; there’s nothing left in the therapy routine."
execution_status: Completed
validation_status: candidate
```

## C-S13 — C-04 Multi-Step Completion

### Scenario

The user indicates that all required components of a multi-step exercise routine have been completed.

### Target task domain

Exercise

### Stage 1 anchors

- **A1:** I finished all five sets.
- **A2:** I completed every exercise in the routine.
- **A3:** All the workout steps are done.

### Semantic invariant

The target task has been executed and is complete.

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I finished all five sets. |
| A1 | V02 | SYN | Every exercise in the routine has been completed. |
| A1 | V03 | NAT | I got through the whole workout. |
| A1 | V04 | EXP | I completed every required set and exercise, so the workout is finished. |
| A1 | V05 | PRG | The full exercise routine is complete. |
| A1 | V06 | DSC | I’ve worked through every set; there’s nothing left to do in the workout. |
| A2 | V01 | LEX | Honestly, i finished all five sets. |
| A2 | V02 | SYN | Okay, every exercise in the routine has been completed. |
| A2 | V03 | NAT | Honestly, i got through the whole workout. |
| A2 | V04 | EXP | As I said, i completed every required set and exercise, so the workout is finished. |
| A2 | V05 | PRG | Right, the full exercise routine is complete. |
| A2 | V06 | DSC | To be honest, i’ve worked through every set; there’s nothing left to do in the workout. |
| A3 | V01 | LEX | To be honest, i finished all five sets. |
| A3 | V02 | SYN | I mean, every exercise in the routine has been completed. |
| A3 | V03 | NAT | Right, i got through the whole workout. |
| A3 | V04 | EXP | I completed every required set and exercise, so the exercise routine is finished. |
| A3 | V05 | PRG | To be honest, the full exercise routine is complete. |
| A3 | V06 | DSC | I’ve worked through every set; there’s nothing left to do in the exercise routine. |

### Production records

```yaml
example_id: C3A-13-A1-V01
lineage_id: C-S13-A1
scenario_id: C-S13
subtype_id: C-04
anchor_id: C-S13-A1
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "I finished all five sets."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-13-A1-V02
lineage_id: C-S13-A1
scenario_id: C-S13
subtype_id: C-04
anchor_id: C-S13-A1
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "Every exercise in the routine has been completed."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-13-A1-V03
lineage_id: C-S13-A1
scenario_id: C-S13
subtype_id: C-04
anchor_id: C-S13-A1
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "I got through the whole workout."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-13-A1-V04
lineage_id: C-S13-A1
scenario_id: C-S13
subtype_id: C-04
anchor_id: C-S13-A1
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "I completed every required set and exercise, so the workout is finished."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-13-A1-V05
lineage_id: C-S13-A1
scenario_id: C-S13
subtype_id: C-04
anchor_id: C-S13-A1
variant_id: V05
variant_type: PRG
task_domain: Exercise
utterance: "The full exercise routine is complete."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-13-A1-V06
lineage_id: C-S13-A1
scenario_id: C-S13
subtype_id: C-04
anchor_id: C-S13-A1
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "I’ve worked through every set; there’s nothing left to do in the workout."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-13-A2-V01
lineage_id: C-S13-A2
scenario_id: C-S13
subtype_id: C-04
anchor_id: C-S13-A2
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "Honestly, i finished all five sets."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-13-A2-V02
lineage_id: C-S13-A2
scenario_id: C-S13
subtype_id: C-04
anchor_id: C-S13-A2
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "Okay, every exercise in the routine has been completed."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-13-A2-V03
lineage_id: C-S13-A2
scenario_id: C-S13
subtype_id: C-04
anchor_id: C-S13-A2
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "Honestly, i got through the whole workout."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-13-A2-V04
lineage_id: C-S13-A2
scenario_id: C-S13
subtype_id: C-04
anchor_id: C-S13-A2
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "As I said, i completed every required set and exercise, so the workout is finished."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-13-A2-V05
lineage_id: C-S13-A2
scenario_id: C-S13
subtype_id: C-04
anchor_id: C-S13-A2
variant_id: V05
variant_type: PRG
task_domain: Exercise
utterance: "Right, the full exercise routine is complete."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-13-A2-V06
lineage_id: C-S13-A2
scenario_id: C-S13
subtype_id: C-04
anchor_id: C-S13-A2
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "To be honest, i’ve worked through every set; there’s nothing left to do in the workout."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-13-A3-V01
lineage_id: C-S13-A3
scenario_id: C-S13
subtype_id: C-04
anchor_id: C-S13-A3
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "To be honest, i finished all five sets."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-13-A3-V02
lineage_id: C-S13-A3
scenario_id: C-S13
subtype_id: C-04
anchor_id: C-S13-A3
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "I mean, every exercise in the routine has been completed."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-13-A3-V03
lineage_id: C-S13-A3
scenario_id: C-S13
subtype_id: C-04
anchor_id: C-S13-A3
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "Right, i got through the whole workout."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-13-A3-V04
lineage_id: C-S13-A3
scenario_id: C-S13
subtype_id: C-04
anchor_id: C-S13-A3
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "I completed every required set and exercise, so the exercise routine is finished."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-13-A3-V05
lineage_id: C-S13-A3
scenario_id: C-S13
subtype_id: C-04
anchor_id: C-S13-A3
variant_id: V05
variant_type: PRG
task_domain: Exercise
utterance: "To be honest, the full exercise routine is complete."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-13-A3-V06
lineage_id: C-S13-A3
scenario_id: C-S13
subtype_id: C-04
anchor_id: C-S13-A3
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "I’ve worked through every set; there’s nothing left to do in the exercise routine."
execution_status: Completed
validation_status: candidate
```

## C-S14 — C-05 Completion with Additional Commentary

### Scenario

The user explicitly completes the medication task and adds commentary that does not change the completed state.

### Target task domain

Medication

### Stage 1 anchors

- **A1:** I took the medication, although I was a little late.
- **A2:** I’ve finished the medicine; I’m feeling tired today.
- **A3:** The dose is done, and I can get back to work now.

### Semantic invariant

The target task has been executed and is complete.

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I took the medication, although I was a little late. |
| A1 | V02 | SYN | The medication has been taken, even though I was running late. |
| A1 | V03 | NAT | I’ve taken it—I was late today, though. |
| A1 | V04 | EXP | I completed the medication task despite being late; the dose has been taken. |
| A1 | V05 | PRG | The medication is finished now, although I was delayed. |
| A1 | V06 | DSC | I’m done with the dose; I was running late, but it’s taken now. |
| A2 | V01 | LEX | As I said, i took the medication, although I was a little late. |
| A2 | V02 | SYN | Basically, the medication has been taken, even though I was running late. |
| A2 | V03 | NAT | So, i’ve taken it—I was late today, though. |
| A2 | V04 | EXP | To be honest, i completed the medication task despite being late; the dose has been taken. |
| A2 | V05 | PRG | Basically, the medication is finished now, although I was delayed. |
| A2 | V06 | DSC | I mean, i’m done with the dose; I was running late, but it’s taken now. |
| A3 | V01 | LEX | I took my dose, although I was a little late. |
| A3 | V02 | SYN | I mean, the medication has been taken, even though I was running late. |
| A3 | V03 | NAT | Look, i’ve taken it—I was late today, though. |
| A3 | V04 | EXP | I completed my dose task despite being late; the dose has been taken. |
| A3 | V05 | PRG | Okay, the medication is finished now, although I was delayed. |
| A3 | V06 | DSC | As I said, i’m done with the dose; I was running late, but it’s taken now. |

### Production records

```yaml
example_id: C3A-14-A1-V01
lineage_id: C-S14-A1
scenario_id: C-S14
subtype_id: C-05
anchor_id: C-S14-A1
variant_id: V01
variant_type: LEX
task_domain: Medication
utterance: "I took the medication, although I was a little late."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-14-A1-V02
lineage_id: C-S14-A1
scenario_id: C-S14
subtype_id: C-05
anchor_id: C-S14-A1
variant_id: V02
variant_type: SYN
task_domain: Medication
utterance: "The medication has been taken, even though I was running late."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-14-A1-V03
lineage_id: C-S14-A1
scenario_id: C-S14
subtype_id: C-05
anchor_id: C-S14-A1
variant_id: V03
variant_type: NAT
task_domain: Medication
utterance: "I’ve taken it—I was late today, though."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-14-A1-V04
lineage_id: C-S14-A1
scenario_id: C-S14
subtype_id: C-05
anchor_id: C-S14-A1
variant_id: V04
variant_type: EXP
task_domain: Medication
utterance: "I completed the medication task despite being late; the dose has been taken."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-14-A1-V05
lineage_id: C-S14-A1
scenario_id: C-S14
subtype_id: C-05
anchor_id: C-S14-A1
variant_id: V05
variant_type: PRG
task_domain: Medication
utterance: "The medication is finished now, although I was delayed."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-14-A1-V06
lineage_id: C-S14-A1
scenario_id: C-S14
subtype_id: C-05
anchor_id: C-S14-A1
variant_id: V06
variant_type: DSC
task_domain: Medication
utterance: "I’m done with the dose; I was running late, but it’s taken now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-14-A2-V01
lineage_id: C-S14-A2
scenario_id: C-S14
subtype_id: C-05
anchor_id: C-S14-A2
variant_id: V01
variant_type: LEX
task_domain: Medication
utterance: "As I said, i took the medication, although I was a little late."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-14-A2-V02
lineage_id: C-S14-A2
scenario_id: C-S14
subtype_id: C-05
anchor_id: C-S14-A2
variant_id: V02
variant_type: SYN
task_domain: Medication
utterance: "Basically, the medication has been taken, even though I was running late."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-14-A2-V03
lineage_id: C-S14-A2
scenario_id: C-S14
subtype_id: C-05
anchor_id: C-S14-A2
variant_id: V03
variant_type: NAT
task_domain: Medication
utterance: "So, i’ve taken it—I was late today, though."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-14-A2-V04
lineage_id: C-S14-A2
scenario_id: C-S14
subtype_id: C-05
anchor_id: C-S14-A2
variant_id: V04
variant_type: EXP
task_domain: Medication
utterance: "To be honest, i completed the medication task despite being late; the dose has been taken."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-14-A2-V05
lineage_id: C-S14-A2
scenario_id: C-S14
subtype_id: C-05
anchor_id: C-S14-A2
variant_id: V05
variant_type: PRG
task_domain: Medication
utterance: "Basically, the medication is finished now, although I was delayed."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-14-A2-V06
lineage_id: C-S14-A2
scenario_id: C-S14
subtype_id: C-05
anchor_id: C-S14-A2
variant_id: V06
variant_type: DSC
task_domain: Medication
utterance: "I mean, i’m done with the dose; I was running late, but it’s taken now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-14-A3-V01
lineage_id: C-S14-A3
scenario_id: C-S14
subtype_id: C-05
anchor_id: C-S14-A3
variant_id: V01
variant_type: LEX
task_domain: Medication
utterance: "I took my dose, although I was a little late."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-14-A3-V02
lineage_id: C-S14-A3
scenario_id: C-S14
subtype_id: C-05
anchor_id: C-S14-A3
variant_id: V02
variant_type: SYN
task_domain: Medication
utterance: "I mean, the medication has been taken, even though I was running late."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-14-A3-V03
lineage_id: C-S14-A3
scenario_id: C-S14
subtype_id: C-05
anchor_id: C-S14-A3
variant_id: V03
variant_type: NAT
task_domain: Medication
utterance: "Look, i’ve taken it—I was late today, though."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-14-A3-V04
lineage_id: C-S14-A3
scenario_id: C-S14
subtype_id: C-05
anchor_id: C-S14-A3
variant_id: V04
variant_type: EXP
task_domain: Medication
utterance: "I completed my dose task despite being late; the dose has been taken."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-14-A3-V05
lineage_id: C-S14-A3
scenario_id: C-S14
subtype_id: C-05
anchor_id: C-S14-A3
variant_id: V05
variant_type: PRG
task_domain: Medication
utterance: "Okay, the medication is finished now, although I was delayed."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-14-A3-V06
lineage_id: C-S14-A3
scenario_id: C-S14
subtype_id: C-05
anchor_id: C-S14-A3
variant_id: V06
variant_type: DSC
task_domain: Medication
utterance: "As I said, i’m done with the dose; I was running late, but it’s taken now."
execution_status: Completed
validation_status: candidate
```

## C-S15 — C-05 Completion with Additional Commentary

### Scenario

The user explicitly completes the exercise task and adds commentary that does not change the completed state.

### Target task domain

Exercise

### Stage 1 anchors

- **A1:** I finished the workout, and it was harder than usual.
- **A2:** I completed my exercise even though I was tired.
- **A3:** The workout is done; I’m going to rest now.

### Semantic invariant

The target task has been executed and is complete.

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I finished the workout, and it was harder than usual. |
| A1 | V02 | SYN | The workout has been completed, although it was harder than usual. |
| A1 | V03 | NAT | I’m done with the workout—it was pretty tough today. |
| A1 | V04 | EXP | I completed the exercise task even though I was tired; the workout is finished. |
| A1 | V05 | PRG | The exercise is finished now, despite being more difficult than usual. |
| A1 | V06 | DSC | That’s done—I finished the workout, so I’m going to rest now. |
| A2 | V01 | LEX | I finished the routine, and it was harder than usual. |
| A2 | V02 | SYN | I must say, the workout has been completed, although it was harder than usual. |
| A2 | V03 | NAT | Listen, i’m done with the workout—it was pretty tough today. |
| A2 | V04 | EXP | Right, i completed the exercise task even though I was tired; the workout is finished. |
| A2 | V05 | PRG | Well, the exercise is finished now, despite being more difficult than usual. |
| A2 | V06 | DSC | I must say, that’s done—I finished the workout, so I’m going to rest now. |
| A3 | V01 | LEX | I finished the exercise routine, and it was harder than usual. |
| A3 | V02 | SYN | Right, the workout has been completed, although it was harder than usual. |
| A3 | V03 | NAT | I’m done with the exercise routine—it was pretty tough today. |
| A3 | V04 | EXP | I completed the exercise routine task even though I was tired; the workout is finished. |
| A3 | V05 | PRG | I mean, the exercise is finished now, despite being more difficult than usual. |
| A3 | V06 | DSC | That’s done—I finished the exercise routine, so I’m going to rest now. |

### Production records

```yaml
example_id: C3A-15-A1-V01
lineage_id: C-S15-A1
scenario_id: C-S15
subtype_id: C-05
anchor_id: C-S15-A1
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "I finished the workout, and it was harder than usual."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-15-A1-V02
lineage_id: C-S15-A1
scenario_id: C-S15
subtype_id: C-05
anchor_id: C-S15-A1
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "The workout has been completed, although it was harder than usual."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-15-A1-V03
lineage_id: C-S15-A1
scenario_id: C-S15
subtype_id: C-05
anchor_id: C-S15-A1
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "I’m done with the workout—it was pretty tough today."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-15-A1-V04
lineage_id: C-S15-A1
scenario_id: C-S15
subtype_id: C-05
anchor_id: C-S15-A1
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "I completed the exercise task even though I was tired; the workout is finished."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-15-A1-V05
lineage_id: C-S15-A1
scenario_id: C-S15
subtype_id: C-05
anchor_id: C-S15-A1
variant_id: V05
variant_type: PRG
task_domain: Exercise
utterance: "The exercise is finished now, despite being more difficult than usual."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-15-A1-V06
lineage_id: C-S15-A1
scenario_id: C-S15
subtype_id: C-05
anchor_id: C-S15-A1
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "That’s done—I finished the workout, so I’m going to rest now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-15-A2-V01
lineage_id: C-S15-A2
scenario_id: C-S15
subtype_id: C-05
anchor_id: C-S15-A2
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "I finished the routine, and it was harder than usual."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-15-A2-V02
lineage_id: C-S15-A2
scenario_id: C-S15
subtype_id: C-05
anchor_id: C-S15-A2
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "I must say, the workout has been completed, although it was harder than usual."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-15-A2-V03
lineage_id: C-S15-A2
scenario_id: C-S15
subtype_id: C-05
anchor_id: C-S15-A2
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "Listen, i’m done with the workout—it was pretty tough today."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-15-A2-V04
lineage_id: C-S15-A2
scenario_id: C-S15
subtype_id: C-05
anchor_id: C-S15-A2
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "Right, i completed the exercise task even though I was tired; the workout is finished."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-15-A2-V05
lineage_id: C-S15-A2
scenario_id: C-S15
subtype_id: C-05
anchor_id: C-S15-A2
variant_id: V05
variant_type: PRG
task_domain: Exercise
utterance: "Well, the exercise is finished now, despite being more difficult than usual."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-15-A2-V06
lineage_id: C-S15-A2
scenario_id: C-S15
subtype_id: C-05
anchor_id: C-S15-A2
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "I must say, that’s done—I finished the workout, so I’m going to rest now."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-15-A3-V01
lineage_id: C-S15-A3
scenario_id: C-S15
subtype_id: C-05
anchor_id: C-S15-A3
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "I finished the exercise routine, and it was harder than usual."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-15-A3-V02
lineage_id: C-S15-A3
scenario_id: C-S15
subtype_id: C-05
anchor_id: C-S15-A3
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "Right, the workout has been completed, although it was harder than usual."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-15-A3-V03
lineage_id: C-S15-A3
scenario_id: C-S15
subtype_id: C-05
anchor_id: C-S15-A3
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "I’m done with the exercise routine—it was pretty tough today."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-15-A3-V04
lineage_id: C-S15-A3
scenario_id: C-S15
subtype_id: C-05
anchor_id: C-S15-A3
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "I completed the exercise routine task even though I was tired; the workout is finished."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-15-A3-V05
lineage_id: C-S15-A3
scenario_id: C-S15
subtype_id: C-05
anchor_id: C-S15-A3
variant_id: V05
variant_type: PRG
task_domain: Exercise
utterance: "I mean, the exercise is finished now, despite being more difficult than usual."
execution_status: Completed
validation_status: candidate
```

```yaml
example_id: C3A-15-A3-V06
lineage_id: C-S15-A3
scenario_id: C-S15
subtype_id: C-05
anchor_id: C-S15-A3
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "That’s done—I finished the exercise routine, so I’m going to rest now."
execution_status: Completed
validation_status: candidate
```

## 6. Acceptance Criteria

### 6.1 Semantic fidelity
- The utterance belongs to the same semantic scenario as its parent anchor.
- Execution has occurred.
- Completion is established rather than merely intended.

### 6.2 Linguistic quality
- The utterance is grammatical and natural in conversational use.
- The variant expresses meaningful linguistic variation rather than mechanical synonym replacement.
- The utterance remains understandable without requiring the reader to infer unsupported facts.

### 6.3 Shortcut resistance
- The utterance does not depend on one fixed completion keyword.
- Completion remains identifiable when lexical realization changes.
- Repeated templates are avoided across unrelated scenarios.

### 6.4 Boundary safety
- The utterance cannot reasonably be interpreted as `Not Started`.
- The utterance cannot reasonably be interpreted as `In Progress`.
- Commentary or temporal framing does not introduce an unfinished remainder.

### 6.5 Lineage integrity
- Every variant remains attached to its Stage 1 scenario.
- Anchor-specific realizations preserve the same semantic subtype and execution condition.
- No descendant is used to introduce a new semantic scenario.

## 7. Quality-Control Requirements

Human validation should assess semantic fidelity, naturalness, completion evidence, boundary safety, and contextual plausibility. Automated validation should verify identifier uniqueness, schema conformity, lineage consistency, duplicate similarity, and execution-status consistency.

Any variant that weakens completion evidence, introduces unfinished execution, or changes the semantic scenario must be rejected or rewritten before acceptance.

## 8. Resource Accounting

```text
15 Stage 1 scenarios
× 3 anchors per scenario
× 6 standard Stage 3A variants per anchor
= 270 candidate variants
```

This is a Stage 3A construction capacity. Acceptance into the final dataset remains subject to semantic, linguistic, boundary, duplication, and leakage validation.

## 9. Final Semantic Constraint

> Stage 3A changes how an existing `Completed` scenario is expressed; it does not change the fact that the target task has reached completion.