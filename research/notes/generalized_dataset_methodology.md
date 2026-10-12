# Generalized Dataset Splitting & Training Methodology

**Document:** `generalized_dataset_methodology.md`
**Scope:** Generic methodology for single-label sentence classifiers trained on synthetically generated conversational variants (e.g., Dialogue Purpose, Response Category, etc.)
**Partition Scheme:** 70% Train / 15% Validation / 15% Test (Stratified by Scenario Family)

---

## 1. Executive Summary

This document formalizes the splitting protocol and model training methodology for conversational intent and behavioral classifiers.

The primary challenge in conversational classification is preventing the model from exploiting **surface-level shortcuts** (e.g., matching topic words, relying on specific punctuation, or memorizing scenario semantics). To ensure the classifier learns true **communicative abstractions** rather than surface heuristics, we enforce **Leakage-Safe Stratified Group Splitting** at the `scenario_id` or `parent_id` level.

```text
+--------------------------------------------------------------------------------------------------+
|                                    SPLITTING & TRAINING FLOW                                     |
+--------------------------------------------------------------------------------------------------+
|                                                                                                  |
|   N Base Scenarios × M Linguistic Realizations = Total Dataset Size                              |
|                                                                                                  |
|                                       │                                                          |
|                                       ▼                                                          |
|                    [STRATIFIED SCENARIO-LEVEL GROUP SPLIT]                                       |
|                    • All M variants of a scenario stay together                                  |
|                    • Zero semantic leakage between splits                                        |
|                    • Stratified evenly across all classes and subtypes                           |
|                                                                                                  |
|              ┌────────────────────────┼────────────────────────┐                                 |
|              ▼                        ▼                        ▼                                 |
|      [TRAIN SET (70%)]        [VAL SET (15%)]          [TEST SET (15%)]                          |
|                                                                                                  |
|              │                        │                        │                                 |
|              ▼                        ▼                        │                                 |
|   ┌──────────────────────┐  ┌───────────────────┐              │                                 |
|   │ Transformer Training │  │ Model Selection & │              │                                 |
|   │ (DeBERTa-v3 / BERT)  │─►│ Early Stopping    │              │                                 |
|   └──────────────────────┘  └───────────────────┘              │                                 |
|                                       │                        ▼                                 |
|                                       └──────────────►┌───────────────────┐                      |
|                                                       │ Final Evaluation  │                      |
|                                                       └───────────────────┘                      |
+--------------------------------------------------------------------------------------------------+
```

---

## 2. Dataset Splitting Methodology

### 2.1 The Semantic Leakage Hazard (Why Random Splitting Fails)

In our dataset construction framework, each approved semantic scenario (the "parent" or "base" scenario) is expanded into multiple linguistic realizations (e.g., Lexical, Syntactic, Conversational, Explicit/Implicit variants).

All generated realizations share the **exact same underlying communicative scenario**.

```text
+--------------------------------------------------------------------------------------------------+
|                             THE SEMANTIC LEAKAGE PROBLEM                                         |
+--------------------------------------------------------------------------------------------------+
|                                                                                                  |
|   NAIVE RANDOM SPLIT (FATAL):                                                                    |
|   [Scenario A]                                                                                   |
|   ├── Train : "Why are you recommending this?" (Direct)                                          |
|   ├── Train : "What is the reason you recommend this?" (Lexical Variant)                         |
|   └── Test  : "Why do you think I should do this?" (Syntactic Variant) <── SEMANTIC LEAKAGE!     |
|                                                                                                  |
|   Result: The model memorizes the recommendation context and achieves 99% test accuracy,         |
|   but collapses when deployed on novel conversational situations in real dialogue.               |
|                                                                                                  |
|   --------------------------------------------------------------------------------------------   |
|                                                                                                  |
|   LEAKAGE-SAFE SCENARIO GROUP SPLIT (OUR METHOD):                                                |
|   [Scenario A] ──► ALL REALIZATIONS ASSIGNED TO TRAIN                                            |
|   [Scenario B] ──► ALL REALIZATIONS ASSIGNED TO VALIDATION                                       |
|   [Scenario C] ──► ALL REALIZATIONS ASSIGNED TO TEST                                             |
|                                                                                                  |
|   Result: The model is forced to generalize the abstract communicative function to               |
|   completely unseen semantic scenarios during validation and testing.                            |
|                                                                                                  |
+--------------------------------------------------------------------------------------------------+
```

### 2.2 Stratified Group Partitioning Algorithm

To guarantee zero data leakage while preserving class balance and subtype coverage:
1. **Grouping Unit:** The grouping key is the base `scenario_id` (or `parent_id`). No base scenario crosses split boundaries. All variants derived from the same base scenario are mapped to the same split.
2. **Class Balance:** The target split ratios are approximately 70% Train, 15% Validation, and 15% Test. These ratios must be applied consistently across all classes.
3. **Subtype Stratification:** Scenarios within each semantic subtype (e.g., difficulty tiers or boundary types) are allocated deterministically to ensure that **every semantic subtype is exposed during training**, while Validation and Test evaluate novel scenarios within those exact same subtypes.

