import json
import os
import sys
import copy

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Ensure script can import validate_phase1
script_dir = os.path.dirname(os.path.abspath(__file__))
workspace_dir = os.path.dirname(script_dir)
if workspace_dir not in sys.path:
    sys.path.insert(0, workspace_dir)
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

from scripts.validate_phase1 import (
    validate_crypto_hashes,
    validate_marks_integrity,
    validate_answerability,
    validate_visual_pages,
    validate_visual_state_consistency,
    validate_damage_audit,
    validate_governance_tiers,
    validate_state_b_semantics,
    validate_document_lifecycle,
    validate_formal_schemas,
    validate_page_audit_bijection,
    validate_page_quality_and_visual_audit_consistency,
    validate_summary_metrics,
    validate_reconciliation_and_counts
)

print("=" * 70)
print("RUNNING TRUE ADVERSARIAL VALIDATOR MUTATION SUITE (36 MUTATIONS)")
print("=" * 70)

# Load authoritative production artifacts
with open('SOURCE_CORPUS_INVENTORY.json', 'r', encoding='utf-8') as f:
    prod_inventory = json.load(f)

with open('RAW_EXTRACTED_QUESTIONS.json', 'r', encoding='utf-8') as f:
    prod_records = json.load(f)

with open('PAGE_EXTRACTION_QUALITY.json', 'r', encoding='utf-8') as f:
    prod_page_quality = json.load(f)

with open('DAMAGED_AND_INCOMPLETE_QUESTIONS_AUDIT.json', 'r', encoding='utf-8') as f:
    prod_damaged = json.load(f)

with open('VISUAL_VERIFICATION_AUDIT.json', 'r', encoding='utf-8') as f:
    prod_visual_audit = json.load(f)

with open('CORPUS_SUMMARY_METRICS.json', 'r', encoding='utf-8') as f:
    prod_metrics = json.load(f)

passed_mutations = 0
total_mutations = 0
mutation_results = []

def record_test(test_id, name, rule_failed, caught, error_msg):
    global passed_mutations, total_mutations
    total_mutations += 1
    status = "PASS" if caught else "FAIL"
    if caught:
        passed_mutations += 1
    mutation_results.append({
        'test_id': test_id,
        'name': name,
        'rule_failed': rule_failed,
        'caught': caught,
        'status': status,
        'validator_rejection_reason': error_msg
    })
    print(f"[{status}] {test_id} — {name}")
    if caught:
        print(f"      -> Correctly rejected by validator rule: {rule_failed}")
        print(f"      -> Validator output: '{error_msg}'")
    else:
        print(f"      -> ERROR: Validator failed to catch corruption! Return: '{error_msg}'")

# ==============================================================================
# SECTION 1: HISTORICAL FOUNDATIONAL MUTATIONS (TEST A - G)
# ==============================================================================

# TEST A: Fabricated Marks
mut_records_a = copy.deepcopy(prod_records)
target_q_a = next(r for r in mut_records_a if r.get('question_instance_id') == 'DOC-01-P01-Q01-sub-i')
target_q_a['marks'] = "12"
target_q_a['marks_status'] = "physically_established"
target_q_a['marks_source_evidence'] = None

try:
    p, msg = validate_marks_integrity(mut_records_a, raise_on_error=True)
    record_test("TEST A", "Fabricated Marks with Null Evidence", "Rule 04", False, "Validator did not raise")
except Exception as e:
    record_test("TEST A", "Fabricated Marks with Null Evidence", "Rule 04", True, str(e))

# TEST B: Incomplete Marks Evidence
mut_records_b = copy.deepcopy(prod_records)
target_q_b = next(r for r in mut_records_b if r.get('question_instance_id') == 'DOC-01-P01-Q01-sub-i')
target_q_b['marks_source_evidence'] = {
    'page': 1,
    'source_reference': "Page 1 Header line",
    'evidence_type': "section_total",
    'confidence': "HIGH"
}

try:
    p, msg = validate_marks_integrity(mut_records_b, raise_on_error=True)
    record_test("TEST B", "Incomplete Marks Evidence (Missing evidence_text)", "Rule 04", False, "Validator did not raise")
