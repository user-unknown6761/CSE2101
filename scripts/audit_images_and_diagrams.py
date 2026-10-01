import fitz
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('SOURCE/DSA-20260930T180448Z-1-001/DSA/DSA Practice Assignment.pdf')
print(f"Total pages: {len(doc)}")
for p_idx, page in enumerate(doc):
    imgs = page.get_images()
    drawings = page.get_drawings()
    if imgs or drawings:
        print(f"Page {p_idx+1}: {len(imgs)} raster images, {len(drawings)} vector drawing paths")
        for img in imgs:
            xref = img[0]
            base = doc.extract_image(xref)
            print(f"   xref {xref}: format {base['ext']}, size {base['width']}x{base['height']}")
