# DSA EXAM SYSTEM (CSE/CSEN 2101) — GOVERNANCE REVIEW MANIFEST
**Project Name:** CSE / CSEN 2101 Data Structures & Algorithms Exam Preparation System  
**Document Version:** 1.1.0 — RECONCILED GOVERNANCE BASELINE  
**Timestamp (UTC):** 2026-10-01T15:38:00Z  
**Local Time:** 2026-10-01T21:08:00+05:30  
**Git Commit Hash:** `6dd5ed8e3e13bdeb9d011e1a4d8f3979ff121e2e` (Short: `6dd5ed8`)  
**Status:** AUDITED, PASS, GATED  

---

## 1. REVIEW SUMMARY & PURPOSE

This manifest accompanies the **Prompt 0.1 Corrected Governance Baseline**. It provides an external auditor or reviewer with complete traceability, SHA-256 integrity hashes, directory structure, and instructions to inspect the ratified engineering constitution, decision register, non-negotiables checklist, pipeline, and correction logs.

---

## 2. PUBLIC REVIEW URLS & CHECKSUMS

| Resource | URL / Location | SHA-256 Checksum | Size |
| :--- | :--- | :--- | :--- |
| **Governance Review Bundle (ZIP)** | [Download Review ZIP](https://tmpfiles.org/dl/wBAeAUBSH15z/cse2101_governance_review_bundle.zip) | `a36cf345ea6434209eeb0273ef73be3ed6c13a4b23acadba1300b8d4d7066b90` | 30.1 KB |
| **Governance Review Web View** | [View on tmpfiles.org](https://tmpfiles.org/wBAeAUBSH15z/cse2101_governance_review_bundle.zip) | — | — |
| **Full Project Archive (ZIP)** | [Download Full Project ZIP](https://tmpfiles.org/dl/wMAXAkGC48Hn/cse2101_project.zip) | *(Includes 33 source PDFs + Governance)* | 28.5 MB |
| **Raw Source Corpus Archive (ZIP)** | [Download Source ZIP](https://tmpfiles.org/dl/w8AWAgJDPsON/source.zip) | *(Contains 33 physical PDFs in SOURCE)* | 28.5 MB |
| **Local Repository Path** | `d:\DOWNLOADS\CSE2101\` | Git branch: `master` @ commit `6dd5ed8` | — |

---

## 3. COMPLETE GOVERNANCE FILE INVENTORY & INTEGRITY HASHES

| File Path | Description | Size | SHA-256 Hash |
| :--- | :--- | :--- | :--- |
| `PROJECT_SYSTEM_CONTRACT.md` | Formalized 30+ constitutional clauses without unapproved assumptions. | 19,931 bytes | `f27fbbab6a2f4988a45f0b46ce52982bdfc5a00c65d30efd5918bff19381dad0` |
| `PROJECT_DECISION_REGISTER.md` | 40 locked product & engineering decisions with explicit authority tags. | 13,981 bytes | `1f9c25aecfd6b576ca0c521de34c98838aa681808ad19f1f302acb6b50cc27b3` |
| `PROJECT_NON_NEGOTIABLES.md` | Compact builder's compliance checklist for all subsequent phases. | 7,761 bytes | `d10feb04f6eea411736936bd01b0f0ec628a84ade1137edc4547ec16cbfff734` |
| `PROJECT_PIPELINE.md` | Corrected 13-phase engineering pipeline (Phase 0 through Phase 12). | 19,131 bytes | `1496a5c93573aad9192d9e13c20f5b546f931628b01be40303b686ed543954f7` |
| `GOVERNANCE_CORRECTION_LOG.md` | Audit log of all 12 reconciled discrepancies between Prompt 0 and 0.1. | 8,781 bytes | `ad7855ab99b332d218af923eedc67e64732a418af8210254b16eb280766920bf` |
| `SYLLABUS_INPUT_REQUIRED.md` | Formal notice gating Phase 2 on the delivery of authoritative syllabus text. | 4,248 bytes | `72a0eb9a4898b0a1118ec71e566132ad5ff11a0ee79e11eb172bf0698cc2c89f` |
| `REVIEW_MANIFEST.md` | This verification manifest. | ~4,500 bytes | Tracked in bundle |

---

## 4. WORKSPACE DIRECTORY TREE

```
d:\DOWNLOADS\CSE2101/
├── .git/                                         [Local Git Repository]
├── GOVERNANCE_CORRECTION_LOG.md                  [Audit & Discrepancy Log]
├── PROJECT_DECISION_REGISTER.md                  [Architectural Decision Register (ADR)]
├── PROJECT_NON_NEGOTIABLES.md                    [Compact Constitutional Checklist]
├── PROJECT_PIPELINE.md                           [13-Phase Engineering Pipeline]
├── PROJECT_SYSTEM_CONTRACT.md                    [Authoritative System Contract]
├── REVIEW_MANIFEST.md                            [Review & Verification Manifest]
├── SYLLABUS_INPUT_REQUIRED.md                    [Syllabus Dependency Gate Notice]
├── CSE2101_GOVERNANCE_REVIEW_BUNDLE.zip          [30.1 KB Review Archive]
├── CSE2101_Project.zip                           [28.5 MB Full Project Archive]
├── SOURCE.zip                                    [28.5 MB Source Only Archive]
└── SOURCE/                                       [Physical Source Corpus - 33 PDFs]
    ├── 2020_CSE2101_CSE_..._Backlog.pdf
    ├── 2021_CSE2101_CSE_...pdf
    ├── ... (14 additional root exam papers 2022-2025)
    └── DSA-20260930T180448Z-1-001/
        └── DSA/
            ├── 1782225402814.pdf
            ├── 2020 DSA Solution.pdf
            ├── 2021 DSA Solution.pdf
            ├── ... (14 additional question banks, problem sets, and solutions)
```

---

## 5. REPRODUCIBILITY & VERIFICATION INSTRUCTIONS

To inspect and verify the governance artifacts independently:

1. **Download the Review Bundle:**
   ```bash
   curl -s -L -o review_bundle.zip https://tmpfiles.org/dl/wBAeAUBSH15z/cse2101_governance_review_bundle.zip
   ```
2. **Verify SHA-256 Checksum:**
   ```bash
   # Windows PowerShell:
   (Get-FileHash review_bundle.zip -Algorithm SHA256).Hash -eq "a36cf345ea6434209eeb0273ef73be3ed6c13a4b23acadba1300b8d4d7066b90"

   # Linux/macOS:
   sha256sum review_bundle.zip
   ```
3. **Extract & Inspect:**
   ```bash
   unzip review_bundle.zip
   ```
4. **Run Cross-Document Consistency Check:**
   Verify that all documents maintain 100% compliance with `PROJECT_NON_NEGOTIABLES.md` (e.g. zero synthetic questions, no inferred Module 1/2 subtopics, C restricted to code questions, unknown provenance preserved as `null`, `localStorage` persistence, and no conversational chatbot).

---

## 6. CLEANLINESS CERTIFICATION

It is certified that:
- **Zero Secrets / Credentials:** No API keys, tokens, or environment credentials exist in the bundle.
- **Zero Temporary Build Artifacts:** No `.env` files, build caches, or `node_modules` directories are present.
- **Physical Corpus Untouched:** In accordance with Prompt 0.1 instructions, none of the 33 source PDFs were modified, parsed, or processed during this governance reconciliation phase.

---
*Ratified and locked into project governance.*
