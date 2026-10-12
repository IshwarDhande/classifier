# Dataset Splitting & Classifier Training Methodology

**Document:** `dialogue_purpose_methodology.md`  
**Ontology:** Dialogue Purpose V1.0 (Frozen 5-Class: `Question`, `Information`, `Agreement`, `Commitment`, `Refusal`)  
**Corpus Size:** 900 Examples (300 Stage-1 Anchors + 600 Stage-3 Linguistic Variants across 100 General Scenarios)  
**Partition Scheme:** 70% Train (630) / 15% Validation (135) / 15% Test (135)

---

## 1. Executive Summary

This document formalizes the splitting protocol and model training methodology for the single-label five-class Dialogue Purpose classifier.

The primary challenge in conversational dialogue intent classification is preventing the model from exploiting **surface-level shortcuts** (e.g., matching topic words, relying on question marks, or memorizing scenario semantics). To ensure the classifier learns true **communicative purpose**, we enforce **Leakage-Safe Stratified Group Splitting** at the `scenario_id` level.

```
+--------------------------------------------------------------------------------------------------+
|                                    SPLITTING & TRAINING FLOW                                     |
+--------------------------------------------------------------------------------------------------+
|                                                                                                  |
|   100 Scenarios (20 per Purpose Class) × 9 Realizations = 900 Examples                          |
|                                                                                                  |
|                                       │                                                          |
|                                       ▼                                                          |
|                    [STRATIFIED SCENARIO-LEVEL GROUP SPLIT]                                       |
|                    • All 9 variants of a scenario stay together                                  |
|                    • Zero semantic leakage between splits                                        |
|                    • Stratified across all 20 semantic subtypes                                  |
|                                                                                                  |
|              ┌────────────────────────┼────────────────────────┐                                 |
|              ▼                        ▼                        ▼                                 |
|      [TRAIN SET (70%)]        [VAL SET (15%)]          [TEST SET (15%)]                          |
|      70 Scenarios             15 Scenarios             15 Scenarios                              |
|      630 Examples             135 Examples             135 Examples                              |
|      (126 / class)            (27 / class)             (27 / class)                              |
|              │                        │                        │                                 |
|              ▼                        ▼                        │                                 |
|   ┌──────────────────────┐  ┌───────────────────┐              │                                 |
|   │ Transformer Training │  │ Model Selection & │              │                                 |
|   │ (DeBERTa-v3 / BERT)  │─►│ Early Stopping    │              │                                 |
|   └──────────────────────┘  └───────────────────┘              │                                 |
|                                       │                        ▼                                 |
|                                       └──────────────►┌───────────────────┐                      |
|                                                       │ Final Evaluation  │                      |
|                                                       │ 10 Boundary Audits│                      |
|                                                       └───────────────────┘                      |
+--------------------------------------------------------------------------------------------------+
```

---

## 2. Dataset Splitting Methodology

### 2.1 The Semantic Leakage Hazard (Why Random Splitting Fails)

In our dataset construction framework, each approved semantic scenario generates 9 realizations:
- **3 Stage-1 core anchors:** Direct, Indirect, Natural
- **6 Stage-3 linguistic variations:** V1 (Lexical), V2 (Syntactic), V3 (Conversational), V4 (Explicit/Implicit), V5 (Length/Lexical), V6 (Conversational/Implicit)

All 9 realizations share the **exact same underlying communicative scenario** (e.g., `Q-ER-01: Recommendation Rationale`).

```
+--------------------------------------------------------------------------------------------------+
|                             THE SEMANTIC LEAKAGE PROBLEM                                         |
+--------------------------------------------------------------------------------------------------+
|                                                                                                  |
|   NAIVE RANDOM SPLIT (FATAL):                                                                    |
|   [Scenario Q-ER-01]                                                                             |
|   ├── Train : "Why are you recommending this?" (Direct)                                          |
|   ├── Train : "What is the reason you recommend this?" (V1)                                      |
|   └── Test  : "Why do you think I should do this?" (Natural) <── SEMANTIC LEAKAGE!               |
|                                                                                                  |
|   Result: The model memorizes the recommendation context and achieves 99% test accuracy,         |
|   but collapses when deployed on novel conversational situations in real dialogue.               |
|                                                                                                  |
|   --------------------------------------------------------------------------------------------   |
|                                                                                                  |
|   LEAKAGE-SAFE SCENARIO GROUP SPLIT (OUR METHOD):                                                |
|   [Scenario Q-ER-01] ──► ALL 9 REALIZATIONS ASSIGNED TO TRAIN                                    |
|   [Scenario Q-ER-04] ──► ALL 9 REALIZATIONS ASSIGNED TO VALIDATION                               |
|   [Scenario Q-ER-05] ──► ALL 9 REALIZATIONS ASSIGNED TO TEST                                     |
|                                                                                                  |
|   Result: The model is forced to generalize the abstract communicative function to               |
|   completely unseen semantic scenarios during validation and testing.                            |
|                                                                                                  |
+--------------------------------------------------------------------------------------------------+
```

