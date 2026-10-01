import fitz
import re
import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Check all question-bearing files
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

print("Scanning for questions referencing diagrams or code...")
for f in files:
    doc = fitz.open(f)
    fname = os.path.basename(f)
    for p_idx, page in enumerate(doc):
        txt = page.get_text()
        imgs = page.get_images()
        draws = page.get_drawings()
        has_visual = (len(imgs) > 0 or len(draws) > 0)
        
        # Check references
        diag_refs = re.findall(r'.{0,40}(?:following (?:figure|diagram|graph|tree)|shown (?:below|in figure)|given (?:figure|diagram|graph|tree)).{0,40}', txt, re.I)
        if diag_refs and not has_visual:
            print(f"FLAGGED: {fname} P{p_idx+1} references visual element but has NO images/drawings: {diag_refs}")
        elif diag_refs:
            print(f"OK (Visual present): {fname} P{p_idx+1} ({len(imgs)} imgs, {len(draws)} draws): {diag_refs[0].strip()[:60]}")
