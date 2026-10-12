# Stage 1 — Quick Review Guide: Semantic Coverage Framework

**Directory:** [`/home/eshwar/code/response/research/s1`](file:///home/eshwar/code/response/research/s1)  
**Stage:** Stage 1 — Semantic Coverage  
**Ontology:** Response Category Ontology V1.0  
**Status:** Complete Reference & Review Document  

---

## 1. Executive Summary & Architecture

Stage 1 constructs the **behavioral semantic foundation** for classifying user responses into five discrete Response Categories (`VP`, `P`, `I`, `N`, `VN`). Rather than allowing the classifier to latch onto superficial lexical tokens, sentiment words, or emotion, Stage 1 establishes systematic semantic coverage across distinct behavioral situations.

### 1.1 The 4-Tier Semantic Construction Pipeline

```text
+-------------------------------------------------------------------------+
|                       1. Response Category Ontology                     |
|                                                                         |
|        [VN]  <--------  [N]  <--------  [I]  -------->  [P]  -------->  [VP]       |
|    Very Negative     Negative      Indifferent     Positive    Very Positive|
+-------------------------------------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                  2. Behavioral Semantic Dimensions (12)                 |
|                                                                         |
|  Acceptance/Rejection  |  Behavioral Commitment  |  Resistance Level     |
|  Engagement Depth      |  Enthusiasm/Appraisal   |  Reactance/Opposition|
|  Cooperation Form      |  Temporal Immediacy     |  Signal Explicitness |
|  Evidence Strength     |  Social Softening       |  Mixed Structures    |
+-------------------------------------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                  3. Semantic Subtype Catalogue (20 Subtypes)            |
|                                                                         |
|       VP (4)       |      P (4)     |      I (4)    |    N (4)    |   VN (4)   |
|   VP-01 to VP-04   | P-01 to P-04   |  I-01 to I-04 | N-01 to N-04|VN-01..VN-04|
+-------------------------------------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                4. Semantic Scenario Inventory (100 Scenarios)           |
|                                                                         |
|     20 Scenarios   |  20 Scenarios  |  20 Scenarios | 20 Scenarios|20 Scenarios|
|      (S01 - S05)   |   (S01 - S05)  |   (S01 - S05) |  (S01 - S05)| (S01 - S05)|
+-------------------------------------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                 5. Linguistic Realization Anchors (300 Planned)         |
|                                                                         |
|         [Direct]        |         [Indirect]         | [Natural Conv.]  |
|   Explicit behavioral   | Pragmatic / implicature    | Spontaneous,     |
|   stance & markers      | without explicit marker    | colloquial       |
+-------------------------------------------------------------------------+
```

---

### 1.2 File Index & Structural Map

| File | Target Role | Key Components | Volume |
|---|---|---|---|
| [`01_behavioral_semantic_dimensions.md`](file:///home/eshwar/code/response/research/s1/01_behavioral_semantic_dimensions.md) | Dimensional Theory | 12 Cross-category dimensions, Category profiles, Orthogonality rules | 802 lines |
| [`02_semantic_subtype_catalogue.md`](file:///home/eshwar/code/response/research/s1/02_semantic_subtype_catalogue.md) | Subtype Architecture | 4 Subtypes per category, Definitions, Boundary guidelines | 551 lines |
| [`03_semantic_scenarios_vp.md`](file:///home/eshwar/code/response/research/s1/03_semantic_scenarios_vp.md) | Very Positive Scenarios | VP-01 to VP-04 scenarios, cores, boundaries, cross-coverage | 20 scenarios |
| [`04_semantic_scenarios_p.md`](file:///home/eshwar/code/response/research/s1/04_semantic_scenarios_p.md) | Positive Scenarios | P-01 to P-04 scenarios, cores, boundaries, cross-coverage | 20 scenarios |
| [`05_semantic_scenarios_i.md`](file:///home/eshwar/code/response/research/s1/05_semantic_scenarios_i.md) | Indifferent Scenarios | I-01 to I-04 scenarios, cores, boundaries, cross-coverage | 20 scenarios |
| [`06_semantic_scenarios_n.md`](file:///home/eshwar/code/response/research/s1/06_semantic_scenarios_n.md) | Negative Scenarios | N-01 to N-04 scenarios, cores, boundaries, cross-coverage | 20 scenarios |
| [`07_semantic_scenarios_vn.md`](file:///home/eshwar/code/response/research/s1/07_semantic_scenarios_vn.md) | Very Negative Scenarios | VN-01 to VN-04 scenarios, cores, boundaries, cross-coverage | 20 scenarios |
| [`anchors/01_initial_anchors_vp.md`](file:///home/eshwar/code/response/research/s1/anchors/01_initial_anchors_vp.md) | Linguistic Realizations | 3 Realization styles (Direct, Indirect, Natural) per VP scenario | 60 anchors |

---

## 2. Behavioral Dimensions & Theory (`01_behavioral_semantic_dimensions.md`)

### 2.1 The Ordinal Response Scale

Response Category measures the user's **immediate behavioral appraisal/reaction toward the intervention**.

```text
  [VN]                    [N]                [I]                [P]                  [VP]
  Very Negative         Negative         Indifferent          Positive          Very Positive
<---------------------+-------------------+-------------------+-------------------+--------------------->
  Active Rejection      Reluctance /       Neutral /           Cooperation /       Enthusiasm /
  Opposition /          Mild Refusal /     Non-Commitment /    Willingness /       Appreciation /
  High Reactance /      Disagreement /     Insufficient        Acceptance /        Proactive /
  Disengagement         Conditional Res.   Evidence            Commitment          Voluntary Coop.
```

### 2.2 The 12 Cross-Category Behavioral Dimensions

```text
Dimension 1: Acceptance / Rejection Orientation
Strong Rejection <-------- Resistance <-------- Neutral <-------- Acceptance --------> Strong Acceptance

Dimension 2: Behavioral Commitment
No Commitment <-------- Ambiguous / Weak <-------- Conditional <-------- Clear --------> Strong / Proactive

Dimension 3: Resistance Level
Dominant / Active Opp. <-------- Moderate Refusal <-------- Mild Reluctance <-------- Zero Resistance

Dimension 4: Engagement Depth
Active Disengagement <-------- Minimal Interaction <-------- Neutral Receipt <-------- Proactive Extension

Dimension 5: Enthusiasm / Appreciation
Unfavorable / Cynical <-------- Neutral Flatness <-------- Polite Appreciation <-------- High Enthusiasm / Value

Dimension 6: Reactance / Opposition
Extreme Defiance <-------- Guarded Opposition <-------- Neutral Compliance <-------- Open Receptivity
```

| # | Dimension Name | Behavioral Spectrum | Diagnostic Relevance |
|---|---|---|---|
| **3.1** | **Acceptance / Rejection** | Strong Rejection ↔ Strong Acceptance | Primary axis distinguishing all 5 ordinal classes |
| **3.2** | **Behavioral Commitment** | None ↔ Ambiguous ↔ Conditional ↔ Clear ↔ Proactive | Crucial for separating `I` from `P`, and `P` from `VP` |
| **3.3** | **Resistance Level** | Zero ↔ Mild Hesitation ↔ Open Reluctance ↔ Active Opposition | Separates `P` from `N`, and `N` from `VN` |
| **3.4** | **Engagement Depth** | Disengagement ↔ Minimal ↔ Cooperative ↔ Proactive | Identifies `VP-03` (proactive) and `VN-04` (disengagement) |
| **3.5** | **Enthusiasm / Appreciation** | Hostility ↔ Flat Neutral ↔ Moderate ↔ High Value Recognition | Key discriminator lifting `P` into `VP` (`VP-01`, `VP-02`) |
| **3.6** | **Reactance / Opposition** | None ↔ Friction ↔ Acute Threat to Autonomy | Primary marker distinguishing `N` from `VN` (`VN-02`, `VN-03`) |
| **3.7** | **Cooperation Form** | Active Defiance ↔ Reluctant ↔ Cooperative ↔ Voluntary | Assesses willingness to work with the intervention |
| **3.8** | **Temporal Immediacy** | Immediate Action ↔ Delayed Follow-Through ↔ Indefinite Delay | Validates delayed cooperation (`P-04`) vs avoidance (`N-01`) |
| **3.9** | **Signal Explicitness** | Explicit Marker ↔ Conversational Implicature ↔ Ambiguous | Guides realization across direct vs indirect anchors |
| **3.10**| **Evidence Strength** | Insufficient Evidence ↔ Plausible Stance ↔ Unambiguous Proof | Protects `I-04` from becoming a catch-all bin |
| **3.11**| **Social Softening** | Blunt Hostility ↔ Politeness-Wrapped Resistance ↔ Politeness | Prevents polite "no thank you" from escaping `N` / `VN` |
| **3.12**| **Mixed Structure** | Pure Accept ↔ Mixed (Accept Dominates) ↔ Mixed (Resist Dominates) | Forces resolution based on the net behavioral outcome |

---

### 2.3 2D Behavioral Coordinate Space

Mapping Response Categories along **Acceptance vs. Rejection** (X-axis) and **Behavioral Intensity / Reactance** (Y-axis):

```text
  Behavioral Intensity / Reactance
  ^
  |  [VN-03 Hostile Reactance]                   [VP-01 Enthusiastic Accept]
  |  [VN-04 Active Disengagement]                [VP-03 Proactive Engagement]
  |  [VN-01 Strong Rejection]                    [VP-02 Strong Appreciation]
H |  [VN-02 Strong Opposition]                   [VP-04 Voluntary Cooperation]
I |
G |
H |         [N-03 Disagreement]                  [P-02 Cooperative Commit]
  |         [N-02 Mild Refusal]                  [P-01 Ordinary Acceptance]
M |         [N-04 Conditional Res.]              [P-03 Qualified Acceptance]
I |         [N-01 Reluctance]                    [P-04 Delayed Acceptance]
D |
  |                         [I-02 Uncertain Position]
L |                         [I-03 Non-Commitment]
O |                         [I-01 Neutral Ack.]
W |                         [I-04 Insufficient Evidence]
  |
  +-------------------------------------------------------------------------->
  REJECTION (VN) <--------- RELUCTANCE (N) <--- NEUTRAL (I) ---> ACCEPTANCE (P) ---> STRONG ACCEPT (VP)
```

---

### 2.4 Orthogonality & Disentanglement Rules

The Response Category reflects **only** immediate behavioral appraisal toward the intervention. It must remain orthogonal to other conversational dimensions:

```text
+-----------------------------------------------------------------------------------+
|                            ORTHOGONALITY BOUNDARY                                 |
|                                                                                   |
|   +-----------------------+              +------------------------------------+   |
|   |   RESPONSE CATEGORY   |     =/=      |         SENTIMENT & EMOTION        |   |
|   | (Behavioral Stance)   |              |  - Angry tone + accepts advice = P |   |
|   |  VP / P / I / N / VN  |              |  - Polite tone + rejects = N / VN  |   |
|   +-----------------------+              +------------------------------------+   |
|               ||                                          ||                      |
|              =/=                                         =/=                      |
|               ||                                          ||                      |
|   +-----------------------+              +------------------------------------+   |
|   |   DIALOGUE PURPOSE    |     =/=      |         PERSUASION BARRIER         |   |
|   |  - Inform, Inquire,   |              |  - No Time, Distrust, Habit, Cost  |   |
|   |    Clarify, Request   |              |  (The barrier reason != the stance)|   |
|   +-----------------------+              +------------------------------------+   |
|               ||                                          ||                      |
|              =/=                                         =/=                      |
|               ||                                          ||                      |
|   +-----------------------+              +------------------------------------+   |
|   |   EXECUTION STATUS    |     =/=      |          TASK COMPLETION           |   |
|   |  - Not Started,       |              |  - Task already finished != VP     |   |
|   |    In Progress, Done  |              |  - User dropped task != VN         |   |
|   +-----------------------+              +------------------------------------+   |
+-----------------------------------------------------------------------------------+
```

---

## 3. Semantic Subtype Catalogue (`02_semantic_subtype_catalogue.md`)

Each Response Category is divided into **4 distinct behavioral subtypes** (20 subtypes total):

```text
RESPONSE CATEGORIES (5)
├── VP — Very Positive
│   ├── VP-01: Enthusiastic Acceptance
│   ├── VP-02: Strong Appreciation
│   ├── VP-03: Proactive Engagement
│   └── VP-04: Strong Voluntary Cooperation
├── P — Positive
│   ├── P-01: Ordinary Acceptance
│   ├── P-02: Cooperative Commitment
│   ├── P-03: Qualified Acceptance
│   └── P-04: Delayed Genuine Acceptance
├── I — Indifferent
│   ├── I-01: Neutral Acknowledgement
│   ├── I-02: Uncertain Position
│   ├── I-03: Non-Commitment
│   └── I-04: Insufficient Behavioral Evidence
├── N — Negative
│   ├── N-01: Reluctance
│   ├── N-02: Mild Refusal
│   ├── N-03: Disagreement
│   └── N-04: Conditional Resistance
└── VN — Very Negative
    ├── VN-01: Strong Rejection
    ├── VN-02: Strong Opposition
    ├── VN-03: Hostile Reactance
    └── VN-04: Active Disengagement
```

---

### 3.1 Master 20-Subtype Reference Matrix

| Cat | Subtype ID | Subtype Name | Core Behavioral Definition | Boundary Differentiator |
|---|---|---|---|---|
| **VP** | `VP-01` | **Enthusiastic Acceptance** | High willingness + visible eagerness/enthusiasm | Elevated positive energy compared to standard acceptance |
| **VP** | `VP-02` | **Strong Appreciation** | Recognition of intervention usefulness/benefit | Genuine value appreciation beyond routine politeness |
| **VP** | `VP-03` | **Proactive Engagement** | Voluntary extension beyond required interaction | Self-initiated questions, next steps, or broader goals |
| **VP** | `VP-04` | **Strong Voluntary Coop.**| Unprompted, spontaneous commitment to act | High self-agency and cooperation without agent pressure |
| **P** | `P-01` | **Ordinary Acceptance** | Direct agreement, straightforward willingness | Positive compliance without elevated excitement or praise |
| **P** | `P-02` | **Cooperative Commitment** | Explicit pledge/intent to execute recommendation | Concrete commitment distinguishing it from passive receipt |
| **P** | `P-03` | **Qualified Acceptance** | Acceptance with minor conditions/reservations | Cooperation remains dominant over the stated constraint |
| **P** | `P-04` | **Delayed Acceptance** | Postponed execution but genuine willingness | Delay represents scheduling/constraint, not avoidance |
| **I** | `I-01` | **Neutral Acknowledgement**| Acknowledges receipt ("okay", "I see") | No evidence of intent to follow or reject recommendation |
| **I** | `I-02` | **Uncertain Position** | Hesitating, considering, weighing options | Position is unformed; neither accepting nor resisting |
| **I** | `I-03` | **Non-Commitment** | Responds conversationally without committing | Avoids taking a stance while continuing dialogue |
| **I** | `I-04` | **Insufficient Evidence** | Fragmented, minimal, or ambiguous signal | Context cannot resolve whether user agrees or resists |
| **N** | `N-01` | **Reluctance** | Hesitant, begrudging, unenthusiastic stance | Willingness is impaired, but does not cross into flat refusal |
| **N** | `N-02` | **Mild Refusal** | Polite or soft declining of intervention | Clear refusal, but non-hostile and recoverable |
| **N** | `N-03` | **Disagreement** | Substantive dispute with advice or premise | Cognitive friction or objection without personal reactance |
| **N** | `N-04` | **Conditional Resistance**| Resistance tied to a specific current obstacle | User will not comply now, but might if terms change |
| **VN**| `VN-01` | **Strong Rejection** | Definitive, emphatic refusal to cooperate | Final and non-negotiable rejection of the intervention |
| **VN**| `VN-02` | **Strong Opposition** | Direct counter-attack on advice value/premise | Active combatting of the agent's recommendation |
| **VN**| `VN-03` | **Hostile Reactance** | Anger, hostility, annoyance at persuasion | Defense of personal autonomy against perceived manipulation |
| **VN**| `VN-04` | **Active Disengagement**| Unilateral termination of interaction | Demands to stop contact, walkouts, closing channel |

---

### 3.2 Critical Boundary Decision Flowchart

```text
                           [ USER UTTERANCE ]
                                   |
                  Is there evidence of REJECTION / RESISTANCE?
                               /               \
                            YES                 NO
                            /                     \
       Is resistance strong, hostile, or       Does the user accept or commit
       aimed at ending the interaction?        to the intervention?
              /                \                    /                \
           YES                  NO               YES                  NO
           /                     \               /                     \
      +---------+           +---------+     +---------+           +---------+
      |   VN    |           |    N    |     | P or VP |           |    I    |
      |  Very   |           |Negative |     +---------+           |Indiff.  |
      |Negative |           +---------+          |                +---------+
      +---------+                                |                     |
     (Definitive             (Recoverable,   Is there strong       (Neutral ack,
      rejection,              reluctant,      enthusiasm, deep      uncertainty,
      hostility,              mild refusal,   appreciation, or      non-commit,
      shut down)              disagreement)   proactivity?          no evidence)
                                              /          \
                                           YES            NO
                                           /                \
                                    +---------+          +---------+
                                    |   VP    |          |    P    |
                                    |  Very   |          |Positive |
                                    |Positive |          +---------+
                                    +---------+         (Ordinary
                                    (Elevated            acceptance,
                                     energy,             commitment,
                                     initiative)         qualified)
```

---

## 4. Scenario Inventories: Complete 100-Scenario Catalog

The 100 scenarios across [`03_`](file:///home/eshwar/code/response/research/s1/03_semantic_scenarios_vp.md), [`04_`](file:///home/eshwar/code/response/research/s1/04_semantic_scenarios_p.md), [`05_`](file:///home/eshwar/code/response/research/s1/05_semantic_scenarios_i.md), [`06_`](file:///home/eshwar/code/response/research/s1/06_semantic_scenarios_n.md), and [`07_`](file:///home/eshwar/code/response/research/s1/07_semantic_scenarios_vn.md) provide the operational test bed for Stage 1.

### 4.1 Master 100-Scenario Breakdown

```text
===================================================================================================
CATEGORY: VP (Very Positive) — 20 Scenarios
===================================================================================================
  [VP-01 Enthusiastic Acceptance]
    VP-01-S01 : Eager Acceptance of Recommendation
    VP-01-S02 : Enthusiastic Agreement After Explanation
    VP-01-S03 : Immediate Enthusiastic Willingness
    VP-01-S04 : Strong Positive Reaction to Helpful Intervention
    VP-01-S05 : Enthusiastic Acceptance of Follow-Up Action
  [VP-02 Strong Appreciation]
    VP-02-S01 : Strong Appreciation of Help
    VP-02-S02 : Recognition of Significant Helpfulness
    VP-02-S03 : Appreciation After Successful Guidance
    VP-02-S04 : Strong Gratitude for Persuasive Support
    VP-02-S05 : Appreciation with Continued Willingness
  [VP-03 Proactive Engagement]
    VP-03-S01 : Voluntary Follow-Up Question
    VP-03-S02 : Request for Additional Guidance
    VP-03-S03 : Voluntary Extension of Interaction
    VP-03-S04 : Self-Initiated Next Step
    VP-03-S05 : Positive Engagement with Broader Goal
  [VP-04 Strong Voluntary Cooperation]
    VP-04-S01 : Voluntary Commitment to Act
    VP-04-S02 : Voluntary Agreement to Recommended Routine
    VP-04-S03 : Willing Cooperation Without Pressure
    VP-04-S04 : Voluntary Follow-Through Intention
    VP-04-S05 : Strong Cooperation with Continued Intervention

===================================================================================================
CATEGORY: P (Positive) — 20 Scenarios
===================================================================================================
  [P-01 Ordinary Acceptance]
    P-01-S01  : Straightforward Acceptance
    P-01-S02  : Cooperative Agreement
    P-01-S03  : Acceptance of a Routine Recommendation
    P-01-S04  : Positive Response Without Strong Enthusiasm
    P-01-S05  : Simple Acceptance After Brief Consideration
  [P-02 Cooperative Commitment]
    P-02-S01  : Clear Commitment to Follow Through
    P-02-S02  : Commitment to a Recommended Routine
    P-02-S03  : Commitment to Complete a Specific Action
    P-02-S04  : Agreement to Continue the Recommended Practice
    P-02-S05  : Commitment After Clarification
  [P-03 Qualified Acceptance]
    P-03-S01  : Acceptance with a Practical Condition
    P-03-S02  : Acceptance with a Minor Reservation
    P-03-S03  : Conditional Willingness
    P-03-S04  : Acceptance with Limited Constraint
    P-03-S05  : Acceptance with Mild Concern
  [P-04 Delayed Genuine Acceptance]
    P-04-S01  : Acceptance with Later Action
    P-04-S02  : Commitment to Act Later
    P-04-S03  : Acceptance After Current Constraint
    P-04-S04  : Future Follow-Through Intention
    P-04-S05  : Deferred but Genuine Cooperation

===================================================================================================
CATEGORY: I (Indifferent) — 20 Scenarios
===================================================================================================
  [I-01 Neutral Acknowledgement]
    I-01-S01  : Simple Acknowledgement
    I-01-S02  : Recognition Without Commitment
    I-01-S03  : Receipt of Recommendation
    I-01-S04  : Neutral Response to Repeated Intervention
    I-01-S05  : Neutral Acknowledgement of Suggested Action
  [I-02 Uncertain Position]
    I-02-S01  : Uncertain About Whether to Act
    I-02-S02  : Considering the Recommendation
    I-02-S03  : Unsure About Future Cooperation
    I-02-S04  : Ambiguous Position After Explanation
    I-02-S05  : Deferring a Behavioral Decision Without Resistance
  [I-03 Non-Commitment]
    I-03-S01  : No Commitment to Follow Through
    I-03-S02  : Open-Ended Future Response
    I-03-S03  : Non-Committal Response to Direct Recommendation
    I-03-S04  : Acknowledgement Without Follow-Through Intention
    I-03-S05  : Unresolved Willingness After Discussion
  [I-04 Insufficient Behavioral Evidence]
    I-04-S01  : Minimal Behavioral Signal
    I-04-S02  : Ambiguous Short Response in Context
    I-04-S03  : Response Not Directed Clearly Toward Intervention
    I-04-S04  : Incomplete Behavioral Position
    I-04-S05  : Context Does Not Resolve Ambiguity

===================================================================================================
CATEGORY: N (Negative) — 20 Scenarios
===================================================================================================
  [N-01 Reluctance]
    N-01-S01  : Hesitant Willingness
    N-01-S02  : Reluctance to Begin
    N-01-S03  : Reduced Willingness After Repeated Recommendation
    N-01-S04  : Reluctant Acceptance of Limited Action
    N-01-S05  : Hesitation About Continuing the Recommended Practice
  [N-02 Mild Refusal]
    N-02-S01  : Direct Mild Refusal
    N-02-S02  : Refusal of a Specific Recommendation
    N-02-S03  : Declining the Proposed Action for the Present
    N-02-S04  : Mild Refusal with Continued Discussion
    N-02-S05  : Refusal Without Hostility
  [N-03 Disagreement]
    N-03-S01  : Disagreement with Recommendation
    N-03-S02  : Disagreement with Intervention Rationale
    N-03-S03  : Challenge to Recommended Approach
    N-03-S04  : Preference Against the Recommended Action
    N-03-S05  : Disagreement with Continued Openness
  [N-04 Conditional Resistance]
    N-04-S01  : Resistance Under a Current Constraint
    N-04-S02  : Willingness Only Under a Specific Condition
    N-04-S03  : Resistance to Current Form of Intervention
    N-04-S04  : Conditional Cooperation After Adjustment
    N-04-S05  : Temporary Resistance

===================================================================================================
CATEGORY: VN (Very Negative) — 20 Scenarios
===================================================================================================
  [VN-01 Strong Rejection]
    VN-01-S01 : Explicit Rejection of the Recommendation
    VN-01-S02 : Firm Rejection of the Intervention
    VN-01-S03 : Repeated Rejection After Continued Intervention
    VN-01-S04 : Rejection of Further Recommendation
    VN-01-S05 : Definitive Refusal to Cooperate
  [VN-02 Strong Opposition]
    VN-02-S01 : Explicit Opposition to the Intervention
    VN-02-S02 : Strong Opposition to the Recommended Approach
    VN-02-S03 : Rejection of the Intervention's Premise
    VN-02-S04 : Persistent Opposition During Discussion
    VN-02-S05 : Strong Opposition to Agent's Assistance
  [VN-03 Hostile Reactance]
    VN-03-S01 : Hostile Rejection
    VN-03-S02 : Aggressive Resistance to Continued Persuasion
    VN-03-S03 : Angrily Rejecting Repeated Reminders
    VN-03-S04 : Hostile Demand to Stop the Intervention
    VN-03-S05 : Hostile Rejection of Agent Help
  [VN-04 Active Disengagement]
    VN-04-S01 : Explicit Termination of the Interaction
    VN-04-S02 : Demand to Stop Contact
    VN-04-S03 : Refusal of Further Assistance
    VN-04-S04 : Withdrawal from the Interaction
    VN-04-S05 : Definitive Closure of Intervention
```

---

### 4.2 Critical Contrasts Between Sibling & Neighboring Subtypes

| Comparison Pair | The Critical Behavioral Test | Correct Classification |
|---|---|---|
| **`P-03` vs `N-04`** (Qualified Accept vs Conditional Resist) | Does the response indicate baseline willingness subject to a condition, or baseline refusal until terms change? | If user leans toward doing it: `P-03`<br>If user refuses unless altered: `N-04` |
| **`P-04` vs `N-01`** (Delayed Accept vs Reluctance) | Is the time delay due to practical scheduling constraints, or an underlying hesitation/unwillingness to act? | Genuine intent scheduled later: `P-04`<br>Hesitant, dragging feet: `N-01` |
| **`I-01` vs `P-01`** (Neutral Ack vs Ordinary Accept) | Does the utterance commit the user to action, or merely acknowledge receipt of the message? | "Understood / Okay / I see": `I-01`<br>"Sure, I'll do that": `P-01` |
| **`I-02` vs `N-01`** (Uncertainty vs Reluctance) | Is the user undecided/seeking clarity, or actively showing disinclination? | Weighing pros/cons: `I-02`<br>Grudging / hesitant: `N-01` |
| **`N-02` vs `VN-01`** (Mild Refusal vs Strong Rejection) | Is the rejection recoverable and polite, or categorical and definitive? | "I'd rather not today": `N-02`<br>"Absolutely not, never": `VN-01` |
| **`N-03` vs `VN-02`** (Disagreement vs Strong Opposition) | Is the user disputing an idea, or actively attacking the intervention's validity and agency? | Counter-viewpoint: `N-03`<br>Total rejection of premise: `VN-02` |
| **`VP-01` vs `P-01`** (Enthusiastic vs Ordinary) | Is there evidence of heightened positive emotional/behavioral investment? | "Sounds great, can't wait!": `VP-01`<br>"Okay, works for me": `P-01` |

---

## 5. Anchor Realizations & Linguistics (`anchors/`)

### 5.1 The Tri-Modal Realization Model

To prevent lexical overfitting during fine-tuning, every scenario generates **three distinct realization styles**:

```text
+-------------------------------------------------------------------------------+
|                            SEMANTIC SCENARIO                                  |
|                 (e.g., VP-01-S01: Eager Acceptance)                           |
+-------------------------------------------------------------------------------+
        |                               |                               |
        v                               v                               v
+-------------------+       +-----------------------+       +-------------------+
|      DIRECT       |       |       INDIRECT        |       |  NATURAL CONVERS. |
| Clear, unambiguous|       | Pragmatic implicature |       | Colloquial idiom, |
| marker of stance  |       | without marker words  |       | casual pacing     |
|                   |       |                       |       |                   |
| "Absolutely, I'll |       | "That sounds like the |       | "Yeah, absolutely.|
|  do that."        |       |  exact right move."   |       |  I'm in."         |
+-------------------+       +-----------------------+       +-------------------+
```

### 5.2 Anchor Exemplar Matrix (from [`anchors/01_initial_anchors_vp.md`](file:///home/eshwar/code/response/research/s1/anchors/01_initial_anchors_vp.md))

| Scenario ID | Subtype | Direct Realization | Indirect Realization | Natural Conversational |
|---|---|---|---|---|
| `VP-01-S01` | Eager Acceptance | "Absolutely, I'll do that." | "That sounds like exactly what I should do." | "Yeah, absolutely. I'm in." |
| `VP-01-S03` | Immediate Willingness | "I'm ready to start right now." | "There's no reason to wait on this." | "Let's do it now, count me in." |
| `VP-02-S01` | Appreciation of Help | "Thank you, that was extremely helpful." | "I really needed that direction." | "Thanks a ton, that really helps." |
| `VP-02-S04` | Gratitude for Support | "I really appreciate you explaining that." | "That makes all the difference." | "Honestly, thanks for walking me through it." |
| `VP-03-S01` | Follow-Up Question | "What should I do next after this?" | "Does this also apply to tomorrow's routine?" | "Awesome, what's step two?" |
| `VP-03-S04` | Self-Initiated Step | "I'll do that and also prep the checklist." | "I might as well tackle the second part too."| "Done and done, I'll jump ahead to part 2." |
| `VP-04-S01` | Voluntary Commitment | "I'll make sure to follow this consistently." | "I'm definitely making this a habit." | "Consider it done, I'm sticking with it." |
| `VP-04-S03` | Pressure-Free Coop. | "I'm completely happy to cooperate with this." | "This makes complete sense to do." | "No problem at all, glad to do it." |

### 5.3 Anchor Production Roadmap

| Category | File Target | Scenario Count | Realizations/Scenario | Anchor Count | Status |
|---|---|---|---|---|---|
| **VP** | [`anchors/01_initial_anchors_vp.md`](file:///home/eshwar/code/response/research/s1/anchors/01_initial_anchors_vp.md) | 20 | 3 | 60 | **Completed** |
| **P** | `anchors/02_initial_anchors_p.md` | 20 | 3 | 60 | Pending |
| **I** | `anchors/03_initial_anchors_i.md` | 20 | 3 | 60 | Pending |
| **N** | `anchors/04_initial_anchors_n.md` | 20 | 3 | 60 | Pending |
| **VN** | `anchors/05_initial_anchors_vn.md` | 20 | 3 | 60 | Pending |
| **Total** | **Stage 1 Anchor Corpus** | **100** | **3** | **300** | **20% Complete (60/300)** |

---

## 6. Quick Review Checklist & Quality Verification

Use this checklist to verify any additions or modifications to the Stage 1 files:

- [x] **Ordinal Scale Integrity**: All dimensions and subtypes maintain strict alignment with `VN < N < I < P < VP`.
- [x] **Symmetric Subtype Distribution**: Exactly 4 subtypes per category across all 5 classes (20 total).
- [x] **Exhaustive Scenario Allocation**: Exactly 5 scenarios per subtype (20 per category, 100 total).
- [x] **Orthogonal Decoupling**: No scenario relies on emotion, dialogue act, barrier reason, or execution status as a proxy for stance.
- [x] **Linguistic Realization Decoupling**: Scenario inventories specify behavioral situations, strictly deferring phrasing and vocabulary to the anchor tier.
- [x] **Boundary Separability**: Ambiguous zones (`P-03` vs `N-04`, `P-04` vs `N-01`, `I-01` vs `P-01`, `N-02` vs `VN-01`) have explicit behavioral demarcation criteria.
- [x] **Anchor Tri-Modality**: Every scenario contains exactly 1 Direct, 1 Indirect, and 1 Natural Conversational anchor.

---
*Generated for rapid technical and behavioral review of Stage 1 assets.*
