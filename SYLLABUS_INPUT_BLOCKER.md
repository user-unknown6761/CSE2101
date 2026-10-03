# CSE2101 DSA Exam System — Syllabus Input Blocker Report
**Document ID:** `SYLLABUS_INPUT_BLOCKER.md`  
**Phase Status:** `BLOCKED — AUTHORITATIVE SYLLABUS INPUT ABSENT`  
**Course Code:** `CSE2101` / `CSEN2101` (Data Structures and Algorithms)  
**Governance Authority:** Project Constitution, `PROJECT_NON_NEGOTIABLES.md` §3, `PROJECT_DECISION_REGISTER.md` (PDR-003, PDR-004, PDR-005, PDR-034), `SYLLABUS_INPUT_REQUIRED.md`  
**Execution Timestamp:** 2026-10-03  
**Verified Phase 1 Commit:** `d519599`  

---

## 1. Executive Summary

Phase 1 data integrity closure and hardening has fully passed all release gates:
- **37/37 Core Validation Rules Passed** (0 failed)
- **48/48 Adversarial Mutation Tests Passed** (0 failed, 100% genuine rejection rate)
- Physical page corpus completeness verified across all 579 pages of all 33 documents ($\{1..\text{page\_count}\}$, Rule 35)
- Categorical separation and structural integrity of validation-run metrics verified (Rule 36)
- Bidirectional canonical $\leftrightarrow$ legacy visual state contract verified across all 579 page records (Rule 37)
- 0 page-key mismatches
- 0 duplicate canonical page keys
- 0 summary metric mismatches
- 0 document lifecycle derivation discrepancies
- 0 visual state contradictions
- 0 formal schema violations
- 0 SHA-256 byte mismatches across all 33 source PDFs

Per the Master Execution Prompt (Section 11 & Section 17), transition to Phase 2 (*Authoritative Syllabus Extraction & Scope Gating*) requires the physical presence of an authoritative syllabus artifact for course `CSE2101` / `CSEN2101`.

A comprehensive, automated forensic search was executed across the entire repository, all 33 registered PDFs, zip bundles, and nested directories. **No authoritative syllabus artifact exists in the repository.**

In strict adherence to the project constitution and source-only governance:
- **No synthetic syllabus topics have been invented.**
- **No Module 1 or Module 2 boundaries have been inferred from textbooks, question frequency, or assistant memory.**
- **No speculative or synthetic question files (`AUTHORITATIVE_SYLLABUS.json`, `CANONICAL_SYLLABUS.json`, `ACTIVE_SYLLABUS_CORPUS.json`) have been fabricated.**

Phase 2 is formally declared:  
**`BLOCKED — AUTHORITATIVE SYLLABUS INPUT ABSENT`**

---

## 2. Forensic Search Record: What Was Searched

The following exhaustive search procedures were executed across the entire repository:

1. **Full-Corpus Text & PDF Stream Search:**
   - Evaluated all 33 registered source documents (`DOC-01` through `DOC-33`) comprising 579 physical pages in `SOURCE/`.
   - Executed pattern matching across every extracted page stream for curriculum tokens: `"syllabus"`, `"curriculum"`, `"course outline"`, `"course handout"`, `"academic regulations"`, `"lecture plan"`, `"course objectives"`, `"learning outcomes"`.
   - **Result:** Exactly 0 matches for course syllabus definitions.

2. **Repository-Wide File Search:**
   - Searched root directory, `SOURCE/`, `scripts/`, `rendered_pages/`, and documentation roots.
   - Evaluated all file extensions (`.pdf`, `.docx`, `.doc`, `.txt`, `.md`, `.json`, `.csv`).
   - Inspected archives: `CSE2101_GOVERNANCE_REVIEW_BUNDLE.zip`, `CSE2101_Project.zip`, `SOURCE.zip`.
   - **Result:** No syllabus file, curriculum booklet, or faculty syllabus handout exists in the repository.

3. **Governance & Documentation Review:**
   - Inspected `SYLLABUS_INPUT_REQUIRED.md`, `DOCUMENT_CLASSIFICATION_AUDIT.md`, `PROJECT_PIPELINE.md`, and `GOVERNANCE_CORRECTION_LOG.md`.
   - **Finding:** The project governance records explicitly confirm that `SYLLABUS_INPUT_REQUIRED.md` was created precisely because the authoritative syllabus artifact has never been supplied to the repository.

---

## 3. Candidate Files Inspected and Why They Do Not Qualify

