import json
import os
import sys
import re
import copy
import hashlib
from collections import defaultdict
import jsonschema

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# AUTHORITATIVE GROUND-TRUTH RECONSTRUCTION CONSTANTS (FOR STATE B SEMANTICS)
# ==============================================================================

AUTHORITATIVE_Q8_LINES = [
    "void fun(struct node* start)",
    "{",
    "    if(start == NULL)",
    "        return;",
    "    printf(\"%d \", start->data);",
    "    if(start->next != NULL )",
    "        fun(start->next->next);",
    "    printf(\"%d \", start->data);",
    "}"
]

AUTHORITATIVE_Q9_VERTICES = {"M", "N", "O", "K", "Q", "P"}
AUTHORITATIVE_Q9_EDGES = {
    tuple(sorted(["M", "K"])),
    tuple(sorted(["M", "N"])),
    tuple(sorted(["M", "Q"])),
    tuple(sorted(["N", "O"])),
    tuple(sorted(["N", "Q"])),
    tuple(sorted(["Q", "P"])),
    tuple(sorted(["P", "O"]))
}

AUTHORITATIVE_Q10_ROOT = "1"
AUTHORITATIVE_Q10_RELATIONSHIPS = {
    ("1", "2"),
    ("2", "5"),
    ("5", "3"),
    ("5", "6"),
    ("3", "4")
}

# ==============================================================================
# REUSABLE VALIDATION FUNCTIONS (PHASE 1.3 MODULAR ARCHITECTURE)
# ==============================================================================

def validate_crypto_hashes(inventory, raise_on_error=False):
    """
    Rule 01:
    - Every inventory PDF has a 64-character SHA-256 cryptographic hash.
    - Recomputes SHA-256 directly from the actual source PDF bytes on disk.
    - Invariant: sha256(actual_pdf_bytes) == recorded_sha256 for all 33 PDFs.
    """
    for d in inventory:
        doc_id = d.get('document_id')
        sha = d.get('sha256', '')
        rel_path = d.get('relative_path')
        if not (isinstance(sha, str) and len(sha) == 64 and re.match(r'^[0-9a-fA-F]{64}$', sha)):
            msg = f"Document {doc_id} has invalid SHA-256 format: '{sha}'"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        if not rel_path or not os.path.exists(rel_path):
            msg = f"Document {doc_id} source PDF file not found at '{rel_path}'"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        with open(rel_path, 'rb') as f:
            actual_sha = hashlib.sha256(f.read()).hexdigest()

        if actual_sha.lower() != sha.lower():
            msg = f"Document {doc_id} SHA-256 mismatch: recorded '{sha}' != actual '{actual_sha}'"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

    return True, f"Recomputed and verified SHA-256 byte hashes across all {len(inventory)} PDFs."


def validate_provenance_and_ids(inventory, records, raise_on_error=False):
    """
    Rules 02, 03, 18:
    - Every source record maps to an existing source document ID.
    - Every record has physical page and source file provenance.
    - All question records have valid record_type.
    """
    valid_doc_ids = set(d['document_id'] for d in inventory)
    valid_record_types = {"paper_question_container", "question_occurrence", "non_question_source_fragment"}

    for r in records:
        inst_id = r.get('question_instance_id')
        doc_id = r.get('document_id')
        rtype = r.get('record_type')

        if doc_id not in valid_doc_ids:
            msg = f"Record {inst_id} maps to invalid document_id '{doc_id}'"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        if r.get('page_start') is None or not r.get('source_file'):
            msg = f"Record {inst_id} is missing physical page_start or source_file"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        if rtype not in valid_record_types:
            msg = f"Record {inst_id} has invalid record_type '{rtype}'"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

    return True, f"Provenance and record types verified across {len(records)} physical records."


def validate_marks_integrity(records, raise_on_error=False):
    """
    Rule 04:
    - No record has fabricated default marks.
    - Every physically established mark has source evidence (source_page, source_reference, evidence_text).
    - Unspecified marks strictly have null marks and null evidence.
    """
    valid_statuses = {"physically_established", "not_specified", "container_aggregate_unallocated"}

    for r in records:
        inst_id = r.get('question_instance_id')
        m = r.get('marks')
        m_st = r.get('marks_status')
        m_ev = r.get('marks_source_evidence')

        if m_st not in valid_statuses:
            msg = f"Record {inst_id} has invalid marks_status '{m_st}'"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        if m_st == "physically_established":
            if m is None:
                msg = f"Record {inst_id} marked physically_established but marks is None"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg
            if m_ev is None:
                msg = f"Record {inst_id} marked physically_established but marks_source_evidence is None"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg
            if not m_ev.get('evidence_text'):
                msg = f"Record {inst_id} marks_source_evidence missing evidence_text"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg
            if not m_ev.get('source_reference'):
                msg = f"Record {inst_id} marks_source_evidence missing source_reference"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg
            if m_ev.get('source_page') is None:
                msg = f"Record {inst_id} marks_source_evidence missing source_page"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg
        elif m_st in {"not_specified", "container_aggregate_unallocated"}:
            if m is not None:
                msg = f"Record {inst_id} has marks_status '{m_st}' but marks is not None: '{m}'"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg
            if m_ev is not None:
                msg = f"Record {inst_id} has marks_status '{m_st}' but marks_source_evidence is not None"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg

    return True, "Marks integrity verified: zero fabricated marks; all physically established marks have full evidence."


def validate_placeholders_and_bounds(records, raise_on_error=False):
    """
    Rules 05, 09, 10:
    - No unknown provenance is replaced with placeholder guesses ("unknown", "tbd", "placeholder", etc.).
    - No active/in-scope/syllabus fields introduced (Rule 09).
    - No canonical question relationships or deduplication created (Rule 10).
    """
    forbidden_fields = ["is_active", "in_syllabus", "canonical_id", "module_number", "topic_id", "difficulty_score"]
    placeholder_terms = {"placeholder", "unknown", "guessed", "tbd", "n/a", "none"}

    for r in records:
        inst_id = r.get('question_instance_id')
        meta = r.get('source_established_metadata', {})
        if isinstance(meta, dict):
            for k, v in meta.items():
                if isinstance(v, str) and v.strip().lower() in placeholder_terms:
                    msg = f"Record {inst_id} contains placeholder metadata '{k}': '{v}'"
                    if raise_on_error:
                        raise AssertionError(msg)
                    return False, msg

        for f in forbidden_fields:
            if f in r:
                msg = f"Record {inst_id} contains forbidden Phase 2 field '{f}'"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg

        for k in r.keys():
            if "canonical" in k.lower():
                msg = f"Record {inst_id} contains forbidden canonical field '{k}'"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg

    return True, "No placeholders, no Phase 2 fields, and no canonical deduplication keys present."


def detect_damage_candidates(records):
    """
    Independent deterministic detection function: scans physical records directly
    and produces deterministic damage candidate tuples across the entire corpus.
    Tuple structure:
      (question_instance_id, detector_id, damage_type, severity, resolution_status, evidence)
    """
    candidates = []
    for r in records:
        inst_id = r.get('question_instance_id')
        rtype = r.get('record_type')
        text = r.get('raw_text') or ""

        # 1. Non-question source fragments (non-answerable physical records)
        if rtype == 'non_question_source_fragment':
            f_type = r.get('fragment_type')
            if f_type == "marks_allocation_equation":
                det_id = "DET_FRAGMENT_MARKS"
                d_type = "marks_footer_contamination"
            elif f_type == "curriculum_outcome_footer":
                det_id = "DET_FRAGMENT_CO_FOOTER"
                d_type = "administrative_metadata_inside_question"
            else:
                det_id = "DET_FRAGMENT_SOLUTION"
                d_type = "solution_code_fragment"
            ev = f"Physical source fragment: '{text[:100]}'"
            candidates.append((inst_id, det_id, d_type, "MAJOR", "RESOLVED", ev))

        # 2. DOC-28 Page 2 column interleaving and visual layout defects
        if r.get('document_id') == 'DOC-28' and r.get('page_start') == 2 and str(r.get('official_question_number')) in ['7', '8', '9', '10', '11']:
            q_num = str(r.get('official_question_number'))
            if q_num == '7':
                ev = "Three horizontal text streams interleaved across multi-column layout on rendered page 2"
                candidates.append((inst_id, "DET_DOC28_LAYOUT_P02_Q07", "page_column_interleaving", "CRITICAL", "RESOLVED", ev))
            elif q_num == '8':
                ev = "C code function `void fun(struct node* start)` embedded in raster image xref 22 omitted from raw text stream"
                candidates.append((inst_id, "DET_DOC28_LAYOUT_P02_Q08", "missing_essential_code_block", "CRITICAL", "RESOLVED", ev))
            elif q_num == '9':
                ev = "Referenced 6-vertex BFS graph diagram with vertices {M, N, O, K, Q, P} located in visual container y=300-450"
                candidates.append((inst_id, "DET_DOC28_LAYOUT_P02_Q09", "missing_referenced_visual", "MAJOR", "RESOLVED", ev))
            elif q_num == '10':
                ev = "Referenced post-order binary tree diagram embedded in raster image xref 24"
                candidates.append((inst_id, "DET_DOC28_LAYOUT_P02_Q10", "missing_referenced_visual", "MAJOR", "RESOLVED", ev))
            elif q_num == '11':
                ev = "Contaminated with text stream fragment from Question 7 center stream ('ements is correct for a circular singly linked list w')"
                candidates.append((inst_id, "DET_DOC28_LAYOUT_P02_Q11", "cross_question_contamination", "CRITICAL", "RESOLVED", ev))

        # 3. Administrative metadata embedded inside questions (CO/Bloom markers)
        if rtype == 'question_occurrence':
            terms = ['[(CO', '(CO1)', '(CO2)', '(CO3)', '(CO4)', '(CO5)', '(CO6)', 'LOCQ', 'IOCQ', 'HOCQ', 'Cognition Level', 'Course Outcome (CO)']
            if any(term in text for term in terms):
                ev = f"Bloom's taxonomy / CO annotation present in text: '{text[:80]}...'"
                candidates.append((inst_id, "DET_QUESTION_ADMIN_METADATA", "administrative_metadata_inside_question", "WARNING", "UNRESOLVED", ev))

    return candidates


