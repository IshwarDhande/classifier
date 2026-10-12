# Response Category — Lexical & Semantic Variation Bank

## 1. Purpose

This document expands the original Short Reply Robustness Corpus (SRCC) into a reusable **master expression bank** for the frozen Response Category classifier.

The original SRCC contains:

- 5 Response Categories
- 3 length bands
- 20 expressions per category × length band
- 300 total expressions

This bank is a larger controlled resource from which future SRCC/training/validation/test subsets can be constructed.

The goal is not to create arbitrary synonyms. The goal is to build **controlled lexical and semantic variation families** around stable Response Category anchors.

---

# 2. Frozen Response Category Ontology

| Code | Category | Core meaning |
|---|---|---|
| `VP` | Very Positive | Strong acceptance, enthusiasm, appreciation, or eager willingness |
| `P` | Positive | Ordinary acceptance, cooperation, willingness, or mild agreement |
| `I` | Indifferent | Neutral acknowledgment, non-commitment, uncertainty, no preference, or low engagement |
| `N` | Negative | Reluctance, mild refusal, resistance, disagreement, or mild dissatisfaction |
| `VN` | Very Negative | Strong refusal, rejection, resistance, hostility, or strong dissatisfaction |

No additional category is introduced.

---

# 3. Core Construction Principle

Each expression in the bank should have:

1. A stable intended Response Category.
2. A semantic family.
3. A lexical anchor.
4. A controlled variation type.
5. A confidence assessment.

The bank must not intentionally use the same expression under multiple categories.

Expressions whose meaning cannot be reliably determined in the standalone setting should be marked **AMBIGUOUS/EXCLUDE**, rather than forced into a category.

---

# 4. Variation Hierarchy

The bank uses three levels.

## Level 1 — Direct lexical anchors

High-frequency expressions with a strong category signal.

Example:

```text
Absolutely. → VP
Yes.        → P
Maybe.      → I
No.         → N
Never.      → VN
```

## Level 2 — Controlled lexical/syntactic variants

Small variations around the same anchor.

Example:

```text
Absolutely.
Absolutely yes.
Yes, absolutely.
Absolutely, I agree.
```

## Level 3 — Broader semantic expressions

Expressions that convey the same behavioral state without repeating the anchor word.

Example:

```text
I'd be very happy to. → VP
That works for me.   → P
I have no preference. → I
I'd rather not.      → N
I strongly object.    → VN
```

Level 3 expressions require stricter semantic review.

---

# 5. VP — Very Positive

## 5.1 Semantic families

1. Strong agreement
2. Strong acceptance
3. Enthusiasm
4. Eager willingness
5. Strong appreciation/satisfaction

---

## 5.2 Strong Agreement — anchor: ABSOLUTELY

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | Absolutely. | Strong agreement | High |
| 2 | Absolutely yes. | Strong agreement | High |
| 3 | Yes, absolutely. | Strong agreement | High |
| 4 | Absolutely, I agree. | Strong agreement | High |
| 5 | I absolutely agree. | Strong agreement | High |
| 6 | Absolutely, yes. | Strong agreement | High |
| 7 | Completely agree. | Strong agreement | High |
| 8 | I strongly agree. | Strong agreement | High |
| 9 | Totally agree. | Strong agreement | High |
| 10 | I totally agree. | Strong agreement | High |

---

## 5.3 Strong Acceptance — anchor: YES

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | Yes! | Strong acceptance | High |
| 2 | Yes, definitely. | Strong acceptance | High |
| 3 | Yes, of course. | Strong acceptance | High |
| 4 | Definitely yes. | Strong acceptance | High |
| 5 | Definitely. | Strong acceptance | High |
| 6 | Certainly. | Strong acceptance | High |
| 7 | Certainly yes. | Strong acceptance | High |
| 8 | Without a doubt. | Strong acceptance | Medium |
| 9 | For sure! | Strong acceptance | High |
| 10 | Definitely, yes. | Strong acceptance | High |

