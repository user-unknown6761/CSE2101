# DSA EXAM SYSTEM — ARCHITECTURAL DECISION REGISTER (ADR)
**Course Code:** CSE / CSEN 2101 (Data Structures and Algorithms)  
**Document Version:** 1.1.0 — RECONCILED & LOCKED  
**Status:** BINDING & AUTHORITATIVE  
**Phase:** Prompt 0.1 Governance Reconciliation  
**Date:** October 2026  

---

## 1. REGISTER OVERVIEW & CLASSIFICATION TAXONOMY

This Architectural Decision Register documents all foundational product and engineering decisions governing the CSE/CSEN 2101 exam-preparation platform.

### Decision Authority & Attribution
- **`USER-MANDATED`**: Decisions stemming directly from authoritative user prompts.
- **`ARCHITECTURE-SELECTED UNDER DELEGATED CHOICE`**: Architectural selections where technical execution was delegated to engineering best practices.
- **`DEFERRED IMPLEMENTATION DECISION`**: Technical decisions explicitly deferred to later implementation phases (e.g. framework choice, diagram renderer, exact JSON schemas).

```
Categories:
- SCP : Scope & Curriculum Boundaries
- AIN : Academic Integrity & Sourced Grounding
- SOL : Solution Verification & Mathematical Rigor
- TAX : Taxonomy, Duplication & Family Architecture
- TCH : Technical & Programming Standards
- PED : Pedagogical & Adaptive Study Engine
- DAT : Data Layer & Architectural Separation
- UIX : User Interface, Presentation & Print Standards
```

---

## 2. RECONCILED DECISION MATRIX

