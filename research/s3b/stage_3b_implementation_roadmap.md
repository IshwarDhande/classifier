# Stage 3B Implementation Roadmap — Remediation Execution Plan

**Target Document:** Stage 3B Implementation Roadmap  
**Scope:** Track 2A (`2a_boundary_anchor`), Track 2B (`2b_minimal_pair`), Track 2C (`2c_hard_negative`), and Dataset Compilation  
**Baseline Audit:** [`research/s3b/stage_3b_audit_report.md`](file:///home/eshwar/code/response/research/s3b/stage_3b_audit_report.md)  
**Governing Plans:** [`research/plan/stage_3b_construction_plan.md`](file:///home/eshwar/code/response/research/plan/stage_3b_construction_plan.md), [`research/plan/stage_3b_2a_boundary_anchor_variants.md`](file:///home/eshwar/code/response/research/plan/stage_3b_2a_boundary_anchor_variants.md), [`research/plan/stage_3b_2b_minimal_pair_variants.md`](file:///home/eshwar/code/response/research/plan/stage_3b_2b_minimal_pair_variants.md), [`research/plan/stage_3b_2c_hard_negative_variants.md`](file:///home/eshwar/code/response/research/plan/stage_3b_2c_hard_negative_variants.md)  
**Location:** [`research/s3b/stage_3b_implementation_roadmap.md`](file:///home/eshwar/code/response/research/s3b/stage_3b_implementation_roadmap.md)  

---

## 1. Executive Master Flowchart

```text
+===================================================================================================+
|                              STAGE 3B REMEDIATION & EXECUTION PIPELINE                            |
+===================================================================================================+
|                                                                                                   |
|   [ PHASE 0: Normalization, Casing & Quality Gate Tooling ]                                       |
|   • Rename all 30 files to lowercase (user rule compliance).                                      |
|   • Normalize BA01 suffix: remove redundant '_stage3b_' infix.                                    |
|   • Deploy automated remediation verification engine in code/scripts/audit_s3b.py.                |
|                                     |                                                             |
|                                     v                                                             |
|   [ PHASE 1: Track 2A (Boundary Anchors) Polish & Canonical Schema ]                             |
|   • Resolve single internal duplicate utterance (BA01-A06-V03 vs BA09-A05-V03).                   |
|   • Standardize canonical IDs (BA01-A01-V01 .. BA10-A06-V06) and explicit lineage headers.        |
|   • Run Track 2A Quality Gate (Target: 360 / 360 Certified Clean, 0 Baseline Dups).              |
|                                     |                                                             |
|                                     v                                                             |
|   [ PHASE 2: Track 2B (Minimal Pairs) Deep Remediation ]                                         |
|   • Phase 2.1: Remediate Tier-1 Adjacent Pairs (MP01 - MP04)                                      |
|                - Replace 40+ verbatim Stage-2 baseline copies in MP-V01 (LEX).                    |
|                - Equalize word-count ratios in MP01 (VP vs P) to eliminate length shortcut.      |
|                - Fix intra-pair duplicate in MP01-01 (V01 vs V05).                                |
|   • Phase 2.2: Remediate Tier-2 Non-Adjacent Pairs (MP05 - MP07)                                  |
|                - Replace verbatim Stage-2 baseline copies in MP-V01 (LEX).                        |
|                - Resolve shared I-utterances between MP02, MP03, and MP05.                         |
|                - Equalize word-count ratios in MP07 (VP vs VN).                                   |
|   • Phase 2.3: Remediate Tier-2 Non-Adjacent Pairs (MP08 - MP10)                                  |
|                - Replace verbatim Stage-2 baseline copies in MP-V01 (LEX).                        |
|                - Replace cross-file shared utterances (MP08 vs MP02, MP10 vs MP03).               |
|   • Phase 2.4: Standardize Canonical IDs (MP01-01-V01 .. MP10-06-V06) & Matched Difficulty Gate  |
|                                     |                                                             |
|                                     v                                                             |
|   [ PHASE 3: Track 2C (Hard Negatives) Baseline Copy Remediation ]                                |
|   • Phase 3.1: Replace the 15 verbatim Stage-2 copies in HN-V01 (LEX) with novel reformulations. |
|   • Phase 3.2: Verify preservation of all 6 adversarial mechanisms across all 60 families.        |
|   • Phase 3.3: Standardize canonical IDs (HN01-01-V01 .. HN10-06-V06) and explicit lineage.       |
|                                     |                                                             |
|                                     v                                                             |
|   [ PHASE 4: Directory Restructuring, Final Audit & Dataset Export ]                              |
|   • Reorganize 30 files into track subdirectories (2a_boundary_anchor, 2b_minimal_pair, etc.).    |
|   • Build code/scripts/create_s3b_csv_dataset.py and compile unified CSV with frozen splits.      |
|   • Final 100% Zero-Defect Certification across all 1,440 utterances.                             |
|                                                                                                   |
+===================================================================================================+
```

---

## 2. Granular Phase Breakdown

```text
+===================================================================================================+
|                       PHASE 0: TOOLING, CASING NORMALIZATION & DIRECTORY CLEANUP                  |
+===================================================================================================+
```

### Objective
Enforce repository-wide naming rules, eliminate filename inconsistencies, and prepare the automated test harness before modifying linguistic content.

### Tasks
1. **Filename Lowercase Normalization:**
   - User Rule: *"name the files and folder in lowercase"*.
   - Rename all 30 files in [`research/s3b`](file:///home/eshwar/code/response/research/s3b) to lowercase:
     - `BA01_VP_P_stage3b_variants.md` $\rightarrow$ `ba01_vp_p_variants.md` (also eliminating `_stage3b_` infix).
     - `BA02_P_I_variants.md` through `BA10_I_VN_variants.md` $\rightarrow$ `ba02_p_i_variants.md` .. `ba10_i_vn_variants.md`.
     - `MP01_VP_P_variants.md` through `MP10_I_VN_variants.md` $\rightarrow$ `mp01_vp_p_variants.md` .. `mp10_i_vn_variants.md`.
     - `HN01_VP_P_variants.md` through `HN10_I_VN_variants.md` $\rightarrow$ `hn01_vp_p_variants.md` .. `hn10_i_vn_variants.md`.
2. **Automated Verification Suite Update:**
   - Update [`code/scripts/audit_s3b.py`](file:///home/eshwar/code/response/code/scripts/audit_s3b.py) to validate lowercase paths and run remediation checks after each phase.

### Exit Criteria
- [ ] 0 files with uppercase letters in `research/s3b/`.
- [ ] No `_stage3b_` infix in filename `ba01_vp_p_variants.md`.
- [ ] Automated audit tool parses all 30 renamed files cleanly.

---

```text
+===================================================================================================+
|                       PHASE 1: TRACK 2A (BOUNDARY ANCHORS) HARMONIZATION                          |
+===================================================================================================+
```

### Objective
Polish the existing Track 2A corpus to eliminate its single duplicate utterance and harmonize its variant headers with canonical production identifiers and lineage.

### Tasks
1. **Remediate Duplicate Utterance:**
   - Utterance: `"okay, i’ll take the walk after dinner."` occurs in both:
     - [`ba01_vp_p_variants.md`](file:///home/eshwar/code/response/research/s3b/BA01_VP_P_stage3b_variants.md) (anchor `A06`, variant `V03` - `NAT`)
     - [`ba09_p_vn_variants.md`](file:///home/eshwar/code/response/research/s3b/BA09_P_VN_variants.md) (anchor `A05`, variant `V03` - `NAT`)
   - Action: In `ba09_p_vn_variants.md`, replace with a novel natural realization:
     `"Sure, I'll go for the walk once dinner is finished."`
2. **Harmonize Canonical Identifiers & Schema:**
   - Upgrade local `### BA-V01 — LEX` headers to globally unique canonical IDs:
     `### BA01-A01-V01 — LEX`
   - Add explicit parent lineage tag under each variant block:
     `- **Lineage:** BA01-A01 → BA01-A01-V01`
3. **Execution Gate:**
   - Run `python3 code/scripts/audit_s3b.py`.

### Exit Criteria
- [ ] 0 internal duplicate utterances across Track 2A.
- [ ] 0 verbatim Stage-2 baseline copies.
- [ ] 360 / 360 variants formatted with canonical identifiers.

---

```text
+===================================================================================================+
|                       PHASE 2: TRACK 2B (MINIMAL PAIRS) DEEP REMEDIATION                          |
+===================================================================================================+
```

### Objective
Remediate the 104 baseline copies, eliminate cross-file duplicate utterances, and neutralize word-count disparities to enforce the **Matched-Difficulty Principle**.

```text
+---------------------------------------------------------------------------------------------------+
| TRACK 2B REMEDIATION TARGET MATRIX                                                                |
|                                                                                                   |
| File     | Target Pair | Verbatim S2 Copies to Fix | Redundant Utterances to Replace | Ratio Fix   |
|----------+-------------+---------------------------+---------------------------------+-------------|
| mp01     | VP <-> P    | 5 VP baseline copies      | Intra-pair dup in MP01-01 (V05) | Word counts |
| mp02     | P <-> I     | 12 baseline copies (V01)  | Shared I-utterances with MP03   | —           |
| mp03     | I <-> N     | 12 baseline copies (V01)  | Shared I-utterances with MP02   | —           |
| mp04     | N <-> VN    | 12 baseline copies (V01)  | Cross-file N-utterances         | —           |
| mp05     | VP <-> I    | 12 baseline copies (V01)  | Shared I-utterances with MP02   | —           |
| mp06     | VP <-> N    | 12 baseline copies (V01)  | Cross-file N-utterances         | —           |
| mp07     | VP <-> VN   | 11 baseline copies (V01)  | Cross-file VN-utterances        | Word counts |
| mp08     | P <-> N     | 12 baseline copies (V01)  | Cross-file P-utterances         | —           |
| mp09     | P <-> VN    | 12 baseline copies (V01)  | Cross-file VN-utterances        | —           |
| mp10     | I <-> VN    | 12 baseline copies (V01)  | Shared I-utterances with MP03   | —           |
+---------------------------------------------------------------------------------------------------+
```

### Tasks
1. **Phase 2.1 — Tier-1 Adjacent Pairs (`mp01`–`mp04`):**
   - **`mp01_vp_p_variants.md`:**
     - Replace verbatim copies in `MP01-02-V01` through `MP01-06-V01` on the `VP` side with novel lexical reformulations.
     - Equalize word count ratios: shorten verbose VP preambles and expand P responses so word count ratios remain $< 1.5\times$.
     - Fix `MP01-01-V05 (LEN)` P side: replace duplicate `"Okay, I’ll put my medication beside my breakfast items tonight."` with concise form: `"I’ll place my medication there tonight."`
   - **`mp02_p_i_variants.md`:**
     - Replace all 6 pairs in `MP-V01 (LEX)` with genuine lexical reformulations instead of the Stage-2 parent text.
     - Replace shared `I` utterances in `MP02-01-V03`, `MP02-01-V06`, `MP02-02-V03`, `MP02-02-V05`, `MP02-02-V06`.
   - **`mp03_i_n_variants.md`:**
     - Replace all 6 pairs in `MP-V01 (LEX)` with novel lexical reformulations.
     - Replace `I` utterances shared with `mp02`.
   - **`mp04_n_vn_variants.md`:**
     - Replace all 6 pairs in `MP-V01 (LEX)` with novel lexical reformulations.
2. **Phase 2.2 — Tier-2 Pairs (`mp05`–`mp07`):**
   - **`mp05_vp_i_variants.md`:**
     - Replace all 6 pairs in `MP-V01 (LEX)`.
     - Replace `I` utterances shared with `mp02` and `mp03`.
   - **`mp06_vp_n_variants.md`:**
     - Replace all 6 pairs in `MP-V01 (LEX)`.
   - **`mp07_vp_vn_variants.md`:**
     - Replace all 6 pairs in `MP-V01 (LEX)`.
     - Equalize length ratios: curb excessive VP preambles to match VN brevity.
3. **Phase 2.3 — Tier-2 Pairs (`mp08`–`mp10`):**
   - **`mp08_p_n_variants.md`:**
     - Replace all 6 pairs in `MP-V01 (LEX)`.
     - Fix duplicate in `MP08-06-V06`: replace `"Alright, I can do the physiotherapy exercises before my evening routine."` with `"I'll get the physiotherapy exercises completed before dinner."`
   - **`mp09_p_vn_variants.md`:**
     - Replace all 6 pairs in `MP-V01 (LEX)`.
   - **`mp10_i_vn_variants.md`:**
     - Replace all 6 pairs in `MP-V01 (LEX)`.
4. **Phase 2.4 — Canonical Header & ID Standardization:**
   - Update variant subheadings to canonical IDs: `### MP01-01-V01 — LEX` through `### MP10-06-V06 — CMK`.

### Exit Criteria
- [ ] 0 verbatim Stage-2 baseline copies across all 10 MP files.
- [ ] 0 duplicate utterances across Minimal Pair files.
- [ ] Max word count ratio $\le 1.5\times$ across all pairs.
- [ ] 360 / 360 pairs fully compliant with matched difficulty.

---

```text
+===================================================================================================+
|                       PHASE 3: TRACK 2C (HARD NEGATIVES) BASELINE REMEDIATION                     |
+===================================================================================================+
```

### Objective
Eliminate the 15 isolated verbatim copies of Stage 2 baseline hard negatives in `HN-V01 (LEX)` while preserving the underlying adversarial mechanisms.

### Tasks
1. **Replace 15 Verbatim Stage-2 Baseline Copies in `HN-V01 (LEX)`:**
   - **`hn01_vp_p_variants.md`:**
     - [`HN01-06-V01`](file:///home/eshwar/code/response/research/s3b/HN01_VP_P_variants.md#L309) (`P`): Replace with novel realization:
       `"You frequently suggest ambitious routine shifts, but in this specific instance, sure, I’ll split the exercises into two sessions today."`
   - **`hn03_i_n_variants.md`:**
     - [`HN03-05-V01`](file:///home/eshwar/code/response/research/s3b/HN03_I_N_variants.md#L254) (`N`): Replace with:
       `"I realize having a routine is helpful and fitness matters to me, but I really don’t want to leave my walking shoes by the door today."`
   - **`hn05_vp_i_variants.md`:**
     - [`HN05-05-V01`](file:///home/eshwar/code/response/research/s3b/HN05_VP_I_variants.md#L254) (`I`): Replace with novel distractor phrasing.
     - [`HN05-06-V01`](file:///home/eshwar/code/response/research/s3b/HN05_VP_I_variants.md#L309) (`I`): Replace with novel distractor phrasing.
   - **`hn06_vp_n_variants.md`:**
     - [`HN06-02-V01`](file:///home/eshwar/code/response/research/s3b/HN06_VP_N_variants.md#L89) (`VP`): Replace with novel distractor phrasing.
     - [`HN06-05-V01`](file:///home/eshwar/code/response/research/s3b/HN06_VP_N_variants.md#L254) (`N`): Replace with novel distractor phrasing.
     - [`HN06-06-V01`](file:///home/eshwar/code/response/research/s3b/HN06_VP_N_variants.md#L309) (`N`): Replace with novel distractor phrasing.
   - **`hn08_p_n_variants.md`:**
     - [`HN08-04-V01`](file:///home/eshwar/code/response/research/s3b/HN08_P_N_variants.md#L199) (`N`): Replace with novel distractor phrasing.
     - [`HN08-05-V01`](file:///home/eshwar/code/response/research/s3b/HN08_P_N_variants.md#L254) (`N`): Replace with novel distractor phrasing.
   - **`hn09_p_vn_variants.md`:**
     - [`HN09-01-V01`](file:///home/eshwar/code/response/research/s3b/HN09_P_VN_variants.md#L34) (`P`): Replace with novel distractor phrasing.
     - [`HN09-02-V01`](file:///home/eshwar/code/response/research/s3b/HN09_P_VN_variants.md#L89) (`P`): Replace with novel distractor phrasing.
     - [`HN09-04-V01`](file:///home/eshwar/code/response/research/s3b/HN09_P_VN_variants.md#L199) (`VN`): Replace with novel distractor phrasing.
     - [`HN09-05-V01`](file:///home/eshwar/code/response/research/s3b/HN09_P_VN_variants.md#L254) (`VN`): Replace with novel distractor phrasing.
   - **`hn10_i_vn_variants.md`:**
     - [`HN10-01-V01`](file:///home/eshwar/code/response/research/s3b/HN10_I_VN_variants.md#L34) (`I`): Replace with novel distractor phrasing.
     - [`HN10-03-V01`](file:///home/eshwar/code/response/research/s3b/HN10_I_VN_variants.md#L144) (`I`): Replace with novel distractor phrasing.
2. **Canonical Header & ID Standardization:**
   - Update variant subheadings to canonical IDs: `### HN01-01-V01 — LEX` through `### HN10-06-V06 — CMK`.

### Exit Criteria
- [ ] 0 verbatim Stage-2 baseline copies across all 10 HN files.
- [ ] 0 internal duplicate utterances.
- [ ] All 6 hard negative mechanisms certified active and non-deterministic.

---

```text
+===================================================================================================+
|                       PHASE 4: REORGANIZATION, EXPORT & FINAL CERTIFICATION                       |
+===================================================================================================+
```

### Objective
Organize files into target track directories per plan, build the automated dataset compilation pipeline, export unified CSV/JSONL splits with zero-leakage groupings, and certify Stage 3B as complete.

### Tasks
1. **Directory Restructuring per Plan:**
   - Move files into track subdirectories under `research/s3b/`:
     ```text
     research/s3b/
     ├── 2a_boundary_anchor/
     │   ├── ba01_vp_p_variants.md
     │   └── ... (ba02 to ba10)
     ├── 2b_minimal_pair/
     │   ├── mp01_vp_p_variants.md
     │   └── ... (mp02 to mp10)
     └── 2c_hard_negative/
         ├── hn01_vp_p_variants.md
         └── ... (hn02 to hn10)
     ```
2. **Develop Unified Dataset Compilation Script:**
   - Create [`code/scripts/create_s3b_csv_dataset.py`](file:///home/eshwar/code/response/code/scripts/create_s3b_csv_dataset.py) modeled after [`code/scripts/create_s3a_csv_dataset.py`](file:///home/eshwar/code/response/code/scripts/create_s3a_csv_dataset.py).
   - Fields:
     `example_id`, `parent_id`, `lineage_id`, `boundary_id`, `track`, `response_category`, `closest_competing_category`, `variation_type`, `hard_negative_mechanism`, `task_domain`, `utterance`.
3. **Generate Production Dataset Partitions:**
   - Export 1,440 examples to `code/data/response_dataset/dataset_3b/`.
   - Partition into 70/15/15 train/val/test splits grouped strictly by Stage-2 parent family to guarantee **zero leakage**.
4. **Final Acceptance Audit:**
   - Re-run [`code/scripts/audit_s3b.py`](file:///home/eshwar/code/response/code/scripts/audit_s3b.py) to achieve 100% clean certification.

### Exit Criteria
- [ ] Complete directory structure matches [`stage_3b_construction_plan.md`](file:///home/eshwar/code/response/research/plan/stage_3b_construction_plan.md).
- [ ] 0 verbatim duplicates of baseline Stage-2 in any file.
- [ ] 0 duplicate utterances across the entire 1,440-utterance corpus.
- [ ] 100% of filenames in lowercase.
- [ ] Production CSV dataset generated and certified.

---

## 3. Implementation Schedule & Verification Matrix

```text
+===================================================================================================================+
| Phase | Action Item                            | Files Impacted | Primary Verifier Script | Target Pass Rate      |
+-------+----------------------------------------+----------------+-------------------------+-----------------------+
| P0    | Casing & Naming Normalization          | 30 files       | code/scripts/audit_s3b.py| 100% Lowercase        |
| P1    | Track 2A Polish & Canonical IDs        | 10 BA files    | code/scripts/audit_s3b.py| 0 Dups, 360 Clean     |
| P2.1  | Track 2B Tier-1 Baseline Copy Removal  | 4 MP files     | code/scripts/audit_s3b.py| 0 Baseline Copies     |
| P2.2  | Track 2B Tier-2 Baseline Copy Removal  | 3 MP files     | code/scripts/audit_s3b.py| 0 Baseline Copies     |
| P2.3  | Track 2B Tier-2 Baseline Copy Removal  | 3 MP files     | code/scripts/audit_s3b.py| 0 Baseline Copies     |
| P2.4  | Track 2B Length Ratios & Canonical IDs | 10 MP files    | code/scripts/audit_s3b.py| Length Ratio < 1.5x   |
| P3.1  | Track 2C 15 Baseline Copies Removal    | 7 HN files     | code/scripts/audit_s3b.py| 0 Baseline Copies     |
| P3.2  | Track 2C Canonical IDs & Lineage       | 10 HN files    | code/scripts/audit_s3b.py| 100% Standard Schema  |
| P4.1  | Directory Restructure (2a, 2b, 2c)     | 30 files       | Shell / Tree linter     | 3 Track Subdirs Match |
| P4.2  | Dataset Compilation (CSV & Splits)     | Export scripts | Python / Pandas Linter  | 1,440 Records Exported|
+===================================================================================================================+
```
