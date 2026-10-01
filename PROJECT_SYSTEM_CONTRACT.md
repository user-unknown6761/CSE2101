# DSA EXAM SYSTEM — SYSTEM CONTRACT & ENGINEERING CONSTITUTION
**Course Code:** CSE / CSEN 2101 (Data Structures and Algorithms)  
**Document Version:** 1.1.0 — RECONCILED & AUTHORITATIVE  
**Status:** RATIFIED & BINDING  
**Phase:** Prompt 0.1 Corrected Governance Baseline  
**Date:** October 2026  

---

## 1. PROJECT IDENTITY & PURPOSE

### 1.1 Academic Context
- **Subject:** Data Structures and Algorithms.
- **Course & Curriculum Context:** CSE / CSEN 2101 (exact nomenclature established in authoritative source materials; no alternate course metadata shall be fabricated).
- **Target Audience:** Undergraduate engineering students preparing for university semester examinations. The student is assumed to be a beginner who may rely heavily on this system for reliable, high-yield preparation.
- **Product Nature:** A **premium digital exam-preparation book + intelligent, source-grounded study engine**.
- **Exclusions:** This system is **NOT** a generic educational app, **NOT** an AI conversational tutor, and **NOT** an AI question generator.
- **Target Preparation Quality:** Approximately 92–95% exam readiness based on verified coverage of syllabus-valid examination questions. The system shall **NEVER** promise, market, or guarantee a specific numerical score, grade, or percentage.

---

## 2. NON-NEGOTIABLE CORE CONSTITUTION

### Rule 2.1 — Zero Generated Exam Questions (Absolute Rule)
The final system may contain **ONLY** questions that physically exist in the supplied source corpus.
- **Strictly Prohibited:** Synthetic questions, invented numerical problems, invented coding challenges, artificial variants, "similar questions", generated reverse problems, AI-created mock questions, and gap-filler questions.
- **Scope of Prohibition:** Applies universally across all subsystems: active learning, practice, mastery evaluation, revision scheduling, mock exams, active recall, and remediation.
- **Recall & Remediation Boundary:** Recall triggers and diagnostic remediation may test already-established syllabus material and methods, but may **NEVER** create new standalone questions.

### Rule 2.2 — Authoritative Source Grounding
The supplied source corpus is the sole authority for:
- What questions exist
- Original question wording
- Source metadata (year, branch, exam type, paper identifier)
- Official marks (only when explicitly stated in the source paper)
- Factual historical recurrence
- Source-specific variations

General DSA theoretical knowledge is utilized exclusively to explain concepts and independently verify solutions. External knowledge must **NEVER** be used to invent source questions, fabricate provenance, manufacture recurrence, or silently alter source content.

### Rule 2.3 — Strict Syllabus Boundary & Module 3 Quarantine
Active learning, mastery, revision, adaptive study selection, mock exams, next-best-action logic, and exam readiness calculations are strictly confined to:

1. **MODULE 1 — FULL:** The complete content of the authoritative supplied syllabus for Module 1.
2. **MODULE 2 — FULL:** The complete content of the authoritative supplied syllabus for Module 2.
3. **MODULE 4 — ONLY THE FOLLOWING TOPICS:**
   - **Sorting:**
     - Bubble Sort
     - Bubble Sort Optimizations
     - Cocktail Shaker Sort
     - Insertion Sort (Best-case analysis, Worst-case analysis, Average-case analysis)
     - Selection Sort
     - Max-Heapify
     - Build-Max-Heap
     - Quick Sort (**CRITICAL RULE:** Algorithm and partitioning logic only; **NO complexity-analysis requirement** in examination answers).
   - **Searching:**
     - Sequential Search
     - Binary Search (Worst-case analysis, Average-case analysis)
     - Interpolation Search

