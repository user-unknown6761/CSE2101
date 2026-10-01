import fitz
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('SOURCE/DSA-20260930T180448Z-1-001/DSA/2021 DSA Solution.pdf')
print(f"Total pages: {len(doc)}")
for p_idx in range(len(doc)):
    txt = doc[p_idx].get_text()
    lines = [l.strip() for l in txt.split('\n') if l.strip()]
    q_lines = [l for l in lines if l.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '(a)', '(b)', '(c)', '(i)', '(ii)', '(iii)', 'Group', 'Ans'))]
    print(f"Page {p_idx+1}: {len(lines)} lines | markers: {q_lines[:6]}")
