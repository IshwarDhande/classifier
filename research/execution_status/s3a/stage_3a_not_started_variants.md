# Execution Status Dataset — Stage 3A Linguistic Expansion: Not Started

## 1. Construction Status

This is the **candidate-generation resource** for Stage 3A `Not Started`.

```yaml
execution_status: Not Started
source_stage: Stage 1
parent_scenarios: 15
parent_anchors: 45
standard_variant_types: 6
candidate_variants: 270
validation_status: candidate
```

The six state-specific standard variation types are `LEX`, `NAT`, `EXP`, `PRG`, `CMK`, and `QST`, as specified for Not Started. The Stage 3A specification requires semantic identity to remain unchanged across variants. fileciteturn156file2L298-L304

## 2. Semantic Invariants

Every candidate must preserve:

- Not Started execution status.
- The same semantic subtype.
- The same semantic scenario.
- The same target task.
- The same execution condition.
- No implication that execution has begun.
- No implication that execution has completed.

Stage 3A is a linguistic expansion layer; it must not introduce new semantic scenarios. fileciteturn156file3L33-L58

## 3. Candidate Resource Schema

| Field | Meaning |
|---|---|
| `example_id` | Unique candidate identifier |
| `scenario_id` | Frozen Stage 1 scenario |
| `parent_id` | Parent anchor |
| `lineage_id` | Leakage-control lineage |
| `execution_status` | Frozen label |
| `semantic_subtype` | Frozen construction subtype |
| `variation_type` | Primary Stage 3A variation |
| `utterance` | Candidate user utterance |
| `target_task` | Parent task domain |
| `validation_status` | Candidate pending semantic QC |

## 4. Generation Coverage

| State | Scenarios | Anchors | Variants / Anchor | Candidates |
|---|---:|---:|---:|---:|
| Not Started | 15 | 45 | 6 | 270 |

This is an **initial generation batch**, not a claim that 270 variants must survive validation. The construction plan explicitly treats Stage 3A variation types as coverage dimensions rather than a blind final quota. fileciteturn156file3L460-L478

## 5. Candidate Variants

### NS-S01 — Task Not Yet Started

- **Subtype:** `NS-01 Direct Non-Execution`
- **Domain:** Exercise

#### Parent Anchor A

> I haven’t started the exercise yet.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S01-A-V01` | `LEX` | I still haven't started the exercise yet. | `candidate` |
| `NS-S01-A-V03` | `NAT` | Honestly, i haven’t started the exercise yet. | `candidate` |
| `NS-S01-A-V04` | `EXP` | I haven’t started the exercise yet. | `candidate` |
| `NS-S01-A-V07` | `PRG` | As of now, i haven’t started the exercise yet. | `candidate` |
| `NS-S01-A-V08` | `CMK` | Okay, i haven’t started the exercise yet. | `candidate` |
| `NS-S01-A-V10` | `QST` | I haven’t started the exercise yet, at least not yet. | `candidate` |

#### Parent Anchor B

> I still haven’t begun the exercise.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S01-B-V01` | `LEX` | I still haven’t begun the workout. | `candidate` |
| `NS-S01-B-V03` | `NAT` | Yeah, i still haven’t begun the exercise. | `candidate` |
| `NS-S01-B-V04` | `EXP` | I still haven’t begun the exercise — I haven't started it. | `candidate` |
| `NS-S01-B-V07` | `PRG` | As of now, i still haven’t begun the exercise. | `candidate` |
| `NS-S01-B-V08` | `CMK` | Basically, yeah, i still haven’t begun the exercise. | `candidate` |
| `NS-S01-B-V10` | `QST` | I still haven’t begun the exercise, at least not yet. | `candidate` |

#### Parent Anchor C

> The exercise hasn’t been started on my side yet.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S01-C-V01` | `LEX` | The exercise hasn’t been started on my side so far. | `candidate` |
| `NS-S01-C-V03` | `NAT` | Yeah, the exercise hasn’t been started on my side yet. | `candidate` |
| `NS-S01-C-V04` | `EXP` | The exercise hasn’t been started on my side yet. | `candidate` |
| `NS-S01-C-V07` | `PRG` | As of now, the exercise hasn’t been started on my side yet. | `candidate` |
| `NS-S01-C-V08` | `CMK` | You know, yeah, the exercise hasn’t been started on my side yet. | `candidate` |
| `NS-S01-C-V10` | `QST` | The exercise hasn’t been started on my side yet, at least not yet. | `candidate` |

---

### NS-S02 — Task Remains Untouched

- **Subtype:** `NS-01 Direct Non-Execution`
- **Domain:** Medication

#### Parent Anchor A

> I haven’t taken any of the medicine yet.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S02-A-V01` | `LEX` | I still haven't taken any of the medicine yet. | `candidate` |
| `NS-S02-A-V03` | `NAT` | No, i haven’t taken any of the medicine yet. | `candidate` |
| `NS-S02-A-V04` | `EXP` | I haven’t taken any of the medicine yet. | `candidate` |
| `NS-S02-A-V07` | `PRG` | As of now, i haven’t taken any of the medicine yet. | `candidate` |
| `NS-S02-A-V08` | `CMK` | Well, i haven’t taken any of the medicine yet. | `candidate` |
| `NS-S02-A-V10` | `QST` | I haven’t taken any of the medicine yet, at least not yet. | `candidate` |

