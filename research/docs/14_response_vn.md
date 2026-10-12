
# 05_RESPONSE_VN.md

**Document ID:** RESPONSE_VN  
**Category:** Very Negative Response (VN)  
**Ontology Module:** User Response Categories  
**Ontology Version:** v1.0  
**Simulator Version:** v1.0  
**Status:** Draft (Pending Ontology Lock)

---

# 1. Purpose

This document formally specifies the **Very Negative Response (VN)** category within the semantic ontology. It provides a rigorous semantic definition for mapping free-form natural language responses to the **Very Negative (VN)** behavioral outcome used by the Reinforcement Learning (RL) simulator.

This specification supports:

- Manual annotation
- Dialogue simulation
- Dataset construction
- LLM-based behavioral classification
- Simulator implementation
- Evaluation and reproducible research

This document shall be interpreted together with **README.md** and **00_ONTOLOGY_GUIDELINES.md**.

---

# 2. Formal Definition

A **Very Negative Response (VN)** is a latent behavioral outcome indicating **strong rejection of the agent's intervention**, characterized by explicit opposition, high psychological reactance, hostility, or active disengagement from the interaction.

The defining characteristic of VN is **active behavioral rejection**, not merely disagreement or reluctance.

Formally,

\[
VN = Strong\ Rejection + High\ Reactance + Minimal\ Cooperation
\]

VN represents the lowest behavioral state on the simulator's ordinal response scale.

---

# 3. Behavioral Interpretation

A Very Negative response reflects one or more of the following latent behavioral states:

- Explicit refusal
- Strong resistance
- Hostility toward the intervention
- Hostility toward the agent
- Psychological reactance
- Desire to terminate the interaction
- Refusal of future cooperation
- Breakdown of conversational alignment

Unlike **Negative (N)**, the interaction is no longer merely resistant—it has become actively adversarial or strongly rejecting.

---

# 4. Conversational Intent

Typical communicative intentions include:

- Rejecting the recommendation
- Rejecting the persuasive attempt
- Rejecting future interaction
- Expressing anger or frustration
- Discouraging further reminders
- Terminating the conversation
- Demonstrating loss of trust

---

# 5. Inclusion Criteria

Assign **Very Negative (VN)** when most of the following conditions are present:

- Explicit rejection of the recommendation.
- Strong psychological resistance.
- High negative affect directed toward the intervention or the agent.
- Active disengagement or conversation termination.
- Minimal or no willingness to cooperate.

Representative examples:

- "No. I'm not doing it."
- "Leave me alone."
- "Stop bothering me."
- "I don't want your help."
- "Never remind me again."

---

# 6. Exclusion Criteria

Do **not** assign VN when:

- The user merely hesitates (→ I).
- The user expresses mild reluctance (→ N).
- The user disagrees politely without hostility (→ N).
- The user accepts the recommendation despite frustration (→ P or N depending on dominant behavior).

---

# 7. Decision Rules

Assign **VN** when all major behavioral evidence indicates:

1. Explicit rejection.
2. Strong reactance or hostility.
3. Minimal behavioral commitment.
4. Active opposition to the intervention or interaction.

If rejection is absent, VN should not be assigned.

If cooperation remains plausible through additional dialogue, consider **Negative (N)** instead.

---

# 8. Linguistic Realizations

## Explicit Rejection

- "No."
- "Absolutely not."
- "I'm not doing that."
- "Forget it."

---

## Hostile Responses

- "Leave me alone."
- "Stop bothering me."
- "You're annoying."
- "Go away."

---

## Strong Frustration

- "I've had enough."
- "Stop asking."
- "Quit reminding me."

---

## Interaction Termination

- "End this conversation."
- "Don't talk to me anymore."
- "I don't want to hear this."

---

## Rejection of Future Assistance

- "Never remind me again."
- "I don't need your advice."
- "Stay out of it."

---

# 9. Confusable Categories

## VN vs N

**Negative (N)**

- Reluctance
- Mild annoyance
- Recoverable interaction

**Very Negative (VN)**

- Explicit rejection
- Hostility
- High reactance
- Active disengagement

---

## VN vs I

Indifferent reflects uncertainty.

VN reflects deliberate rejection.

---

## VN vs P

Statements such as

> "I'll do it, but stop talking."

contain both compliance and rejection.

Behavioral dominance determines the final category.

---

# 10. Boundary Conditions

## Mixed Response

Example:

> "Thanks, but leave me alone."

Although gratitude is present, the dominant behavioral outcome is interaction rejection.

Recommended label:

**VN**

---

## Sarcasm

Example:

> "Oh, thanks a lot."

Literal wording should never determine classification.

Behavioral intent inferred from dialogue context should dominate.

---

## Emotional Outburst

The user may express temporary frustration without rejecting the recommendation.

If cooperation remains likely, classify as **Negative (N)** rather than VN.

---

## Silence

Silence should never automatically be interpreted as Very Negative.

Simulator policy should determine the treatment of non-response.

---

# 11. Difficult Cases

| Example | Recommended Label | Reason |
|----------|-------------------|--------|
| "Leave me alone." | VN | Explicit rejection |
| "Stop reminding me." | N / VN | Depends on hostility and intensity |
| "Go away." | VN | Interaction termination |
| "I don't care." | I / VN | Context dependent |
| "No." | N / VN | Depends on dialogue history and strength |

---

# 12. Annotation Guidelines

Annotators should determine:

1. Has the recommendation been explicitly rejected?
2. Is strong behavioral resistance present?
3. Is hostility directed toward the intervention or agent?
4. Has the user attempted to terminate the interaction?
5. Is future cooperation unlikely without substantial intervention?

If the answer to most questions is **Yes**, assign **Very Negative (VN)**.

Dialogue history should always be considered before assigning VN.

---

# 13. Simulator Notes

Within the simulator:

- VN represents the lowest behavioral outcome.
- It corresponds to strong persuasion failure.
- Future persuasion remains theoretically possible but is substantially less likely than from N.
- Multiple linguistic realizations map to the same behavioral state.

---

# 14. Future LLM Classifier Notes

Future classifiers should prioritize:

- Explicit rejection
- Psychological reactance
- Hostility
- Interaction termination
- Refusal of future cooperation

The classifier should avoid relying solely on negative lexical items.

Behavioral interpretation and dialogue context should dominate the classification process.

---

# 15. Literature Notes

The semantic interpretation is informed by:

- Psychological Reactance Theory
- Conversation Analysis
- Dialogue Systems
- Human–Robot Interaction
- Persuasion Research
- Speech Act Theory

These works motivate the semantic interpretation while the simulator ontology remains the authoritative behavioral representation.

---

# 16. Summary

## Core Definition

A Very Negative Response represents explicit behavioral rejection of the intervention, characterized by hostility, high reactance, and active disengagement.

## Required Characteristics

- Explicit rejection
- Strong resistance
- High reactance
- Minimal cooperation

## Insufficient Evidence Alone

- Mild annoyance
- Temporary frustration
- Uncertainty
- Clarification requests
- General negative mood unrelated to the intervention

---

# 17. Relationship to Other Categories

| Category | Primary Difference |
|-----------|--------------------|
| VP | Strong acceptance and enthusiasm |
| P | Cooperative acceptance |
| I | No clear behavioral commitment |
| N | Recoverable resistance |
| VN | Explicit rejection and interaction breakdown |

VN defines the lower semantic boundary of the simulator's ordinal response scale.

---

# 18. Status

**Status:** Draft

This specification establishes the lowest behavioral state in the simulator's response ontology:

**VN < N < I < P < VP**

All subsequent ontology components shall remain consistent with this boundary.