---

## 5.4 Enthusiasm — anchor: GREAT

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | Great! | Enthusiasm | High |
| 2 | Excellent! | Enthusiasm | High |
| 3 | Fantastic! | Enthusiasm | High |
| 4 | Wonderful! | Enthusiasm | High |
| 5 | Amazing! | Enthusiasm | High |
| 6 | Perfect! | Enthusiasm | High |
| 7 | Sounds excellent. | Enthusiasm | High |
| 8 | That sounds great. | Enthusiasm | High |
| 9 | That's fantastic. | Enthusiasm | High |
| 10 | That's wonderful. | Enthusiasm | High |

---

## 5.5 Eager Willingness — anchor: GLADLY

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | Gladly. | Eager willingness | High |
| 2 | Happily. | Eager willingness | High |
| 3 | I'd love to. | Eager willingness | High |
| 4 | I'd be happy to. | Eager willingness | High |
| 5 | Happy to help. | Eager willingness | High |
| 6 | I'd gladly do it. | Eager willingness | High |
| 7 | I'd be glad to. | Eager willingness | High |
| 8 | I'm happy to. | Eager willingness | High |
| 9 | I'm very willing. | Eager willingness | Medium |
| 10 | I'd be delighted. | Eager willingness | High |

---

## 5.6 Strong Appreciation/Satisfaction

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | Love it! | Appreciation | High |
| 2 | I love it. | Appreciation | High |
| 3 | I really like it. | Appreciation | High |
| 4 | I absolutely love it. | Appreciation | High |
| 5 | I really appreciate it. | Appreciation | High |
| 6 | Much appreciated! | Appreciation | High |
| 7 | That's excellent. | Satisfaction | High |
| 8 | That's perfect. | Satisfaction | High |
| 9 | I'm very pleased. | Satisfaction | High |
| 10 | I'm delighted. | Satisfaction | High |

---

# 6. P — Positive

## 6.1 Semantic families

1. Ordinary agreement
2. Acceptance
3. Cooperation
4. Willingness
5. Mild satisfaction

---

## 6.2 Agreement — anchor: AGREE

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | Agree. | Agreement | High |
| 2 | I agree. | Agreement | High |
| 3 | Yes. | Agreement | High |
| 4 | Yes, I agree. | Agreement | High |
| 5 | That works. | Agreement | High |
| 6 | Works for me. | Agreement | High |
| 7 | That sounds good. | Agreement | High |
| 8 | Sounds good. | Agreement | High |
| 9 | Good point. | Agreement | Medium |
| 10 | I think so. | Agreement | Medium |

---

## 6.3 Acceptance — anchor: SURE

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | Sure. | Acceptance | High |
| 2 | Sure thing. | Acceptance | High |
| 3 | Yes, sure. | Acceptance | High |
| 4 | Sure, okay. | Acceptance | High |
| 5 | Okay, sure. | Acceptance | Medium |
| 6 | That's fine. | Acceptance | High |
| 7 | Fine by me. | Acceptance | High |
| 8 | That's okay. | Acceptance | High |
| 9 | Okay with me. | Acceptance | High |
| 10 | I'm okay with that. | Acceptance | High |

---

## 6.4 Cooperation — anchor: OKAY

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | Okay. | Cooperation | Medium |
| 2 | Okay, I'll do it. | Cooperation | High |
| 3 | Okay, I can. | Cooperation | High |
| 4 | I can do that. | Cooperation | High |
| 5 | I'll do that. | Cooperation | High |
| 6 | I can help. | Cooperation | High |
| 7 | I can do it. | Cooperation | High |
| 8 | I'll help. | Cooperation | High |
| 9 | That should work. | Cooperation | High |
| 10 | I can manage that. | Cooperation | High |

---