#### Parent Anchor B

> I haven’t done anything with the dose so far.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S02-B-V01` | `LEX` | I still haven't done anything with the dose so far. | `candidate` |
| `NS-S02-B-V03` | `NAT` | No, i haven’t done anything with the dose so far. | `candidate` |
| `NS-S02-B-V04` | `EXP` | I haven’t done anything with the dose so far — I haven't started it. | `candidate` |
| `NS-S02-B-V07` | `PRG` | As of now, i haven’t done anything with the dose so far. | `candidate` |
| `NS-S02-B-V08` | `CMK` | Well, i haven’t done anything with the dose so far. | `candidate` |
| `NS-S02-B-V10` | `QST` | I haven’t done anything with the dose so far, at least not yet. | `candidate` |

#### Parent Anchor C

> The dose is still untouched.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S02-C-V01` | `LEX` | The medicine is still untouched. | `candidate` |
| `NS-S02-C-V03` | `NAT` | No, the dose is still untouched. | `candidate` |
| `NS-S02-C-V04` | `EXP` | The dose is still untouched — I haven't started it. | `candidate` |
| `NS-S02-C-V07` | `PRG` | As of now, the dose is still untouched. | `candidate` |
| `NS-S02-C-V08` | `CMK` | Well, the dose is still untouched. | `candidate` |
| `NS-S02-C-V10` | `QST` | The dose is still untouched, at least not yet. | `candidate` |

---

### NS-S03 — Current Non-Execution

- **Subtype:** `NS-01 Direct Non-Execution`
- **Domain:** Exercise

#### Parent Anchor A

> I’m not exercising right now.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S03-A-V01` | `LEX` | I'm currently not exercising right now. | `candidate` |
| `NS-S03-A-V03` | `NAT` | Yeah, i’m not exercising right now. | `candidate` |
| `NS-S03-A-V04` | `EXP` | I’m not exercising right now — I haven't started it. | `candidate` |
| `NS-S03-A-V07` | `PRG` | As of now, i’m not exercising right now. | `candidate` |
| `NS-S03-A-V08` | `CMK` | Right, yeah, i’m not exercising right now. | `candidate` |
| `NS-S03-A-V10` | `QST` | I’m not exercising right now, at least not yet. | `candidate` |

#### Parent Anchor B

> I’m not doing the exercise at the moment.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S03-B-V01` | `LEX` | I'm currently not doing the exercise at the moment. | `candidate` |
| `NS-S03-B-V03` | `NAT` | No, i’m not doing the exercise at the moment. | `candidate` |
| `NS-S03-B-V04` | `EXP` | I’m not doing the exercise at the moment — I haven't started it. | `candidate` |
| `NS-S03-B-V07` | `PRG` | As of now, i’m not doing the exercise at the moment. | `candidate` |
| `NS-S03-B-V08` | `CMK` | Well, i’m not doing the exercise at the moment. | `candidate` |
| `NS-S03-B-V10` | `QST` | I’m not doing the exercise at the moment, at least not yet. | `candidate` |

#### Parent Anchor C

> I’m not on the exercise yet.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S03-C-V01` | `LEX` | I'm currently not on the exercise yet. | `candidate` |
| `NS-S03-C-V03` | `NAT` | At the moment, i’m not on the exercise yet. | `candidate` |
| `NS-S03-C-V04` | `EXP` | I’m not on the exercise yet. | `candidate` |
| `NS-S03-C-V07` | `PRG` | As of now, i’m not on the exercise yet. | `candidate` |
| `NS-S03-C-V08` | `CMK` | Right, i’m not on the exercise yet. | `candidate` |
| `NS-S03-C-V10` | `QST` | I’m not on the exercise yet, at least not yet. | `candidate` |

---

### NS-S04 — Straightforward Future Action

- **Subtype:** `NS-02 Future / Deferred Action`
- **Domain:** Medication

#### Parent Anchor A

> I’ll take the medicine later.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S04-A-V01` | `LEX` | I'm going to take the medicine later. | `candidate` |
| `NS-S04-A-V03` | `NAT` | At the moment, i’ll take the medicine later. | `candidate` |
| `NS-S04-A-V04` | `EXP` | I’ll take the medicine later — I haven't started yet. | `candidate` |
| `NS-S04-A-V07` | `PRG` | Just to clarify, i’ll take the medicine later. | `candidate` |
| `NS-S04-A-V08` | `CMK` | Right, i’ll take the medicine later. | `candidate` |
| `NS-S04-A-V10` | `QST` | I’ll take the medicine later, is that okay? | `candidate` |

