# Completed — Semantic Variation Bank

## Purpose

This file combines two complementary forms of linguistic variation for the `C — Completed` Execution Status category:

1. **Direct lexical variants** of `Done` and `Finished`.
2. **Broader semantic variation families** expressing completed execution.

The purpose is to provide controlled linguistic coverage without treating exact duplicate expressions as separate training instances.

---

# 1. Direct Variants of "Done"

| ID | Variation Type | Expression | Label |
|---|---|---|---|
| D01 | Bare | Done. | C |
| D02 | Quantifier | All done. | C |
| D03 | Copular | It's done. | C |
| D04 | Temporal | Already done. | C |
| D05 | Degree | Fully done. | C |
| D06 | Degree | Completely done. | C |
| D07 | Temporal | Finally done. | C |
| D08 | Temporal | Done already. | C |
| D09 | Temporal | Done now. | C |
| D10 | Demonstrative | That's done. | C |
| D11 | Totality | It's all done. | C |
| D12 | Copular + temporal | It's done now. | C |
| D13 | Copular + temporal | It's already done. | C |
| D14 | Copular + temporal | It's finally done. | C |
| D15 | First-person | I've done it. | C |
| D16 | First-person | I have done it. | C |
| D17 | First-person | I've done that. | C |
| D18 | Causative completion | I got it done. | C |
| D19 | First-person + perfective | I've got it done. | C |
| D20 | Totality | It's completely done. | C |

---

# 2. Direct Variants of "Finished"

| ID | Variation Type | Expression | Label |
|---|---|---|---|
| F01 | Bare | Finished. | C |
| F02 | Quantifier | All finished. | C |
| F03 | Copular | It's finished. | C |
| F04 | Temporal | Already finished. | C |
| F05 | Degree | Fully finished. | C |
| F06 | Degree | Completely finished. | C |
| F07 | Temporal | Finally finished. | C |
| F08 | Temporal | Finished already. | C |
| F09 | Temporal | Finished now. | C |
| F10 | Demonstrative | That's finished. | C |
| F11 | Totality | It's all finished. | C |
| F12 | Copular + temporal | It's finished now. | C |
| F13 | Copular + temporal | It's already finished. | C |
| F14 | Copular + temporal | It's finally finished. | C |
| F15 | First-person | I've finished. | C |
| F16 | First-person | I've finished it. | C |
| F17 | First-person | I finished it. | C |
| F18 | First-person | I have finished it. | C |
| F19 | First-person | I've finished that. | C |
| F20 | Causative completion | I got it finished. | C |

---

# 3. Semantic Variation Families

| # | Semantic Variation | Example | Label |
|---|---|---|---|
| 1 | Direct completion | Done. | C |
| 2 | Explicit finished state | Finished. | C |
| 3 | Explicit completion state | Completed. | C |
| 4 | Task completed | The task is done. | C |
| 5 | Work completed | The work is finished. | C |
| 6 | First-person completion | I finished it. | C |
| 7 | First-person completion — perfective | I've completed it. | C |
| 8 | Already completed | I already did it. | C |
| 9 | Everything completed | Everything is done. | C |
| 10 | All required work completed | I finished everything required. | C |
| 11 | Completion confirmation | It's all done. | C |
| 12 | Result achieved | It's taken care of. | C |
| 13 | Requirement fulfilled | That's been taken care of. | C |
| 14 | Outcome achieved | It's been completed. | C |
| 15 | Final state | Nothing remains. | C |
| 16 | No remaining work | There's nothing left. | C |
| 17 | Retrospective completion | I got it done. | C |
| 18 | Successful completion | I completed it successfully. | C |
| 19 | Completion + confirmation | Yes, it's finished. | C |
| 20 | Completion + totality | It's completely done. | C |

---

# 4. Variation Hierarchy

```text
COMPLETED
│
├── Level 1 — Direct lexical anchors
│   ├── Done.
│   ├── Finished.
│   └── Completed.
│
├── Level 2 — Direct lexical/syntactic variants
│   ├── All done.
│   ├── It's done.
│   ├── Already done.
│   ├── I've done it.
│   ├── All finished.
│   ├── It's finished.
│   ├── Already finished.
│   └── I've finished it.
│
└── Level 3 — Broader semantic expressions
    ├── Everything is done.
    ├── I already did it.
    ├── Nothing remains.
    ├── There's nothing left.
    ├── It's taken care of.
    └── I completed it successfully.
```

---

# 5. Recommended Use

The direct `Done` and `Finished` variants should be treated as **lexical reinforcement**, not as 40 independent semantic concepts.

The broader semantic families provide **semantic generalization**.

```text
Done
Finished
Completed
      ↓
Direct lexical variants
      ↓
Broader completion expressions
      ↓
C — Completed
```

Exact duplicates should not be multiplied merely to increase dataset size.

The objective is to teach the classifier that multiple natural linguistic forms can express the same underlying execution state:

> **The target task has actually finished.**

---

# 6. Quality Control

- [ ] Actual execution has finished.
- [ ] The expression maps to `C — Completed`.
- [ ] No `In Progress` interpretation is required.
- [ ] No task-specific context is required where standalone use is intended.
- [ ] Natural user language.
- [ ] No duplicate used merely for count inflation.
- [ ] Direct lexical variants remain distinguishable from broader semantic variants.
- [ ] Temporal words such as `already`, `now`, or `finally` are not the sole reason for the `C` label.

---

# Final Principle

> **Use direct variants to reinforce high-frequency completion signals such as `done` and `finished`, and use semantic variants to ensure that the classifier learns the broader concept of completed execution rather than memorizing individual keywords.**
