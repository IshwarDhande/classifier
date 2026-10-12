# HN07 — VP ↔ VN Hard Negative Variants

## Boundary

**VP (Very Positive) ↔ VN (Very Negative)**

## Construction Focus

The examples preserve the hard-negative mechanism while the label is determined by the user's dominant behavioral response to the task reminder, not by surface cues.

The expansion varies the misleading surface realization while preserving the underlying contrast between strong proactive acceptance (`VP`) and strong rejection, opposition, or active disengagement (`VN`).

## Variant Construction Rules

- Preserve the original target category for each parent.
- Preserve the VP ↔ VN boundary.
- Preserve the original hard-negative mechanism.
- Preserve the task and conversational situation.
- For `VP`, retain strong enthusiasm, proactive agency, appreciation, or voluntary cooperation.
- For `VN`, retain strong rejection, explicit opposition, autonomy shutdown, or active disengagement.
- Surface negativity must not automatically determine VN when strong behavioral acceptance remains dominant.
- Surface politeness or appreciation must not automatically weaken a VN label when the user clearly rejects the interaction.
- The preceding task reminder/intervention is implicit; only the user response is represented.

---

## HN07-01 — VP

**Parent:** HN07-01  
**Task:** Medication  
**Hard-negative mechanism:** Competing Keyword  
**Gold label:** `VP`

### HN07-01-V01 — LEX
- **Lineage:** HN07-01 → HN07-01-V01

**User:**  
“I never expected to like this idea, but it’s excellent and I’m putting the medication dispenser beside the coffee maker right now.”

**Label:** `VP`

### HN07-01-V02 — NAT
- **Lineage:** HN07-01 → HN07-01-V02

**User:**  
“I honestly didn’t think I’d like the idea, but I really love it and I’m putting the medication dispenser beside the coffee maker now.”

**Label:** `VP`

### HN07-01-V03 — EXP
- **Lineage:** HN07-01 → HN07-01-V03

**User:**  
“I was surprised by how much I liked the idea, and I’m acting on that reaction now by putting the medication dispenser beside the coffee maker.”

**Label:** `VP`

### HN07-01-V04 — DSC
- **Lineage:** HN07-01 → HN07-01-V04

**User:**  
“I’m putting the medication dispenser beside the coffee maker right now. I never expected to like the idea, but it’s actually fantastic.”

**Label:** `VP`

### HN07-01-V05 — PRG
- **Lineage:** HN07-01 → HN07-01-V05

**User:**  
“My initial expectation was that I wouldn’t like it, but that changed completely—I think it’s fantastic and I’m already setting up the dispenser.”

**Label:** `VP`

### HN07-01-V06 — CMK
- **Lineage:** HN07-01 → HN07-01-V06

**User:**  
“Really, I didn’t expect to like it—but I do. It’s fantastic, and I’m putting the medication dispenser beside the coffee maker now.”

**Label:** `VP`

---

## HN07-02 — VP

**Parent:** HN07-02  
**Task:** Hydration  
**Hard-negative mechanism:** Competing Phrase  
**Gold label:** `VP`

### HN07-02-V01 — LEX
- **Lineage:** HN07-02 → HN07-02-V01

**User:**  
“I really dislike clutter around my workspace, but this idea is excellent and I’m filling the bottle right now.”

**Label:** `VP`

### HN07-02-V02 — NAT
- **Lineage:** HN07-02 → HN07-02-V02

**User:**  
“I normally hate having extra things around my workspace, but I genuinely love this idea and I’m filling the bottle now.”

**Label:** `VP`

### HN07-02-V03 — EXP
- **Lineage:** HN07-02 → HN07-02-V03

**User:**  
“Workspace clutter is usually something I strongly dislike, but that doesn’t change my reaction to this plan—I’m excited about it and already filling the bottle.”

**Label:** `VP`

### HN07-02-V04 — DSC
- **Lineage:** HN07-02 → HN07-02-V04

**User:**  
“I’m filling the bottle right now because I really like this idea. I absolutely dislike workspace clutter, but I’m happy to make this exception.”

**Label:** `VP`

### HN07-02-V05 — PRG
- **Lineage:** HN07-02 → HN07-02-V05

**User:**  
“Even though clutter around my workspace normally bothers me, this idea is genuinely appealing to me, so I’m filling the bottle and getting started.”