#### Parent Anchor B

> I’m going to take it tonight.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S04-B-V01` | `LEX` | I'm planning to to take it tonight. | `candidate` |
| `NS-S04-B-V03` | `NAT` | Honestly, i’m going to take it tonight. | `candidate` |
| `NS-S04-B-V04` | `EXP` | I’m going to take it tonight — I haven't started yet. | `candidate` |
| `NS-S04-B-V07` | `PRG` | Just to clarify, i’m going to take it tonight. | `candidate` |
| `NS-S04-B-V08` | `CMK` | Okay, i’m going to take it tonight. | `candidate` |
| `NS-S04-B-V10` | `QST` | I’m going to take it tonight, is that okay? | `candidate` |

#### Parent Anchor C

> I’ll get to the dose later.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S04-C-V01` | `LEX` | I'm going to get to the dose later. | `candidate` |
| `NS-S04-C-V03` | `NAT` | At the moment, i’ll get to the dose later. | `candidate` |
| `NS-S04-C-V04` | `EXP` | I’ll get to the dose later — I haven't started yet. | `candidate` |
| `NS-S04-C-V07` | `PRG` | Just to clarify, i’ll get to the dose later. | `candidate` |
| `NS-S04-C-V08` | `CMK` | Right, i’ll get to the dose later. | `candidate` |
| `NS-S04-C-V10` | `QST` | I’ll get to the dose later, is that okay? | `candidate` |

---

### NS-S05 — Deferred Start

- **Subtype:** `NS-02 Future / Deferred Action`
- **Domain:** Exercise

#### Parent Anchor A

> I haven’t started the exercises yet; I’ll do them after lunch.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S05-A-V01` | `LEX` | I still haven't started the exercises yet; I’ll do them after lunch. | `candidate` |
| `NS-S05-A-V03` | `NAT` | Yeah, i haven’t started the exercises yet; I’ll do them after lunch. | `candidate` |
| `NS-S05-A-V04` | `EXP` | I haven’t started the exercises yet; I’ll do them after lunch — I haven't started yet. | `candidate` |
| `NS-S05-A-V07` | `PRG` | Just to clarify, i haven’t started the exercises yet; I’ll do them after lunch. | `candidate` |
| `NS-S05-A-V08` | `CMK` | I mean, yeah, i haven’t started the exercises yet; I’ll do them after lunch. | `candidate` |
| `NS-S05-A-V10` | `QST` | I haven’t started the exercises yet; I’ll do them after lunch, is that okay? | `candidate` |

#### Parent Anchor B

> I’ll start the exercises this evening.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S05-B-V01` | `LEX` | I'm going to start the exercises this evening. | `candidate` |
| `NS-S05-B-V03` | `NAT` | Yeah, i’ll start the exercises this evening. | `candidate` |
| `NS-S05-B-V04` | `EXP` | I’ll start the exercises this evening — I haven't started yet. | `candidate` |
| `NS-S05-B-V07` | `PRG` | Just to clarify, i’ll start the exercises this evening. | `candidate` |
| `NS-S05-B-V08` | `CMK` | I must say, yeah, i’ll start the exercises this evening. | `candidate` |
| `NS-S05-B-V10` | `QST` | I’ll start the exercises this evening, is that okay? | `candidate` |

#### Parent Anchor C

> I’ll get started on the routine when I’m back.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S05-C-V01` | `LEX` | I'm going to get started on the routine when I’m back. | `candidate` |
| `NS-S05-C-V03` | `NAT` | No, i’ll get started on the routine when I’m back. | `candidate` |
| `NS-S05-C-V04` | `EXP` | I’ll get started on the routine when I’m back — I haven't started yet. | `candidate` |
| `NS-S05-C-V07` | `PRG` | Just to clarify, i’ll get started on the routine when I’m back. | `candidate` |
| `NS-S05-C-V08` | `CMK` | Well, i’ll get started on the routine when I’m back. | `candidate` |
| `NS-S05-C-V10` | `QST` | I’ll get started on the routine when I’m back, is that okay? | `candidate` |

---

### NS-S06 — Later Completion Intention

- **Subtype:** `NS-02 Future / Deferred Action`
- **Domain:** Physiotherapy

#### Parent Anchor A

> I haven’t started it; I’ll finish the routine tonight.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S06-A-V01` | `LEX` | I still haven't started it; I’ll finish the routine tonight. | `candidate` |
| `NS-S06-A-V03` | `NAT` | For now, i haven’t started it; I’ll finish the routine tonight. | `candidate` |
| `NS-S06-A-V04` | `EXP` | I haven’t started it; I’ll finish the routine tonight — I haven't started yet. | `candidate` |
| `NS-S06-A-V07` | `PRG` | Just to clarify, i haven’t started it; I’ll finish the routine tonight. | `candidate` |
| `NS-S06-A-V08` | `CMK` | Honestly, i haven’t started it; I’ll finish the routine tonight. | `candidate` |
| `NS-S06-A-V10` | `QST` | I haven’t started it; I’ll finish the routine tonight, is that okay? | `candidate` |

