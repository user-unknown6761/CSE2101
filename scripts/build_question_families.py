import json
import re
import sys
from collections import defaultdict, Counter

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Load classified questions and inventory metadata
with open('RAW_EXTRACTED_QUESTIONS.json', 'r', encoding='utf-8') as f:
    raw_records = json.load(f)

all_questions = [r for r in raw_records if r.get('record_type') == 'question_occurrence']
assert len(all_questions) == 1260, f"Expected 1260, got {len(all_questions)}"
with open('SOURCE_CORPUS_INVENTORY.json', 'r', encoding='utf-8') as f:
    inventory = {doc['document_id']: doc for doc in json.load(f)}

from build_phase2_classifier_engine import classify_question_occurrence

in_scope_questions = []

for q in all_questions:
    scope, topic_id, reason = classify_question_occurrence(q)
    if scope == 'IN_SCOPE':
        doc_meta = inventory.get(q['document_id'], {})
        year = doc_meta.get('academic_year') or doc_meta.get('year') or "Unknown"
        in_scope_questions.append({
            "question_instance_id": q["question_instance_id"],
            "document_id": q["document_id"],
            "source_file": q["source_file"],
            "page_start": q["page_start"],
            "official_question_number": q.get("official_question_number", ""),
            "raw_text": q["raw_text"],
            "marks": q.get("marks"),
            "topic_id": topic_id,
            "year": str(year)
        })

print(f"Total in-scope questions: {len(in_scope_questions)}")

# Helper to normalize text for similarity
def normalize_text(text):
    t = text.lower()
    t = re.sub(r'\[.*?\]', '', t) # remove CO codes
    t = re.sub(r'\(.*?\)', '', t) # remove options
    t = re.sub(r'[^a-z0-9\s]', ' ', t)
    tokens = [w for w in t.split() if len(w) > 2 and w not in ['what', 'explain', 'write', 'with', 'using', 'from', 'given', 'show', 'that', 'find', 'which', 'following', 'state', 'calculate', 'prove', 'your', 'answer']]
    return tokens