**Example Allocation Logic (for sets of 6 scenarios per subtype):**
- Scenario Index 1, 2, 3, 4 $\rightarrow$ Train (66.7%)
- Scenario Index 5 $\rightarrow$ Validation (16.7%)
- Scenario Index 6 $\rightarrow$ Test (16.7%)

This logic ensures a roughly 70/15/15 ratio while maintaining perfect grouped splits.

---

## 3. Classifier Training Methodology & Architecture Plan

### 3.1 Task Formulation

The model solves a single-sentence classification task:
$$\hat{y} = \arg\max_{c \in C} P(y = c \mid x)$$

Where:
- $x$: The user's conversational utterance (string).
- $y$: Ground-truth label mapped to a discrete set of classes $C$ (e.g., `{0, 1, 2, 3, 4}`).

### 3.2 Candidate Model Architectures

```text
+--------------------------------------------------------------------------------------------------+
|                                    MODEL ARCHITECTURE SELECTION                                  |
+--------------------------------------------------------------------------------------------------+
|                                                                                                  |
|   [OPTION 1: DeBERTa-v3-base / small] (PRIMARY RECOMMENDATION)                                   |
|   • Disentangled attention captures syntax and semantic roles cleanly.                           |
|   • Ideal for short, pragmatic utterances where subtle syntactic shifts flip classes.            |
|   • Parameter size: 86M (small) to 142M (base) -> fast inference (< 10ms latency).               |
|                                                                                                  |
|   [OPTION 2: ModernBERT-base / ModernBERT-large]                                                 |
|   • Modernized architecture with Rotary Position Embeddings (RoPE) and FlashAttention-2.         |
|   • High throughput, excellent contextual representations across diverse conversational lengths. |
|                                                                                                  |
|   [OPTION 3: Small Language Model (SLM) with Classification Head]                                |
|   • SmolLM2-360M / Qwen2.5-0.5B / Gemma-2-2B with LoRA fine-tuning.                              |
|   • Suitable if multi-task reasoning or chain-of-thought rationale extraction is required later. |
|                                                                                                  |
+--------------------------------------------------------------------------------------------------+
```

### 3.3 Training Configuration & Hyperparameter Schedule

```text
+------------------------------+-------------------------------------------------------------------+
| Hyperparameter               | Recommended Setting                                               |
+------------------------------+-------------------------------------------------------------------+
| Base Model                   | microsoft/deberta-v3-base (or answerdotai/ModernBERT-base)        |
| Max Sequence Length          | 128 tokens (covers most dialogue corpora without truncation)      |
| Batch Size                   | 16 (or 32 with gradient accumulation = 2)                         |
| Learning Rate                | 2e-5 (with AdamW optimizer, betas=(0.9, 0.999), eps=1e-8)         |
| LR Scheduler                 | Linear Warmup (10% of total steps) + Cosine Decay                 |
| Weight Decay                 | 0.01                                                              |
| Loss Function                | Cross-Entropy with Label Smoothing (epsilon = 0.05)               |
| Training Epochs              | 5 to 8 epochs                                                     |
| Early Stopping Criterion     | Validation Macro-F1 (patience = 2 epochs)                         |
| Mixed Precision              | FP16 (CUDA) or BF16 (Ampere+)                                     |
+------------------------------+-------------------------------------------------------------------+
```

### 3.4 Loss Function Formulation

To prevent overconfidence on ambiguous boundary samples, we train with label smoothed Cross-Entropy:
$$\mathcal{L}_{LS}(y, \hat{y}) = - \sum_{k=1}^{K} q_k \log \hat{y}_k$$
$$q_k = (1 - \alpha) \cdot \mathbb{I}(y = k) + \frac{\alpha}{K}$$
where $K$ is the number of classes and $\alpha = 0.05$.

Label smoothing prevents the logits from growing unbounded when learning conversational boundary nuances (e.g. distinguishing `VP` vs `P`, or `Agreement` vs `Commitment`).

---

## 4. Evaluation & Diagnostic Auditing Protocol

### 4.1 Quantitative Performance Metrics

1. **Macro F1 Score (Primary Target):**
   $$\text{Macro F1} = \frac{1}{K} \sum_{c=1}^{K} F1_c$$
   Target: $\ge 0.94$ on held-out test scenarios.
2. **Per-Class Precision, Recall, and F1:** Tracked individually for each class to monitor boundary degradation.
3. **Confusion Matrix ($K \times K$):** Normalized by row (recall) and column (precision).

### 4.2 Boundary Auditing

Model evaluation should be audited along **canonical confusion boundaries**. This involves closely examining the confusion matrix for specific pairs of classes that are semantically adjacent (e.g., Very Positive vs Positive, Question vs Agreement).

### 4.3 Anti-Shortcut Audit

To verify that the model did not learn trivial lexical shortcuts, the test set must evaluate:
1. **Punctuation Independence:** Can the model correctly classify utterances without relying on question marks or exclamation points?
2. **Keyword Independence:** Does the model understand context rather than relying on keywords like "okay", "sure", "no", etc.?
3. **Length Independence:** Does the model perform equally well on short and long utterances without assuming length correlates with intensity or commitment?
