import json
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('RAW_EXTRACTED_QUESTIONS.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

# Find records whose text is primarily marks equation or footer
bad_records = []
for q in qs:
    if q.get('record_type') == 'paper_question_container':
        continue
    text = (q.get('raw_text') or '').strip()
    
    # 1. Text starts with +, =, or is primarily arithmetic equation
    # e.g., "+ 6 = 12", "+ (1 + (2 + 2)) = 12", "+ 4 + (2 + 2) = 12"
    m_arith = bool(re.match(r'^\s*[\+\=]', text) or re.match(r'^\s*\(?\d+[\s\+\-\*\/\(\)\×\=]+\d+\s*$', text))
    
    # 2. Text is only marks allocation + optional CO footer
    # e.g., "+ 4 + 2 = 12 Cognition Level LOCQ..."
    m_arith_footer = bool(re.match(r'^\s*[\+\=].*?=\s*\d+', text))
    
    # 3. Text is footer / course outcome / submission link / cognitive level table
    m_pure_footer = bool(re.match(r'^\s*(\d+\s+)?(Course Outcome|Cognition Level|LOCQ|Department & Section|Submission Link)\b', text, re.I))
    
    if m_arith or m_arith_footer or m_pure_footer:
        bad_records.append({
            'id': q['question_instance_id'],
            'doc': q['document_id'],
            'page': q['page_start'],
            'q_num': q['official_question_number'],
            'text': text[:80],
            'full_len': len(text),
            'marks': q.get('marks')
        })

print(f"Total misclassified records found: {len(bad_records)}")
for b in bad_records:
    print(f"[{b['id']}] Doc: {b['doc']} P{b['page']} Q{b['q_num']} (marks: {b['marks']}): {repr(b['text'])}")
