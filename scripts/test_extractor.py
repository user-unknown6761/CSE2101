import fitz
import re
import sys
import os

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def parse_exam_paper(fpath):
    doc = fitz.open(fpath)
    pages_text = [doc[p].get_text() for p in range(len(doc))]
    
    # We want to extract question occurrences
    # Let's inspect page by page
    questions = []
    current_group = None
    
    for p_idx, text in enumerate(pages_text):
        p_num = p_idx + 1
        lines = text.split('\n')
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Check group
            grp_m = re.match(r'^(Group\s*[-–]\s*[A-E])', line, re.I)
            if grp_m:
                current_group = grp_m.group(1).replace('–', '-').strip()
                i += 1
                continue
                
            # Check Q1 start
            if re.match(r'^1\.\s+(Choose|Answer)', line, re.I):
                q1_header = line
                # Q1 is a parent question
                questions.append({
                    'type': 'PARENT_QUESTION',
                    'q_num': '1',
                    'sub_id': None,
                    'group': current_group or 'Group - A',
                    'page': p_num,
                    'text': q1_header,
                    'marks': '10' if '10' in line else ('12' if '12' in line else None)
                })
                i += 1
                continue
                
            # Check sub-question of Q1: (i), (ii), etc.
            sub_q1_m = re.match(r'^\(([i|v|x]+)\)\s*(.*)', line, re.I)
            if sub_q1_m and (current_group == 'Group - A' or p_num <= 2):
                sub_id = sub_q1_m.group(1).lower()
                q_text = sub_q1_m.group(2)
                # Collect following lines until next sub-q or group or next question
                j = i + 1
                sub_lines = [q_text] if q_text else []
                while j < len(lines):
                    next_l = lines[j].strip()
                    if re.match(r'^\(([i|v|x]+)\)', next_l, re.I) or re.match(r'^(Group\s*[-–]\s*[A-E]|[2-9]\.)', next_l, re.I):
                        break
                    # Also stop if page footer
                    if 'B.TECH/' in next_l or 'CSEN ' in next_l or next_l == str(p_num):
                        j += 1
                        continue
                    sub_lines.append(next_l)
                    j += 1
                questions.append({
                    'type': 'SUB_QUESTION',
                    'q_num': '1',
                    'sub_id': sub_id,
                    'parent': '1',
                    'group': 'Group - A',
                    'page': p_num,
                    'text': " ".join(sub_lines).strip(),
                    'marks': '1'
                })
                i = j
                continue
                
            # Check main question 2-9
            main_q_m = re.match(r'^([2-9])\.\s*(.*)', line)
            if main_q_m:
                q_num = main_q_m.group(1)
                rest = main_q_m.group(2).strip()
                
                # Check if it has (a) immediately on the same line
                sub_m = re.match(r'^\(([a-e])\)\s*(.*)', rest, re.I)
                if sub_m:
                    # Parent question
                    questions.append({
                        'type': 'PARENT_QUESTION',
                        'q_num': q_num,
                        'sub_id': None,
                        'group': current_group,
                        'page': p_num,
                        'text': f"Question {q_num}",
                        'marks': None
                    })
                    sub_id = sub_m.group(1).lower()
                    sub_text = sub_m.group(2).strip()
                    # Collect lines until next sub or next question
                    j = i + 1
                    sub_lines = [sub_text] if sub_text else []
                    while j < len(lines):
                        next_l = lines[j].strip()
                        if re.match(r'^\(([a-e])\)', next_l, re.I) or re.match(r'^(Group\s*[-–]\s*[A-E]|[2-9]\.)', next_l, re.I):
                            break
                        if 'B.TECH/' in next_l or 'CSEN ' in next_l or next_l == str(p_num):
                            j += 1
                            continue
                        sub_lines.append(next_l)
                        j += 1
                    questions.append({
                        'type': 'SUB_QUESTION',
                        'q_num': q_num,
                        'sub_id': sub_id,
                        'parent': q_num,
                        'group': current_group,
                        'page': p_num,
                        'text': " ".join(sub_lines).strip(),
                        'marks': None
                    })
                    i = j
                    continue
                else:
                    # Single standalone question or parent
                    j = i + 1
                    q_lines = [rest] if rest else []
                    while j < len(lines):
                        next_l = lines[j].strip()
                        if re.match(r'^\(([a-e])\)', next_l, re.I) or re.match(r'^(Group\s*[-–]\s*[A-E]|[2-9]\.)', next_l, re.I):
                            break
                        if 'B.TECH/' in next_l or 'CSEN ' in next_l or next_l == str(p_num):
                            j += 1
                            continue
                        q_lines.append(next_l)
                        j += 1
                    questions.append({
                        'type': 'QUESTION',
                        'q_num': q_num,
                        'sub_id': None,
                        'group': current_group,
                        'page': p_num,
                        'text': " ".join(q_lines).strip(),
                        'marks': None
                    })
                    i = j
                    continue
                    
            # Check standalone subquestion (a), (b), (c)
            sub_standalone_m = re.match(r'^\(([a-e])\)\s*(.*)', line, re.I)
            if sub_standalone_m and current_group != 'Group - A':
                sub_id = sub_standalone_m.group(1).lower()
                sub_text = sub_standalone_m.group(2).strip()
                last_main_q = [q['q_num'] for q in questions if q['q_num'] != '1']
                parent_num = last_main_q[-1] if last_main_q else 'UNKNOWN'
                j = i + 1
                sub_lines = [sub_text] if sub_text else []
                while j < len(lines):
                    next_l = lines[j].strip()
                    if re.match(r'^\(([a-e])\)', next_l, re.I) or re.match(r'^(Group\s*[-–]\s*[A-E]|[2-9]\.)', next_l, re.I):
                        break
                    if 'B.TECH/' in next_l or 'CSEN ' in next_l or next_l == str(p_num):
                        j += 1
                        continue
                    sub_lines.append(next_l)
                    j += 1
                questions.append({
                    'type': 'SUB_QUESTION',
                    'q_num': parent_num,
                    'sub_id': sub_id,
                    'parent': parent_num,
                    'group': current_group,
                    'page': p_num,
                    'text': " ".join(sub_lines).strip(),
                    'marks': None
                })
                i = j
                continue
                
            i += 1
            
    return questions

sample_res = parse_exam_paper('SOURCE/2020_CSE2101_CSE_Data_Structures_and_Algorithms_Backlog.pdf')
print(f"Extracted {len(sample_res)} items from 2020 Backlog:")
for q in sample_res[:15]:
    print(f"  P{q['page']} Q{q['q_num']}({q['sub_id'] or '-'}): {q['text'][:60]}")
