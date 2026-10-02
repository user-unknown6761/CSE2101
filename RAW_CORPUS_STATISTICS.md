# CSE2101 — Raw Corpus Statistics
**Phase 1.3A: Final Integrity Closure & Release Gate Certification**  
**Corpus Name:** user-unknown6761/CSE2101  
**Generated On:** 2026-10-02  
**Status:** FULLY RECONCILED & INDEPENDENTLY VALIDATED (33/33 Core Rules Passed, 19/19 Adversarial Mutations Passed)

---

## 1. Primary Ingestion Metrics

| Metric | Count | Governance / Source Rule |
| :--- | :---: | :--- |
| **Total Source Documents** | **33** | Discovered across repository root and nested subdirectories |
| **Total Source PDFs** | **33** | Canonical immutable PDF artifacts with recomputed SHA-256 byte validation |
| **Total Corpus Pages** | **579** | Audited across all 33 documents |
| **Total Raw Characters Extracted** | **660,272** | Digital text extracted directly via PyMuPDF |
| **Total Physical Source Records** | **1,584** | Every physical entry preserved in `RAW_EXTRACTED_QUESTIONS.json` |
| **Paper Question Containers (Parent Groups)** | **213** | Structural non-answerable parent groupings (`record_type: paper_question_container`) |
| **Non-Question Source Fragments** | **111** | Physical marks equations, CO footers, noise fragments (`record_type: non_question_source_fragment`) |
| **True Atomic Question Occurrences** | **1,260** | **Actual student-answerable question occurrences** (`record_type: question_occurrence`) |
| **— Atomic Sub-Question Occurrences** | **825** | Sub-questions `(a)`, `(b)`, `(i)`, `(ii)` linked to containers |
| **— Standalone Question Occurrences** | **435** | Single-part questions without parent containers |
| **Total Exact Occurrences (State A)** | **1,255** | Verbatim extraction from digital vector source |
| **Total Reconstructed Occurrences (State B)** | **5** | Safely reconstructed from rendered source visual (DOC-28 Q7–Q11) |
| **Total Source-Incomplete Occurrences (State C)** | **0** | Zero unrecoverable fatal cutoffs |
| **Visual Pages Detected** | **238** | Pages containing images/drawings via automated presence analysis |
| **Visual Pages Rendered** | **1** | Pages backed by actual physical render artifacts on disk (`rendered_pages/DOC-28_page_2.png`) |
| **Visual Pages Reviewed** | **1** | DOC-28 Page 2 reviewed via `DOC28_PAGE2_RECONSTRUCTION_AUDIT.md` and `DOC28_Q9_VISUAL_SEMANTIC_AUDIT.md` |
| **Visual Pages Verified** | **1** | DOC-28 Page 2 verified with full review record and verification basis |
| **Visual Pages Flagged** | **154** | Pages with complex vector/raster graphics or scanned elements requiring review |
| **Document Rendering Status (DOC-28)** | **PARTIALLY_RENDERED** | 1 of 14 pages physically rendered (`rendering_complete: false` across all 33 docs) |
| **Document Rendering Status (Others)** | **NOT_RENDERED (32)** | Remaining 32 documents have no rendered pages |
| **Deterministic Damage Audit Entries** | **507** | Fully audited in `DAMAGED_AND_INCOMPLETE_QUESTIONS_AUDIT.json` (116 Resolved, 391 Warnings) |
| **Deterministic Damage Conditions** | **507** | Exact bijection with independent detector `(qid, detector_id, damage_type, severity, resolution_status)` |
| **Total Flagged Heuristic Anomalies** | **391** | Tracked in `SUSPICIOUS_EXTRACTION_AUDIT.json` without silent deletion |
| **Core Validation Rules Passed** | **33 / 33** | Certified by `validate_phase1.py` (Rules 01 through 33) |
| **Adversarial Mutation Tests Passed** | **19 / 19** | True in-memory mutation test suite (`test_phase1_validator_mutations.py`) |
| **Formal Schema Validation** | **PASS** | `PHASE1_SCHEMA.json` validated across all 4 production deliverables |

---

## 2. Breakdown by Document Classification

| Document Classification | Document Count | Total Records | Paper Containers | True Question Occurrences | Non-Question Fragments | Total Pages |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **University Examination Paper** | 20 | 985 | 180 | 701 | 104 | 86 |
| **Backlog / Special Examination Paper** | 2 | 86 | 16 | 68 | 2 | 8 |
| **Question Bank — Authority Unconfirmed** (`DOC-30`) | 1 | 99 | 0 | 99 | 0 | 30 |
| **Objective Question Bank — Authority Unconfirmed** (`DOC-31`) | 1 | 191 | 0 | 191 | 0 | 187 |
| **Practice / Problem Set** (`DOC-28`) | 1 | 126 | 0 | 126 | 0 | 14 |
| **Solution Document / Answer Key** | 2 | 97 | 17 | 75 | 5 | 34 |
| **Notes / Study Material** | 6 | 0 | 0 | 0 | 0 | 220 |
| **Total** | **33** | **1,584** | **213** | **1,260** | **111** | **579** |

