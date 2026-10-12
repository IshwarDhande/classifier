# BA01 — VP ↔ P Boundary Anchors

## Boundary

**VP — Very Positive** ↔ **P — Positive**

### Core distinction

- **VP:** The user shows strong acceptance, enthusiasm, appreciation, proactive engagement, or unusually strong voluntary cooperation.
- **P:** The user shows genuine acceptance and cooperation without strong enthusiasm or elevated engagement.

The distinction must be based on the user's **behavioral reaction** to the intervention, not sentiment, politeness, isolated keywords, or punctuation.

---

## BA01-A01 — VP Prototype

**Context:**  
Assistant: “Would you like me to set a reminder for your evening medication?”

**User:**  
“Absolutely. That would make it much easier for me to stay on track, and I want to get started tonight.”

**Label:** `VP`

---

## BA01-A02 — P Prototype

**Context:**  
Assistant: “Would you like me to set a reminder for your evening medication?”

**User:**  
“Okay, that works. I’ll take the medication tonight.”

**Label:** `P`

---

## BA01-A03 — VP-Leaning Boundary

**Context:**  
Assistant: “You could keep a water bottle on your desk so it is easier to drink regularly throughout the day.”

**User:**  
“Yes, let’s do that. Having it right in front of me will really help, and I’ll fill one up now.”

**Label:** `VP`

---

## BA01-A04 — P-Leaning Boundary

**Context:**  
Assistant: “You could keep a water bottle on your desk so it is easier to drink regularly throughout the day.”

**User:**  
“Yes, let’s do that. I’ll keep the water bottle on my desk and drink from it today.”

**Label:** `P`

---

## BA01-A05 — Implicit VP

**Context:**  
Assistant: “Would you be open to taking a short walk around the block after dinner?”

**User:**  
“Go ahead and plan for that. I’ll have my walking shoes by the door so I’m ready as soon as dinner finishes.”

**Label:** `VP`

---

## BA01-A06 — Implicit P

**Context:**  
Assistant: “Would you be open to taking a short walk around the block after dinner?”

**User:**  
“Go ahead and plan for that. I’ll take the walk after dinner.”

**Label:** `P`
