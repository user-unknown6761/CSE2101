import fitz
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('SOURCE/DSA-20260930T180448Z-1-001/DSA/_OBJECTIVE TYPE QUESTIONS.pdf')

full_text = ""
for p in doc:
    full_text += p.get_text() + "\n---PAGE---\n"

# Split into Part I and Part II
parts = re.split(r'PART\s+II\s+DESCRIPTIVES', full_text, flags=re.I)
print(f"Parts found: {len(parts)}")

part1_text = parts[0]
part2_text = parts[1] if len(parts) > 1 else ""

# Check Part I
p1_matches = list(re.finditer(r'Q\.(\d+)\s*(.*?)(?=(?:Q\.\d+|\Z))', part1_text, re.S))
print(f"Part I questions found: {len(p1_matches)}")

# Check Part II
p2_matches = list(re.finditer(r'Q\.(\d+)\s*(.*?)(?=(?:Q\.\d+|\Z))', part2_text, re.S))
print(f"Part II questions found: {len(p2_matches)}")

# Check for incomplete in Part I
p1_incomplete = []
for m in p1_matches:
    q_num = int(m.group(1))
    content = m.group(2).strip()
    if 'Ans:' not in content and 'Ans :' not in content and 'Ans.' not in content:
        p1_incomplete.append((q_num, "Missing Ans marker"))

print(f"Part I without Ans marker: {len(p1_incomplete)}")
for item in p1_incomplete:
    print(" ", item)
