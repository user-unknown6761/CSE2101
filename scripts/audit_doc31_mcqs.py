import fitz
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('SOURCE/DSA-20260930T180448Z-1-001/DSA/_OBJECTIVE TYPE QUESTIONS.pdf')

full_text = ""
for p in doc[:16]:
    full_text += p.get_text() + "\n"

matches = list(re.finditer(r'Q\.(\d+)\s*(.*?)(?=(?:Q\.\d+|\Z))', full_text, re.S))
print(f"Total MCQs parsed: {len(matches)}")

incomplete_mcqs = []
for m in matches:
    q_num = int(m.group(1))
    body = m.group(2)
    has_a = bool(re.search(r'\(A\)', body, re.I))
    has_b = bool(re.search(r'\(B\)', body, re.I))
    has_c = bool(re.search(r'\(C\)', body, re.I))
    has_d = bool(re.search(r'\(D\)', body, re.I))
    has_ans = bool(re.search(r'Ans\s*:', body, re.I))
    
    if not (has_a and has_b and has_c and has_d):
        incomplete_mcqs.append((q_num, f"Options: A={has_a}, B={has_b}, C={has_c}, D={has_d}"))
    if not has_ans:
        incomplete_mcqs.append((q_num, "Missing Ans"))

print(f"MCQs with missing options or answers: {len(incomplete_mcqs)}")
for item in incomplete_mcqs:
    print(" ", item)