def validate_damage_audit(records, damaged, raise_on_error=False):
    """
    Rules 06, 20:
    - Real damage audit is populated with valid damage records.
    - Deterministic damage condition identity: (question_instance_id, detector_id, damage_type, severity, resolution_status, evidence).
    - Invariant: detected_deterministic_damage_set == audited_deterministic_damage_set.
    - Zero duplicates allowed in damage audit.
    - Detects missing entries, wrong damage_type, wrong detector, wrong severity, wrong resolution_status, fabricated entries.
    - No active question contains pure marks-only equation or cross-question contamination (Rule 20).
    """
    if not damaged:
        msg = "Damage audit is empty while deterministic damage candidates exist in corpus."
        if raise_on_error:
            raise AssertionError(msg)
        return False, msg

    valid_severities = {"WARNING", "MAJOR", "CRITICAL"}
    valid_statuses = {"RESOLVED", "UNRESOLVED", "NOT_APPLICABLE"}

    # 1. Check for duplicates in damage audit
    serialized = [json.dumps(d, sort_keys=True) for d in damaged]
    if len(serialized) != len(set(serialized)):
        msg = f"Damage audit contains duplicate entries: {len(damaged)} total vs {len(set(serialized))} unique"
        if raise_on_error:
            raise AssertionError(msg)
        return False, msg

    # 2. Validate individual entry formatting
    audited_tuples = []
    for d in damaged:
        inst_id = d.get('question_instance_id')
        det_id = d.get('detector_id')
        d_type = d.get('damage_type')
        sev = d.get('severity')
        res_st = d.get('resolution_status')
        ev = d.get('evidence')

        if not inst_id or not d_type:
            msg = f"Damage entry missing question_instance_id or damage_type: {d}"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        if not det_id:
            msg = f"Damage entry {inst_id} missing detector_id: {d}"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        if sev not in valid_severities:
            msg = f"Damage entry {inst_id} has invalid severity '{sev}'"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        if res_st not in valid_statuses:
            msg = f"Damage entry {inst_id} has invalid resolution_status '{res_st}'"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        audited_tuples.append((inst_id, det_id, d_type, sev, res_st, ev))

    # 3. Independent deterministic candidate detection
    detected_candidates = detect_damage_candidates(records)
    detected_set = set(detected_candidates)
    audited_set = set(audited_tuples)

    # Missing audit entries
    missing = detected_set - audited_set
    if missing:
        sample = next(iter(missing))
        msg = f"Deterministic damage candidate missing from damage audit: {sample}"
        if raise_on_error:
            raise AssertionError(msg)
        return False, msg

    # Fabricated audit entries
    extra = audited_set - detected_set
    if extra:
        sample = next(iter(extra))
        msg = f"Fabricated or altered damage entry found in damage audit: {sample}"
        if raise_on_error:
            raise AssertionError(msg)
        return False, msg

    # Exact equality check
    if detected_set != audited_set:
        msg = f"Exact deterministic damage equality failed: {len(detected_set)} detected != {len(audited_set)} audited"
        if raise_on_error:
            raise AssertionError(msg)
        return False, msg

    # Rule 20 check: no active question has pure marks equation or cross-question contamination
    for r in records:
        if r.get('record_type') == 'question_occurrence':
            text = r.get('raw_text') or ""
            if re.match(r'^\s*(\+[\s\d\+\-\*\(\)\=]+|\d+[\s\d\+\-\*\(\)]*\s*=\s*\d+)\s*$', text):
                msg = f"Question occurrence {r.get('question_instance_id')} contains pure marks equation"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg

    # Specific check for DOC-28 Q11 purity
    doc28_q11 = next((q for q in records if q.get('document_id') == 'DOC-28' and str(q.get('official_question_number')) == '11' and q.get('record_type') == 'question_occurrence'), None)
    if doc28_q11:
        text11 = doc28_q11.get('raw_text', '').lower()
        if 'singly linked list' in text11 or 'start pointer' in text11:
            msg = f"DOC-28 Q11 contains cross-question contamination from Q7: '{text11}'"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

    return True, f"Deterministic damage audit validated: {len(damaged)} audited conditions match {len(detected_candidates)} detected conditions exactly."


def validate_wording_states(records, raise_on_error=False):
    """
    Rules 07, 23:
    - Every question occurrence has a valid wording state (STATE A, STATE B, STATE C).
    - Containers and fragments strictly have null wording_state.
    - STATE C items have explicit incomplete evidence.
    """
    valid_wording_states = {"STATE A — EXACT", "STATE B — RECONSTRUCTED", "STATE C — SOURCE-INCOMPLETE"}

    for r in records:
        inst_id = r.get('question_instance_id')
        rtype = r.get('record_type')
        wstate = r.get('wording_state')

        if rtype == 'question_occurrence':
            if wstate not in valid_wording_states:
                msg = f"Question occurrence {inst_id} has invalid wording_state '{wstate}'"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg
            if wstate == "STATE C — SOURCE-INCOMPLETE":
                meta = r.get('reconstruction_metadata') or {}
                if not meta.get('incomplete_evidence'):
                    msg = f"STATE C item {inst_id} missing incomplete_evidence in reconstruction_metadata"
                    if raise_on_error:
                        raise AssertionError(msg)
                    return False, msg
        else:
            if wstate is not None:
                msg = f"Non-question record {inst_id} of type '{rtype}' has non-null wording_state '{wstate}'"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg

    return True, "Wording states verified across all records; null for containers/fragments."


def validate_governance_tiers(inventory, records, raise_on_error=False):
    """
    Rules 08, 16, 17, 22:
    - No solution or study material assigned to Tier < 4 (Rule 08).
    - Practice Assignment does not appear as exam_type (Rule 16).
    - Unverified Question Bank authority not promoted to Tier 2 (DOC-30, DOC-31) (Rule 17).
    - DOC-31 classification is consistent at Tier 3 Authority Unconfirmed across inventory and records (Rule 22).
    """
    # Rule 08
    for d in inventory:
        if d.get('document_classification') in ["Solution Document / Answer Key", "Notes / Study Material"]:
            if d.get('source_tier', 0) < 4:
                msg = f"Document {d.get('document_id')} is solution/notes but assigned to Tier {d.get('source_tier')}"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg

    for r in records:
        if r.get('source_type') in ["Solution Document / Answer Key", "Notes / Study Material"]:
            if r.get('source_tier', 0) < 4:
                msg = f"Record {r.get('question_instance_id')} is solution/notes but assigned to Tier {r.get('source_tier')}"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg

    # Rule 16
    doc28_meta = next((d for d in inventory if d['document_id'] == 'DOC-28'), None)
    if doc28_meta and doc28_meta.get('apparent_exam_type') is not None:
        msg = f"DOC-28 inventory has non-null apparent_exam_type '{doc28_meta.get('apparent_exam_type')}'"
        if raise_on_error:
            raise AssertionError(msg)
        return False, msg

    # Rule 17 & Rule 22 (DOC-30 and DOC-31)
    doc30_meta = next((d for d in inventory if d['document_id'] == 'DOC-30'), None)
    doc31_meta = next((d for d in inventory if d['document_id'] == 'DOC-31'), None)

    if doc30_meta:
        if doc30_meta.get('source_tier') != 3 or "Authority Unconfirmed" not in doc30_meta.get('document_classification', ''):
            msg = f"DOC-30 not classified as Tier 3 Authority Unconfirmed: {doc30_meta.get('source_tier')}, {doc30_meta.get('document_classification')}"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

    if doc31_meta:
        if doc31_meta.get('source_tier') != 3 or "Authority Unconfirmed" not in doc31_meta.get('document_classification', ''):
            msg = f"DOC-31 inventory not classified as Tier 3 Authority Unconfirmed: {doc31_meta.get('source_tier')}, {doc31_meta.get('document_classification')}"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

    # Ensure records of DOC-31 match Tier 3
    doc31_records = [r for r in records if r.get('document_id') == 'DOC-31']
    for r in doc31_records:
        if r.get('source_tier') != 3:
            msg = f"DOC-31 record {r.get('question_instance_id')} has source_tier {r.get('source_tier')} != 3"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

    return True, "Governance tiers and document classification verified (Tier 4 solutions, Tier 3 unconfirmed banks)."


