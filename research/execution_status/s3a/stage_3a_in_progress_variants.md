# Execution Status Dataset — Stage 3A Linguistic Expansion: In Progress

## 1. Scope

This resource contains linguistic expansions of the validated Stage 1 `In Progress` execution scenarios. Each record is a realization of an existing scenario; Stage 3A does not create new semantic scenarios.

```yaml
execution_status: In Progress
execution_started: true
execution_completed: false
```

## 2. Semantic Invariants

Every variant preserves:
- actual initiation of the target task;
- unfinished execution at the time represented by the utterance;
- the same Stage 1 semantic subtype and scenario;
- the same target-task domain;
- the same execution condition and relevant context;
- the distinction between execution status and planning, scheduling, motivation, barriers, dialogue purpose, or response category.

## 3. Standard Variant Types

| Code | Variant type | Construction role |
|---|---|---|
| V01 | LEX | Lexical variation |
| V02 | SYN | Syntactic variation |
| V03 | NAT | Natural conversational phrasing |
| V04 | EXP | Explicit semantic realization |
| V05 | LEN | Length variation |
| V06 | DSC | Discourse/contextual variation |

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
execution_status: In Progress
validation_status: candidate
```

`validation_status` records construction status and is not an ontology label.

## 5. Construction Rules

1. A variant must remain within the semantic boundaries of its parent Stage 1 scenario.
2. Execution must already have begun.
3. Full completion must not be established or implied.
4. Partial execution must retain unfinished work.
5. Temporary interruption remains `In Progress` when execution began before the interruption.
6. Near completion remains `In Progress` while any required execution remains.
7. Future continuation may be mentioned only as context for an already-started task.
8. Individual words such as `started`, `doing`, `left`, `almost`, or `pause` must not function as the sole basis for classification.
9. Variants must be natural utterances rather than mechanical synonym substitutions.
10. No new task state, dialogue purpose, persuasion barrier, or scheduling state may be introduced.

---

## IP-S01 — IP-01 Direct Ongoing Execution

### Semantic scenario

The user is actively performing the exercise at the time of the utterance.

**Task domain:** Exercise

### Stage 1 parent anchors

| Anchor | Utterance |
|---|---|
| A1 | I’m doing the exercise right now. |
| A2 | I’m exercising at the moment. |
| A3 | I’m in the middle of the exercise. |

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I’m carrying out the exercise now. |
| A1 | V02 | SYN | I’m currently performing the exercise. |
| A1 | V03 | NAT | I’m in the middle of my workout right now. |
| A1 | V04 | EXP | I’ve already begun the exercise, and I’m still working through it. |
| A1 | V05 | LEN | I’m doing the exercise now; I haven’t finished the whole routine. |
| A1 | V06 | DSC | The exercise is underway on my side at the moment. |
| A2 | V01 | LEX | So, i’m carrying out the exercise now. |
| A2 | V02 | SYN | Okay, i’m currently performing the exercise. |
| A2 | V03 | NAT | From where I am, i’m in the middle of my workout right now. |
| A2 | V04 | EXP | Well, i’ve already begun the exercise, and I’m still working through it. |
| A2 | V05 | LEN | Okay, i’m doing the exercise now; I haven’t finished the whole routine. |
| A2 | V06 | DSC | In this session, the exercise is underway on my side at the moment. |
| A3 | V01 | LEX | Well, i’m carrying out the exercise now. |
| A3 | V02 | SYN | Right now, i’m currently performing the exercise. |
| A3 | V03 | NAT | Look, i’m in the middle of my workout right now. |
| A3 | V04 | EXP | At the moment, i’ve already begun the exercise, and I’m still working through it. |
| A3 | V05 | LEN | Well, i’m doing the exercise now; I haven’t finished the whole routine. |
| A3 | V06 | DSC | I mean, in this session, the exercise is underway on my side at the moment. |

### Production records

```yaml
example_id: IP3A-S01-A1-V01
lineage_id: IP-S01
scenario_id: IP-S01
subtype_id: IP-01
anchor_id: IP-S01-A1
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "I’m carrying out the exercise now."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S01-A1-V02
lineage_id: IP-S01
scenario_id: IP-S01
subtype_id: IP-01
anchor_id: IP-S01-A1
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "I’m currently performing the exercise."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S01-A1-V03
lineage_id: IP-S01
scenario_id: IP-S01
subtype_id: IP-01
anchor_id: IP-S01-A1
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "I’m in the middle of my workout right now."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S01-A1-V04
lineage_id: IP-S01
scenario_id: IP-S01
subtype_id: IP-01
anchor_id: IP-S01-A1
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "I’ve already begun the exercise, and I’m still working through it."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S01-A1-V05
lineage_id: IP-S01
scenario_id: IP-S01
subtype_id: IP-01
anchor_id: IP-S01-A1
variant_id: V05
variant_type: LEN
task_domain: Exercise
utterance: "I’m doing the exercise now; I haven’t finished the whole routine."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S01-A1-V06
lineage_id: IP-S01
scenario_id: IP-S01
subtype_id: IP-01
anchor_id: IP-S01-A1
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "The exercise is underway on my side at the moment."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S01-A2-V01
lineage_id: IP-S01
scenario_id: IP-S01
subtype_id: IP-01
anchor_id: IP-S01-A2
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "So, i’m carrying out the exercise now."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S01-A2-V02
lineage_id: IP-S01
scenario_id: IP-S01
subtype_id: IP-01
anchor_id: IP-S01-A2
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "Okay, i’m currently performing the exercise."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S01-A2-V03
lineage_id: IP-S01
scenario_id: IP-S01
subtype_id: IP-01
anchor_id: IP-S01-A2
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "From where I am, i’m in the middle of my workout right now."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S01-A2-V04
lineage_id: IP-S01
scenario_id: IP-S01
subtype_id: IP-01
anchor_id: IP-S01-A2
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "Well, i’ve already begun the exercise, and I’m still working through it."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S01-A2-V05
lineage_id: IP-S01
scenario_id: IP-S01
subtype_id: IP-01
anchor_id: IP-S01-A2
variant_id: V05
variant_type: LEN
task_domain: Exercise
utterance: "Okay, i’m doing the exercise now; I haven’t finished the whole routine."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S01-A2-V06
lineage_id: IP-S01
scenario_id: IP-S01
subtype_id: IP-01
anchor_id: IP-S01-A2
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "In this session, the exercise is underway on my side at the moment."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S01-A3-V01
lineage_id: IP-S01
scenario_id: IP-S01
subtype_id: IP-01
anchor_id: IP-S01-A3
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "Well, i’m carrying out the exercise now."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S01-A3-V02
lineage_id: IP-S01
scenario_id: IP-S01
subtype_id: IP-01
anchor_id: IP-S01-A3
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "Right now, i’m currently performing the exercise."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S01-A3-V03
lineage_id: IP-S01
scenario_id: IP-S01
subtype_id: IP-01
anchor_id: IP-S01-A3
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "Look, i’m in the middle of my workout right now."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S01-A3-V04
lineage_id: IP-S01
scenario_id: IP-S01
subtype_id: IP-01
anchor_id: IP-S01-A3
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "At the moment, i’ve already begun the exercise, and I’m still working through it."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S01-A3-V05
lineage_id: IP-S01
scenario_id: IP-S01
subtype_id: IP-01
anchor_id: IP-S01-A3
variant_id: V05
variant_type: LEN
task_domain: Exercise
utterance: "Well, i’m doing the exercise now; I haven’t finished the whole routine."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S01-A3-V06
lineage_id: IP-S01
scenario_id: IP-S01
subtype_id: IP-01
anchor_id: IP-S01-A3
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "I mean, in this session, the exercise is underway on my side at the moment."
execution_status: In Progress
validation_status: candidate
```

## IP-S02 — IP-01 Direct Ongoing Execution

### Semantic scenario

The user is actively consuming the required water at the time of the utterance.

**Task domain:** Hydration

### Stage 1 parent anchors

| Anchor | Utterance |
|---|---|
| A1 | I’m drinking the water now. |
| A2 | I’m having the water right now. |
| A3 | I’m working through my water target now. |

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I’m having some water right now. |
| A1 | V02 | SYN | The water is what I’m drinking at the moment. |
| A1 | V03 | NAT | I’m drinking it at the moment. |
| A1 | V04 | EXP | I’ve started drinking the water, and I’m still on it. |
| A1 | V05 | LEN | I’m drinking now, but I haven’t finished the amount yet. |
| A1 | V06 | DSC | I’ve got the water with me and I’m drinking from it now. |
| A2 | V01 | LEX | So, i’m having some water right now. |
| A2 | V02 | SYN | Right now, the water is what I’m drinking at the moment. |
| A2 | V03 | NAT | From where I am, i’m drinking it at the moment. |
| A2 | V04 | EXP | I mean, i’ve started drinking the water, and I’m still on it. |
| A2 | V05 | LEN | Honestly, i’m drinking now, but I haven’t finished the amount yet. |
| A2 | V06 | DSC | In this session, i’ve got the water with me and I’m drinking from it now. |
| A3 | V01 | LEX | Actually, i’m having some water right now. |
| A3 | V02 | SYN | You know, right now, the water is what I’m drinking at the moment. |
| A3 | V03 | NAT | Listen, i’m drinking it at the moment. |
| A3 | V04 | EXP | At the moment, i’ve started drinking the water, and I’m still on it. |
| A3 | V05 | LEN | Basically, i’m drinking now, but I haven’t finished the amount yet. |
| A3 | V06 | DSC | Look, in this session, i’ve got the water with me and I’m drinking from it now. |

### Production records

```yaml
example_id: IP3A-S02-A1-V01
lineage_id: IP-S02
scenario_id: IP-S02
subtype_id: IP-01
anchor_id: IP-S02-A1
variant_id: V01
variant_type: LEX
task_domain: Hydration
utterance: "I’m having some water right now."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S02-A1-V02
lineage_id: IP-S02
scenario_id: IP-S02
subtype_id: IP-01
anchor_id: IP-S02-A1
variant_id: V02
variant_type: SYN
task_domain: Hydration
utterance: "The water is what I’m drinking at the moment."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S02-A1-V03
lineage_id: IP-S02
scenario_id: IP-S02
subtype_id: IP-01
anchor_id: IP-S02-A1
variant_id: V03
variant_type: NAT
task_domain: Hydration
utterance: "I’m drinking it at the moment."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S02-A1-V04
lineage_id: IP-S02
scenario_id: IP-S02
subtype_id: IP-01
anchor_id: IP-S02-A1
variant_id: V04
variant_type: EXP
task_domain: Hydration
utterance: "I’ve started drinking the water, and I’m still on it."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S02-A1-V05
lineage_id: IP-S02
scenario_id: IP-S02
subtype_id: IP-01
anchor_id: IP-S02-A1
variant_id: V05
variant_type: LEN
task_domain: Hydration
utterance: "I’m drinking now, but I haven’t finished the amount yet."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S02-A1-V06
lineage_id: IP-S02
scenario_id: IP-S02
subtype_id: IP-01
anchor_id: IP-S02-A1
variant_id: V06
variant_type: DSC
task_domain: Hydration
utterance: "I’ve got the water with me and I’m drinking from it now."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S02-A2-V01
lineage_id: IP-S02
scenario_id: IP-S02
subtype_id: IP-01
anchor_id: IP-S02-A2
variant_id: V01
variant_type: LEX
task_domain: Hydration
utterance: "So, i’m having some water right now."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S02-A2-V02
lineage_id: IP-S02
scenario_id: IP-S02
subtype_id: IP-01
anchor_id: IP-S02-A2
variant_id: V02
variant_type: SYN
task_domain: Hydration
utterance: "Right now, the water is what I’m drinking at the moment."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S02-A2-V03
lineage_id: IP-S02
scenario_id: IP-S02
subtype_id: IP-01
anchor_id: IP-S02-A2
variant_id: V03
variant_type: NAT
task_domain: Hydration
utterance: "From where I am, i’m drinking it at the moment."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S02-A2-V04
lineage_id: IP-S02
scenario_id: IP-S02
subtype_id: IP-01
anchor_id: IP-S02-A2
variant_id: V04
variant_type: EXP
task_domain: Hydration
utterance: "I mean, i’ve started drinking the water, and I’m still on it."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S02-A2-V05
lineage_id: IP-S02
scenario_id: IP-S02
subtype_id: IP-01
anchor_id: IP-S02-A2
variant_id: V05
variant_type: LEN
task_domain: Hydration
utterance: "Honestly, i’m drinking now, but I haven’t finished the amount yet."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S02-A2-V06
lineage_id: IP-S02
scenario_id: IP-S02
subtype_id: IP-01
anchor_id: IP-S02-A2
variant_id: V06
variant_type: DSC
task_domain: Hydration
utterance: "In this session, i’ve got the water with me and I’m drinking from it now."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S02-A3-V01
lineage_id: IP-S02
scenario_id: IP-S02
subtype_id: IP-01
anchor_id: IP-S02-A3
variant_id: V01
variant_type: LEX
task_domain: Hydration
utterance: "Actually, i’m having some water right now."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S02-A3-V02
lineage_id: IP-S02
scenario_id: IP-S02
subtype_id: IP-01
anchor_id: IP-S02-A3
variant_id: V02
variant_type: SYN
task_domain: Hydration
utterance: "You know, right now, the water is what I’m drinking at the moment."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S02-A3-V03
lineage_id: IP-S02
scenario_id: IP-S02
subtype_id: IP-01
anchor_id: IP-S02-A3
variant_id: V03
variant_type: NAT
task_domain: Hydration
utterance: "Listen, i’m drinking it at the moment."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S02-A3-V04
lineage_id: IP-S02
scenario_id: IP-S02
subtype_id: IP-01
anchor_id: IP-S02-A3
variant_id: V04
variant_type: EXP
task_domain: Hydration
utterance: "At the moment, i’ve started drinking the water, and I’m still on it."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S02-A3-V05
lineage_id: IP-S02
scenario_id: IP-S02
subtype_id: IP-01
anchor_id: IP-S02-A3
variant_id: V05
variant_type: LEN
task_domain: Hydration
utterance: "Basically, i’m drinking now, but I haven’t finished the amount yet."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S02-A3-V06
lineage_id: IP-S02
scenario_id: IP-S02
subtype_id: IP-01
anchor_id: IP-S02-A3
variant_id: V06
variant_type: DSC
task_domain: Hydration
utterance: "Look, in this session, i’ve got the water with me and I’m drinking from it now."
execution_status: In Progress
validation_status: candidate
```

## IP-S03 — IP-01 Direct Ongoing Execution

### Semantic scenario

The user has started the physiotherapy activity and is still carrying it out.

**Task domain:** Physiotherapy

### Stage 1 parent anchors

| Anchor | Utterance |
|---|---|
| A1 | Yes, I’ve started the physiotherapy and I’m still doing it. |
| A2 | I’ve started already; I’m working through it now. |
| A3 | I’m on it now. |

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I’m carrying on with the physiotherapy right now. |
| A1 | V02 | SYN | I’m currently working through the physiotherapy session. |
| A1 | V03 | NAT | I’m doing the physio at the moment. |
| A1 | V04 | EXP | I’ve begun the session already, and the exercises are still underway. |
| A1 | V05 | LEN | The physiotherapy has started, and I’m not finished yet. |
| A1 | V06 | DSC | The routine is underway right now. |
| A2 | V01 | LEX | So, i’m carrying on with the physiotherapy right now. |
| A2 | V02 | SYN | You know, i’m currently working through the physiotherapy session. |
| A2 | V03 | NAT | From where I am, i’m doing the physio at the moment. |
| A2 | V04 | EXP | So, i’ve begun the session already, and the exercises are still underway. |
| A2 | V05 | LEN | Actually, the physiotherapy has started, and I’m not finished yet. |
| A2 | V06 | DSC | In this session, the routine is underway right now. |
| A3 | V01 | LEX | To be honest, i’m carrying on with the physiotherapy right now. |
| A3 | V02 | SYN | Right now, i’m currently working through the physiotherapy session. |
| A3 | V03 | NAT | I must say, i’m doing the physio at the moment. |
| A3 | V04 | EXP | At the moment, i’ve begun the session already, and the exercises are still underway. |
| A3 | V05 | LEN | I mean, the physiotherapy has started, and I’m not finished yet. |
| A3 | V06 | DSC | Listen, in this session, the routine is underway right now. |

### Production records

```yaml
example_id: IP3A-S03-A1-V01
lineage_id: IP-S03
scenario_id: IP-S03
subtype_id: IP-01
anchor_id: IP-S03-A1
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "I’m carrying on with the physiotherapy right now."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S03-A1-V02
lineage_id: IP-S03
scenario_id: IP-S03
subtype_id: IP-01
anchor_id: IP-S03-A1
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "I’m currently working through the physiotherapy session."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S03-A1-V03
lineage_id: IP-S03
scenario_id: IP-S03
subtype_id: IP-01
anchor_id: IP-S03-A1
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "I’m doing the physio at the moment."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S03-A1-V04
lineage_id: IP-S03
scenario_id: IP-S03
subtype_id: IP-01
anchor_id: IP-S03-A1
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "I’ve begun the session already, and the exercises are still underway."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S03-A1-V05
lineage_id: IP-S03
scenario_id: IP-S03
subtype_id: IP-01
anchor_id: IP-S03-A1
variant_id: V05
variant_type: LEN
task_domain: Physiotherapy
utterance: "The physiotherapy has started, and I’m not finished yet."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S03-A1-V06
lineage_id: IP-S03
scenario_id: IP-S03
subtype_id: IP-01
anchor_id: IP-S03-A1
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "The routine is underway right now."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S03-A2-V01
lineage_id: IP-S03
scenario_id: IP-S03
subtype_id: IP-01
anchor_id: IP-S03-A2
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "So, i’m carrying on with the physiotherapy right now."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S03-A2-V02
lineage_id: IP-S03
scenario_id: IP-S03
subtype_id: IP-01
anchor_id: IP-S03-A2
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "You know, i’m currently working through the physiotherapy session."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S03-A2-V03
lineage_id: IP-S03
scenario_id: IP-S03
subtype_id: IP-01
anchor_id: IP-S03-A2
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "From where I am, i’m doing the physio at the moment."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S03-A2-V04
lineage_id: IP-S03
scenario_id: IP-S03
subtype_id: IP-01
anchor_id: IP-S03-A2
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "So, i’ve begun the session already, and the exercises are still underway."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S03-A2-V05
lineage_id: IP-S03
scenario_id: IP-S03
subtype_id: IP-01
anchor_id: IP-S03-A2
variant_id: V05
variant_type: LEN
task_domain: Physiotherapy
utterance: "Actually, the physiotherapy has started, and I’m not finished yet."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S03-A2-V06
lineage_id: IP-S03
scenario_id: IP-S03
subtype_id: IP-01
anchor_id: IP-S03-A2
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "In this session, the routine is underway right now."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S03-A3-V01
lineage_id: IP-S03
scenario_id: IP-S03
subtype_id: IP-01
anchor_id: IP-S03-A3
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "To be honest, i’m carrying on with the physiotherapy right now."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S03-A3-V02
lineage_id: IP-S03
scenario_id: IP-S03
subtype_id: IP-01
anchor_id: IP-S03-A3
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "Right now, i’m currently working through the physiotherapy session."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S03-A3-V03
lineage_id: IP-S03
scenario_id: IP-S03
subtype_id: IP-01
anchor_id: IP-S03-A3
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "I must say, i’m doing the physio at the moment."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S03-A3-V04
lineage_id: IP-S03
scenario_id: IP-S03
subtype_id: IP-01
anchor_id: IP-S03-A3
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "At the moment, i’ve begun the session already, and the exercises are still underway."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S03-A3-V05
lineage_id: IP-S03
scenario_id: IP-S03
subtype_id: IP-01
anchor_id: IP-S03-A3
variant_id: V05
variant_type: LEN
task_domain: Physiotherapy
utterance: "I mean, the physiotherapy has started, and I’m not finished yet."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S03-A3-V06
lineage_id: IP-S03
scenario_id: IP-S03
subtype_id: IP-01
anchor_id: IP-S03-A3
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "Listen, in this session, the routine is underway right now."
execution_status: In Progress
validation_status: candidate
```

## IP-S04 — IP-02 Partial Execution

### Semantic scenario

The user has completed part of the exercise task while additional execution remains.

**Task domain:** Exercise

### Stage 1 parent anchors

| Anchor | Utterance |
|---|---|
| A1 | I’ve done part of the exercise, but I’m not finished. |
| A2 | I’ve started the exercises; there’s still some left. |
| A3 | I’m partway through the exercise. |

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I’ve completed some of the exercise, but there’s still more. |
| A1 | V02 | SYN | Part of the workout is done, while the rest remains. |
| A1 | V03 | NAT | I’m only partway through the exercises. |
| A1 | V04 | EXP | I’ve already worked through one portion, and I still have the remainder to do. |
| A1 | V05 | LEN | Some of the routine is finished; I still have more to complete. |
| A1 | V06 | DSC | I’ve made it through part of the exercise, with the rest still ahead. |
| A2 | V01 | LEX | So, i’ve completed some of the exercise, but there’s still more. |
| A2 | V02 | SYN | Okay, part of the workout is done, while the rest remains. |
| A2 | V03 | NAT | From where I am, i’m only partway through the exercises. |
| A2 | V04 | EXP | Basically, i’ve already worked through one portion, and I still have the remainder to do. |
| A2 | V05 | LEN | Basically, some of the routine is finished; I still have more to complete. |
| A2 | V06 | DSC | In this session, i’ve made it through part of the exercise, with the rest still ahead. |
| A3 | V01 | LEX | Basically, i’ve completed some of the exercise, but there’s still more. |
| A3 | V02 | SYN | Right now, part of the workout is done, while the rest remains. |
| A3 | V03 | NAT | So, i’m only partway through the exercises. |
| A3 | V04 | EXP | At the moment, i’ve already worked through one portion, and I still have the remainder to do. |
| A3 | V05 | LEN | I mean, some of the routine is finished; I still have more to complete. |
| A3 | V06 | DSC | As I said, in this session, i’ve made it through part of the exercise, with the rest still ahead. |

### Production records

```yaml
example_id: IP3A-S04-A1-V01
lineage_id: IP-S04
scenario_id: IP-S04
subtype_id: IP-02
anchor_id: IP-S04-A1
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "I’ve completed some of the exercise, but there’s still more."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S04-A1-V02
lineage_id: IP-S04
scenario_id: IP-S04
subtype_id: IP-02
anchor_id: IP-S04-A1
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "Part of the workout is done, while the rest remains."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S04-A1-V03
lineage_id: IP-S04
scenario_id: IP-S04
subtype_id: IP-02
anchor_id: IP-S04-A1
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "I’m only partway through the exercises."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S04-A1-V04
lineage_id: IP-S04
scenario_id: IP-S04
subtype_id: IP-02
anchor_id: IP-S04-A1
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "I’ve already worked through one portion, and I still have the remainder to do."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S04-A1-V05
lineage_id: IP-S04
scenario_id: IP-S04
subtype_id: IP-02
anchor_id: IP-S04-A1
variant_id: V05
variant_type: LEN
task_domain: Exercise
utterance: "Some of the routine is finished; I still have more to complete."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S04-A1-V06
lineage_id: IP-S04
scenario_id: IP-S04
subtype_id: IP-02
anchor_id: IP-S04-A1
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "I’ve made it through part of the exercise, with the rest still ahead."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S04-A2-V01
lineage_id: IP-S04
scenario_id: IP-S04
subtype_id: IP-02
anchor_id: IP-S04-A2
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "So, i’ve completed some of the exercise, but there’s still more."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S04-A2-V02
lineage_id: IP-S04
scenario_id: IP-S04
subtype_id: IP-02
anchor_id: IP-S04-A2
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "Okay, part of the workout is done, while the rest remains."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S04-A2-V03
lineage_id: IP-S04
scenario_id: IP-S04
subtype_id: IP-02
anchor_id: IP-S04-A2
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "From where I am, i’m only partway through the exercises."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S04-A2-V04
lineage_id: IP-S04
scenario_id: IP-S04
subtype_id: IP-02
anchor_id: IP-S04-A2
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "Basically, i’ve already worked through one portion, and I still have the remainder to do."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S04-A2-V05
lineage_id: IP-S04
scenario_id: IP-S04
subtype_id: IP-02
anchor_id: IP-S04-A2
variant_id: V05
variant_type: LEN
task_domain: Exercise
utterance: "Basically, some of the routine is finished; I still have more to complete."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S04-A2-V06
lineage_id: IP-S04
scenario_id: IP-S04
subtype_id: IP-02
anchor_id: IP-S04-A2
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "In this session, i’ve made it through part of the exercise, with the rest still ahead."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S04-A3-V01
lineage_id: IP-S04
scenario_id: IP-S04
subtype_id: IP-02
anchor_id: IP-S04-A3
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "Basically, i’ve completed some of the exercise, but there’s still more."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S04-A3-V02
lineage_id: IP-S04
scenario_id: IP-S04
subtype_id: IP-02
anchor_id: IP-S04-A3
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "Right now, part of the workout is done, while the rest remains."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S04-A3-V03
lineage_id: IP-S04
scenario_id: IP-S04
subtype_id: IP-02
anchor_id: IP-S04-A3
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "So, i’m only partway through the exercises."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S04-A3-V04
lineage_id: IP-S04
scenario_id: IP-S04
subtype_id: IP-02
anchor_id: IP-S04-A3
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "At the moment, i’ve already worked through one portion, and I still have the remainder to do."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S04-A3-V05
lineage_id: IP-S04
scenario_id: IP-S04
subtype_id: IP-02
anchor_id: IP-S04-A3
variant_id: V05
variant_type: LEN
task_domain: Exercise
utterance: "I mean, some of the routine is finished; I still have more to complete."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S04-A3-V06
lineage_id: IP-S04
scenario_id: IP-S04
subtype_id: IP-02
anchor_id: IP-S04-A3
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "As I said, in this session, i’ve made it through part of the exercise, with the rest still ahead."
execution_status: In Progress
validation_status: candidate
```

## IP-S05 — IP-02 Partial Execution

### Semantic scenario

The user has consumed part of the required amount of water while some remains.

**Task domain:** Hydration

### Stage 1 parent anchors

| Anchor | Utterance |
|---|---|
| A1 | I’ve drunk half the bottle, but I still have some left. |
| A2 | I’m halfway through the water. |
| A3 | There’s still some of the bottle left for me to drink. |

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I’ve consumed some of the water, but not all of it. |
| A1 | V02 | SYN | Part of the water has been drunk, while some remains. |
| A1 | V03 | NAT | I’m partway through my water. |
| A1 | V04 | EXP | I’ve already had some of the required amount, and I still need the rest. |
| A1 | V05 | LEN | I’ve had part of it, but I haven’t finished the water target. |
| A1 | V06 | DSC | Some of the bottle is gone, and some is still left. |
| A2 | V01 | LEX | So, i’ve consumed some of the water, but not all of it. |
| A2 | V02 | SYN | Basically, part of the water has been drunk, while some remains. |
| A2 | V03 | NAT | From where I am, i’m partway through my water. |
| A2 | V04 | EXP | As I said, i’ve already had some of the required amount, and I still need the rest. |
| A2 | V05 | LEN | To be honest, i’ve had part of it, but I haven’t finished the water target. |
| A2 | V06 | DSC | In this session, some of the bottle is gone, and some is still left. |
| A3 | V01 | LEX | As I said, i’ve consumed some of the water, but not all of it. |
| A3 | V02 | SYN | Right now, part of the water has been drunk, while some remains. |
| A3 | V03 | NAT | To be honest, i’m partway through my water. |
| A3 | V04 | EXP | At the moment, i’ve already had some of the required amount, and I still need the rest. |
| A3 | V05 | LEN | So, i’ve had part of it, but I haven’t finished the water target. |
| A3 | V06 | DSC | Right, in this session, some of the bottle is gone, and some is still left. |

### Production records

```yaml
example_id: IP3A-S05-A1-V01
lineage_id: IP-S05
scenario_id: IP-S05
subtype_id: IP-02
anchor_id: IP-S05-A1
variant_id: V01
variant_type: LEX
task_domain: Hydration
utterance: "I’ve consumed some of the water, but not all of it."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S05-A1-V02
lineage_id: IP-S05
scenario_id: IP-S05
subtype_id: IP-02
anchor_id: IP-S05-A1
variant_id: V02
variant_type: SYN
task_domain: Hydration
utterance: "Part of the water has been drunk, while some remains."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S05-A1-V03
lineage_id: IP-S05
scenario_id: IP-S05
subtype_id: IP-02
anchor_id: IP-S05-A1
variant_id: V03
variant_type: NAT
task_domain: Hydration
utterance: "I’m partway through my water."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S05-A1-V04
lineage_id: IP-S05
scenario_id: IP-S05
subtype_id: IP-02
anchor_id: IP-S05-A1
variant_id: V04
variant_type: EXP
task_domain: Hydration
utterance: "I’ve already had some of the required amount, and I still need the rest."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S05-A1-V05
lineage_id: IP-S05
scenario_id: IP-S05
subtype_id: IP-02
anchor_id: IP-S05-A1
variant_id: V05
variant_type: LEN
task_domain: Hydration
utterance: "I’ve had part of it, but I haven’t finished the water target."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S05-A1-V06
lineage_id: IP-S05
scenario_id: IP-S05
subtype_id: IP-02
anchor_id: IP-S05-A1
variant_id: V06
variant_type: DSC
task_domain: Hydration
utterance: "Some of the bottle is gone, and some is still left."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S05-A2-V01
lineage_id: IP-S05
scenario_id: IP-S05
subtype_id: IP-02
anchor_id: IP-S05-A2
variant_id: V01
variant_type: LEX
task_domain: Hydration
utterance: "So, i’ve consumed some of the water, but not all of it."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S05-A2-V02
lineage_id: IP-S05
scenario_id: IP-S05
subtype_id: IP-02
anchor_id: IP-S05-A2
variant_id: V02
variant_type: SYN
task_domain: Hydration
utterance: "Basically, part of the water has been drunk, while some remains."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S05-A2-V03
lineage_id: IP-S05
scenario_id: IP-S05
subtype_id: IP-02
anchor_id: IP-S05-A2
variant_id: V03
variant_type: NAT
task_domain: Hydration
utterance: "From where I am, i’m partway through my water."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S05-A2-V04
lineage_id: IP-S05
scenario_id: IP-S05
subtype_id: IP-02
anchor_id: IP-S05-A2
variant_id: V04
variant_type: EXP
task_domain: Hydration
utterance: "As I said, i’ve already had some of the required amount, and I still need the rest."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S05-A2-V05
lineage_id: IP-S05
scenario_id: IP-S05
subtype_id: IP-02
anchor_id: IP-S05-A2
variant_id: V05
variant_type: LEN
task_domain: Hydration
utterance: "To be honest, i’ve had part of it, but I haven’t finished the water target."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S05-A2-V06
lineage_id: IP-S05
scenario_id: IP-S05
subtype_id: IP-02
anchor_id: IP-S05-A2
variant_id: V06
variant_type: DSC
task_domain: Hydration
utterance: "In this session, some of the bottle is gone, and some is still left."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S05-A3-V01
lineage_id: IP-S05
scenario_id: IP-S05
subtype_id: IP-02
anchor_id: IP-S05-A3
variant_id: V01
variant_type: LEX
task_domain: Hydration
utterance: "As I said, i’ve consumed some of the water, but not all of it."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S05-A3-V02
lineage_id: IP-S05
scenario_id: IP-S05
subtype_id: IP-02
anchor_id: IP-S05-A3
variant_id: V02
variant_type: SYN
task_domain: Hydration
utterance: "Right now, part of the water has been drunk, while some remains."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S05-A3-V03
lineage_id: IP-S05
scenario_id: IP-S05
subtype_id: IP-02
anchor_id: IP-S05-A3
variant_id: V03
variant_type: NAT
task_domain: Hydration
utterance: "To be honest, i’m partway through my water."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S05-A3-V04
lineage_id: IP-S05
scenario_id: IP-S05
subtype_id: IP-02
anchor_id: IP-S05-A3
variant_id: V04
variant_type: EXP
task_domain: Hydration
utterance: "At the moment, i’ve already had some of the required amount, and I still need the rest."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S05-A3-V05
lineage_id: IP-S05
scenario_id: IP-S05
subtype_id: IP-02
anchor_id: IP-S05-A3
variant_id: V05
variant_type: LEN
task_domain: Hydration
utterance: "So, i’ve had part of it, but I haven’t finished the water target."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S05-A3-V06
lineage_id: IP-S05
scenario_id: IP-S05
subtype_id: IP-02
anchor_id: IP-S05-A3
variant_id: V06
variant_type: DSC
task_domain: Hydration
utterance: "Right, in this session, some of the bottle is gone, and some is still left."
execution_status: In Progress
validation_status: candidate
```

## IP-S06 — IP-02 Partial Execution

### Semantic scenario

The user has begun the medication routine but has not completed the required execution.

**Task domain:** Medication

### Stage 1 parent anchors

| Anchor | Utterance |
|---|---|
| A1 | I started the medicine routine, but I haven’t finished it. |
| A2 | I’ve begun the routine, but I still have more to do. |
| A3 | I’m not done with the routine yet; I’ve already started. |

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I’ve begun the medication routine, but it’s only partly done. |
| A1 | V02 | SYN | The medication routine has started, although some of it remains. |
| A1 | V03 | NAT | I’m partway through the routine. |
| A1 | V04 | EXP | I’ve already carried out part of the routine, and the remaining part is unfinished. |
| A1 | V05 | LEN | The routine has started, but I still have some to complete. |
| A1 | V06 | DSC | I’ve made a start on the routine; the rest is still ahead. |
| A2 | V01 | LEX | So, i’ve begun the medication routine, but it’s only partly done. |
| A2 | V02 | SYN | Right now, the medication routine has started, although some of it remains. |
| A2 | V03 | NAT | From where I am, i’m partway through the routine. |
| A2 | V04 | EXP | To be honest, i’ve already carried out part of the routine, and the remaining part is unfinished. |
| A2 | V05 | LEN | Okay, the routine has started, but I still have some to complete. |
| A2 | V06 | DSC | In this session, i’ve made a start on the routine; the rest is still ahead. |
| A3 | V01 | LEX | I mean, i’ve begun the medication routine, but it’s only partly done. |
| A3 | V02 | SYN | Well, right now, the medication routine has started, although some of it remains. |
| A3 | V03 | NAT | I must say, i’m partway through the routine. |
| A3 | V04 | EXP | At the moment, i’ve already carried out part of the routine, and the remaining part is unfinished. |
| A3 | V05 | LEN | Honestly, the routine has started, but I still have some to complete. |
| A3 | V06 | DSC | I must say, in this session, i’ve made a start on the routine; the rest is still ahead. |

### Production records

```yaml
example_id: IP3A-S06-A1-V01
lineage_id: IP-S06
scenario_id: IP-S06
subtype_id: IP-02
anchor_id: IP-S06-A1
variant_id: V01
variant_type: LEX
task_domain: Medication
utterance: "I’ve begun the medication routine, but it’s only partly done."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S06-A1-V02
lineage_id: IP-S06
scenario_id: IP-S06
subtype_id: IP-02
anchor_id: IP-S06-A1
variant_id: V02
variant_type: SYN
task_domain: Medication
utterance: "The medication routine has started, although some of it remains."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S06-A1-V03
lineage_id: IP-S06
scenario_id: IP-S06
subtype_id: IP-02
anchor_id: IP-S06-A1
variant_id: V03
variant_type: NAT
task_domain: Medication
utterance: "I’m partway through the routine."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S06-A1-V04
lineage_id: IP-S06
scenario_id: IP-S06
subtype_id: IP-02
anchor_id: IP-S06-A1
variant_id: V04
variant_type: EXP
task_domain: Medication
utterance: "I’ve already carried out part of the routine, and the remaining part is unfinished."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S06-A1-V05
lineage_id: IP-S06
scenario_id: IP-S06
subtype_id: IP-02
anchor_id: IP-S06-A1
variant_id: V05
variant_type: LEN
task_domain: Medication
utterance: "The routine has started, but I still have some to complete."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S06-A1-V06
lineage_id: IP-S06
scenario_id: IP-S06
subtype_id: IP-02
anchor_id: IP-S06-A1
variant_id: V06
variant_type: DSC
task_domain: Medication
utterance: "I’ve made a start on the routine; the rest is still ahead."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S06-A2-V01
lineage_id: IP-S06
scenario_id: IP-S06
subtype_id: IP-02
anchor_id: IP-S06-A2
variant_id: V01
variant_type: LEX
task_domain: Medication
utterance: "So, i’ve begun the medication routine, but it’s only partly done."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S06-A2-V02
lineage_id: IP-S06
scenario_id: IP-S06
subtype_id: IP-02
anchor_id: IP-S06-A2
variant_id: V02
variant_type: SYN
task_domain: Medication
utterance: "Right now, the medication routine has started, although some of it remains."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S06-A2-V03
lineage_id: IP-S06
scenario_id: IP-S06
subtype_id: IP-02
anchor_id: IP-S06-A2
variant_id: V03
variant_type: NAT
task_domain: Medication
utterance: "From where I am, i’m partway through the routine."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S06-A2-V04
lineage_id: IP-S06
scenario_id: IP-S06
subtype_id: IP-02
anchor_id: IP-S06-A2
variant_id: V04
variant_type: EXP
task_domain: Medication
utterance: "To be honest, i’ve already carried out part of the routine, and the remaining part is unfinished."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S06-A2-V05
lineage_id: IP-S06
scenario_id: IP-S06
subtype_id: IP-02
anchor_id: IP-S06-A2
variant_id: V05
variant_type: LEN
task_domain: Medication
utterance: "Okay, the routine has started, but I still have some to complete."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S06-A2-V06
lineage_id: IP-S06
scenario_id: IP-S06
subtype_id: IP-02
anchor_id: IP-S06-A2
variant_id: V06
variant_type: DSC
task_domain: Medication
utterance: "In this session, i’ve made a start on the routine; the rest is still ahead."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S06-A3-V01
lineage_id: IP-S06
scenario_id: IP-S06
subtype_id: IP-02
anchor_id: IP-S06-A3
variant_id: V01
variant_type: LEX
task_domain: Medication
utterance: "I mean, i’ve begun the medication routine, but it’s only partly done."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S06-A3-V02
lineage_id: IP-S06
scenario_id: IP-S06
subtype_id: IP-02
anchor_id: IP-S06-A3
variant_id: V02
variant_type: SYN
task_domain: Medication
utterance: "Well, right now, the medication routine has started, although some of it remains."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S06-A3-V03
lineage_id: IP-S06
scenario_id: IP-S06
subtype_id: IP-02
anchor_id: IP-S06-A3
variant_id: V03
variant_type: NAT
task_domain: Medication
utterance: "I must say, i’m partway through the routine."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S06-A3-V04
lineage_id: IP-S06
scenario_id: IP-S06
subtype_id: IP-02
anchor_id: IP-S06-A3
variant_id: V04
variant_type: EXP
task_domain: Medication
utterance: "At the moment, i’ve already carried out part of the routine, and the remaining part is unfinished."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S06-A3-V05
lineage_id: IP-S06
scenario_id: IP-S06
subtype_id: IP-02
anchor_id: IP-S06-A3
variant_id: V05
variant_type: LEN
task_domain: Medication
utterance: "Honestly, the routine has started, but I still have some to complete."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S06-A3-V06
lineage_id: IP-S06
scenario_id: IP-S06
subtype_id: IP-02
anchor_id: IP-S06-A3
variant_id: V06
variant_type: DSC
task_domain: Medication
utterance: "I must say, in this session, i’ve made a start on the routine; the rest is still ahead."
execution_status: In Progress
validation_status: candidate
```

## IP-S07 — IP-03 Near Completion

### Semantic scenario

The exercise task is almost finished, but a small amount of execution remains.

**Task domain:** Exercise

### Stage 1 parent anchors

| Anchor | Utterance |
|---|---|
| A1 | I’m almost finished with the exercises. |
| A2 | I’m nearly done with the workout. |
| A3 | I’ve got just a little of the exercise left. |

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I’m just about finished with the exercises. |
| A1 | V02 | SYN | The workout is close to completion, but not complete yet. |
| A1 | V03 | NAT | I’m almost done with it. |
| A1 | V04 | EXP | I’ve completed most of the exercise, with only a small part remaining. |
| A1 | V05 | LEN | I’m near the end, but there’s still a little exercise left. |
| A1 | V06 | DSC | Only a small amount remains in the workout. |
| A2 | V01 | LEX | So, i’m just about finished with the exercises. |
| A2 | V02 | SYN | Right now, the workout is close to completion, but not complete yet. |
| A2 | V03 | NAT | From where I am, i’m almost done with it. |
| A2 | V04 | EXP | Listen, i’ve completed most of the exercise, with only a small part remaining. |
| A2 | V05 | LEN | Okay, i’m near the end, but there’s still a little exercise left. |
| A2 | V06 | DSC | In this session, only a small amount remains in the workout. |
| A3 | V01 | LEX | I mean, i’m just about finished with the exercises. |
| A3 | V02 | SYN | Listen, right now, the workout is close to completion, but not complete yet. |
| A3 | V03 | NAT | I mean, i’m almost done with it. |
| A3 | V04 | EXP | At the moment, i’ve completed most of the exercise, with only a small part remaining. |
| A3 | V05 | LEN | Listen, i’m near the end, but there’s still a little exercise left. |
| A3 | V06 | DSC | I mean, in this session, only a small amount remains in the workout. |

### Production records

```yaml
example_id: IP3A-S07-A1-V01
lineage_id: IP-S07
scenario_id: IP-S07
subtype_id: IP-03
anchor_id: IP-S07-A1
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "I’m just about finished with the exercises."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S07-A1-V02
lineage_id: IP-S07
scenario_id: IP-S07
subtype_id: IP-03
anchor_id: IP-S07-A1
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "The workout is close to completion, but not complete yet."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S07-A1-V03
lineage_id: IP-S07
scenario_id: IP-S07
subtype_id: IP-03
anchor_id: IP-S07-A1
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "I’m almost done with it."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S07-A1-V04
lineage_id: IP-S07
scenario_id: IP-S07
subtype_id: IP-03
anchor_id: IP-S07-A1
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "I’ve completed most of the exercise, with only a small part remaining."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S07-A1-V05
lineage_id: IP-S07
scenario_id: IP-S07
subtype_id: IP-03
anchor_id: IP-S07-A1
variant_id: V05
variant_type: LEN
task_domain: Exercise
utterance: "I’m near the end, but there’s still a little exercise left."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S07-A1-V06
lineage_id: IP-S07
scenario_id: IP-S07
subtype_id: IP-03
anchor_id: IP-S07-A1
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "Only a small amount remains in the workout."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S07-A2-V01
lineage_id: IP-S07
scenario_id: IP-S07
subtype_id: IP-03
anchor_id: IP-S07-A2
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "So, i’m just about finished with the exercises."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S07-A2-V02
lineage_id: IP-S07
scenario_id: IP-S07
subtype_id: IP-03
anchor_id: IP-S07-A2
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "Right now, the workout is close to completion, but not complete yet."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S07-A2-V03
lineage_id: IP-S07
scenario_id: IP-S07
subtype_id: IP-03
anchor_id: IP-S07-A2
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "From where I am, i’m almost done with it."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S07-A2-V04
lineage_id: IP-S07
scenario_id: IP-S07
subtype_id: IP-03
anchor_id: IP-S07-A2
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "Listen, i’ve completed most of the exercise, with only a small part remaining."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S07-A2-V05
lineage_id: IP-S07
scenario_id: IP-S07
subtype_id: IP-03
anchor_id: IP-S07-A2
variant_id: V05
variant_type: LEN
task_domain: Exercise
utterance: "Okay, i’m near the end, but there’s still a little exercise left."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S07-A2-V06
lineage_id: IP-S07
scenario_id: IP-S07
subtype_id: IP-03
anchor_id: IP-S07-A2
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "In this session, only a small amount remains in the workout."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S07-A3-V01
lineage_id: IP-S07
scenario_id: IP-S07
subtype_id: IP-03
anchor_id: IP-S07-A3
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "I mean, i’m just about finished with the exercises."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S07-A3-V02
lineage_id: IP-S07
scenario_id: IP-S07
subtype_id: IP-03
anchor_id: IP-S07-A3
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "Listen, right now, the workout is close to completion, but not complete yet."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S07-A3-V03
lineage_id: IP-S07
scenario_id: IP-S07
subtype_id: IP-03
anchor_id: IP-S07-A3
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "I mean, i’m almost done with it."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S07-A3-V04
lineage_id: IP-S07
scenario_id: IP-S07
subtype_id: IP-03
anchor_id: IP-S07-A3
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "At the moment, i’ve completed most of the exercise, with only a small part remaining."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S07-A3-V05
lineage_id: IP-S07
scenario_id: IP-S07
subtype_id: IP-03
anchor_id: IP-S07-A3
variant_id: V05
variant_type: LEN
task_domain: Exercise
utterance: "Listen, i’m near the end, but there’s still a little exercise left."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S07-A3-V06
lineage_id: IP-S07
scenario_id: IP-S07
subtype_id: IP-03
anchor_id: IP-S07-A3
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "I mean, in this session, only a small amount remains in the workout."
execution_status: In Progress
validation_status: candidate
```

## IP-S08 — IP-03 Near Completion

### Semantic scenario

The user is performing the final remaining part of a multi-step exercise task.

**Task domain:** Exercise

### Stage 1 parent anchors

| Anchor | Utterance |
|---|---|
| A1 | I’ve got one exercise left. |
| A2 | I’m on the last set now. |
| A3 | Just one more part of the routine remains. |

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I have a single exercise remaining. |
| A1 | V02 | SYN | Only one exercise remains for me to complete. |
| A1 | V03 | NAT | I’m down to the last exercise. |
| A1 | V04 | EXP | I’ve completed the earlier exercises, and the final one is still unfinished. |
| A1 | V05 | LEN | Most of the routine is done; one exercise remains. |
| A1 | V06 | DSC | I’m at the final exercise, but it isn’t finished yet. |
| A2 | V01 | LEX | So, i have a single exercise remaining. |
| A2 | V02 | SYN | To be honest, only one exercise remains for me to complete. |
| A2 | V03 | NAT | From where I am, i’m down to the last exercise. |
| A2 | V04 | EXP | To be honest, i’ve completed the earlier exercises, and the final one is still unfinished. |
| A2 | V05 | LEN | So, most of the routine is done; one exercise remains. |
| A2 | V06 | DSC | In this session, i’m at the final exercise, but it isn’t finished yet. |
| A3 | V01 | LEX | Look, i have a single exercise remaining. |
| A3 | V02 | SYN | Right now, only one exercise remains for me to complete. |
| A3 | V03 | NAT | Look, i’m down to the last exercise. |
| A3 | V04 | EXP | At the moment, i’ve completed the earlier exercises, and the final one is still unfinished. |
| A3 | V05 | LEN | As I said, most of the routine is done; one exercise remains. |
| A3 | V06 | DSC | Look, in this session, i’m at the final exercise, but it isn’t finished yet. |

### Production records

```yaml
example_id: IP3A-S08-A1-V01
lineage_id: IP-S08
scenario_id: IP-S08
subtype_id: IP-03
anchor_id: IP-S08-A1
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "I have a single exercise remaining."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S08-A1-V02
lineage_id: IP-S08
scenario_id: IP-S08
subtype_id: IP-03
anchor_id: IP-S08-A1
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "Only one exercise remains for me to complete."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S08-A1-V03
lineage_id: IP-S08
scenario_id: IP-S08
subtype_id: IP-03
anchor_id: IP-S08-A1
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "I’m down to the last exercise."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S08-A1-V04
lineage_id: IP-S08
scenario_id: IP-S08
subtype_id: IP-03
anchor_id: IP-S08-A1
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "I’ve completed the earlier exercises, and the final one is still unfinished."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S08-A1-V05
lineage_id: IP-S08
scenario_id: IP-S08
subtype_id: IP-03
anchor_id: IP-S08-A1
variant_id: V05
variant_type: LEN
task_domain: Exercise
utterance: "Most of the routine is done; one exercise remains."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S08-A1-V06
lineage_id: IP-S08
scenario_id: IP-S08
subtype_id: IP-03
anchor_id: IP-S08-A1
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "I’m at the final exercise, but it isn’t finished yet."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S08-A2-V01
lineage_id: IP-S08
scenario_id: IP-S08
subtype_id: IP-03
anchor_id: IP-S08-A2
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "So, i have a single exercise remaining."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S08-A2-V02
lineage_id: IP-S08
scenario_id: IP-S08
subtype_id: IP-03
anchor_id: IP-S08-A2
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "To be honest, only one exercise remains for me to complete."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S08-A2-V03
lineage_id: IP-S08
scenario_id: IP-S08
subtype_id: IP-03
anchor_id: IP-S08-A2
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "From where I am, i’m down to the last exercise."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S08-A2-V04
lineage_id: IP-S08
scenario_id: IP-S08
subtype_id: IP-03
anchor_id: IP-S08-A2
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "To be honest, i’ve completed the earlier exercises, and the final one is still unfinished."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S08-A2-V05
lineage_id: IP-S08
scenario_id: IP-S08
subtype_id: IP-03
anchor_id: IP-S08-A2
variant_id: V05
variant_type: LEN
task_domain: Exercise
utterance: "So, most of the routine is done; one exercise remains."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S08-A2-V06
lineage_id: IP-S08
scenario_id: IP-S08
subtype_id: IP-03
anchor_id: IP-S08-A2
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "In this session, i’m at the final exercise, but it isn’t finished yet."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S08-A3-V01
lineage_id: IP-S08
scenario_id: IP-S08
subtype_id: IP-03
anchor_id: IP-S08-A3
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "Look, i have a single exercise remaining."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S08-A3-V02
lineage_id: IP-S08
scenario_id: IP-S08
subtype_id: IP-03
anchor_id: IP-S08-A3
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "Right now, only one exercise remains for me to complete."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S08-A3-V03
lineage_id: IP-S08
scenario_id: IP-S08
subtype_id: IP-03
anchor_id: IP-S08-A3
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "Look, i’m down to the last exercise."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S08-A3-V04
lineage_id: IP-S08
scenario_id: IP-S08
subtype_id: IP-03
anchor_id: IP-S08-A3
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "At the moment, i’ve completed the earlier exercises, and the final one is still unfinished."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S08-A3-V05
lineage_id: IP-S08
scenario_id: IP-S08
subtype_id: IP-03
anchor_id: IP-S08-A3
variant_id: V05
variant_type: LEN
task_domain: Exercise
utterance: "As I said, most of the routine is done; one exercise remains."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S08-A3-V06
lineage_id: IP-S08
scenario_id: IP-S08
subtype_id: IP-03
anchor_id: IP-S08-A3
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "Look, in this session, i’m at the final exercise, but it isn’t finished yet."
execution_status: In Progress
validation_status: candidate
```

## IP-S09 — IP-03 Near Completion

### Semantic scenario

The physiotherapy session is nearly finished while additional commentary does not change its unfinished state.

**Task domain:** Physiotherapy

### Stage 1 parent anchors

| Anchor | Utterance |
|---|---|
| A1 | I’m almost finished with the therapy, but it took a while. |
| A2 | I’m nearly through the routine; it’s been tiring. |
| A3 | There’s only a little left, although this session has been long. |

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I’m nearly finished with the therapy session. |
| A1 | V02 | SYN | The physiotherapy routine is close to completion. |
| A1 | V03 | NAT | I’m just about through the physio session. |
| A1 | V04 | EXP | I’ve completed most of the therapy, but a small part is still left. |
| A1 | V05 | LEN | There’s only a little therapy left, although the session has been tiring. |
| A1 | V06 | DSC | The session is nearing its end, with a small amount still underway. |
| A2 | V01 | LEX | So, i’m nearly finished with the therapy session. |
| A2 | V02 | SYN | Right now, the physiotherapy routine is close to completion. |
| A2 | V03 | NAT | From where I am, i’m just about through the physio session. |
| A2 | V04 | EXP | Look, i’ve completed most of the therapy, but a small part is still left. |
| A2 | V05 | LEN | Honestly, there’s only a little therapy left, although the session has been tiring. |
| A2 | V06 | DSC | In this session, the session is nearing its end, with a small amount still underway. |
| A3 | V01 | LEX | Right, i’m nearly finished with the therapy session. |
| A3 | V02 | SYN | I mean, right now, the physiotherapy routine is close to completion. |
| A3 | V03 | NAT | Okay, i’m just about through the physio session. |
| A3 | V04 | EXP | At the moment, i’ve completed most of the therapy, but a small part is still left. |
| A3 | V05 | LEN | So, there’s only a little therapy left, although the session has been tiring. |
| A3 | V06 | DSC | You know, in this session, the session is nearing its end, with a small amount still underway. |

### Production records

```yaml
example_id: IP3A-S09-A1-V01
lineage_id: IP-S09
scenario_id: IP-S09
subtype_id: IP-03
anchor_id: IP-S09-A1
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "I’m nearly finished with the therapy session."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S09-A1-V02
lineage_id: IP-S09
scenario_id: IP-S09
subtype_id: IP-03
anchor_id: IP-S09-A1
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "The physiotherapy routine is close to completion."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S09-A1-V03
lineage_id: IP-S09
scenario_id: IP-S09
subtype_id: IP-03
anchor_id: IP-S09-A1
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "I’m just about through the physio session."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S09-A1-V04
lineage_id: IP-S09
scenario_id: IP-S09
subtype_id: IP-03
anchor_id: IP-S09-A1
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "I’ve completed most of the therapy, but a small part is still left."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S09-A1-V05
lineage_id: IP-S09
scenario_id: IP-S09
subtype_id: IP-03
anchor_id: IP-S09-A1
variant_id: V05
variant_type: LEN
task_domain: Physiotherapy
utterance: "There’s only a little therapy left, although the session has been tiring."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S09-A1-V06
lineage_id: IP-S09
scenario_id: IP-S09
subtype_id: IP-03
anchor_id: IP-S09-A1
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "The session is nearing its end, with a small amount still underway."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S09-A2-V01
lineage_id: IP-S09
scenario_id: IP-S09
subtype_id: IP-03
anchor_id: IP-S09-A2
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "So, i’m nearly finished with the therapy session."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S09-A2-V02
lineage_id: IP-S09
scenario_id: IP-S09
subtype_id: IP-03
anchor_id: IP-S09-A2
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "Right now, the physiotherapy routine is close to completion."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S09-A2-V03
lineage_id: IP-S09
scenario_id: IP-S09
subtype_id: IP-03
anchor_id: IP-S09-A2
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "From where I am, i’m just about through the physio session."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S09-A2-V04
lineage_id: IP-S09
scenario_id: IP-S09
subtype_id: IP-03
anchor_id: IP-S09-A2
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "Look, i’ve completed most of the therapy, but a small part is still left."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S09-A2-V05
lineage_id: IP-S09
scenario_id: IP-S09
subtype_id: IP-03
anchor_id: IP-S09-A2
variant_id: V05
variant_type: LEN
task_domain: Physiotherapy
utterance: "Honestly, there’s only a little therapy left, although the session has been tiring."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S09-A2-V06
lineage_id: IP-S09
scenario_id: IP-S09
subtype_id: IP-03
anchor_id: IP-S09-A2
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "In this session, the session is nearing its end, with a small amount still underway."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S09-A3-V01
lineage_id: IP-S09
scenario_id: IP-S09
subtype_id: IP-03
anchor_id: IP-S09-A3
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "Right, i’m nearly finished with the therapy session."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S09-A3-V02
lineage_id: IP-S09
scenario_id: IP-S09
subtype_id: IP-03
anchor_id: IP-S09-A3
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "I mean, right now, the physiotherapy routine is close to completion."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S09-A3-V03
lineage_id: IP-S09
scenario_id: IP-S09
subtype_id: IP-03
anchor_id: IP-S09-A3
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "Okay, i’m just about through the physio session."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S09-A3-V04
lineage_id: IP-S09
scenario_id: IP-S09
subtype_id: IP-03
anchor_id: IP-S09-A3
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "At the moment, i’ve completed most of the therapy, but a small part is still left."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S09-A3-V05
lineage_id: IP-S09
scenario_id: IP-S09
subtype_id: IP-03
anchor_id: IP-S09-A3
variant_id: V05
variant_type: LEN
task_domain: Physiotherapy
utterance: "So, there’s only a little therapy left, although the session has been tiring."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S09-A3-V06
lineage_id: IP-S09
scenario_id: IP-S09
subtype_id: IP-03
anchor_id: IP-S09-A3
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "You know, in this session, the session is nearing its end, with a small amount still underway."
execution_status: In Progress
validation_status: candidate
```

## IP-S10 — IP-04 Multi-Step Execution

### Semantic scenario

The user has completed some required exercise steps while at least one required step remains.

**Task domain:** Exercise

### Stage 1 parent anchors

| Anchor | Utterance |
|---|---|
| A1 | I’ve finished the first two exercises, but I still have one left. |
| A2 | I’ve done the first couple of sets and still have more to go. |
| A3 | I’m partway through the routine; a few steps remain. |

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I’ve completed the first two exercises, with one more remaining. |
| A1 | V02 | SYN | The first few steps are done, but the routine is still incomplete. |
| A1 | V03 | NAT | I’m through a few exercises and still have more to do. |
| A1 | V04 | EXP | I’ve finished several required steps, while the remaining step is still unfinished. |
| A1 | V05 | LEN | Part of the routine is complete; the later exercise is still left. |
| A1 | V06 | DSC | I’ve moved through the first section, and the rest is still ahead. |
| A2 | V01 | LEX | So, i’ve completed the first two exercises, with one more remaining. |
| A2 | V02 | SYN | Right now, the first few steps are done, but the routine is still incomplete. |
| A2 | V03 | NAT | From where I am, i’m through a few exercises and still have more to do. |
| A2 | V04 | EXP | I mean, i’ve finished several required steps, while the remaining step is still unfinished. |
| A2 | V05 | LEN | Honestly, part of the routine is complete; the later exercise is still left. |
| A2 | V06 | DSC | In this session, i’ve moved through the first section, and the rest is still ahead. |
| A3 | V01 | LEX | Honestly, i’ve completed the first two exercises, with one more remaining. |
| A3 | V02 | SYN | Right, right now, the first few steps are done, but the routine is still incomplete. |
| A3 | V03 | NAT | As I said, i’m through a few exercises and still have more to do. |
| A3 | V04 | EXP | At the moment, i’ve finished several required steps, while the remaining step is still unfinished. |
| A3 | V05 | LEN | So, part of the routine is complete; the later exercise is still left. |
| A3 | V06 | DSC | Well, in this session, i’ve moved through the first section, and the rest is still ahead. |

### Production records

```yaml
example_id: IP3A-S10-A1-V01
lineage_id: IP-S10
scenario_id: IP-S10
subtype_id: IP-04
anchor_id: IP-S10-A1
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "I’ve completed the first two exercises, with one more remaining."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S10-A1-V02
lineage_id: IP-S10
scenario_id: IP-S10
subtype_id: IP-04
anchor_id: IP-S10-A1
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "The first few steps are done, but the routine is still incomplete."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S10-A1-V03
lineage_id: IP-S10
scenario_id: IP-S10
subtype_id: IP-04
anchor_id: IP-S10-A1
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "I’m through a few exercises and still have more to do."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S10-A1-V04
lineage_id: IP-S10
scenario_id: IP-S10
subtype_id: IP-04
anchor_id: IP-S10-A1
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "I’ve finished several required steps, while the remaining step is still unfinished."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S10-A1-V05
lineage_id: IP-S10
scenario_id: IP-S10
subtype_id: IP-04
anchor_id: IP-S10-A1
variant_id: V05
variant_type: LEN
task_domain: Exercise
utterance: "Part of the routine is complete; the later exercise is still left."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S10-A1-V06
lineage_id: IP-S10
scenario_id: IP-S10
subtype_id: IP-04
anchor_id: IP-S10-A1
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "I’ve moved through the first section, and the rest is still ahead."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S10-A2-V01
lineage_id: IP-S10
scenario_id: IP-S10
subtype_id: IP-04
anchor_id: IP-S10-A2
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "So, i’ve completed the first two exercises, with one more remaining."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S10-A2-V02
lineage_id: IP-S10
scenario_id: IP-S10
subtype_id: IP-04
anchor_id: IP-S10-A2
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "Right now, the first few steps are done, but the routine is still incomplete."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S10-A2-V03
lineage_id: IP-S10
scenario_id: IP-S10
subtype_id: IP-04
anchor_id: IP-S10-A2
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "From where I am, i’m through a few exercises and still have more to do."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S10-A2-V04
lineage_id: IP-S10
scenario_id: IP-S10
subtype_id: IP-04
anchor_id: IP-S10-A2
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "I mean, i’ve finished several required steps, while the remaining step is still unfinished."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S10-A2-V05
lineage_id: IP-S10
scenario_id: IP-S10
subtype_id: IP-04
anchor_id: IP-S10-A2
variant_id: V05
variant_type: LEN
task_domain: Exercise
utterance: "Honestly, part of the routine is complete; the later exercise is still left."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S10-A2-V06
lineage_id: IP-S10
scenario_id: IP-S10
subtype_id: IP-04
anchor_id: IP-S10-A2
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "In this session, i’ve moved through the first section, and the rest is still ahead."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S10-A3-V01
lineage_id: IP-S10
scenario_id: IP-S10
subtype_id: IP-04
anchor_id: IP-S10-A3
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "Honestly, i’ve completed the first two exercises, with one more remaining."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S10-A3-V02
lineage_id: IP-S10
scenario_id: IP-S10
subtype_id: IP-04
anchor_id: IP-S10-A3
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "Right, right now, the first few steps are done, but the routine is still incomplete."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S10-A3-V03
lineage_id: IP-S10
scenario_id: IP-S10
subtype_id: IP-04
anchor_id: IP-S10-A3
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "As I said, i’m through a few exercises and still have more to do."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S10-A3-V04
lineage_id: IP-S10
scenario_id: IP-S10
subtype_id: IP-04
anchor_id: IP-S10-A3
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "At the moment, i’ve finished several required steps, while the remaining step is still unfinished."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S10-A3-V05
lineage_id: IP-S10
scenario_id: IP-S10
subtype_id: IP-04
anchor_id: IP-S10-A3
variant_id: V05
variant_type: LEN
task_domain: Exercise
utterance: "So, part of the routine is complete; the later exercise is still left."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S10-A3-V06
lineage_id: IP-S10
scenario_id: IP-S10
subtype_id: IP-04
anchor_id: IP-S10-A3
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "Well, in this session, i’ve moved through the first section, and the rest is still ahead."
execution_status: In Progress
validation_status: candidate
```

## IP-S11 — IP-04 Multi-Step Execution

### Semantic scenario

The user is progressing through a multi-step physiotherapy sequence that has not yet reached its end.

**Task domain:** Physiotherapy

### Stage 1 parent anchors

| Anchor | Utterance |
|---|---|
| A1 | I’m on the third step of the physiotherapy routine. |
| A2 | I’m working through the routine one step at a time. |
| A3 | I’m in the middle of the therapy sequence. |

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I’m working through the third stage of the physiotherapy routine. |
| A1 | V02 | SYN | The physiotherapy sequence is underway, and I’m partway through it. |
| A1 | V03 | NAT | I’m in the middle of the physio routine. |
| A1 | V04 | EXP | I’ve completed some earlier steps and am now carrying out the next one. |
| A1 | V05 | LEN | I’m partway through the sequence, with later steps still remaining. |
| A1 | V06 | DSC | I’ve moved beyond the opening steps and am continuing through the routine. |
| A2 | V01 | LEX | So, i’m working through the third stage of the physiotherapy routine. |
| A2 | V02 | SYN | Right now, the physiotherapy sequence is underway, and I’m partway through it. |
| A2 | V03 | NAT | From where I am, i’m in the middle of the physio routine. |
| A2 | V04 | EXP | I must say, i’ve completed some earlier steps and am now carrying out the next one. |
| A2 | V05 | LEN | You know, i’m partway through the sequence, with later steps still remaining. |
| A2 | V06 | DSC | In this session, i’ve moved beyond the opening steps and am continuing through the routine. |
| A3 | V01 | LEX | Basically, i’m working through the third stage of the physiotherapy routine. |
| A3 | V02 | SYN | Honestly, right now, the physiotherapy sequence is underway, and I’m partway through it. |
| A3 | V03 | NAT | So, i’m in the middle of the physio routine. |
| A3 | V04 | EXP | At the moment, i’ve completed some earlier steps and am now carrying out the next one. |
| A3 | V05 | LEN | I mean, i’m partway through the sequence, with later steps still remaining. |
| A3 | V06 | DSC | I mean, in this session, i’ve moved beyond the opening steps and am continuing through the routine. |

### Production records

```yaml
example_id: IP3A-S11-A1-V01
lineage_id: IP-S11
scenario_id: IP-S11
subtype_id: IP-04
anchor_id: IP-S11-A1
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "I’m working through the third stage of the physiotherapy routine."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S11-A1-V02
lineage_id: IP-S11
scenario_id: IP-S11
subtype_id: IP-04
anchor_id: IP-S11-A1
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "The physiotherapy sequence is underway, and I’m partway through it."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S11-A1-V03
lineage_id: IP-S11
scenario_id: IP-S11
subtype_id: IP-04
anchor_id: IP-S11-A1
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "I’m in the middle of the physio routine."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S11-A1-V04
lineage_id: IP-S11
scenario_id: IP-S11
subtype_id: IP-04
anchor_id: IP-S11-A1
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "I’ve completed some earlier steps and am now carrying out the next one."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S11-A1-V05
lineage_id: IP-S11
scenario_id: IP-S11
subtype_id: IP-04
anchor_id: IP-S11-A1
variant_id: V05
variant_type: LEN
task_domain: Physiotherapy
utterance: "I’m partway through the sequence, with later steps still remaining."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S11-A1-V06
lineage_id: IP-S11
scenario_id: IP-S11
subtype_id: IP-04
anchor_id: IP-S11-A1
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "I’ve moved beyond the opening steps and am continuing through the routine."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S11-A2-V01
lineage_id: IP-S11
scenario_id: IP-S11
subtype_id: IP-04
anchor_id: IP-S11-A2
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "So, i’m working through the third stage of the physiotherapy routine."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S11-A2-V02
lineage_id: IP-S11
scenario_id: IP-S11
subtype_id: IP-04
anchor_id: IP-S11-A2
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "Right now, the physiotherapy sequence is underway, and I’m partway through it."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S11-A2-V03
lineage_id: IP-S11
scenario_id: IP-S11
subtype_id: IP-04
anchor_id: IP-S11-A2
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "From where I am, i’m in the middle of the physio routine."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S11-A2-V04
lineage_id: IP-S11
scenario_id: IP-S11
subtype_id: IP-04
anchor_id: IP-S11-A2
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "I must say, i’ve completed some earlier steps and am now carrying out the next one."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S11-A2-V05
lineage_id: IP-S11
scenario_id: IP-S11
subtype_id: IP-04
anchor_id: IP-S11-A2
variant_id: V05
variant_type: LEN
task_domain: Physiotherapy
utterance: "You know, i’m partway through the sequence, with later steps still remaining."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S11-A2-V06
lineage_id: IP-S11
scenario_id: IP-S11
subtype_id: IP-04
anchor_id: IP-S11-A2
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "In this session, i’ve moved beyond the opening steps and am continuing through the routine."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S11-A3-V01
lineage_id: IP-S11
scenario_id: IP-S11
subtype_id: IP-04
anchor_id: IP-S11-A3
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "Basically, i’m working through the third stage of the physiotherapy routine."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S11-A3-V02
lineage_id: IP-S11
scenario_id: IP-S11
subtype_id: IP-04
anchor_id: IP-S11-A3
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "Honestly, right now, the physiotherapy sequence is underway, and I’m partway through it."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S11-A3-V03
lineage_id: IP-S11
scenario_id: IP-S11
subtype_id: IP-04
anchor_id: IP-S11-A3
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "So, i’m in the middle of the physio routine."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S11-A3-V04
lineage_id: IP-S11
scenario_id: IP-S11
subtype_id: IP-04
anchor_id: IP-S11-A3
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "At the moment, i’ve completed some earlier steps and am now carrying out the next one."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S11-A3-V05
lineage_id: IP-S11
scenario_id: IP-S11
subtype_id: IP-04
anchor_id: IP-S11-A3
variant_id: V05
variant_type: LEN
task_domain: Physiotherapy
utterance: "I mean, i’m partway through the sequence, with later steps still remaining."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S11-A3-V06
lineage_id: IP-S11
scenario_id: IP-S11
subtype_id: IP-04
anchor_id: IP-S11-A3
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "I mean, in this session, i’ve moved beyond the opening steps and am continuing through the routine."
execution_status: In Progress
validation_status: candidate
```

## IP-S12 — IP-04 Multi-Step Execution

### Semantic scenario

The user identifies several completed exercise steps while explicitly retaining unfinished steps.

**Task domain:** Exercise

### Stage 1 parent anchors

| Anchor | Utterance |
|---|---|
| A1 | I’ve done three sets, and two more are left. |
| A2 | I’ve got most of the routine done, but there’s still more to finish. |
| A3 | I’m through the first few parts; the rest is still pending. |

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I’ve completed three sets, with two still remaining. |
| A1 | V02 | SYN | Three sets are done, while two more are still required. |
| A1 | V03 | NAT | I’m most of the way through, but I’ve still got a couple of sets left. |
| A1 | V04 | EXP | I’ve finished the first three sets, and the final two have not yet been done. |
| A1 | V05 | LEN | Three sets are complete; two are still to go. |
| A1 | V06 | DSC | I’m well into the workout, with two sets still ahead. |
| A2 | V01 | LEX | So, i’ve completed three sets, with two still remaining. |
| A2 | V02 | SYN | I must say, three sets are done, while two more are still required. |
| A2 | V03 | NAT | From where I am, i’m most of the way through, but I’ve still got a couple of sets left. |
| A2 | V04 | EXP | Listen, i’ve finished the first three sets, and the final two have not yet been done. |
| A2 | V05 | LEN | Actually, three sets are complete; two are still to go. |
| A2 | V06 | DSC | In this session, i’m well into the workout, with two sets still ahead. |
| A3 | V01 | LEX | Honestly, i’ve completed three sets, with two still remaining. |
| A3 | V02 | SYN | Right now, three sets are done, while two more are still required. |
| A3 | V03 | NAT | So, i’m most of the way through, but I’ve still got a couple of sets left. |
| A3 | V04 | EXP | At the moment, i’ve finished the first three sets, and the final two have not yet been done. |
| A3 | V05 | LEN | To be honest, three sets are complete; two are still to go. |
| A3 | V06 | DSC | As I said, in this session, i’m well into the workout, with two sets still ahead. |

### Production records

```yaml
example_id: IP3A-S12-A1-V01
lineage_id: IP-S12
scenario_id: IP-S12
subtype_id: IP-04
anchor_id: IP-S12-A1
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "I’ve completed three sets, with two still remaining."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S12-A1-V02
lineage_id: IP-S12
scenario_id: IP-S12
subtype_id: IP-04
anchor_id: IP-S12-A1
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "Three sets are done, while two more are still required."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S12-A1-V03
lineage_id: IP-S12
scenario_id: IP-S12
subtype_id: IP-04
anchor_id: IP-S12-A1
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "I’m most of the way through, but I’ve still got a couple of sets left."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S12-A1-V04
lineage_id: IP-S12
scenario_id: IP-S12
subtype_id: IP-04
anchor_id: IP-S12-A1
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "I’ve finished the first three sets, and the final two have not yet been done."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S12-A1-V05
lineage_id: IP-S12
scenario_id: IP-S12
subtype_id: IP-04
anchor_id: IP-S12-A1
variant_id: V05
variant_type: LEN
task_domain: Exercise
utterance: "Three sets are complete; two are still to go."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S12-A1-V06
lineage_id: IP-S12
scenario_id: IP-S12
subtype_id: IP-04
anchor_id: IP-S12-A1
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "I’m well into the workout, with two sets still ahead."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S12-A2-V01
lineage_id: IP-S12
scenario_id: IP-S12
subtype_id: IP-04
anchor_id: IP-S12-A2
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "So, i’ve completed three sets, with two still remaining."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S12-A2-V02
lineage_id: IP-S12
scenario_id: IP-S12
subtype_id: IP-04
anchor_id: IP-S12-A2
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "I must say, three sets are done, while two more are still required."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S12-A2-V03
lineage_id: IP-S12
scenario_id: IP-S12
subtype_id: IP-04
anchor_id: IP-S12-A2
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "From where I am, i’m most of the way through, but I’ve still got a couple of sets left."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S12-A2-V04
lineage_id: IP-S12
scenario_id: IP-S12
subtype_id: IP-04
anchor_id: IP-S12-A2
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "Listen, i’ve finished the first three sets, and the final two have not yet been done."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S12-A2-V05
lineage_id: IP-S12
scenario_id: IP-S12
subtype_id: IP-04
anchor_id: IP-S12-A2
variant_id: V05
variant_type: LEN
task_domain: Exercise
utterance: "Actually, three sets are complete; two are still to go."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S12-A2-V06
lineage_id: IP-S12
scenario_id: IP-S12
subtype_id: IP-04
anchor_id: IP-S12-A2
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "In this session, i’m well into the workout, with two sets still ahead."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S12-A3-V01
lineage_id: IP-S12
scenario_id: IP-S12
subtype_id: IP-04
anchor_id: IP-S12-A3
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "Honestly, i’ve completed three sets, with two still remaining."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S12-A3-V02
lineage_id: IP-S12
scenario_id: IP-S12
subtype_id: IP-04
anchor_id: IP-S12-A3
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "Right now, three sets are done, while two more are still required."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S12-A3-V03
lineage_id: IP-S12
scenario_id: IP-S12
subtype_id: IP-04
anchor_id: IP-S12-A3
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "So, i’m most of the way through, but I’ve still got a couple of sets left."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S12-A3-V04
lineage_id: IP-S12
scenario_id: IP-S12
subtype_id: IP-04
anchor_id: IP-S12-A3
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "At the moment, i’ve finished the first three sets, and the final two have not yet been done."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S12-A3-V05
lineage_id: IP-S12
scenario_id: IP-S12
subtype_id: IP-04
anchor_id: IP-S12-A3
variant_id: V05
variant_type: LEN
task_domain: Exercise
utterance: "To be honest, three sets are complete; two are still to go."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S12-A3-V06
lineage_id: IP-S12
scenario_id: IP-S12
subtype_id: IP-04
anchor_id: IP-S12-A3
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "As I said, in this session, i’m well into the workout, with two sets still ahead."
execution_status: In Progress
validation_status: candidate
```

## IP-S13 — IP-05 Temporarily Interrupted Execution

### Semantic scenario

The user began exercising and then paused before the task was complete.

**Task domain:** Exercise

### Stage 1 parent anchors

| Anchor | Utterance |
|---|---|
| A1 | I started the exercise, but I had to pause. |
| A2 | I was doing the exercise and stopped for a moment. |
| A3 | I’m taking a short break in the middle of it. |

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I began the exercise and then took a temporary pause. |
| A1 | V02 | SYN | The exercise was underway before I stopped briefly. |
| A1 | V03 | NAT | I was doing it and took a quick break. |
| A1 | V04 | EXP | I had already started the exercise when I paused, so the task remains unfinished. |
| A1 | V05 | LEN | I started the workout but paused before completing it. |
| A1 | V06 | DSC | The routine is still underway despite the short break. |
| A2 | V01 | LEX | So, i began the exercise and then took a temporary pause. |
| A2 | V02 | SYN | Right now, the exercise was underway before I stopped briefly. |
| A2 | V03 | NAT | From where I am, i was doing it and took a quick break. |
| A2 | V04 | EXP | Honestly, i had already started the exercise when I paused, so the task remains unfinished. |
| A2 | V05 | LEN | Look, i started the workout but paused before completing it. |
| A2 | V06 | DSC | In this session, the routine is still underway despite the short break. |
| A3 | V01 | LEX | Listen, i began the exercise and then took a temporary pause. |
| A3 | V02 | SYN | To be honest, right now, the exercise was underway before I stopped briefly. |
| A3 | V03 | NAT | Right, i was doing it and took a quick break. |
| A3 | V04 | EXP | At the moment, i had already started the exercise when I paused, so the task remains unfinished. |
| A3 | V05 | LEN | Right, i started the workout but paused before completing it. |
| A3 | V06 | DSC | To be honest, in this session, the routine is still underway despite the short break. |

### Production records

```yaml
example_id: IP3A-S13-A1-V01
lineage_id: IP-S13
scenario_id: IP-S13
subtype_id: IP-05
anchor_id: IP-S13-A1
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "I began the exercise and then took a temporary pause."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S13-A1-V02
lineage_id: IP-S13
scenario_id: IP-S13
subtype_id: IP-05
anchor_id: IP-S13-A1
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "The exercise was underway before I stopped briefly."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S13-A1-V03
lineage_id: IP-S13
scenario_id: IP-S13
subtype_id: IP-05
anchor_id: IP-S13-A1
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "I was doing it and took a quick break."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S13-A1-V04
lineage_id: IP-S13
scenario_id: IP-S13
subtype_id: IP-05
anchor_id: IP-S13-A1
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "I had already started the exercise when I paused, so the task remains unfinished."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S13-A1-V05
lineage_id: IP-S13
scenario_id: IP-S13
subtype_id: IP-05
anchor_id: IP-S13-A1
variant_id: V05
variant_type: LEN
task_domain: Exercise
utterance: "I started the workout but paused before completing it."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S13-A1-V06
lineage_id: IP-S13
scenario_id: IP-S13
subtype_id: IP-05
anchor_id: IP-S13-A1
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "The routine is still underway despite the short break."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S13-A2-V01
lineage_id: IP-S13
scenario_id: IP-S13
subtype_id: IP-05
anchor_id: IP-S13-A2
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "So, i began the exercise and then took a temporary pause."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S13-A2-V02
lineage_id: IP-S13
scenario_id: IP-S13
subtype_id: IP-05
anchor_id: IP-S13-A2
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "Right now, the exercise was underway before I stopped briefly."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S13-A2-V03
lineage_id: IP-S13
scenario_id: IP-S13
subtype_id: IP-05
anchor_id: IP-S13-A2
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "From where I am, i was doing it and took a quick break."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S13-A2-V04
lineage_id: IP-S13
scenario_id: IP-S13
subtype_id: IP-05
anchor_id: IP-S13-A2
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "Honestly, i had already started the exercise when I paused, so the task remains unfinished."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S13-A2-V05
lineage_id: IP-S13
scenario_id: IP-S13
subtype_id: IP-05
anchor_id: IP-S13-A2
variant_id: V05
variant_type: LEN
task_domain: Exercise
utterance: "Look, i started the workout but paused before completing it."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S13-A2-V06
lineage_id: IP-S13
scenario_id: IP-S13
subtype_id: IP-05
anchor_id: IP-S13-A2
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "In this session, the routine is still underway despite the short break."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S13-A3-V01
lineage_id: IP-S13
scenario_id: IP-S13
subtype_id: IP-05
anchor_id: IP-S13-A3
variant_id: V01
variant_type: LEX
task_domain: Exercise
utterance: "Listen, i began the exercise and then took a temporary pause."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S13-A3-V02
lineage_id: IP-S13
scenario_id: IP-S13
subtype_id: IP-05
anchor_id: IP-S13-A3
variant_id: V02
variant_type: SYN
task_domain: Exercise
utterance: "To be honest, right now, the exercise was underway before I stopped briefly."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S13-A3-V03
lineage_id: IP-S13
scenario_id: IP-S13
subtype_id: IP-05
anchor_id: IP-S13-A3
variant_id: V03
variant_type: NAT
task_domain: Exercise
utterance: "Right, i was doing it and took a quick break."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S13-A3-V04
lineage_id: IP-S13
scenario_id: IP-S13
subtype_id: IP-05
anchor_id: IP-S13-A3
variant_id: V04
variant_type: EXP
task_domain: Exercise
utterance: "At the moment, i had already started the exercise when I paused, so the task remains unfinished."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S13-A3-V05
lineage_id: IP-S13
scenario_id: IP-S13
subtype_id: IP-05
anchor_id: IP-S13-A3
variant_id: V05
variant_type: LEN
task_domain: Exercise
utterance: "Right, i started the workout but paused before completing it."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S13-A3-V06
lineage_id: IP-S13
scenario_id: IP-S13
subtype_id: IP-05
anchor_id: IP-S13-A3
variant_id: V06
variant_type: DSC
task_domain: Exercise
utterance: "To be honest, in this session, the routine is still underway despite the short break."
execution_status: In Progress
validation_status: candidate
```

## IP-S14 — IP-05 Temporarily Interrupted Execution

### Semantic scenario

The user began physiotherapy, was interrupted, and still has unfinished work.

**Task domain:** Physiotherapy

### Stage 1 parent anchors

| Anchor | Utterance |
|---|---|
| A1 | I started the therapy, but I got interrupted before finishing. |
| A2 | I was doing the routine when something came up, and I still have some left. |
| A3 | I had to stop halfway through, so I’m not finished yet. |

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I began the physiotherapy, but an interruption stopped me before the end. |
| A1 | V02 | SYN | The therapy was underway when I had to stop, and some work remains. |
| A1 | V03 | NAT | I was in the middle of physio when I got interrupted. |
| A1 | V04 | EXP | I had already completed part of the session before the interruption, but the rest is unfinished. |
| A1 | V05 | LEN | I started the session and had to pause; there is still therapy left. |
| A1 | V06 | DSC | The session was underway when I stepped away, so it remains incomplete. |
| A2 | V01 | LEX | So, i began the physiotherapy, but an interruption stopped me before the end. |
| A2 | V02 | SYN | Right now, the therapy was underway when I had to stop, and some work remains. |
| A2 | V03 | NAT | From where I am, i was in the middle of physio when I got interrupted. |
| A2 | V04 | EXP | As I said, i had already completed part of the session before the interruption, but the rest is unfinished. |
| A2 | V05 | LEN | Listen, i started the session and had to pause; there is still therapy left. |
| A2 | V06 | DSC | In this session, the session was underway when I stepped away, so it remains incomplete. |
| A3 | V01 | LEX | Basically, i began the physiotherapy, but an interruption stopped me before the end. |
| A3 | V02 | SYN | Look, right now, the therapy was underway when I had to stop, and some work remains. |
| A3 | V03 | NAT | Listen, i was in the middle of physio when I got interrupted. |
| A3 | V04 | EXP | At the moment, i had already completed part of the session before the interruption, but the rest is unfinished. |
| A3 | V05 | LEN | Actually, i started the session and had to pause; there is still therapy left. |
| A3 | V06 | DSC | Well, in this session, the session was underway when I stepped away, so it remains incomplete. |

### Production records

```yaml
example_id: IP3A-S14-A1-V01
lineage_id: IP-S14
scenario_id: IP-S14
subtype_id: IP-05
anchor_id: IP-S14-A1
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "I began the physiotherapy, but an interruption stopped me before the end."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S14-A1-V02
lineage_id: IP-S14
scenario_id: IP-S14
subtype_id: IP-05
anchor_id: IP-S14-A1
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "The therapy was underway when I had to stop, and some work remains."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S14-A1-V03
lineage_id: IP-S14
scenario_id: IP-S14
subtype_id: IP-05
anchor_id: IP-S14-A1
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "I was in the middle of physio when I got interrupted."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S14-A1-V04
lineage_id: IP-S14
scenario_id: IP-S14
subtype_id: IP-05
anchor_id: IP-S14-A1
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "I had already completed part of the session before the interruption, but the rest is unfinished."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S14-A1-V05
lineage_id: IP-S14
scenario_id: IP-S14
subtype_id: IP-05
anchor_id: IP-S14-A1
variant_id: V05
variant_type: LEN
task_domain: Physiotherapy
utterance: "I started the session and had to pause; there is still therapy left."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S14-A1-V06
lineage_id: IP-S14
scenario_id: IP-S14
subtype_id: IP-05
anchor_id: IP-S14-A1
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "The session was underway when I stepped away, so it remains incomplete."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S14-A2-V01
lineage_id: IP-S14
scenario_id: IP-S14
subtype_id: IP-05
anchor_id: IP-S14-A2
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "So, i began the physiotherapy, but an interruption stopped me before the end."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S14-A2-V02
lineage_id: IP-S14
scenario_id: IP-S14
subtype_id: IP-05
anchor_id: IP-S14-A2
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "Right now, the therapy was underway when I had to stop, and some work remains."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S14-A2-V03
lineage_id: IP-S14
scenario_id: IP-S14
subtype_id: IP-05
anchor_id: IP-S14-A2
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "From where I am, i was in the middle of physio when I got interrupted."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S14-A2-V04
lineage_id: IP-S14
scenario_id: IP-S14
subtype_id: IP-05
anchor_id: IP-S14-A2
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "As I said, i had already completed part of the session before the interruption, but the rest is unfinished."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S14-A2-V05
lineage_id: IP-S14
scenario_id: IP-S14
subtype_id: IP-05
anchor_id: IP-S14-A2
variant_id: V05
variant_type: LEN
task_domain: Physiotherapy
utterance: "Listen, i started the session and had to pause; there is still therapy left."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S14-A2-V06
lineage_id: IP-S14
scenario_id: IP-S14
subtype_id: IP-05
anchor_id: IP-S14-A2
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "In this session, the session was underway when I stepped away, so it remains incomplete."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S14-A3-V01
lineage_id: IP-S14
scenario_id: IP-S14
subtype_id: IP-05
anchor_id: IP-S14-A3
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "Basically, i began the physiotherapy, but an interruption stopped me before the end."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S14-A3-V02
lineage_id: IP-S14
scenario_id: IP-S14
subtype_id: IP-05
anchor_id: IP-S14-A3
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "Look, right now, the therapy was underway when I had to stop, and some work remains."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S14-A3-V03
lineage_id: IP-S14
scenario_id: IP-S14
subtype_id: IP-05
anchor_id: IP-S14-A3
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "Listen, i was in the middle of physio when I got interrupted."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S14-A3-V04
lineage_id: IP-S14
scenario_id: IP-S14
subtype_id: IP-05
anchor_id: IP-S14-A3
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "At the moment, i had already completed part of the session before the interruption, but the rest is unfinished."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S14-A3-V05
lineage_id: IP-S14
scenario_id: IP-S14
subtype_id: IP-05
anchor_id: IP-S14-A3
variant_id: V05
variant_type: LEN
task_domain: Physiotherapy
utterance: "Actually, i started the session and had to pause; there is still therapy left."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S14-A3-V06
lineage_id: IP-S14
scenario_id: IP-S14
subtype_id: IP-05
anchor_id: IP-S14-A3
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "Well, in this session, the session was underway when I stepped away, so it remains incomplete."
execution_status: In Progress
validation_status: candidate
```

## IP-S15 — IP-05 Temporarily Interrupted Execution

### Semantic scenario

The user has started physiotherapy, temporarily stopped, and retains unfinished execution that can be resumed.

**Task domain:** Physiotherapy

### Stage 1 parent anchors

| Anchor | Utterance |
|---|---|
| A1 | I started the routine and paused; I still need to finish it. |
| A2 | I’ve begun it, but I’ll continue after this break. |
| A3 | I’m halfway through and will pick it up again shortly. |

### Linguistic variants

| Anchor | Variant | Type | Utterance |
|---|---|---|---|
| A1 | V01 | LEX | I began the routine and then paused, with some work still remaining. |
| A1 | V02 | SYN | The therapy session has started, but I stopped temporarily before finishing. |
| A1 | V03 | NAT | I’m partway through and will get back to it after the break. |
| A1 | V04 | EXP | I’ve already started the routine; the pause is temporary and the remaining work is unfinished. |
| A1 | V05 | LEN | I’ve started the session but paused before completing it. |
| A1 | V06 | DSC | I’ve made a start and will continue from where I left off. |
| A2 | V01 | LEX | So, i began the routine and then paused, with some work still remaining. |
| A2 | V02 | SYN | Right now, the therapy session has started, but I stopped temporarily before finishing. |
| A2 | V03 | NAT | From where I am, i’m partway through and will get back to it after the break. |
| A2 | V04 | EXP | I must say, i’ve already started the routine; the pause is temporary and the remaining work is unfinished. |
| A2 | V05 | LEN | As I said, i’ve started the session but paused before completing it. |
| A2 | V06 | DSC | In this session, i’ve made a start and will continue from where I left off. |
| A3 | V01 | LEX | Okay, i began the routine and then paused, with some work still remaining. |
| A3 | V02 | SYN | So, right now, the therapy session has started, but I stopped temporarily before finishing. |
| A3 | V03 | NAT | Actually, i’m partway through and will get back to it after the break. |
| A3 | V04 | EXP | At the moment, i’ve already started the routine; the pause is temporary and the remaining work is unfinished. |
| A3 | V05 | LEN | Listen, i’ve started the session but paused before completing it. |
| A3 | V06 | DSC | To be honest, in this session, i’ve made a start and will continue from where I left off. |

### Production records

```yaml
example_id: IP3A-S15-A1-V01
lineage_id: IP-S15
scenario_id: IP-S15
subtype_id: IP-05
anchor_id: IP-S15-A1
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "I began the routine and then paused, with some work still remaining."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S15-A1-V02
lineage_id: IP-S15
scenario_id: IP-S15
subtype_id: IP-05
anchor_id: IP-S15-A1
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "The therapy session has started, but I stopped temporarily before finishing."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S15-A1-V03
lineage_id: IP-S15
scenario_id: IP-S15
subtype_id: IP-05
anchor_id: IP-S15-A1
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "I’m partway through and will get back to it after the break."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S15-A1-V04
lineage_id: IP-S15
scenario_id: IP-S15
subtype_id: IP-05
anchor_id: IP-S15-A1
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "I’ve already started the routine; the pause is temporary and the remaining work is unfinished."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S15-A1-V05
lineage_id: IP-S15
scenario_id: IP-S15
subtype_id: IP-05
anchor_id: IP-S15-A1
variant_id: V05
variant_type: LEN
task_domain: Physiotherapy
utterance: "I’ve started the session but paused before completing it."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S15-A1-V06
lineage_id: IP-S15
scenario_id: IP-S15
subtype_id: IP-05
anchor_id: IP-S15-A1
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "I’ve made a start and will continue from where I left off."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S15-A2-V01
lineage_id: IP-S15
scenario_id: IP-S15
subtype_id: IP-05
anchor_id: IP-S15-A2
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "So, i began the routine and then paused, with some work still remaining."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S15-A2-V02
lineage_id: IP-S15
scenario_id: IP-S15
subtype_id: IP-05
anchor_id: IP-S15-A2
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "Right now, the therapy session has started, but I stopped temporarily before finishing."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S15-A2-V03
lineage_id: IP-S15
scenario_id: IP-S15
subtype_id: IP-05
anchor_id: IP-S15-A2
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "From where I am, i’m partway through and will get back to it after the break."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S15-A2-V04
lineage_id: IP-S15
scenario_id: IP-S15
subtype_id: IP-05
anchor_id: IP-S15-A2
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "I must say, i’ve already started the routine; the pause is temporary and the remaining work is unfinished."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S15-A2-V05
lineage_id: IP-S15
scenario_id: IP-S15
subtype_id: IP-05
anchor_id: IP-S15-A2
variant_id: V05
variant_type: LEN
task_domain: Physiotherapy
utterance: "As I said, i’ve started the session but paused before completing it."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S15-A2-V06
lineage_id: IP-S15
scenario_id: IP-S15
subtype_id: IP-05
anchor_id: IP-S15-A2
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "In this session, i’ve made a start and will continue from where I left off."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S15-A3-V01
lineage_id: IP-S15
scenario_id: IP-S15
subtype_id: IP-05
anchor_id: IP-S15-A3
variant_id: V01
variant_type: LEX
task_domain: Physiotherapy
utterance: "Okay, i began the routine and then paused, with some work still remaining."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S15-A3-V02
lineage_id: IP-S15
scenario_id: IP-S15
subtype_id: IP-05
anchor_id: IP-S15-A3
variant_id: V02
variant_type: SYN
task_domain: Physiotherapy
utterance: "So, right now, the therapy session has started, but I stopped temporarily before finishing."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S15-A3-V03
lineage_id: IP-S15
scenario_id: IP-S15
subtype_id: IP-05
anchor_id: IP-S15-A3
variant_id: V03
variant_type: NAT
task_domain: Physiotherapy
utterance: "Actually, i’m partway through and will get back to it after the break."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S15-A3-V04
lineage_id: IP-S15
scenario_id: IP-S15
subtype_id: IP-05
anchor_id: IP-S15-A3
variant_id: V04
variant_type: EXP
task_domain: Physiotherapy
utterance: "At the moment, i’ve already started the routine; the pause is temporary and the remaining work is unfinished."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S15-A3-V05
lineage_id: IP-S15
scenario_id: IP-S15
subtype_id: IP-05
anchor_id: IP-S15-A3
variant_id: V05
variant_type: LEN
task_domain: Physiotherapy
utterance: "Listen, i’ve started the session but paused before completing it."
execution_status: In Progress
validation_status: candidate
```

```yaml
example_id: IP3A-S15-A3-V06
lineage_id: IP-S15
scenario_id: IP-S15
subtype_id: IP-05
anchor_id: IP-S15-A3
variant_id: V06
variant_type: DSC
task_domain: Physiotherapy
utterance: "To be honest, in this session, i’ve made a start and will continue from where I left off."
execution_status: In Progress
validation_status: candidate
```

## 6. Acceptance Criteria

A candidate is eligible for acceptance only when:
- the semantic scenario is unchanged;
- execution has clearly begun;
- completion has not occurred;
- the wording is natural and grammatically sound;
- the intended variant type is genuinely represented;
- no single lexical cue is sufficient to determine the label;
- the utterance is not a disguised future intention;
- temporary interruption, partial completion, and near completion remain correctly represented;
- the utterance does not introduce another ontology or task-manager state;
- lineage and metadata are valid.

## 7. Validation Responsibilities

Human review verifies semantic fidelity, naturalness, boundary safety, and scenario preservation. Automated validation verifies identifiers, required fields, state consistency, duplicate similarity, and lineage integrity.

Candidates that fail validation are removed or rewritten before acceptance into the dataset.

## 8. Resource Accounting

```text
15 Stage 1 scenarios
× 3 Stage 1 anchors per scenario
× 6 standard Stage 3A variants per anchor
= 270 candidate variants
```

The candidate count is a construction resource count. It does not imply that every candidate will survive semantic, linguistic, duplication, and boundary validation.

## 9. Final Semantic Constraint

> Stage 3A changes the linguistic realization of an existing `In Progress` scenario; it does not change the execution state represented by that scenario.