except Exception as e:
    record_test("TEST B", "Incomplete Marks Evidence (Missing evidence_text)", "Rule 04", True, str(e))

# TEST C: Answerable Source Fragment Corruption
mut_records_c = copy.deepcopy(prod_records)
target_frag_c = next(r for r in mut_records_c if r.get('record_type') == 'non_question_source_fragment')
target_frag_c['is_student_answerable'] = True

try:
    p, msg = validate_answerability(mut_records_c, raise_on_error=True)
    record_test("TEST C", "Answerable Source Fragment Corruption", "Rule 12", False, "Validator did not raise")
except Exception as e:
    record_test("TEST C", "Answerable Source Fragment Corruption", "Rule 12", True, str(e))

# TEST D: Fake Visual Verification Without Review Evidence
mut_pq_d = copy.deepcopy(prod_page_quality)
target_p_d = next(p for p in mut_pq_d if p.get('document_id') == 'DOC-01' and p.get('page_number') == 1)
target_p_d['verification_status'] = "VERIFIED"
target_p_d['visually_reviewed'] = True
target_p_d['verified'] = True
target_p_d['review_record'] = None

try:
    p, msg = validate_visual_state_consistency(mut_pq_d, prod_visual_audit, raise_on_error=True)
    record_test("TEST D", "Fake Visual Verification Without Review Evidence", "Rules 14 & 27", False, "Validator did not raise")
except Exception as e:
    record_test("TEST D", "Fake Visual Verification Without Review Evidence", "Rules 14 & 27", True, str(e))

# TEST E: Empty Damage Audit Mutation
try:
    p, msg = validate_damage_audit(prod_records, [], raise_on_error=True)
    record_test("TEST E", "Empty Damage Audit Mutation", "Rule 06", False, "Validator did not raise")
except Exception as e:
    record_test("TEST E", "Empty Damage Audit Mutation", "Rule 06", True, str(e))

# TEST F: Classification Mismatch (DOC-31 Tier 2 Promotion)
mut_inv_f = copy.deepcopy(prod_inventory)
doc31_f = next(d for d in mut_inv_f if d.get('document_id') == 'DOC-31')
doc31_f['source_tier'] = 2

try:
    p, msg = validate_governance_tiers(mut_inv_f, prod_records, raise_on_error=True)
    record_test("TEST F", "Classification Mismatch (DOC-31 Tier 2 Promotion)", "Rules 17 & 22", False, "Validator did not raise")
except Exception as e:
    record_test("TEST F", "Classification Mismatch (DOC-31 Tier 2 Promotion)", "Rules 17 & 22", True, str(e))

# TEST G: Incorrect STATE B Visual Semantics (DOC-28 Q9 Vertex K -> R)
mut_records_g = copy.deepcopy(prod_records)
q9_g = next(r for r in mut_records_g if r.get('question_instance_id') == 'DOC-28-P02-MCQ-Q09')
q9_g['raw_text'] = q9_g['raw_text'].replace("6 nodes {M, N, O, K, Q, P}", "6 nodes {M, N, O, R, Q, P}")
q9_g['raw_text'] = q9_g['raw_text'].replace("(M,K)", "(M,R)")

try:
    p, msg = validate_state_b_semantics(mut_records_g, raise_on_error=True)
    record_test("TEST G", "Incorrect STATE B Visual Semantics (DOC-28 Q9 Vertex K -> R)", "Rule 31", False, "Validator did not raise")
except Exception as e:
    record_test("TEST G", "Incorrect STATE B Visual Semantics (DOC-28 Q9 Vertex K -> R)", "Rule 31", True, str(e))

# ==============================================================================
# SECTION 2: ADVERSARIAL VALIDATION MUTATIONS (TEST H1 - H12)
# ==============================================================================

# TEST H1: Delete Legitimate Damage Entry
mut_damaged_h1 = copy.deepcopy(prod_damaged)
mut_damaged_h1.pop(0)

try:
    p, msg = validate_damage_audit(prod_records, mut_damaged_h1, raise_on_error=True)
    record_test("TEST H1", "Delete Legitimate Damage Entry", "Rule 06", False, "Validator did not raise")
except Exception as e:
    record_test("TEST H1", "Delete Legitimate Damage Entry", "Rule 06", True, str(e))

