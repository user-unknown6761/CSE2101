import glob
import fitz
import os
import json
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Load classified documents to get stable document_ids
with open('classified_documents.json', 'r', encoding='utf-8') as f:
    classified_docs = json.load(f)

doc_map = {d['relative_path']: d for d in classified_docs}

page_quality_records = []

for doc_meta in classified_docs:
    fpath = doc_meta['relative_path']
    doc_id = doc_meta['document_id']
    fname = doc_meta['filename']
    doc = fitz.open(fpath)
    
    for p_idx, page in enumerate(doc):
        p_num = p_idx + 1
        text = page.get_text()
        char_count = len(text.strip())
        imgs = page.get_images()
        draws = page.get_drawings()
        
        # Detect characteristics
        diagram_present = (len(imgs) > 0 or len(draws) > 5)
        table_present = bool(re.search(r'(\+[-+]+\+|\|[\s\w]+\||\bPass\s+\d+\b|\bIndex\s+Item\b)', text, re.I))
        formula_present = bool(re.search(r'(O\s*\(|Θ\s*\(|Ω\s*\(|θ\s*\(|T\(n\)|∑|\^|\b<=|\b>=|2n\+1)', text))
        
        # Check text extraction status
        if char_count > 50:
            extraction_status = "SUCCESS"
            unreadable_area = False
            ocr_needed = False
        elif len(imgs) > 0 and char_count <= 50:
            # Scanned page
            extraction_status = "SCANNED_IMAGE_ONLY"
            unreadable_area = True
            ocr_needed = True
        else:
            extraction_status = "MINIMAL_TEXT"
            unreadable_area = False
            ocr_needed = False
            
        # Question numbering clarity
        has_q_markers = bool(re.search(r'(\bGroup\s*[-–]\s*[A-E]\b|\bQ[\.\s]*\d+|\b\d+\.\s+[A-Z]|\([a-z]\)|\([i|v|x]+\))', text, re.I))
        if doc_meta['content_type'] in ['question-bearing', 'mixed']:
            q_clarity = "HIGH" if has_q_markers else ("MEDIUM" if char_count > 100 else "LOW")
        else:
            q_clarity = "N/A"
            
        visual_inspection_required = (extraction_status != "SUCCESS") or (diagram_present and doc_meta['content_type'] != 'non-question academic material')
        
        confidence = "HIGH"
        if extraction_status == "SCANNED_IMAGE_ONLY":
            confidence = "FLAGGED"
        elif extraction_status == "MINIMAL_TEXT" and doc_meta['content_type'] == 'question-bearing':
            confidence = "MEDIUM"

        page_record = {
            'document_id': doc_id,
            'filename': fname,
            'relative_path': fpath,
            'page_number': p_num,
            'character_count': char_count,
            'text_extraction_status': extraction_status,
            'visual_inspection_required': visual_inspection_required,
            'ocr_used': False,
            'ocr_recommended': ocr_needed,
            'unreadable_area': unreadable_area,
            'raster_images_count': len(imgs),
            'vector_drawings_count': len(draws),
            'diagram_present': diagram_present,
            'table_present': table_present,
            'equation_or_formula_present': formula_present,
            'question_numbering_clarity': q_clarity,
            'confidence': confidence
        }
        page_quality_records.append(page_record)

print(f"Total pages audited: {len(page_quality_records)}")
with open('PAGE_EXTRACTION_QUALITY.json', 'w', encoding='utf-8') as f:
    json.dump(page_quality_records, f, indent=2)

print("Saved to PAGE_EXTRACTION_QUALITY.json")
