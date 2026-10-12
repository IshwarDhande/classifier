
# 01_RESPONSE_VP.md

**Category:** Very Positive Response (VP)  
**Ontology Module:** User Response Categories  
**Version:** 1.0  
**Status:** Draft (Pending Ontology Lock)

---

# 1. Purpose

This document formally specifies the **Very Positive Response (VP)** category used by the RL simulator. It operationalizes the abstract simulator variable into deterministic semantic criteria suitable for:

- Manual annotation
- Synthetic dialogue generation
- LLM-based classification
- Simulator implementation
- Evaluation

This document shall be interpreted together with **README.md** and **00_ONTOLOGY_GUIDELINES.md**.

---

# 2. Formal Definition

A **Very Positive Response (VP)** is a latent behavioral outcome indicating that the user reacts to the agent's intervention with **strong acceptance, high engagement, explicit appreciation, and negligible psychological resistance**.

The defining property is **enthusiastic cooperation**, not merely agreement.

---

# 3. Behavioral Interpretation

A VP response reflects one or more of the following behavioral states:

- Strong acceptance
- High willingness to comply
- Appreciation toward the intervention
- Trust in the agent
- Positive reinforcement of future interaction
- Voluntary engagement beyond the minimum required

The response indicates that the intervention was perceived as genuinely useful or motivating.

---

# 4. Conversational Intent

Typical communicative intents include:

- Express gratitude
- Reinforce agreement
- Encourage continued interaction
- Acknowledge usefulness
- Signal intrinsic motivation

---

# 5. Inclusion Criteria

Assign **VP** when most of the following are present:

- Explicit acceptance of the recommendation.
- Positive affect directed toward the recommendation or the agent.
- No observable reluctance or reactance.
- Evidence of enthusiasm or appreciation.
- Active engagement (e.g., asking follow-up questions, volunteering to continue).

---

# 6. Exclusion Criteria

Do **not** assign VP when:

- Agreement is merely neutral ("Okay.", "Sure.")
- Compliance is reluctant ("Fine, I'll do it.")
- Gratitude is purely conventional without evidence of enthusiasm.
- Positive emotion is unrelated to the intervention.
- The user complies while expressing annoyance.

These cases generally belong to **Positive (P)** or **Negative (N)** depending on context.

---

# 7. Decision Rules

Decision logic:

1. Was the recommendation accepted?
2. Is there explicit appreciation or enthusiasm?
3. Is resistance absent?
4. Does the response go beyond minimal compliance?

Only if all major conditions hold should VP be assigned.

---

# 8. Linguistic Realizations

## Strong Acceptance

- "Absolutely!"
- "Definitely!"
- "Of course!"
- "You're right!"

## Appreciation

- "Thank you so much."
- "That really helped."
- "I'm glad you reminded me."

## Acceptance + Commitment

- "I'll start immediately."
- "Thanks, I'll take care of it now."

## Continued Engagement

- "Anything else I should do?"
- "Can you help me plan the next step?"

## Implicit VP

- User immediately begins the task.
- User proactively asks for additional advice.

---

# 9. Confusable Categories

## VP vs Positive (P)

Positive:
- Acceptance without enthusiasm.

Very Positive:
- Acceptance accompanied by appreciation and high engagement.

---

## VP vs Indifferent (I)

Indifferent:
- Minimal acknowledgement.

VP:
- Clear emotional investment.

---

## VP vs Compliance Under Pressure

Example:

> "Fine, I'll do it."

This is **not VP** because compliance is accompanied by reluctance.

---

# 10. Boundary Conditions

## Mixed Response

> "Thanks, but don't remind me again."

Positive appreciation and negative resistance coexist.

Dominant behavioral outcome should determine the final label.

---

## Sarcasm

Literal wording must never override pragmatic interpretation.

Dialogue history should be considered.

---

## Habitual Politeness

Many users say "Thanks" automatically.

Gratitude alone is insufficient for VP.

---

# 11. Difficult Cases

| Example | Recommended Label | Reason |
|---------|-------------------|--------|
| "Thanks." | P or VP | Depends on enthusiasm and context |
| "You're right." | P | Agreement only |
| "Awesome!" | VP | Strong positive engagement if directed at intervention |
| "Haha, thanks!" | Context | Could be genuine or sarcastic |

---

# 12. Annotation Guidelines

Annotators should follow this sequence:

1. Infer behavioral state.
2. Ignore keywords in isolation.
3. Evaluate appreciation.
4. Evaluate willingness.
5. Check for resistance.
6. Assign exactly one response category.

When uncertain, prefer dialogue context over isolated utterances.

---

# 13. Simulator Notes

Simulator semantics:

- VP is a **behavioral outcome**, not a sentiment label.
- Multiple utterances may map to the same VP state.
- Non-verbal evidence (if available) may increase confidence but is not required.

---

# 14. Future LLM Classifier Notes

Future classifiers should prioritize:

- Behavioral commitment
- Psychological acceptance
- Appreciation toward the intervention
- Absence of reactance
- Multi-turn conversational context

The model should avoid keyword-based classification.

---

# 15. Literature Notes

Conceptually related work includes:

- Conversation Analysis
- Speech Act Theory
- Dialogue Act Taxonomies (DAMSL, ISO 24617-2)
- Psychological Reactance Theory
- Human–Robot Interaction
- Persuasion Research

These provide theoretical grounding while the simulator ontology remains authoritative.

---

# 16. Summary

**Core Definition**

A Very Positive Response represents enthusiastic behavioral acceptance of the agent's intervention, characterized by appreciation, engagement, and minimal resistance.

**Required Characteristics**

- Acceptance
- Appreciation
- Positive engagement
- No meaningful resistance

**Insufficient Evidence Alone**

- "Thanks"
- "Okay"
- "Sure"
- Positive wording without behavioral acceptance

---

# 17. Status

**Status:** Draft

This specification establishes the upper semantic boundary of the simulator's ordinal response scale:

VN < N < I < P < **VP**

Subsequent response categories shall remain consistent with this boundary.
