<!-- research/06_experiments/response_model_calibration.md -->

# Response Model Calibration Plan

## Status

**Status:** PLANNED EXPERIMENTAL STUDY

---

## 1. Scope

This document specifies the calibration methodology for the User Response Model. The mathematical formulation is considered **frozen** for Version 1; only model parameters are subject to calibration.

```text
  Phase 1: Grid Search ────────► Phase 2: Sensitivity ────────► Phase 3: Ablation
                                                                       │
                                                                       ▼
  Selected Parameters ◄──────── Phase 4: Robustness ◄──────────────────┘
```

The following mathematical components will be calibrated:

### Appraisal Coefficients
$$
z = b + w_Y Y - w_F F - w_X X - w_k \hat{k}
$$

Parameters to calibrate:
- $w_Y$: task success weight
- $w_F$: fatigue sensitivity weight
- $w_X$: excess intervention penalty weight
- $w_k$: repetition penalty weight

### Ordinal Logistic Thresholds
$$
\theta_1 < \theta_2 < \theta_3 < \theta_4
$$

Initial baseline thresholds:

$$
(-1.5, -0.5, 0.5, 1.5)
$$

These thresholds determine the mapping from latent appraisal $z$ to ordinal response probabilities.

---

## 2. Calibration Objectives

The calibrated model should satisfy:
- Psychologically plausible responses.
- Smooth probability transitions.
- Stable reinforcement learning convergence.
- Meaningful differentiation between persuasion strategies.
- Robustness across heterogeneous user profiles.
- No pathological response distributions.

---

## 3. Stage 1 — Grid Search

### Objective
Identify stable parameter regions.

### Appraisal Coefficients
Suggested search ranges:

| Parameter | Candidate Values |
| :--- | :--- |
| $w_Y$ | 1.0, 1.5, 2.0, 2.5, 3.0 |
| $w_F$ | 0.5, 1.0, 1.5, 2.0 |
| $w_X$ | 0.5, 1.0, 1.5, 2.0 |
| $w_k$ | 0.0, 0.25, 0.5, 0.75, 1.0 |

### Thresholds
Explore symmetric threshold configurations such as:
- $(-2.0, -1.0, 1.0, 2.0)$
- $(-1.5, -0.5, 0.5, 1.5)$
- $(-1.0, -0.25, 0.25, 1.0)$

Record metrics: cumulative reward, response distribution, task completion, fatigue, and learning convergence.

---

## 4. Stage 2 — Sensitivity Analysis

Vary one parameter at a time while fixing all others.

Measure:
- Latent appraisal distribution ($z$)
- Response probabilities
- Policy behavior
- Cumulative reward
- Completion rate
- Fatigue evolution

---

## 5. Stage 3 — Ablation Study

Evaluate the contribution of each appraisal component.

Ablation conditions:
- $w_Y = 0$
- $w_F = 0$
- $w_X = 0$
- $w_k = 0$

Also evaluate threshold sensitivity by widening and narrowing threshold spacing.

---

## 6. Stage 4 — Robustness Study

Evaluate the calibrated parameters under different simulated users:
- fatigue-sensitive
- fatigue-resistant
- highly compliant
- highly resistant
- low-adherence
- high-adherence

---

## 7. Evaluation Metrics

### Primary Metrics
- Average cumulative reward
- Task completion rate
- Average fatigue
- Remaining persuasion budget
- Response category frequencies

### Secondary Metrics
- Policy entropy
- Action diversity
- Repetition frequency
- Excess intervention frequency
- Training stability

---

## 8. Acceptance Criteria

A calibrated response model must satisfy:
- Stable RL convergence.
- Smooth response probability curves.
- Realistic response distributions.
- No dominant persuasion strategy.
- Robust behavior across user populations.
- No reward hacking or pathological policies.

---

## 9. Frozen Mathematical Structure

The following equations are **not** modified during calibration:

### Appraisal Model
$$
z = b + w_Y Y - w_F F - w_X X - w_k \hat{k}
$$

### Ordinal Logistic Model
$$
P(R \le c) = \sigma(\theta_c - z)
$$

### Response Sampling
$$
R_t \sim \text{Categorical}(P(\text{VN}), P(\text{N}), P(\text{I}), P(\text{P}), P(\text{VP}))
$$

Only the coefficients ($w_Y, w_F, w_X, w_k$) and thresholds ($\theta_1, \theta_2, \theta_3, \theta_4$) are subject to calibration.
