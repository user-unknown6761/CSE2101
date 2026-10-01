import json

with open('corpus_inspection_raw.json', encoding='utf-8') as f:
    docs = json.load(f)

tot_pages = sum(d['page_count'] for d in docs)
tot_chars = sum(d['total_char_count'] for d in docs)

print(f"Total Documents: {len(docs)}")
print(f"Total Pages across all 33 PDFs: {tot_pages}")
print(f"Total Characters: {tot_chars}")

print("\n=== DETAILED DOCUMENT PROFILES ===")
for d in docs:
    p = d['path']
    snippet = d['header_sample'].replace('\n', ' ')[:140]
    print(f"{d['page_count']:3d} pgs | {d['total_char_count']:6d} chars | {p}")
    print(f"   Snippet: {snippet}")