def validate_answerability(records, raise_on_error=False):
    """
    Rules 11, 12:
    - Containers are not answerable (is_student_answerable == False).
    - Question occurrences are answerable (is_student_answerable == True).
    - Non-question source fragments are not answerable (is_student_answerable == False).
    """
    for r in records:
        inst_id = r.get('question_instance_id')
        rtype = r.get('record_type')
        ans = r.get('is_student_answerable')

        if rtype == 'paper_question_container' and ans is not False:
            msg = f"Container {inst_id} has is_student_answerable = {ans} (expected False)"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        if rtype == 'question_occurrence' and ans is not True:
            msg = f"Question occurrence {inst_id} has is_student_answerable = {ans} (expected True)"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        if rtype == 'non_question_source_fragment' and ans is not False:
            msg = f"Source fragment {inst_id} has is_student_answerable = {ans} (expected False)"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

    return True, "Answerability strictly verified: containers and fragments are False, occurrences are True."


def validate_state_b_semantics(records, raise_on_error=False):
    """
    Rules 13, 21, 29, 30, 31:
    - Rule 13: Every STATE B question has complete reconstruction metadata.
    - Rule 21: Every question requiring a visual has source_visual_page and source_visual_reason.
    - Rule 29: STATE B visual questions require semantic verification metadata.
    - Rule 30: STATE B visual semantics must be marked verified only if all required elements match.
    - Rule 31: True independent semantic verification without trusting match=true:
        * Q8: Structured C code lines independently compared against authoritative C function.
        * Q9: Structured graph vertices and normalized undirected edges independently compared against authoritative graph.
        * Q10: Structured binary tree root and parent-child relationships independently compared against authoritative tree.
    """
    for r in records:
        inst_id = r.get('question_instance_id')
        rtype = r.get('record_type')
        wstate = r.get('wording_state')

        # Rule 21: Source visual required metadata
        if r.get('source_visual_required'):
            if r.get('source_visual_page') is None or not r.get('source_visual_reason'):
                msg = f"Record {inst_id} requires visual but lacks source_visual_page or source_visual_reason"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg

        if rtype == 'question_occurrence' and wstate == "STATE B — RECONSTRUCTED":
            meta = r.get('reconstruction_metadata')
            if not meta:
                msg = f"STATE B question {inst_id} missing reconstruction_metadata"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg

            for field in ['reconstruction_method', 'visual_source_reference', 'reconstructed_text', 'reconstruction_confidence']:
                if not meta.get(field):
                    msg = f"STATE B question {inst_id} reconstruction_metadata missing '{field}'"
                    if raise_on_error:
                        raise AssertionError(msg)
                    return False, msg

            sem = meta.get('visual_semantic_verification')
            if not sem:
                msg = f"STATE B question {inst_id} missing visual_semantic_verification object"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg

            if not sem.get('status') or not sem.get('verification_basis') or sem.get('source_page') is None:
                msg = f"STATE B question {inst_id} visual_semantic_verification missing core fields"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg

            findings = sem.get('element_level_findings', [])
            if not findings:
                msg = f"STATE B question {inst_id} visual_semantic_verification has empty element_level_findings"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg

            if sem.get('status') == 'VERIFIED':
                for finding in findings:
                    if not finding.get('match'):
                        msg = f"STATE B question {inst_id} marked VERIFIED but element '{finding.get('element')}' match is False"
                        if raise_on_error:
                            raise AssertionError(msg)
                        return False, msg

            # Q8 INDEPENDENT C CODE SEMANTIC VERIFICATION
            if inst_id == "DOC-28-P02-MCQ-Q08":
                code_sem = sem.get('code_semantics')
                if not code_sem or not code_sem.get('lines'):
                    msg = "DOC-28 Q8 structured code_semantics is missing or contains no lines"
                    if raise_on_error:
                        raise AssertionError(msg)
                    return False, msg

                lines = code_sem.get('lines', [])
                if len(lines) != len(AUTHORITATIVE_Q8_LINES):
                    msg = f"DOC-28 Q8 code line count mismatch: {len(lines)} != {len(AUTHORITATIVE_Q8_LINES)}"
                    if raise_on_error:
                        raise AssertionError(msg)
                    return False, msg

                for idx, (actual_line, auth_line) in enumerate(zip(lines, AUTHORITATIVE_Q8_LINES)):
                    if actual_line.strip() != auth_line.strip():
                        msg = f"DOC-28 Q8 code semantic corruption at line {idx+1}: '{actual_line}' != '{auth_line}'"
                        if raise_on_error:
                            raise AssertionError(msg)
                        return False, msg

            # Q9 INDEPENDENT GRAPH SEMANTIC VERIFICATION
            if inst_id == "DOC-28-P02-MCQ-Q09":
                raw_text = r.get('raw_text', '')
                if "6 nodes {M, N, O, K, Q, P}" not in raw_text or "(M,K)" not in raw_text:
                    msg = "DOC-28 Q9 raw_text does not contain faithful vertex 'K' and edge '(M,K)'"
                    if raise_on_error:
                        raise AssertionError(msg)
                    return False, msg

                if "6 nodes {M, N, O, R, Q, P}" in raw_text or "(M,R)" in raw_text:
                    msg = "DOC-28 Q9 graph representation incorrectly contains erroneous vertex 'R'"
                    if raise_on_error:
                        raise AssertionError(msg)
                    return False, msg

                graph_sem = sem.get('graph_semantics')
                if not graph_sem:
                    msg = "DOC-28 Q9 structured graph_semantics is missing"
                    if raise_on_error:
                        raise AssertionError(msg)
                    return False, msg

                vertices = set(graph_sem.get('vertices', []))
                if vertices != AUTHORITATIVE_Q9_VERTICES or "R" in vertices:
                    msg = f"DOC-28 Q9 graph vertices mismatch: {vertices} != {AUTHORITATIVE_Q9_VERTICES}"
                    if raise_on_error:
                        raise AssertionError(msg)
                    return False, msg

                edges = graph_sem.get('edges', [])
                norm_edges = {tuple(sorted(e)) for e in edges if len(e) == 2}
                if norm_edges != AUTHORITATIVE_Q9_EDGES:
                    msg = f"DOC-28 Q9 graph normalized edges mismatch: {norm_edges} != {AUTHORITATIVE_Q9_EDGES}"
                    if raise_on_error:
                        raise AssertionError(msg)
                    return False, msg

            # Q10 INDEPENDENT TREE SEMANTIC VERIFICATION
            if inst_id == "DOC-28-P02-MCQ-Q10":
                tree_sem = sem.get('tree_semantics')
                if not tree_sem:
                    msg = "DOC-28 Q10 structured tree_semantics is missing"
                    if raise_on_error:
                        raise AssertionError(msg)
                    return False, msg

                if tree_sem.get('root') != AUTHORITATIVE_Q10_ROOT:
                    msg = f"DOC-28 Q10 tree root mismatch: '{tree_sem.get('root')}' != '{AUTHORITATIVE_Q10_ROOT}'"
                    if raise_on_error:
                        raise AssertionError(msg)
                    return False, msg

                rel_list = tree_sem.get('parent_child_relationships', [])
                norm_rels = {(rel.get('parent'), rel.get('child')) for rel in rel_list}
                if norm_rels != AUTHORITATIVE_Q10_RELATIONSHIPS:
                    msg = f"DOC-28 Q10 tree parent-child relationships mismatch: {norm_rels} != {AUTHORITATIVE_Q10_RELATIONSHIPS}"
                    if raise_on_error:
                        raise AssertionError(msg)
                    return False, msg

    return True, "STATE B reconstruction provenance and independent semantic representations validated."