# Define canonical families taxonomy per topic
FAMILIES_TAXONOMY = {
    "M1_INTRO_NEED": [
        ("M1_FAM_NEED_DEF", "Need and importance of data structures in software and computer science", ["need", "importance", "areas", "applied", "extensively"]),
    ],
    "M1_INTRO_CONCEPTS": [
        ("M1_FAM_ADT_VS_DT", "Abstract Data Type (ADT) vs Concrete Data Type and Data Structure", ["abstract", "adt", "data type", "differ", "variable"]),
        ("M1_FAM_LINEAR_NONLINEAR", "Linear vs Non-Linear and Primitive vs Non-Primitive data structures", ["linear", "nonlinear", "non linear", "primitive"]),
    ],
    "M1_INTRO_ALGO_PROG": [
        ("M1_FAM_ALGO_VS_PROG", "Algorithm vs Program and Characteristics of good algorithms", ["program", "characteristics", "pseudo", "pseudocode", "problem solving"]),
    ],
    "M1_INTRO_EFFICIENCY": [
        ("M1_FAM_TIME_SPACE_COMPLEXITY", "Time and Space complexity concepts, definitions, and frequency count", ["time", "space", "efficiency", "frequency", "relation", "independent"]),
    ],
    "M1_INTRO_ASYMPTOTIC": [
        ("M1_FAM_ASYMPTOTIC_NOTATIONS_DEF", "Formal definitions of Big-O, Big-Omega (Ω), and Big-Theta (Θ) notations", ["define", "big oh", "big omega", "big theta", "notations", "tightly bounded"]),
        ("M1_FAM_ASYMPTOTIC_PROOF", "Mathematical proofs of asymptotic bounds for given functions f(n)", ["prove", "3n2", "48n100", "100", "t n/3", "slowest", "order of growth", "compare"]),
    ],
    "M1_ARRAY_REPRESENTATION": [
        ("M1_FAM_ARRAY_ADDRESS_CALC", "Row-major and Column-major 2D/multidimensional array element address calculation", ["row major", "column major", "address", "base address", "two dimensional", "multidimensional"]),
        ("M1_FAM_SPECIAL_MATRICES", "Upper triangular and Symmetric matrix compact 1D array representations", ["triangular", "symmetric", "multiplication", "syntax"]),
        ("M1_FAM_ARRAY_OPERATIONS", "In-place duplicate removal and array manipulation without extra space", ["remove duplicates", "ordered array", "linear array", "merge two sorted"]),
    ],
    "M1_ARRAY_SPARSE": [
        ("M1_FAM_SPARSE_TRIPLET_REP", "Sparse matrix 3-tuple / triplet representation and memory benefit analysis", ["triplet", "sparse", "beneficial", "order of its corresponding"]),
        ("M1_FAM_SPARSE_TRANSPOSE", "Sparse matrix transpose and fast transpose algorithms", ["transpose", "fast transpose"]),
    ],
    "M1_ARRAY_POLYNOMIAL": [
        ("M1_FAM_ARRAY_POLYNOMIAL_OP", "Array representation of polynomials, addition, and evaluation", ["polynomial", "evaluate", "4x3", "addition using array"]),
    ],
    "M1_LL_SINGLY": [
        ("M1_FAM_SLL_INSERT_DELETE", "Singly linked list: node structure, insertion and deletion operations", ["insert", "delete", "node", "first element", "last element", "pointer to a node x", "sorted list"]),
        ("M1_FAM_SLL_REVERSAL", "In-place reversal of singly linked list (iterative pointer manipulation)", ["reverse", "reversing"]),
        ("M1_FAM_SLL_SEARCH_COUNT", "Search, count nodes, and traversal operations in singly linked list", ["count", "search", "traversal"]),
    ],
    "M1_LL_CIRCULAR": [
        ("M1_FAM_CLL_OPERATIONS", "Circular linked list: structure, insertion, deletion, and comparison with linear linked list", ["circular", "cll", "header"]),
    ],
    "M1_LL_DOUBLY": [
        ("M1_FAM_DLL_OPERATIONS", "Doubly linked list: structure, two-way pointers, insertion, deletion, and trade-offs", ["doubly", "double linked", "dll", "self referential"]),
    ],
    "M1_LL_DOUBLY_CIRCULAR": [
        ("M1_FAM_CDLL_OPERATIONS", "Doubly circular linked list: structure, bidirectional circular pointer updates", ["doubly circular", "circular doubly", "cdll"]),
    ],
    "M1_LL_POLYNOMIAL": [
        ("M1_FAM_LL_POLYNOMIAL_ADD", "Linked list representation and addition of polynomials", ["polynomial", "add two polynomials"]),
    ],
    "M1_LL_APPLICATIONS": [
        ("M1_FAM_LL_VS_ARRAY", "Linked list vs Array comparison, advantages, limitations, and applications", ["advantage", "disadvantage", "limitations", "multilinked", "vs array"]),
    ],
    "M2_STACK_IMPL": [
        ("M2_FAM_STACK_ARRAY_LL", "Stack implementation using array and linked list, overflow and underflow conditions", ["stack using array", "stack using linked list", "overflow", "underflow", "lifo", "top of stack", "top push"]),
        ("M2_FAM_MULTI_STACK_ARRAY", "Two stacks implementation on a single array and memory sharing", ["two stacks", "same array", "queue using stack", "stack using queue"]),
    ],
    "M2_STACK_APPLICATIONS": [
        ("M2_FAM_INFIX_TO_POSTFIX", "Infix to Postfix expression conversion using stack with tabular trace", ["infix to postfix", "convert the following infix", "postfix form", "postfix equivalent", "translate infix"]),
        ("M2_FAM_INFIX_TO_PREFIX", "Infix to Prefix expression conversion using stack", ["infix to prefix", "prefix form", "prefix notation"]),
        ("M2_FAM_POSTFIX_EVAL", "Evaluation of Postfix (Reverse Polish) expression using stack", ["evaluate", "single digit operands", "reverse polish", "arithmetic expression"]),
        ("M2_FAM_PARENTHESIS_MATCH", "Parenthesis matching and balanced bracket checking using stack", ["parenthes", "balanced", "well formed"]),
        ("M2_FAM_STACK_STRING_APP", "Stack applications for string reversal and adjacent duplicate removal", ["adjacent duplicates", "string entered is printed in reverse"]),
    ],
    "M2_QUEUE_LINEAR_CIRCULAR": [
        ("M2_FAM_QUEUE_LINEAR_IMPL", "Linear Queue: array and linked list implementations, front/rear pointers", ["linear queue", "fifo", "enqueue", "dequeue", "queue using array", "queue using linked list"]),
        ("M2_FAM_CIRCULAR_QUEUE_IMPL", "Circular Queue: wrap-around conditions, empty/full formula, array implementation", ["circular queue", "empty queue", "front and rear in each case", "advantages of a circular queue"]),
    ],
    "M2_QUEUE_APPLICATIONS": [
        ("M2_FAM_QUEUE_REAL_WORLD", "Applications of queues: CPU scheduling, spooling, buffer management, priority queues", ["applications of queue", "priority queue", "scheduling", "spooling"]),
    ],
    "M2_DEQUE": [
        ("M2_FAM_DEQUE_OPERATIONS", "Deque: Input-restricted and Output-restricted double-ended queue operations", ["deque", "double ended", "input restricted", "output restricted"]),
    ],
    "M2_REC_PRINCIPLES": [
        ("M2_FAM_REC_CONCEPTS_STACK", "Principles of recursion, activation records, and system call stack usage", ["principles of recursion", "recursion vs iteration", "difference between recursion and iteration", "data structures used to perform recursion"]),
        ("M2_FAM_REC_TRACE_OUTPUT", "Dry-run tracing of recursive functions and return value prediction", ["consider the following code snippet", "predict the output", "fun 5", "recursive sum of digits", "gcd", "ackerman"]),
    ],
    "M2_REC_TAIL": [
        ("M2_FAM_TAIL_RECURSION", "Tail recursion: definition, compiler optimization, and conversion to iteration", ["tail recursion", "tail call", "tail recursive"]),
    ],
    "M2_REC_APPLICATIONS": [
        ("M2_FAM_TOWER_OF_HANOI", "Tower of Hanoi: recursive algorithm, step-by-step move sequence, and recurrence", ["tower", "hanoi", "number of discs", "4 disks"]),
        ("M2_FAM_EIGHT_QUEENS_BACKTRACKING", "Eight Queens Puzzle and Backtracking algorithmic paradigm", ["eight queens", "8 queens", "backtracking"]),
    ],
    "M4_SORT_BUBBLE": [
        ("M4_FAM_BUBBLE_SORT_OPT", "Bubble Sort: algorithm, step-by-step pass trace, and early termination optimization", ["bubble sort", "modified bubble", "optimized bubble", "sorting foundations", "stable sort"]),
    ],
    "M4_SORT_COCKTAIL": [
        ("M4_FAM_COCKTAIL_SHAKER", "Cocktail Shaker Sort (Bidirectional Bubble Sort): mechanism and pass trace", ["cocktail", "shaker"]),
    ],
    "M4_SORT_INSERTION": [
        ("M4_FAM_INSERTION_SORT_ANALYSIS", "Insertion Sort: algorithm, pass trace, and Best/Worst/Average case complexity analysis", ["insertion sort", "best if the list is already sorted"]),
    ],
    "M4_SORT_SELECTION": [
        ("M4_FAM_SELECTION_SORT_TRACE", "Selection Sort: algorithm, minimum element selection, and pass-by-pass trace", ["selection sort", "smallest element in the array", "sort 20"]),
    ],
    "M4_SORT_HEAPIFY": [
        ("M4_FAM_BUILD_MAX_HEAP_TRACE", "Build-Max-Heap: step-by-step construction from an array and heap property", ["build max heap", "construct a max heap", "create a heap", "elements 32", "resultant max heap"]),
        ("M4_FAM_MAX_HEAPIFY_ALGO", "Max-Heapify procedure, parent/child index calculation in array (2i, 2i+1, i/2)", ["max heapify", "left child", "right child", "index of", "heap size", "exchange a"]),
        ("M4_FAM_HEAP_COMPLEXITY_PROOF", "Build-Max-Heap O(n) linear-time mathematical derivation and summation proof", ["justify that a max heap can be generated in o n", "time complexity of building a max heap", "turned into a heap", "summation"]),
        ("M4_FAM_HEAP_PROPERTIES", "Heap properties: root element, complete binary tree structure, max vs min heap", ["true regarding a max heap", "identical", "can a binary search tree be called a max heap", "exact height"]),
    ],
    "M4_SORT_QUICK": [
        ("M4_FAM_QUICK_SORT_ALGO", "Quick Sort: Partitioning algorithms (Lomuto / Hoare), pivot selection, and dry run", ["quick sort", "quicksort", "partition", "pivot", "what are partitions"]),
    ],
    "M4_SEARCH_SEQUENTIAL": [
        ("M4_FAM_SEQUENTIAL_SEARCH", "Sequential Search (Linear Search): algorithm, sentinel, and average-case comparison analysis", ["sequential search", "linear search", "sentinel", "expected number of comparisons", "uniformly distributed", "second largest"]),
    ],
    "M4_SEARCH_BINARY": [
        ("M4_FAM_BINARY_SEARCH_ANALYSIS", "Binary Search: algorithm, mid element calculation, and Best/Worst/Average case complexity", ["binary search", "middle element among n elements"]),
    ],
    "M4_SEARCH_INTERPOLATION": [
        ("M4_FAM_INTERPOLATION_SEARCH", "Interpolation Search: probe position calculation formula, uniform distribution requirement, and performance", ["interpolation search", "probe"]),
    ]
}

