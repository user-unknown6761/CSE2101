import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

os.makedirs('web/data', exist_ok=True)

# 1. syllabus.json
with open('AUTHORITATIVE_SYLLABUS.json', 'r', encoding='utf-8') as f:
    syllabus = json.load(f)

with open('web/data/syllabus.json', 'w', encoding='utf-8') as f:
    json.dump(syllabus, f, indent=2, ensure_ascii=False)

# 2. topics.json (from PEDAGOGICAL_CONTENT.json)
with open('PEDAGOGICAL_CONTENT.json', 'r', encoding='utf-8') as f:
    topics = json.load(f)

with open('web/data/topics.json', 'w', encoding='utf-8') as f:
    json.dump(topics, f, indent=2, ensure_ascii=False)

# 3. question-families.json
with open('QUESTION_FAMILIES.json', 'r', encoding='utf-8') as f:
    question_families = json.load(f)

if isinstance(question_families, list):
    for f in question_families:
        if "title" not in f and "canonical_title" in f:
            f["title"] = f["canonical_title"]
        if "canonical_family_id" not in f and "family_id" in f:
            f["canonical_family_id"] = f["family_id"]
    families_dict = {f["family_id"]: f for f in question_families}
    fams_export = {
        "total_families": len(question_families),
        "question_families": question_families,
        "families_by_id": families_dict
    }
else:
    fams_export = question_families

with open('web/data/question-families.json', 'w', encoding='utf-8') as f:
    json.dump(fams_export, f, indent=2, ensure_ascii=False)

# 4. solutions.json (indexed as dict for O(1) lookup + list of 780 solutions)
with open('SOLUTIONS_BANK.json', 'r', encoding='utf-8') as f:
    solutions_list = json.load(f)

solutions_dict = {s["question_instance_id"]: s for s in solutions_list}
solutions_export = {
    "total_solutions": len(solutions_list),
    "solutions_list": solutions_list,
    "solutions_by_id": solutions_dict
}

with open('web/data/solutions.json', 'w', encoding='utf-8') as f:
    json.dump(solutions_export, f, indent=2, ensure_ascii=False)

# 5. sources.json
with open('SOURCE_CORPUS_INVENTORY.json', 'r', encoding='utf-8') as f:
    inventory = json.load(f)

with open('SYLLABUS_SCOPE_AUDIT.json', 'r', encoding='utf-8') as f:
    audit = json.load(f)

doc_stats = audit.get("document_breakdown", {})
sources_list = []
for doc in inventory:
    did = doc["document_id"]
    st = doc_stats.get(did, {"in_scope": 0, "out_of_scope": 0, "ambiguous": 0})
    sources_list.append({
        "document_id": did,
        "title": doc.get("title") or doc.get("filename") or did,
        "filename": doc.get("filename", ""),
        "source_type": doc.get("source_type", "EXAM_PAPER"),
        "academic_year": doc.get("academic_year") or doc.get("year") or "Historical",
        "page_count": doc.get("page_count", 0),
        "total_questions": st["in_scope"] + st["out_of_scope"] + st["ambiguous"],
        "in_scope_count": st["in_scope"],
        "out_of_scope_count": st["out_of_scope"],
        "ambiguous_count": st["ambiguous"]
    })

with open('web/data/sources.json', 'w', encoding='utf-8') as f:
    json.dump(sources_list, f, indent=2, ensure_ascii=False)

# 6. questions.json (all 1260 questions with clean text and classification)
with open('RAW_EXTRACTED_QUESTIONS.json', 'r', encoding='utf-8') as f:
    raw_records = json.load(f)

from build_solutions_bank import clean_student_text
from build_phase2_classifier_engine import classify_question_occurrence

all_questions = [r for r in raw_records if r.get('record_type') == 'question_occurrence']
web_questions = []

for q in all_questions:
    scope, tid, reason = classify_question_occurrence(q)
    web_questions.append({
        "question_instance_id": q["question_instance_id"],
        "document_id": q["document_id"],
        "source_file": q["source_file"],
        "page": q["page_start"],
        "official_question_number": q.get("official_question_number", ""),
        "sub_question_id": q.get("sub_question_id", ""),
        "marks": q.get("marks"),
        "marks_source_evidence": q.get("marks_source_evidence", ""),
        "wording_state": q.get("wording_state", "STATE_A"),
        "raw_text": clean_student_text(q["raw_text"]),
        "scope_status": scope,
        "topic_id": tid if scope == "IN_SCOPE" else None,
        "classification_id": tid,
        "classification_reason": reason,
        "has_solution": (scope == "IN_SCOPE")
    })

