import json
import sys
from extract_all_questions import parse_university_exam_paper

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('classified_documents.json', 'r', encoding='utf-8') as f:
    docs = json.load(f)

tier1_and_sol = [d for d in docs if d['document_id'] in [f'DOC-{i:02d}' for i in range(1, 17)] + ['DOC-18', 'DOC-19', 'DOC-20', 'DOC-21', 'DOC-22', 'DOC-23', 'DOC-25', 'DOC-26']]

total = 0
for d in tier1_and_sol:
    qs = parse_university_exam_paper(d)
    total += len(qs)
    print(f"{d['document_id']}: {d['filename']} -> {len(qs)} question instances")
print(f"Total question instances across 24 papers: {total}")
