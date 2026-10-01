# DSA EXAM SYSTEM — BUILDER'S NON-NEGOTIABLES
**Course Code:** CSE / CSEN 2101 (Data Structures and Algorithms)  
**Document Version:** 1.1.0 — RECONCILED & AUTHORITATIVE  
**Status:** MANDATORY COMPLIANCE CHECKLIST  
**Phase:** Prompt 0.1 Corrected Governance Baseline  
**Date:** October 2026  

---

> ### ⚠️ CONSTITUTIONAL NOTICE TO ALL BUILDERS & SUBAGENTS
> Every engineer, builder, and autonomous agent executing any phase of this project must strictly comply with this checklist. Violating any single item halts the pipeline and invalidates the release candidate.

---

### 1. ZERO GENERATED QUESTIONS (ABSOLUTE PROHIBITION)
- [ ] **NEVER** generate synthetic or AI-authored examination questions.
- [ ] **NEVER** invent artificial numerical problems, coding exercises, or "similar/parallel" questions.
- [ ] **NEVER** create synthetic gap-filler questions or AI-written mock questions.
- [ ] **100% of all active questions MUST physically exist in the supplied source corpus.** This applies across learning, practice, mastery, revision, mocks, recall, and remediation.

### 2. EXACT SOURCE GROUNDING & TRUTHFUL PROVENANCE
- [ ] **NEVER** guess or invent provenance fields (`year`, `branch`, `exam_type`, `paper_id`, `question_number`, `marks`).
- [ ] **WHEN PROVENANCE IS NOT ESTABLISHED BY THE SOURCE, STORE NULL / UNKNOWN.**
- [ ] **NEVER** infer year or official exam status from a filename alone.
- [ ] **NEVER** infer engineering branch from subject matter alone.
- [ ] **NEVER** rewrite source questions into generic paraphrases; preserve verbatim (State A) or explicitly label minor typographical restorations as `"Reconstructed from source"` (State B).

### 3. STRICT SYLLABUS BOUNDARY & NO INVENTED TOPICS
- [ ] **ACTIVE LEARNING CONTAINS ONLY:**
  - **Module 1 (FULL):** Complete content of authoritative supplied syllabus document.
  - **Module 2 (FULL):** Complete content of authoritative supplied syllabus document.
  - **Module 4 (ONLY):**
    - *Sorting:* Bubble, Bubble Opt, Cocktail, Insertion (Best/Worst/Avg), Selection, Max-Heapify, Build-Max-Heap, Quick Sort.
    - *Searching:* Sequential, Binary (Worst/Avg), Interpolation.
- [ ] **MODULE 3 IS STRICTLY OUT OF SCOPE.**
- [ ] **DO NOT INVENT MODULE 1 OR MODULE 2 CONTENTS.** Detailed subtopics must NOT be inferred from general DSA memory; they must be extracted from an authoritative syllabus artifact in Phase 2 (`SYLLABUS_INPUT_REQUIRED.md` gates extraction).
- [ ] **NEVER** allow out-of-scope questions to enter active learning, revision, mastery, or mock exams.
- [ ] **NEVER** elevate a `SUPPORTING PREREQUISITE` into an active examination topic.

### 4. INCOMPLETE SOURCE QUESTION EXCLUSION
- [ ] **COMPLETELY EXCLUDE** any source question missing essential text, continuation, inputs, diagrams, or code.
- [ ] **NEVER** guess what the missing portion was or silently repair physically incomplete questions.
- [ ] **ALWAYS** log exclusions in the damaged questions audit ledger.

### 5. INDEPENDENT SOLUTION VERIFICATION (TIER 4 IS REFERENCE ONLY)
- [ ] **NEVER** blindly adopt supplied solutions, answer keys, or student notes without independent derivation.
- [ ] **ALWAYS** verify solutions using the method appropriate to the question type (algorithmic reasoning, code analysis, dry run, complexity derivation, mathematical reasoning).
- [ ] **ALWAYS** log discrepancies between independent derivations and flawed Tier 4 keys in the Discrepancy Ledger.

### 6. C LANGUAGE ONLY FOR CODE-BASED QUESTIONS
- [ ] **ALL CODE-BASED DSA IMPLEMENTATIONS USE C.**
- [ ] **DO NOT GLOBALLY LABEL EVERY SOLUTION AS C.** Theory questions receive theory answers, algorithm questions receive algorithms, pseudocode questions receive pseudocode, traces receive dry runs, and complexity questions receive derivations.
- [ ] **STANDARD, PORTABLE C:** Avoid compiler-specific extensions. Do not prematurely lock ANSI/C99 or specific compiler dialects in governance.
- [ ] **NO C++, Java, or Python** in student-facing code implementation answers.

