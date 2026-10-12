# User Response Mapping Model

## Status

**Status:** PROVISIONALLY FROZEN (Architecture)

---

# Objective

Map the user's latent psychological appraisal into one of five observable response categories.

\[
R_t \in \{VP,\;P,\;I,\;N,\;VN\}
\]

The mapping should be:

- stochastic,
- smooth,
- psychologically plausible,
- suitable for RL environments.

---

# Selected Architecture

The response model consists of three stages.

```text
Environment State
      │
      ▼
Latent Response Score (z)
      │
      ▼
Ordinal Logistic Mapping
      │
      ▼
Response Probability Distribution
      │
      ▼
Sample User Response
```

---

# Stage 1 — Latent Response Score

Compute a latent appraisal score

\[
z = f(N,\;Y,\;F,\;X,\;k)
\]

where

- \(N\): Task need
- \(Y\): Task success
- \(F\): Fatigue
- \(X\): Excess intervention
- \(k\): Consecutive repetition count

The exact functional form will be derived separately.

---

# Stage 2 — Ordinal Logistic Mapping

Convert the latent score into an ordered probability distribution

\[
P(R_t \mid z)
=
\{
P(VP),\;
P(P),\;
P(I),\;
P(N),\;
P(VN)
\}.
\]

The ordinal logistic model preserves the natural ordering

\[
VP > P > I > N > VN
\]

while producing smooth probability transitions.

---

# Stage 3 — Response Sampling

Sample one response according to the computed distribution.

\[
R_t \sim P(R_t \mid z)
\]

The sampled response is then used by downstream simulator components (e.g., fatigue dynamics).



## Example Behavioral Probability Distribution

The ordinal logistic model produces a smooth probability distribution over the ordered response categories. The values below are **illustrative only** and are **not** the final calibrated probabilities.

| Latent Score \(z\) | VP | P | I | N | VN |
|-------------------:|---:|---:|---:|---:|---:|
| 2.5  | 0.75 | 0.20 | 0.05 | 0.00 | 0.00 |
| 1.0  | 0.20 | 0.50 | 0.25 | 0.05 | 0.00 |
| 0.0  | 0.05 | 0.20 | 0.50 | 0.20 | 0.05 |
| -1.0 | 0.00 | 0.05 | 0.25 | 0.50 | 0.20 |
| -2.5 | 0.00 | 0.00 | 0.05 | 0.20 | 0.75 |

### Interpretation

- Larger **positive** latent scores shift probability mass toward **VP** and **P**.
- Scores near **0** are dominated by **Indifferent (I)**.
- Larger **negative** latent scores shift probability mass toward **N** and **VN**.
- Neighboring response categories retain non-zero probability, producing smooth, psychologically plausible transitions instead of abrupt threshold changes.

---

# Rationale

This architecture combines:

- **Ordinal Logistic Mapping** (smooth ordered probabilities)
- **Behavioral Distribution Sampling** (stochastic human behavior)

Advantages:

- Preserves ordinal structure.
- Produces realistic variability.
- Avoids hard thresholds.
- Supports robust RL training.
- Easy to calibrate experimentally.

---

# Comparison with Alternatives

| Method | Decision | Reason |
|---------|:--------:|--------|
| Hard thresholds | ❌ Reject | Deterministic, discontinuous |
| Softmax classifier | ❌ Reject | Ignores ordinal nature |
| Continuous score + binning | ⚠ Acceptable | Extra unnecessary stage |
| **Ordinal logistic + sampling** | ✅ Selected | Ordered, stochastic, interpretable |

---

# Remaining Work

The following remain to be derived:

1. Functional form of the latent score \(z\).
2. Ordinal logistic parameters (thresholds/coefficients).
3. Parameter calibration and sensitivity analysis.
