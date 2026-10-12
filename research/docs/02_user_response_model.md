<!-- research/03_simulator_design/12_user_response_model.md -->

# User Response Model

## Status

**Status:** PROVISIONAL --- NOT FROZEN

---

## 1. Purpose

This document defines the user's **immediate behavioral reaction** to a persuasion intervention.

User response is separate from:
- task completion;
- user tolerance;
- future persuasion effectiveness.

---

## 2. Design Principle

The simulator separates three constructs:

```text
                  Action a_t ─────────────┐
                       │                  │
                       ▼                  ▼
               Completion Y_t      Excess X_t
                       │                  │
                       └────────┬─────────┘
                                │ (Generation)
                                ▼
                       User Response R_t
                                │
                                ▼
                       Tolerance Update Z_{t+1}
                                │
                                ▼
                        Future State S_{t+1}
```

Task completion measures **whether the task was performed**.

User response measures **how the user reacted to the intervention**.

Tolerance is a longer-term latent state updated from user responses.

---

## 3. Response Variable

Define:

$$
R_t \in \{VP, P, I, N, VN\}
$$

where:

| Symbol | Meaning |
| :---: | :--- |
| VP | Very Positive |
| P | Positive |
| I | Indifferent |
| N | Negative |
| VN | Very Negative |

These are ordered from most favorable to least favorable.

---

## 4. Response vs. Task Completion

Task completion is:

$$
Y_t \in \{0, 1\}.
$$

Response and completion are **not equivalent**.

Examples:

| Outcome | Completion | Response |
| :--- | :---: | :---: |
| User completes task and appreciates reminder | 1 | P / VP |
| User completes task but feels pressured | 1 | N |
| User ignores reminder without annoyance | 0 | I |
| User rejects intervention and becomes irritated | 0 | VN |

Therefore:

$$
Y_t \not\Rightarrow R_t, \quad R_t \not\Rightarrow Y_t.
$$

---

## 5. Response Generation

The provisional response model is:

$$
P(R_t) = f(Y_t, X_t, H_t),
$$

where:
- $Y_t$: task completion;
- $X_t = \max(0, I_{a_t} - N_t)$: excess intervention;
- $H_t$: relevant interaction history.

The exact probabilistic model remains to be designed.

---

## 6. Design Assumptions

- Response represents **behavioral reaction**, not emotion modeling.
- Excess intervention increases the likelihood of negative responses.
- Repeated interventions may worsen response through history effects.
- Task-context intervention need $N_t$ does not directly determine response; it influences response indirectly through intervention success and excess intervention.

---

## 7. Role in Environment

User response does **not** directly change task completion.

Instead:
```text
  Action
     │
     ▼
  Task Completion
     │
     ▼
  User Response
     │
     ▼
  Tolerance Update
     │
     ▼
  Future State
```
This preserves a clear causal structure.

---

## 8. Current Decisions

| Item | Status |
| :--- | :--- |
| Separate completion and response | SELECTED |
| Five ordered response levels | SELECTED |
| Behavioral (not emotional) response | SELECTED |
| Response depends on completion, excess intervention and history | PROVISIONAL |
| Exact response probabilities | NOT DESIGNED |

**USER RESPONSE MODEL STATUS: PROVISIONAL**