# Assign each in-scope question to a family
family_members = defaultdict(list)
assigned_count = 0

for q in in_scope_questions:
    tid = q["topic_id"]
    text = q["raw_text"].lower()
    norm_tokens = set(normalize_text(q["raw_text"]))
    
    cand_families = FAMILIES_TAXONOMY.get(tid, [])
    best_fam_id = None
    best_score = -1
    
    for fid, ftitle, keywords in cand_families:
        score = sum(1 for kw in keywords if kw in text or any(k in norm_tokens for k in kw.split()))
        if score > best_score:
            best_score = score
            best_fam_id = fid
            
    if best_fam_id is None or best_score == 0:
        # Default to first family of the topic
        best_fam_id = cand_families[0][0] if cand_families else f"{tid}_FAM_GENERIC"
        
    family_members[best_fam_id].append(q)
    assigned_count += 1

print(f"Assigned {assigned_count} questions across {len(family_members)} question families.")

# Build canonical question families dataset
families_dataset = []

# Map of family ID to details
fam_details = {}
for tid, flist in FAMILIES_TAXONOMY.items():
    for fid, ftitle, kw in flist:
        fam_details[fid] = {"title": ftitle, "topic_id": tid}

for fid, members in family_members.items():
    details = fam_details.get(fid, {"title": fid.replace('_', ' ').title(), "topic_id": members[0]["topic_id"]})
    
    # Sort members by document and question ID
    members_sorted = sorted(members, key=lambda x: (x["document_id"], x["question_instance_id"]))
    
    # Choose a high-quality representative question occurrence
    # Prefer complete, clear questions from early exams with good marks
    rep = members_sorted[0]
    for m in members_sorted:
        if len(m["raw_text"]) > len(rep["raw_text"]) and len(m["raw_text"]) < 400:
            rep = m
            
    # Calculate recurrence intelligence
    distinct_years = sorted(list(set(m["year"] for m in members_sorted if m["year"] != "Unknown")))
    distinct_docs = sorted(list(set(m["document_id"] for m in members_sorted)))
    
    # Determine member variants relative to representative
    rep_text_norm = set(normalize_text(rep["raw_text"]))
    member_records = []
    
    for m in members_sorted:
        m_text_norm = set(normalize_text(m["raw_text"]))
        # Variant classification
        if m["question_instance_id"] == rep["question_instance_id"]:
            var_type = "REPRESENTATIVE_ORIGIN"
        elif m["raw_text"].strip() == rep["raw_text"].strip():
            var_type = "EXACT_OR_NEAR_DUPLICATE"
        else:
            jaccard = len(rep_text_norm & m_text_norm) / max(1, len(rep_text_norm | m_text_norm))
            # Check for numerical differences
            nums_rep = re.findall(r'\d+', rep["raw_text"])
            nums_m = re.findall(r'\d+', m["raw_text"])
            if nums_rep != nums_m and len(nums_rep) > 0 and len(nums_m) > 0 and jaccard > 0.4:
                var_type = "NUMERICAL_VARIANT"
            elif jaccard > 0.6:
                var_type = "WORDING_VARIANT"
            elif re.search(r'(c\s+code|program|pseudocode|algorithm)', m["raw_text"].lower()) != re.search(r'(c\s+code|program|pseudocode|algorithm)', rep["raw_text"].lower()):
                var_type = "METHOD_VARIANT"
            elif jaccard > 0.35:
                var_type = "STRUCTURAL_VARIANT"
            else:
                var_type = "RELATED_BUT_DISTINCT"
                
        member_records.append({
            "question_instance_id": m["question_instance_id"],
            "document_id": m["document_id"],
            "source_file": m["source_file"],
            "page_start": m["page_start"],
            "official_question_number": m["official_question_number"],
            "marks": m["marks"],
            "variant_type": var_type,
            "raw_text": m["raw_text"]
        })
        
    families_dataset.append({
        "family_id": fid,
        "canonical_title": details["title"],
        "topic_id": details["topic_id"],
        "representative_question_instance_id": rep["question_instance_id"],
        "representative_text": rep["raw_text"],
        "representative_document_id": rep["document_id"],
        "representative_source_file": rep["source_file"],
        "representative_page": rep["page_start"],
        "occurrence_count": len(members),
        "distinct_papers_count": len(distinct_docs),
        "distinct_papers": distinct_docs,
        "distinct_years": distinct_years,
        "observed_recurrence_tier": "HIGH_RECURRENCE" if len(distinct_docs) >= 5 else ("MODERATE_RECURRENCE" if len(distinct_docs) >= 2 else "SPORADIC_OCCURRENCE"),
        "recurrence_label": f"Observed historical source occurrence across {len(distinct_docs)} distinct papers",
        "members": member_records
    })