### 2.2 Stratified Group Partitioning Algorithm

To guarantee zero data leakage while preserving class balance and subtype coverage:
1. **Grouping Unit:** The grouping key is `scenario_id`. No scenario crosses split boundaries.
2. **Class Balance:** Exactly 14 scenarios per class are assigned to Train, 3 to Validation, and 3 to Test.
3. **Subtype Stratification:** Each class has 4 semantic subtypes with 5 scenarios each. Scenarios within each subtype are allocated deterministically to ensure that **every semantic subtype is exposed during training**, while Validation and Test evaluate novel scenarios within those subtypes.

```
+--------------------------------------------------------------------------------------------------+
|                             SUBTYPE ALLOCATION MATRIX (PER CLASS)                                |
+--------------------------------------------------------------------------------------------------+
|   Subtype Index   | Scenario IDs     | Train Scenarios (70%)  | Val (15%)  | Test (15%)          |
+-------------------+------------------+------------------------+------------+---------------------+
|   Subtype 1 (ER)  | 01, 02, 03, 04, 05| 01, 02, 03 (3)        | 04 (1)     | 05 (1)              |
|   Subtype 2 (PH)  | 01, 02, 03, 04, 05| 01, 02, 03, 04 (4)    | 05 (1)     | — (0)               |
|   Subtype 3 (TC)  | 01, 02, 03, 04, 05| 01, 02, 03, 04 (4)    | — (0)      | 05 (1)              |
|   Subtype 4 (CS)  | 01, 02, 03, 04, 05| 01, 02, 03 (3)        | 04 (1)     | 05 (1)              |
+-------------------+------------------+------------------------+------------+---------------------+
|   TOTAL PER CLASS | 20 Scenarios     | 14 Scenarios (70%)     | 3 Scenarios| 3 Scenarios (15%)   |
+-------------------+------------------+------------------------+------------+---------------------+
```

### 2.3 Exact Scenario-to-Split Mapping (All 100 Scenarios)

```
+---------------+---------------------+-----------------------------+------------------------------+
| Dialogue Class| Train Scenarios (14)| Validation Scenarios (3)    | Test Scenarios (3)           |
+---------------+---------------------+-----------------------------+------------------------------+
| Question      | Q-ER-01, 02, 03     | Q-ER-04 (Purpose of Instr.) | Q-ER-05 (Reason Continued)   |
|               | Q-PH-01, 02, 03, 04 | Q-PH-05 (Correct Execution) | Q-TC-05 (Timing Missed Opp.) |
|               | Q-TC-01, 02, 03, 04 | Q-CS-04 (Feasibility)       | Q-CS-05 (Exception / Case)   |
|               | Q-CS-01, 02, 03     |                             |                              |
+---------------+---------------------+-----------------------------+------------------------------+
| Information   | I-CS-01, 02, 03     | I-CS-04 (Immediate Circum.) | I-CS-05 (Change Circumst.)   |
|               | I-CA-01, 02, 03, 04 | I-CA-05 (Temp Constraint)   | I-EH-05 (Relevant History)   |
|               | I-EH-01, 02, 03, 04 | I-PC-04 (Environ Context)   | I-PC-05 (Relevant Fact)      |
|               | I-PC-01, 02, 03     |                             |                              |
+---------------+---------------------+-----------------------------+------------------------------+
| Agreement     | A-DA-01, 02, 03     | A-DA-04 (Accept Approach)   | A-DA-05 (Accept No Qualif.)  |
|               | A-AA-01, 02, 03, 04 | A-AA-05 (Ack as Accept)     | A-CA-05 (Tentative Accept)   |
|               | A-CA-01, 02, 03, 04 | A-AR-04 (Need Assessment)   | A-AR-05 (Convers Conclusion) |
|               | A-AR-01, 02, 03     |                             |                              |
+---------------+---------------------+-----------------------------+------------------------------+
| Commitment    | C-II-01, 02, 03     | C-II-04 (Resume Action)     | C-II-05 (Follow-through Now) |
|               | C-SF-01, 02, 03, 04 | C-SF-05 (Delayed Intention) | C-CI-05 (Contingent Follow)  |
|               | C-CI-01, 02, 03, 04 | C-PF-04 (Follow Strategy)   | C-PF-05 (Sustained Plan)     |
|               | C-PF-01, 02, 03     |                             |                              |
+---------------+---------------------+-----------------------------+------------------------------+
| Refusal       | R-DR-01, 02, 03     | R-DR-04 (Reject Approach)   | R-DR-05 (Clear Non-Accept)   |
|               | R-IP-01, 02, 03, 04 | R-IP-05 (Non-Participation) | R-PS-05 (Final Refusal)      |
|               | R-PS-01, 02, 03, 04 | R-CD-04 (Situational Decl.) | R-CD-05 (Temp Non-Accept)    |
|               | R-CD-01, 02, 03     |                             |                              |
+---------------+---------------------+-----------------------------+------------------------------+
```