def validate_visual_state_consistency(page_quality, visual_audit, raise_on_error=False):
    """
    Rules 14, 15, 25, 26, 27, 28 / Fix D: Complete Canonical <-> Legacy Visual State Consistency.
    - Canonical visual lifecycle states: detection_status, render_status, visual_review_status, verification_status.
    - Contradiction rejection against legacy fields (verified, visually_reviewed, render_artifact_reference).
    - RENDERED requires physical artifact on disk.
    - REVIEWED requires review record.
    - VERIFIED requires review record and verification basis.
    - DETECTED alone must never become VERIFIED without review evidence.
    """
    for p in page_quality:
        p_num = p.get('page_number')
        doc_id = p.get('document_id')
        det_st = p.get('detection_status')
        ren_st = p.get('render_status')
        ren_ref = p.get('render_artifact_reference')
        rev_st = p.get('visual_review_status')
        ver_st = p.get('verification_status')
        v_rev = p.get('visually_reviewed')
        ver = p.get('verified')
        rec = p.get('review_record')
        basis = p.get('verification_basis')

        # D1: Contradiction: verification_status vs verified
        if ver_st == "VERIFIED" and v_rev is not True:
            msg = f"Contradiction: Page {doc_id} P{p_num} verification_status is VERIFIED but visually_reviewed is not True"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        if ver_st == "VERIFIED" and ver is not True:
            msg = f"Contradiction: Page {doc_id} P{p_num} verification_status is VERIFIED but verified is False"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        if ver is True and ver_st != "VERIFIED":
            msg = f"Contradiction: Page {doc_id} P{p_num} verified is True but verification_status is '{ver_st}'"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        # D2: Contradiction: visual_review_status vs visually_reviewed
        if rev_st == "REVIEWED" and v_rev is not True:
            msg = f"Contradiction: Page {doc_id} P{p_num} visual_review_status is REVIEWED but visually_reviewed is False"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        if v_rev is True and rev_st != "REVIEWED":
            msg = f"Contradiction: Page {doc_id} P{p_num} visually_reviewed is True but visual_review_status is '{rev_st}'"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        # D3: Contradiction: visual_verification_status vs verification_status
        if p.get('visual_verification_status') == "VERIFIED" and ver_st != "VERIFIED":
            msg = f"Contradiction: Page {doc_id} P{p_num} visual_verification_status is VERIFIED but verification_status is '{ver_st}'"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        # D5: Contradiction: render_status vs render_artifact_reference
        if ren_st == "NOT_RENDERED" and ren_ref is not None:
            msg = f"Contradiction: Page {doc_id} P{p_num} render_status is NOT_RENDERED but render_artifact_reference is '{ren_ref}'"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        # D4: RENDERED + missing artifact
        if ren_st == "RENDERED":
            if not ren_ref:
                msg = f"Page {doc_id} P{p_num} render_status is RENDERED but render_artifact_reference is null"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg
            if not os.path.exists(ren_ref):
                msg = f"Page {doc_id} P{p_num} render artifact '{ren_ref}' does not exist on disk"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg

        # D6: Contradiction: VERIFIED without REVIEWED
        if ver_st == "VERIFIED" and rev_st != "REVIEWED":
            msg = f"Contradiction: Page {doc_id} P{p_num} verification_status is VERIFIED but visual_review_status is '{rev_st}' (expected 'REVIEWED')"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        # D7: Contradiction: REVIEWED without render evidence
        if rev_st == "REVIEWED" and (ren_st != "RENDERED" or not ren_ref or not os.path.exists(ren_ref)):
            msg = f"Contradiction: Page {doc_id} P{p_num} visual_review_status is REVIEWED but render evidence is missing (render_status='{ren_st}', ref='{ren_ref}')"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        # VISUALLY_REVIEWED requires review record
        if rev_st == "REVIEWED":
            if not rec:
                msg = f"Page {doc_id} P{p_num} is marked visually reviewed but review_record is null"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg

        # VERIFIED requires review record and verification basis
        if ver_st == "VERIFIED":
            if not (rec and basis):
                msg = f"Page {doc_id} P{p_num} is marked VERIFIED without full review record and verification basis"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg

        # DETECTED must not automatically become VERIFIED
        if p.get('visual_verification_status') == "DETECTED" or (det_st == "DETECTED" and ver_st != "VERIFIED"):
            if ver is True or v_rev is True or ver_st == "VERIFIED":
                msg = f"Page {doc_id} P{p_num} is DETECTED but inappropriately claimed as VERIFIED/REVIEWED"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg

    # Repeat for visual_audit records
    for v in visual_audit:
        p_num = v.get('page_number')
        doc_id = v.get('document_id')
        ver_st = v.get('verification_status')
        rev_st = v.get('visual_review_status')
        ren_st = v.get('render_status')
        ren_ref = v.get('render_artifact_reference')
        v_rev = v.get('visually_reviewed')
        ver = v.get('verified')

        # D1
        if ver_st == "VERIFIED" and ver is not True:
            msg = f"Contradiction: Visual audit {doc_id} P{p_num} verification_status is VERIFIED but verified is False"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        # D2
        if rev_st == "REVIEWED" and v_rev is not True:
            msg = f"Contradiction: Visual audit {doc_id} P{p_num} visual_review_status is REVIEWED but visually_reviewed is False"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        # D3
        if v.get('visual_verification_status') == "VERIFIED" and ver_st != "VERIFIED":
            msg = f"Contradiction: Visual audit {doc_id} P{p_num} visual_verification_status is VERIFIED but verification_status is '{ver_st}'"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        # D5
        if ren_st == "NOT_RENDERED" and ren_ref is not None:
            msg = f"Contradiction: Visual audit {doc_id} P{p_num} render_status is NOT_RENDERED but render_artifact_reference is not null"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        # D4
        if ren_st == "RENDERED":
            if not ren_ref or not os.path.exists(ren_ref):
                msg = f"Visual audit {doc_id} P{p_num} render_status is RENDERED but artifact is missing: '{ren_ref}'"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg

        # D6
        if ver_st == "VERIFIED" and rev_st != "REVIEWED":
            msg = f"Contradiction: Visual audit {doc_id} P{p_num} verification_status is VERIFIED but visual_review_status is '{rev_st}'"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        # D7
        if rev_st == "REVIEWED" and (ren_st != "RENDERED" or not ren_ref or not os.path.exists(ren_ref)):
            msg = f"Contradiction: Visual audit {doc_id} P{p_num} visual_review_status is REVIEWED but render evidence is missing"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        if v.get('visual_verification_status') == "VERIFIED" or ver_st == "VERIFIED":
            if not (v_rev is True and ver is True and v.get('review_record') and v.get('verification_basis')):
                msg = f"Visual audit {doc_id} P{p_num} is marked VERIFIED without complete review evidence"
                if raise_on_error:
                    raise AssertionError(msg)
                return False, msg

    return True, "Visual page extraction quality and verification audit validated across all dimensions."
validate_visual_pages = validate_visual_state_consistency


def derive_document_rendering_lifecycle(page_quality):
    """
    Fix B: Document Rendering Lifecycle Derivation.
    Derives document-level rendering lifecycle strictly from page_quality page-level evidence.
    Returns: dict mapping doc_id -> {
        'total_pages': int,
        'rendered_pages': int,
        'reviewed_pages': int,
        'verified_pages': int,
        'document_rendering_status': 'NOT_RENDERED' | 'PARTIALLY_RENDERED' | 'FULLY_RENDERED',
        'rendering_complete': bool
    }
    """
    doc_groups = defaultdict(list)
    for p in page_quality:
        doc_groups[p.get('document_id')].append(p)

    lifecycle_map = {}
    for doc_id, pages in doc_groups.items():
        total_pages = len(pages)
        rendered_pages = sum(1 for p in pages if p.get('render_status') == "RENDERED")
        reviewed_pages = sum(1 for p in pages if p.get('visual_review_status') == "REVIEWED" or p.get('visually_reviewed') is True)
        verified_pages = sum(1 for p in pages if p.get('verification_status') == "VERIFIED" or p.get('verified') is True)

        if rendered_pages == 0:
            lifecycle = "NOT_RENDERED"
        elif rendered_pages == total_pages and total_pages > 0:
            lifecycle = "FULLY_RENDERED"
        else:
            lifecycle = "PARTIALLY_RENDERED"

        rendering_complete = (rendered_pages == total_pages and total_pages > 0)
        lifecycle_map[doc_id] = {
            'total_pages': total_pages,
            'rendered_pages': rendered_pages,
            'reviewed_pages': reviewed_pages,
            'verified_pages': verified_pages,
            'document_rendering_status': lifecycle,
            'rendering_complete': rendering_complete
        }
    return lifecycle_map


