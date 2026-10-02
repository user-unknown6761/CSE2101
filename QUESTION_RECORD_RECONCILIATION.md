# CSE2101 — Question Record Reconciliation Report
**Phase 1.1: Extraction Integrity Correction**  
**Corpus Name:** user-unknown6761/CSE2101  
**Generated Date:** 2026-10-02  
**Status:** COMPLETE & RECONCILED (22/22 Validation Rules Passed)

---

## 1. Executive Reconciliation Summary

In accordance with Prompt 1.1 Sections 1 and 2, this document provides the formal mathematical and structural reconciliation between the initial Phase 1 extraction and the corrected Phase 1.1 two-tier question model.

The prior Phase 1 implementation erroneously treated structural parent question containers (e.g., "Question 3", "Question 4", "Question 5" in Group B, C, D exam sections) as standalone question occurrences. These parent records contained synthetic placeholder wording, unallocated marks aggregates, and distorted the true count of student-answerable questions. 

Under the revised Phase 1.1 schema, the corpus strictly decouples **Paper Question Containers** from **Question Occurrences**.

---

## 2. Core Reconciliation Metrics

| Metric Category | Prior Count (Phase 1) | Corrected Count (Phase 1.1) | Net Delta | Structural Rationale |
| :--- | :---: | :---: | :---: | :--- |
| **Total Source Records** | **1,584** | **1,584** | **0** | Total physical entry rows preserved in `RAW_EXTRACTED_QUESTIONS.json` |
| **Paper Question Containers** | 0 *(unseparated)* | **227** | **+227** | Structural parent headers (`record_type: paper_question_container`) |
| **Atomic Sub-Question Occurrences** | 825 | **825** | **0** | Constituent sub-questions (`(a)`, `(b)`, `(i)`, `(ii)`) |
| **Standalone Question Occurrences** | 759 *(conflated)* | **532** | **-227** | True standalone single-part questions (`occurrence_type: standalone`) |
| **True Atomic Question Occurrences** | **1,584** *(conflated)* | **1,357** | **-227** | **Actual student-answerable questions** (`is_student_answerable: true`) |

---

## 3. Mathematical Reconciliation Proof

The 1,584 records in [RAW_EXTRACTED_QUESTIONS.json](file:///d:/DOWNLOADS/CSE2101/RAW_EXTRACTED_QUESTIONS.json) satisfy the following exact equalities:

$$\text{Total Records (1,584)} = \text{Paper Question Containers (227)} + \text{True Question Occurrences (1,357)}$$

$$\text{True Question Occurrences (1,357)} = \text{Atomic Sub-Questions (825)} + \text{Standalone Questions (532)}$$

```
TOTAL SOURCE RECORDS (1,584)
├── PAPER QUESTION CONTAINERS (227)
│   ├── Group A Containers (e.g., Q1 objective headers): 24
│   └── Group B/C/D/E Containers (e.g., Q2-Q9 multipart headers): 203
└── TRUE QUESTION OCCURRENCES (1,357) [is_student_answerable: true]
    ├── Atomic Sub-Questions (825) [occurrence_type: sub_question]
    │   ├── Group A short items (i) to (xv): 244
    │   └── Multipart sub-questions (a), (b), (c): 581
    └── Standalone Questions (532) [occurrence_type: standalone]
        ├── Exam standalone questions: 85
        ├── DOC-28 Practice Assignment (MCQ + SA + LA): 126
        ├── DOC-30 Topic Question Bank: 130
        └── DOC-31 Objective & Descriptive Question Bank: 191
```

---

## 4. Why the Counts Changed

### 4.1 Root Cause of Prior Distortion
In semester exam papers (e.g. 2023 CSE, 2024 AIML), a paper question typically presents as:
```text
3. (a) Define AVL tree. State balance factor.                  [3]
   (b) Construct an AVL tree with elements: 14, 17, 11, 7, ... [5]
```
The original extraction created three records:
1. `Question 3` (marks: 8 or unallocated) — **Structural container**
2. `Question 3(a)` (marks: 3) — Sub-question
3. `Question 3(b)` (marks: 5) — Sub-question

Under the old scheme, all 3 records were classified as `question_occurrence`, giving a total of 3 "questions". If a student were asked how many questions they answered, they answered 3(a) and 3(b). Treating "Question 3" as a 3rd question created artificial question inflation (+227 non-questions).

### 4.2 Strict Architectural Remediation (Rule 11 & Rule 12)
1. **Zero Fake Wording:** All 227 `paper_question_container` records have `raw_text: null`. No synthetic "Question 3" strings are treated as question stems.
2. **Zero Inferred Marks:** Containers have `marks: null` and `marks_status: "container_aggregate_unallocated"`.
3. **Non-Answerable Status:** All containers have `is_student_answerable: false`.
4. **Clean Downstream Boundary:** Containers are explicitly blocked from entering:
   - Syllabus and topic mapping (Phase 2)
   - Question-family classification and recurrence clustering (Phase 2)
   - Student mastery tracking
   - Model solution requirements (Phase 3)
5. **Bidirectional Provenance Preserved:**
   - Every container lists its children in `child_question_instance_ids`.
   - Every atomic sub-question references its container in `parent_question_container_id`.

---

## 5. Verification Against Source Corpus

Automated validation rule 19 in [validate_phase1.py](file:///d:/DOWNLOADS/CSE2101/scripts/validate_phase1.py) asserts and certifies this exact breakdown:
- Rule 19 assertion: `(cont_cnt + true_cnt == 1584) and (sub_cnt + stand_cnt == 1357) and (cont_cnt == 227) and (sub_cnt == 825) and (stand_cnt == 532)`
- Result: **PASS** (Zero discrepancies).
