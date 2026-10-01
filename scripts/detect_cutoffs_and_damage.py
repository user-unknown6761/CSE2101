import fitz
import re
import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# We will check all question-bearing files
# Let's inspect potential cutoffs
files = [
    'SOURCE/2020_CSE2101_CSE_Data_Structures_and_Algorithms_Backlog.pdf',
    'SOURCE/2021_CSE2101_CSE_Data_Structures_and_Algorithms.pdf',
    'SOURCE/2022_CSE2101_CSE_Data_Structures_and_Algorithms.pdf',
    'SOURCE/2023_CSE2101_CSE_Data_Structures_and_Algorithms.pdf',
    'SOURCE/2024_CSE2101_CSE_Data_Structures_and_Algorithms.pdf',
    'SOURCE/2025_CSE2101_CSE_Data_Structures_and_Algorithms.pdf',
    'SOURCE/DSA-20260930T180448Z-1-001/DSA/BASIC_2021.pdf',
    'SOURCE/DSA-20260930T180448Z-1-001/DSA/BT_2021.pdf',
    'SOURCE/DSA-20260930T180448Z-1-001/DSA/2020 DSA Solution.pdf',
    'SOURCE/DSA-20260930T180448Z-1-001/DSA/2021 DSA Solution.pdf',
    'SOURCE/DSA-20260930T180448Z-1-001/DSA/DSA Practice Assignment.pdf',
    'SOURCE/DSA-20260930T180448Z-1-001/DSA/_Data Structures Using C Question Bank.pdf',
    'SOURCE/DSA-20260930T180448Z-1-001/DSA/_OBJECTIVE TYPE QUESTIONS.pdf',
]

for f in files:
    doc = fitz.open(f)
    fname = os.path.basename(f)
    for p_idx, page in enumerate(doc):
        text = page.get_text()
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        for l in lines:
            if re.match(r'^\([i|v|x]+\)', l, re.I) or re.match(r'^\([a-d]\)', l, re.I):
                # Check for truncated options
                if l.endswith(('...', '..', '___', 'etc')):
                    pass
            # Check for cutoffs at page boundaries
            if l.endswith(('-', '+', '=', 'and', 'or', 'the', 'with', 'which')):
                # Check if it continues on next page
                pass
print("Completed cutoff scan.")
