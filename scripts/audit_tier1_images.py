import glob
import fitz
import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

tier1_files = [
    'SOURCE/2020_CSE2101_CSE_Data_Structures_and_Algorithms_Backlog.pdf',
    'SOURCE/2021_CSE2101_CSE_Data_Structures_and_Algorithms.pdf',
    'SOURCE/2022_CSE2101_AIML_Data_Structures_and_Algorithms.pdf',
    'SOURCE/2022_CSE2101_CSE_Data_Structures_and_Algorithms.pdf',
    'SOURCE/2022_CSE2101_DS_Data_Structures_and_Algorithms.pdf',
    'SOURCE/2023_CSE2101_AIML_Data_Structures_and_Algorithms.pdf',
    'SOURCE/2023_CSE2101_CSE_Data_Structures_and_Algorithms.pdf',
    'SOURCE/2023_CSE2101_DS_Data_Structures_and_Algorithms.pdf',
    'SOURCE/2023_CSE2101_IOT_Data_Structures_and_Algorithms.pdf',
    'SOURCE/2024_CSE2101_AIML_Data_Structures_and_Algorithms.pdf',
    'SOURCE/2024_CSE2101_CSE_Data_Structures_and_Algorithms.pdf',
    'SOURCE/2024_CSE2101_DS_Data_Structures_and_Algorithms.pdf',
    'SOURCE/2025_CSE2101_AIML_Data_Structures_and_Algorithms.pdf',
    'SOURCE/2025_CSE2101_CSE_Data_Structures_and_Algorithms.pdf',
    'SOURCE/2025_CSE2101_DS_Data_Structures_and_Algorithms.pdf',
    'SOURCE/2025_CSE2101_IOT_Data_Structures_and_Algorithms.pdf',
    'SOURCE/DSA-20260930T180448Z-1-001/DSA/2021.pdf',
    'SOURCE/DSA-20260930T180448Z-1-001/DSA/BACKLOG_2020.pdf',
    'SOURCE/DSA-20260930T180448Z-1-001/DSA/BASIC_2021(1).pdf',
    'SOURCE/DSA-20260930T180448Z-1-001/DSA/BASIC_2021.pdf',
    'SOURCE/DSA-20260930T180448Z-1-001/DSA/BT_2021.pdf',
    'SOURCE/DSA-20260930T180448Z-1-001/DSA/DATA STRUCTURES AND ALGORITHMS CSEN 2101.pdf',
]

for fpath in tier1_files:
    doc = fitz.open(fpath)
    total_imgs = sum(len(page.get_images()) for page in doc)
    total_draws = sum(len(page.get_drawings()) for page in doc)
    fname = os.path.basename(fpath)
    print(f"{fname}: {len(doc)} pages | {total_imgs} images | {total_draws} drawings")
    for p_idx, page in enumerate(doc):
        imgs = len(page.get_images())
        draws = len(page.get_drawings())
        if imgs > 0 or draws > 0:
            print(f"   P{p_idx+1}: {imgs} imgs, {draws} draws")