# TEST H2: Mutate Damage Type
mut_damaged_h2 = copy.deepcopy(prod_damaged)
mut_damaged_h2[0]['damage_type'] = "corrupted_damage_type"

try:
    p, msg = validate_damage_audit(prod_records, mut_damaged_h2, raise_on_error=True)
    record_test("TEST H2", "Mutate Damage Type", "Rule 06", False, "Validator did not raise")
except Exception as e:
    record_test("TEST H2", "Mutate Damage Type", "Rule 06", True, str(e))

# TEST H3: Mutate Damage Severity
mut_damaged_h3 = copy.deepcopy(prod_damaged)
mut_damaged_h3[1]['severity'] = "CRITICAL"

try:
    p, msg = validate_damage_audit(prod_records, mut_damaged_h3, raise_on_error=True)
    record_test("TEST H3", "Mutate Damage Severity", "Rule 06", False, "Validator did not raise")
except Exception as e:
    record_test("TEST H3", "Mutate Damage Severity", "Rule 06", True, str(e))

# TEST H4: Insert Fabricated Damage Entry
mut_damaged_h4 = copy.deepcopy(prod_damaged)
mut_damaged_h4.append({
    'question_instance_id': "DOC-01-P01-Q99-FABRICATED",
    'document_id': "DOC-01",
    'page': 1,
    'detector_id': "DET_FABRICATED",
    'damage_type': "fabricated_damage",
    'severity': "MAJOR",
    'evidence': "Fabricated non-existent damage condition",
    'resolution_status': "UNRESOLVED",
    'resolution_method': "none",
    'source_visual_reference': None,
    'notes': "Adversarial test injection"
})

try:
    p, msg = validate_damage_audit(prod_records, mut_damaged_h4, raise_on_error=True)
    record_test("TEST H4", "Insert Fabricated Damage Entry", "Rule 06", False, "Validator did not raise")
except Exception as e:
    record_test("TEST H4", "Insert Fabricated Damage Entry", "Rule 06", True, str(e))

# TEST H5: Duplicate Legitimate Damage Entry
mut_damaged_h5 = copy.deepcopy(prod_damaged)
mut_damaged_h5.append(copy.deepcopy(mut_damaged_h5[0]))

try:
    p, msg = validate_damage_audit(prod_records, mut_damaged_h5, raise_on_error=True)
    record_test("TEST H5", "Duplicate Legitimate Damage Entry", "Rule 06", False, "Validator did not raise")
except Exception as e:
    record_test("TEST H5", "Duplicate Legitimate Damage Entry", "Rule 06", True, str(e))

# TEST H6: Q8 C Code Semantic Corruption (keep match=true)
mut_records_h6 = copy.deepcopy(prod_records)
target_h6 = next(r for r in mut_records_h6 if r['question_instance_id'] == 'DOC-28-P02-MCQ-Q08')
target_h6['reconstruction_metadata']['visual_semantic_verification']['code_semantics']['lines'][4] = '    printf("%s ", start->data);'

try:
    p, msg = validate_state_b_semantics(mut_records_h6, raise_on_error=True)
    record_test("TEST H6", "Q8 C Code Semantic Corruption (match=True preserved)", "Rule 31", False, "Validator did not raise")
except Exception as e:
    record_test("TEST H6", "Q8 C Code Semantic Corruption (match=True preserved)", "Rule 31", True, str(e))

# TEST H7: Q9 Graph Edge Semantic Corruption (keep match=true)
mut_records_h7 = copy.deepcopy(prod_records)
target_h7 = next(r for r in mut_records_h7 if r['question_instance_id'] == 'DOC-28-P02-MCQ-Q09')
target_h7['reconstruction_metadata']['visual_semantic_verification']['graph_semantics']['edges'][0] = ["M", "Z"]

try:
    p, msg = validate_state_b_semantics(mut_records_h7, raise_on_error=True)
    record_test("TEST H7", "Q9 Graph Edge Semantic Corruption (match=True preserved)", "Rule 31", False, "Validator did not raise")
except Exception as e:
    record_test("TEST H7", "Q9 Graph Edge Semantic Corruption (match=True preserved)", "Rule 31", True, str(e))