#### Absolute Syllabus Constraints:
- **MODULE 3 IS STRICTLY OUT OF SCOPE.** Any question originating from Module 3 or any topic outside the explicit list above must **NEVER** enter active study. All such questions are quarantined in a dedicated Out-of-Syllabus Archive.
- **NO INVENTED SYLLABUS DETAILS:** Detailed sub-topics of Module 1 and Module 2 must **NOT** be invented, assumed, or inferred from general DSA knowledge, file names, question bank contents, or memory. "Module 1 — full" and "Module 2 — full" mean the *complete content of the authoritative supplied syllabus for those modules*. If the authoritative syllabus document is absent from the workspace, it must not be fabricated; `SYLLABUS_INPUT_REQUIRED.md` enforces this gate until authoritative text is supplied.

### Rule 2.4 — Supporting Prerequisites Policy
When a foundational prerequisite concept outside the active syllabus is genuinely necessary to understand or solve an otherwise in-syllabus question:
- It must be explicitly tagged and displayed as a **`SUPPORTING PREREQUISITE`**.
- It is **NOT** part of the active examination syllabus.
- It must **NEVER** expand the active syllabus, contribute to active syllabus coverage, or enter readiness calculations.

### Rule 2.5 — Incomplete Source Question Exclusion & Three-State Wording Model
If a physical source question is defective due to missing continuation, missing required input data, missing essential diagrams, missing essential code, cut-off pages, or unreadable essential text:
- **EXCLUDE IT COMPLETELY** from the active examination corpus.
- Do **NOT** reconstruct missing content from assumptions or external knowledge.
- Do **NOT** guess what the missing portion was or silently repair the question.
- Record the exclusion, source file, page, and exact defect in `DAMAGED_AND_INCOMPLETE_QUESTIONS_AUDIT.json`.

#### Three-State Wording Decision Model:
- **State A — Exact:** The source wording is confidently recoverable. $\longrightarrow$ Preserve verbatim.
- **State B — Reconstructed:** The physical source is complete, but text extraction or OCR exhibits minor typographical/spacing glitches and the intended wording can be safely reconstructed from the immediate source page context. $\longrightarrow$ Preserve the reconstruction and clearly label: `"Reconstructed from source"`.
- **State C — Source-Incomplete:** The source itself is missing essential information. $\longrightarrow$ **EXCLUDE** from active corpus. OCR uncertainty must not be confused with a physically incomplete source.

---

## 3. SOURCE PROVENANCE & RECORD INTEGRITY

### 3.1 Unknown Fields Remain Unknown
The source bundle contains university examination papers, backlog papers, departmental question banks, practice problem sheets, and notes. For any provenance field that the physical source does not explicitly establish:
$$\mathbf{STORE\ NULL\ /\ UNKNOWN}$$
- **NEVER** guess or invent metadata.
- **NEVER** infer year from filename alone unless verified evidence exists and the classification process explicitly logs the evidence.
- **NEVER** infer engineering branch from subject matter alone.
- **NEVER** infer official exam session status from a filename alone.

### 3.2 Provenance Tracking Schema
Every sourced question records:
- `source_file`: Filename of the source document
- `page_number`: Page number when available (`null` if unpaginated/unknown)
- `source_type`: e.g. `University_Exam_Paper`, `Question_Bank`, `Practice_Assignment`
- `source_tier`: Tier 1, Tier 2, or Tier 3
- `branch`: Engineering branch when established (`null` if unstated)
- `year`: Examination year when established (`null` if unstated)
- `exam_type`: Session when established (e.g. `Regular`, `Backlog`, `null`)
- `paper_id`: Official course/paper identifier when established (`null` if unstated)
- `question_number`: Question identifier when established (`null` if unstated)
- `sub_question_id`: Sub-part identifier when established (`null` if unstated)
- `marks`: Numerical marks when explicitly present in source (`null` if unstated)
- `extraction_confidence`: Quality rating (`High`, `Medium`, `Flagged`)
- `completeness_status`: Verification status (`Complete`, `Incomplete_Quarantined`)

