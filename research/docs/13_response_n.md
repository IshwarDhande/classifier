
# 04_RESPONSE_N.md

**Document ID:** RESPONSE_N  
**Category:** Negative Response (N)  
**Ontology Module:** User Response Categories  
**Ontology Version:** v1.0  
**Simulator Version:** v1.0  
**Status:** Draft (Pending Ontology Lock)

---

# 1. Purpose

This document formally specifies the **Negative Response (N)** category used by the semantic ontology. It defines the behavioral conditions under which a user's natural language response should be mapped to the **Negative (N)** outcome in the RL simulator.

This specification supports:

- Manual annotation
- Dataset construction
- Dialogue simulation
- LLM-based response classification
- Simulator implementation
- Evaluation

This document shall be interpreted together with **README.md** and **00_ONTOLOGY_GUIDELINES.md**.

---

# 2. Formal Definition

A **Negative Response (N)** is a latent behavioral outcome indicating that the user exhibits **behavioral resistance, reluctance, disagreement, or reduced willingness** toward the agent's intervention, while **not reaching the level of explicit hostility or strong rejection** required for the **Very Negative (VN)** category.

Formally,

\[
N = Resistance + Low\ Cooperation + Moderate\ Reactance
\]

Unlike **VN**, the interaction remains recoverable through subsequent dialogue.

---

# 3. Behavioral Interpretation

A Negative response may reflect:

- reluctance
- disagreement
- mild frustration
- annoyance
- hesitation due to resistance
- reduced trust
- unwillingness to cooperate immediately

The user is moving away from cooperation but has not completely rejected the interaction.

---

# 4. Conversational Intent

Typical communicative intentions include:

- expressing disagreement
- resisting persuasion
- postponing due to unwillingness
- questioning the recommendation
- discouraging further persuasion
- expressing mild irritation

---

# 5. Inclusion Criteria

Assign **N** when one or more of the following dominate:

- Explicit reluctance
- Mild refusal
- Behavioral resistance
- Annoyance without hostility
- Weak commitment accompanied by negative attitude
- Desire to avoid the recommendation

Examples:

- "I don't feel like it."
- "Not now."
- "I'd rather not."
- "Please stop reminding me."
- "I don't think that's necessary."

---

# 6. Exclusion Criteria

Do **not** assign **N** when:

- The recommendation is accepted (→ P or VP).
- The user remains genuinely undecided without resistance (→ I).
- The user displays explicit hostility, abuse, or complete rejection (→ VN).

---

# 7. Decision Rules

Assign **N** when:

1. Behavioral resistance is present.
2. Cooperation is weak or absent.
3. Explicit hostility is absent.
4. The interaction appears recoverable.

If strong rejection dominates, classify as **VN**.

---

# 8. Linguistic Realizations

## Mild Refusal

- "Not now."
- "Maybe later."
- "I'd rather not."

## Disagreement

- "I don't agree."
- "I don't think that's a good idea."
- "That doesn't make sense to me."

## Mild Annoyance

- "You keep reminding me."
- "That's getting annoying."
- "Please stop asking."

## Conditional Resistance

- "Only if I have to."
- "I'll do it eventually."

## Passive Resistance

- "I'm too busy."
- "I don't have time."

---

# 9. Confusable Categories

## N vs I

**Indifferent (I)**

- uncertain
- non-committal
- neutral

**Negative (N)**

- reluctant
- resistant
- mildly opposed

---

## N vs VN

**Negative**

- recoverable interaction
- mild annoyance
- reluctance

**Very Negative**

- explicit rejection
- hostility
- strong reactance
- interaction breakdown

---

## N vs P

"I'll do it, but stop reminding me."

Behavior includes compliance and resistance.

The dominant behavioral state determines the final label.

---

# 10. Boundary Conditions

## Delayed Compliance

"I'll do it later."

If delay reflects scheduling constraints, consider **P**.

If delay reflects unwillingness, classify as **N**.

---

## Information Seeking

Questions alone do not imply resistance.

Resistance must be behaviorally evident.

---

## Emotional Frustration

"I'm exhausted today."

This is not automatically **N** unless directed toward the intervention.

---

# 11. Difficult Cases

| Example | Recommended Label | Reason |
|----------|-------------------|--------|
| "Not now." | N | Temporary resistance |
| "Maybe later." | I / N | Context dependent |
| "Fine." | P / N | Depends on reluctance |
| "Please stop." | N / VN | Depends on intensity |
| "I don't want to." | N | Clear resistance |

---

# 12. Annotation Guidelines

Annotators should determine:

1. Is the recommendation resisted?
2. Is the resistance explicit?
3. Is hostility absent?
4. Could future persuasion reasonably succeed?

If yes, assign **Negative (N)**.

When uncertain, compare with neighboring categories (**I** and **VN**) before final assignment.

---

# 13. Simulator Notes

Within the simulator:

- **N** represents partial persuasion failure rather than complete failure.
- Future interventions may still change the user's behavioral state.
- The category captures recoverable resistance.

---

# 14. Future LLM Classifier Notes

The classifier should prioritize:

- resistance
- reluctance
- disagreement
- reduced willingness
- mild reactance

The classifier should distinguish:

- uncertainty (I)
- reluctance (N)
- hostility (VN)

using dialogue context rather than isolated phrases.

---

# 15. Literature Notes

The interpretation is informed by:

- Psychological Reactance Theory
- Conversation Analysis
- Dialogue Systems
- Human–Robot Interaction
- Persuasion Research
- Speech Act Theory

The simulator ontology remains the authoritative semantic framework.

---

# 16. Summary

## Core Definition

A Negative Response represents behavioral resistance toward the intervention without escalating to explicit rejection or hostility.

## Required Characteristics

- Resistance
- Reluctance
- Reduced cooperation
- Recoverable interaction

## Insufficient Evidence Alone

- Neutral uncertainty
- Clarification requests
- General negative mood unrelated to the intervention

---

# 17. Relationship to Other Categories

| Category | Primary Difference |
|-----------|--------------------|
| VP | Strong acceptance and enthusiasm |
| P | Cooperative acceptance |
| I | No clear acceptance or resistance |
| VN | Explicit rejection and strong reactance |

Negative occupies the second-lowest position on the simulator's ordinal response scale.

---

# 18. Status

**Status:** Draft

This specification defines the behavioral state immediately above **Very Negative**:

VN < **N** < I < P < VP

Future revisions should preserve this semantic boundary.
