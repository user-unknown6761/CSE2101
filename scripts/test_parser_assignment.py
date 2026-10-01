import fitz
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('SOURCE/DSA-20260930T180448Z-1-001/DSA/DSA Practice Assignment.pdf')
full_text = ""
page_map = []
for p_idx, page in enumerate(doc):
    t = page.get_text()
    page_map.append((len(full_text), len(full_text) + len(t), p_idx + 1))
    full_text += t

# Section 1: Multiple Choice Questions
# Ends at "Short Answer" or "1. Linked lists are not suitable"
s1_match = re.search(r'Multiple Choice Questions\s*(.*?)(?=(?:Short Answer|\b1\.\s+Linked lists))', full_text, re.S)
if s1_match:
    s1_text = s1_match.group(1)
    s1_qs = list(re.finditer(r'(?:^|\n)(\d+)\.\s*(.*?)(?=(?:\n\d+\.|\Z))', s1_text, re.S))
    print(f"Assignment Section 1 (MCQs): {len(s1_qs)} questions found.")

# Section 2: Short Answer
s2_match = re.search(r'(?:Short Answer.*?\n|1\.\s+Linked lists.*?\n)(.*?)(?=(?:Long Answer|Analytical|\b1\.\s+Define Big-Oh))', full_text, re.S)
if s2_match:
    s2_text = s2_match.group(1)
    s2_qs = list(re.finditer(r'(?:^|\n)(\d+)\.\s*(.*?)(?=(?:\n\d+\.|\Z))', s2_text, re.S))
    print(f"Assignment Section 2 (Short Answer): {len(s2_qs)} questions found.")

# Section 3: Long Answer / Analytical
s3_match = re.search(r'(?:Long Answer.*?\n|1\.\s+Define Big-Oh.*?\n)(.*?)$', full_text, re.S)
if s3_match:
    s3_text = s3_match.group(1)
    s3_qs = list(re.finditer(r'(?:^|\n)(\d+)\.\s*(.*?)(?=(?:\n\d+\.|\Z))', s3_text, re.S))
    print(f"Assignment Section 3 (Long Answer): {len(s3_qs)} questions found.")