## 6.5 Willingness — anchor: WILLING

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | Willing. | Willingness | High |
| 2 | I'm willing. | Willingness | High |
| 3 | I'm willing to. | Willingness | High |
| 4 | I'd be willing. | Willingness | High |
| 5 | I'd be willing to. | Willingness | High |
| 6 | I don't mind. | Willingness | Medium |
| 7 | I can do that. | Willingness | High |
| 8 | I'd do that. | Willingness | High |
| 9 | That's acceptable. | Willingness | High |
| 10 | I'm fine with that. | Willingness | High |

---

## 6.6 Mild Satisfaction

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | Good. | Satisfaction | Medium |
| 2 | Nice. | Satisfaction | High |
| 3 | Fine. | Satisfaction | Medium |
| 4 | Sounds good. | Satisfaction | High |
| 5 | Looks good. | Satisfaction | High |
| 6 | That's good. | Satisfaction | High |
| 7 | That's nice. | Satisfaction | High |
| 8 | Pretty good. | Satisfaction | High |
| 9 | Seems good. | Satisfaction | High |
| 10 | I'm satisfied. | Satisfaction | High |

---

# 7. I — Indifferent

## 7.1 Semantic families

1. Neutral acknowledgment
2. Uncertainty
3. Non-commitment
4. No preference
5. Low engagement

---

## 7.2 Neutral Acknowledgment

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | Okay. | Neutral acknowledgment | Medium |
| 2 | Alright. | Neutral acknowledgment | Medium |
| 3 | I see. | Neutral acknowledgment | High |
| 4 | Understood. | Neutral acknowledgment | High |
| 5 | Noted. | Neutral acknowledgment | High |
| 6 | Right. | Neutral acknowledgment | Medium |
| 7 | Sure. | Neutral acknowledgment | Low |
| 8 | Fine. | Neutral acknowledgment | Low |
| 9 | Got it. | Neutral acknowledgment | High |
| 10 | Understood, thanks. | Neutral acknowledgment | High |

**Note:** `Okay`, `Sure`, and `Fine` are context-sensitive and should normally be excluded from a high-confidence standalone training subset unless the experiment deliberately fixes their mapping.

---

## 7.3 Uncertainty — anchor: MAYBE

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | Maybe. | Uncertainty | High |
| 2 | Perhaps. | Uncertainty | High |
| 3 | Possibly. | Uncertainty | High |
| 4 | Not sure. | Uncertainty | High |
| 5 | I'm unsure. | Uncertainty | High |
| 6 | I'm not sure. | Uncertainty | High |
| 7 | Maybe so. | Uncertainty | High |
| 8 | I suppose. | Uncertainty | Medium |
| 9 | Could be. | Uncertainty | High |
| 10 | I don't know. | Uncertainty | High |

---

## 7.4 Non-Commitment

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | We'll see. | Non-commitment | High |
| 2 | I don't know yet. | Non-commitment | High |
| 3 | Not decided. | Non-commitment | High |
| 4 | I'm undecided. | Non-commitment | High |
| 5 | Hard to say. | Non-commitment | High |
| 6 | Can't say yet. | Non-commitment | High |
| 7 | I'm not certain. | Non-commitment | High |
| 8 | I haven't decided. | Non-commitment | High |
| 9 | Not sure yet. | Non-commitment | High |
| 10 | I need to think. | Non-commitment | High |

---

## 7.5 No Preference

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | Either way. | No preference | High |
| 2 | No preference. | No preference | High |
| 3 | I don't mind. | No preference | Medium |
| 4 | Either is fine. | No preference | High |
| 5 | Both are fine. | No preference | High |
| 6 | Doesn't matter. | No preference | High |
| 7 | It doesn't matter. | No preference | High |
| 8 | I'm okay either way. | No preference | High |
| 9 | Any option is fine. | No preference | High |
| 10 | I have no preference. | No preference | High |

---