#### Parent Anchor B

> I’m going to get the physiotherapy done later.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S06-B-V01` | `LEX` | I'm planning to to get the physiotherapy done later. | `candidate` |
| `NS-S06-B-V03` | `NAT` | Yeah, i’m going to get the physiotherapy done later. | `candidate` |
| `NS-S06-B-V04` | `EXP` | I’m going to get the physiotherapy done later — I haven't started yet. | `candidate` |
| `NS-S06-B-V07` | `PRG` | Just to clarify, i’m going to get the physiotherapy done later. | `candidate` |
| `NS-S06-B-V08` | `CMK` | I mean, yeah, i’m going to get the physiotherapy done later. | `candidate` |
| `NS-S06-B-V10` | `QST` | I’m going to get the physiotherapy done later, is that okay? | `candidate` |

#### Parent Anchor C

> The routine is something I’ll take care of this evening.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S06-C-V01` | `LEX` | The routine is something I'm going to take care of this evening. | `candidate` |
| `NS-S06-C-V03` | `NAT` | Yeah, the routine is something I’ll take care of this evening. | `candidate` |
| `NS-S06-C-V04` | `EXP` | The routine is something I’ll take care of this evening — I haven't started yet. | `candidate` |
| `NS-S06-C-V07` | `PRG` | Just to clarify, the routine is something I’ll take care of this evening. | `candidate` |
| `NS-S06-C-V08` | `CMK` | As I said, yeah, the routine is something I’ll take care of this evening. | `candidate` |
| `NS-S06-C-V10` | `QST` | The routine is something I’ll take care of this evening, is that okay? | `candidate` |

---

### NS-S07 — Condition-Dependent Start

- **Subtype:** `NS-03 Conditional Future Action`
- **Domain:** Exercise

#### Parent Anchor A

> If I get enough time, I’ll do the exercise.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S07-A-V01` | `LEX` | If I get enough time, I'm going to do the exercise. | `candidate` |
| `NS-S07-A-V03` | `NAT` | Yeah, if I get enough time, I’ll do the exercise. | `candidate` |
| `NS-S07-A-V04` | `EXP` | If I get enough time, I’ll do the exercise — I haven't begun the task. | `candidate` |
| `NS-S07-A-V07` | `PRG` | Just to clarify, if I get enough time, I’ll do the exercise. | `candidate` |
| `NS-S07-A-V08` | `CMK` | I mean, yeah, if I get enough time, I’ll do the exercise. | `candidate` |
| `NS-S07-A-V10` | `QST` | If I get enough time, I’ll do the exercise, is that okay? | `candidate` |

#### Parent Anchor B

> I’ll exercise if I get a free hour.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S07-B-V01` | `LEX` | I'm going to exercise if I get a free hour. | `candidate` |
| `NS-S07-B-V03` | `NAT` | At the moment, i’ll exercise if I get a free hour. | `candidate` |
| `NS-S07-B-V04` | `EXP` | I’ll exercise if I get a free hour — I haven't begun the task. | `candidate` |
| `NS-S07-B-V07` | `PRG` | Just to clarify, i’ll exercise if I get a free hour. | `candidate` |
| `NS-S07-B-V08` | `CMK` | Right, i’ll exercise if I get a free hour. | `candidate` |
| `NS-S07-B-V10` | `QST` | I’ll exercise if I get a free hour, is that okay? | `candidate` |

#### Parent Anchor C

> The exercise will happen if I can get some time later.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S07-C-V01` | `LEX` | The exercise will happen if I can get some time later. | `candidate` |
| `NS-S07-C-V03` | `NAT` | Honestly, the exercise will happen if I can get some time later. | `candidate` |
| `NS-S07-C-V04` | `EXP` | The exercise will happen if I can get some time later — I haven't begun the task. | `candidate` |
| `NS-S07-C-V07` | `PRG` | Just to clarify, the exercise will happen if I can get some time later. | `candidate` |
| `NS-S07-C-V08` | `CMK` | Okay, the exercise will happen if I can get some time later. | `candidate` |
| `NS-S07-C-V10` | `QST` | The exercise will happen if I can get some time later, is that okay? | `candidate` |

---

### NS-S08 — Event-Triggered Future Start

- **Subtype:** `NS-03 Conditional Future Action`
- **Domain:** Medication

#### Parent Anchor A

> I’ll take the medicine after dinner.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S08-A-V01` | `LEX` | I'm going to take the medicine after dinner. | `candidate` |
| `NS-S08-A-V03` | `NAT` | For now, i’ll take the medicine after dinner. | `candidate` |
| `NS-S08-A-V04` | `EXP` | I’ll take the medicine after dinner — I haven't begun the task. | `candidate` |
| `NS-S08-A-V07` | `PRG` | Just to clarify, i’ll take the medicine after dinner. | `candidate` |
| `NS-S08-A-V08` | `CMK` | Honestly, i’ll take the medicine after dinner. | `candidate` |
| `NS-S08-A-V10` | `QST` | I’ll take the medicine after dinner, is that okay? | `candidate` |

