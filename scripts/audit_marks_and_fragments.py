import json
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('RAW_EXTRACTED_QUESTIONS.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

print(f"Total records in RAW_EXTRACTED_QUESTIONS.json: {len(qs)}")

# 1. Investigate marks
twelve_marks = [q for q in qs if q.get('marks') == '12']
print(f"Records with marks == '12': {len(twelve_marks)}")
for q in twelve_marks[:10]:
    print(f"  [{q['question_instance_id']}] Doc: {q['document_id']}, P{q['page_start']}, Q{q['official_question_number']}: {q.get('raw_text', '')[:60]}")

# 2. Investigate marks-only records or arithmetic text fragments
arithmetic_records = []
very_short_records = []
footer_records = []

for q in qs:
    text = (q.get('raw_text') or '').strip()
    if not text:
        continue
    # Match patterns like: "+ 6 + 3 = 12", "+ (1 + (2 + 2)) = 12", "= 12", "3 + 2 = 5"
    if re.match(r'^\s*[\+\=]', text) or re.search(r'^\s*[\+\(]?\s*\d+[\s\+\-\*\/\(\)]+=\s*\d+\s*$', text):
        arithmetic_records.append(q)
    elif len(text) < 20 and any(c in text for c in ['+', '=', 'CO', 'Marks', 'BL']):
        very_short_records.append(q)
    elif any(term in text.lower() for term in ['course outcome', 'blooms taxonomy', 'page ', 'turn over', 'contd']):
        footer_records.append(q)

print(f"\nArithmetic / Marks-only records ({len(arithmetic_records)}):")
for q in arithmetic_records:
    print(f"  [{q['question_instance_id']}] P{q['page_start']} Q{q['official_question_number']}: {repr(q['raw_text'])}")

print(f"\nVery short / fragment records ({len(very_short_records)}):")
for q in very_short_records:
    print(f"  [{q['question_instance_id']}] P{q['page_start']} Q{q['official_question_number']}: {repr(q['raw_text'])}")

print(f"\nFooter / admin records ({len(footer_records)}):")
for q in footer_records:
    print(f"  [{q['question_instance_id']}] P{q['page_start']} Q{q['official_question_number']}: {repr(q['raw_text'])}")

# Check distinct marks values across the whole corpus
marks_dist = {}
for q in qs:
    m = q.get('marks')
    m_stat = q.get('marks_status')
    key = (m, m_stat)
    marks_dist[key] = marks_dist.get(key, 0) + 1

print("\nMarks distribution (marks, marks_status):")
for k, v in sorted(marks_dist.items(), key=lambda x: str(x[0])):
    print(f"  {k}: {v}")
