# Stage 2B — Minimal Pairs: B01 Not Started ↔ In Progress

## Boundary

**Boundary ID:** `B01`  
**State A:** `Not Started`  
**State B:** `In Progress`

### Diagnostic distinction

The pair must isolate whether execution of the **target task has actually begun**.

- **Not Started:** the target task has not begun.
- **In Progress:** execution of the target task has begun but is unfinished.

Preparation, intention, scheduling, or being about to begin do not establish `In Progress`.

---

## MP01-01 — Explicit initiation

**Context:** Immediately after a medication reminder.

**Not Started:**  
“I haven't started taking the medication yet.”

**In Progress:**  
“I've started taking the medication, but I haven't finished it yet.”

---

## MP01-02 — Immediate action vs preparation

**Context:** The user is preparing for the exercise routine.

**Not Started:**  
“I've got everything ready, but I haven't started the exercises.”

**In Progress:**  
“I've got everything ready, and I've started the first exercise.”

---

## MP01-03 — Hydration initiation

**Context:** The user is responding to a hydration reminder.

**Not Started:**  
“The bottle is still full; I haven't had any water yet.”

**In Progress:**  
“The bottle isn't full anymore; I've started drinking from it.”

---

## MP01-04 — Ongoing partial execution

**Context:** The user is discussing today's physiotherapy routine.

**Not Started:**  
“I haven't done any of the routine yet.”

**In Progress:**  
“I've done the first few exercises and still have some of the routine left.”

---

## MP01-05 — Future action vs current execution

**Context:** The user is deciding whether to begin the medication task.

**Not Started:**  
“I'll take the medication after I finish breakfast.”

**In Progress:**  
“I started taking the medication after breakfast, and I'm still finishing the dose.”

---

## MP01-06 — Implicit execution evidence

**Context:** The user is describing the current exercise session.

**Not Started:**  
“The exercise mat is out, but I haven't done any of the exercises.”

**In Progress:**  
“The exercise mat is out, and I'm already working through the routine.”

---

## Pair-Level Construction Rule

Across all six families:

- The target task remains the same within each pair.
- The conversational situation remains comparable.
- The primary change is **execution initiation**.
- The `Not Started` side must not contain evidence that target-task execution has begun.
- The `In Progress` side must contain actual execution evidence while remaining unfinished.
- Preparation must not be treated as execution.
- Future intention must not be treated as execution.
- Completion evidence must not replace the B01 distinction.
- The contrast must not depend on a single lexical marker such as “started” or “yet”.

## Production Metadata

```yaml
boundary_id: B01
resource_type: minimal_pair
states: [Not Started, In Progress]
pair_count: 6
utterance_count: 12
primary_diagnostic: execution_initiation
lineage_unit: pair_family
target_tasks: [Medication, Exercise, Hydration, Physiotherapy]
```

## Boundary Invariant

> **Not Started = target execution has not begun.**  
> **In Progress = target execution has begun but is unfinished.**
