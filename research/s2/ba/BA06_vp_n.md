# BA06 — VP ↔ N Boundary Anchors

## Boundary

**VP — Very Positive** ↔ **N — Negative**

### Core distinction

- **VP:** The user shows strong acceptance, enthusiasm, appreciation, proactive engagement, or unusually strong voluntary cooperation.
- **N:** The user expresses behavioral resistance, reluctance, disagreement, or reduced willingness to follow the intervention, while remaining recoverable.

The distinction is based on **behavioral stance toward the intervention**, not on sentiment, politeness, or isolated refusal words.

---

## BA06-A01 — VP Prototype

**Context:**  
Assistant: “Would you like to split your physiotherapy routine into two shorter sessions today?”

**User:**  
“Yes, that sounds great. I’ll do the first session now and the second after work.”

**Label:** `VP`

---

## BA06-A02 — N Prototype

**Context:**  
Assistant: “Would you like to split your physiotherapy routine into two shorter sessions today?”

**User:**  
“I’d rather not split the physiotherapy routine. I don’t want to change my schedule that way.”

**Label:** `N`

---

## BA06-A03 — VP-Leaning Boundary

**Context:**  
Assistant: “You could put your medication beside your breakfast items to make it easier to remember.”

**User:**  
“I like that idea. I’ll set the medication by my breakfast items tonight so I start tomorrow.”

**Label:** `VP`

---

## BA06-A04 — N-Leaning Boundary

**Context:**  
Assistant: “You could put your medication beside your breakfast items to make it easier to remember.”

**User:**  
“I understand the suggestion, but I don’t want to keep my medication out on the breakfast counter.”

**Label:** `N`

---

## BA06-A05 — Implicit VP

**Context:**  
Assistant: “Keeping a full water bottle on your desk can help you stay hydrated while working.”

**User:**  
“That would make drinking water much easier. I’ll fill up a large bottle and keep it beside my monitor.”

**Label:** `VP`

---

## BA06-A06 — Implicit N

**Context:**  
Assistant: “Keeping a full water bottle on your desk can help you stay hydrated while working.”

**User:**  
“I know it could help with hydration, but I don’t want to crowd my desk with a water bottle.”

**Label:** `N`
