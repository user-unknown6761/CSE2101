import fitz
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('SOURCE/DSA-20260930T180448Z-1-001/DSA/2021 DSA Solution.pdf')
print("Parsing 2021 DSA Solution across all 17 pages...")

qs = []
current_group = "Group - A"
current_q = None

for p_idx, page in enumerate(doc):
    p_num = p_idx + 1
    text = page.get_text()
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    for l in lines:
        if 'Group' in l and any(ch in l for ch in ['A', 'B', 'C', 'D', 'E']):
            current_group = l
        if re.match(r'^\(([i|v|x]+)\)', l, re.I) and p_num <= 4:
            sub = re.match(r'^\(([i|v|x]+)\)', l, re.I).group(1)
            qs.append((p_num, current_group, '1', sub, l[:50]))
        elif re.match(r'^\(([a-e])\)', l, re.I):
            sub = re.match(r'^\(([a-e])\)', l, re.I).group(1)
            qs.append((p_num, current_group, current_q or 'Q', sub, l[:50]))
        elif re.match(r'^([2-9])\.', l):
            current_q = re.match(r'^([2-9])\.', l).group(1)

print(f"Total subparts found in DOC-19: {len(qs)}")
for item in qs[:15]:
    print(" ", item)
