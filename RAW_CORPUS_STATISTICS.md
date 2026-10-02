# CSE2101 — Raw Corpus Statistics
**Phase 1.1: Extraction Integrity Correction**  
**Corpus Name:** user-unknown6761/CSE2101  
**Generated On:** 2026-10-02  
**Status:** FULLY RECONCILED (22/22 Validation Rules Passed)

---

## 1. Primary Ingestion Metrics

| Metric | Count | Governance / Source Rule |
| :--- | :---: | :--- |
| **Total Source Documents** | **33** | Discovered across repository root and nested subdirectories |
| **Total Source PDFs** | **33** | Canonical immutable PDF artifacts |
| **Total Corpus Pages** | **579** | Audited across all 33 documents |
| **Total Raw Characters Extracted** | **660,272** | Digital text extracted directly via PyMuPDF |
| **Total Physical Source Records** | **1,584** | Every physical entry preserved in `RAW_EXTRACTED_QUESTIONS.json` |
| **Paper Question Containers (Parent Groups)** | **227** | Structural non-answerable parent groupings (`record_type: paper_question_container`) |
| **True Atomic Question Occurrences** | **1,357** | **Actual student-answerable question occurrences** (`record_type: question_occurrence`) |
| **— Atomic Sub-Question Occurrences** | **825** | Sub-questions `(a)`, `(b)`, `(i)`, `(ii)` linked to containers |
| **— Standalone Question Occurrences** | **532** | Single-part questions without parent containers |
| **Total Exact Occurrences (State A)** | **1,352** | Verbatim extraction from digital vector source |
| **Total Reconstructed Occurrences (State B)** | **5** | Safely reconstructed from rendered source visual (DOC-28 Q7–Q11) |
| **Total Source-Incomplete Occurrences (State C)** | **0** | Zero unrecoverable fatal cutoffs |
| **Total Flagged Heuristic Anomalies** | **98** | Tracked in `SUSPICIOUS_EXTRACTION_AUDIT.json` without silent deletion |

---

## 2. Breakdown by Document Classification

| Document Classification | Document Count | Total Records | Paper Containers | True Question Occurrences | Total Pages |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **University Examination Paper** | 20 | 985 | 191 | 794 | 86 |
| **Backlog / Special Examination Paper** | 2 | 86 | 16 | 70 | 8 |
| **Question Bank — Authority Unconfirmed** (`DOC-30`) | 1 | 99 | 0 | 99 | 30 |
| **Objective Question Bank — Authority Unconfirmed** (`DOC-31`) | 1 | 191 | 0 | 191 | 187 |
| **Practice / Problem Set** (`DOC-28`) | 1 | 126 | 0 | 126 | 14 |
| **Solution Document / Answer Key** | 2 | 97 | 20 | 77 | 34 |
| **Notes / Study Material** | 6 | 0 | 0 | 0 | 220 |
| **Total** | **33** | **1,584** | **227** | **1,357** | **579** |

---

## 3. Breakdown by Source Tier

| Source Tier | Classification Description | Document Count | Total Records | Containers | True Question Occurrences | Evidentiary Role |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Tier 1** | Confirmed official university examination papers | 22 | 1,071 | 207 | 864 | Primary exam authority |
| **Tier 2** | Confirmed official / institutional question banks | 0 | 0 | 0 | 0 | None confirmed without institutional seal |
| **Tier 3** | Problem sets, assignments, unconfirmed question banks | 3 | 416 | 0 | 416 | Supplementary academic practice |
| **Tier 4** | Solutions, answer keys, study notes, lecture slides | 8 | 97 | 20 | 77 | Reference & verification only |
| **Tier 5** | AI / Synthetically generated questions | 0 | 0 | 0 | 0 | **STRICTLY DISABLED (Rule 1)** |
| **Total** | | **33** | **1,584** | **227** | **1,357** | |

---

## 4. Breakdown by Established Examination Year (Where Established)

| Academic Year | Established Documents | Total Records | Paper Containers | True Question Occurrences | Document IDs |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **2020** | 4 | 133 | 24 | 109 | `DOC-01` (Backlog), `DOC-18` (Solution), `DOC-21` (Backlog) |
| **2021** | 7 | 258 | 49 | 209 | `DOC-02`, `DOC-19` (Solution), `DOC-20`, `DOC-22` (AEIE), `DOC-23` (AEIE), `DOC-25` (BT), `DOC-26` |
| **2022** | 3 | 144 | 26 | 118 | `DOC-03` (AIML), `DOC-04` (CSE), `DOC-05` (DS) |
| **2023** | 4 | 212 | 43 | 169 | `DOC-06` (AIML), `DOC-07` (CSE), `DOC-08` (DS), `DOC-09` (IOT) |
| **2024** | 3 | 147 | 37 | 110 | `DOC-10` (AIML), `DOC-11` (CSE), `DOC-12` (DS) |
| **2025** | 4 | 212 | 48 | 164 | `DOC-13` (AIML), `DOC-14` (CSE), `DOC-15` (DS), `DOC-16` (IOT) |
| **Unspecified / Question Banks** | 8 | 478 | 0 | 478 | `DOC-17`, `DOC-24`, `DOC-27`, `DOC-28`, `DOC-29`, `DOC-30`, `DOC-31`, `DOC-32`, `DOC-33` |
| **Total** | **33** | **1,584** | **227** | **1,357** | |

---

## 5. Breakdown by Established Branch (Where Established)

| Academic Branch | Established Documents | Total Records | Paper Containers | True Question Occurrences | Document IDs |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **CSE** | 5 | 223 | 42 | 181 | `DOC-01`, `DOC-02`, `DOC-04`, `DOC-07`, `DOC-11`, `DOC-14`, `DOC-18`, `DOC-19`, `DOC-20`, `DOC-21`, `DOC-26` |
| **CSE / AIML / DS** | 6 | 291 | 63 | 228 | `DOC-03`, `DOC-05`, `DOC-10`, `DOC-12` |
| **CSE / AIML / DS / IOT** | 8 | 424 | 91 | 333 | `DOC-06`, `DOC-08`, `DOC-09`, `DOC-13`, `DOC-15`, `DOC-16` |
| **AEIE (Applied Electronics)** | 2 | 92 | 22 | 70 | `DOC-22`, `DOC-23` (Course CSEN 2004) |
| **BT (Biotechnology)** | 1 | 40 | 9 | 31 | `DOC-25` (Course CSEN 2005) |
| **Unspecified / General Notes** | 11 | 514 | 0 | 514 | `DOC-17`, `DOC-24`, `DOC-27`, `DOC-28`, `DOC-29`, `DOC-30`, `DOC-31`, `DOC-32`, `DOC-33` |
| **Total** | **33** | **1,584** | **227** | **1,357** | |

---

## 6. Critical Non-Inference Integrity Note
In strict accordance with Prompt 1 and Prompt 1.1:
- ZERO syllabus topic mapping was performed in this phase.
- ZERO question deduplication or canonical question merging was performed.
- ZERO model solutions were created.
- ZERO synthetic questions were generated.
- ZERO structural parent containers enter question-family or solution pipelines.