## 7.6 Low Engagement

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | Whatever. | Low engagement | Medium |
| 2 | I don't care. | Low engagement | Medium |
| 3 | As you wish. | Low engagement | Medium |
| 4 | Up to you. | Low engagement | High |
| 5 | Your choice. | Low engagement | High |
| 6 | Doesn't matter to me. | Low engagement | High |
| 7 | Either works. | Low engagement | High |
| 8 | I have no opinion. | Low engagement | High |
| 9 | No strong preference. | Low engagement | High |
| 10 | I don't really mind. | Low engagement | Medium |

---

# 8. N — Negative

## 8.1 Semantic families

1. Disagreement
2. Reluctance
3. Mild refusal
4. Resistance
5. Mild dissatisfaction

---

## 8.2 Disagreement — anchor: NO

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | No. | Disagreement | High |
| 2 | I disagree. | Disagreement | High |
| 3 | Don't agree. | Disagreement | High |
| 4 | I don't agree. | Disagreement | High |
| 5 | Not really. | Disagreement | High |
| 6 | I don't think so. | Disagreement | High |
| 7 | I disagree with that. | Disagreement | High |
| 8 | I don't see it that way. | Disagreement | High |
| 9 | I'm not convinced. | Disagreement | High |
| 10 | I wouldn't agree. | Disagreement | High |

---

## 8.3 Reluctance — anchor: RELUCTANT

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | Reluctant. | Reluctance | High |
| 2 | I'm reluctant. | Reluctance | High |
| 3 | I'm not keen. | Reluctance | High |
| 4 | Not keen. | Reluctance | High |
| 5 | I'm hesitant. | Reluctance | High |
| 6 | Hesitant. | Reluctance | High |
| 7 | I'd rather not. | Reluctance | High |
| 8 | I'm not comfortable. | Reluctance | High |
| 9 | I'm unsure about that. | Reluctance | Medium |
| 10 | I have reservations. | Reluctance | High |

---

## 8.4 Mild Refusal

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | No thanks. | Mild refusal | High |
| 2 | Not this time. | Mild refusal | High |
| 3 | I'd rather not. | Mild refusal | High |
| 4 | I can't. | Mild refusal | High |
| 5 | I don't want to. | Mild refusal | High |
| 6 | I won't. | Mild refusal | High |
| 7 | Probably not. | Mild refusal | High |
| 8 | I don't think so. | Mild refusal | High |
| 9 | Not for me. | Mild refusal | High |
| 10 | I'll pass. | Mild refusal | High |

---

## 8.5 Resistance

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | Not really. | Resistance | Medium |
| 2 | I'd prefer not. | Resistance | High |
| 3 | I don't want that. | Resistance | High |
| 4 | I'm against it. | Resistance | High |
| 5 | I object. | Resistance | High |
| 6 | I can't agree. | Resistance | High |
| 7 | That won't work. | Resistance | High |
| 8 | I don't support that. | Resistance | High |
| 9 | I'm not comfortable with that. | Resistance | High |
| 10 | I don't think that's right. | Resistance | High |

---

## 8.6 Mild Dissatisfaction

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | Not good. | Dissatisfaction | High |
| 2 | Not great. | Dissatisfaction | High |
| 3 | Not ideal. | Dissatisfaction | High |
| 4 | That's disappointing. | Dissatisfaction | High |
| 5 | I'm not happy. | Dissatisfaction | High |
| 6 | I'm not satisfied. | Dissatisfaction | High |
| 7 | I don't like it. | Dissatisfaction | High |
| 8 | That's not good. | Dissatisfaction | High |
| 9 | I'm unhappy with that. | Dissatisfaction | High |
| 10 | I don't like that. | Dissatisfaction | High |

---

# 9. VN — Very Negative

## 9.1 Semantic families

1. Strong disagreement
2. Strong refusal
3. Strong rejection
4. Strong resistance
5. Strong dissatisfaction/aversion

---

