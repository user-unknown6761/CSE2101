import json
import re

with open('RAW_EXTRACTED_QUESTIONS.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

fragments = []
for q in qs:
    if q.get('record_type') == 'paper_question_container':
        continue
    text = (q.get('raw_text') or '').strip()
    
    # 1. Marks arithmetic expressions
    is_marks_arith = bool(re.match(r'^\s*[\+\=]', text) or re.search(r'^\s*[\+\(]?\s*\d+[\s\+\-\*\/\(\)]+=\s*\d+', text))
    
    # 2. Course outcome / Bloom's taxonomy / footer
    is_footer = bool(re.search(r'\b(Course Outcome|Cognition Level|LOCQ|HOCQ|IOCQ|Bloom\'s Taxonomy|Submission Link)\b', text, re.I))
    
    # 3. Administrative page text
    is_admin = bool(re.match(r'^\s*(Page \d+|Contd|Turn Over|\d+\s+Course Outcome)\b', text, re.I))
    
    if is_marks_arith or is_footer or is_admin:
        fragments.append({
            'id': q['question_instance_id'],
            'doc': q['document_id'],
            'page': q['page_start'],
            'q_num': q['official_question_number'],
            'text': text[:100],
            'is_marks_arith': is_marks_arith,
            'is_footer': is_footer,
            'is_admin': is_admin
        })

print(f"Total non-question fragments found: {len(fragments)}")
for f in fragments:
    print(f"[{f['id']}] Doc {f['doc']} P{f['page']} Q{f['q_num']}: {f['text']!r} (arith={f['is_marks_arith']}, footer={f['is_footer']}, admin={f['is_admin']})")
