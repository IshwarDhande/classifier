# Not Started — Direct Lexical Variation Bank

## Purpose

Controlled direct variants for five core Not Started lexical anchors.

**Category:** `NS — Not Started`

**Total:** 5 anchors × 10 variants = **50 expressions**

---

# 1. START — 10 Variants

| ID | Expression | Category |
|---|---|---|
| S01 | Not started. | NS |
| S02 | Haven't started. | NS |
| S03 | Never started. | NS |
| S04 | Haven't started yet. | NS |
| S05 | Not started yet. | NS |
| S06 | I haven't started. | NS |
| S07 | I haven't started it. | NS |
| S08 | I haven't started yet. | NS |
| S09 | I still haven't started. | NS |
| S10 | I haven't even started. | NS |

---

# 2. BEGIN — 10 Variants

| ID | Expression | Category |
|---|---|---|
| B01 | Not begun. | NS |
| B02 | Haven't begun. | NS |
| B03 | Haven't begun yet. | NS |
| B04 | Never begun. | NS |
| B05 | I haven't begun. | NS |
| B06 | I haven't begun it. | NS |
| B07 | I haven't begun yet. | NS |
| B08 | I still haven't begun. | NS |
| B09 | Still not begun. | NS |
| B10 | I haven't even begun. | NS |

---

# 3. ATTEMPT — 10 Variants

| ID | Expression | Category |
|---|---|---|
| A01 | Not attempted. | NS |
| A02 | Haven't attempted. | NS |
| A03 | Haven't attempted it. | NS |
| A04 | Never attempted. | NS |
| A05 | I haven't attempted it. | NS |
| A06 | I haven't attempted yet. | NS |
| A07 | Haven't attempted yet. | NS |
| A08 | I still haven't attempted it. | NS |
| A09 | Still not attempted. | NS |
| A10 | I haven't even attempted it. | NS |

---

# 4. TRY — 10 Variants

| ID | Expression | Category |
|---|---|---|
| T01 | Haven't tried. | NS |
| T02 | Never tried. | NS |
| T03 | Haven't tried yet. | NS |
| T04 | Never tried it. | NS |
| T05 | I haven't tried. | NS |
| T06 | I haven't tried it. | NS |
| T07 | I haven't tried yet. | NS |
| T08 | I haven't tried it yet. | NS |
| T09 | I still haven't tried. | NS |
| T10 | I still haven't tried it. | NS |

---

# 5. DO — 10 Variants

| ID | Expression | Category |
|---|---|---|
| D01 | Not done. | NS |
| D02 | Haven't done it. | NS |
| D03 | Haven't done it yet. | NS |
| D04 | Never done it. | NS |
| D05 | I haven't done it. | NS |
| D06 | I haven't done it yet. | NS |
| D07 | I still haven't done it. | NS |
| D08 | Still haven't done it. | NS |
| D09 | I never did it. | NS |
| D10 | Not done yet. | NS |

---

# 6. Structure

```text
NOT STARTED
│
├── START
│   └── 10 variants
│
├── BEGIN
│   └── 10 variants
│
├── ATTEMPT
│   └── 10 variants
│
├── TRY
│   └── 10 variants
│
└── DO
    └── 10 variants
```

**Total: 50 expressions**

---

# 7. Boundary Control

The expressions must indicate **absence of actual execution**.

```text
I haven't started.       → NS
I haven't begun.         → NS
I haven't attempted it. → NS
I haven't tried it.     → NS
I haven't done it yet.  → NS
```

Positive forms are not automatically NS:

```text
I'm working on it.       → IP
I'm doing it.            → IP
I'm trying to finish it. → IP
I've finished it.        → C
I've done it.            → C
```

## Final Principle

> **For Not Started, lexical variation should reinforce the absence of execution rather than merely future intention, delay, or temporal information.**