| Candidate Category | File / Document IDs | Forensic Findings | Disqualification Rationale |
| :--- | :--- | :--- | :--- |
| **Midterm / Endterm University Exam Papers** | `DOC-01` to `DOC-16`, `DOC-20` to `DOC-23`, `DOC-25`, `DOC-26` | Contain individual exam questions. Several question headers include Course Outcome tags (`[CO1]`, `[CO2]`, `[CO3]`, `[CO4]`, `[CO5]`, `[CO6]`) and Bloom taxonomy levels (`[B2]`, `[B3]`). | **Disqualified:** Exam papers test sample subsets of material; they do NOT define the authoritative universe of examinable syllabus topics. Inferring module boundaries from CO tags would constitute unverified guesswork and violate Rule 2.1. |
| **Practice Assignment Sheet** | `DOC-28` | Contains 12 discrete DSA practice problems (linked lists, graphs, binary trees, recursion, sorting). | **Disqualified:** This is a single problem set, not a curriculum specification. |
| **Study Notes & Reference Materials (Tier 4)** | `DOC-17`, `DOC-24`, `DOC-27`, `DOC-29`, `DOC-32`, `DOC-33` | Contains informal student/faculty notes on data structures topics (arrays, stacks, queues, trees, graphs, sorting). | **Disqualified:** Isolated study notes lack institutional curriculum authority and cannot establish formal module boundaries or the locked Module 4 algorithm exclusions. |
| **Question Bank 1 (Tier 3)** | `DOC-30` | Topic-wise question-and-answer compilation for "Data Structures Using C". | **Disqualified:** Document possesses no institutional seal, university course code (`CSE2101`/`CSEN2101`), or official syllabus outline. |
| **Question Bank 2 (Tier 3)** | `DOC-31` | Objective & descriptive question bank with answers. | **Disqualified:** Explicitly marked for Course Code `DC08` under the IETE curriculum, not the university `CSE2101` / `CSEN2101` syllabus. |
| **Solution Documents (Tier 4)** | `DOC-18`, `DOC-19` | Solutions to specific historical examination questions. | **Disqualified:** Solutions contain question answers, not syllabus boundaries. |

---

## 4. Exact Artifact Required to Unblock Phase 2

To unblock Phase 2, the user must provide one of the following authoritative institutional artifacts into the repository (e.g., in a `syllabus/` directory or at workspace root):

1. **Official University / Departmental Course Syllabus Document for CSE2101 / CSEN2101**, containing:
   - **Module 1:** Official module title, complete list of topics, subtopics, and examinable competencies.
   - **Module 2:** Official module title, complete list of topics, subtopics, and examinable competencies.
   - Prescribed textbook and reference book list.
2. **Official Academic Regulations / Curriculum Booklet** covering the 2nd-year B.Tech Computer Science curriculum defining course code `CSE2101` / `CSEN2101`.
3. **Confirmed Faculty-Issued Course Handout / Lecture Plan** explicitly defining the authorized boundaries of Modules 1 and 2 for `CSE2101` / `CSEN2101`.

---

## 5. Scope Gating Invariants Ready for Phase 2 Execution

Once the authoritative syllabus document is supplied, Phase 2 will execute with the following pre-established governance invariants:

1. **Module 1 (FULL):** Sourced strictly and completely from the authoritative syllabus artifact without additions or omissions.
2. **Module 2 (FULL):** Sourced strictly and completely from the authoritative syllabus artifact without additions or omissions.
3. **Module 3:** Permanently **OUT OF SCOPE**. All Module 3 questions will be quarantined into `OUT_OF_SYLLABUS_ARCHIVE.json`.
4. **Module 4 (Locked Algorithm Whitelist):**
   - **Sorting (Strict Whitelist):** Bubble Sort, Bubble Sort optimizations, Cocktail Shaker Sort, Insertion Sort (Best/Worst/Average analysis), Selection Sort, Max-Heapify, Build-Max-Heap, Quick Sort (no complexity analysis requirement).
   - **Searching (Strict Whitelist):** Sequential Search, Binary Search (Worst/Average analysis), Interpolation Search.
   - All other sorting/searching algorithms (Merge Sort, Shell Sort, Radix Sort, etc.) are strictly OUT OF SCOPE.
5. **No Question Loss:** All 1,260 true question occurrences will be partitioned into `IN_SCOPE`, `OUT_OF_SCOPE`, or `AMBIGUOUS`. Out-of-scope questions remain preserved with source citations.
6. **Zero Synthetic Questions & Zero Solutions:** Phase 2 will perform classification and partitioning only; no deduplication, taxonomy canonicalization, or solution writing.

---

## 6. Current Operational State

- **Phase 1 Status:** `CERTIFIED COMPLETE` (Release gate passed: 37 core rules, 48 adversarial mutations).
- **Phase 2 Status:** `BLOCKED — AUTHORITATIVE SYLLABUS INPUT ABSENT`.
- **System Action:** Awaiting user provision of the authoritative syllabus artifact.
