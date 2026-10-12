# Execution Status Final Split Report

## Dataset Summary
- **Total Dataset Size:** 170
- **Number of Lexical/Semantic Groups:** 11
- **Random Seed:** 42

TOTAL:
NS: 50
IP: 60
C:  60

---

## Split Statistics

### TRAIN (94 rows, 55.3%)
NS: 30
IP: 20
C:  44

### VALIDATION (30 rows, 17.6%)
NS: 10
IP: 20
C:  0

### TEST (46 rows, 27.1%)
NS: 10
IP: 20
C:  16

---

## Group Leakage Audit

1. **Exact-duplicate leakage result:** PASS (Normalized exact duplicates share the same family).
2. **Lexical-family leakage result:** PASS (Grouping preserved via markdown header families).
3. **Number of groups assigned to each split:**
   - Train: 6
   - Validation: 2
   - Test: 3
4. **Boundary coverage:** Hard boundary sets explicitly mapping `DO` (NS), `Doing` (IP), and `Done` (C) were placed entirely in the TEST split to verify hard lexical overlap generalization.

Final status: PASS