def derive_document_rendering_status(doc_id, page_quality):
    """
    Helper function to dynamically derive document rendering lifecycle for a single document.
    """
    lmap = derive_document_rendering_lifecycle(page_quality)
    return lmap.get(doc_id, {
        'total_pages': 0,
        'rendered_pages': 0,
        'reviewed_pages': 0,
        'verified_pages': 0,
        'document_rendering_status': "NOT_RENDERED",
        'rendering_complete': False
    })


def validate_document_lifecycle(inventory, page_quality, raise_on_error=False):
    """
    Rule 32 / Fix B: Document-Level Rendering Lifecycle Derivation.
    - Derives total_pages, rendered_pages, reviewed_pages, verified_pages from page_quality.
    - Derives NOT_RENDERED, PARTIALLY_RENDERED, FULLY_RENDERED dynamically.
    - Invariant: inventory.document_rendering_status == derived_status
    - Invariant: inventory.rendering_complete == (rendered_pages == total_pages)
    - Zero hardcoding of any document ID.
    """
    valid_lifecycle_statuses = {"NOT_RENDERED", "PARTIALLY_RENDERED", "FULLY_RENDERED"}
    lifecycle_map = derive_document_rendering_lifecycle(page_quality)

    for d in inventory:
        doc_id = d.get('document_id')
        derived = lifecycle_map.get(doc_id)
        if not derived:
            msg = f"Document {doc_id} in inventory has no corresponding pages in PAGE_EXTRACTION_QUALITY"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        doc_ren_st = d.get('document_rendering_status')
        ren_comp = d.get('rendering_complete')

        if doc_ren_st not in valid_lifecycle_statuses:
            msg = f"Document {doc_id} has invalid document_rendering_status '{doc_ren_st}'"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        if doc_ren_st != derived['document_rendering_status']:
            msg = f"Document {doc_id} document_rendering_status '{doc_ren_st}' does not match derived status '{derived['document_rendering_status']}' from page quality (rendered {derived['rendered_pages']}/{derived['total_pages']} pages)"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

        if ren_comp != derived['rendering_complete']:
            msg = f"Document {doc_id} rendering_complete is {ren_comp} but derived completion is {derived['rendering_complete']} (rendered {derived['rendered_pages']}/{derived['total_pages']} pages)"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

    return True, "Document rendering lifecycle dynamically derived from page quality dataset and verified across all inventory documents."


def validate_page_audit_bijection(page_quality, visual_audit, raise_on_error=False):
    """
    Rule 34 / Fix A: Page Dataset <-> Visual Audit Bijection.
    Canonical page identity: (document_id, page_number)
    Invariants:
    1. Every PAGE_EXTRACTION_QUALITY detected page key exists exactly once in VISUAL_VERIFICATION_AUDIT.
    2. Every VISUAL_VERIFICATION_AUDIT page key exists exactly once in PAGE_EXTRACTION_QUALITY (and has detection_status == 'DETECTED').
    3. No duplicate canonical page keys exist in either dataset.
    4. For every matching page key, all fields that are intended to represent the same lifecycle state must agree.
    5. At minimum reconcile:
       - detection_status
       - render_status
       - render_artifact_reference
       - visual_review_status
       - verification_status
       - visually_reviewed
       - verified
       - review_record
       - verification_basis
       - legacy visual_verification_status, where present
    6. Do not compare irrelevant descriptive metadata merely because it exists.
    7. The validator must derive the comparison from actual records, not hard-coded page counts.
    """
    # 1. Check duplicate keys in page_quality
    pq_keys = [(p.get('document_id'), p.get('page_number')) for p in page_quality]
    if len(pq_keys) != len(set(pq_keys)):
        seen = set()
        dups = set()
        for k in pq_keys:
            if k in seen:
                dups.add(k)
            seen.add(k)
        msg = f"Duplicate canonical page keys found in PAGE_EXTRACTION_QUALITY: {dups}"
        if raise_on_error:
            raise AssertionError(msg)
        return False, msg

    # 2. Check duplicate keys in visual_audit
    va_keys = [(v.get('document_id'), v.get('page_number')) for v in visual_audit]
    if len(va_keys) != len(set(va_keys)):
        seen = set()
        dups = set()
        for k in va_keys:
            if k in seen:
                dups.add(k)
            seen.add(k)
        msg = f"Duplicate canonical page keys found in VISUAL_VERIFICATION_AUDIT: {dups}"
        if raise_on_error:
            raise AssertionError(msg)
        return False, msg

    # 3. Exact bijection between detected visual pages
    pq_vis = { (p['document_id'], p['page_number']): p for p in page_quality if p.get('detection_status') == 'DETECTED' }
    va_map = { (v['document_id'], v['page_number']): v for v in visual_audit }

    pq_keys_set = set(pq_vis.keys())
    va_keys_set = set(va_map.keys())

    if pq_keys_set != va_keys_set:
        missing_in_va = pq_keys_set - va_keys_set
        extra_in_va = va_keys_set - pq_keys_set
        msg = f"Visual page key mismatch between page quality and visual audit: missing in audit: {missing_in_va}, extra in audit: {extra_in_va}"
        if raise_on_error:
            raise AssertionError(msg)
        return False, msg

    fields_to_compare = [
        'detection_status',
        'render_status',
        'render_artifact_reference',
        'visual_review_status',
        'verification_status',
        'visually_reviewed',
        'verified',
        'review_record',
        'verification_basis',
        'visual_verification_status'
    ]

    for k in sorted(pq_keys_set):
        p_rec = pq_vis[k]
        v_rec = va_map[k]
        for f in fields_to_compare:
            if f in p_rec or f in v_rec:
                p_val = p_rec.get(f)
                v_val = v_rec.get(f)
                if p_val != v_val:
                    msg = f"Cross-artifact visual inconsistency for page {k[0]} P{k[1]} on field '{f}': page_quality has '{p_val}', visual_audit has '{v_val}'"
                    if raise_on_error:
                        raise AssertionError(msg)
                    return False, msg

    return True, f"Page audit bijection validated: all {len(pq_keys_set)} visual pages agree exactly across all canonical fields."

validate_page_quality_and_visual_audit_consistency = validate_page_audit_bijection


def validate_formal_schemas(inventory, records, page_quality, visual_audit, damaged, schema_path='PHASE1_SCHEMA.json', raise_on_error=False):
    """
    Rule 33:
    - Formally validates all production records against authoritative PHASE1_SCHEMA.json.
    - Covers SOURCE_CORPUS_INVENTORY, RAW_EXTRACTED_QUESTIONS, PAGE_EXTRACTION_QUALITY,
      VISUAL_VERIFICATION_AUDIT, and DAMAGED_AND_INCOMPLETE_QUESTIONS_AUDIT.
    """
    if not os.path.exists(schema_path):
        msg = f"Schema file not found at '{schema_path}'"
        if raise_on_error:
            raise AssertionError(msg)
        return False, msg

    with open(schema_path, 'r', encoding='utf-8') as f:
        schema = json.load(f)

    resolver = jsonschema.RefResolver.from_schema(schema)

    # 1. Validate Documents
    doc_schema = schema['definitions']['Document']
    for idx, d in enumerate(inventory):
        try:
            jsonschema.validate(instance=d, schema=doc_schema, resolver=resolver)
        except Exception as e:
            msg = f"Schema validation error in inventory [{idx}] ({d.get('document_id')}): {e.message}"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

    # 2. Validate Records
    rec_schema = schema['definitions']['Record']
    for idx, r in enumerate(records):
        try:
            jsonschema.validate(instance=r, schema=rec_schema, resolver=resolver)
        except Exception as e:
            msg = f"Schema validation error in record [{idx}] ({r.get('question_instance_id')}): {e.message}"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

    # 3. Validate Page Audits
    page_schema = schema['definitions']['PageAudit']
    for idx, p in enumerate(page_quality):
        try:
            jsonschema.validate(instance=p, schema=page_schema, resolver=resolver)
        except Exception as e:
            msg = f"Schema validation error in page quality [{idx}] ({p.get('document_id')} P{p.get('page_number')}): {e.message}"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

    # 4. Validate Visual Verification Records
    vva_schema = schema['definitions']['VisualVerificationRecord']
    for idx, v in enumerate(visual_audit):
        try:
            jsonschema.validate(instance=v, schema=vva_schema, resolver=resolver)
        except Exception as e:
            msg = f"Schema validation error in visual verification [{idx}] ({v.get('document_id')} P{v.get('page_number')}): {e.message}"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

    # 5. Validate Damage Audits
    dmg_schema = schema['definitions']['DamageAudit']
    for idx, d in enumerate(damaged):
        try:
            jsonschema.validate(instance=d, schema=dmg_schema, resolver=resolver)
        except Exception as e:
            msg = f"Schema validation error in damage audit [{idx}] ({d.get('question_instance_id')}): {e.message}"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

    return True, f"Formal schema validation passed for all 5 production datasets against {schema_path}."


