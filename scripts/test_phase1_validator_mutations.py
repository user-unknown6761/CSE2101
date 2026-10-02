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
    validate_reconciliation_and_counts
)

print("=" * 70)
print("RUNNING TRUE ADVERSARIAL VALIDATOR MUTATION SUITE (19 IN-MEMORY MUTATIONS)")
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
total_mutations = 19
mutation_results = []

def record_test(test_id, name, rule_failed, caught, error_msg):
    global passed_mutations
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

# ------------------------------------------------------------------------------
# TEST A: Fabricated Marks (marks="12", marks_status="physically_established", evidence=None)
# ------------------------------------------------------------------------------
mut_records_a = copy.deepcopy(prod_records)
target_a = next(r for r in mut_records_a if r['record_type'] == 'question_occurrence')
target_a['marks'] = "12"
target_a['marks_status'] = "physically_established"
target_a['marks_source_evidence'] = None

ok_a, msg_a = validate_marks_integrity(mut_records_a)
record_test("TEST A", "Fabricated Marks with Null Evidence", "Rule 04", not ok_a, msg_a)

# ------------------------------------------------------------------------------
# TEST B: Invalid Marks Evidence (marks_status="physically_established", evidence_text omitted)
# ------------------------------------------------------------------------------
mut_records_b = copy.deepcopy(prod_records)
target_b = next(r for r in mut_records_b if r.get('marks_status') == 'physically_established')
target_b['marks_source_evidence'] = {
    'source_page': 3,
    'source_reference': "Page 3 header"
    # evidence_text deliberately deleted
}

ok_b, msg_b = validate_marks_integrity(mut_records_b)
record_test("TEST B", "Incomplete Marks Evidence (Missing evidence_text)", "Rule 04", not ok_b, msg_b)

# ------------------------------------------------------------------------------
# TEST C: Answerable Source Fragment (non_question_source_fragment marked answerable)
# ------------------------------------------------------------------------------
mut_records_c = copy.deepcopy(prod_records)
target_c = next(r for r in mut_records_c if r['record_type'] == 'non_question_source_fragment')
target_c['is_student_answerable'] = True

ok_c, msg_c = validate_answerability(mut_records_c)
record_test("TEST C", "Answerable Source Fragment Corruption", "Rule 12", not ok_c, msg_c)

# ------------------------------------------------------------------------------
# TEST D: Fake Visual Verification (Page marked VERIFIED without inspection evidence)
# ------------------------------------------------------------------------------
mut_page_d = copy.deepcopy(prod_page_quality)
target_d = next(p for p in mut_page_d if p.get('detection_status') == 'DETECTED' and p.get('verification_status') != 'VERIFIED')
target_d['verification_status'] = "VERIFIED"
target_d['visual_verification_status'] = "VERIFIED"
target_d['visually_reviewed'] = True
target_d['verified'] = True
target_d['review_record'] = None
target_d['verification_basis'] = None

ok_d, msg_d = validate_visual_pages(mut_page_d, prod_visual_audit)
record_test("TEST D", "Fake Visual Verification Without Review Evidence", "Rules 14 & 27", not ok_d, msg_d)

# ------------------------------------------------------------------------------
# TEST E: Empty Damage Audit (Empty damage_audit while deterministic damage exists)
# ------------------------------------------------------------------------------
mut_damaged_e = []

ok_e, msg_e = validate_damage_audit(prod_records, mut_damaged_e)
record_test("TEST E", "Empty Damage Audit Mutation", "Rule 06", not ok_e, msg_e)

# ------------------------------------------------------------------------------
# TEST F: Classification Mismatch (DOC-31 promoted to Tier 2 in inventory)
# ------------------------------------------------------------------------------
mut_inventory_f = copy.deepcopy(prod_inventory)
target_f = next(d for d in mut_inventory_f if d['document_id'] == 'DOC-31')
target_f['source_tier'] = 2

ok_f, msg_f = validate_governance_tiers(mut_inventory_f, prod_records)
record_test("TEST F", "Classification Mismatch (DOC-31 Tier 2 Promotion)", "Rules 17 & 22", not ok_f, msg_f)