# TEST H8: Q10 Tree Relationship Corruption (keep match=true)
mut_records_h8 = copy.deepcopy(prod_records)
target_h8 = next(r for r in mut_records_h8 if r['question_instance_id'] == 'DOC-28-P02-MCQ-Q10')
target_h8['reconstruction_metadata']['visual_semantic_verification']['tree_semantics']['parent_child_relationships'][2]['child'] = "99"

try:
    p, msg = validate_state_b_semantics(mut_records_h8, raise_on_error=True)
    record_test("TEST H8", "Q10 Tree Relationship Corruption (match=True preserved)", "Rule 31", False, "Validator did not raise")
except Exception as e:
    record_test("TEST H8", "Q10 Tree Relationship Corruption (match=True preserved)", "Rule 31", True, str(e))

# TEST H9: Recorded SHA-256 Hash Byte Mutation
mut_inv_h9 = copy.deepcopy(prod_inventory)
mut_inv_h9[0]['sha256'] = mut_inv_h9[0]['sha256'][:-1] + ('a' if mut_inv_h9[0]['sha256'][-1] != 'a' else 'b')

try:
    p, msg = validate_crypto_hashes(mut_inv_h9, raise_on_error=True)
    record_test("TEST H9", "Recorded SHA-256 Hash Byte Mutation", "Rule 01", False, "Validator did not raise")
except Exception as e:
    record_test("TEST H9", "Recorded SHA-256 Hash Byte Mutation", "Rule 01", True, str(e))

# TEST H10: Canonical Visual Lifecycle Contradiction (VERIFIED vs verified=False)
mut_page_h10 = copy.deepcopy(prod_page_quality)
target_h10 = next(p for p in mut_page_h10 if p.get('verification_status') == 'VERIFIED')
target_h10['verified'] = False

try:
    p, msg = validate_visual_state_consistency(mut_page_h10, prod_visual_audit, raise_on_error=True)
    record_test("TEST H10", "Canonical Visual Lifecycle Contradiction (VERIFIED vs verified=False)", "Rules 14 & 27", False, "Validator did not raise")
except Exception as e:
    record_test("TEST H10", "Canonical Visual Lifecycle Contradiction (VERIFIED vs verified=False)", "Rules 14 & 27", True, str(e))

# TEST H11: Render-Status / Artifact Contradiction (NOT_RENDERED with artifact)
mut_page_h11 = copy.deepcopy(prod_page_quality)
target_h11 = next(p for p in mut_page_h11 if p.get('render_status') == 'NOT_RENDERED')
target_h11['render_artifact_reference'] = "rendered_pages/phantom_render_page.png"

try:
    p, msg = validate_visual_state_consistency(mut_page_h11, prod_visual_audit, raise_on_error=True)
    record_test("TEST H11", "Render-Status / Artifact Contradiction (NOT_RENDERED with artifact)", "Rule 25", False, "Validator did not raise")
except Exception as e:
    record_test("TEST H11", "Render-Status / Artifact Contradiction (NOT_RENDERED with artifact)", "Rule 25", True, str(e))

# TEST H12: Formal Schema Violation in Production Records
mut_records_h12 = copy.deepcopy(prod_records)
mut_records_h12[0]['raw_text'] = True

try:
    p, msg = validate_formal_schemas(prod_inventory, mut_records_h12, prod_page_quality, prod_visual_audit, prod_damaged, raise_on_error=True)
    record_test("TEST H12", "Formal Schema Violation in Production Records", "Rule 33", False, "Validator did not raise")
except Exception as e:
    record_test("TEST H12", "Formal Schema Violation in Production Records", "Rule 33", True, str(e))

# ==============================================================================
# SECTION 3: NEW ARCHITECTURAL MUTATIONS (MUTATION M1 - M17)
# ==============================================================================

# ------------------------------------------------------------------------------
# FIX A: Page Dataset <-> Visual Audit Bijection (M1 - M5)
# ------------------------------------------------------------------------------

# MUTATION M1: Delete One Visual-Audit Page
mut_va_m1 = copy.deepcopy(prod_visual_audit)
mut_va_m1.pop(0)