### 2.4 Quantitative Verification Metrics

```
+--------------------+-----------+-----------+----------+---------------+
| Split              | Scenarios | Seeds (1) | Vars (3) | Total Records |
+--------------------+-----------+-----------+----------+---------------+
| Train (70.0%)      | 70        | 210       | 420      | 630 (100.0%)  |
| Validation (15.0%) | 15        | 45        | 90       | 135 (100.0%)  |
| Test (15.0%)       | 15        | 45        | 90       | 135 (100.0%)  |
+--------------------+-----------+-----------+----------+---------------+
| TOTAL              | 100       | 300       | 600      | 900 (100.0%)  |
+--------------------+-----------+-----------+----------+---------------+
```

Each split is **strictly balanced across all five classes**:
- **Train:** 126 Question, 126 Information, 126 Agreement, 126 Commitment, 126 Refusal
- **Val:** 27 Question, 27 Information, 27 Agreement, 27 Commitment, 27 Refusal
- **Test:** 27 Question, 27 Information, 27 Agreement, 27 Commitment, 27 Refusal

---

## 3. Classifier Training Methodology & Architecture Plan

### 3.1 Task Formulation

The model solves a single-sentence classification task:
$$\hat{y} = \arg\max_{c \in \{0, 1, 2, 3, 4\}} P(y = c \mid x)$$

Where:
- $x$: The user's conversational utterance (string).
- $y$: Dialogue Purpose ground-truth label ($0 = \text{Question}$, $1 = \text{Information}$, $2 = \text{Agreement}$, $3 = \text{Commitment}$, $4 = \text{Refusal}$).

### 3.2 Candidate Model Architectures

```
+--------------------------------------------------------------------------------------------------+
|                                    MODEL ARCHITECTURE SELECTION                                  |
+--------------------------------------------------------------------------------------------------+
|                                                                                                  |
|   [OPTION 1: DeBERTa-v3-base / small] (PRIMARY RECOMMENDATION)                                    |
|   • Disentangled attention captures syntax and semantic roles cleanly.                           |
|   • Ideal for short, pragmatic utterances where subtle syntactic shifts flip classes.            |
|   • Parameter size: 86M (small) to 142M (base) -> fast inference (< 10ms latency).              |
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

```
+------------------------------+-------------------------------------------------------------------+
| Hyperparameter               | Recommended Setting                                               |
+------------------------------+-------------------------------------------------------------------+
| Base Model                   | microsoft/deberta-v3-base (or answerdotai/ModernBERT-base)       |
| Max Sequence Length          | 128 tokens (covers 100% of corpus without truncation)             |
| Batch Size                   | 16 (or 32 with gradient accumulation = 2)                         |
| Learning Rate                | 2e-5 (with AdamW optimizer, betas=(0.9, 0.999), eps=1e-8)         |
| LR Scheduler                 | Linear Warmup (10% of total steps) + Cosine Decay                |
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
where $K = 5$ classes and $\alpha = 0.05$.

