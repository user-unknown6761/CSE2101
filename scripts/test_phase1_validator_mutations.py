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
    validate_damage_audit,
    validate_governance_tiers,
    validate_state_b_semantics,
    validate_document_lifecycle,
    validate_formal_schemas,
    validate_page_quality_and_visual_audit_consistency,
    validate_summary_metrics,
    validate_reconciliation_and_counts
)

print("=" * 70)
print("RUNNING TRUE ADVERSARIAL VALIDATOR MUTATION SUITE")
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
# FOUNDATIONAL MUTATIONS (TEST A - G, H1 - H5, H9, H12)
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
    p, msg = validate_visual_pages(mut_pq_d, prod_visual_audit, raise_on_error=True)
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

# TEST H9: Recorded SHA-256 Hash Byte Mutation
mut_inv_h9 = copy.deepcopy(prod_inventory)
mut_inv_h9[0]['sha256'] = mut_inv_h9[0]['sha256'][:-1] + ('a' if mut_inv_h9[0]['sha256'][-1] != 'a' else 'b')

try:
    p, msg = validate_crypto_hashes(mut_inv_h9, raise_on_error=True)
    record_test("TEST H9", "Recorded SHA-256 Hash Byte Mutation", "Rule 01", False, "Validator did not raise")
except Exception as e:
    record_test("TEST H9", "Recorded SHA-256 Hash Byte Mutation", "Rule 01", True, str(e))

# TEST H12: Formal Schema Violation in Production Records
mut_records_h12 = copy.deepcopy(prod_records)
mut_records_h12[0]['raw_text'] = True

try:
    p, msg = validate_formal_schemas(prod_inventory, mut_records_h12, prod_page_quality, prod_visual_audit, prod_damaged, raise_on_error=True)
    record_test("TEST H12", "Formal Schema Violation in Production Records", "Rule 33", False, "Validator did not raise")
except Exception as e:
    record_test("TEST H12", "Formal Schema Violation in Production Records", "Rule 33", True, str(e))

# ==============================================================================
# GROUP A: DOCUMENT RENDERING LIFECYCLE (A1, A2, A3)
# ==============================================================================

# A1: Change DOC-28 rendered page to NOT_RENDERED -> document lifecycle changes -> reject stale inventory
mut_pq_a1 = copy.deepcopy(prod_page_quality)
doc28_p2_a1 = next(p for p in mut_pq_a1 if p.get('document_id') == 'DOC-28' and p.get('page_number') == 2)
doc28_p2_a1['render_status'] = "NOT_RENDERED"
doc28_p2_a1['render_artifact_reference'] = None