### 7. DUPLICATE & VARIANT DISCIPLINE
- [ ] **Exact and near duplicates:** Map to **ONE** Canonical Question with **ONE** complete verified solution, linking all historical occurrences.
- [ ] **Material variants (data, structural, method, reverse):** Provide a **COMPLETE, DEDICATED INDEPENDENT SOLUTION** for each variant.
- [ ] **NEVER** use *"Same as above"* or *"Left as exercise"* as a substitute for solving a genuine variant.

### 8. NO CHATBOT TUTOR
- [ ] **DO NOT BUILD A CHATBOT.**
- [ ] **NO "Ask AI", NO tutor chat, NO conversational dialog widgets, NO Socratic hint bots.**
- [ ] Mistake handling is deterministic: Error $\longrightarrow$ Diagnostic classification (9 categories) $\longrightarrow$ Targeted conceptual callout $\longrightarrow$ Sourced retry $\longrightarrow$ Spaced revision scheduling.

### 9. FACTUAL RECURRENCE OVER PREDICTION
- [ ] Multi-year occurrences are documented factually: *"Seen in 2021, 2023, 2025"*.
- [ ] **NEVER** produce likelihood scores, probability percentages, "high yield forecasts", or claims of exam prediction.

### 10. CORPUS-DEPTH AWARE MASTERY
- [ ] Mastery is evidence-based (recognition, recall, canonical proof, material variant proof).
- [ ] 2–3 distinct sourced questions are desirable where supported by corpus depth.
- [ ] **IF A FAMILY HAS ONLY ONE SOURCED QUESTION, DO NOT INVENT QUESTIONS.** Record: *"Insufficient corpus depth for multi-question mastery evidence."*
- [ ] Exact duplicates do NOT count as separate mastery evidence.
- [ ] **NEVER** promise or guarantee specific exam scores or percentages to students.

### 11. QUICK SORT COMPLEXITY RESTRICTION
- [ ] Quick Sort algorithm and partitioning logic are in-scope.
- [ ] **NO COMPLEXITY-ANALYSIS REQUIREMENT in exam answers for Quick Sort.**
- [ ] **NEVER** convert Quick Sort complexity analysis into a student exam test requirement or mock exam question.
- [ ] Binary Search requires Worst-case and Average-case analysis as explicitly mandated by the syllabus.

### 12. SELECTIVE DRY RUNS & DUAL DIAGRAMS
- [ ] **DO NOT generate exhaustive traces for every algorithm simply because it exists.** Construct detailed traces only when asked, required for state transition, or materially aiding understanding.
- [ ] **Maintain two diagram representations where useful:** Learning View (rich, detailed) vs. Exam View (technically correct, clear, fast to draw, hand-reproducible).
- [ ] Do not hard-code diagram rendering technologies in governance.

### 13. DATA DECOUPLING & LOCALSTORAGE PERSISTENCE
- [ ] **ACADEMIC CONTENT MUST BE SEPARATED FROM UI CODE.** Structured data is the source of truth.
- [ ] **ZERO hard-coding of question text or solution logic inside UI templates.**
- [ ] **Current persistence target is `localStorage`.** Do not introduce IndexedDB, cloud storage, backend accounts, or sync at this stage.
- [ ] Keep state access abstract via a repository pattern for future backend compatibility.

### 14. NO PREMATURE FRAMEWORK OR PERFORMANCE ASSUMPTIONS
- [ ] **DO NOT hard-code the frontend stack in governance.** Framework and tooling decisions belong to implementation phases.
- [ ] **DO NOT establish arbitrary speculative numeric latency targets** in governance. Requirement: the corpus must remain responsive, smooth, and usable on target student environments.

### 15. CLEAN EXAM SHEET / PRINT VIEW
- [ ] Provide an **EXAM SHEET / PRINT VIEW** that strips website UI/navigation while preserving questions, answers, code, diagrams, and tables.
- [ ] The print view is a clean, publication-grade document stylesheet, devoid of simulated handwriting effects or decorative distortions.

---
*Ratified as the immutable Non-Negotiables checklist for the CSE/CSEN 2101 Exam System.*