#### Parent Anchor B

> Once I finish dinner, I’ll take it.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S08-B-V01` | `LEX` | Once I finish dinner, I'm going to take it. | `candidate` |
| `NS-S08-B-V03` | `NAT` | At the moment, once I finish dinner, I’ll take it. | `candidate` |
| `NS-S08-B-V04` | `EXP` | Once I finish dinner, I’ll take it — I haven't begun the task. | `candidate` |
| `NS-S08-B-V07` | `PRG` | Just to clarify, once I finish dinner, I’ll take it. | `candidate` |
| `NS-S08-B-V08` | `CMK` | Right, once I finish dinner, I’ll take it. | `candidate` |
| `NS-S08-B-V10` | `QST` | Once I finish dinner, I’ll take it, is that okay? | `candidate` |

#### Parent Anchor C

> The dose comes after I’m done eating.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S08-C-V01` | `LEX` | The dose comes after I'm done eating. | `candidate` |
| `NS-S08-C-V03` | `NAT` | No, the dose comes after I’m done eating. | `candidate` |
| `NS-S08-C-V04` | `EXP` | The dose comes after I’m done eating — I haven't begun the task. | `candidate` |
| `NS-S08-C-V07` | `PRG` | Just to clarify, the dose comes after I’m done eating. | `candidate` |
| `NS-S08-C-V08` | `CMK` | Well, the dose comes after I’m done eating. | `candidate` |
| `NS-S08-C-V10` | `QST` | The dose comes after I’m done eating, is that okay? | `candidate` |

---

### NS-S09 — Conditional Availability

- **Subtype:** `NS-03 Conditional Future Action`
- **Domain:** Physiotherapy

#### Parent Anchor A

> If I have enough time, I’ll do the physiotherapy.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S09-A-V01` | `LEX` | If I have enough time, I'm going to do the physiotherapy. | `candidate` |
| `NS-S09-A-V03` | `NAT` | No, if I have enough time, I’ll do the physiotherapy. | `candidate` |
| `NS-S09-A-V04` | `EXP` | If I have enough time, I’ll do the physiotherapy — I haven't begun the task. | `candidate` |
| `NS-S09-A-V07` | `PRG` | Just to clarify, if I have enough time, I’ll do the physiotherapy. | `candidate` |
| `NS-S09-A-V08` | `CMK` | Well, if I have enough time, I’ll do the physiotherapy. | `candidate` |
| `NS-S09-A-V10` | `QST` | If I have enough time, I’ll do the physiotherapy, is that okay? | `candidate` |

#### Parent Anchor B

> I’ll do the routine if I get a break later.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S09-B-V01` | `LEX` | I'm going to do the routine if I get a break later. | `candidate` |
| `NS-S09-B-V03` | `NAT` | Honestly, i’ll do the routine if I get a break later. | `candidate` |
| `NS-S09-B-V04` | `EXP` | I’ll do the routine if I get a break later — I haven't begun the task. | `candidate` |
| `NS-S09-B-V07` | `PRG` | Just to clarify, i’ll do the routine if I get a break later. | `candidate` |
| `NS-S09-B-V08` | `CMK` | Okay, i’ll do the routine if I get a break later. | `candidate` |
| `NS-S09-B-V10` | `QST` | I’ll do the routine if I get a break later, is that okay? | `candidate` |

#### Parent Anchor C

> I can get to the therapy if I’m free this evening.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S09-C-V01` | `LEX` | I can get to the therapy if I'm free this evening. | `candidate` |
| `NS-S09-C-V03` | `NAT` | Yeah, i can get to the therapy if I’m free this evening. | `candidate` |
| `NS-S09-C-V04` | `EXP` | I can get to the therapy if I’m free this evening — I haven't begun the task. | `candidate` |
| `NS-S09-C-V07` | `PRG` | Just to clarify, i can get to the therapy if I’m free this evening. | `candidate` |
| `NS-S09-C-V08` | `CMK` | Basically, yeah, i can get to the therapy if I’m free this evening. | `candidate` |
| `NS-S09-C-V10` | `QST` | I can get to the therapy if I’m free this evening, is that okay? | `candidate` |

---

### NS-S10 — Direct Refusal

- **Subtype:** `NS-04 Refusal Without Execution`
- **Domain:** Exercise

#### Parent Anchor A

> I’m not going to do the exercise.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S10-A-V01` | `LEX` | I'm currently not going to do the exercise. | `candidate` |
| `NS-S10-A-V03` | `NAT` | Honestly, i’m not going to do the exercise. | `candidate` |
| `NS-S10-A-V04` | `EXP` | I’m not going to do the exercise — I haven't started it. | `candidate` |
| `NS-S10-A-V07` | `PRG` | My answer is no — i’m not going to do the exercise. | `candidate` |
| `NS-S10-A-V08` | `CMK` | Okay, i’m not going to do the exercise. | `candidate` |
| `NS-S10-A-V10` | `QST` | I’m not going to do the exercise, okay? | `candidate` |

