import fitz
import re
import sys
import os
import glob

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

all_pdfs = sorted(glob.glob('SOURCE/**/*.pdf', recursive=True))

missing_diag_candidates = []

for f in all_pdfs:
    doc = fitz.open(f)
    fname = os.path.basename(f)
    for p_idx, page in enumerate(doc):
        text = page.get_text()
        imgs = page.get_images()
        draws = page.get_drawings()
        
        # Check if text references a figure or diagram or graph
        fig_refs = re.findall(r'.{0,30}(?:following (?:graph|tree|figure|diagram)|shown (?:below|in figure)|given (?:graph|tree|figure|diagram)).{0,30}', text, re.I)
        if fig_refs and len(imgs) == 0 and len(draws) == 0:
            missing_diag_candidates.append({
                'file': fname,
                'page': p_idx + 1,
                'refs': [r.strip().replace('\n', ' ') for r in fig_refs]
            })

print(f"Total pages across entire corpus referencing visual element with 0 images and 0 drawings: {len(missing_diag_candidates)}")
for c in missing_diag_candidates:
    print(f"  {c['file']} Page {c['page']}: {c['refs']}")