## 9.2 Strong Disagreement — anchor: ABSOLUTELY NOT

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | Absolutely not. | Strong disagreement | High |
| 2 | Definitely not. | Strong disagreement | High |
| 3 | No way. | Strong disagreement | High |
| 4 | Never. | Strong disagreement | High |
| 5 | I strongly disagree. | Strong disagreement | High |
| 6 | I completely disagree. | Strong disagreement | High |
| 7 | Not at all. | Strong disagreement | High |
| 8 | Absolutely no. | Strong disagreement | High |
| 9 | Certainly not. | Strong disagreement | High |
| 10 | I totally disagree. | Strong disagreement | High |

---

## 9.3 Strong Refusal

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | Never. | Strong refusal | High |
| 2 | No, never. | Strong refusal | High |
| 3 | Absolutely not. | Strong refusal | High |
| 4 | I refuse. | Strong refusal | High |
| 5 | I won't do it. | Strong refusal | High |
| 6 | I will not. | Strong refusal | High |
| 7 | No chance. | Strong refusal | High |
| 8 | Not a chance. | Strong refusal | High |
| 9 | I refuse completely. | Strong refusal | High |
| 10 | I would never. | Strong refusal | High |

---

## 9.4 Strong Rejection

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | Rejected. | Strong rejection | High |
| 2 | Completely rejected. | Strong rejection | High |
| 3 | Totally unacceptable. | Strong rejection | High |
| 4 | Completely unacceptable. | Strong rejection | High |
| 5 | I reject that. | Strong rejection | High |
| 6 | I strongly reject that. | Strong rejection | High |
| 7 | That's unacceptable. | Strong rejection | High |
| 8 | I won't accept that. | Strong rejection | High |
| 9 | Absolutely unacceptable. | Strong rejection | High |
| 10 | I reject it completely. | Strong rejection | High |

---

## 9.5 Strong Resistance

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | I strongly object. | Strong resistance | High |
| 2 | I strongly oppose it. | Strong resistance | High |
| 3 | I'm completely against it. | Strong resistance | High |
| 4 | I will not support it. | Strong resistance | High |
| 5 | I strongly oppose that. | Strong resistance | High |
| 6 | I completely oppose it. | Strong resistance | High |
| 7 | I refuse to cooperate. | Strong resistance | High |
| 8 | I won't cooperate. | Strong resistance | High |
| 9 | I strongly object to that. | Strong resistance | High |
| 10 | I'm totally against it. | Strong resistance | High |

---

## 9.6 Strong Dissatisfaction / Aversion

| # | Expression | Family | Confidence |
|---:|---|---|---|
| 1 | I hate it. | Strong dissatisfaction | High |
| 2 | I absolutely hate it. | Strong dissatisfaction | High |
| 3 | That's terrible. | Strong dissatisfaction | High |
| 4 | That's awful. | Strong dissatisfaction | High |
| 5 | That's horrible. | Strong dissatisfaction | High |
| 6 | Completely unacceptable. | Strong dissatisfaction | High |
| 7 | I can't stand it. | Strong dissatisfaction | High |
| 8 | I strongly dislike it. | Strong dissatisfaction | High |
| 9 | I'm extremely unhappy. | Strong dissatisfaction | High |
| 10 | I'm absolutely dissatisfied. | Strong dissatisfaction | High |

---

# 10. High-Risk / Context-Sensitive Expressions

The following expressions should **not automatically enter the high-confidence standalone training pool**:

```text
Okay.
Sure.
Fine.
Good.
Right.
Maybe.
Whatever.
I don't mind.
I think so.
Sounds good.
```

Some of these can be positive, neutral, or negative depending on conversational context, prosody, or preceding dialogue.

For the controlled SRCC experiment, an expression should be included only when its intended mapping is sufficiently stable under the standalone setting.

The original SRCC specification explicitly requires ambiguous standalone expressions to be excluded rather than assigned to multiple categories.

---

# 11. Critical Category Boundaries

