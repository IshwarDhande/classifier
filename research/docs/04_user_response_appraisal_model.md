<!-- research/03_simulator_design/user_response_appraisal_model_v1.md -->

# User Response Model — Version 1 Appraisal Function (Frozen)

## Status

**Status:** FROZEN (Version 1)

---

## 1. Mathematical Formulation

The latent appraisal function is:

$$
z = b + w_Y Y - w_F F - w_X X - w_k \hat{k}
$$

where:
- $b$: baseline appraisal
- $Y$: binary task completion (Version 1)
- $F$: normalized fatigue
- $X$: excess intervention
- $\hat{k}$: normalized repetition

```text
  Inputs:
  - Task success (Y) ─────────► [ w_Y * Y (+) ] ──┐
  - Fatigue (F) ──────────────► [ w_F * F (-) ] ──┼──► [ z = 2Y - F - 1.5X - 0.5k̂ ]
  - Excess Intensity (X) ─────► [ w_X * X (-) ] ──┤
  - Repetition (k̂) ───────────► [ w_k * k̂ (-) ] ──┘
```

### Normalization
$$
\hat{k} = \frac{\min(k, k_{\max})}{k_{\max}}, \qquad k_{\max} = 5
$$

### Baseline
$$
b = 0
$$

---

## 2. Initial Coefficients

| Parameter | Value | Description |
| :--- | :---: | :--- |
| $w_Y$ | 2.0 | Task success positive weight |
| $w_F$ | 1.0 | Fatigue negative weight |
| $w_X$ | 1.5 | Excess intervention penalty weight |
| $w_k$ | 0.5 | Repetition penalty weight |

Therefore:

$$
z = 2Y - F - 1.5X - 0.5\hat{k}
$$

---

## 3. Design Decisions

- **Linear and Interpretable:** A clear formulation for ease of gradient propagation and value estimation.
- **Normalized Inputs:** Features are scaled to prevent single-feature scale dominance.
- **Binary Success:** Binary task completion ($Y \in \{0, 1\}$) represents the baseline outcome feedback.
- **Excess Intervention:** Defined as:
  $$
  X = \max(0, I - N)
  $$
- **Calibration Focus:** The initial coefficients are starting values. The core structure is frozen for Version 1.

---

## 4. Planned Parameter Calibration

The coefficients:

$$
w_Y, \ w_F, \ w_X, \ w_k
$$

are treated as **hyperparameters** for the simulation environment.

The following validation and optimization steps are planned:
1. **Grid Search:** Explore candidate coefficient values to identify stable policy regions.
2. **Sensitivity Analysis:** Quantify the influence of each coefficient on the resulting policy.
3. **Ablation Study:** Evaluate the necessity of each component to overall user behavioral representation.
4. **Robustness Study:** Test across diverse simulated user distributions to ensure learning stability.

> [!IMPORTANT]
> Calibration will only adjust coefficient values. The mathematical structure:
> $$ z = b + w_Y Y - w_F F - w_X X - w_k \hat{k} $$
> is frozen and will remain unchanged.
