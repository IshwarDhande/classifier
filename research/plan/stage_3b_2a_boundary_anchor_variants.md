# Stage 3B-A — Boundary Anchor Variant Specification

**Input:** Stage 2A Boundary Anchors  
**Expansion unit:** Individual boundary anchor  
**Goal:** Boundary-preserving linguistic expansion

## 1. Purpose

Stage 2A anchors teach where two Response Categories meet. Stage 3B-A increases linguistic diversity while preserving the anchor's exact position and diagnostic evidence.

## 2. Fixed Invariants

Preserve:

- target category;
- competing category;
- boundary ID;
- anchor role;
- semantic position;
- behavioral evidence;
- intervention;
- conversational situation.

An A-Leaning Boundary variant must remain A-Leaning Boundary, not become an A Prototype.

## 3. Anchor Roles

| Role | Required property |
|---|---|
| A Prototype | Clear A behavior |
| B Prototype | Clear B behavior |
| A-Leaning Boundary | Subtle but sufficient A evidence |
| B-Leaning Boundary | Subtle but sufficient B evidence |
| Implicit A | A inferred through behavior/pragmatics |
| Implicit B | B inferred through behavior/pragmatics |

## 4. Standard Six Variants

| Variant | Type | Purpose |
|---|---|---|
| BA-V01 | `LEX` | Different vocabulary |
| BA-V02 | `SYN` | Different syntax |
| BA-V03 | `NAT` | Natural conversational realization |
| BA-V04 | `EXP` | Explicit/implicit variation |
| BA-V05 | `PRG` | Pragmatic reformulation |
| BA-V06 | `CMK` | Conversational-marker variation |

`LEN`, `DSC`, `HES`, and `QST` may be used selectively.

## 5. Boundary Rules

Adjacent boundaries require highest precision:

```text
VP ↔ P
P  ↔ I
I  ↔ N
N  ↔ VN
```

For non-adjacent boundaries, variants must still be behaviorally justified and must not collapse into generic positive/negative examples.

## 6. Forbidden Transformations

Reject variants that:

- intensify or weaken the boundary position;
- move the example into the neighboring category;
- remove the diagnostic evidence;
- add a new competing behavioral response;
- rely on a single boundary keyword.

## 7. Acceptance Test

```text
[✓] Same boundary
[✓] Same anchor role
[✓] Same behavioral evidence
[✓] Same category
[✓] Natural wording
[✓] No lexical shortcut
[✓] No boundary drift
```

Key question:

> Would expert annotators place the original and variant on the same side of the same boundary for the same behavioral reason?
