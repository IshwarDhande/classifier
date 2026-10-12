# Execution Status — Stage 3A Audit Report

**Date:** 2026-09-28
**Scope:** `research/execution_status/s3a`

## Overview

An automated semantic audit was conducted on the Stage 3A variant files for the Execution Status dataset. The audit checked for the correct number of scenarios (15 per file), the correct number of variants per scenario (18), and intra-file duplicate utterances.

## Findings

### 1. `stage_3a_completed_variants.md`
- **Scenarios Found:** 15
- **Variant Count:** Correct (18 variants per scenario).
- **Status:** **FAIL (Duplicates)**
- **Errors:** 
  - **76 duplicate utterances** found across the file.
  - *Examples of duplicates:*
    - "The therapy session was finished earlier today."
    - "The workout was finished earlier today."
    - "I’m done with the dose; I was running late, but it’s taken now."
    - "The entire therapy sequence is finished now."
    - "I completed every required set and exercise, so the workout is finished."

### 2. `stage_3a_in_progress_variants.md`
- **Scenarios Found:** 15
- **Variant Count:** Correct (18 variants per scenario).
- **Status:** **FAIL (Duplicates)**
- **Errors:**
  - **90 duplicate utterances** found across the file.
  - *Examples of duplicates:*
    - "Three sets are done, while two more are still required."
    - "I’m only partway through the exercises."
    - "Right now, the physiotherapy sequence is underway, and I’m partway through it."
    - "Right now, the water is what I’m drinking at the moment."
    - "Right now, the therapy was underway when I had to stop, and some work remains."

### 3. `stage_3a_not_started_variants.md`
- **Scenarios Found:** 15
- **Variant Count:** Correct (18 variants per scenario).
- **Status:** **FAIL (Duplicates)**
- **Errors:**
  - **14 duplicate utterances** found across the file.
  - *Examples of duplicates:*
    - "Yeah, i forgot to take the medicine."
    - "Yeah, i’m going to get the physiotherapy done later."
    - "Yeah, i can get to the therapy if I’m free this evening."
    - "Yeah, i’m not going to take the medicine."
    - "Yeah, i haven’t started the exercises yet; I’ll do them after lunch."

## Recommended Actions

1. **Remediate Duplicates:** Rewrite the duplicated utterances in all three files to ensure strict uniqueness. There are 180 total duplicates to remediate across the Stage 3A variants.
