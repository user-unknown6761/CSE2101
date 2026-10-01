import sys
import glob
import os
import json
import fitz

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

nested_files = sorted(glob.glob('SOURCE/DSA-20260930T180448Z-1-001/DSA/*.pdf'))

print(f"Inspecting {len(nested_files)} nested PDFs:")
for p in nested_files:
    fname = os.path.basename(p)
    doc = fitz.open(p)
    page_count = len(doc)
    text_sample = ""
    for i in range(min(page_count, 3)):
        text_sample += f"\n--- Page {i+1} ---\n" + doc[i].get_text()[:400]
    
    print("=" * 60)
    print(f"File: {fname} ({page_count} pages, {os.path.getsize(p)} bytes)")
    print(text_sample[:800])