def validate_reconciliation_and_counts(records, metrics, raise_on_error=False):
    """
    Rules 19, 24:
    - Containers + question occurrences + fragments == total physical records.
    - Subquestions + standalone == question occurrences.
    - Machine-readable summary metrics match physical records and visual metrics.
    """
    total_cnt = len(records)
    containers = [r for r in records if r.get('record_type') == 'paper_question_container']
    questions = [r for r in records if r.get('record_type') == 'question_occurrence']
    fragments = [r for r in records if r.get('record_type') == 'non_question_source_fragment']
    atomic_sub = [q for q in questions if q.get('occurrence_type') == 'sub_question']
    standalone = [q for q in questions if q.get('occurrence_type') == 'standalone']

    cont_cnt = len(containers)
    true_cnt = len(questions)
    frag_cnt = len(fragments)
    sub_cnt = len(atomic_sub)
    stand_cnt = len(standalone)

    if cont_cnt + true_cnt + frag_cnt != total_cnt:
        msg = f"Record count math failed: {cont_cnt} containers + {true_cnt} questions + {frag_cnt} fragments != {total_cnt} total"
        if raise_on_error:
            raise AssertionError(msg)
        return False, msg

    if sub_cnt + stand_cnt != true_cnt:
        msg = f"Question breakdown math failed: {sub_cnt} sub + {stand_cnt} standalone != {true_cnt} questions"
        if raise_on_error:
            raise AssertionError(msg)
        return False, msg

    if metrics:
        if metrics.get('physical_records') != total_cnt:
            msg = f"Metrics physical_records {metrics.get('physical_records')} != {total_cnt}"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg
        if metrics.get('paper_question_containers') != cont_cnt:
            msg = f"Metrics containers {metrics.get('paper_question_containers')} != {cont_cnt}"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg
        if metrics.get('question_occurrences') != true_cnt:
            msg = f"Metrics question_occurrences {metrics.get('question_occurrences')} != {true_cnt}"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

    return True, f"Reconciliation validated: {total_cnt} physical records = {cont_cnt} containers + {true_cnt} occurrences ({sub_cnt} sub + {stand_cnt} standalone) + {frag_cnt} fragments."


def recompute_summary_metrics(inventory, records, page_quality, visual_audit, damage_audit, suspicious_audit=None):
    """
    Fix C: Summary Metrics Independent Recomputation.
    Independently derive all summary metrics from raw production datasets.
    """
    containers = [r for r in records if r.get('record_type') == 'paper_question_container']
    true_questions = [r for r in records if r.get('record_type') == 'question_occurrence']
    fragments = [r for r in records if r.get('record_type') == 'non_question_source_fragment']

    atomic_sub = [q for q in true_questions if q.get('occurrence_type') == 'sub_question']
    standalone = [q for q in true_questions if q.get('occurrence_type') == 'standalone']

    state_a = sum(1 for q in true_questions if q.get('wording_state') == "STATE A — EXACT")
    state_b = sum(1 for q in true_questions if q.get('wording_state') == "STATE B — RECONSTRUCTED")
    state_c = sum(1 for q in true_questions if q.get('wording_state') == "STATE C — SOURCE-INCOMPLETE")

    complete_cnt = sum(1 for q in true_questions if q.get('completeness_status') == "COMPLETE")
    incomplete_cnt = sum(1 for q in true_questions if q.get('completeness_status') == "INCOMPLETE")
    flagged_ext = sum(1 for q in true_questions if q.get('extraction_confidence') == "FLAGGED")

    v_detected = sum(1 for p in page_quality if p.get('detection_status') == "DETECTED")
    v_rendered = sum(1 for p in page_quality if p.get('render_status') == "RENDERED")
    v_reviewed = sum(1 for p in page_quality if p.get('visual_review_status') == "REVIEWED" or p.get('visually_reviewed') is True)
    v_verified = sum(1 for p in page_quality if p.get('verification_status') == "VERIFIED" or p.get('verified') is True)
    v_flagged = sum(1 for p in page_quality if p.get('verification_status') == "FLAGGED")

    unresolved_dmg = sum(1 for d in damage_audit if d.get('resolution_status') == 'UNRESOLVED')

    return {
        "documents": len(inventory),
        "pages": len(page_quality),
        "physical_records": len(records),
        "paper_question_containers": len(containers),
        "question_occurrences": len(true_questions),
        "atomic_sub_questions": len(atomic_sub),
        "standalone_questions": len(standalone),
        "non_question_source_fragments": len(fragments),
        "state_a": state_a,
        "state_b": state_b,
        "state_c": state_c,
        "complete_questions": complete_cnt,
        "incomplete_questions": incomplete_cnt,
        "flagged_questions": flagged_ext,
        "complete": complete_cnt,
        "incomplete": incomplete_cnt,
        "flagged_extraction": flagged_ext,
        "visual_detected_pages": v_detected,
        "visual_rendered_pages": v_rendered,
        "visual_reviewed_pages": v_reviewed,
        "visual_verified_pages": v_verified,
        "visual_flagged_pages": v_flagged,
        "visual_detected": v_detected,
        "visual_rendered": v_rendered,
        "visual_reviewed": v_reviewed,
        "visual_verified": v_verified,
        "visual_flagged": v_flagged,
        "damage_records": len(damage_audit),
        "damage_audit_entries": len(damage_audit),
        "deterministic_damage_conditions": len(damage_audit),
        "unresolved_damage_records": unresolved_dmg
    }

derive_summary_metrics = recompute_summary_metrics


def validate_summary_metrics(metrics, inventory, records, page_quality, visual_audit, damaged, raise_on_error=False):
    """
    Rule 24 / Fix C: Summary Metrics Independence & Full Derivation.
    - CORPUS_SUMMARY_METRICS.json treated as output, not evidence.
    - Recomputes and compares every reported metric against independently derived values.
    """
    recomputed = recompute_summary_metrics(inventory, records, page_quality, visual_audit, damaged)

    for k, expected_val in recomputed.items():
        stored_val = metrics.get(k)
        if stored_val != expected_val:
            msg = f"Summary metric mismatch for key '{k}': stored {stored_val} != independently derived {expected_val}"
            if raise_on_error:
                raise AssertionError(msg)
            return False, msg

    return True, f"All {len(recomputed)} summary metrics verified equal to independently derived values."


# ==============================================================================
# MAIN EXECUTION (34 INTEGRITY RULES)
# ==============================================================================

