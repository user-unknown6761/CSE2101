# CSE2101 — Raw Corpus Statistics
**Phase 1: Source Corpus Audit & Ingestion**  
**Generated On:** 2026-10-01  

---

## 1. Primary Ingestion Metrics

| Metric | Count | Governance / Source Rule |
| :--- | :---: | :--- |
| **Total Source Documents** | **33** | Discovered across repository root and nested subdirectories |
| **Total Source PDFs** | **33** | Canonical immutable PDF artifacts |
| **Total Corpus Pages** | **579** | Audited across all 33 documents |
| **Total Raw Characters Extracted** | **660,272** | Digital text extracted directly via PyMuPDF |
| **Total Question Occurrences Extracted** | **1,584** | Every physical occurrence preserved without deduplication |
| **Total Multipart Questions (Parent Groups)** | **265** | Preserved with atomic child sub-question links |
| **Total Atomic Sub-Question Occurrences** | **825** | Linked via `parent_question_instance_id` |
| **Total Source-Incomplete Occurrences (State C)** | **0** | Excluded from active raw question corpus |
| **Total Flagged / Reconstructed Occurrences (State B)** | **5** | Reconstructed safely from page visual layout |
| **Total Exact Occurrences (State A)** | **1,579** | Verbatim extraction from digital vector source |

---

## 2. Breakdown by Document Classification

| Document Classification | Document Count | Question Occurrences Extracted | Total Pages |
| :--- | :---: | :---: | :---: |
| **University Examination Paper** | 20 | 977 | 86 |
| **Backlog / Special Examination Paper** | 2 | 86 | 8 |
| **Official / Institutional Question Bank** | 1 | 99 | 30 |
| **Objective Question Bank** | 1 | 191 | 187 |
| **Practice / Problem Set** | 1 | 126 | 14 |
| **Solution Document / Answer Key** | 2 | 97 | 34 |
| **Notes / Study Material** | 6 | 0 | 220 |
| **Total** | **33** | **1,584** | **579** |

---

## 3. Breakdown by Source Tier

| Source Tier | Classification Description | Document Count | Question Occurrences Extracted | Evidentiary Role |
| :--- | :--- | :---: | :---: | :--- |
| **Tier 1** | Confirmed official university examination papers | 22 | 1,063 | Primary exam authority |
| **Tier 2** | Confirmed official / institutional question banks | 1 | 99 | Institutional curriculum authority |
| **Tier 3** | Supplied problem sets, assignments & objective QB | 2 | 317 | Supplementary academic practice |
| **Tier 4** | Solutions, answer keys, study notes, lecture slides | 8 | 97 | Reference & verification only |
| **Tier 5** | AI / Synthetically generated questions | 0 | 0 | **STRICTLY DISABLED (Rule 1)** |
| **Total** | | **33** | **1,584** | |

---

## 4. Breakdown by Established Examination Year (Where Established)

| Academic Year | Established Documents | Question Occurrences | Document IDs |
| :--- | :---: | :---: | :--- |
| **2020** | 4 | 133 | `DOC-01` (Backlog), `DOC-18` (Solution), `DOC-21` (Backlog) |
| **2021** | 7 | 258 | `DOC-02`, `DOC-19` (Solution), `DOC-20`, `DOC-22` (AEIE), `DOC-23` (AEIE), `DOC-25` (BT), `DOC-26` |
| **2022** | 3 | 144 | `DOC-03` (AIML), `DOC-04` (CSE), `DOC-05` (DS) |
| **2023** | 4 | 212 | `DOC-06` (AIML), `DOC-07` (CSE), `DOC-08` (DS), `DOC-09` (IOT) |
| **2024** | 3 | 147 | `DOC-10` (AIML), `DOC-11` (CSE), `DOC-12` (DS) |
| **2025** | 4 | 212 | `DOC-13` (AIML), `DOC-14` (CSE), `DOC-15` (DS), `DOC-16` (IOT) |
| **Unspecified / Question Banks** | 8 | 478 | `DOC-17`, `DOC-24`, `DOC-27`, `DOC-28`, `DOC-29`, `DOC-30`, `DOC-31`, `DOC-32`, `DOC-33` |

---

## 5. Breakdown by Established Branch (Where Established)

| Academic Branch | Established Documents | Question Occurrences | Document IDs |
| :--- | :---: | :---: | :--- |
| **CSE** | 5 | 223 | `DOC-01`, `DOC-02`, `DOC-04`, `DOC-07`, `DOC-11`, `DOC-14`, `DOC-18`, `DOC-19`, `DOC-20`, `DOC-21`, `DOC-26` |
| **CSE / AIML / DS** | 6 | 291 | `DOC-03`, `DOC-05`, `DOC-10`, `DOC-12` |
| **CSE / AIML / DS / IOT** | 8 | 424 | `DOC-06`, `DOC-08`, `DOC-09`, `DOC-13`, `DOC-15`, `DOC-16` |
| **AEIE (Applied Electronics)** | 2 | 92 | `DOC-22`, `DOC-23` (Course CSEN 2004) |
| **BT (Biotechnology)** | 1 | 40 | `DOC-25` (Course CSEN 2005) |
| **Unspecified / General Notes** | 11 | 514 | `DOC-17`, `DOC-24`, `DOC-27`, `DOC-28`, `DOC-29`, `DOC-30`, `DOC-31`, `DOC-32`, `DOC-33` |

---

## 6. Critical Non-Inference Integrity Note
In strict accordance with Prompt 1 Section 19, 20, 25, and 34:
- ZERO syllabus topic mapping was performed in this phase.
- ZERO question deduplication or canonical question merging was performed.
- ZERO model solutions were created.
- ZERO synthetic questions were generated.
