import json
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('RAW_EXTRACTED_QUESTIONS.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

with open('SUSPICIOUS_EXTRACTION_AUDIT.json', 'r', encoding='utf-8') as f:
    suspicious = json.load(f)

susp_ids = set(s['question_instance_id'] for s in suspicious)

print(f"Total suspicious items: {len(susp_ids)}")

# Let's inspect the text of all 98 items
susp_records = [q for q in qs if q['question_instance_id'] in susp_ids]

for idx, q in enumerate(susp_records, 1):
    text = q.get('raw_text', '')
    is_arith = bool(re.match(r'^\s*[\+\=]', text) or re.search(r'^\s*[\+\(]?\s*\d+[\s\+\-\*\/\(\)\×\=]+\d+\s*$', text))
    is_co = 'course outcome' in text.lower() or 'cognition level' in text.lower() or 'locq' in text.lower()
    print(f"{idx:02d}. [{q['question_instance_id']}] P{q['page_start']} Q{q['official_question_number']} | Arith:{is_arith} | CO:{is_co} | Text: {text[:60]!r}")