def run_all_validation_rules(inventory, records, page_quality, damaged, visual_audit, suspicious, metrics):
    passed_checks = 0
    failed_checks = 0
    results = []

    def check(rule_num, description, condition, details=""):
        nonlocal passed_checks, failed_checks
        status = "PASS" if condition else "FAIL"
        if condition:
            passed_checks += 1
        else:
            failed_checks += 1
        results.append({
            'rule': rule_num,
            'description': description,
            'status': status,
            'details': details
        })
        print(f"Rule {rule_num:02d}: [{status}] {description}")
        if not condition and details:
            print(f"   -> Failure details: {details}")

    # Rule 01: Actual SHA-256 Byte Recomputation across all 33 PDFs
    p1, msg1 = validate_crypto_hashes(inventory)
    check(1, "Actual SHA-256 byte recomputation across all 33 PDFs", p1, msg1)

    # Rule 02: Every source record maps to an existing source document ID
    valid_doc_ids = set(d['document_id'] for d in inventory)
    r2_pass = all(r.get('document_id') in valid_doc_ids for r in records)
    check(2, "Every source record maps to an existing source document ID", r2_pass, f"All {len(records)} records map to registered documents.")

    # Rule 03: Every record has physical page and source file provenance
    r3_pass = all(r.get('page_start') is not None and r.get('source_file') for r in records)
    check(3, "Every record has physical page and source file provenance", r3_pass, f"Page and file provenance verified for {len(records)} records.")

    # Rule 04: Marks integrity (Rule A & Rule C)
    p4, msg4 = validate_marks_integrity(records)
    check(4, "No record has fabricated marks; every physically established mark has source evidence (Rule A & C)", p4, msg4)

    # Rule 05: No unknown provenance replaced with placeholder guesses
    p5, msg5 = validate_placeholders_and_bounds(records)
    check(5, "No unknown provenance is replaced with placeholder guesses", p5, msg5)

    # Rule 06: Real damage audit populated with exact deterministic condition equality
    p6, msg6 = validate_damage_audit(records, damaged)
    check(6, "Exact deterministic damage audit equality: detected == audited conditions with zero duplicates (Rule H)", p6, msg6)

    # Rule 07: Every question occurrence has a valid wording state
    p7, msg7 = validate_wording_states(records)
    check(7, "Every question occurrence has a valid wording state (null for containers and fragments)", p7, msg7)

    # Rule 08: No solution/reference material accidentally assigned to Tier 1
    p8, msg8 = validate_governance_tiers(inventory, records)
    check(8, "No solution/reference material accidentally assigned to Tier 1", p8, msg8)

    # Rule 09: No active/in-scope/syllabus fields introduced in Phase 1
    forbidden_fields = ["is_active", "in_syllabus", "canonical_id", "module_number", "topic_id", "difficulty_score"]
    r9_pass = not any(f in r for r in records for f in forbidden_fields)
    check(9, "No active/in-scope/syllabus fields introduced in Phase 1", r9_pass, f"Forbidden fields absent: {forbidden_fields}.")

    # Rule 10: No canonical question relationships or deduplication created
    r10_pass = not any("canonical" in k.lower() for r in records for k in r.keys())
    check(10, "No canonical question relationships or deduplication created", r10_pass, "All physical source occurrences remain fully independent.")

    # Rule 11: No structural parent container is counted as an answerable question (Rule D)
    containers = [r for r in records if r.get('record_type') == 'paper_question_container']
    true_questions = [r for r in records if r.get('record_type') == 'question_occurrence']
    fragments = [r for r in records if r.get('record_type') == 'non_question_source_fragment']
    r11_pass = all(c.get('is_student_answerable') is False for c in containers) and all(q.get('is_student_answerable') is True for q in true_questions)
    check(11, "No structural parent container is counted as an answerable question (Rule D)", r11_pass, f"{len(containers)} containers marked non-answerable; {len(true_questions)} question occurrences are answerable.")

    # Rule 12: No non-question source fragment is counted as an answerable question (Rule B & Rule E)
    r12_pass = all(f.get('is_student_answerable') is False for f in fragments)
    check(12, "No non-question source fragment is answerable (Rule B & Rule E)", r12_pass, f"All {len(fragments)} fragments strictly marked non-answerable.")

    # Rule 13: Every reconstructed question (STATE B) has verified reconstruction metadata
    state_b_qs = [q for q in true_questions if q.get('wording_state') == "STATE B — RECONSTRUCTED"]
    r13_pass = all(
        q.get('reconstruction_metadata') and
        q['reconstruction_metadata'].get('reconstruction_method') and
        q['reconstruction_metadata'].get('visual_source_reference') and
        q['reconstruction_metadata'].get('reconstructed_text') and
        q['reconstruction_metadata'].get('reconstruction_confidence')
        for q in state_b_qs
    )
    check(13, "Every STATE B question has complete verified reconstruction metadata", r13_pass, f"Reconstruction metadata verified for {len(state_b_qs)} items.")

    # Rule 14: Evidence-based visual verification (Rule F)
    p14, msg14 = validate_visual_pages(page_quality, visual_audit)
    check(14, "No VERIFIED visual item exists without explicit inspection evidence (Rule F)", p14, msg14)

    # Rule 15: Visual presence detection separation (Detected != Verified) (Rule G)
    detected_pages = [p for p in page_quality if p.get('visual_verification_status') == "DETECTED"]
    r15_pass = len(detected_pages) > 0 and all(p.get('verified') is False and p.get('visually_reviewed') is False for p in detected_pages)
    check(15, "Automated visual presence detection is distinct from verification (Rule G)", r15_pass, f"{len(detected_pages)} pages correctly classified as DETECTED without claiming verification.")

    # Rule 16: Practice Assignment does not appear as exam_type
    doc28_meta = next(d for d in inventory if d['document_id'] == 'DOC-28')
    doc28_qs = [q for q in records if q['document_id'] == 'DOC-28']
    r16_pass = doc28_meta.get('apparent_exam_type') is None and all(q.get('source_established_metadata', {}).get('exam_type') is None for q in doc28_qs)
    check(16, "Practice Assignment does not appear as exam_type", r16_pass, "exam_type is strictly null for Practice Assignment.")

    # Rule 17: Unverified Question Bank authority is not promoted to Tier 2
    doc30_meta = next(d for d in inventory if d['document_id'] == 'DOC-30')
    doc31_meta = next(d for d in inventory if d['document_id'] == 'DOC-31')
    r17_pass = doc30_meta['source_tier'] == 3 and doc31_meta['source_tier'] == 3 and "Authority Unconfirmed" in doc30_meta['document_classification'] and "Authority Unconfirmed" in doc31_meta['document_classification']
    check(17, "Unverified Question Bank authority is not promoted to Tier 2", r17_pass, "DOC-30 and DOC-31 classified as Authority Unconfirmed at Tier 3.")

    # Rule 18: All question records have valid record_type
    valid_record_types = {"paper_question_container", "question_occurrence", "non_question_source_fragment"}
    r18_pass = all(r.get('record_type') in valid_record_types for r in records)
    check(18, "All question records have valid record_type", r18_pass, f"All {len(records)} records have record_type in {valid_record_types}.")

    # Rule 19: Question counts dynamically reconcile from raw JSON dataset (Rule J)
    p19, msg19 = validate_reconciliation_and_counts(records, metrics)
    check(19, "Question counts reconcile dynamically from JSON dataset (Rule J)", p19, msg19)

    # Rule 20: No question contains unflagged marks footer contamination (Rule K)
    r20_no_pure_marks_qs = not any(
        re.match(r'^\s*(\+[\s\d\+\-\*\(\)\=]+|\d+[\s\d\+\-\*\(\)]*\s*=\s*\d+)\s*$', q.get('raw_text', ''))
        for q in true_questions
    )
    doc28_q11 = next((q for q in true_questions if q['document_id'] == 'DOC-28' and str(q['official_question_number']) == '11'), None)
    r20_doc28_clean = doc28_q11 and 'singly linked list' not in doc28_q11['raw_text'].lower() and 'start pointer' not in doc28_q11['raw_text'].lower()
    check(20, "No active question contains marks-only equation or cross-question contamination (Rule K)", r20_no_pure_marks_qs and r20_doc28_clean, "Marks-only equations reclassified as source fragments; DOC-28 Q11 purged.")

    # Rule 21: Every question referencing an essential visual has source-visual metadata
    v_req_qs = [q for q in true_questions if q.get('source_visual_required')]
    r21_pass = all(q.get('source_visual_page') is not None and q.get('source_visual_reason') for q in v_req_qs)
    check(21, "Every question referencing an essential visual has source-visual metadata", r21_pass, f"{len(v_req_qs)} visual questions have explicit source page and reason metadata.")

    # Rule 22: Document classification consistency across artifacts (DOC-31)
    r22_inv_class = doc31_meta.get('document_classification')
    r22_inv_tier = doc31_meta.get('source_tier')
    r22_consistent = (r22_inv_class == "Objective Question Bank — Authority Unconfirmed" and r22_inv_tier == 3)
    check(22, "DOC-31 classification is consistent at Tier 3 Authority Unconfirmed across inventory and records", r22_consistent, f"DOC-31 classification: '{r22_inv_class}', Tier: {r22_inv_tier}.")

    # Rule 23: STATE C items must have explicit incomplete evidence (Rule I)
    state_c_qs = [q for q in true_questions if q.get('wording_state') == "STATE C — SOURCE-INCOMPLETE"]
    r23_pass = all(q.get('reconstruction_metadata', {}).get('incomplete_evidence') for q in state_c_qs)
    check(23, "STATE C items have explicit incomplete evidence (Rule I)", r23_pass, f"{len(state_c_qs)} STATE C items in corpus; all have explicit source-incomplete evidence.")

    # Rule 24: Summary metrics synchronization (Prompt Master Part A3)
    p24, msg24 = validate_summary_metrics(metrics, inventory, records, page_quality, visual_audit, damaged)
    check(24, "Machine-readable summary metrics independently derived and verified across all metrics", p24, msg24)

    # Rule 25: RENDERED cannot be true without render evidence (Section 12)
    rendered_pages = [p for p in page_quality if p.get('render_status') == "RENDERED"]
    r25_pass = len(rendered_pages) > 0 and all(
        p.get('render_artifact_reference') and os.path.exists(p.get('render_artifact_reference'))
        for p in rendered_pages
    )
    check(25, "RENDERED cannot be true without render evidence existing on disk", r25_pass, f"{len(rendered_pages)} rendered pages backed by physical artifacts on disk.")

    # Rule 26: VISUALLY_REVIEWED cannot be true without a review record (Section 12)
    reviewed_pages = [p for p in page_quality if p.get('visual_review_status') == "REVIEWED" or p.get('visually_reviewed') is True]
    r26_pass = len(reviewed_pages) > 0 and all(p.get('review_record') for p in reviewed_pages)
    check(26, "VISUALLY_REVIEWED cannot be true without a review record", r26_pass, f"{len(reviewed_pages)} reviewed pages have review_record references.")

    # Rule 27: VERIFIED cannot be true without review record + verification basis (Section 12)
    verified_pages = [p for p in page_quality if p.get('verification_status') == "VERIFIED" or p.get('verified') is True]
    r27_pass = len(verified_pages) > 0 and all(
        p.get('review_record') and p.get('verification_basis') and p.get('visually_reviewed') is True
        for p in verified_pages
    )
    check(27, "VERIFIED cannot be true without review record + verification basis", r27_pass, f"{len(verified_pages)} verified pages backed by review records and basis.")

    # Rule 28: A detected visual page must not automatically become VERIFIED (Section 12)
    unverified_detected = [p for p in page_quality if p.get('detection_status') == "DETECTED" and p.get('verification_status') != "VERIFIED"]
    r28_pass = len(unverified_detected) > 0 and all(p.get('verified') is False and p.get('visually_reviewed') is False for p in unverified_detected)
    check(28, "Detected visual pages do not automatically become VERIFIED without review", r28_pass, f"{len(unverified_detected)} detected pages remain unverified pending physical review.")

    # Rule 29: STATE B visual questions require semantic verification metadata (Section 12)
    state_b_visual = [q for q in state_b_qs if q.get('source_visual_required')]
    r29_pass = len(state_b_visual) > 0 and all(
        q.get('reconstruction_metadata', {}).get('visual_semantic_verification') is not None
        for q in state_b_visual
    )
    check(29, "STATE B visual questions require semantic verification metadata", r29_pass, f"{len(state_b_visual)} visual STATE B questions contain structured semantic verification metadata.")

    # Rule 30: STATE B visual semantics must be marked verified only if all required elements match (Section 12)
    r30_pass = True
    for q in state_b_visual:
        sem = q.get('reconstruction_metadata', {}).get('visual_semantic_verification', {})
        if sem.get('status') == 'VERIFIED':
            findings = sem.get('element_level_findings', [])
            if not findings or any(not f.get('match') for f in findings):
                r30_pass = False
                break
    check(30, "STATE B visual semantics marked verified only when all elements match source", r30_pass, "All verified STATE B visual items have 100% matching element-level findings.")

    # Rule 31: DOC-28 Q9 graph semantic integrity (Section 12 & 15)
    p31, msg31 = validate_state_b_semantics(records)
    check(31, "DOC-28 Q9 graph representation is source-faithful (Vertex K, 7 edges, R eliminated)", p31, msg31)

    # Rule 32: Document-Level Rendering Lifecycle Semantics (Prompt Master Part A1)
    p32, msg32 = validate_document_lifecycle(inventory, page_quality)
    check(32, "Document-level rendering lifecycle dynamically derived from page quality dataset", p32, msg32)

    # Rule 33: Formal JSON Schema Release Gate (Prompt Master Part A8)
    p33, msg33 = validate_formal_schemas(inventory, records, page_quality, visual_audit, damaged)
    check(33, "Formal JSON Schema release gate passed across all production deliverables (PHASE1_SCHEMA.json)", p33, msg33)

    # Rule 34: Cross-Artifact Visual Evidence Consistency (Prompt Master Part A2)
    p34, msg34 = validate_page_quality_and_visual_audit_consistency(page_quality, visual_audit)
    check(34, "Cross-artifact visual evidence consistency between PAGE_EXTRACTION_QUALITY and VISUAL_VERIFICATION_AUDIT", p34, msg34)

    return passed_checks, failed_checks, results


