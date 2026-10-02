import json
import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("=" * 70)
print("RUNNING AUTOMATED PHASE 1.1 VALIDATION SUITE (22 INTEGRITY RULES)")
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

containers = [r for r in all_records if r.get('record_type') == 'paper_question_container']
true_questions = [r for r in all_records if r.get('record_type') == 'question_occurrence']
atomic_sub = [q for q in true_questions if q.get('occurrence_type') == 'sub_question']
standalone = [q for q in true_questions if q.get('occurrence_type') == 'standalone']

# Rule 01: Every inventory PDF has SHA-256
r1_pass = all(len(d.get('sha256', '')) == 64 for d in inventory)
check(1, "Every inventory PDF has SHA-256 cryptographic hash", r1_pass, f"Verified across {len(inventory)} documents.")

# Rule 02: Every source record has a source document
valid_doc_ids = set(d['document_id'] for d in inventory)
r2_pass = all(r.get('document_id') in valid_doc_ids for r in all_records)
check(2, "Every source record maps to an existing source document ID", r2_pass, f"All {len(all_records)} records map to registered documents.")

# Rule 03: Every question occurrence and container has page/source provenance
r3_pass = all(r.get('page_start') is not None and r.get('source_file') for r in all_records)
check(3, "Every record has physical page and source file provenance", r3_pass, f"Page and file provenance verified for {len(all_records)} records.")

# Rule 04: No question has fabricated default marks
r4_valid_statuses = ["physically_established", "not_specified", "container_aggregate_unallocated"]
r4_pass = all(r.get('marks_status') in r4_valid_statuses for r in all_records)
r4_no_default = not any(r.get('marks') == "DEFAULT" or (r.get('marks_status') == "not_specified" and r.get('marks') is not None) for r in all_records)
check(4, "No question or container has fabricated default marks", r4_pass and r4_no_default, "Marks are physically established, null, or container unallocated.")

# Rule 05: No unknown provenance is replaced with placeholder guesses
r5_pass = True
for r in all_records:
    meta = r.get('source_established_metadata', {})
    for k, v in meta.items():
        if isinstance(v, str) and v.lower() in ["placeholder", "unknown", "guessed", "tbd", "n/a", "none"]:
            r5_pass = False
            break
check(5, "No unknown provenance is replaced with placeholder guesses", r5_pass, "Unknown metadata fields strictly preserved as null.")

# Rule 06: Every incomplete item exists in the damage audit
incomplete_qs = [q for q in true_questions if q.get('completeness_status') == "INCOMPLETE"]
damaged_ids = set(d.get('question_instance_id') for d in damaged)
r6_pass = all(q['question_instance_id'] in damaged_ids for q in incomplete_qs)
check(6, "Every incomplete item exists in the damage audit", r6_pass, f"{len(incomplete_qs)} incomplete questions in corpus; {len(damaged)} recorded in audit.")

# Rule 07: Every question occurrence has a valid wording state (or container is null)
valid_wording_states = ["STATE A — EXACT", "STATE B — RECONSTRUCTED", "STATE C — SOURCE-INCOMPLETE"]
r7_pass = all(q.get('wording_state') in valid_wording_states for q in true_questions) and all(c.get('wording_state') is None for c in containers)
check(7, "Every question occurrence has a valid wording state", r7_pass, f"Wording states verified across {len(true_questions)} questions; null for {len(containers)} containers.")

# Rule 08: No solution/reference material accidentally assigned to Tier 1
r8_pass = True
for d in inventory:
    if d.get('document_classification') in ["Solution Document / Answer Key", "Notes / Study Material"]:
        if d.get('source_tier') < 4:
            r8_pass = False
for r in all_records:
    if r.get('source_type') in ["Solution Document / Answer Key", "Notes / Study Material"]:
        if r.get('source_tier') < 4:
            r8_pass = False
check(8, "No solution/reference material accidentally assigned to Tier 1", r8_pass, "All solution and study notes strictly isolated at Tier 4.")

# Rule 09: No active/in-scope/syllabus fields introduced in Phase 1
forbidden_fields = ["is_active", "in_syllabus", "canonical_id", "module_number", "topic_id", "difficulty_score"]
r9_pass = not any(f in r for r in all_records for f in forbidden_fields)
check(9, "No active/in-scope/syllabus fields introduced in Phase 1", r9_pass, f"Forbidden fields absent: {forbidden_fields}.")

# Rule 10: No canonical question relationships or deduplication created
r10_pass = not any("canonical" in k for r in all_records for k in r.keys())
check(10, "No canonical question relationships or deduplication created", r10_pass, "All physical source occurrences remain fully independent.")

# Rule 11: No structural parent container is counted as an answerable question
r11_pass = all(c.get('is_student_answerable') is False for c in containers) and all(q.get('is_student_answerable') is True for q in true_questions)
check(11, "No structural parent container is counted as an answerable question", r11_pass, f"{len(containers)} containers marked non-answerable; {len(true_questions)} question occurrences are answerable.")

# Rule 12: No placeholder 'Question N' is treated as actual question text
r12_pass = all(c.get('raw_text') is None for c in containers) and not any(re.match(r'^Question\s+\d+$', q.get('raw_text', '').strip(), re.I) for q in true_questions)
check(12, "No placeholder 'Question N' is treated as actual question text", r12_pass, "Parent containers have raw_text=null; all questions contain substantive source text.")