#### Parent Anchor B

> No, I’m not doing it.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S10-B-V01` | `LEX` | No, I'm currently not doing it. | `candidate` |
| `NS-S10-B-V03` | `NAT` | At the moment, no, I’m not doing it. | `candidate` |
| `NS-S10-B-V04` | `EXP` | No, I’m not doing it — I haven't started it. | `candidate` |
| `NS-S10-B-V07` | `PRG` | My answer is no — no, I’m not doing it. | `candidate` |
| `NS-S10-B-V08` | `CMK` | Right, no, I’m not doing it. | `candidate` |
| `NS-S10-B-V10` | `QST` | No, I’m not doing it, okay? | `candidate` |

#### Parent Anchor C

> I’ll pass on the exercise today.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S10-C-V01` | `LEX` | I'm going to pass on the exercise today. | `candidate` |
| `NS-S10-C-V03` | `NAT` | For now, i’ll pass on the exercise today. | `candidate` |
| `NS-S10-C-V04` | `EXP` | I’ll pass on the exercise today — I haven't started it. | `candidate` |
| `NS-S10-C-V07` | `PRG` | My answer is no — i’ll pass on the exercise today. | `candidate` |
| `NS-S10-C-V08` | `CMK` | Honestly, i’ll pass on the exercise today. | `candidate` |
| `NS-S10-C-V10` | `QST` | I’ll pass on the exercise today, okay? | `candidate` |

---

### NS-S11 — Rejection of the Task

- **Subtype:** `NS-04 Refusal Without Execution`
- **Domain:** Physiotherapy

#### Parent Anchor A

> I’m not going to take the medicine.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S11-A-V01` | `LEX` | I'm currently not going to take the medicine. | `candidate` |
| `NS-S11-A-V03` | `NAT` | Yeah, i’m not going to take the medicine. | `candidate` |
| `NS-S11-A-V04` | `EXP` | I’m not going to take the medicine — I haven't started it. | `candidate` |
| `NS-S11-A-V07` | `PRG` | My answer is no — i’m not going to take the medicine. | `candidate` |
| `NS-S11-A-V08` | `CMK` | Basically, yeah, i’m not going to take the medicine. | `candidate` |
| `NS-S11-A-V10` | `QST` | I’m not going to take the medicine, okay? | `candidate` |

#### Parent Anchor B

> I don’t want to do the routine.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S11-B-V01` | `LEX` | I don’t want to do the therapy routine. | `candidate` |
| `NS-S11-B-V03` | `NAT` | Yeah, i don’t want to do the routine. | `candidate` |
| `NS-S11-B-V04` | `EXP` | I don’t want to do the routine — I haven't started it. | `candidate` |
| `NS-S11-B-V07` | `PRG` | My answer is no — i don’t want to do the routine. | `candidate` |
| `NS-S11-B-V08` | `CMK` | Well, yeah, i don’t want to do the routine. | `candidate` |
| `NS-S11-B-V10` | `QST` | I don’t want to do the routine, okay? | `candidate` |

#### Parent Anchor C

> I’m skipping the therapy today.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S11-C-V01` | `LEX` | I'm skipping the therapy today. | `candidate` |
| `NS-S11-C-V03` | `NAT` | At the moment, i’m skipping the therapy today. | `candidate` |
| `NS-S11-C-V04` | `EXP` | I’m skipping the therapy today — I haven't started it. | `candidate` |
| `NS-S11-C-V07` | `PRG` | My answer is no — i’m skipping the therapy today. | `candidate` |
| `NS-S11-C-V08` | `CMK` | Right, i’m skipping the therapy today. | `candidate` |
| `NS-S11-C-V10` | `QST` | I’m skipping the therapy today, okay? | `candidate` |

---

### NS-S12 — Refusal Without Explicit Reason

- **Subtype:** `NS-04 Refusal Without Execution`
- **Domain:** Hydration

#### Parent Anchor A

> No, I won’t do it.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S12-A-V01` | `LEX` | No, I won’t do it. | `candidate` |
| `NS-S12-A-V03` | `NAT` | Yeah, no, I won’t do it. | `candidate` |
| `NS-S12-A-V04` | `EXP` | No, I won’t do it — I haven't started it. | `candidate` |
| `NS-S12-A-V07` | `PRG` | My answer is no — no, I won’t do it. | `candidate` |
| `NS-S12-A-V08` | `CMK` | Look, yeah, no, I won’t do it. | `candidate` |
| `NS-S12-A-V10` | `QST` | No, I won’t do it, okay? | `candidate` |

#### Parent Anchor B

