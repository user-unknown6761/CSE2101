import fitz

doc = fitz.open('SOURCE/DSA-20260930T180448Z-1-001/DSA/DSA Practice Assignment.pdf')
page2 = doc[1]
for img_info in page2.get_images():
    xref = img_info[0]
    base = doc.extract_image(xref)
    out_name = f"scratch_img_{xref}.{base['ext']}"
    with open(out_name, 'wb') as f:
        f.write(base['image'])
    print(f"Saved {out_name}: {base['width']}x{base['height']}")