# ------------------------------------------------------------------------------
# TEST G: Incorrect STATE B Visual Semantics (DOC-28 Q9 vertex K reverted to R)
# ------------------------------------------------------------------------------
mut_records_g = copy.deepcopy(prod_records)
target_g = next(r for r in mut_records_g if r['question_instance_id'] == 'DOC-28-P02-MCQ-Q09')
target_g['raw_text'] = (
    "The Breadth First Search algorithm has been implemented using the queue data structure. "
    "One possible order of visiting the nodes of the following graph is\n"
    "[Graph with 6 nodes {M, N, O, R, Q, P} and 7 edges (M,K), (M,N), (M,Q), (N,O), (N,Q), (Q,P), (P,O)]\n"
    "(a) MNOPQR\n(b) NQMPOR\n(c) QMNPRO\n(d) QMNPOR"
)
target_g['reconstruction_metadata']['reconstructed_text'] = target_g['raw_text']
target_g['reconstruction_metadata']['visual_semantic_verification']['graph_semantics']['vertices'] = ["M", "N", "O", "R", "Q", "P"]

ok_g, msg_g = validate_state_b_semantics(mut_records_g)
record_test("TEST G", "Incorrect STATE B Visual Semantics (DOC-28 Q9 Vertex K -> R)", "Rule 31", not ok_g, msg_g)

# ------------------------------------------------------------------------------
# TEST H1: Delete Legitimate Damage Entry
# ------------------------------------------------------------------------------
mut_damaged_h1 = copy.deepcopy(prod_damaged)
mut_damaged_h1.pop(0)

ok_h1, msg_h1 = validate_damage_audit(prod_records, mut_damaged_h1)
record_test("TEST H1", "Delete Legitimate Damage Entry", "Rule 06", not ok_h1, msg_h1)

# ------------------------------------------------------------------------------
# TEST H2: Change Damage Type
# ------------------------------------------------------------------------------
mut_damaged_h2 = copy.deepcopy(prod_damaged)
mut_damaged_h2[0]['damage_type'] = "corrupted_damage_type"

ok_h2, msg_h2 = validate_damage_audit(prod_records, mut_damaged_h2)
record_test("TEST H2", "Mutate Damage Type", "Rule 06", not ok_h2, msg_h2)

# ------------------------------------------------------------------------------
# TEST H3: Change Damage Severity
# ------------------------------------------------------------------------------
mut_damaged_h3 = copy.deepcopy(prod_damaged)
target_h3 = next(d for d in mut_damaged_h3 if d['severity'] == 'WARNING')
target_h3['severity'] = "CRITICAL"

ok_h3, msg_h3 = validate_damage_audit(prod_records, mut_damaged_h3)
record_test("TEST H3", "Mutate Damage Severity", "Rule 06", not ok_h3, msg_h3)

# ------------------------------------------------------------------------------
# TEST H4: Insert Fabricated Damage Entry
# ------------------------------------------------------------------------------
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
    'resolution_method': "None",
    'source_visual_reference': "None",
    'notes': "Fabricated"
})

ok_h4, msg_h4 = validate_damage_audit(prod_records, mut_damaged_h4)
record_test("TEST H4", "Insert Fabricated Damage Entry", "Rule 06", not ok_h4, msg_h4)

# ------------------------------------------------------------------------------
# TEST H5: Duplicate Legitimate Damage Entry
# ------------------------------------------------------------------------------
mut_damaged_h5 = copy.deepcopy(prod_damaged)
mut_damaged_h5.append(copy.deepcopy(mut_damaged_h5[0]))

ok_h5, msg_h5 = validate_damage_audit(prod_records, mut_damaged_h5)
record_test("TEST H5", "Duplicate Legitimate Damage Entry", "Rule 06", not ok_h5, msg_h5)

# ------------------------------------------------------------------------------
# TEST H6: Q8 C Code Semantic Corruption (keep match=true)
# ------------------------------------------------------------------------------
mut_records_h6 = copy.deepcopy(prod_records)
target_h6 = next(r for r in mut_records_h6 if r['question_instance_id'] == 'DOC-28-P02-MCQ-Q08')
# Corrupt one C code line while leaving all match=True
target_h6['reconstruction_metadata']['visual_semantic_verification']['code_semantics']['lines'][4] = '    printf("%s ", start->data);'

ok_h6, msg_h6 = validate_state_b_semantics(mut_records_h6)
record_test("TEST H6", "Q8 C Code Semantic Corruption (match=True preserved)", "Rule 31", not ok_h6, msg_h6)

