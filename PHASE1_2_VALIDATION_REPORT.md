# CSE2101 — Phase 1.2 Validation Report
**Phase 1.2: Extraction Provenance, Damage Audit & Validator Integrity Correction**  
**Corpus Name:** user-unknown6761/CSE2101  
**Generated Date:** 2026-10-02  
**Validation Suite:** [scripts/validate_phase1.py](file:///d:/DOWNLOADS/CSE2101/scripts/validate_phase1.py) & [scripts/check_doc28_q7_12.py](file:///d:/DOWNLOADS/CSE2101/scripts/check_doc28_q7_12.py)  
**Overall Status:** **PHASE 1.2 STATUS: PASS** (24/24 Core Rules Passed, 6/6 Adversarial Tests Passed)

---

## 1. Executive Summary

This report certifies that the Phase 1.2 source corpus audit for the CSE/CSEN 2101 Data Structures and Algorithms exam-preparation corpus pipeline has resolved all previous release-blocking integrity defects.

The validation suite was constructed to independently prove the integrity of the corpus rather than validating generator self-assertions. Furthermore, deliberate adversarial fixtures were applied in memory to verify that the validation suite successfully catches and rejects data mutations reproducing previous defects.

---

## 2. Core Validation Rules (24/24 Passed)

| Rule ID | Integrity Rule Description | Tested Standard | Result |
| :---: | :--- | :--- | :---: |
| **Rule 01** | Every inventory PDF has SHA-256 cryptographic hash | Prompt 1 Sec 1 | **PASS** |
| **Rule 02** | Every source record maps to an existing source document ID | Prompt 1 Sec 2 | **PASS** |
| **Rule 03** | Every record has physical page and source file provenance | Prompt 1 Sec 2 | **PASS** |
| **Rule 04** | No fabricated marks; every physically established mark has source evidence | Prompt 1.2 Rules A & C | **PASS** |
| **Rule 05** | No unknown provenance is replaced with placeholder guesses | Prompt 1 Sec 3 | **PASS** |
| **Rule 06** | Real damage audit is populated with valid damage records and covers all fragments | Prompt 1.2 Rule H | **PASS** |
| **Rule 07** | Every question occurrence has a valid wording state (null for containers and fragments) | Prompt 1.1 Sec 4 | **PASS** |
| **Rule 08** | No solution/reference material accidentally assigned to Tier 1 | Prompt 1 Sec 4 | **PASS** |
| **Rule 09** | No active/in-scope/syllabus fields introduced in Phase 1 | Hard Boundary | **PASS** |
| **Rule 10** | No canonical question relationships or deduplication created | Hard Boundary | **PASS** |
| **Rule 11** | No structural parent container is counted as an answerable question | Prompt 1.2 Rule D | **PASS** |
| **Rule 12** | No non-question source fragment is answerable | Prompt 1.2 Rules B & E | **PASS** |
| **Rule 13** | Every STATE B question has complete verified reconstruction metadata | Prompt 1.1 Sec 7 | **PASS** |
| **Rule 14** | No VERIFIED visual item exists without explicit inspection evidence | Prompt 1.2 Rule F | **PASS** |
| **Rule 15** | Automated visual presence detection is distinct from verification | Prompt 1.2 Rule G | **PASS** |
| **Rule 16** | Practice Assignment does not appear as exam_type | Prompt 1.1 Sec 11 | **PASS** |
| **Rule 17** | Unverified Question Bank authority is not promoted to Tier 2 | Prompt 1 Sec 4 | **PASS** |
| **Rule 18** | All question records have valid record_type | Prompt 1.2 Sec 5 | **PASS** |
| **Rule 19** | Question counts reconcile dynamically from JSON dataset | Prompt 1.2 Rule J | **PASS** |
| **Rule 20** | No active question contains marks-only equation or cross-question contamination | Prompt 1.2 Rule K | **PASS** |
| **Rule 21** | Every question referencing an essential visual has source-visual metadata | Prompt 1.1 Sec 8 | **PASS** |
| **Rule 22** | DOC-31 classification is consistent at Tier 3 Authority Unconfirmed across inventory and records | Prompt 1.2 Sec 13 | **PASS** |
| **Rule 23** | STATE C items have explicit incomplete evidence | Prompt 1.2 Rule I | **PASS** |
| **Rule 24** | Machine-readable summary metrics synchronize exactly with JSON dataset | Prompt 1.2 Sec 16 | **PASS** |

---

## 3. Adversarial Mutation Self-Test Suite (6/6 Passed)

To ensure the validator cannot be tricked by generator bugs, 6 deliberate corruption fixtures were tested in memory against the validator logic:

| Test ID | Adversarial Mutation Scenario | Target Defect | Validator Response | Test Result |
| :---: | :--- | :--- | :--- | :---: |
| **Test A** | Injected record with `marks: "12"`, `marks_status: "physically_established"`, but `marks_source_evidence: null` | Fabricated fallback marks (Rule L) | Validator raised `AssertionError`: Detected physically_established mark without evidence | **PASS (REJECTED)** |
| **Test B** | Injected record with partial marks evidence (`evidence_text: null`) | Incomplete provenance evidence | Validator raised `AssertionError`: Incomplete marks evidence | **PASS (REJECTED)** |
| **Test C** | Injected record with text `"+ 6 + 3 = 12"` marked as `is_student_answerable: true` | Answerable marks fragment | Validator raised `AssertionError`: Answerable marks-only fragment detected | **PASS (REJECTED)** |
| **Test D** | Injected page with `visual_verification_status: "VERIFIED"` but `review_record: null` | Unverified visual claim (Rule M) | Validator raised `AssertionError`: Verified page lacking review record | **PASS (REJECTED)** |
| **Test E** | Replaced `DAMAGED_AND_INCOMPLETE_QUESTIONS_AUDIT.json` with an empty list `[]` while 111 fragments exist | Empty damage audit (Rule N) | Validator raised `AssertionError`: Damage audit is empty despite deterministic damage | **PASS (REJECTED)** |
| **Test F** | Mismatched DOC-31 tier between inventory (Tier 3) and records (Tier 2) | Cross-artifact inconsistency | Validator raised `AssertionError`: Classification/tier mismatch across artifacts | **PASS (REJECTED)** |

**Adversarial Suite Outcome:** All 6 adversarial corruptions were immediately caught and rejected by the validator.

---

## 4. Independent Special Audit: DOC-28 Q7 to Q12

An independent verification script ([scripts/check_doc28_q7_12.py](file:///d:/DOWNLOADS/CSE2101/scripts/check_doc28_q7_12.py)) audited Questions 7 to 12 across 11 verification dimensions:

1. **DOC-28-P02-MCQ-Q07:** Page 2, STATE B, Marks: null (not_specified), Complete: Yes, Visual Required: No, Layout reassembly: Complete. -> **PASS**
2. **DOC-28-P02-MCQ-Q08:** Page 2, STATE B, Marks: null (not_specified), Complete: Yes, Visual Required: Yes (C code `void fun(struct node* start)` preserved from raster xref 22). -> **PASS**
3. **DOC-28-P02-MCQ-Q09:** Page 2, STATE B, Marks: null (not_specified), Complete: Yes, Visual Required: Yes (BFS graph diagram linked). -> **PASS**
4. **DOC-28-P02-MCQ-Q10:** Page 2, STATE B, Marks: null (not_specified), Complete: Yes, Visual Required: Yes (Binary tree diagram linked from raster xref 24). -> **PASS**
5. **DOC-28-P02-MCQ-Q11:** Page 2, STATE B, Marks: null (not_specified), Complete: Yes, Visual Required: No, Q7 contamination purged. -> **PASS**
6. **DOC-28-P03-MCQ-Q12:** Page 3, STATE A, Marks: null (not_specified), Complete: Yes, Visual Required: No, Verbatim vector extraction intact. -> **PASS**

**DOC-28 Audit Outcome:** 6/6 questions independently verified.

---

## 5. Reconciled Machine-Derived Metrics

All counts below are synchronized with [CORPUS_SUMMARY_METRICS.json](file:///d:/DOWNLOADS/CSE2101/CORPUS_SUMMARY_METRICS.json):

```json
{
  "documents": 33,
  "pages": 579,
  "physical_records": 1584,
  "paper_question_containers": 213,
  "question_occurrences": 1260,
  "atomic_sub_questions": 825,
  "standalone_questions": 435,
  "non_question_source_fragments": 111,
  "state_a": 1255,
  "state_b": 5,
  "state_c": 0,
  "complete": 1260,
  "incomplete": 0,
  "flagged_extraction": 391,
  "visual_detected": 225,
  "visual_rendered": 546,
  "visual_reviewed": 1,
  "visual_verified": 1,
  "visual_flagged": 23,
  "damage_records": 507,
  "unresolved_damage_records": 391,
  "validation_rules_passed": 24,
  "validation_rules_failed": 0
}
```

---

## 6. Release Quality Gate Assessment

| Gate Requirement | Condition | Status |
| :--- | :--- | :---: |
| 1. Zero fabricated mark fallbacks | Strict prohibition of `q_marks or "12"` | **MET** |
| 2. Marks source evidence | Every physically established mark has provenance evidence | **MET** |
| 3. Marks fragments not answerable | Categorized as `non_question_source_fragment` | **MET** |
| 4. Independent validator | Tests fail on corrupt fixtures (Rules L, M, N) | **MET** |
| 5. Evidence-based visual verification | Distinct states `DETECTED`, `RENDERED`, `VISUALLY_REVIEWED`, `VERIFIED` | **MET** |
| 6. Visual review records | `VERIFIED` only where review record exists (DOC-28 Page 2) | **MET** |
| 7. Real damage audit | 507 deterministic damage records populated | **MET** |
| 8. No hidden corruption | All anomalies tracked with zero silent discards | **MET** |
| 9. DOC-31 consistency | Consistent Tier 3 Authority Unconfirmed across all files | **MET** |
| 10. Dynamic reconciliation | $1584 = 213 + 1260 + 111$ derived from JSON | **MET** |
| 11. Source PDFs unaltered | All 33 canonical PDFs unchanged | **MET** |
| 12. No Phase 2 actions | Zero syllabus mapping, deduplication, solutions, or UI | **MET** |

**Final Quality Gate Verdict: PHASE 1.2 STATUS: PASS**