---

## 3. Breakdown by Source Tier

| Source Tier | Classification Description | Document Count | Total Records | Containers | True Question Occurrences | Non-Question Fragments | Evidentiary Role |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Tier 1** | Confirmed official university examination papers | 22 | 1,071 | 196 | 769 | 106 | Primary exam authority |
| **Tier 2** | Confirmed official / institutional question banks | 0 | 0 | 0 | 0 | 0 | None confirmed without institutional seal |
| **Tier 3** | Problem sets, assignments, unconfirmed question banks | 3 | 416 | 0 | 416 | 0 | Supplementary academic practice |
| **Tier 4** | Solutions, answer keys, study notes, lecture slides | 8 | 97 | 17 | 75 | 5 | Reference & verification only |
| **Tier 5** | AI / Synthetically generated questions | 0 | 0 | 0 | 0 | 0 | **STRICTLY DISABLED (Rule 1)** |
| **Total** | | **33** | **1,584** | **213** | **1,260** | **111** | |

---

## 4. Breakdown by Established Examination Year (Where Established)

| Academic Year | Total Records | Paper Containers | True Question Occurrences | Non-Question Fragments | Document IDs |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **2020** | 133 | 25 | 101 | 7 | `DOC-01` (Backlog), `DOC-18` (Solution), `DOC-21` (Backlog) |
| **2021** | 320 | 62 | 237 | 21 | `DOC-02`, `DOC-19` (Solution), `DOC-20`, `DOC-22` (AEIE), `DOC-23` (AEIE), `DOC-25` (BT), `DOC-26` |
| **2022** | 144 | 27 | 96 | 21 | `DOC-03` (AIML), `DOC-04` (CSE), `DOC-05` (DS) |
| **2023** | 212 | 36 | 144 | 32 | `DOC-06` (AIML), `DOC-07` (CSE), `DOC-08` (DS), `DOC-09` (IOT) |
| **2024** | 147 | 27 | 114 | 6 | `DOC-10` (AIML), `DOC-11` (CSE), `DOC-12` (DS) |
| **2025** | 212 | 36 | 152 | 24 | `DOC-13` (AIML), `DOC-14` (CSE), `DOC-15` (DS), `DOC-16` (IOT) |
| **Unspecified / Question Banks** | 416 | 0 | 416 | 0 | `DOC-17`, `DOC-24`, `DOC-27`, `DOC-28`, `DOC-29`, `DOC-30`, `DOC-31`, `DOC-32`, `DOC-33` |
| **Total** | **1,584** | **213** | **1,260** | **111** | |

---

## 5. Breakdown by Established Branch (Where Established)

| Academic Branch | Total Records | Paper Containers | True Question Occurrences | Non-Question Fragments | Document IDs |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **AEIE (Applied Electronics)** | 92 | 18 | 68 | 6 | `DOC-22`, `DOC-23` (Course CSEN 2004) |
| **BT (Biotechnology)** | 40 | 9 | 28 | 3 | `DOC-25` (Course CSEN 2005) |
| **CSE** | 321 | 60 | 242 | 19 | `DOC-01`, `DOC-02`, `DOC-04`, `DOC-07`, `DOC-11`, `DOC-14`, `DOC-18`, `DOC-19`, `DOC-20`, `DOC-21`, `DOC-26` |
| **CSE / AIML / DS** | 144 | 27 | 96 | 21 | `DOC-03`, `DOC-05`, `DOC-10`, `DOC-12` |
| **CSE / AIML / DS / IOT** | 571 | 99 | 410 | 62 | `DOC-06`, `DOC-08`, `DOC-09`, `DOC-13`, `DOC-15`, `DOC-16` |
| **Unspecified / General Notes** | 416 | 0 | 416 | 0 | `DOC-17`, `DOC-24`, `DOC-27`, `DOC-28`, `DOC-29`, `DOC-30`, `DOC-31`, `DOC-32`, `DOC-33` |
| **Total** | **1,584** | **213** | **1,260** | **111** | |

---

## 6. Critical Non-Inference Integrity Note
In strict accordance with Prompt 1, Prompt 1.1, and Prompt 1.2:
- ZERO syllabus topic mapping was performed in this phase.
- ZERO question deduplication or canonical question merging was performed.
- ZERO model solutions were created.
- ZERO synthetic questions were generated.
- ZERO structural parent containers or non-question fragments enter student question-family or solution pipelines.
- ZERO fabricated marks or fallback values exist in the dataset.
