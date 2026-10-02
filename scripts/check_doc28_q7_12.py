import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('RAW_EXTRACTED_QUESTIONS.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

doc28_mcq_7_12 = [
    q for q in qs 
    if q.get('document_id') == 'DOC-28' and q.get('group_or_section') == 'Multiple Choice Questions' and q.get('official_question_number') in ['7', '8', '9', '10', '11', '12']
]

for q in doc28_mcq_7_12:
    print("=" * 60)
    print(f"ID: {q['question_instance_id']}")
    print(f"Official Question Number: {q['official_question_number']}")
    print(f"Section: {q['group_or_section']}")
    print(f"Page: {q['page_start']}")
    print(f"Wording State: {q['wording_state']}")
    print(f"Visual Required: {q['source_visual_required']}")
    print(f"Visual Page: {q['source_visual_page']}")
    print(f"Visual Region: {q['source_visual_region']}")
    print(f"Visual Reason: {q['source_visual_reason']}")
    print(f"Reconstruction Metadata: {q['reconstruction_metadata']}")
    print(f"Text:\n{q['raw_text']}")
