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
    validate_marks_integrity,
    validate_answerability,
    validate_visual_pages,
    validate_damage_audit,
    validate_governance_tiers,
    validate_state_b_semantics,
    validate_reconciliation_and_counts
)

print("=" * 70)
print("RUNNING TRUE ADVERSARIAL VALIDATOR MUTATION SUITE (7 IN-MEMORY MUTATIONS)")
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
total_mutations = 7
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
target_d['visually_reviewed'] = False
target_d['verified'] = False
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
# Mutate reconstructed text back to erroneous vertex R
target_g['raw_text'] = (
    "The Breadth First Search algorithm has been implemented using the queue data structure. "
    "One possible order of visiting the nodes of the following graph is\n"
    "[Graph with 6 nodes {M, N, O, R, Q, P} and edges (M,N), (N,O), (M,R), (M,Q), (N,Q), (O,P), (Q,P)]\n"
    "(a) MNOPQR\n(b) NQMPOR\n(c) QMNPRO\n(d) QMNPOR"
)
target_g['reconstruction_metadata']['reconstructed_text'] = target_g['raw_text']
# Mutate finding to falsely report match
target_g['reconstruction_metadata']['visual_semantic_verification']['element_level_findings'] = [
    {
        'element': "vertex_labels",
        'source': "6 circular nodes: {M, N, O, K, Q, P}",
        'reconstructed': "6 nodes {M, N, O, R, Q, P}",
        'match': True # False match claim
    }
]

ok_g, msg_g = validate_state_b_semantics(mut_records_g)
record_test("TEST G", "Incorrect STATE B Visual Semantics (DOC-28 Q9 Vertex K -> R)", "Rule 31", not ok_g, msg_g)

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
    print("\nALL 7 ADVERSARIAL MUTATIONS PASSED GENUINE VALIDATOR REJECTION")
    sys.exit(0)