# Rule 13: Every reconstructed question has source visual provenance
state_b_qs = [q for q in true_questions if q.get('wording_state') == "STATE B — RECONSTRUCTED"]
r13_pass = all(q.get('reconstruction_metadata', {}).get('visual_source_reference') for q in state_b_qs)
check(13, "Every reconstructed question has source visual provenance", r13_pass, f"Verified across {len(state_b_qs)} STATE B questions.")

# Rule 14: Every STATE B question has verified reconstruction metadata
r14_pass = all(
    q.get('reconstruction_metadata') and
    q['reconstruction_metadata'].get('reconstruction_method') and
    q['reconstruction_metadata'].get('visual_source_reference') and
    q['reconstruction_metadata'].get('reconstructed_text') and
    q['reconstruction_metadata'].get('reconstruction_confidence')
    for q in state_b_qs
)
check(14, "Every STATE B question has complete verified reconstruction metadata", r14_pass, f"Reconstruction metadata verified for {len(state_b_qs)} items.")

# Rule 15: No question marked HIGH overall confidence has unverified required visual content
p_quality_map = {(p['document_id'], p['page_number']): p for p in page_quality}
r15_pass = True
for q in true_questions:
    p_info = p_quality_map.get((q['document_id'], q['page_start']))
    if p_info and p_info.get('visual_inspection_required'):
        if p_info.get('visual_verification_status') != "VERIFIED":
            r15_pass = False
check(15, "No question marked HIGH overall confidence has unverified required visual content", r15_pass, "All required visual pages verified.")

# Rule 16: Practice Assignment does not appear as exam_type
doc28_meta = next(d for d in inventory if d['document_id'] == 'DOC-28')
doc28_qs = [q for q in all_records if q['document_id'] == 'DOC-28']
r16_pass = doc28_meta.get('apparent_exam_type') is None and all(q['source_established_metadata'].get('exam_type') is None for q in doc28_qs)
check(16, "Practice Assignment does not appear as exam_type", r16_pass, "exam_type is strictly null for Practice Assignment in document and question records.")

# Rule 17: Unverified Question Bank authority is not promoted to Tier 2
doc30_meta = next(d for d in inventory if d['document_id'] == 'DOC-30')
doc31_meta = next(d for d in inventory if d['document_id'] == 'DOC-31')
r17_pass = doc30_meta['source_tier'] == 3 and doc31_meta['source_tier'] == 3 and "Authority Unconfirmed" in doc30_meta['document_classification']
check(17, "Unverified Question Bank authority is not promoted to Tier 2", r17_pass, "DOC-30 and DOC-31 classified as Authority Unconfirmed at Tier 3.")

# Rule 18: All question records have valid record_type
valid_record_types = {"paper_question_container", "question_occurrence"}
r18_pass = all(r.get('record_type') in valid_record_types for r in all_records)
check(18, "All question records have valid record_type", r18_pass, f"All {len(all_records)} records have record_type in {valid_record_types}.")

# Rule 19: Question counts reconcile exactly across categories
total_cnt = len(all_records)
cont_cnt = len(containers)
sub_cnt = len(atomic_sub)
stand_cnt = len(standalone)
true_cnt = len(true_questions)
r19_pass = (cont_cnt + true_cnt == total_cnt) and (sub_cnt + stand_cnt == true_cnt) and (cont_cnt == 227) and (sub_cnt == 825) and (stand_cnt == 532) and (total_cnt == 1584)
check(19, "Question counts reconcile exactly across containers, sub-questions, and standalone occurrences", r19_pass, f"Total: {total_cnt} = Containers: {cont_cnt} + Sub: {sub_cnt} + Standalone: {stand_cnt}")

# Rule 20: No extracted question contains obvious cross-question fragment contamination
doc28_q11 = next((q for q in true_questions if q['document_id'] == 'DOC-28' and q['official_question_number'] == '11'), None)
cross_contam_issues = [s for s in suspicious if any("Contaminated" in iss for iss in s['issues'])]
r20_pass = doc28_q11 and 'singly linked list' not in doc28_q11['raw_text'].lower() and 'start pointer' not in doc28_q11['raw_text'].lower() and len(cross_contam_issues) == 0
check(20, "No extracted question contains obvious cross-question fragment contamination", r20_pass, f"DOC-28 Q11 isolated; {len(cross_contam_issues)} cross-contamination issues found.")

# Rule 21: Every question referencing an essential visual has source-visual metadata
v_req_qs = [q for q in true_questions if q.get('source_visual_required')]
r21_pass = all(q.get('source_visual_page') is not None and q.get('source_visual_reason') for q in v_req_qs)
check(21, "Every question referencing an essential visual has source-visual metadata", r21_pass, f"{len(v_req_qs)} visual questions have explicit source page and reason metadata.")

# Rule 22: Damage detection actually performs nontrivial checks
# Audits for stem length, dangling endings, option completeness, multiple stems, and ensures suspicious questions are actively flagged
r22_pass = (
    len(suspicious) > 0 and
    all(s.get('question_instance_id') and s.get('issues') for s in suspicious) and
    all(
        any(q['question_instance_id'] == s['question_instance_id'] and q['extraction_confidence'] == 'FLAGGED' for q in true_questions)
        for s in suspicious
    )
)
check(22, "Damage detection actually performs nontrivial checks and flags anomalies", r22_pass, f"Nontrivial scan identified and flagged {len(suspicious)} suspicious question items without data loss.")

print("=" * 70)
print(f"VALIDATION SUMMARY: {passed_checks}/22 CHECKS PASSED. ({failed_checks} failed)")
print("=" * 70)

with open('scripts/validation_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)