try:
    p, msg = validate_document_lifecycle(prod_inventory, mut_pq_a1, raise_on_error=True)
    record_test("MUTATION A1", "DOC-28 Page Render Reverted to NOT_RENDERED (Stale Inventory Disagreement)", "Rule 32", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION A1", "DOC-28 Page Render Reverted to NOT_RENDERED (Stale Inventory Disagreement)", "Rule 32", True, str(e))

# A2: Add a fake rendered page in page quality without artifact on disk
mut_pq_a2 = copy.deepcopy(prod_page_quality)
doc01_p1_a2 = next(p for p in mut_pq_a2 if p.get('document_id') == 'DOC-01' and p.get('page_number') == 1)
doc01_p1_a2['render_status'] = "RENDERED"
doc01_p1_a2['render_artifact_reference'] = "rendered_pages/non_existent_fake_render_doc01.png"

try:
    p, msg = validate_visual_pages(mut_pq_a2, prod_visual_audit, raise_on_error=True)
    record_test("MUTATION A2", "Fake Rendered Page Without Disk Artifact", "Rule 25", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION A2", "Fake Rendered Page Without Disk Artifact", "Rule 25", True, str(e))

# A3: Make document lifecycle in inventory disagree with page-level evidence
mut_inv_a3 = copy.deepcopy(prod_inventory)
doc01_a3 = next(d for d in mut_inv_a3 if d.get('document_id') == 'DOC-01')
doc01_a3['document_rendering_status'] = "PARTIALLY_RENDERED"

try:
    p, msg = validate_document_lifecycle(mut_inv_a3, prod_page_quality, raise_on_error=True)
    record_test("MUTATION A3", "Inventory Lifecycle Disagrees with Page-Level Evidence", "Rule 32", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION A3", "Inventory Lifecycle Disagrees with Page-Level Evidence", "Rule 32", True, str(e))

# ==============================================================================
# GROUP B: PAGE_EXTRACTION_QUALITY <-> VISUAL_VERIFICATION_AUDIT (B1, B2, B3, B4)
# ==============================================================================

# B1: Delete one visual-audit record
mut_va_b1 = copy.deepcopy(prod_visual_audit)
mut_va_b1.pop(0)

try:
    p, msg = validate_page_quality_and_visual_audit_consistency(prod_page_quality, mut_va_b1, raise_on_error=True)
    record_test("MUTATION B1", "Delete Visual-Audit Record", "Rule 34", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION B1", "Delete Visual-Audit Record", "Rule 34", True, str(e))

# B2: Mutate visual-audit verification_status
mut_va_b2 = copy.deepcopy(prod_visual_audit)
mut_va_b2[0]['verification_status'] = "FLAGGED"

try:
    p, msg = validate_page_quality_and_visual_audit_consistency(prod_page_quality, mut_va_b2, raise_on_error=True)
    record_test("MUTATION B2", "Mutate Visual-Audit Verification Status", "Rule 34", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION B2", "Mutate Visual-Audit Verification Status", "Rule 34", True, str(e))

# B3: Mutate visual-audit render artifact reference
mut_va_b3 = copy.deepcopy(prod_visual_audit)
doc28_p2_va = next(v for v in mut_va_b3 if v.get('document_id') == 'DOC-28' and v.get('page_number') == 2)
doc28_p2_va['render_artifact_reference'] = "rendered_pages/tampered_path.png"

try:
    p, msg = validate_page_quality_and_visual_audit_consistency(prod_page_quality, mut_va_b3, raise_on_error=True)
    record_test("MUTATION B3", "Mutate Visual-Audit Render Artifact Reference", "Rule 34", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION B3", "Mutate Visual-Audit Render Artifact Reference", "Rule 34", True, str(e))

# B4: Mutate one canonical lifecycle field only on one side (visual_review_status in visual_audit)
mut_va_b4 = copy.deepcopy(prod_visual_audit)
doc28_p2_va4 = next(v for v in mut_va_b4 if v.get('document_id') == 'DOC-28' and v.get('page_number') == 2)
doc28_p2_va4['visual_review_status'] = "NOT_REVIEWED"

try:
    p, msg = validate_page_quality_and_visual_audit_consistency(prod_page_quality, mut_va_b4, raise_on_error=True)
    record_test("MUTATION B4", "One-Sided Lifecycle Mismatch (visual_review_status)", "Rule 34", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION B4", "One-Sided Lifecycle Mismatch (visual_review_status)", "Rule 34", True, str(e))

# ==============================================================================
# GROUP C: SUMMARY METRICS DERIVATION (C1, C2, C3, C4)
# ==============================================================================

# C1: Mutate summary count (physical_records)
mut_metrics_c1 = copy.deepcopy(prod_metrics)
mut_metrics_c1['physical_records'] = 9999

try:
    p, msg = validate_summary_metrics(mut_metrics_c1, prod_inventory, prod_records, prod_page_quality, prod_visual_audit, prod_damaged, raise_on_error=True)
    record_test("MUTATION C1", "Mutate Summary Physical Records Count", "Rule 24", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION C1", "Mutate Summary Physical Records Count", "Rule 24", True, str(e))

# C2: Mutate visual metric (visual_detected_pages)
mut_metrics_c2 = copy.deepcopy(prod_metrics)
mut_metrics_c2['visual_detected_pages'] = 9999

try:
    p, msg = validate_summary_metrics(mut_metrics_c2, prod_inventory, prod_records, prod_page_quality, prod_visual_audit, prod_damaged, raise_on_error=True)
    record_test("MUTATION C2", "Mutate Summary Visual Detected Pages Metric", "Rule 24", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION C2", "Mutate Summary Visual Detected Pages Metric", "Rule 24", True, str(e))

# C3: Mutate damage metric (damage_audit_entries)
mut_metrics_c3 = copy.deepcopy(prod_metrics)
mut_metrics_c3['damage_audit_entries'] = 9999

try:
    p, msg = validate_summary_metrics(mut_metrics_c3, prod_inventory, prod_records, prod_page_quality, prod_visual_audit, prod_damaged, raise_on_error=True)
    record_test("MUTATION C3", "Mutate Summary Damage Audit Entries Metric", "Rule 24", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION C3", "Mutate Summary Damage Audit Entries Metric", "Rule 24", True, str(e))

# C4: Mutate state count (state_a)
mut_metrics_c4 = copy.deepcopy(prod_metrics)
mut_metrics_c4['state_a'] = 9999

try:
    p, msg = validate_summary_metrics(mut_metrics_c4, prod_inventory, prod_records, prod_page_quality, prod_visual_audit, prod_damaged, raise_on_error=True)
    record_test("MUTATION C4", "Mutate Summary State A Count", "Rule 24", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION C4", "Mutate Summary State A Count", "Rule 24", True, str(e))

# ==============================================================================
# GROUP D: VISUAL STATUS CONSISTENCY (D1 - D7)
# ==============================================================================

# D1: VERIFIED + verified=False
mut_pq_d1 = copy.deepcopy(prod_page_quality)
p2_d1 = next(p for p in mut_pq_d1 if p.get('document_id') == 'DOC-28' and p.get('page_number') == 2)
p2_d1['verification_status'] = "VERIFIED"
p2_d1['verified'] = False

try:
    p, msg = validate_visual_pages(mut_pq_d1, prod_visual_audit, raise_on_error=True)
    record_test("MUTATION D1", "Visual Contradiction: VERIFIED + verified=False", "Rule 15", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION D1", "Visual Contradiction: VERIFIED + verified=False", "Rule 15", True, str(e))

# D2: REVIEWED + visually_reviewed=False
mut_pq_d2 = copy.deepcopy(prod_page_quality)
p2_d2 = next(p for p in mut_pq_d2 if p.get('document_id') == 'DOC-28' and p.get('page_number') == 2)
p2_d2['visual_review_status'] = "REVIEWED"
p2_d2['visually_reviewed'] = False

try:
    p, msg = validate_visual_pages(mut_pq_d2, prod_visual_audit, raise_on_error=True)
    record_test("MUTATION D2", "Visual Contradiction: REVIEWED + visually_reviewed=False", "Rule 15", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION D2", "Visual Contradiction: REVIEWED + visually_reviewed=False", "Rule 15", True, str(e))

# D3: visual_verification_status=VERIFIED + verification_status=UNVERIFIED
mut_pq_d3 = copy.deepcopy(prod_page_quality)
p2_d3 = next(p for p in mut_pq_d3 if p.get('document_id') == 'DOC-28' and p.get('page_number') == 2)
p2_d3['visual_verification_status'] = "VERIFIED"
p2_d3['verification_status'] = "UNVERIFIED"

try:
    p, msg = validate_visual_pages(mut_pq_d3, prod_visual_audit, raise_on_error=True)
    record_test("MUTATION D3", "Visual Contradiction: visual_verification_status=VERIFIED + verification_status=UNVERIFIED", "Rule 15", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION D3", "Visual Contradiction: visual_verification_status=VERIFIED + verification_status=UNVERIFIED", "Rule 15", True, str(e))

# D4: RENDERED + missing artifact reference
mut_pq_d4 = copy.deepcopy(prod_page_quality)
p2_d4 = next(p for p in mut_pq_d4 if p.get('document_id') == 'DOC-28' and p.get('page_number') == 2)
p2_d4['render_status'] = "RENDERED"
p2_d4['render_artifact_reference'] = None

try:
    p, msg = validate_visual_pages(mut_pq_d4, prod_visual_audit, raise_on_error=True)
    record_test("MUTATION D4", "Visual Contradiction: RENDERED + null artifact reference", "Rule 25", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION D4", "Visual Contradiction: RENDERED + null artifact reference", "Rule 25", True, str(e))

# D5: NOT_RENDERED + artifact reference
mut_pq_d5 = copy.deepcopy(prod_page_quality)
p1_d5 = next(p for p in mut_pq_d5 if p.get('document_id') == 'DOC-01' and p.get('page_number') == 1)
p1_d5['render_status'] = "NOT_RENDERED"
p1_d5['render_artifact_reference'] = "rendered_pages/DOC-28_page_2.png"

try:
    p, msg = validate_visual_pages(mut_pq_d5, prod_visual_audit, raise_on_error=True)
    record_test("MUTATION D5", "Visual Contradiction: NOT_RENDERED + artifact reference", "Rule 15", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION D5", "Visual Contradiction: NOT_RENDERED + artifact reference", "Rule 15", True, str(e))

# D6: VERIFIED without REVIEWED
mut_pq_d6 = copy.deepcopy(prod_page_quality)
p2_d6 = next(p for p in mut_pq_d6 if p.get('document_id') == 'DOC-28' and p.get('page_number') == 2)
p2_d6['verification_status'] = "VERIFIED"
p2_d6['visual_review_status'] = "NOT_REVIEWED"

try:
    p, msg = validate_visual_pages(mut_pq_d6, prod_visual_audit, raise_on_error=True)
    record_test("MUTATION D6", "Visual Contradiction: VERIFIED without REVIEWED", "Rule 15", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION D6", "Visual Contradiction: VERIFIED without REVIEWED", "Rule 15", True, str(e))

# D7: REVIEWED without render evidence
mut_pq_d7 = copy.deepcopy(prod_page_quality)
p2_d7 = next(p for p in mut_pq_d7 if p.get('document_id') == 'DOC-28' and p.get('page_number') == 2)
p2_d7['visual_review_status'] = "REVIEWED"
p2_d7['render_status'] = "NOT_RENDERED"
p2_d7['render_artifact_reference'] = None

try:
    p, msg = validate_visual_pages(mut_pq_d7, prod_visual_audit, raise_on_error=True)
    record_test("MUTATION D7", "Visual Contradiction: REVIEWED without render evidence", "Rule 15", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION D7", "Visual Contradiction: REVIEWED without render evidence", "Rule 15", True, str(e))

# ==============================================================================
# GROUP E: SEMANTIC VERIFICATION MUTATIONS (E1 - E7)
# ==============================================================================

# E1: Remove one Q8 code line
mut_records_e1 = copy.deepcopy(prod_records)
q8_e1 = next(r for r in mut_records_e1 if r.get('question_instance_id') == 'DOC-28-P02-MCQ-Q08')
q8_e1['reconstruction_metadata']['visual_semantic_verification']['code_semantics']['lines'].pop()

try:
    p, msg = validate_state_b_semantics(mut_records_e1, raise_on_error=True)
    record_test("MUTATION E1", "Remove Q8 Code Line (match=True preserved)", "Rule 31", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION E1", "Remove Q8 Code Line (match=True preserved)", "Rule 31", True, str(e))

# E2: Duplicate one Q8 code line
mut_records_e2 = copy.deepcopy(prod_records)
q8_e2 = next(r for r in mut_records_e2 if r.get('question_instance_id') == 'DOC-28-P02-MCQ-Q08')
lines_e2 = q8_e2['reconstruction_metadata']['visual_semantic_verification']['code_semantics']['lines']
lines_e2.append(lines_e2[-1])

try:
    p, msg = validate_state_b_semantics(mut_records_e2, raise_on_error=True)
    record_test("MUTATION E2", "Duplicate Q8 Code Line (match=True preserved)", "Rule 31", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION E2", "Duplicate Q8 Code Line (match=True preserved)", "Rule 31", True, str(e))

# E3: Mutate Q9 vertex (replace 'K' with 'Z')
mut_records_e3 = copy.deepcopy(prod_records)
q9_e3 = next(r for r in mut_records_e3 if r.get('question_instance_id') == 'DOC-28-P02-MCQ-Q09')
verts_e3 = q9_e3['reconstruction_metadata']['visual_semantic_verification']['graph_semantics']['vertices']
idx_k = verts_e3.index('K')
verts_e3[idx_k] = 'Z'

try:
    p, msg = validate_state_b_semantics(mut_records_e3, raise_on_error=True)
    record_test("MUTATION E3", "Mutate Q9 Graph Vertex (K -> Z, match=True preserved)", "Rule 31", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION E3", "Mutate Q9 Graph Vertex (K -> Z, match=True preserved)", "Rule 31", True, str(e))

# E4: Remove one Q9 edge
mut_records_e4 = copy.deepcopy(prod_records)
q9_e4 = next(r for r in mut_records_e4 if r.get('question_instance_id') == 'DOC-28-P02-MCQ-Q09')
q9_e4['reconstruction_metadata']['visual_semantic_verification']['graph_semantics']['edges'].pop()

try:
    p, msg = validate_state_b_semantics(mut_records_e4, raise_on_error=True)
    record_test("MUTATION E4", "Remove Q9 Graph Edge (match=True preserved)", "Rule 31", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION E4", "Remove Q9 Graph Edge (match=True preserved)", "Rule 31", True, str(e))

# E5: Add fake Q9 edge
mut_records_e5 = copy.deepcopy(prod_records)
q9_e5 = next(r for r in mut_records_e5 if r.get('question_instance_id') == 'DOC-28-P02-MCQ-Q09')
q9_e5['reconstruction_metadata']['visual_semantic_verification']['graph_semantics']['edges'].append(["K", "O"])

try:
    p, msg = validate_state_b_semantics(mut_records_e5, raise_on_error=True)
    record_test("MUTATION E5", "Add Fake Q9 Graph Edge (match=True preserved)", "Rule 31", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION E5", "Add Fake Q9 Graph Edge (match=True preserved)", "Rule 31", True, str(e))

# E6: Mutate Q10 tree root ('1' -> '99')
mut_records_e6 = copy.deepcopy(prod_records)
q10_e6 = next(r for r in mut_records_e6 if r.get('question_instance_id') == 'DOC-28-P02-MCQ-Q10')
q10_e6['reconstruction_metadata']['visual_semantic_verification']['tree_semantics']['root'] = "99"

try:
    p, msg = validate_state_b_semantics(mut_records_e6, raise_on_error=True)
    record_test("MUTATION E6", "Mutate Q10 Tree Root (1 -> 99, match=True preserved)", "Rule 31", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION E6", "Mutate Q10 Tree Root (1 -> 99, match=True preserved)", "Rule 31", True, str(e))

# E7: Remove Q10 parent-child relationship
mut_records_e7 = copy.deepcopy(prod_records)
q10_e7 = next(r for r in mut_records_e7 if r.get('question_instance_id') == 'DOC-28-P02-MCQ-Q10')
q10_e7['reconstruction_metadata']['visual_semantic_verification']['tree_semantics']['parent_child_relationships'].pop()

try:
    p, msg = validate_state_b_semantics(mut_records_e7, raise_on_error=True)
    record_test("MUTATION E7", "Remove Q10 Tree Parent-Child Relationship (match=True preserved)", "Rule 31", False, "Validator did not raise")
except Exception as e:
    record_test("MUTATION E7", "Remove Q10 Tree Parent-Child Relationship (match=True preserved)", "Rule 31", True, str(e))

print("=" * 70)
print(f"ADVERSARIAL MUTATION SUITE: {passed_mutations}/{total_mutations} CORRUPTIONS SUCCESSFULLY CAUGHT & REJECTED")
print("=" * 70)

with open('scripts/mutation_results.json', 'w', encoding='utf-8') as f:
    json.dump({
        'adversarial_passed': passed_mutations,
        'adversarial_total': total_mutations,
        'mutations': mutation_results
    }, f, indent=2)

print("Mutation results saved to scripts/mutation_results.json\n")

if passed_mutations == total_mutations:
    print(f"ALL {total_mutations} ADVERSARIAL MUTATIONS PASSED GENUINE VALIDATOR REJECTION\n")
    sys.exit(0)
else:
    print(f"FAILED: Only {passed_mutations}/{total_mutations} mutations caught!\n")
    sys.exit(1)