try:
    p, msg = validate_page_audit_bijection(prod_page_quality, mut_va_m1, raise_on_error=True)
    record_test("MUTATION M1", "Delete One Visual-Audit Page", "Rule 34", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION M1", "Delete One Visual-Audit Page", "Rule 34", True, str(e))

# MUTATION M2: Add One Phantom Visual-Audit Page
mut_va_m2 = copy.deepcopy(prod_visual_audit)
mut_va_m2.append({
    'document_id': 'DOC-99',
    'page_number': 99,
    'detection_status': 'DETECTED',
    'render_status': 'NOT_RENDERED',
    'render_artifact_reference': None,
    'visual_review_status': 'NOT_REVIEWED',
    'verification_status': 'UNVERIFIED',
    'visually_reviewed': False,
    'verified': False,
    'review_record': None,
    'verification_basis': None,
    'visual_verification_status': 'DETECTED'
})

try:
    p, msg = validate_page_audit_bijection(prod_page_quality, mut_va_m2, raise_on_error=True)
    record_test("MUTATION M2", "Add One Phantom Visual-Audit Page", "Rule 34", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION M2", "Add One Phantom Visual-Audit Page", "Rule 34", True, str(e))

# MUTATION M3: Conflicting Verification Status for Same Page
mut_va_m3 = copy.deepcopy(prod_visual_audit)
target_va_m3 = next(v for v in mut_va_m3 if v['document_id'] == 'DOC-01' and v['page_number'] == 1)
target_va_m3['verification_status'] = "FLAGGED"

try:
    p, msg = validate_page_audit_bijection(prod_page_quality, mut_va_m3, raise_on_error=True)
    record_test("MUTATION M3", "Conflicting Verification Status for Same Page", "Rule 34", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION M3", "Conflicting Verification Status for Same Page", "Rule 34", True, str(e))

# MUTATION M4: Conflicting Render Status for Same Page
mut_va_m4 = copy.deepcopy(prod_visual_audit)
target_va_m4 = next(v for v in mut_va_m4 if v['document_id'] == 'DOC-28' and v['page_number'] == 2)
target_va_m4['render_status'] = "NOT_RENDERED"

try:
    p, msg = validate_page_audit_bijection(prod_page_quality, mut_va_m4, raise_on_error=True)
    record_test("MUTATION M4", "Conflicting Render Status for Same Page", "Rule 34", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION M4", "Conflicting Render Status for Same Page", "Rule 34", True, str(e))

# MUTATION M5: Conflicting Artifact Reference for Same Page
mut_va_m5 = copy.deepcopy(prod_visual_audit)
target_va_m5 = next(v for v in mut_va_m5 if v['document_id'] == 'DOC-28' and v['page_number'] == 2)
target_va_m5['render_artifact_reference'] = "rendered_pages/conflicting_tampered_path.png"

try:
    p, msg = validate_page_audit_bijection(prod_page_quality, mut_va_m5, raise_on_error=True)
    record_test("MUTATION M5", "Conflicting Artifact Reference for Same Page", "Rule 34", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION M5", "Conflicting Artifact Reference for Same Page", "Rule 34", True, str(e))

# ------------------------------------------------------------------------------
# FIX B: Document Lifecycle Must Be Derived (M6 - M8)
# ------------------------------------------------------------------------------

# MUTATION M6: Mark Previously NOT_RENDERED Page as RENDERED Without Inventory Update
mut_pq_m6 = copy.deepcopy(prod_page_quality)
target_pq_m6 = next(p for p in mut_pq_m6 if p.get('document_id') == 'DOC-01' and p.get('page_number') == 1)
target_pq_m6['render_status'] = "RENDERED"
target_pq_m6['render_artifact_reference'] = "rendered_pages/DOC-28_page_2.png"

try:
    p, msg = validate_document_lifecycle(prod_inventory, mut_pq_m6, raise_on_error=True)
    record_test("MUTATION M6", "Mark Previously NOT_RENDERED Page as RENDERED (Stale Inventory Disagreement)", "Rule 32", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION M6", "Mark Previously NOT_RENDERED Page as RENDERED (Stale Inventory Disagreement)", "Rule 32", True, str(e))

# MUTATION M7: Change Inventory Document Rendering Status Without Changing Page Evidence
mut_inv_m7 = copy.deepcopy(prod_inventory)
target_inv_m7 = next(d for d in mut_inv_m7 if d.get('document_id') == 'DOC-01')
target_inv_m7['document_rendering_status'] = "PARTIALLY_RENDERED"

try:
    p, msg = validate_document_lifecycle(mut_inv_m7, prod_page_quality, raise_on_error=True)
    record_test("MUTATION M7", "Change Inventory Document Rendering Status Without Page Evidence", "Rule 32", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION M7", "Change Inventory Document Rendering Status Without Page Evidence", "Rule 32", True, str(e))

# MUTATION M8: Set rendering_complete=True for a Document That Is Not Fully Rendered
mut_inv_m8 = copy.deepcopy(prod_inventory)
target_inv_m8 = next(d for d in mut_inv_m8 if d.get('document_id') == 'DOC-28')
target_inv_m8['rendering_complete'] = True

try:
    p, msg = validate_document_lifecycle(mut_inv_m8, prod_page_quality, raise_on_error=True)
    record_test("MUTATION M8", "Set rendering_complete=True for Partially Rendered Document", "Rule 32", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION M8", "Set rendering_complete=True for Partially Rendered Document", "Rule 32", True, str(e))

# ------------------------------------------------------------------------------
# FIX C: Recompute and Validate Summary Metrics (M9 - M14)
# ------------------------------------------------------------------------------

# MUTATION M9: Corrupt state_a in Summary Metrics
mut_metrics_m9 = copy.deepcopy(prod_metrics)
mut_metrics_m9['state_a'] = 9999

try:
    p, msg = validate_summary_metrics(mut_metrics_m9, prod_inventory, prod_records, prod_page_quality, prod_visual_audit, prod_damaged, raise_on_error=True)
    record_test("MUTATION M9", "Corrupt state_a in Summary Metrics", "Rule 24", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION M9", "Corrupt state_a in Summary Metrics", "Rule 24", True, str(e))

# MUTATION M10: Corrupt state_b in Summary Metrics
mut_metrics_m10 = copy.deepcopy(prod_metrics)
mut_metrics_m10['state_b'] = 9999

try:
    p, msg = validate_summary_metrics(mut_metrics_m10, prod_inventory, prod_records, prod_page_quality, prod_visual_audit, prod_damaged, raise_on_error=True)
    record_test("MUTATION M10", "Corrupt state_b in Summary Metrics", "Rule 24", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION M10", "Corrupt state_b in Summary Metrics", "Rule 24", True, str(e))

# MUTATION M11: Corrupt visual_verified_pages in Summary Metrics
mut_metrics_m11 = copy.deepcopy(prod_metrics)
mut_metrics_m11['visual_verified_pages'] = 9999

try:
    p, msg = validate_summary_metrics(mut_metrics_m11, prod_inventory, prod_records, prod_page_quality, prod_visual_audit, prod_damaged, raise_on_error=True)
    record_test("MUTATION M11", "Corrupt visual_verified_pages in Summary Metrics", "Rule 24", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION M11", "Corrupt visual_verified_pages in Summary Metrics", "Rule 24", True, str(e))

# MUTATION M12: Corrupt damage_records in Summary Metrics
mut_metrics_m12 = copy.deepcopy(prod_metrics)
mut_metrics_m12['damage_records'] = 9999

try:
    p, msg = validate_summary_metrics(mut_metrics_m12, prod_inventory, prod_records, prod_page_quality, prod_visual_audit, prod_damaged, raise_on_error=True)
    record_test("MUTATION M12", "Corrupt damage_records in Summary Metrics", "Rule 24", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION M12", "Corrupt damage_records in Summary Metrics", "Rule 24", True, str(e))

# MUTATION M13: Corrupt unresolved_damage_records in Summary Metrics
mut_metrics_m13 = copy.deepcopy(prod_metrics)
mut_metrics_m13['unresolved_damage_records'] = 9999

try:
    p, msg = validate_summary_metrics(mut_metrics_m13, prod_inventory, prod_records, prod_page_quality, prod_visual_audit, prod_damaged, raise_on_error=True)
    record_test("MUTATION M13", "Corrupt unresolved_damage_records in Summary Metrics", "Rule 24", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION M13", "Corrupt unresolved_damage_records in Summary Metrics", "Rule 24", True, str(e))

# MUTATION M14: Corrupt question_occurrences in Summary Metrics
mut_metrics_m14 = copy.deepcopy(prod_metrics)
mut_metrics_m14['question_occurrences'] = 9999

try:
    p, msg = validate_summary_metrics(mut_metrics_m14, prod_inventory, prod_records, prod_page_quality, prod_visual_audit, prod_damaged, raise_on_error=True)
    record_test("MUTATION M14", "Corrupt question_occurrences in Summary Metrics", "Rule 24", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION M14", "Corrupt question_occurrences in Summary Metrics", "Rule 24", True, str(e))

# ------------------------------------------------------------------------------
# FIX D: Visual State Consistency Contract (M15 - M17)
# ------------------------------------------------------------------------------

# MUTATION M15: Legacy VERIFIED While Canonical Status Is Not VERIFIED
mut_pq_m15 = copy.deepcopy(prod_page_quality)
target_pq_m15 = next(p for p in mut_pq_m15 if p.get('document_id') == 'DOC-01' and p.get('page_number') == 1)
target_pq_m15['visual_verification_status'] = "VERIFIED"
target_pq_m15['verification_status'] = "UNVERIFIED"

try:
    p, msg = validate_visual_state_consistency(mut_pq_m15, prod_visual_audit, raise_on_error=True)
    record_test("MUTATION M15", "Legacy VERIFIED While Canonical Status Is Not VERIFIED", "Rule 15", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION M15", "Legacy VERIFIED While Canonical Status Is Not VERIFIED", "Rule 15", True, str(e))

# MUTATION M16: visually_reviewed=True While visual_review_status Is Not REVIEWED
mut_pq_m16 = copy.deepcopy(prod_page_quality)
target_pq_m16 = next(p for p in mut_pq_m16 if p.get('document_id') == 'DOC-01' and p.get('page_number') == 1)
target_pq_m16['visually_reviewed'] = True
target_pq_m16['visual_review_status'] = "NOT_REVIEWED"

try:
    p, msg = validate_visual_state_consistency(mut_pq_m16, prod_visual_audit, raise_on_error=True)
    record_test("MUTATION M16", "visually_reviewed=True While visual_review_status Is Not REVIEWED", "Rule 15", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION M16", "visually_reviewed=True While visual_review_status Is Not REVIEWED", "Rule 15", True, str(e))

# MUTATION M17: verified=True While verification_status Is Not VERIFIED
mut_pq_m17 = copy.deepcopy(prod_page_quality)
target_pq_m17 = next(p for p in mut_pq_m17 if p.get('document_id') == 'DOC-01' and p.get('page_number') == 1)
target_pq_m17['verified'] = True
target_pq_m17['verification_status'] = "UNVERIFIED"

try:
    p, msg = validate_visual_state_consistency(mut_pq_m17, prod_visual_audit, raise_on_error=True)
    record_test("MUTATION M17", "verified=True While verification_status Is Not VERIFIED", "Rule 15", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION M17", "verified=True While verification_status Is Not VERIFIED", "Rule 15", True, str(e))

# ==============================================================================
# SUMMARY & ARTIFACT EXPORT
# ==============================================================================

print("=" * 70)
print(f"ADVERSARIAL MUTATION SUITE: {passed_mutations}/{total_mutations} CORRUPTIONS SUCCESSFULLY CAUGHT & REJECTED")
print("=" * 70)

# Save machine-readable mutation test output
output_file = 'scripts/mutation_results.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump({
        'adversarial_passed': passed_mutations,
        'adversarial_total': total_mutations,
        'test_results': mutation_results
    }, f, indent=2)

print(f"Mutation results saved to {output_file}")

if passed_mutations < total_mutations:
    print("\nADVERSARIAL TEST SUITE FAILED")
    sys.exit(1)
else:
    print(f"\nALL {total_mutations} ADVERSARIAL MUTATIONS PASSED GENUINE VALIDATOR REJECTION")
    sys.exit(0)
