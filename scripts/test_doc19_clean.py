import json
import sys
from extract_all_questions import parse_university_exam_paper

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('classified_documents.json', 'r', encoding='utf-8') as f:
    docs = json.load(f)

doc19 = next(d for d in docs if d['document_id'] == 'DOC-19')

# Temporarily test with full page count
qs = parse_university_exam_paper(doc19)
print(f"DOC-19: Extracted {len(qs)} question instances.")
for q in qs[:15]:
    print(f"  P{q['page_start']} Q{q['official_question_number']}({q['sub_question_id'] or '-'}): {q['raw_text'][:60]}")
