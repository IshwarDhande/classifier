# Stage 2 — Four-Task Orthogonal Boundary Construction Plan

**Target:** Stage 2 Boundary Datasets (`BA` Boundary Anchors, `MP` Minimal Pairs, `HN` Hard Negatives)  
**Ontology:** Response Category Ontology V1.0 (`VP`, `P`, `I`, `N`, `VN`)  
**Domain Scope:** Assistive Health & Behavioral Coaching  
**Core Tasks:** `Medication`, `Hydration`, `Exercise`, `Physiotherapy`  
**Location:** [`research/s2/stage_2_four_task_construction_plan.md`](file:///home/eshwar/code/response/research/s2/stage_2_four_task_construction_plan.md)  

---

## 1. Executive Summary & Problem Formulation

In Stage 2, all boundary evaluation and contrast resources are restricted to four primary daily health tasks:
1. **Medication Adherence**
2. **Hydration**
3. **General Exercise** (e.g., walking, stretching)
4. **Physiotherapy Routines** (e.g., rehab movements, session management)

### The Primary Machine Learning Threat: Topic Confounding

When an NLP classifier is trained on a closed set of domain tasks, it is susceptible to **topic shortcut learning**. If certain tasks disproportionately co-occur with specific categories (e.g., simple hydration tasks paired primarily with `P` / `VP`, or complex physiotherapy paired with `N` / `VN`), the neural network learns spurious topical correlations rather than genuine behavioral appraisal:

```
SPURIOUS SHORTCUT (FAILED MODEL):
  "water" / "bottle"  -----------> Predicted Label: P / VP (regardless of stance)
  "physiotherapy"     -----------> Predicted Label: N / VN (regardless of stance)

OBJECTIVE MODEL (BEHAVIORAL APPRAISAL):
  Communicative Intention + Action Commitment ----------> Response Category (VP/P/I/N/VN)
  Task Domain (Med / Hyd / Ex / Phys)        ----------> Zero Predictive Correlation
```

### The Architectural Solution: Orthogonal Closed-Domain Construction

To guarantee that the classifier learns human appraisal rather than domain proxies, the four tasks must be distributed **orthogonally** across all five Response Categories and all ten pairwise boundaries. Every task must exhibit the full behavioral spectrum—from proactive eagerness (`VP`) to hostile reactance (`VN`).

---

## 2. Global Architecture & Boundary Network

```
+===================================================================================================+
|                                  STAGE 2 BOUNDARY RESOURCE SUITE                                  |
+===================================================================================================+

   +-------------------------------+   +-------------------------------+   +-------------------------------+
   |      Stage 2A: BA Files       |   |      Stage 2B: MP Files       |   |      Stage 2C: HN Files       |
   |      (Boundary Anchors)       |   |        (Minimal Pairs)        |   |       (Hard Negatives)        |
   |  10 files x 6 anchors = 60    |   |  10 files x 6 pairs = 60      |   |  10 files x 6 pairs = 60      |
   |  research/s2/ba/              |   |  research/s2/mp/              |   |  research/s2/hn/              |
   +-------------------------------+   +-------------------------------+   +-------------------------------+
                                   \                   |                   /
                                    \                  |                  /
                                     v                 v                 v
   +===================================================================================================+
   |                             FOUR-TASK CLOSED-DOMAIN ORTHOGONAL MESH                                |
   |               [1. Medication]   [2. Hydration]   [3. Exercise]   [4. Physiotherapy]               |
   |                                                                                                   |
   |           EQUAL CLASS COVERAGE: 20% VP  |  20% P  |  20% I  |  20% N  |  20% VN                   |
   |           ZERO TOPIC CORRELATION: Mutual Information(Task, Category) ≈ 0                          |
   +===================================================================================================+
```

---

## 3. Intervention Mechanism Matrix (Preventing Monotony)

To avoid repetitive dialogues, the assistant's prompts rotate systematically through **five intervention modalities** across each of the four health tasks:

```
+===================================================================================================+
|                                4 TASKS x 5 INTERVENTION MECHANISMS                                |
+===================================================================================================+
| Intervention Modality     | 1. Medication        | 2. Hydration         | 3. Exercise          | 4. Physiotherapy     |
|---------------------------+----------------------+----------------------+----------------------+----------------------|
| 1. Environmental Cues     | Beside toothbrush    | Bottle on work desk  | Shoes by front door  | Mat unrolled by bed  |
| 2. Timing / Rescheduling  | Move to post-brkfst  | Glass with each meal | Walk during lunch    | Move session evening |
| 3. Effort / Vol Splitting | Pre-sorted pillbox   | Half-glass increments| 5-min starter walk   | 2 split mini-sessions|
| 4. Scheduled Reminder     | Evening alert chime  | Hourly sip prompt    | Midday calendar alert| Morning push prompt  |
| 5. Facilitating Pairing   | Pair with morning tea| Slice of lemon/fruit | Audio/music pairing  | Companion stretching |
+===================================================================================================+
```

---

## 4. Deterministic Task Allocation Across Files

### A. Stage 2A: Boundary Anchors (`ba/`)

Each BA file contains **6 anchors** grouped into **3 paired contexts**:
- Context 1: Anchors `A01` (Proto A) & `A02` (Proto B)
- Context 2: Anchors `A03` (Leaning A) & `A04` (Leaning B)
- Context 3: Anchors `A05` (Implicit A) & `A06` (Implicit B)

To balance the 30 contexts across 4 tasks, tasks are rotated cyclically using a Latin-Square schedule:

```
+===================================================================================================+
|                                  BA LATIN-SQUARE TASK ALLOCATION                                  |
+===================================================================================================+
| File Name         | Boundary   | Tier   | Context 1 (A01/A02) | Context 2 (A03/A04) | Context 3 (A05/A06) |
|-------------------+------------+--------+---------------------+---------------------+---------------------|
| BA01_vp_p.md      | VP <-> P   | Tier 1 | 1. Medication       | 2. Hydration        | 3. Exercise         |
| BA02_p_i.md       | P <-> I    | Tier 1 | 4. Physiotherapy    | 1. Medication       | 2. Hydration        |
| BA03_i_n.md       | I <-> N    | Tier 1 | 3. Exercise         | 4. Physiotherapy    | 1. Medication       |
| BA04_n_vn.md      | N <-> VN   | Tier 1 | 2. Hydration        | 3. Exercise         | 4. Physiotherapy    |
| BA05_vp_i.md      | VP <-> I   | Tier 2 | 1. Medication       | 2. Hydration        | 3. Exercise         |
| BA06_vp_n.md      | VP <-> N   | Tier 2 | 4. Physiotherapy    | 1. Medication       | 2. Hydration        |
| BA07_vp_vn.md     | VP <-> VN  | Tier 2 | 3. Exercise         | 4. Physiotherapy    | 1. Medication       |
| BA08_p_n.md       | P <-> N    | Tier 2 | 2. Hydration        | 3. Exercise         | 4. Physiotherapy    |
| BA09_p_vn.md      | P <-> VN   | Tier 2 | 1. Medication       | 2. Hydration        | 3. Exercise         |
| BA10_i_vn.md      | I <-> VN   | Tier 2 | 4. Physiotherapy    | 1. Medication       | 2. Hydration        |
+===================================================================================================+
Total Contexts in BA: Medication: 8 | Hydration: 7 | Exercise: 8 | Physiotherapy: 7 (Sum = 30)
```

### B. Stage 2B: Minimal Pairs (`mp/`)

Each MP file contains **6 minimal pairs** (`MPxx-01` to `MPxx-06`). To achieve exact parity across all 60 pairs ($15 \times 4 = 60$):
- Pair 01: **Medication**
- Pair 02: **Hydration**
- Pair 03: **Exercise**
- Pair 04: **Physiotherapy**
- Pair 05: Alternate between **Medication** (odd files) and **Exercise** (even files)
- Pair 06: Alternate between **Hydration** (odd files) and **Physiotherapy** (even files)

### C. Stage 2C: Hard Negatives (`hn/`)

Each HN file contains **6 adversarial distraction patterns**:
1. `HNxx-01`: Competing Keyword
2. `HNxx-02`: Competing Phrase
3. `HNxx-03`: Misleading Opening Clause
4. `HNxx-04`: Mid-Sentence Self-Correction
5. `HNxx-05`: Multiple Competing Cues
6. `HNxx-06`: Pragmatic / Sarcastic Inversion

The 6 patterns rotate through the 4 tasks in identical fashion, guaranteeing that no hard negative pattern is exclusive to one health task.

---

## 5. Pragmatic Phrasing Rubrics per Response Category

To ensure natural, diverse, and human-like utterances, generation across all four tasks must follow these exact behavioral markers:

```
+===================================================================================================+
|                                    PRAGMATIC REALIZATION PATTERNS                                 |
+===================================================================================================+
| Label | Behavioral Core       | Key Linguistic Features                     | Counter-Example Traps               |
|-------+-----------------------+---------------------------------------------+-------------------------------------|
| VP    | Eager Appraisal &     | • Value appraisal ("makes it much easier")  | DO NOT rely on hyperbolic exclam-   |
|       | Proactive Preparation | • Immediate agency ("setting it up now")    | ations ("OMG wonderful!!!"). Focus  |
|       |                       | • Forward commitment ("start tonight")      | on behavioral agency.               |
|-------+-----------------------+---------------------------------------------+-------------------------------------|
| P     | Routine Cooperation   | • Mechanical consent ("okay", "sure", "yes")| DO NOT add enthusiasm or proactive  |
|       | & Minimum Compliance  | • Simple adherence ("I'll take it then")    | preparation. Must remain simple.    |
|       |                       | • No extra appraisal or proactive steps     |                                     |
|-------+-----------------------+---------------------------------------------+-------------------------------------|
| I     | Neutral Deferral &    | • Decision postponement ("decide later")    | DO NOT include refusal verbs. Must  |
|       | Cognitive Uncertainty | • Option acknowledgement ("one possibility")| remain genuinely uncommitted        |
|       |                       | • Feasibility hedging ("might work")        | without resisting the assistant.    |
|-------+-----------------------+---------------------------------------------+-------------------------------------|
| N     | Recoverable           | • Preference resistance ("rather not")      | DO NOT shut down the conversation.  |
|       | Behavioral Resistance | • Alternative timing ("prefer later")       | Must remain open to recovery or     |
|       |                       | • Manageable refusal ("skip for today")     | alternative scheduling.             |
|-------+-----------------------+---------------------------------------------+-------------------------------------|
| VN    | Unrecoverable Rejection| • Directive shutdown ("stop asking me")    | DO NOT assume politeness means P.   |
|       | & High Reactance      | • Autonomy assertion ("manage my own life") | "Please stop offering" is still VN  |
|       |                       | • Permanent refusal ("done discussing this")| due to absolute topic shutdown.     |
+===================================================================================================+
```

### Exemplary 4-Task Phrasing Matrix

```
Task: 1. MEDICATION
  VP: "That'll make it much simpler to remember. I'll place the pillbox right next to my cup tonight."
   P: "Okay, that works. I'll take the morning dose right after breakfast."
   I: "That's one option. I haven't decided if I want to shift the timing yet."
   N: "I'd rather keep taking it in the evening; shifting to breakfast doesn't suit my schedule."
  VN: "Stop trying to manage my medication schedule. I'm not changing it, so drop it."

Task: 2. HYDRATION
  VP: "Having it right in front of me will really help. I'm filling a fresh bottle for my desk now."
   P: "Sure, I can keep a water bottle on my desk today."
   I: "A bottle on the desk might be helpful. I'll see how my workspace looks later."
   N: "My desk is already crowded, so I'd rather not keep a water bottle sitting there."
  VN: "I don't need you monitoring how much water I drink. Stop bringing this up."

Task: 3. EXERCISE
  VP: "That sounds like a great routine. I'll put my shoes by the door so I'm ready immediately."
   P: "Alright, I'll take a short walk around the block after lunch."
   I: "Taking a walk after lunch is a possibility. I'll see what the weather is like then."
   N: "I have other things to catch up on during lunch, so I'd prefer to skip the walk today."
  VN: "I told you I'm not exercising today. Stop nagging me about it."

Task: 4. PHYSIOTHERAPY
  VP: "Splitting the session will take the pressure off. I'll do the first set before work today."
   P: "Okay, I'll divide the exercises into two shorter sessions."
   I: "Two shorter sessions could be an option. I'll decide when I look at my schedule later."
   N: "Doing two separate sessions feels like more hassle. I'd rather do them all at once or not at all."
  VN: "Leave my physiotherapy alone. I'm sick of hearing these exercise suggestions."
```

---

## 6. Formatting & Schema Standardization Rules

All 30 files in [`research/s2/`](file:///home/eshwar/code/response/research/s2/) must adhere to identical formatting standards:

1. **Heading Hierarchy**:
   - Level 1: `# <CODE> — <PAIR> <TYPE>` (e.g., `# MP08 — P ↔ N Minimal Pairs`)
   - Level 2: `## Boundary`, followed by `### Core distinction` (or `### Construction focus`)
   - Level 2 for items: `## BA01-A01 — VP Prototype` or `## MP08-01`
2. **Context Representation**:
   - Strict conversational dialogue turn format:
     ```markdown
     **Context:**  
     Assistant: “Would you like to keep your medication beside your morning tea?”
     ```
   - No third-person descriptive narrative text (`The assistant suggests...` is deprecated).
3. **Turn Formatting & Typography**:
   - User utterances enclosed in standard directional curly quotes (`“...”`).
   - Explicit role labels (`**User:**`, `**VP:**`, `**P:**`).
4. **Dividers**:
   - Clean horizontal rules (`---`) preceding every anchor or pair block.
5. **Gold Labels Key**:
   - Every file must conclude with an unambiguous Markdown mapping table (`## Gold Labels` or `## Label Key`).

---

## 7. Deterministic Auditing & Verification Protocol

Before finalizing any changes to Stage 2 files, automated test scripts in [`code/scripts/`](file:///home/eshwar/code/response/code/scripts/) must verify the following properties:

1. **Zero Topical Bias**:
   $$\chi^2 \text{ test of independence between } \text{Task Domain} \text{ and } \text{Response Category} \implies p > 0.95$$
2. **Lexical Leakage Audit**:
   - Zero duplicate user utterances across all 60 anchors in `ba/`, all 60 pairs in `mp/`, and all 60 pairs in `hn/`.
3. **Exact Class Parity**:
   - Exactly equal row counts for all five categories across the collective suite.

---

### Reference Links
- Boundary Anchors Directory: [`research/s2/ba/`](file:///home/eshwar/code/response/research/s2/ba/)
- Minimal Pairs Directory: [`research/s2/mp/`](file:///home/eshwar/code/response/research/s2/mp/)
- Hard Negatives Directory: [`research/s2/hn/`](file:///home/eshwar/code/response/research/s2/hn/)
- Stage 2 Construction Plan: [`research/plan/stage_2_construction_plan.md`](file:///home/eshwar/code/response/research/plan/stage_2_construction_plan.md)
- Audit Scripts: [`code/scripts/audit_s2_ba.py`](file:///home/eshwar/code/response/code/scripts/audit_s2_ba.py), [`code/scripts/audit_s2_mp.py`](file:///home/eshwar/code/response/code/scripts/audit_s2_mp.py)