with open('web/data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(web_questions, f, indent=2, ensure_ascii=False)

# 7. revision.json (High-yield condensed cramming engines)
revision_data = {
    "five_minute_cram": {
        "title": "5-Minute Final Exam Countdown",
        "description": "Essential formulas, triggers, invariants, and zero-mistake rules for the immediate minutes before entering the exam hall.",
        "formulas": [
            {"name": "2D Array Row-Major Address", "formula": "Addr(A[i][j]) = B + w · [ (i - L1) · C + (j - L2) ]"},
            {"name": "2D Array Column-Major Address", "formula": "Addr(A[i][j]) = B + w · [ (j - L2) · R + (i - L1) ]"},
            {"name": "Upper Triangular Matrix Entries", "formula": "Total non-zero entries = n(n + 1) / 2"},
            {"name": "Sparse Triplet Benefit Threshold", "formula": "Beneficial iff 3 · (k + 1) < m · n  (non-zero ratio < 33.3%)"},
            {"name": "Circular Queue Full Condition", "formula": "(rear + 1) % MAX == front"},
            {"name": "Circular Queue Empty Condition", "formula": "front == -1 && rear == -1  (or front == rear)"},
            {"name": "Tower of Hanoi Total Moves", "formula": "Total moves = 2ⁿ - 1  (Recurrence: T(n) = 2T(n-1) + 1, O(2ⁿ))"},
            {"name": "1-Based Heap Array Indices", "formula": "Parent(i) = ⌊i/2⌋, LeftChild(i) = 2i, RightChild(i) = 2i + 1"},
            {"name": "Build-Max-Heap Complexity", "formula": "O(n) linear time  (Proof: ∑_{h=0}^∞ h/2^h = 2)"},
            {"name": "Binary Search Worst Case", "formula": "⌊log2 n⌋ + 1 comparisons = O(log n)"},
            {"name": "Sequential Search Average Comparisons", "formula": "(n + 1) / 2  (or (n + 1) / 3 if item appears twice)"},
            {"name": "Interpolation Search Probe Position", "formula": "pos = low + ⌊((key - A[low]) · (high - low)) / (A[high] - A[low])⌋"}
        ],
        "complexity_table": [
            {"algorithm": "Bubble Sort (Optimized)", "best": "O(n)", "worst": "O(n²)", "avg": "O(n²)", "space": "O(1)", "stable": "Yes"},
            {"algorithm": "Cocktail Shaker Sort", "best": "O(n)", "worst": "O(n²)", "avg": "O(n²)", "space": "O(1)", "stable": "Yes"},
            {"algorithm": "Insertion Sort", "best": "O(n)", "worst": "O(n²)", "avg": "O(n²)", "space": "O(1)", "stable": "Yes"},
            {"algorithm": "Selection Sort", "best": "O(n²)", "worst": "O(n²)", "avg": "O(n²)", "space": "O(1)", "stable": "No"},
            {"algorithm": "Build-Max-Heap", "best": "O(n)", "worst": "O(n)", "avg": "O(n)", "space": "O(1)", "stable": "No"},
            {"algorithm": "Binary Search", "best": "O(1)", "worst": "O(log n)", "avg": "O(log n)", "space": "O(1)", "stable": "N/A"},
            {"algorithm": "Sequential Search", "best": "O(1)", "worst": "O(n)", "avg": "O(n)", "space": "O(1)", "stable": "N/A"},
            {"algorithm": "Interpolation Search", "best": "O(1)", "worst": "O(n)", "avg": "O(log log n)", "space": "O(1)", "stable": "N/A"}
        ],
        "common_traps": [
            "Quick Sort complexity analysis is OUT OF SCOPE — do not write recurrence derivations for it!",
            "In Postfix Evaluation, pop op2 first, then op1. Compute op1 - op2 (NOT op2 - op1).",
            "In Circular Queue, always use modulo arithmetic `(rear + 1) % MAX`. Never do simple `rear++`.",
            "In Singly Linked List reversal, use 3 pointers (prev, curr, next). Save `next = curr->next` before breaking link!",
            "Selection sort always performs exactly n(n-1)/2 comparisons even if the array is already sorted."
        ]
    },
    "fifteen_minute_review": {
        "title": "15-Minute Core Comparisons and Tracing Review",
        "comparisons": [
            {
                "topic": "Linear vs Non-Linear Data Structures",
                "points": [
                    "Elements arranged in sequential order vs hierarchical/interconnected order.",
                    "Single level traversal vs multiple level traversal.",
                    "Memory allocation is straightforward vs complex node allocations.",
                    "Examples: Array, Linked List, Stack, Queue vs Tree, Graph."
                ]
            },
            {
                "topic": "Array vs Linked List",
                "points": [
                    "Static fixed size vs Dynamic runtime resizing.",
                    "O(1) random index access A[i] vs O(n) sequential pointer traversal.",
                    "Costly O(n) element shifting for inserts/deletes vs O(1) pointer updates if node known.",
                    "Zero pointer memory overhead vs extra 4-8 bytes per node for links."
                ]
            },
            {
                "topic": "Recursion vs Iteration",
                "points": [
                    "Repeated self-calls vs repeated execution of loop control structure.",
                    "Consumes O(n) call stack memory vs consumes O(1) auxiliary space.",
                    "Has function call activation record overhead vs fast direct jump instructions.",
                    "Tail recursion can be optimized by compilers to eliminate stack frames."
                ]
            },
            {
                "topic": "Stack vs Queue",
                "points": [
                    "LIFO (Last-In, First-Out) vs FIFO (First-In, First-Out).",
                    "Single access point (Top) vs Two access points (Front for delete, Rear for insert).",
                    "Applications: Infix-to-postfix, parentheses, call stack vs Scheduling, spooling, buffers."
                ]
            }
        ]
    }
}

with open('web/data/revision.json', 'w', encoding='utf-8') as f:
    json.dump(revision_data, f, indent=2, ensure_ascii=False)

print(f"Exported all 7 web data packages to web/data/:")
print(f"  syllabus.json ({len(syllabus['modules'])} modules)")
print(f"  topics.json ({len(topics)} topics)")
print(f"  question-families.json ({len(question_families)} families)")
print(f"  solutions.json ({len(solutions_list)} solutions)")
print(f"  sources.json ({len(sources_list)} documents)")
print(f"  questions.json ({len(web_questions)} questions: {sum(1 for q in web_questions if q['scope_status'] == 'IN_SCOPE')} in-scope)")
print(f"  revision.json (5-min and 15-min cram engines)")
