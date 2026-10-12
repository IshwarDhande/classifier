# Stage 2 — Boundary Pair Matrix

## Purpose

This matrix defines the ten pairwise Response Category boundaries used for Stage 2 boundary construction. The four adjacent ordinal boundaries receive primary semantic priority; the six non-adjacent boundaries provide broader contrast coverage and reduce coarse polarity shortcuts.

## Frozen Ordinal Scale

```text
VN < N < I < P < VP
```

## Boundary Pairs

| ID | Pair | Boundary class | Primary distinction | Diagnostic focus |
|---|---|---|---|---|
| `B01` | `VP ↔ P` | Adjacent | Enthusiastic/high-engagement acceptance ↔ ordinary cooperative acceptance | VP: strong appreciation, enthusiasm, proactive engagement | P: acceptance/cooperation without VP-level enthusiasm |
| `B02` | `P ↔ I` | Adjacent | Behavioral acceptance/commitment ↔ uncertainty or non-commitment | P: sufficient evidence of willingness/cooperation | I: insufficient evidence of acceptance |
| `B03` | `I ↔ N` | Adjacent | Neutral/non-committal response ↔ behavioral resistance | I: no clear resistance | N: meaningful but potentially recoverable resistance |
| `B04` | `N ↔ VN` | Adjacent | Recoverable resistance ↔ strong rejection/reactance/disengagement | N: reluctance, mild refusal, disagreement | VN: strong rejection, hostility, high reactance, active disengagement |
| `B05` | `VP ↔ I` | Non-adjacent | Strong positive engagement ↔ insufficient behavioral commitment | VP: clear acceptance plus enthusiasm/engagement | I: no sufficiently strong acceptance |
| `B06` | `VP ↔ N` | Non-adjacent | Strong positive acceptance ↔ behavioral resistance | VP: strong acceptance/engagement | N: meaningful resistance |
| `B07` | `VP ↔ VN` | Non-adjacent | Strong positive engagement ↔ strong rejection/reactance | VP: enthusiastic/cooperative response | VN: decisive opposition/rejection/disengagement |
| `B08` | `P ↔ N` | Non-adjacent | Ordinary cooperation ↔ meaningful resistance | P: willingness/cooperation | N: reluctance/refusal/disagreement/resistance |
| `B09` | `P ↔ VN` | Non-adjacent | Ordinary cooperation ↔ strong rejection/reactance | P: cooperative acceptance | VN: strong opposition/rejection/disengagement |
| `B10` | `I ↔ VN` | Non-adjacent | Insufficient behavioral evidence ↔ strong rejection/reactance | I: uncertainty/non-commitment without strong resistance | VN: explicit strong rejection/opposition/disengagement |

## Priority

### Tier 1 — Adjacent ordinal boundaries

`B01 VP↔P`, `B02 P↔I`, `B03 I↔N`, `B04 N↔VN`

These boundaries define the principal transitions of the ordinal response scale and receive the strongest semantic scrutiny.

### Tier 2 — Non-adjacent boundaries

`B05 VP↔I`, `B06 VP↔N`, `B07 VP↔VN`, `B08 P↔N`, `B09 P↔VN`, `B10 I↔VN`

These boundaries are retained to prevent the classifier from learning only adjacent polarity transitions or broad positive/negative shortcuts.

## Construction Rule

Every boundary resource must answer:

> Why does the behavioral evidence support Category A rather than Category B?

Boundary construction must prioritize behavioral commitment, behavioral resistance, communicative intention, pragmatic meaning, and only then surface wording. Emotion, sentiment, topic, task completion, execution status, Dialogue Purpose, and Persuasion Barrier must not serve as hidden category proxies.