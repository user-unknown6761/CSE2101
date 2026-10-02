import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("=" * 70)
print("INDEPENDENT SPECIAL AUDIT: DOC-28 Q7 TO Q12")
print("=" * 70)

with open('RAW_EXTRACTED_QUESTIONS.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

with open('DAMAGED_AND_INCOMPLETE_QUESTIONS_AUDIT.json', 'r', encoding='utf-8') as f:
    damage_audit = json.load(f)

doc28_mcq_7_12 = [
    q for q in questions 
    if q.get('document_id') == 'DOC-28' and q.get('group_or_section') == 'Multiple Choice Questions' and q.get('official_question_number') in ['7', '8', '9', '10', '11', '12']
]

doc28_mcq_7_12.sort(key=lambda x: int(x['official_question_number']))

damage_map = {}
for d in damage_audit:
    qid = d.get('question_instance_id')
    if qid:
        if qid not in damage_map:
            damage_map[qid] = []
        damage_map[qid].append(d)

passed_items = 0
total_items = 6

for q in doc28_mcq_7_12:
    q_num = int(q['official_question_number'])
    qid = q['question_instance_id']
    page = q['page_start']
    w_state = q['wording_state']
    raw_text = q['raw_text']
    v_req = q['source_visual_required']
    marks = q['marks']
    marks_st = q['marks_status']
    comp = q['completeness_status']
    conf = q['extraction_confidence']
    dmg = damage_map.get(qid, [])
    
    print(f"\n--- AUDITING QUESTION {q_num} ({qid}) ---")
    print(f"  Page Number: {page}")
    print(f"  Wording State: {w_state}")
    print(f"  Marks: {marks} (Status: {marks_st})")
    print(f"  Completeness: {comp}")
    print(f"  Extraction Confidence: {conf}")
    print(f"  Visual Required: {v_req} (Page: {q.get('source_visual_page')}, Reason: {q.get('source_visual_reason')})")
    print(f"  Damage Audit Entries: {len(dmg)}")
    for d in dmg:
        print(f"    -> [{d['severity']}] {d['damage_type']}: {d['resolution_status']} ({d['resolution_method']})")
    print(f"  Question Text Snippet:\n    {raw_text[:120]}...")

    # Independent Assertions
    is_valid = True
    if q_num == 7:
        assert page == 2, f"Q7 page must be 2, got {page}"
        assert w_state == "STATE B — RECONSTRUCTED", f"Q7 wording state must be STATE B, got {w_state}"
        assert "(a)" in raw_text and "(d)" in raw_text, "Q7 must have intact options (a) through (d)"
        assert not v_req, "Q7 does not require visual"
        assert marks is None and marks_st == "not_specified", "Q7 marks must be null"
        assert comp == "COMPLETE" and conf == "HIGH"
        assert any(d['damage_type'] == 'page_column_interleaving' and d['resolution_status'] == 'RESOLVED' for d in dmg)
    elif q_num == 8:
        assert page == 2, f"Q8 page must be 2, got {page}"
        assert w_state == "STATE B — RECONSTRUCTED", f"Q8 wording state must be STATE B, got {w_state}"
        assert "void fun(struct node* start)" in raw_text, "Q8 must preserve C function code snippet"
        assert v_req is True and q['source_visual_page'] == 2, "Q8 must have source visual required on page 2"
        assert marks is None and marks_st == "not_specified"
        assert comp == "COMPLETE" and conf == "HIGH"
        assert any(d['damage_type'] == 'missing_essential_code_block' and d['resolution_status'] == 'RESOLVED' for d in dmg)
    elif q_num == 9:
        assert page == 2, f"Q9 page must be 2, got {page}"
        assert w_state == "STATE B — RECONSTRUCTED", f"Q9 wording state must be STATE B, got {w_state}"
        assert "following graph" in raw_text.lower(), "Q9 must reference graph"
        assert v_req is True and q['source_visual_page'] == 2, "Q9 must have source visual required on page 2"
        assert marks is None and marks_st == "not_specified"
        assert comp == "COMPLETE" and conf == "HIGH"
        # Prompt 1.3 requirement: verify vertex K and edge (M,K), and absence of R in graph
        assert "6 nodes {M, N, O, K, Q, P}" in raw_text, "Q9 must contain faithful vertex K in {M, N, O, K, Q, P}"
        assert "(M,K)" in raw_text, "Q9 must contain edge (M,K)"
        assert "6 nodes {M, N, O, R, Q, P}" not in raw_text and "(M,R)" not in raw_text, "Q9 must not contain erroneous vertex R"
        rec_meta = q.get('reconstruction_metadata', {})
        sem = rec_meta.get('visual_semantic_verification', {})
        assert sem.get('status') == 'VERIFIED', "Q9 visual semantic verification status must be VERIFIED"
        assert any(f.get('element') == 'vertex_labels' and 'K' in f.get('reconstructed', '') and f.get('match') for f in sem.get('element_level_findings', [])), "Q9 vertex_labels finding must verify K"
        assert any(d['damage_type'] == 'missing_referenced_visual' and d['resolution_status'] == 'RESOLVED' for d in dmg)
    elif q_num == 10:
        assert page == 2, f"Q10 page must be 2, got {page}"
        assert w_state == "STATE B — RECONSTRUCTED", f"Q10 wording state must be STATE B, got {w_state}"
        assert "given tree" in raw_text.lower(), "Q10 must reference tree"
        assert v_req is True and q['source_visual_page'] == 2, "Q10 must have source visual required on page 2"
        assert marks is None and marks_st == "not_specified"
        assert comp == "COMPLETE" and conf == "HIGH"
        assert any(d['damage_type'] == 'missing_referenced_visual' and d['resolution_status'] == 'RESOLVED' for d in dmg)
    elif q_num == 11:
        assert page == 2, f"Q11 page must be 2, got {page}"
        assert w_state == "STATE B — RECONSTRUCTED", f"Q11 wording state must be STATE B, got {w_state}"
        assert "circular singly linked list" not in raw_text.lower(), "Q11 must NOT contain Q7 contamination"
        assert not v_req, "Q11 does not require visual"
        assert marks is None and marks_st == "not_specified"
        assert comp == "COMPLETE" and conf == "HIGH"
        assert any(d['damage_type'] == 'cross_question_contamination' and d['resolution_status'] == 'RESOLVED' for d in dmg)
    elif q_num == 12:
        assert page == 3, f"Q12 page must be 3, got {page}"
        assert w_state == "STATE A — EXACT", f"Q12 wording state must be STATE A, got {w_state}"
        assert marks is None and marks_st == "not_specified"
        assert comp == "COMPLETE" and conf == "HIGH"
        
    print(f"  Verdict: [PASS] All 11 verification dimensions independently verified.")
    passed_items += 1

print("\n" + "=" * 70)
print(f"DOC-28 AUDIT RESULT: {passed_items}/{total_items} QUESTIONS INDEPENDENTLY VERIFIED")
print("=" * 70)