**Label:** `VP`

### HN07-02-V06 — CMK
- **Lineage:** HN07-02 → HN07-02-V06

**User:**  
“Yeah, I hate clutter around my workspace, but honestly, this is a game changer. I’m filling the bottle right now.”

**Label:** `VP`

---

## HN07-03 — VP

**Parent:** HN07-03  
**Task:** Exercise  
**Hard-negative mechanism:** Misleading Opening Clause  
**Gold label:** `VP`

### HN07-03-V01 — LEX
- **Lineage:** HN07-03 → HN07-03-V01

**User:**  
“Hold on—that is actually a brilliant suggestion, and I’m putting on my shoes to take the walk now.”

**Label:** `VP`

### HN07-03-V02 — NAT
- **Lineage:** HN07-03 → HN07-03-V02

**User:**  
“Wait a second—that’s actually a fantastic suggestion, and I’m already putting my shoes on for the walk.”

**Label:** `VP`

### HN07-03-V03 — EXP
- **Lineage:** HN07-03 → HN07-03-V03

**User:**  
“I initially reacted as though I wanted to stop the conversation, but the suggestion is genuinely brilliant, and I’m getting ready to take the walk now.”

**Label:** `VP`

### HN07-03-V04 — DSC
- **Lineage:** HN07-03 → HN07-03-V04

**User:**  
“I’m putting on my shoes to take the walk now. Stop right there? Actually, no—the suggestion is brilliant and I’m excited to do it.”

**Label:** `VP`

### HN07-03-V05 — PRG
- **Lineage:** HN07-03 → HN07-03-V05

**User:**  
“My first reaction sounded like I wanted to stop, but that isn’t my actual response—I think the suggestion is brilliant and I’m already getting ready.”

**Label:** `VP`

### HN07-03-V06 — CMK
- **Lineage:** HN07-03 → HN07-03-V06

**User:**  
“Wait, stop—well, actually, this is brilliant. I’m putting my shoes on and taking the walk now.”

**Label:** `VP`

---

## HN07-04 — VN

**Parent:** HN07-04  
**Task:** Medication  
**Hard-negative mechanism:** Mid-Sentence Self-Correction  
**Gold label:** `VN`

### HN07-04-V01 — LEX
- **Lineage:** HN07-04 → HN07-04-V01

**User:**  
“I’ll organize my medication that way today—no, forget that. Stop telling me how to manage it; I’m completely fed up with these suggestions.”

**Label:** `VN`

### HN07-04-V02 — NAT
- **Lineage:** HN07-04 → HN07-04-V02

**User:**  
“I was going to organize it that way, but no, I’m done with that. Stop telling me how to manage my medication—I’m fed up with these suggestions.”

**Label:** `VN`

### HN07-04-V03 — EXP
- **Lineage:** HN07-04 → HN07-04-V03

**User:**  
“I initially said I would follow the plan, but I’m withdrawing that completely. Stop directing me about my medication; I don’t want these suggestions anymore.”

**Label:** `VN`

### HN07-04-V04 — DSC
- **Lineage:** HN07-04 → HN07-04-V04

**User:**  
“Stop telling me how to manage my medication. I’m completely fed up with these suggestions. I was going to organize it that way, but no, I’m done with it.”

**Label:** `VN`

### HN07-04-V05 — PRG
- **Lineage:** HN07-04 → HN07-04-V05

**User:**  
“The initial agreement is withdrawn—I’m ending the discussion about how I manage my medication. Stop giving me these suggestions.”

**Label:** `VN`

### HN07-04-V06 — CMK
- **Lineage:** HN07-04 → HN07-04-V06

**User:**  
“Sure, I’ll organize it that way—no, actually, stop. I’m completely fed up with these medication suggestions.”

**Label:** `VN`

---

## HN07-05 — VN

**Parent:** HN07-05  
**Task:** Exercise  
**Hard-negative mechanism:** Multiple Competing Cues  
**Gold label:** `VN`

### HN07-05-V01 — LEX
- **Lineage:** HN07-05 → HN07-05-V01

**User:**  
“I know you’re trying to help, but stop pushing me about getting ready for walks and leave me alone about it.”

**Label:** `VN`

### HN07-05-V02 — NAT
- **Lineage:** HN07-05 → HN07-05-V02

