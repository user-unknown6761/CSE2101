import sys
import fitz

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

papers = [
    'SOURCE/2020_CSE2101_CSE_Data_Structures_and_Algorithms_Backlog.pdf',
    'SOURCE/2021_CSE2101_CSE_Data_Structures_and_Algorithms.pdf',
    'SOURCE/2022_CSE2101_CSE_Data_Structures_and_Algorithms.pdf',
    'SOURCE/2023_CSE2101_CSE_Data_Structures_and_Algorithms.pdf',
    'SOURCE/2024_CSE2101_CSE_Data_Structures_and_Algorithms.pdf',
    'SOURCE/2025_CSE2101_CSE_Data_Structures_and_Algorithms.pdf',
]

for p in papers:
    print("=" * 70)
    print(f"FILE: {p}")
    doc = fitz.open(p)
    for pno in range(len(doc)):
        print(f"--- PAGE {pno+1} ---")
        lines = [line.strip() for line in doc[pno].get_text().split('\n') if line.strip()]
        for l in lines[:25]:
            print("  ", l)
