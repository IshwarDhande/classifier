# Stage 3B — Comprehensive Corpus Audit Report (Full Corpus)

**Audit Target Directory:** [`/home/eshwar/code/response/research/s3b`](file:///home/eshwar/code/response/research/s3b)  
**Baseline & Reference Plans:** [`research/plan`](file:///home/eshwar/code/response/research/plan), [`research/s2`](file:///home/eshwar/code/response/research/s2)  
**Audit Automation Tool:** [`code/scripts/audit_s3b.py`](file:///home/eshwar/code/response/code/scripts/audit_s3b.py)  
**Corpus Audit Status:** Full 30-File Corpus Analyzed — 100% Quantitative Generation Reached (1,440 / 1,440 Utterances)  

---

## 1. Executive Summary & Full-Corpus Architecture

Stage 3B expands the boundary-focused evaluation and training resources created in Stage 2 without weakening their diagnostic properties. According to [`stage_3b_construction_plan.md`](file:///home/eshwar/code/response/research/plan/stage_3b_construction_plan.md), Stage 3B comprises three independent tracks:

```text
+===================================================================================================+
|                               STAGE 3B FULL-CORPUS PRODUCTION ARCHITECTURE                        |
+===================================================================================================+
|                                                                                                   |
|   STAGE 2 PARENT CORPUS (Frozen)                STAGE 3B EXPANSION TRACKS        FINAL CORPUS     |
|                                                                                                   |
|   +-----------------------------+           +------------------------------+   +---------------+  |
|   | 2A: 60 Boundary Anchors     | --------> | 3B-2A: Boundary Preservation |-> | 360 Variants  |  |
|   | (10 boundaries x 6 anchors) |           | (6 variants x 60 anchors)    |   | [100% DONE]   |  |
|   +-----------------------------+           +------------------------------+   +---------------+  |
|                                                                                                   |
|   +-----------------------------+           +------------------------------+   +---------------+  |
|   | 2B: 60 Minimal Pairs        | --------> | 3B-2B: Contrast Preservation |-> | 720 Utterances|  |
|   | (10 boundaries x 6 pairs)   |           | (6 paired vars x 60 pairs)   |   | [100% DONE]   |  |
|   +-----------------------------+           +------------------------------+   +---------------+  |
|                                                                                                   |
|   +-----------------------------+           +------------------------------+   +---------------+  |
|   | 2C: 60 Hard Negatives       | --------> | 3B-2C: Distractor Expansion  |-> | 360 Variants  |  |
|   | (10 boundaries x 6 examples)|           | (6 variants x 60 examples)   |   | [100% DONE]   |  |
|   +-----------------------------+           +------------------------------+   +---------------+  |
|                                                                                                   |
|   TOTAL PRODUCTION VOLUME: 1,440 / 1,440 Utterances Generated Across 30 Files (100% Coverage)     |
+===================================================================================================+
```

---

## 2. Master 30-File Audit Scorecard (All 10 Boundaries × 3 Tracks)

```text
+===================================================================================================================+
| Boundary ID | Pair      | Tier   | Track 2A (Anchors)  | Track 2B (Minimal Pairs) | Track 2C (Hard Negatives)     |
+-------------+-----------+--------+---------------------+--------------------------+-------------------------------+
| B01         | VP <-> P  | Tier 1 | 36 / 36 (PASS)      | 36 pairs / 72 utts (PASS)| 36 / 36 (WARN - 1 S2 copy)    |
| B02         | P <-> I   | Tier 1 | 36 / 36 (PASS)      | 36 pairs / 72 utts (WARN)| 36 / 36 (PASS)                |
| B03         | I <-> N   | Tier 1 | 36 / 36 (PASS)      | 36 pairs / 72 utts (WARN)| 36 / 36 (WARN - 1 S2 copy)    |
| B04         | N <-> VN  | Tier 1 | 36 / 36 (PASS)      | 36 pairs / 72 utts (WARN)| 36 / 36 (PASS)                |
| B05         | VP <-> I  | Tier 2 | 36 / 36 (PASS)      | 36 pairs / 72 utts (WARN)| 36 / 36 (WARN - 2 S2 copies)  |
| B06         | VP <-> N  | Tier 2 | 36 / 36 (PASS)      | 36 pairs / 72 utts (WARN)| 36 / 36 (WARN - 3 S2 copies)  |
| B07         | VP <-> VN | Tier 2 | 36 / 36 (PASS)      | 36 pairs / 72 utts (WARN)| 36 / 36 (PASS)                |
| B08         | P <-> N   | Tier 2 | 36 / 36 (PASS)      | 36 pairs / 72 utts (WARN)| 36 / 36 (WARN - 2 S2 copies)  |
| B09         | P <-> VN  | Tier 2 | 36 / 36 (PASS)      | 36 pairs / 72 utts (WARN)| 36 / 36 (WARN - 4 S2 copies)  |
| B10         | I <-> VN  | Tier 2 | 36 / 36 (PASS)      | 36 pairs / 72 utts (WARN)| 36 / 36 (WARN - 2 S2 copies)  |
+===================================================================================================================+
| TOTALS                  | 30 F   | 360 / 360 (100%)    | 360 / 360 pairs (100%)   | 360 / 360 (100%)              |
+===================================================================================================================+
| UTTERANCES GENERATED    |        | 360 Utterances      | 720 Utterances           | 360 Utterances                |
| GRAND TOTAL             |        | 1,440 / 1,440 Utterances Generated (100% Target Volume Reached)                |
+===================================================================================================================+
```

---

## 3. Detailed Track-by-Track Audit Findings

### A. Track 2A (Boundary Anchors) — **CERTIFIED HIGH QUALITY (PASS)**
- **Coverage:** 10 / 10 files present ([`BA01`](file:///home/eshwar/code/response/research/s3b/BA01_VP_P_stage3b_variants.md) to [`BA10`](file:///home/eshwar/code/response/research/s3b/BA10_I_VN_variants.md)). Exactly 360 variants generated.
- **Anchor Roles & Labels:** Every anchor faithfully preserves its role and label from [`research/s2/ba`](file:///home/eshwar/code/response/research/s2/ba):
  - `A01` (Proto A) & `A02` (Proto B)
  - `A03` (Leaning A) & `A04` (Leaning B)
  - `A05` (Implicit A) & `A06` (Implicit B)
  - Zero label mismatches (100% label fidelity).
- **Variant Sequence Conformance:** Every anchor block strictly implements the standard 6-variant sequence from [`stage_3b_2a_boundary_anchor_variants.md#L37-L49`](file:///home/eshwar/code/response/research/plan/stage_3b_2a_boundary_anchor_variants.md#L37-L49):
  `BA-V01 LEX` → `BA-V02 SYN` → `BA-V03 NAT` → `BA-V04 EXP` → `BA-V05 PRG` → `BA-V06 CMK`.
- **Zero Baseline Duplicates:** **0 / 360** variants duplicate baseline Stage 2 anchors verbatim (100% novel linguistic realizations).
- **Internal Duplication:** Only 1 cross-anchor duplicate utterance exists across all 360 variants:
  - *"okay, i’ll take the walk after dinner."* in `BA01-A06-V03` and `BA09-A05-V03`.

---

### B. Track 2B (Minimal Pairs) — **CRITICAL DEFECTS IDENTIFIED**
All 10 files ([`MP01`](file:///home/eshwar/code/response/research/s3b/MP01_VP_P_variants.md) through [`MP10`](file:///home/eshwar/code/response/research/s3b/MP10_I_VN_variants.md)) are now generated (360 pairs, 720 utterances). However, three critical quality defects require systematic remediation:

1. **Critical Defect 1 — Systematic Verbatim Copying of Stage 2 Baseline in `MP-V01 (LEX)`:**
   - In 9 out of 10 files, the `MP-V01 (LEX)` variant copied the Stage 2 baseline pair word-for-word rather than generating a novel lexical reformulation.
   - **104 pairs (108 utterances)** in Track 2B are 100% verbatim duplicates of [`research/s2/mp`](file:///home/eshwar/code/response/research/s2/mp).
   - This directly violates the core expansion principle of [`stage_3b_2b_minimal_pair_variants.md`](file:///home/eshwar/code/response/research/plan/stage_3b_2b_minimal_pair_variants.md), which requires genuine linguistic expansion beyond the baseline parent.
2. **Critical Defect 2 — High Utterance Redundancy Across Files (72 duplicate occurrences):**
   - Identical `I` utterances shared across multiple files:
     - *"i could keep my medication by my toothbrush."* (shared across `MP02-01-V03`, `MP03-01-V03`, `MP05-01-V03`)
     - *"okay, that’s one place i could keep my medication."* (shared across `MP02-01-V06`, `MP03-01-V06`, `MP05-01-V06`)
     - *"i could take the walk after lunch."* (shared across `MP02-02-V03`, `MP03-02-V03`)
     - *"i could walk after lunch."* (shared across `MP02-02-V05`, `MP03-02-V05`)
     - *"alright, after lunch is one possibility."* (shared across `MP02-02-V06`, `MP03-02-V06`)
   - Intra-pair duplicate in `MP01-01`: `MP-V01` and `MP-V05` share the identical P utterance (*"okay, i’ll put my medication beside my breakfast items tonight."*).
3. **Critical Defect 3 — Matched-Difficulty Length Asymmetry:**
   - [`stage_3b_2b_minimal_pair_variants.md#L65-L75`](file:///home/eshwar/code/response/research/plan/stage_3b_2b_minimal_pair_variants.md#L65-L75) mandates comparable complexity and forbids making one side substantially longer or emotional.
   - In `MP01` (`VP ↔ P`) and `MP07` (`VP ↔ VN`), 27 pairs have length ratios $\ge 2.0\times$. VP variants average 18–22 words (incorporating elaborate praise/preambles), while P variants average 8–10 words (plain compliance). This creates a serious risk of a token-length shortcut.

---

### C. Track 2C (Hard Negatives) — **STRONG STRUCTURE WITH ISOLATED DEFECTS**
All 10 files ([`HN01`](file:///home/eshwar/code/response/research/s3b/HN01_VP_P_variants.md) through [`HN10`](file:///home/eshwar/code/response/research/s3b/HN10_I_VN_variants.md)) are now generated (60 examples × 6 variants = 360 variants).
- **Hard-Negative Mechanism Preservation:** All 6 mechanisms from [`stage_3b_2c_hard_negative_variants.md#L27-L44`](file:///home/eshwar/code/response/research/plan/stage_3b_2c_hard_negative_variants.md#L27-L44) are systematically preserved:
  - `01`: Competing Keyword
  - `02`: Competing Phrase
  - `03`: Misleading Opening Clause
  - `04`: Mid-Sentence Self-Correction
  - `05`: Multiple Competing Cues
  - `06`: Conversational Distractor
- **Sequence Conformance:** 100% adherence to the standard 6-variant sequence:
  `HN-V01 LEX` → `HN-V02 NAT` → `HN-V03 EXP` → `HN-V04 DSC` → `HN-V05 PRG` → `HN-V06 CMK`.
- **Zero Internal Duplicates:** **0 internal duplicate utterances** within Track 2C.
- **Zero Cross-Track Duplicates:** **0 duplicates** between Track 2C and Tracks 2A or 2B.
- **Defect: 15 Baseline Verbatim Copies in `HN-V01 (LEX)`:**
  In 15 isolated instances, the `HN-V01` variant copied the Stage 2 baseline hard negative verbatim instead of reformulating the distractor:
  1. [`HN01-06-V01`](file:///home/eshwar/code/response/research/s3b/HN01_VP_P_variants.md#L309) matches [`HN01-06`](file:///home/eshwar/code/response/research/s2/hn/HN01_vp_p.md#L59) (`P`)
  2. [`HN03-05-V01`](file:///home/eshwar/code/response/research/s3b/HN03_I_N_variants.md#L254) matches [`HN03-05`](file:///home/eshwar/code/response/research/s2/hn/HN03_i_n.md#L51) (`N`)
  3. [`HN05-05-V01`](file:///home/eshwar/code/response/research/s3b/HN05_VP_I_variants.md#L254) matches [`HN05-05`](file:///home/eshwar/code/response/research/s2/hn/HN05_vp_i.md#L51) (`I`)
  4. [`HN05-06-V01`](file:///home/eshwar/code/response/research/s3b/HN05_VP_I_variants.md#L309) matches [`HN05-06`](file:///home/eshwar/code/response/research/s2/hn/HN05_vp_i.md#L59) (`I`)
  5. [`HN06-02-V01`](file:///home/eshwar/code/response/research/s3b/HN06_VP_N_variants.md#L89) matches [`HN06-02`](file:///home/eshwar/code/response/research/s2/hn/HN06_vp_n.md#L24) (`VP`)
  6. [`HN06-05-V01`](file:///home/eshwar/code/response/research/s3b/HN06_VP_N_variants.md#L254) matches [`HN06-05`](file:///home/eshwar/code/response/research/s2/hn/HN06_vp_n.md#L51) (`N`)
  7. [`HN06-06-V01`](file:///home/eshwar/code/response/research/s3b/HN06_VP_N_variants.md#L309) matches [`HN06-06`](file:///home/eshwar/code/response/research/s2/hn/HN06_vp_n.md#L59) (`N`)
  8. [`HN08-04-V01`](file:///home/eshwar/code/response/research/s3b/HN08_P_N_variants.md#L199) matches [`HN08-04`](file:///home/eshwar/code/response/research/s2/hn/HN08_p_n.md#L43) (`N`)
  9. [`HN08-05-V01`](file:///home/eshwar/code/response/research/s3b/HN08_P_N_variants.md#L254) matches [`HN08-05`](file:///home/eshwar/code/response/research/s2/hn/HN08_p_n.md#L51) (`N`)
  10. [`HN09-01-V01`](file:///home/eshwar/code/response/research/s3b/HN09_P_VN_variants.md#L34) matches [`HN09-01`](file:///home/eshwar/code/response/research/s2/hn/HN09_p_vn.md#L16) (`P`)
  11. [`HN09-02-V01`](file:///home/eshwar/code/response/research/s3b/HN09_P_VN_variants.md#L89) matches [`HN09-02`](file:///home/eshwar/code/response/research/s2/hn/HN09_p_vn.md#L24) (`P`)
  12. [`HN09-04-V01`](file:///home/eshwar/code/response/research/s3b/HN09_P_VN_variants.md#L199) matches [`HN09-04`](file:///home/eshwar/code/response/research/s2/hn/HN09_p_vn.md#L43) (`VN`)
  13. [`HN09-05-V01`](file:///home/eshwar/code/response/research/s3b/HN09_P_VN_variants.md#L254) matches [`HN09-05`](file:///home/eshwar/code/response/research/s2/hn/HN09_p_vn.md#L51) (`VN`)
  14. [`HN10-01-V01`](file:///home/eshwar/code/response/research/s3b/HN10_I_VN_variants.md#L34) matches [`HN10-01`](file:///home/eshwar/code/response/research/s2/hn/HN10_i_vn.md#L17) (`I`)
  15. [`HN10-03-V01`](file:///home/eshwar/code/response/research/s3b/HN10_I_VN_variants.md#L144) matches [`HN10-03`](file:///home/eshwar/code/response/research/s2/hn/HN10_i_vn.md#L35) (`I`)

---

## 4. User Rule & Schema Compliance

1. **User Rule Violation (Uppercase Filenames):**
   - User Rule: *"name the files and folder in lowercase"*.
   - All 30 files are named with uppercase letters (`BA01_...`, `MP01_...`, `HN01_...`).
2. **Suffix Inconsistency:**
   - [`BA01_VP_P_stage3b_variants.md`](file:///home/eshwar/code/response/research/s3b/BA01_VP_P_stage3b_variants.md) includes a redundant `_stage3b_` infix, while all other 29 files use the clean `_variants.md` suffix.
3. **Directory Layout vs. Plan:**
   - [`stage_3b_construction_plan.md#L182-L192`](file:///home/eshwar/code/response/research/plan/stage_3b_construction_plan.md#L182-L192) specifies organizing Stage 3B into 3 separate subdirectories:
     `03b_linguistic_expansion/ ├── 2a_boundary_anchor/ ├── 2b_minimal_pair/ └── 2c_hard_negative/`. Current files reside flat inside [`research/s3b`](file:///home/eshwar/code/response/research/s3b).
4. **Schema Identifiers & Lineage:**
   - Variant subheadings use repeated local identifiers (`### BA-V01`, `### MP-V01`, `### HN-V01`) without unique canonical identifiers (e.g. `BA01-A01-V01`, `MP01-01-V01-VP`, `HN01-01-V01`).
   - Lineage fields (`parent_id`, `lineage_id`) recommended in Section 9 are omitted from variant blocks.
   - Context is declared implicit (`"The preceding task reminder/intervention is implicit"`), omitting the explicit assistant prompt.

---

## 5. Remediation Action Plan

```text
+===================================================================================================+
|                                    REMEDIATION WORKFLOW (STAGE 3B)                                |
+===================================================================================================+
|                                                                                                   |
|   1. REMEDIATE VERBATIM BASELINE COPIES                                                           |
|      - Track 2B: Replace all 104 verbatim Stage 2 copies in MP-V01 (LEX) with novel phrasing.      |
|      - Track 2C: Replace the 15 verbatim copies in HN-V01 (LEX) with novel distractor phrasing.   |
|                                                                                                   |
|   2. RESOLVE TRACK 2B REDUNDANCIES                                                                |
|      - Replace the 72 cross-file shared utterances (e.g. between MP02, MP03, MP05, MP08, MP10).   |
|      - Fix intra-pair repetition in MP01-01 (V01 vs V05).                                         |
|                                                                                                   |
|   3. REBALANCE MINIMAL-PAIR LENGTHS                                                               |
|      - Balance VP, P, and VN word counts in MP01 and MP07 to neutralize length shortcuts.         |
|                                                                                                   |
|   4. RENAME FILES TO LOWERCASE (USER RULE)                                                        |
|      - Rename all 30 files to lowercase (e.g. ba01_vp_p_variants.md, mp01_vp_p_variants.md).        |
|      - Normalize BA01 suffix: remove '_stage3b_'.                                                 |
|                                                                                                   |
|   5. STANDARDIZE METADATA & CANONICAL IDS                                                         |
|      - Upgrade headers to canonical IDs (e.g. BA01-A01-V01, MP01-01-V01-VP, HN01-01-V01).        |
|                                                                                                   |
+===================================================================================================+
```
