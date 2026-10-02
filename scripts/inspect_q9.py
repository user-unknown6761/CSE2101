import fitz

doc = fitz.open('SOURCE/DSA-20260930T180448Z-1-001/DSA/DSA Practice Assignment.pdf')
page = doc[1]

# Let's inspect raw text and fonts in Q9 region
page_dict = page.get_text('dict')
print("All blocks in Q9 region:")
for b_idx, block in enumerate(page_dict['blocks']):
    if 'lines' in block:
        for line in block['lines']:
            for span in line['spans']:
                if 280 <= span['bbox'][1] <= 500:
                    print(f"bbox={span['bbox']}, font={span['font']}, size={span['size']:.1f}, text='{span['text']}'")
    elif 'image' in block:
        print(f"Image block: bbox={block['bbox']}, width={block['width']}, height={block['height']}")

# Let's crop very tightly on the graph: bbox around 150, 320, 400, 450 at 600 DPI
crop_graph = fitz.Rect(120, 320, 350, 450)
pix = page.get_pixmap(dpi=600, clip=crop_graph)
pix.save('rendered_pages/DOC-28_Q9_graph_600dpi.png')
print('Saved rendered_pages/DOC-28_Q9_graph_600dpi.png')
