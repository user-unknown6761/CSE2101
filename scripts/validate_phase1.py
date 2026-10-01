import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("=" * 60)
print("RUNNING AUTOMATED PHASE 1 VALIDATION SUITE")
print("=" * 60)

with open('SOURCE_CORPUS_INVENTORY.json', 'r', encoding='utf-8') as f:
    inventory = json.load(f)

with open('RAW_EXTRACTED_QUESTIONS.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

with open('PAGE_EXTRACTION_QUALITY.json', 'r', encoding='utf-8') as f:
    page_quality = json.load(f)

with open('DAMAGED_AND_INCOMPLETE_QUESTIONS_AUDIT.json', 'r', encoding='utf-8') as f:
    damaged = json.load(f)

passed_checks = 0
failed_checks = 0
results = []

def check(rule_num, description, condition, details=""):
    global passed_checks, failed_checks
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

# 1. Every inventory PDF has SHA-256.
r1_pass = all(len(d.get('sha256', '')) == 64 for d in inventory)
r1_details = f"Verified across {len(inventory)} documents."
check(1, "Every inventory PDF has SHA-256", r1_pass, r1_details)

# 2. Every source question has a source document.
valid_doc_ids = set(d['document_id'] for d in inventory)
r2_pass = all(q.get('document_id') in valid_doc_ids for q in questions)
r2_details = f"All {len(questions)} question instances map to known document IDs."
check(2, "Every source question has a source document", r2_pass, r2_details)

# 3. Every question occurrence has page/source provenance where available.
r3_pass = all(q.get('page_start') is not None and q.get('source_file') for q in questions)
r3_details = f"All {len(questions)} question instances have explicit page and source file provenance."
check(3, "Every question occurrence has page/source provenance", r3_pass, r3_details)

# 4. No question has fabricated default marks.
r4_pass = all(q.get('marks_status') in ["physically_established", "not_specified"] for q in questions)
r4_no_default = not any(q.get('marks') == "DEFAULT" or (q.get('marks_status') == "not_specified" and q.get('marks') is not None) for q in questions)
check(4, "No question has fabricated default marks", r4_pass and r4_no_default, "Marks are either physically established or explicitly null with not_specified status.")

# 5. No unknown provenance is replaced with placeholder guesses.
r5_pass = True
for q in questions:
    meta = q.get('source_established_metadata', {})
    for k, v in meta.items():
        if isinstance(v, str) and v.lower() in ["placeholder", "unknown", "guessed", "tbd", "n/a", "none"]:
            r5_pass = False
            break
check(5, "No unknown provenance is replaced with placeholder guesses", r5_pass, "Unknown provenance attributes are strictly preserved as null.")

# 6. Every incomplete item exists in the damage audit.
incomplete_qs = [q for q in questions if q.get('completeness_status') == "INCOMPLETE"]
damaged_ids = set(d.get('question_instance_id') for d in damaged)
r6_pass = all(q['question_instance_id'] in damaged_ids for q in incomplete_qs)
check(6, "Every incomplete item exists in the damage audit", r6_pass, f"{len(incomplete_qs)} incomplete items in corpus; {len(damaged)} recorded in audit.")

# 7. Every extracted question has a wording state.
valid_wording_states = ["STATE A — EXACT", "STATE B — RECONSTRUCTED", "STATE C — SOURCE-INCOMPLETE"]
r7_pass = all(q.get('wording_state') in valid_wording_states for q in questions)
check(7, "Every extracted question has a valid wording state", r7_pass, f"Wording states verified across {len(questions)} items.")

# 8. Every source file classified as solution/reference does not accidentally become Tier 1.
r8_pass = True
for d in inventory:
    if d.get('document_classification') in ["Solution Document / Answer Key", "Notes / Study Material"]:
        if d.get('source_tier') < 4:
            r8_pass = False
            break
for q in questions:
    if q.get('source_type') in ["Solution Document / Answer Key", "Notes / Study Material"]:
        if q.get('source_tier') < 4:
            r8_pass = False
            break
check(8, "No solution/reference material accidentally assigned to Tier 1", r8_pass, "All solution and study notes strictly isolated at Tier 4.")

# 9. No active/in-scope fields are introduced in Phase 1.
forbidden_fields = ["is_active", "in_syllabus", "canonical_id", "module_number", "topic_id", "difficulty_score"]
r9_pass = True
found_forbidden = []
for q in questions:
    for f_field in forbidden_fields:
        if f_field in q:
            r9_pass = False
            found_forbidden.append(f_field)
check(9, "No active/in-scope/syllabus fields introduced in Phase 1", r9_pass, f"Forbidden fields checked: {forbidden_fields}.")

# 10. No canonical question relationships are created in Phase 1.
r10_pass = not any("canonical" in k for q in questions for k in q.keys())
check(10, "No canonical question relationships or deduplication created", r10_pass, "All physical source occurrences remain fully independent.")

print("=" * 60)
print(f"VALIDATION SUMMARY: {passed_checks}/10 CHECKS PASSED. ({failed_checks} failed)")
print("=" * 60)

with open('scripts/validation_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)