# ------------------------------------------------------------------------------
# TEST H7: Q9 Graph Edge Semantic Corruption (keep match=true)
# ------------------------------------------------------------------------------
mut_records_h7 = copy.deepcopy(prod_records)
target_h7 = next(r for r in mut_records_h7 if r['question_instance_id'] == 'DOC-28-P02-MCQ-Q09')
# Mutate one edge from (M,K) to (M,Z) while leaving all match=True
target_h7['reconstruction_metadata']['visual_semantic_verification']['graph_semantics']['edges'][0] = ["M", "Z"]

ok_h7, msg_h7 = validate_state_b_semantics(mut_records_h7)
record_test("TEST H7", "Q9 Graph Edge Semantic Corruption (match=True preserved)", "Rule 31", not ok_h7, msg_h7)

# ------------------------------------------------------------------------------
# TEST H8: Q10 Tree Relationship Semantic Corruption (keep match=true)
# ------------------------------------------------------------------------------
mut_records_h8 = copy.deepcopy(prod_records)
target_h8 = next(r for r in mut_records_h8 if r['question_instance_id'] == 'DOC-28-P02-MCQ-Q10')
# Mutate parent-child relationship (parent 5 -> child 99) while leaving all match=True
target_h8['reconstruction_metadata']['visual_semantic_verification']['tree_semantics']['parent_child_relationships'][2]['child'] = "99"

ok_h8, msg_h8 = validate_state_b_semantics(mut_records_h8)
record_test("TEST H8", "Q10 Tree Relationship Corruption (match=True preserved)", "Rule 31", not ok_h8, msg_h8)

# ------------------------------------------------------------------------------
# TEST H9: Recorded SHA-256 Mutation
# ------------------------------------------------------------------------------
mut_inventory_h9 = copy.deepcopy(prod_inventory)
# Mutate last character of SHA-256 for DOC-01
old_sha = mut_inventory_h9[0]['sha256']
mut_sha = old_sha[:-1] + ('0' if old_sha[-1] != '0' else '1')
mut_inventory_h9[0]['sha256'] = mut_sha

ok_h9, msg_h9 = validate_crypto_hashes(mut_inventory_h9)
record_test("TEST H9", "Recorded SHA-256 Hash Byte Mutation", "Rule 01", not ok_h9, msg_h9)

# ------------------------------------------------------------------------------
# TEST H10: Canonical Visual-Status Contradiction (VERIFIED but verified=False)
# ------------------------------------------------------------------------------
mut_page_h10 = copy.deepcopy(prod_page_quality)
target_h10 = next(p for p in mut_page_h10 if p.get('verification_status') == 'VERIFIED')
target_h10['verified'] = False  # Direct contradiction with canonical verification_status

ok_h10, msg_h10 = validate_visual_pages(mut_page_h10, prod_visual_audit)
record_test("TEST H10", "Canonical Visual Lifecycle Contradiction (VERIFIED vs verified=False)", "Rules 14 & 27", not ok_h10, msg_h10)

# ------------------------------------------------------------------------------
# TEST H11: Render-Status / Artifact Reference Contradiction
# ------------------------------------------------------------------------------
mut_page_h11 = copy.deepcopy(prod_page_quality)
target_h11 = next(p for p in mut_page_h11 if p.get('render_status') == 'NOT_RENDERED')
target_h11['render_artifact_reference'] = "rendered_pages/phantom_render_page.png"  # Contradiction

ok_h11, msg_h11 = validate_visual_pages(mut_page_h11, prod_visual_audit)
record_test("TEST H11", "Render-Status / Artifact Contradiction (NOT_RENDERED with artifact)", "Rule 25", not ok_h11, msg_h11)

# ------------------------------------------------------------------------------
# TEST H12: Formal Schema Violation in Production Deliverables
# ------------------------------------------------------------------------------
mut_records_h12 = copy.deepcopy(prod_records)
# Invalidate record schema by setting record_type to an illegal string
mut_records_h12[0]['record_type'] = "corrupted_illegal_record_type"

ok_h12, msg_h12 = validate_formal_schemas(prod_inventory, mut_records_h12, prod_page_quality, prod_visual_audit, prod_damaged)
record_test("TEST H12", "Formal Schema Violation in Production Records", "Rule 33", not ok_h12, msg_h12)

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