| Decision ID | Cat | Decision Title | Decision Type | Status | Scope / Rule Summary | Strict Prohibition | Phase Gate |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **PDR-001** | `AIN` | Zero Synthetic Questions | USER-MANDATED | `LOCKED` | 100% sourced questions only. Exactly zero synthetic, AI-generated, or invented questions across all subsystems. | No AI mock questions, no synthetic numericals, no invented variants, no synthetic gap-fillers. | Phase 1 & 2 Gates |
| **PDR-002** | `AIN` | Authoritative Source Hierarchy | USER-MANDATED | `LOCKED` | Tier 1 (Official PYQs) > Tier 2 (Question Banks) > Tier 3 (Problem Sets). Tier 4 is reference only. Tier 5 disabled. | No treating Tier 4 solutions as automatically correct. Zero Tier 5 content. | Phase 1 Audit Gate |
| **PDR-003** | `SCP` | Syllabus Hard Boundary & Module 3 Exclusion | USER-MANDATED | `LOCKED` | Module 1 (FULL), Module 2 (FULL), Module 4 (Selected algorithms only). Module 3 is strictly out of scope. | Module 3 topics must never enter active learning, revision, mastery, or mock exams. | Phase 2 Syllabus Gate |
| **PDR-004** | `SCP` | Module 1 & 2 Syllabus Gating (No Inference) | USER-MANDATED | `LOCKED` | "Module 1/2 — full" means the complete content of the authoritative supplied syllabus document. | Never invent, assume, or infer Module 1/2 subtopics from general DSA knowledge. `SYLLABUS_INPUT_REQUIRED.md` gates extraction. | Phase 2 Syllabus Gate |
| **PDR-005** | `SCP` | Module 4 Explicit Algorithm Inclusions | USER-MANDATED | `LOCKED` | Sorting: Bubble, Bubble Opt, Cocktail, Insertion (Best/Worst/Avg), Selection, Max-Heapify, Build-Max-Heap, Quick Sort. Searching: Sequential, Binary (Worst/Avg), Interpolation. | No Merge Sort, Shell Sort, Radix Sort, or non-listed sorting/searching algorithms. | Phase 2 Syllabus Gate |
| **PDR-006** | `SCP` | Quick Sort Complexity Analysis Restriction | USER-MANDATED | `LOCKED` | Quick Sort algorithm and partitioning are in-scope; complexity analysis is excluded from examination answers. | Never make Quick Sort complexity analysis an examination requirement or mock exam question. | Phase 4 & 7 Gates |
| **PDR-007** | `SCP` | Supporting Prerequisites Policy | USER-MANDATED | `LOCKED` | Non-syllabus prerequisites permitted only when essential for in-syllabus understanding, tagged as `SUPPORTING PREREQUISITE`. | Prerequisites must never expand the active syllabus or count toward exam readiness scores. | Phase 2 Syllabus Gate |
| **PDR-008** | `AIN` | Defective Source Question Exclusion | USER-MANDATED | `LOCKED` | Any source question with cut-off text, missing input, missing continuation, or missing required diagram is excluded. | Never guess, reconstruct from outside memory, or silently repair physically damaged questions. | Phase 1 Audit Gate |
| **PDR-009** | `AIN` | Unknown Provenance Policy | USER-MANDATED | `LOCKED` | When source does not establish year, branch, exam type, or marks, store `NULL / UNKNOWN`. Source metadata is authoritative evidence only when physically established by the source. | Never guess provenance. Never infer year/branch from filename or subject matter alone. | Phase 1 Audit Gate |
| **PDR-010** | `AIN` | Student-Facing Provenance Display | ARCHITECTURE-SELECTED UNDER DELEGATED CHOICE | `LOCKED` | Compact view: `[YEAR] · [BRANCH] · [EXAM]` where available, or `Question Bank`. Expandable drawer for deep metadata. | Avoid visual clutter in primary question views. No anonymous untracked questions. | Phase 9 & 10 Gates |
| **PDR-011** | `AIN` | Three-State Wording Model | USER-MANDATED | `LOCKED` | State A (Exact verbatim) > State B (Reconstructed from immediate page context & labeled) > State C (Incomplete $\rightarrow$ Exclude). | Never rewrite source questions into generic paraphrases using outside knowledge. | Phase 1 & 3 Gates |
| **PDR-012** | `AIN` | Official Marks Integrity | USER-MANDATED | `LOCKED` | Explicit source marks preserved exactly. If unstated, display "Marks not specified". | Never estimate marks and present the estimate as official. | Phase 1 Audit Gate |
| **PDR-013** | `SOL` | Independent Solution Verification | USER-MANDATED | `LOCKED` | Every distinct question independently solved/verified; cross-checked against Tier 4 keys with discrepancy logging. | Never blindly adopt supplied solutions. Never silently preserve errors from answer keys. | Phase 4 Verification Gate |
| **PDR-014** | `SOL` | Verification Methods Matched to Question Type | ARCHITECTURE-SELECTED UNDER DELEGATED CHOICE | `LOCKED` | Verification uses algorithmic reasoning, code analysis, dry run, complexity derivation, or structural reasoning. | Do not mandate formal mathematical proof where algorithmic or trace analysis is appropriate. | Phase 4 Verification Gate |
| **PDR-015** | `TAX` | Seven-Class Question Categorization | USER-MANDATED | `LOCKED` | Exact Duplicate, Near Duplicate, Data Variant, Structural Variant, Method Variant, Reverse Variant, Unique. | Never collapse distinct variants together merely to reduce database size. | Phase 3 Taxonomy Gate |
| **PDR-016** | `TAX` | Canonical Question Mapping | USER-MANDATED | `LOCKED` | Exact and near duplicates map to 1 Canonical Question with all confirmed historical occurrences linked. | Never create redundant study pages for identical questions. | Phase 3 Taxonomy Gate |
| **PDR-017** | `TAX` | Material Variant Dedicated Solution Mandate | USER-MANDATED | `LOCKED` | Data, structural, method, and reverse variants receive complete, dedicated, independent solutions. | Never substitute "Same as above" or "Exercise left to reader" for a real variant. | Phase 4 Verification Gate |
| **PDR-018** | `TAX` | Five-Tier Hierarchical Taxonomy | USER-MANDATED | `LOCKED` | Module $\longrightarrow$ Topic $\longrightarrow$ Core Question Family $\longrightarrow$ Question Form $\longrightarrow$ Source Question. | Never create ad-hoc question forms unsupported by actual source materials. | Phase 3 Taxonomy Gate |
| **PDR-019** | `TAX` | Factual Recurrence Over Prediction | USER-MANDATED | `LOCKED` | Show factual multi-year occurrences (`Seen in 2021, 2023, 2025`). | Never produce likelihood scores, probability percentages, or exam predictions. | Phase 3 & 7 Gates |
| **PDR-020** | `TAX` | Multi-Branch Unified Learning Model | USER-MANDATED | `LOCKED` | Unify CSE, AIML, DS, IoT under common conceptual families while preserving individual source provenance. | Never erase branch origin or homogenize specialized examination records. | Phase 1 & 3 Gates |
| **PDR-021** | `TAX` | Multipart Question Decomposition | USER-MANDATED | `LOCKED` | Preserve complete original exam paper questions; decompose sub-parts for mapping and mastery. | Never destroy original multi-part question context. | Phase 1 & 3 Gates |
| **PDR-022** | `TCH` | C Language Scope (Code Questions Only) | USER-MANDATED | `LOCKED` | All code-based DSA implementations use C. Theory gets theory, algorithm gets algorithm, etc. | Do not globally label every solution as C. No C++, Java, or Python in code answers. | Phase 4 & 5 Gates |
| **PDR-023** | `TCH` | C Language Standard (Standard & Portable) | USER-MANDATED | `LOCKED` | Standard, portable C; avoid compiler-specific extensions. Specific C standard uncommitted in governance. | Do not prematurely lock ANSI/C99 or specific compiler dialect in governance. | Phase 4 Gate |
| **PDR-024** | `TCH` | Question-Type-Specific Solution Structures | USER-MANDATED | `LOCKED` | Solution structures adapt directly to what was asked (Algorithm, Pseudocode, C Program, Trace, Complexity, Explain). | Do not force identical boilerplate sections onto every question type. | Phase 4 & 5 Gates |
| **PDR-025** | `TCH` | Selective State Tracing Standard | ARCHITECTURE-SELECTED UNDER DELEGATED CHOICE | `LOCKED` | Detailed tabular state traces generated only when asked, required for state transition, or materially aiding understanding. | Do not generate exhaustive traces for every algorithm simply because it exists. | Phase 5 Trace Gate |
| **PDR-026** | `TCH` | Dual Diagram Representations | ARCHITECTURE-SELECTED UNDER DELEGATED CHOICE | `LOCKED` | Learning View (rich, detailed) vs. Exam View (technically correct, clear, fast to draw, hand-reproducible). | Do not reduce learning diagrams to sketches; no decorative graphics obscuring logic. | Phase 5 Visual Gate |
| **PDR-027** | `TCH` | Diagram Technology Selection | DEFERRED IMPLEMENTATION DECISION | `LOCKED` | Diagram rendering format (SVG, HTML/CSS, ASCII, KaTeX/MathJax) deferred to implementation phases based on content needs. | Do not hard-code diagram rendering technologies in governance. | Phase 5 & 9 Gates |
| **PDR-028** | `PED` | Prohibition of Conversational AI Chatbot | USER-MANDATED | `LOCKED` | Exactly zero AI tutors, chatbots, "Ask AI", or floating dialog agents. Mistake handling is deterministic. | Never build an open-ended conversational chatbot or conversational hint engine. | Phase 7 & 9 Gates |
| **PDR-029** | `PED` | Nine-Category Diagnostic Error Triage | USER-MANDATED | `LOCKED` | Systematic classification of errors into 9 failure modes with smallest useful intervention. | Never generate new synthetic questions to remediate student weaknesses. | Phase 7 Engine Gate |
| **PDR-030** | `PED` | Corpus-Depth Aware Mastery Model | USER-MANDATED | `LOCKED` | Mastery requires evidence from available sourced questions. 2–3 questions desirable when supported by corpus depth. | If family has 1 question, do NOT invent questions; record "Insufficient corpus depth for multi-question evidence". | Phase 7 Engine Gate |
| **PDR-031** | `PED` | Adaptive Spaced Revision Engine | ARCHITECTURE-SELECTED UNDER DELEGATED CHOICE | `LOCKED` | Dynamic interval scheduling prioritized by student error frequency, hesitation, and exam proximity. | No static uniform flashcard queues. | Phase 7 Engine Gate |
| **PDR-032** | `PED` | Source-Grounded Active Recall | USER-MANDATED | `LOCKED` | Flashcards and recall triggers sourced strictly from verified questions and syllabus facts. | Recall must never become a backdoor for generating synthetic examination questions. | Phase 7 Engine Gate |
| **PDR-033** | `PED` | Dual-Mode Mock Examination Engine | USER-MANDATED | `LOCKED` | Mode 1: Authentic Paper Mode (replica of actual papers). Mode 2: Custom Source-Only Mode. Zero synthetic items. | Never include generated or unverified questions in mock exams. | Phase 8 Exam Gate |
| **PDR-034** | `SCP` | Out-of-Syllabus Archive Quarantine | USER-MANDATED | `LOCKED` | All Module 3 and unapproved questions segregated in dedicated queryable archive with conflict tags. | Never leak quarantined questions into active study, revision, or readiness calculations. | Phase 2 Syllabus Gate |
| **PDR-035** | `DAT` | Decoupled Academic Data Architecture | DEFERRED IMPLEMENTATION DECISION | `LOCKED` | Academic content stored in structured data models, fully isolated from UI presentation. Exact JSON schema deferred to Phase 6. | Never hard-code questions, solutions, or proofs inside UI templates. | Phase 6 Data Gate |
| **PDR-036** | `DAT` | Local Persistence Target: localStorage | ARCHITECTURE-SELECTED UNDER DELEGATED CHOICE | `LOCKED` | Current persistence target is browser `localStorage` with abstract repository pattern. | Do not add IndexedDB, cloud storage, backend user accounts, or sync at this stage. | Phase 6 & 10 Gates |
| **PDR-037** | `UIX` | Frontend Framework & Stack Selection | DEFERRED IMPLEMENTATION DECISION | `LOCKED` | Framework and stack selection (React, Next.js, Vanilla, TypeScript, etc.) deferred to Phase 9/10 architecture. | Do not hard-code frontend frameworks, bundlers, or specific files in governance. | Phase 9 & 10 Gates |
| **PDR-038** | `UIX` | Student Environment Usability Standard | ARCHITECTURE-SELECTED UNDER DELEGATED CHOICE | `LOCKED` | Full question corpus must remain responsive, smooth, and usable on target student devices; empirical benchmarks in Phase 10/11. | Do not establish arbitrary speculative numeric latency targets in governance. | Phase 10 & 11 Gates |
| **PDR-039** | `UIX` | Clean Exam Sheet / Print View | ARCHITECTURE-SELECTED UNDER DELEGATED CHOICE | `LOCKED` | Dedicated print stylesheet removing UI navigation, preserving questions, answers, code, diagrams, and tables. | Clean print stylesheet; devoid of simulated handwriting or artificial sketch effects. | Phase 10 Print Gate |
| **PDR-040** | `AIN` | Readiness Score Policy | USER-MANDATED | `LOCKED` | Readiness formulated strictly on verified coverage of syllabus families; target ~92–95% exam readiness. | Never guarantee, market, or promise a specific numerical exam mark or grade. | Phase 7 Engine Gate |
| **PDR-041** | `AIN` | Document Classification Precedence | USER-MANDATED | `LOCKED` | Phase 1 explicitly models DOCUMENT CLASSIFICATION before QUESTION EXTRACTION. | Never extract question instances without first establishing document-level classification and Tier. | Phase 1 Audit Gate |

---

## 3. DEFERRED UI DESIGN REFERENCE (PHASE 9/10 DIRECTION)

The project visual aesthetic is guided by the official Refero design reference:
- **Design Reference URL:** [https://styles.refero.design/style/7088d695-362b-4e09-b325-fa8136d4f350](https://styles.refero.design/style/7088d695-362b-4e09-b325-fa8136d4f350)
- **Status:** Deferred design reference for Phase 9 (UI Design System) and Phase 10 (Frontend Application).
- **Core Aesthetic:** Balanced modern textbook density, elegant typographic hierarchy, clean contrast for C code listings, restrained functional transitions, and complete absence of decorative animations.
- **Phase 1 Isolation:** This reference has zero impact on Phase 1 data audit, document classification, or raw question extraction.

---
*Ratified and locked into project governance.*