def main():
    print("=" * 70)
    print("RUNNING AUTOMATED PHASE 1 VALIDATION SUITE (34 INTEGRITY RULES)")
    print("=" * 70)

    with open('SOURCE_CORPUS_INVENTORY.json', 'r', encoding='utf-8') as f:
        inventory = json.load(f)

    with open('RAW_EXTRACTED_QUESTIONS.json', 'r', encoding='utf-8') as f:
        all_records = json.load(f)

    with open('PAGE_EXTRACTION_QUALITY.json', 'r', encoding='utf-8') as f:
        page_quality = json.load(f)

    with open('DAMAGED_AND_INCOMPLETE_QUESTIONS_AUDIT.json', 'r', encoding='utf-8') as f:
        damaged = json.load(f)

    with open('VISUAL_VERIFICATION_AUDIT.json', 'r', encoding='utf-8') as f:
        visual_audit = json.load(f)

    with open('SUSPICIOUS_EXTRACTION_AUDIT.json', 'r', encoding='utf-8') as f:
        suspicious = json.load(f)

    with open('CORPUS_SUMMARY_METRICS.json', 'r', encoding='utf-8') as f:
        metrics = json.load(f)

    # Note: We do NOT pre-sync metrics in memory. Stored metrics are validated as-is against independent recomputation.

    passed_checks, failed_checks, results = run_all_validation_rules(
        inventory, all_records, page_quality, damaged, visual_audit, suspicious, metrics
    )

    print("=" * 70)
    print(f"CORE VALIDATION RESULT: {passed_checks}/34 RULES PASSED ({failed_checks} failed)")
    print("=" * 70)

    # Now execute the standalone adversarial mutation test suite against real validator functions
    import subprocess
    print("\nExecuting True Adversarial Validator Mutation Suite...")
    mut_proc = subprocess.run([sys.executable, 'scripts/test_phase1_validator_mutations.py'], capture_output=True, text=True, encoding='utf-8')
    print(mut_proc.stdout)
    if mut_proc.stderr:
        print(mut_proc.stderr)

    adv_passed = 0
    adv_total = 0
    if os.path.exists('scripts/mutation_results.json'):
        with open('scripts/mutation_results.json', 'r', encoding='utf-8') as f:
            m_res = json.load(f)
            adv_passed = m_res.get('adversarial_passed', 0)
            adv_total = m_res.get('adversarial_total', 0)

    # Update summary metrics
    metrics['damage_audit_entries'] = len(damaged)
    metrics['deterministic_damage_conditions'] = len(damaged)
    metrics['validation_rules_passed'] = passed_checks
    metrics['validation_rules_failed'] = failed_checks
    metrics['adversarial_tests_passed'] = adv_passed
    metrics['adversarial_tests_total'] = adv_total
    metrics['core_validation_rules_passed'] = passed_checks
    metrics['core_validation_rules_failed'] = failed_checks
    metrics['schema_validation_passed'] = 1 if failed_checks == 0 else 0
    metrics['schema_validation_failed'] = 0 if failed_checks == 0 else 1

    with open('CORPUS_SUMMARY_METRICS.json', 'w', encoding='utf-8') as f:
        json.dump(metrics, f, indent=2)

    with open('scripts/validation_results.json', 'w', encoding='utf-8') as f:
        json.dump({
            'core_results': results,
            'passed_rules': passed_checks,
            'failed_rules': failed_checks,
            'adversarial_passed': adv_passed,
            'adversarial_total': adv_total
        }, f, indent=2)

    if failed_checks > 0 or adv_passed < adv_total or mut_proc.returncode != 0:
        print("\nOVERALL STATUS: VALIDATION BLOCKED")
        sys.exit(1)
    else:
        print(f"\nOVERALL STATUS: ALL {passed_checks} RULES AND ALL {adv_passed} ADVERSARIAL MUTATIONS PASSED")
        sys.exit(0)


if __name__ == '__main__':
    main()
