
# 02_RESPONSE_P.md

**Document ID:** RESPONSE_P  
**Category:** Positive Response (P)  
**Ontology Module:** User Response Categories  
**Ontology Version:** v1.0  
**Simulator Version:** v1.0  
**Status:** Draft (Pending Ontology Lock)

---

# 1. Purpose

This document formally specifies the **Positive Response (P)** category within the semantic ontology. It defines the behavioral conditions under which a user's natural language response should be mapped to the **Positive (P)** response variable in the RL simulator.

The specification is intended for:

- Manual annotation
- Dataset construction
- Dialogue simulation
- LLM-based response classification
- Simulator implementation
- Evaluation

This document shall be interpreted together with **README.md** and **00_ONTOLOGY_GUIDELINES.md**.

---

# 2. Formal Definition

A **Positive Response (P)** is a latent behavioral outcome indicating that the user **accepts or cooperates with the agent's intervention** while exhibiting **little or no explicit enthusiasm**.

The defining characteristic of **P** is **cooperative acceptance**, without the strong appreciation or engagement required for **Very Positive (VP)**.

Formally,

\[
P = Acceptance + Cooperation + Low\ Resistance
\]

Unlike VP, positive affect is optional rather than defining.

---

# 3. Behavioral Interpretation

A Positive response reflects one or more of the following:

- Acceptance of the recommendation
- Willingness to comply
- Cooperative interaction
- Mild appreciation
- Low psychological reactance
- Readiness to continue the conversation

The user agrees with the intervention but does not strongly reinforce or celebrate it.

---

# 4. Conversational Intent

Typical communicative objectives include:

- Agreeing
- Confirming
- Accepting advice
- Acknowledging the recommendation
- Committing to perform the task
- Cooperating with the interaction

The user is behaviorally aligned with the agent but without exceptional enthusiasm.

---

# 5. Inclusion Criteria

Assign **P** when most of the following hold:

- Recommendation is accepted.
- User indicates willingness to cooperate.
- No significant resistance is expressed.
- Emotional intensity is low or moderate.
- Appreciation, if present, appears routine rather than enthusiastic.

---

# 6. Exclusion Criteria

Do **not** assign P when:

- The user expresses strong enthusiasm or appreciation (→ VP).
- The response is neutral or merely acknowledges the message (→ I).
- Agreement is reluctant or accompanied by irritation (→ N).
- The recommendation is explicitly rejected (→ N or VN).

---

# 7. Decision Rules

Assign **P** when:

1. The recommendation is accepted.
2. Cooperation is evident.
3. No meaningful resistance exists.
4. Enthusiasm is absent or modest.

If strong appreciation and proactive engagement are present, assign **VP**.

---

# 8. Linguistic Realizations

## Direct Agreement

- "Okay."
- "Sure."
- "I'll do it."
- "Sounds good."
- "Alright."

## Commitment

- "I'll take care of it."
- "I'll finish it later today."
- "I'll remember."

## Polite Acceptance

- "Thanks, I'll do that."
- "Okay, thank you."
- "Sounds reasonable."

## Mild Appreciation

- "That helps."
- "Good suggestion."
- "I appreciate the reminder."

## Implicit Cooperation

- User begins discussing how they will complete the task.
- User asks a clarification question before proceeding.

---

# 9. Confusable Categories

## P vs VP

**P**

- Acceptance
- Cooperation
- Mild appreciation

**VP**

- Acceptance
- Strong appreciation
- High enthusiasm
- Active engagement

---

## P vs I

Indifferent responses acknowledge the interaction without demonstrating commitment.

Example:

"I see."

→ Indifferent

"I'll do it."

→ Positive

---

## P vs N

Example:

"I'll do it, but stop reminding me."

The negative component introduces resistance.

This should generally not be classified as P.

---

# 10. Boundary Conditions

## Conventional Gratitude

Many users habitually say "Thank you."

Do not interpret routine politeness as VP.

---

## Delayed Compliance

"I'll do it this evening."

Still represents acceptance.

Assign **P** unless reluctance dominates.

---

## Conditional Agreement

"I'll do it if I have time."

Requires context.

If commitment is weak or uncertain, consider **Indifferent (I)**.

---

# 11. Difficult Cases

| Example | Recommended Label | Reason |
|----------|-------------------|--------|
| "Okay." | P | Direct acceptance |
| "Sure." | P | Cooperative agreement |
| "Thanks." | P / VP | Depends on enthusiasm |
| "I'll try." | I or P | Depends on commitment strength |
| "Fine." | P / N | Depends on dialogue context |

---

# 12. Annotation Guidelines

Annotators should determine:

1. Has the recommendation been accepted?
2. Is the commitment genuine?
3. Is resistance absent?
4. Is enthusiasm limited?

If the answer to all is yes, assign **P**.

When uncertain, compare the response against neighboring categories (**VP**, **I**, **N**) before making the final decision.

---

# 13. Simulator Notes

Within the simulator:

- **P** represents successful persuasion without strong emotional reinforcement.
- Numerous linguistic realizations may correspond to the same behavioral outcome.
- Non-verbal cooperation (e.g., immediate task initiation) may strengthen confidence but is not required.

---

# 14. Future LLM Classifier Notes

A classifier should prioritize:

- Acceptance of the recommendation
- Behavioral commitment
- Cooperative intent
- Absence of reactance

Avoid using words such as "okay" or "thanks" as deterministic indicators.

Dialogue context should always be considered.

---

# 15. Literature Notes

The semantic interpretation is informed by:

- Conversation Analysis
- Dialogue Systems
- Speech Act Theory
- Dialogue Act Taxonomies
- Human–Robot Interaction
- Persuasion Research

These references motivate the behavioral interpretation while the simulator ontology remains the authoritative classification framework.

---

# 16. Summary

## Core Definition

A Positive Response represents cooperative acceptance of the intervention without the high enthusiasm required for the Very Positive category.

## Required Characteristics

- Acceptance
- Cooperation
- Behavioral commitment
- Low resistance

## Insufficient Evidence Alone

- "Thanks"
- "Okay"
- Positive wording without commitment
- General positive mood unrelated to the intervention

---

# 17. Relationship to Other Categories

| Category | Key Difference |
|----------|----------------|
| VP | Adds strong appreciation and enthusiastic engagement |
| I | Lacks clear behavioral commitment |
| N | Introduces reluctance or resistance |
| VN | Represents explicit rejection and strong reactance |

---

# 18. Status

**Status:** Draft

This specification defines the second-highest behavioral outcome on the simulator's ordinal response scale:

VN < N < I < **P** < VP

Subsequent response specifications shall remain consistent with this semantic boundary.