> I’m not doing that.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S12-B-V01` | `LEX` | I'm currently not doing that. | `candidate` |
| `NS-S12-B-V03` | `NAT` | Yeah, i’m not doing that. | `candidate` |
| `NS-S12-B-V04` | `EXP` | I’m not doing that — I haven't started it. | `candidate` |
| `NS-S12-B-V07` | `PRG` | My answer is no — i’m not doing that. | `candidate` |
| `NS-S12-B-V08` | `CMK` | Right, yeah, i’m not doing that. | `candidate` |
| `NS-S12-B-V10` | `QST` | I’m not doing that, okay? | `candidate` |

#### Parent Anchor C

> I’ll pass.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S12-C-V01` | `LEX` | I'm going to pass. | `candidate` |
| `NS-S12-C-V03` | `NAT` | At the moment, i’ll pass. | `candidate` |
| `NS-S12-C-V04` | `EXP` | I’ll pass — I haven't started it. | `candidate` |
| `NS-S12-C-V07` | `PRG` | My answer is no — i’ll pass. | `candidate` |
| `NS-S12-C-V08` | `CMK` | Right, i’ll pass. | `candidate` |
| `NS-S12-C-V10` | `QST` | I’ll pass, okay? | `candidate` |

---

### NS-S13 — Non-Execution Due to Time Constraint

- **Subtype:** `NS-05 Reason-Linked Non-Execution`
- **Domain:** Exercise

#### Parent Anchor A

> I haven’t exercised because I’m too busy.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S13-A-V01` | `LEX` | I still haven't exercised because I’m too busy. | `candidate` |
| `NS-S13-A-V03` | `NAT` | Honestly, i haven’t exercised because I’m too busy. | `candidate` |
| `NS-S13-A-V04` | `EXP` | I haven’t exercised because I’m too busy — the task hasn't started. | `candidate` |
| `NS-S13-A-V07` | `PRG` | As of now, i haven’t exercised because I’m too busy. | `candidate` |
| `NS-S13-A-V08` | `CMK` | Okay, i haven’t exercised because I’m too busy. | `candidate` |
| `NS-S13-A-V10` | `QST` | I haven’t exercised because I’m too busy, at least not yet. | `candidate` |

#### Parent Anchor B

> I haven’t had time to do the exercises.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S13-B-V01` | `LEX` | I still haven't had time to do the exercises. | `candidate` |
| `NS-S13-B-V03` | `NAT` | At the moment, i haven’t had time to do the exercises. | `candidate` |
| `NS-S13-B-V04` | `EXP` | I haven’t had time to do the exercises — the task hasn't started. | `candidate` |
| `NS-S13-B-V07` | `PRG` | As of now, i haven’t had time to do the exercises. | `candidate` |
| `NS-S13-B-V08` | `CMK` | Right, i haven’t had time to do the exercises. | `candidate` |
| `NS-S13-B-V10` | `QST` | I haven’t had time to do the exercises, at least not yet. | `candidate` |

#### Parent Anchor C

> The exercise hasn’t happened; my schedule has been packed.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S13-C-V01` | `LEX` | The exercise hasn’t happened; my schedule has been packed. | `candidate` |
| `NS-S13-C-V03` | `NAT` | For now, the exercise hasn’t happened; my schedule has been packed. | `candidate` |
| `NS-S13-C-V04` | `EXP` | The exercise hasn’t happened; my schedule has been packed — the task hasn't started. | `candidate` |
| `NS-S13-C-V07` | `PRG` | As of now, the exercise hasn’t happened; my schedule has been packed. | `candidate` |
| `NS-S13-C-V08` | `CMK` | Honestly, the exercise hasn’t happened; my schedule has been packed. | `candidate` |
| `NS-S13-C-V10` | `QST` | The exercise hasn’t happened; my schedule has been packed, at least not yet. | `candidate` |

---

### NS-S14 — Non-Execution Due to Forgetting

- **Subtype:** `NS-05 Reason-Linked Non-Execution`
- **Domain:** Medication

#### Parent Anchor A

> I forgot to take the medicine.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S14-A-V01` | `LEX` | It slipped my mind to take the medicine. | `candidate` |
| `NS-S14-A-V03` | `NAT` | Yeah, i forgot to take the medicine. | `candidate` |
| `NS-S14-A-V04` | `EXP` | I forgot to take the medicine — the task hasn't started. | `candidate` |
| `NS-S14-A-V07` | `PRG` | As of now, i forgot to take the medicine. | `candidate` |
| `NS-S14-A-V08` | `CMK` | I mean, yeah, i forgot to take the medicine. | `candidate` |
| `NS-S14-A-V10` | `QST` | I forgot to take the medicine, at least not yet. | `candidate` |

#### Parent Anchor B

