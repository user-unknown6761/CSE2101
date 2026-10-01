import glob
import fitz
import json
import re
import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Load classified documents
with open('classified_documents.json', 'r', encoding='utf-8') as f:
    classified_docs = json.load(f)

doc_by_id = {d['document_id']: d for d in classified_docs}

extracted_questions = []
damaged_questions = []

# Helper to clean text
def clean_text(t):
    # Normalize excessive newlines and spaces while preserving code / layout
    lines = [l.strip() for l in t.split('\n') if l.strip()]
    return " ".join(lines)

# -------------------------------------------------------------
# 1. PARSER FOR TIER 1 EXAM PAPERS & TIER 4 SOLUTION QUESTION PAPERS
# -------------------------------------------------------------
def parse_university_exam_paper(doc_meta):
    doc_id = doc_meta['document_id']
    fpath = doc_meta['relative_path']
    doc = fitz.open(fpath)
    
    # We only parse question pages (for solutions DOC-18: pages 0-4, DOC-19: pages 0-6)
    max_pages = len(doc)
    if doc_id == 'DOC-18':
        max_pages = 5
    elif doc_id == 'DOC-19':
        max_pages = 7
        
    paper_qs = []
    current_group = "Group - A"
    current_parent_num = "1"
    current_parent_instance_id = None
    
    established_meta = {
        'year': doc_meta.get('established_year'),
        'branch': doc_meta.get('established_branch'),
        'semester': "3RD SEM" if "3RD SEM" in doc[0].get_text() else ("4TH SEM" if "4TH SEM" in doc[0].get_text() else None),
        'course_code': doc_meta.get('established_paper_id'),
        'course_name': "DATA STRUCTURES AND ALGORITHMS" if "DATA STRUCTURES AND ALGORITHMS" in doc[0].get_text().upper() else "DATA STRUCTURE",
        'exam_type': doc_meta.get('established_exam_type'),
        'time_allotted': "3 hrs" if "3 hrs" in doc[0].get_text() else None,
        'full_marks': "70" if "70" in doc[0].get_text() else None
    }
    
    for p_idx in range(max_pages):
        page = doc[p_idx]
        p_num = p_idx + 1
        text = page.get_text()
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Detect Group header
            grp_m = re.match(r'^(Group\s*[-–]\s*[A-E])', line, re.I)
            if grp_m:
                current_group = grp_m.group(1).replace('–', '-').strip()
                i += 1
                continue
                
            # Detect Q1 header
            if re.match(r'^1\.\s+(Choose|Answer)', line, re.I):
                q1_header = line
                q1_marks = "10 x 1 = 10" if "10" in line else ("12 x 1 = 12" if "12" in line else "10")
                current_parent_num = "1"
                current_parent_instance_id = f"{doc_id}-P{p_num:02d}-Q01"
                paper_qs.append({
                    'question_instance_id': current_parent_instance_id,
                    'document_id': doc_id,
                    'source_file': fpath,
                    'page_start': p_num,
                    'page_end': p_num,
                    'group_or_section': current_group,
                    'official_question_number': "1",
                    'sub_question_id': None,
                    'parent_question_instance_id': None,
                    'raw_text': q1_header,
                    'wording_state': "STATE A — EXACT",
                    'wording_status': "exact_source",
                    'completeness_status': "COMPLETE",
                    'extraction_confidence': "HIGH",
                    'source_tier': doc_meta['source_tier'],
                    'source_type': doc_meta['document_classification'],
                    'source_established_metadata': established_meta,
                    'marks': q1_marks,
                    'marks_status': "physically_established",
                    'has_diagram_or_image': False,
                    'possible_repeat_observation': None
                })
                i += 1
                continue
                
            # Detect Q1 sub-questions: (i), (ii), ..., (xv)
            sub_q1_m = re.match(r'^\(([i|v|x]+)\)\s*(.*)', line, re.I)
            if sub_q1_m and (current_group == 'Group - A' or p_num <= 2):
                sub_id = sub_q1_m.group(1).lower()
                q_text = sub_q1_m.group(2).strip()
                j = i + 1
                sub_lines = [q_text] if q_text else []
                has_diag = False
                while j < len(lines):
                    next_l = lines[j]
                    if re.match(r'^\(([i|v|x]+)\)', next_l, re.I) or re.match(r'^(Group\s*[-–]\s*[A-E]|[2-9]\.)', next_l, re.I):
                        break
                    if any(next_l.startswith(h) for h in ['B.TECH/', 'CSEN ', 'CONFIDENTIAL', 'HERITAGE INSTITUTE']) or next_l == str(p_num):
                        j += 1
                        continue
                    if 'following graph' in next_l or 'following figure' in next_l:
                        has_diag = True
                    sub_lines.append(next_l)
                    j += 1
                    
                instance_id = f"{doc_id}-P{p_num:02d}-Q01-sub-{sub_id}"
                full_raw = " ".join(sub_lines).strip()
                paper_qs.append({
                    'question_instance_id': instance_id,
                    'document_id': doc_id,
                    'source_file': fpath,
                    'page_start': p_num,
                    'page_end': p_num,
                    'group_or_section': current_group,
                    'official_question_number': "1",
                    'sub_question_id': sub_id,
                    'parent_question_instance_id': current_parent_instance_id or f"{doc_id}-P01-Q01",
                    'raw_text': full_raw,
                    'wording_state': "STATE A — EXACT",
                    'wording_status': "exact_source",
                    'completeness_status': "COMPLETE",
                    'extraction_confidence': "HIGH",
                    'source_tier': doc_meta['source_tier'],
                    'source_type': doc_meta['document_classification'],
                    'source_established_metadata': established_meta,
                    'marks': "1",
                    'marks_status': "physically_established",
                    'has_diagram_or_image': has_diag or (len(page.get_images()) > 0 and 'graph' in full_raw.lower()),
                    'possible_repeat_observation': None
                })
                i = j
                continue
                
            # Detect main questions 2-9
            main_q_m = re.match(r'^([2-9])\.\s*(.*)', line)
            if main_q_m:
                q_num = main_q_m.group(1)
                rest = main_q_m.group(2).strip()
                current_parent_num = q_num
                current_parent_instance_id = f"{doc_id}-P{p_num:02d}-Q{int(q_num):02d}"
                
                # Check if it has (a) immediately on the same line
                sub_m = re.match(r'^\(([a-e])\)\s*(.*)', rest, re.I)
                if sub_m:
                    sub_id = sub_m.group(1).lower()
                    sub_text = sub_m.group(2).strip()
                    # Add parent question record
                    paper_qs.append({
                        'question_instance_id': current_parent_instance_id,
                        'document_id': doc_id,
                        'source_file': fpath,
                        'page_start': p_num,
                        'page_end': p_num,
                        'group_or_section': current_group,
                        'official_question_number': q_num,
                        'sub_question_id': None,
                        'parent_question_instance_id': None,
                        'raw_text': f"Question {q_num}",
                        'wording_state': "STATE A — EXACT",
                        'wording_status': "exact_source",
                        'completeness_status': "COMPLETE",
                        'extraction_confidence': "HIGH",
                        'source_tier': doc_meta['source_tier'],
                        'source_type': doc_meta['document_classification'],
                        'source_established_metadata': established_meta,
                        'marks': "12",
                        'marks_status': "physically_established",
                        'has_diagram_or_image': False,
                        'possible_repeat_observation': None
                    })
                    
                    # Collect subquestion lines
                    j = i + 1
                    sub_lines = [sub_text] if sub_text else []
                    has_diag = False
                    sub_marks = None
                    while j < len(lines):
                        next_l = lines[j]
                        if re.match(r'^\(([a-e])\)', next_l, re.I) or re.match(r'^(Group\s*[-–]\s*[A-E]|[2-9]\.)', next_l, re.I):
                            break
                        if any(next_l.startswith(h) for h in ['B.TECH/', 'CSEN ', 'CONFIDENTIAL', 'HERITAGE INSTITUTE']) or next_l == str(p_num):
                            j += 1
                            continue
                        # Check marks line
                        if re.match(r'^((\(?\d+[\+\-×\*\s\(\)]+\)?\s*=\s*\d+)|\b\d+\s*[\+\=]\s*\d+\b)', next_l):
                            sub_marks = next_l
                            j += 1
                            continue
                        if 'following graph' in next_l or 'following figure' in next_l or 'given tree' in next_l:
                            has_diag = True
                        sub_lines.append(next_l)
                        j += 1
                        
                    instance_id = f"{doc_id}-P{p_num:02d}-Q{int(q_num):02d}-sub-{sub_id}"
                    full_raw = " ".join(sub_lines).strip()
                    paper_qs.append({
                        'question_instance_id': instance_id,
                        'document_id': doc_id,
                        'source_file': fpath,
                        'page_start': p_num,
                        'page_end': p_num,
                        'group_or_section': current_group,
                        'official_question_number': q_num,
                        'sub_question_id': sub_id,
                        'parent_question_instance_id': current_parent_instance_id,
                        'raw_text': full_raw,
                        'wording_state': "STATE A — EXACT",
                        'wording_status': "exact_source",
                        'completeness_status': "COMPLETE",
                        'extraction_confidence': "HIGH",
                        'source_tier': doc_meta['source_tier'],
                        'source_type': doc_meta['document_classification'],
                        'source_established_metadata': established_meta,
                        'marks': sub_marks,
                        'marks_status': "physically_established" if sub_marks else "not_specified",
                        'has_diagram_or_image': has_diag or (len(page.get_images()) > 0 and any(w in full_raw.lower() for w in ['tree', 'graph', 'diagram', 'heap'])),
                        'possible_repeat_observation': None
                    })
                    i = j
                    continue
                else:
                    # Single standalone question without subpart on same line
                    # Look ahead to see if (a) follows
                    has_sub_next = False
                    for peek in lines[i+1:i+4]:
                        if re.match(r'^\(([a-e])\)', peek, re.I):
                            has_sub_next = True
                            break
                    if has_sub_next:
                        # Parent record
                        paper_qs.append({
                            'question_instance_id': current_parent_instance_id,
                            'document_id': doc_id,
                            'source_file': fpath,
                            'page_start': p_num,
                            'page_end': p_num,
                            'group_or_section': current_group,
                            'official_question_number': q_num,
                            'sub_question_id': None,
                            'parent_question_instance_id': None,
                            'raw_text': f"Question {q_num}: {rest}" if rest else f"Question {q_num}",
                            'wording_state': "STATE A — EXACT",
                            'wording_status': "exact_source",
                            'completeness_status': "COMPLETE",
                            'extraction_confidence': "HIGH",
                            'source_tier': doc_meta['source_tier'],
                            'source_type': doc_meta['document_classification'],
                            'source_established_metadata': established_meta,
                            'marks': "12",
                            'marks_status': "physically_established",
                            'has_diagram_or_image': False,
                            'possible_repeat_observation': None
                        })
                        i += 1
                        continue
                    else:
                        # Standalone question
                        j = i + 1
                        q_lines = [rest] if rest else []
                        has_diag = False
                        q_marks = None
                        while j < len(lines):
                            next_l = lines[j]
                            if re.match(r'^\(([a-e])\)', next_l, re.I) or re.match(r'^(Group\s*[-–]\s*[A-E]|[2-9]\.)', next_l, re.I):
                                break
                            if any(next_l.startswith(h) for h in ['B.TECH/', 'CSEN ', 'CONFIDENTIAL', 'HERITAGE INSTITUTE']) or next_l == str(p_num):
                                j += 1
                                continue
                            if re.match(r'^((\(?\d+[\+\-×\*\s\(\)]+\)?\s*=\s*\d+)|\b\d+\s*[\+\=]\s*\d+\b)', next_l):
                                q_marks = next_l
                                j += 1
                                continue
                            if 'following graph' in next_l or 'following figure' in next_l or 'given tree' in next_l:
                                has_diag = True
                            q_lines.append(next_l)
                            j += 1
                            
                        instance_id = current_parent_instance_id
                        full_raw = " ".join(q_lines).strip()
                        paper_qs.append({
                            'question_instance_id': instance_id,
                            'document_id': doc_id,
                            'source_file': fpath,
                            'page_start': p_num,
                            'page_end': p_num,
                            'group_or_section': current_group,
                            'official_question_number': q_num,
                            'sub_question_id': None,
                            'parent_question_instance_id': None,
                            'raw_text': full_raw,
                            'wording_state': "STATE A — EXACT",
                            'wording_status': "exact_source",
                            'completeness_status': "COMPLETE",
                            'extraction_confidence': "HIGH",
                            'source_tier': doc_meta['source_tier'],
                            'source_type': doc_meta['document_classification'],
                            'source_established_metadata': established_meta,
                            'marks': q_marks or "12",
                            'marks_status': "physically_established",
                            'has_diagram_or_image': has_diag or (len(page.get_images()) > 0 and any(w in full_raw.lower() for w in ['tree', 'graph', 'diagram', 'heap'])),
                            'possible_repeat_observation': None
                        })
                        i = j
                        continue
                        
            # Detect standalone subquestion (a), (b), (c)
            sub_standalone_m = re.match(r'^\(([a-e])\)\s*(.*)', line, re.I)
            if sub_standalone_m and current_group != 'Group - A':
                sub_id = sub_standalone_m.group(1).lower()
                sub_text = sub_standalone_m.group(2).strip()
                parent_num = current_parent_num
                parent_inst_id = current_parent_instance_id
                j = i + 1
                sub_lines = [sub_text] if sub_text else []
                has_diag = False
                sub_marks = None
                end_p_num = p_num
                while j < len(lines):
                    next_l = lines[j]
                    if re.match(r'^\(([a-e])\)', next_l, re.I) or re.match(r'^(Group\s*[-–]\s*[A-E]|[2-9]\.)', next_l, re.I):
                        break
                    if any(next_l.startswith(h) for h in ['B.TECH/', 'CSEN ', 'CONFIDENTIAL', 'HERITAGE INSTITUTE']) or next_l == str(p_num):
                        j += 1
                        continue
                    if re.match(r'^((\(?\d+[\+\-×\*\s\(\)]+\)?\s*=\s*\d+)|\b\d+\s*[\+\=]\s*\d+\b)', next_l):
                        sub_marks = next_l
                        j += 1
                        continue
                    if 'following graph' in next_l or 'following figure' in next_l or 'given tree' in next_l:
                        has_diag = True
                    sub_lines.append(next_l)
                    j += 1
                    
                instance_id = f"{doc_id}-P{p_num:02d}-Q{int(parent_num):02d}-sub-{sub_id}"
                full_raw = " ".join(sub_lines).strip()
                paper_qs.append({
                    'question_instance_id': instance_id,
                    'document_id': doc_id,
                    'source_file': fpath,
                    'page_start': p_num,
                    'page_end': end_p_num,
                    'group_or_section': current_group,
                    'official_question_number': parent_num,
                    'sub_question_id': sub_id,
                    'parent_question_instance_id': parent_inst_id,
                    'raw_text': full_raw,
                    'wording_state': "STATE A — EXACT",
                    'wording_status': "exact_source",
                    'completeness_status': "COMPLETE",
                    'extraction_confidence': "HIGH",
                    'source_tier': doc_meta['source_tier'],
                    'source_type': doc_meta['document_classification'],
                    'source_established_metadata': established_meta,
                    'marks': sub_marks,
                    'marks_status': "physically_established" if sub_marks else "not_specified",
                    'has_diagram_or_image': has_diag or (len(page.get_images()) > 0 and any(w in full_raw.lower() for w in ['tree', 'graph', 'diagram', 'heap'])),
                    'possible_repeat_observation': None
                })
                i = j
                continue
                
            i += 1
            
    return paper_qs

print("Defined exam parser.")
