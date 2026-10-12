# Stage 2 Implementation Roadmap — Granular Phase Execution Plan

**Document:** Stage 2 Implementation Roadmap  
**Scope:** Stage 2A (`ba/`), Stage 2B (`mp/`), Stage 2C (`hn/`), and Dataset Compilation  
**Ontology:** Response Category Ontology V1.0 (`VP`, `P`, `I`, `N`, `VN`)  
**Domain Constraint:** 4 Closed Tasks (`Medication`, `Hydration`, `Exercise`, `Physiotherapy`)  
**Target File:** [`research/s2/stage_2_implementation_roadmap.md`](file:///home/eshwar/code/response/research/stage_2_implementation_roadmap.md)  
**Governing Plan:** [`research/s2/stage_2_four_task_construction_plan.md`](file:///home/eshwar/code/response/research/s2/stage_2_four_task_construction_plan.md)  

---

## 1. Executive Master Flowchart

```
+===================================================================================================+
|                               STAGE 2 GRANULAR EXECUTION PIPELINE                                 |
+===================================================================================================+

  [ PHASE 0: Baseline Audit & Automated Linter ]
  • Inventory 10 BA, 10 MP, and 1 HN files
  • Build code/scripts/audit_s2_suite.py (automated validation gate)
                            |
                            v
  [ PHASE 1: Stage 2A — Boundary Anchors (BA) Task Rebalancing ]
  • Phase 1.1: Tier-1 Adjacent Pairs (BA01 - BA04) Rebalance (Med, Hyd, Ex, Phys)
  • Phase 1.2: Tier-2 Non-Adjacent Pairs (BA05 - BA07) Rebalance
  • Phase 1.3: Tier-2 Non-Adjacent Pairs (BA08 - BA10) Rebalance
  • Phase 1.4: BA Suite Audit Gate (Exact 8-7-8-7 Task Balance, 60 Anchors)
                            |
                            v
  [ PHASE 2: Stage 2B — Minimal Pairs (MP) Syntax Standardization & Balancing ]
  • Phase 2.1: Tier-1 Adjacent Pairs (MP01 - MP04) Syntax & Task Parity
  • Phase 2.2: Tier-2 Non-Adjacent Pairs (MP05 - MP07) Syntax & Task Parity
  • Phase 2.3: Tier-2 Non-Adjacent Pairs (MP08 - MP10) Syntax & Task Parity
  • Phase 2.4: MP Suite Audit Gate (15-15-15-15 Task Parity, Dialogue Turn Syntax)
                            |
                            v
  [ PHASE 3: Stage 2C — Hard Negatives (HN) Complete Construction ]
  • Phase 3.1: Standardize HN01_vp_p.md to Dialogue Syntax
  • Phase 3.2: Construct Tier-1 Adjacent Files (HN02, HN03, HN04)
  • Phase 3.3: Construct Tier-2 Non-Adjacent Files (HN05, HN06, HN07)
  • Phase 3.4: Construct Tier-2 Non-Adjacent Files (HN08, HN09, HN10)
  • Phase 3.5: HN Suite Audit Gate (6 Adversarial Cue Types, 15-15-15-15 Task Parity)
                            |
                            v
  [ PHASE 4: Global Dataset Compilation & Statistical Verification ]
  • Phase 4.1: Develop code/scripts/create_s2_csv_dataset.py
  • Phase 4.2: Export code/data/response_dataset/dataset_2/ (Unified CSV + Splits)
  • Phase 4.3: Final Statistical Audit (Chi-Square Independence Test, Zero Leakage)
+===================================================================================================+
```

---

## 2. Granular Phase Breakdown

```
+===================================================================================================+
|                                    PHASE 0: PRE-REQUISITES & LINTER                               |
+===================================================================================================+
| Sub-Phase   | Target File / Action                  | Task Description                                    |
|-------------+---------------------------------------+-----------------------------------------------------|
| Phase 0.1   | research/s2/ba/, mp/, hn/             | Verify current file inventory and baseline hashes.  |
| Phase 0.2   | code/scripts/audit_s2_suite.py        | Implement automated multi-file validator checking:  |
|             |                                       | 1. Dialogue syntax ("Assistant: “...”")             |
|             |                                       | 2. Exactly 6 anchors/pairs per file                 |
|             |                                       | 3. Task assignment (Med/Hyd/Ex/Phys) counts         |
|             |                                       | 4. Zero duplicate user utterances across all files  |
+===================================================================================================+
```

---

```
+===================================================================================================+
|                               PHASE 1: STAGE 2A — BOUNDARY ANCHORS (BA)                           |
+===================================================================================================+
| Sub-Phase   | Target Files                          | Detailed Granular Actions                           |
|-------------+---------------------------------------+-----------------------------------------------------|
| Phase 1.1   | BA01_vp_p.md                          | • Rebalance Context 2 to Hydration (desk bottle).   |
|             | BA02_p_i.md                           | • Ensure Context 1 is Medication, Context 3 is Ex.  |
|             | BA03_i_n.md                           | • Check leaning anchors (A03/A04) maintain razor-   |
|             | BA04_n_vn.md                          |   sharp boundary distinction.                       |
|             |                                       | • Verify all 4 files adhere to Level 2 headers.     |
|-------------+---------------------------------------+-----------------------------------------------------|
| Phase 1.2   | BA05_vp_i.md                          | • Apply Latin-Square task mapping:                  |
|             | BA06_vp_n.md                          |   - BA05: Med (C1), Hyd (C2), Ex (C3)               |
|             | BA07_vp_vn.md                         |   - BA06: Phys (C1), Med (C2), Hyd (C3)             |
|             |                                       |   - BA07: Ex (C1), Phys (C2), Med (C3)              |
|             |                                       | • Verify non-adjacent pairs avoid lexical polarity. |
|-------------+---------------------------------------+-----------------------------------------------------|
| Phase 1.3   | BA08_p_n.md                           | • Apply Latin-Square task mapping:                  |
|             | BA09_p_vn.md                          |   - BA08: Hyd (C1), Ex (C2), Phys (C3)              |
|             | BA10_i_vn.md                          |   - BA09: Med (C1), Hyd (C2), Ex (C3)               |
|             |                                       |   - BA10: Phys (C1), Med (C2), Hyd (C3)             |
|             |                                       | • Standardize punctuation and curly quotes.         |
|-------------+---------------------------------------+-----------------------------------------------------|
| Phase 1.4   | Quality Gate Verification             | • Run `python3 code/scripts/audit_s2_suite.py --ba` |
|             |                                       | • Assert: Exactly 60 anchors, 12 per class,         |
|             |                                       |   Med=8, Hyd=7, Ex=8, Phys=7. Zero duplicates.      |
+===================================================================================================+
```

---

```
+===================================================================================================+
|                               PHASE 2: STAGE 2B — MINIMAL PAIRS (MP)                              |
+===================================================================================================+
| Sub-Phase   | Target Files                          | Detailed Granular Actions                           |
|-------------+---------------------------------------+-----------------------------------------------------|
| Phase 2.1   | MP01_vp_p.md                          | • Migrate MP02, MP03, MP04 from narrative context   |
|             | MP02_p_i.md                           |   to dialogue turns (`Assistant: “...”`).           |
|             | MP03_i_n.md                           | • Restructure pairs 01-06 to strictly cover:        |
|             | MP04_n_vn.md                          |   P01: Med, P02: Hyd, P03: Ex, P04: Phys,           |
|             |                                       |   P05: Med/Ex, P06: Hyd/Phys.                       |
|             |                                       | • Keep underlying context identical within pair.    |
|-------------+---------------------------------------+-----------------------------------------------------|
| Phase 2.2   | MP05_vp_i.md                          | • Migrate context syntax to dialogue turns.         |
|             | MP06_vp_n.md                          | • Re-assign pairs to exact 4-task distribution.     |
|             | MP07_vp_vn.md                         | • Ensure gold labels table matches at bottom.       |
|-------------+---------------------------------------+-----------------------------------------------------|
| Phase 2.3   | MP08_p_n.md                           | • Migrate context syntax to dialogue turns.         |
|             | MP09_p_vn.md                          | • Re-assign pairs to exact 4-task distribution.     |
|             | MP10_i_vn.md                          | • Eliminate repetitive verb templates.              |
|-------------+---------------------------------------+-----------------------------------------------------|
| Phase 2.4   | Quality Gate Verification             | • Run `python3 code/scripts/audit_s2_suite.py --mp` |
|             |                                       | • Assert: Exactly 60 pairs (120 turns).             |
|             |                                       |   Med=15, Hyd=15, Ex=15, Phys=15. Zero duplicates.  |
+===================================================================================================+
```

---

```
+===================================================================================================+
|                               PHASE 3: STAGE 2C — HARD NEGATIVES (HN)                             |
+===================================================================================================+
| Sub-Phase   | Target Files                          | Detailed Granular Actions                           |
|-------------+---------------------------------------+-----------------------------------------------------|
| Phase 3.1   | HN01_vp_p.md                          | • Convert narrative context to dialogue turn syntax.|
|             |                                       | • Verify the 6 adversarial cue patterns.            |
|-------------+---------------------------------------+-----------------------------------------------------|
| Phase 3.2   | HN02_p_i.md                           | • Generate HN02, HN03, HN04 following standard      |
|             | HN03_i_n.md                           |   adversarial patterns (competing word, self-       |
|             | HN04_n_vn.md                          |   correction, misleading clause, pragmatic shift).  |
|             |                                       | • Distribute across Med, Hyd, Ex, Phys.             |
|-------------+---------------------------------------+-----------------------------------------------------|
| Phase 3.3   | HN05_vp_i.md                          | • Construct Tier-2 non-adjacent hard negatives.     |
|             | HN06_vp_n.md                          | • Pair adversarial distractions with true ground    |
|             | HN07_vp_vn.md                         |   truth behavioral engagement level.                |
|-------------+---------------------------------------+-----------------------------------------------------|
| Phase 3.4   | HN08_p_n.md                           | • Construct remaining Tier-2 hard negatives.        |
|             | HN09_p_vn.md                          | • Validate that surface politeness does not mask    |
|             | HN10_i_vn.md                          |   negative resistance.                              |
|-------------+---------------------------------------+-----------------------------------------------------|
| Phase 3.5   | Quality Gate Verification             | • Run `python3 code/scripts/audit_s2_suite.py --hn` |
|             |                                       | • Assert: 10 files, 60 pairs, 15 per task.          |
|             |                                       |   Zero lexical overlap with BA or MP files.         |
+===================================================================================================+
```

---

```
+===================================================================================================+
|                          PHASE 4: GLOBAL COMPILATION & STATISTICAL AUDIT                          |
+===================================================================================================+
| Sub-Phase   | Target File / Output                  | Detailed Granular Actions                           |
|-------------+---------------------------------------+-----------------------------------------------------|
| Phase 4.1   | code/scripts/create_s2_csv_dataset.py | • Build deterministic CSV compiler for Stage 2.     |
|             |                                       | • Extract BA (60), MP (120), HN (60) = 240 rows.    |
|             |                                       | • Assign standard schema:                           |
|             |                                       |   [utterance_id, utterance, label, category_no,     |
|             |                                       |    task_domain, resource_type, boundary_id, ...]   |
|-------------+---------------------------------------+-----------------------------------------------------|
| Phase 4.2   | code/data/response_dataset/dataset_2/ | • Export:                                           |
|             |                                       |   - stage_2_dataset.csv (240 rows)                  |
|             |                                       |   - stage_2_ba.csv (60 rows)                        |
|             |                                       |   - stage_2_mp.csv (120 rows)                       |
|             |                                       |   - stage_2_hn.csv (60 rows)                        |
|-------------+---------------------------------------+-----------------------------------------------------|
| Phase 4.3   | Statistical Audit & Sign-off          | • Compute Task x Category Contingency Matrix.       |
|             |                                       | • Verify Mutual Information I(Task; Label) < 0.02.  |
|             |                                       | • Ensure 0% data leakage and 100% schema alignment. |
+===================================================================================================+
```

---

## 3. Quantitative Deliverables Summary

```
+===================================================================================================+
|                                    STAGE 2 CORPUS DELIVERABLES                                    |
+===================================================================================================+
| Component      | Files    | Examples / Turns  | Class Balance (VP / P / I / N / VN) | Task Parity |
|----------------+----------+-------------------+-------------------------------------+-------------|
| Stage 2A (BA)  | 10 files | 60 anchors        | Exactly 12 per class (Balanced)     | 8 / 7 / 8 / 7|
| Stage 2B (MP)  | 10 files | 120 turns         | Exactly 24 per class (Balanced)     | 15 each     |
| Stage 2C (HN)  | 10 files | 60 examples       | Exactly 12 per class (Balanced)     | 15 each     |
|----------------+----------+-------------------+-------------------------------------+-------------|
| TOTAL STAGE 2  | 30 files | 240 examples      | Exactly 48 per class (100% Balanced)| 60 each     |
+===================================================================================================+
```

---

### Reference Links
- Construction Plan: [`research/s2/stage_2_four_task_construction_plan.md`](file:///home/eshwar/code/response/research/s2/stage_2_four_task_construction_plan.md)
- Boundary Anchors Directory: [`research/s2/ba/`](file:///home/eshwar/code/response/research/s2/ba/)
- Minimal Pairs Directory: [`research/s2/mp/`](file:///home/eshwar/code/response/research/s2/mp/)
- Hard Negatives Directory: [`research/s2/hn/`](file:///home/eshwar/code/response/research/s2/hn/)
- Audit Script: [`code/scripts/audit_s2_ba.py`](file:///home/eshwar/code/response/code/scripts/audit_s2_ba.py)
