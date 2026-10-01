import json

with open('classified_documents.json', encoding='utf-8') as f:
    docs = json.load(f)

for d in docs:
    y = d['established_year'] or 'Unknown'
    b = d['established_branch'] or 'Unknown'
    p = d['established_paper_id'] or 'Unknown'
    e = d['established_exam_type'] or 'Unknown'
    print(f"[{d['document_id']}] Tier {d['source_tier']} | {d['document_classification']:35s} | Year: {str(y):4s} | Br: {b:20s} | Code: {p:10s} | {d['filename']}")
