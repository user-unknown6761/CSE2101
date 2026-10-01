import fitz
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('SOURCE/DSA-20260930T180448Z-1-001/DSA/_Data Structures Using C Question Bank.pdf')

full_text = ""
page_offsets = []
for p_idx, page in enumerate(doc):
    t = page.get_text()
    page_offsets.append((len(full_text), len(full_text) + len(t), p_idx + 1))
    full_text += t

# Find all Q<number>.
matches = list(re.finditer(r'Q(\d+)\.\s*(.*?)(?=(?:Q\d+\.|\Z))', full_text, re.S))
print(f"Total question blocks found in DOC-30: {len(matches)}")

incomplete_list = []
for m in matches:
    q_num = int(m.group(1))
    content = m.group(2).strip()
    
    # Check if question statement or answer is cut off
    lines = [l.strip() for l in content.split('\n') if l.strip()]
    if not lines:
        incomplete_list.append((q_num, "Empty question block"))
    elif len(lines) == 1 and not lines[0].endswith(('?', '.')):
        incomplete_list.append((q_num, f"Single short line without punctuation: {lines[0]}"))

print(f"Potential incomplete questions in DOC-30: {len(incomplete_list)}")
for item in incomplete_list:
    print(" ", item)