### 3.3 Student-Facing Provenance Display
Default question provenance is compact and uncluttered:
- Where established: **`YEAR · BRANCH · EXAM`** *(e.g., `2024 · CSE · Regular` or `2024 · CSE · Backlog`)*.
- Where insufficient/bank source: **`Question Bank`** or **`Practice Assignment`**.
- An expandable "Source Details" drawer exposes source filename, page number, question number, and known archive metadata without cluttering the primary study view.

### 3.4 Marks Policy
- If marks are explicitly stated in the source: Preserve them exactly.
- If marks are absent: Display as `"Marks not specified"`.
- Never estimate marks and present the estimate as official. Internal answer depth classification is pedagogical and does not replace official marks.

---

## 4. INDEPENDENT SOLUTION VERIFICATION PROTOCOL

### 4.1 Verification Mandate
Every distinct eligible source question requires an independently verified solution authored by subject-matter expertise.
- **Tier 4 Status:** Supplied solutions, answer keys, and student notes are **REFERENCE ONLY** and are never assumed to be correct.
- **Workflow:** Source Question $\longrightarrow$ Independent Verification $\longrightarrow$ Compare with Supplied Key (if available) $\longrightarrow$ Identify Discrepancies $\longrightarrow$ Resolve Rigorously $\longrightarrow$ Store Verified Solution $\longrightarrow$ Retain Discrepancy Log.
- **Prohibition on Blind Adoption:** Never copy supplied solutions without independent derivation. Never silently preserve an incorrect supplied solution.

### 4.2 Verification Methods Adapted by Question Type
Verification must match the question form; formal mathematical proof is **NOT** required for every question:
- Theory & Discussion $\longrightarrow$ Conceptual and structural reasoning
- Code Implementation $\longrightarrow$ Code analysis, compilation, and pointer safety verification
- Dry Run / Tracing $\longrightarrow$ Step-by-step state-transition dry run
- Complexity Questions $\longrightarrow$ Formal asymptotic derivation and recurrence expansion
- Algorithmic Questions $\longrightarrow$ Algorithmic correctness arguments and invariant verification
- Mathematical / Numerical $\longrightarrow$ Step-by-step mathematical reasoning and calculation check

---

## 5. TAXONOMY: DUPLICATES, VARIANTS & CANONICAL FAMILIES

### 5.1 Question Classification Taxonomy
Every sourced question instance is categorized into one of seven classes:
1. **Exact Duplicate:** Identical wording, parameters, and structure.
2. **Near Duplicate:** Negligible syntactic variation with identical intent.
3. **Data / Input Variation:** Same conceptual requirement, different input dataset (e.g. different array numbers for sorting).
4. **Structural Variation:** Same core concept applied to a different data structure variant (e.g. Queue via Array vs. Circular Queue vs. Linked Queue).
5. **Method Variation:** Same problem solved via alternative method specified by source (e.g. recursive vs. iterative BST traversal).
6. **Reverse / Inference Variation:** Inverse reasoning required (e.g. constructing tree from traversal pairs).
7. **Genuinely Unique:** Distinct pedagogical requirement.

### 5.2 Canonical Questions & Material Variants
- **Exact & Near Duplicates:** Map to **ONE** Canonical Question with **ONE** complete verified solution. Consolidate and preserve all confirmed source occurrences:
  *(e.g., "Seen in 2021 CSE, 2023 AIML, 2025 DS")*.
- **Material Variants (Data, Structural, Method, Reverse):** Group under a common family concept, but author a **COMPLETE, DEDICATED INDEPENDENT SOLUTION** for each variant. Never write *"Same as above"* or *"Left as an exercise"*.

### 5.3 Factual Recurrence Over Prediction
Repeated questions provide factual historical evidence, **NOT** predictive foresight.
- Expose factual historical occurrences: *"Seen in 2021, 2023, 2025"*.
- **Strictly Prohibited:** Assigning likelihood scores, probability percentages, "high yield forecasts", or claims of exam prediction.

