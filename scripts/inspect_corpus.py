import glob
import os
import hashlib
import json
import fitz

def inspect_all():
    files = sorted(glob.glob('SOURCE/**/*.pdf', recursive=True))
    data = []
    
    for fpath in files:
        size = os.path.getsize(fpath)
        with open(fpath, 'rb') as f:
            sha256 = hashlib.sha256(f.read()).hexdigest()
            
        doc = fitz.open(fpath)
        page_count = len(doc)
        
        pages_info = []
        full_text_len = 0
        total_images = 0
        
        for pno in range(page_count):
            page = doc[pno]
            txt = page.get_text()
            txt_len = len(txt)
            full_text_len += txt_len
            imgs = page.get_images()
            total_images += len(imgs)
            pages_info.append({
                'page': pno + 1,
                'char_count': txt_len,
                'word_count': len(txt.split()),
                'image_count': len(imgs),
                'preview': txt[:150].replace('\n', ' ')
            })
            
        header_sample = doc[0].get_text()[:600] if page_count > 0 else ""
        
        data.append({
            'path': fpath.replace('\\', '/'),
            'size': size,
            'sha256': sha256,
            'page_count': page_count,
            'total_char_count': full_text_len,
            'total_images': total_images,
            'header_sample': header_sample,
            'pages_info': pages_info
        })
        
    with open('corpus_inspection_raw.json', 'w', encoding='utf-8') as out:
        json.dump(data, out, indent=2)
        
    print(f"Inspected {len(data)} documents. Saved to corpus_inspection_raw.json")
    for d in data:
        print(f"[{d['page_count']} pgs | {d['total_char_count']} chars] {d['path']}")

if __name__ == '__main__':
    inspect_all()