# Sort families by occurrence count descending
families_dataset.sort(key=lambda x: -x["occurrence_count"])

with open('QUESTION_FAMILIES.json', 'w', encoding='utf-8') as f:
    json.dump(families_dataset, f, indent=2, ensure_ascii=False)

print(f"Generated QUESTION_FAMILIES.json with {len(families_dataset)} families.")

# Build QUESTION_FAMILIES.md
qf_md = [
    "# CSE2101 / CSEN2101 Canonical Question Families",
    "## Source-Grounded Clustering & Historical Recurrence Intelligence",
    "",
    "> [!NOTE]",
    "> Every question family uses an authentic source occurrence as its representative. Zero synthetic questions have been created. Recurrence metrics reflect observed historical paper appearances.",
    "",
    "| Family ID | Canonical Concept Title | Topic ID | Historical Occurrences | Papers | Observed Frequency Tier |",
    "| :--- | :--- | :--- | :--- | :--- | :--- |"
]

for fam in families_dataset:
    qf_md.append(f"| `{fam['family_id']}` | **{fam['canonical_title']}** | `{fam['topic_id']}` | {fam['occurrence_count']} | {fam['distinct_papers_count']} | `{fam['observed_recurrence_tier']}` |")

qf_md.extend([
    "",
    "---",
    "",
    "## Detailed Question Family Specifications",
    ""
])

for fam in families_dataset:
    qf_md.append(f"### {fam['canonical_title']} (`{fam['family_id']}`)")
    qf_md.append(f"- **Topic**: `{fam['topic_id']}`")
    qf_md.append(f"- **Historical Frequency**: {fam['occurrence_count']} occurrences across {fam['distinct_papers_count']} papers ({fam['observed_recurrence_tier']})")
    qf_md.append(f"- **Representative Question** (`{fam['representative_question_instance_id']}` from `{fam['representative_document_id']}` Page {fam['representative_page']}):")
    qf_md.append(f"  > *\"{fam['representative_text']}\"*")
    qf_md.append(f"- **Member Question Occurrences ({len(fam['members'])})**:")
    for m in fam['members'][:10]:
        qf_md.append(f"  - [`{m['question_instance_id']}`] ({m['variant_type']}) - *\"{m['raw_text'][:100]}...\"*")
    if len(fam['members']) > 10:
        qf_md.append(f"  - *(... and {len(fam['members']) - 10} additional source occurrences)*")
    qf_md.append("")

with open('QUESTION_FAMILIES.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(qf_md))

print("Generated QUESTION_FAMILIES.md")