---

## 6. PROGRAMMING LANGUAGE & SOLUTION TEMPLATES

### 6.1 C Programming Language Scope
**ALL CODE-BASED DSA IMPLEMENTATIONS USE C.**
- This does **NOT** mean every question is solved in C.
- Solutions adapt directly to what the question asks:
  - Theory question $\longrightarrow$ Theory answer
  - Explain question $\longrightarrow$ Clear explanation
  - Algorithm question $\longrightarrow$ Formal algorithm
  - Pseudocode question $\longrightarrow$ Clean pseudocode
  - Trace question $\longrightarrow$ Tabular dry run
  - Complexity question $\longrightarrow$ Derivation and bound
  - Programming question $\longrightarrow$ Complete C program
- **C Standard:** Standard, portable C; avoid compiler-specific extensions. No specific standard (e.g. ANSI/C99/C11) is locked in governance; implementation phases will follow clean, portable C conventions.
- Algorithms and pseudocode remain language-independent when the source asks specifically for an algorithm or pseudocode.

### 6.2 Complexity Standards & Quick Sort Rule
- **Quick Sort Rule:** In accordance with the syllabus, Quick Sort is in-scope for algorithm and partition logic, but has **NO complexity-analysis requirement** in examination answers. Do not convert Quick Sort complexity into an exam requirement or mock exam test question.
- **Binary Search:** Provide formal Worst-case and Average-case analysis as explicitly mandated by the syllabus.

### 6.3 State Tracing & Dry-Run Standard
Exhaustive traces must **NOT** be generated for every algorithm simply because the algorithm exists. A detailed trace is constructed when:
1. The sourced question explicitly asks for a trace / dry run.
2. The question requires explicit state transitions to demonstrate correctness.
3. The representation materially aids understanding of a sourced question.

When required, state transitions follow a structured format:
$$\text{Initial State} \longrightarrow \text{Step / Pass} \longrightarrow \text{Changed State} \longrightarrow \text{Why It Changed} \longrightarrow \text{Next Step} \longrightarrow \text{Final Result}$$

### 6.4 Diagram Standards: Dual Representation
Where diagrams materially improve understanding, the system maintains two representations where useful:
1. **Learning View:** May be visually rich, detailed, and dynamic (utilizing SVG, HTML/CSS, structured text diagrams, or KaTeX/MathJax where appropriate).
2. **Exam View:** Must be technically correct, clear, fast to draw, and strictly **hand-reproducible** on university paper answer booklets.
- Diagram rendering technologies are not hard-coded in governance; implementation phases choose appropriate tools based on rendering requirements.
- Avoid decorative artwork that harms logical clarity.

---

## 7. PEDAGOGICAL ENGINE: DETERMINISTIC STUDY & MASTERY

### 7.1 Absolute Ban on Conversational AI Chatbot
There is **NO** AI tutor, conversational chatbot, "Ask AI", floating dialog agent, or conversational hint system in this product.
- Pedagogical intelligence is built directly into the **deterministic Study Engine**:
  $$\text{Student Answer} \longrightarrow \text{Diagnostic Error Triage} \longrightarrow \text{Targeted Concept Callout} \longrightarrow \text{Targeted Sourced Retry} \longrightarrow \text{Verified Solution} \longrightarrow \text{Weakness Update} \longrightarrow \text{Revision Scheduling}$$

### 7.2 Diagnostic Error Taxonomy
When an error occurs, the engine classifies it into one of nine root-cause failure modes:
1. `Concept Misunderstanding` (e.g. confusing LIFO with FIFO)
2. `Recognition Failure` (e.g. failing to recognize an infix evaluation pattern)
3. `Method Invalidation` (e.g. partitioning without moving both pointers)
4. `Implementation Error` (e.g. pointer dereference without NULL validation)
5. `Tracing / State Slip` (e.g. off-by-one loop index during pass 2)
6. `Complexity Derivation Gap` (e.g. miscalculating recurrence summation)
7. `Calculation Flaw` (e.g. arithmetic mistake in binary search mid)
8. `Presentation / Format Omission` (e.g. missing algorithm termination step)
9. `Recall Decay` (e.g. forgetting tree height definition)

