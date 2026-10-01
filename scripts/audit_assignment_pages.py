import fitz
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('SOURCE/DSA-20260930T180448Z-1-001/DSA/DSA Practice Assignment.pdf')
for p_idx, p in enumerate(doc):
    txt = p.get_text()
    # Check if lines look fragmented (e.g. starting with lowercase letters or fragments)
    lines = [l.strip() for l in txt.split('\n') if l.strip()]
    lowercase_starts = [l for l in lines if l[0].islower() and not l.startswith(('(a)', '(b)', '(c)', '(d)', '(i)', '(ii)', 'void', 'int', 'return', 'struct', 'if', 'else', 'for', 'while', 'printf'))]
    print(f"Page {p_idx+1}: {len(lines)} lines, lowercase fragment starts: {len(lowercase_starts)}")
    if lowercase_starts:
        print("   Samples:", lowercase_starts[:3])