## VP ↔ P

The distinction is **strength of positive response**.

```text
P:
Yes.
Sure.
Sounds good.
I'd be willing.

VP:
Absolutely.
Definitely.
I'd love to.
That's fantastic.
I strongly agree.
```

Do not use merely positive words as VP without evidence of strong intensity.

---

## P ↔ I

The distinction is **positive acceptance versus neutral/non-committal response**.

```text
P:
Yes.
Sure.
That works.
I'm okay with that.

I:
Maybe.
Not sure.
Either way.
No preference.
I don't know yet.
```

Expressions such as `Okay` require special review because they can be positive, neutral, or merely acknowledging.

---

## I ↔ N

The distinction is **neutral/non-committal versus actual resistance/negative response**.

```text
I:
Maybe.
Not sure.
Either way.
No preference.

N:
No.
I disagree.
I'd rather not.
I don't want to.
I'll pass.
```

---

## N ↔ VN

The distinction is **negative strength**.

```text
N:
No.
I'd rather not.
I'm reluctant.
I disagree.

VN:
Absolutely not.
No way.
I strongly disagree.
I refuse.
That's unacceptable.
```

---

# 12. Anchor Quality Tiers

Every expression should ultimately be assigned a quality tier.

### Tier A — Strong anchor

Stable standalone category signal.

Suitable for core training.

### Tier B — Controlled variant

Strongly related to a Tier A anchor and still reasonably stable.

Suitable for controlled training expansion.

### Tier C — Context-sensitive

Plausible category interpretation but potentially dependent on context/prosody.

Suitable primarily for robustness evaluation or carefully reviewed training.

### EXCLUDE

Ambiguous, unnatural, contradictory, or requiring context to determine the category.

Do not include.

---

# 13. Recommended Master-Bank Metadata

The final machine-readable bank should contain:

```text
expression
category
semantic_family
anchor
strength
confidence
variation_type
quality_tier
length_band
source
notes
```

Recommended `variation_type` values:

```text
direct_anchor
lexical_variant
syntactic_variant
intensified_variant
semantic_variant
acceptance_variant
agreement_variant
refusal_variant
uncertainty_variant
```

---

# 14. Dataset Construction Rule

Do not automatically put the entire master bank into training.

The master bank is a **source resource**.

Future datasets should be constructed by controlled sampling:

```text
MASTER EXPRESSION BANK
        ↓
quality filtering
        ↓
lexical-family grouping
        ↓
category balancing
        ↓
length-band balancing
        ↓
train / validation / test assignment
```

Near-duplicate lexical variants from the same family should not be randomly distributed across train and test.

---

# 15. Initial SRCC Extraction

The original SRCC target remains:

```text
5 categories
× 3 length bands
× 20 expressions
=
300 expressions
```

Therefore this expanded bank does **not replace the original 300-expression experimental target**.

Instead:

```text
Master Bank
     ↓
Controlled selection
     ↓
300-expression SRCC
```

This preserves comparability with the original experiment.

---

# 16. Important Warning

Response Category is more context-sensitive than Execution Status.

Therefore:

> **Do not assume that a word is a deterministic category label merely because it frequently appears in one category.**

The bank is a controlled experimental resource, not a claim that natural language always has fixed lexical-to-category mappings.

The classifier should eventually be evaluated on contextual examples in addition to this standalone corpus.

---

# 17. Recommended Next Step

After this master bank is reviewed:

1. Freeze the high-confidence anchors.
2. Remove/flag ambiguous expressions.
3. Build category-specific variation banks.
4. Select the 300-expression SRCC subset.
5. Create grouped train/validation/test splits.
6. Reserve lexical-family and boundary groups for controlled generalization testing.

---

## Final Principle

> **Expand Response Category coverage through controlled lexical and semantic variation, but preserve the frozen five-category ontology and never manufacture certainty for inherently context-sensitive expressions.**