### 7.3 Corpus-Depth Aware Mastery Architecture
Mastery is evidence-based and cannot be achieved by merely marking an item as read or viewing an answer.
- **Evidence Ladder:**
  1. Trigger Recognition
  2. Rule / Method Recall
  3. Solving Canonical Sourced Question
  4. Solving Materially Different Sourced Variant
  5. Additional Sourced Evidence when available
- **Corpus-Depth Awareness:** Where the corpus contains sufficient genuinely distinct questions, 2–3 distinct questions are desirable for mastery.
- **CRITICAL RULE:** If a question family has only **ONE** valid sourced question in the corpus, the system shall **NEVER** invent another question. Instead, it records:
  $$\text{"Insufficient corpus depth for multi-question mastery evidence."}$$
  Mastery logic must dynamically adapt to available corpus depth.

### 7.4 Adaptive Revision & Active Recall
- Spaced revision schedules prioritize items based on student error frequency, hesitation, and exam proximity.
- Active recall flashcards and triggers are derived strictly from verified source facts and algorithm rules. Recall may **NEVER** become a backdoor for generating synthetic examination questions.

### 7.5 Dual-Mode Mock Examination Engine
- **Mode 1: Authentic Paper Mode:** Exact digital replica of an original university paper as preserved, with historical sections, options, and marks.
- **Mode 2: Custom Source-Only Mode:** Balanced exam papers dynamically assembled exclusively from verified sourced questions across in-scope modules.
- **Absolute Rule:** Exactly ZERO synthetic or AI-authored questions in any mock exam mode.

---

## 8. SYSTEM ARCHITECTURE & INTERACTION PRINCIPLES

### 8.1 Decoupling of Academic Content and Presentation
- Academic truth (questions, solutions, traces, diagrams, provenance, recurrence) resides in structured data models.
- **Zero hardcoding** of question text or solution logic inside UI templates or presentation components.
- The exact file organization and schema will be established in Phase 6 (Academic Data Architecture).

### 8.2 Client-Side Persistence
- The current implementation persistence target is **`localStorage`**.
- Do not introduce IndexedDB, cloud storage, backend user accounts, or server synchronization unless a later phase explicitly decides to do so.
- State access logic is abstracted through a repository pattern so a backend can be attached in the future without altering data schemas.

### 8.3 Frontend Stack Independence
- The governance layer does **NOT** hard-code the frontend stack (frameworks, bundlers, or specific files such as `index.html` or `app.js`).
- Framework and tooling decisions are deferred to Phase 9 & 10 architectural phases.

### 8.4 Usability & Performance Standard
- The system must remain responsive, smooth, and fully usable across standard student devices and screen sizes.
- Arbitrary numeric latency thresholds are avoided in governance; empirical performance benchmarks belong to implementation testing.

### 8.5 Clean Exam Sheet / Print View
- The eventual system must support an **EXAM SHEET / PRINT VIEW**.
- It strips website UI navigation, header chrome, and interactive widgets, leaving a clean, high-readability study document containing: question, answer, algorithms, pseudocode, C code, diagrams, tables, and required calculations.
- It is a clean, publication-grade print document stylesheet, devoid of simulated physical handwriting effects or decorative distortions.

### 8.6 Unknown Fact Policy
- **When the authoritative source does not establish a fact, the system stores the fact as unknown rather than guessing.**
- Applies to: syllabus topics, source type, year, branch, exam type, marks, recurrence, question wording, and source authority.

---
*Ratified as the authoritative System Contract for CSE/CSEN 2101 Data Structures and Algorithms.*