Label smoothing prevents the logits from growing unbounded when learning conversational boundary nuances (e.g. distinguishing `Agreement` vs `Commitment`).

---

## 4. Evaluation & Diagnostic Auditing Protocol

### 4.1 Quantitative Performance Metrics

1. **Macro F1 Score (Primary Target):**
   $$\text{Macro F1} = \frac{1}{5} \sum_{c=1}^{5} F1_c$$
   Target: $\ge 0.94$ on held-out test scenarios.
2. **Per-Class Precision, Recall, and F1:** Tracked individually for each class to monitor boundary degradation.
3. **Confusion Matrix ($5 \times 5$):** Normalized by row (recall) and column (precision).

### 4.2 The 10 Pairwise Boundary Audits

The model evaluation is audited along the **10 canonical confusion boundaries**:

```
                  10 CANONICAL PAIRWISE BOUNDARIES
             ┌───────────┐
             │ Question  │◄────────────┐
             └─┬───┬───┬─┘             │
       ┌───────┘   │   └──────┐        │
       ▼           ▼          ▼        │
┌─────────────┐┌───────────┐┌───────┐  │
│ Information ││ Agreement ││Refusal│  │
└──────┬──────┘└─────┬─────┘└───┬───┘  │
       │             ▼          │      │
       └───────►┌──────────┐◄───┘      │
                │Commitment│───────────┘
                └──────────┘
```

| Boundary Index | Pairwise Confusion | Crucial Diagnostic Test |
| :---: | :--- | :--- |
| **B01** | `Question` ↔ `Information` | Distinguish rhetorical inquiry from descriptive context |
| **B02** | `Question` ↔ `Agreement` | Distinguish confirmatory questions from genuine agreement |
| **B03** | `Question` ↔ `Commitment` | Distinguish procedural queries from action commitments |
| **B04** | `Question` ↔ `Refusal` | Distinguish skeptical inquiry from actual rejection |
| **B05** | `Information` ↔ `Agreement` | Distinguish agreeing to a premise from stating a personal fact |
| **B06** | `Information` ↔ `Commitment` | Distinguish reporting a schedule from committing to act |
| **B07** | `Information` ↔ `Refusal` | Distinguish describing an obstacle from declaring refusal |
| **B08** | `Agreement` ↔ `Commitment` | Distinguish accepting a recommendation from intending to act |
| **B09** | `Agreement` ↔ `Refusal` | Distinguish qualified agreement from polite decline |
| **B10** | `Commitment` ↔ `Refusal` | Distinguish deferred commitment from temporary refusal |

### 4.3 Anti-Shortcut Audit

To verify that the model did not learn trivial lexical shortcuts, the test set evaluates:
1. **Punctuation Independence:** Utterances without `?` that are questions (e.g., `"Could you tell me what to do"`), and utterances with `?` that are agreement (e.g., `"Why not, sounds good?"`).
2. **Keyword Independence:** Utterances containing `"okay"` or `"sure"` that are `Commitment` rather than `Agreement`.
3. **Negative Form Independence:** Utterances containing `"no"` that are `Agreement` (e.g., `"No problem, I can do that."`).

---

## 5. Artifact Manifest

The following datasets and code artifacts have been produced:

```
code/
├── scripts/
│   ├── build_dataset.py       # Extracts 900 records from research/data/ markdown files
│   ├── create_core_dataset.py # Produces 3-column core dataset
│   └── split_dataset.py       # Deterministic leakage-free stratified group splitting
└── data/
    ├── dialogue_purpose_dataset.csv            # 900 rows (full metadata)
    ├── dialogue_purpose_dataset_core.csv       # 900 rows (utterance_id, utterance, label)
    ├── dialogue_purpose_dataset_with_split.csv # 900 rows (with 'split' column)
    ├── train.csv                               # 630 rows (70% - full metadata)
    ├── val.csv                                 # 135 rows (15% - full metadata)
    ├── test.csv                                # 135 rows (15% - full metadata)
    ├── train_core.csv                          # 630 rows (3-column)
    ├── val_core.csv                            # 135 rows (3-column)
    └── test_core.csv                           # 135 rows (3-column)
```