**User:**  
“I understand you mean well, but please stop pushing the walking routine. I want to be left alone about it.”

**Label:** `VN`

### HN07-05-V03 — EXP
- **Lineage:** HN07-05 → HN07-05-V03

**User:**  
“I appreciate that you’re trying to help, but I’m rejecting the conversation altogether—stop pushing me about getting ready for walks and leave me alone.”

**Label:** `VN`

### HN07-05-V04 — DSC
- **Lineage:** HN07-05 → HN07-05-V04

**User:**  
“Leave me alone about the walks. I know you’re trying to help, but stop pushing me about getting ready for them.”

**Label:** `VN`

### HN07-05-V05 — PRG
- **Lineage:** HN07-05 → HN07-05-V05

**User:**  
“Your intention to help doesn’t change my response—I’m ending this discussion about getting ready for walks. Stop pushing me and leave me alone.”

**Label:** `VN`

### HN07-05-V06 — CMK
- **Lineage:** HN07-05 → HN07-05-V06

**User:**  
“Thanks, I know you’re trying to help, but no—stop pushing me about the walks and leave me alone about it.”

**Label:** `VN`

---

## HN07-06 — VN

**Parent:** HN07-06  
**Task:** Physiotherapy  
**Hard-negative mechanism:** Conversational Distractor  
**Gold label:** `VN`

### HN07-06-V01 — LEX
- **Lineage:** HN07-06 → HN07-06-V01

**User:**  
“We’ve had good conversations before, but I’m completely done discussing my physiotherapy. Drop the subject.”

**Label:** `VN`

### HN07-06-V02 — NAT
- **Lineage:** HN07-06 → HN07-06-V02

**User:**  
“We’ve talked well before, but I’m done talking about my physiotherapy now. Please drop the subject.”

**Label:** `VN`

### HN07-06-V03 — EXP
- **Lineage:** HN07-06 → HN07-06-V03

**User:**  
“I value the good conversations we’ve had, but I’m ending this topic completely. I’m done discussing physiotherapy, so stop bringing it up.”

**Label:** `VN`

### HN07-06-V04 — DSC
- **Lineage:** HN07-06 → HN07-06-V04

**User:**  
“Drop the subject. We’ve had good conversations before, but I’m completely done discussing my physiotherapy with you.”

**Label:** `VN`

### HN07-06-V05 — PRG
- **Lineage:** HN07-06 → HN07-06-V05

**User:**  
“Our earlier conversations may have gone well, but that doesn’t change my current response—I’m ending the physiotherapy discussion. Drop it.”

**Label:** `VN`

### HN07-06-V06 — CMK
- **Lineage:** HN07-06 → HN07-06-V06

**User:**  
“Yeah, we’ve had good conversations, but no, I’m done discussing physiotherapy. Drop the subject.”

**Label:** `VN`

---

## Gold Labels

| ID | Variant | Label | Task | Distractor Pattern |
|---|---|---|---|---|
| HN07-01 | HN-V01–HN-V06 | VP | Medication | Competing Keyword |
| HN07-02 | HN-V01–HN-V06 | VP | Hydration | Competing Phrase |
| HN07-03 | HN-V01–HN-V06 | VP | Exercise | Misleading Opening Clause |
| HN07-04 | HN-V01–HN-V06 | VN | Medication | Mid-Sentence Self-Correction |
| HN07-05 | HN-V01–HN-V06 | VN | Exercise | Multiple Competing Cues |
| HN07-06 | HN-V01–HN-V06 | VN | Physiotherapy | Conversational Distractor |

## QC Checklist

- [x] Same target category within each parent family
- [x] Same hard-negative mechanism
- [x] Competing surface cue remains present
- [x] Target behavioral evidence remains dominant
- [x] VP examples preserve strong enthusiasm and proactive agency
- [x] VN examples preserve strong rejection or active disengagement
- [x] Surface negativity does not override clear VP behavioral evidence
- [x] Politeness/appreciation does not weaken clear VN rejection
- [x] Self-correction preserves the final behavioral state
- [x] No reminder-configuration semantics
- [x] No sentiment-only labeling
- [x] No category drift across variants
- [x] Natural conversational wording
- [x] Parent-family lineage preserved for leakage-controlled splitting
