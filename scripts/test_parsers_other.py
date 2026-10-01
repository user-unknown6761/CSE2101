import fitz
import re
import sys
import json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Test DOC-30 parser
def test_doc30():
    doc = fitz.open('SOURCE/DSA-20260930T180448Z-1-001/DSA/_Data Structures Using C Question Bank.pdf')
    qs = []
    full_text = ""
    page_map = []
    for p_idx, page in enumerate(doc):
        t = page.get_text()
        page_map.append((len(full_text), len(full_text) + len(t), p_idx + 1))
        full_text += t
        
    matches = list(re.finditer(r'Q(\d+)\.\s*(.*?)(?=\bAns:|\bAns\.|\bQ\d+\.|\Z)', full_text, re.S))
    for m in matches:
        q_num = m.group(1)
        start_char = m.start()
        end_char = m.end()
        # Find page
        p_start = next(p for s, e, p in page_map if s <= start_char < e)
        p_end = next(p for s, e, p in page_map if s < end_char <= e)
        q_text = " ".join([l.strip() for l in m.group(2).split('\n') if l.strip()])
        qs.append({
            'q_num': q_num,
            'p_start': p_start,
            'p_end': p_end,
            'text': q_text
        })
    print(f"DOC-30: Parsed {len(qs)} questions. First: Q{qs[0]['q_num']} on P{qs[0]['p_start']}, Last: Q{qs[-1]['q_num']} on P{qs[-1]['p_start']}")

# Test DOC-31 parser
def test_doc31():
    doc = fitz.open('SOURCE/DSA-20260930T180448Z-1-001/DSA/_OBJECTIVE TYPE QUESTIONS.pdf')
    qs_p1 = []
    qs_p2 = []
    
    # Part 1: pages 0 to 14
    for p_idx in range(15):
        text = doc[p_idx].get_text()
        matches = list(re.finditer(r'Q\.(\d+)\s*(.*?)(?=\bAns|\bQ\.\d+|\Z)', text, re.S))
        for m in matches:
            q_num = m.group(1)
            q_text = " ".join([l.strip() for l in m.group(2).split('\n') if l.strip()])
            qs_p1.append({'q_num': q_num, 'page': p_idx + 1, 'text': q_text})
            
    # Part 2: pages 15 to len(doc)
    full_p2 = ""
    page_map = []
    for p_idx in range(15, len(doc)):
        t = doc[p_idx].get_text()
        page_map.append((len(full_p2), len(full_p2) + len(t), p_idx + 1))
        full_p2 += t
        
    p2_matches = list(re.finditer(r'Q\.(\d+)\s*(.*?)(?=\bAns:|\bAns\.|\bQ\.\d+|\Z)', full_p2, re.S))
    for m in p2_matches:
        q_num = m.group(1)
        start_char = m.start()
        end_char = m.end()
        p_start = next(p for s, e, p in page_map if s <= start_char < e)
        p_end = next(p for s, e, p in page_map if s < end_char <= e)
        q_text = " ".join([l.strip() for l in m.group(2).split('\n') if l.strip()])
        qs_p2.append({'q_num': q_num, 'p_start': p_start, 'p_end': p_end, 'text': q_text})
        
    print(f"DOC-31: Parsed {len(qs_p1)} Part 1 questions and {len(qs_p2)} Part 2 questions.")

test_doc30()
test_doc31()