> I completely forgot about the dose.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S14-B-V01` | `LEX` | I completely forgot about the medicine. | `candidate` |
| `NS-S14-B-V03` | `NAT` | For now, i completely forgot about the dose. | `candidate` |
| `NS-S14-B-V04` | `EXP` | I completely forgot about the dose — the task hasn't started. | `candidate` |
| `NS-S14-B-V07` | `PRG` | As of now, i completely forgot about the dose. | `candidate` |
| `NS-S14-B-V08` | `CMK` | Honestly, i completely forgot about the dose. | `candidate` |
| `NS-S14-B-V10` | `QST` | I completely forgot about the dose, at least not yet. | `candidate` |

#### Parent Anchor C

> The medicine never got taken because I forgot.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S14-C-V01` | `LEX` | The medicine never got taken because It slipped my mind. | `candidate` |
| `NS-S14-C-V03` | `NAT` | No, the medicine never got taken because I forgot. | `candidate` |
| `NS-S14-C-V04` | `EXP` | The medicine never got taken because I forgot — the task hasn't started. | `candidate` |
| `NS-S14-C-V07` | `PRG` | As of now, the medicine never got taken because I forgot. | `candidate` |
| `NS-S14-C-V08` | `CMK` | Well, the medicine never got taken because I forgot. | `candidate` |
| `NS-S14-C-V10` | `QST` | The medicine never got taken because I forgot, at least not yet. | `candidate` |

---

### NS-S15 — Non-Execution Due to Inability / Unavailability

- **Subtype:** `NS-05 Reason-Linked Non-Execution`
- **Domain:** Physiotherapy

#### Parent Anchor A

> I couldn’t start the physiotherapy today.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S15-A-V01` | `LEX` | I wasn't able to start the physiotherapy today. | `candidate` |
| `NS-S15-A-V03` | `NAT` | For now, i couldn’t start the physiotherapy today. | `candidate` |
| `NS-S15-A-V04` | `EXP` | I couldn’t start the physiotherapy today — the task hasn't started. | `candidate` |
| `NS-S15-A-V07` | `PRG` | As of now, i couldn’t start the physiotherapy today. | `candidate` |
| `NS-S15-A-V08` | `CMK` | Honestly, i couldn’t start the physiotherapy today. | `candidate` |
| `NS-S15-A-V10` | `QST` | I couldn’t start the physiotherapy today, at least not yet. | `candidate` |

#### Parent Anchor B

> I wasn’t able to do the routine.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S15-B-V01` | `LEX` | I wasn't in a position to do the routine. | `candidate` |
| `NS-S15-B-V03` | `NAT` | No, i wasn’t able to do the routine. | `candidate` |
| `NS-S15-B-V04` | `EXP` | I wasn’t able to do the routine — the task hasn't started. | `candidate` |
| `NS-S15-B-V07` | `PRG` | As of now, i wasn’t able to do the routine. | `candidate` |
| `NS-S15-B-V08` | `CMK` | Well, i wasn’t able to do the routine. | `candidate` |
| `NS-S15-B-V10` | `QST` | I wasn’t able to do the routine, at least not yet. | `candidate` |

#### Parent Anchor C

> I never got to the therapy because I couldn’t.

| ID | Type | Candidate utterance | Status |
|---|---|---|---|
| `NS-S15-C-V01` | `LEX` | I never got to the therapy because I wasn't able to. | `candidate` |
| `NS-S15-C-V03` | `NAT` | Honestly, i never got to the therapy because I couldn’t. | `candidate` |
| `NS-S15-C-V04` | `EXP` | I never got to the therapy because I couldn’t — the task hasn't started. | `candidate` |
| `NS-S15-C-V07` | `PRG` | As of now, i never got to the therapy because I couldn’t. | `candidate` |
| `NS-S15-C-V08` | `CMK` | Okay, i never got to the therapy because I couldn’t. | `candidate` |
| `NS-S15-C-V10` | `QST` | I never got to the therapy because I couldn’t, at least not yet. | `candidate` |

---

## 6. Stage 3A Acceptance Gate

A candidate is not production data until it passes semantic and linguistic validation.

Reject when:

- execution has accidentally begun;
- completion is implied;
- the semantic subtype changes;
- the parent scenario changes;
- the target task changes;
- the wording becomes unnatural;
- the candidate is a near-duplicate;
- another ontology becomes the primary signal;
- a lexical shortcut determines the state.

The formal acceptance test requires the same semantic scenario, execution status, execution condition, target task, natural language, genuine linguistic variation, no deterministic lexical shortcut, no near-duplicate, and preserved lineage. fileciteturn156file2L438-L463

## 7. Current File Progress

| Stage 3A production file | Status |
|---|---|
| `stage_3a_standard_variants.md` | ✅ Specification complete |
| `stage_3a_not_started_variants.md` | 🔄 Candidate generation complete; semantic QC pending |
| `stage_3a_in_progress_variants.md` | ⏳ Not started |
| `stage_3a_completed_variants.md` | ⏳ Not started |

## 8. Lineage Rule

All descendants of a Stage 1 scenario remain one leakage group:

```text
Execution State
  ↓
Subtype
  ↓
Scenario
  ↓
Initial Anchor
  ↓
Stage 3A Variant
```

The complete lineage tree must remain together for the later group-based dataset split. fileciteturn156file3L518-L544