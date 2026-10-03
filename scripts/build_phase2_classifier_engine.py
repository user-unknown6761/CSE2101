import json
import re
import sys
from collections import defaultdict, Counter

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('RAW_EXTRACTED_QUESTIONS.json', 'r', encoding='utf-8') as f:
    records = json.load(f)

containers = {r['question_instance_id']: r for r in records if r.get('record_type') == 'paper_question_container'}
questions = [r for r in records if r.get('record_type') == 'question_occurrence']

container_questions = defaultdict(list)
for q in questions:
    pid = q.get('parent_question_container_id')
    if pid:
        container_questions[pid].append(q)

def classify_question_occurrence(q):
    raw_text = q['raw_text']
    text_clean = raw_text.lower().replace('’', "'").replace('‘', "'")
    
    pid = q.get('parent_question_container_id')
    parent_text = ""
    sibling_context = ""
    if pid and pid in containers:
        parent_text = (containers[pid].get('raw_text') or containers[pid].get('container_title') or "")
    
    if pid and pid in container_questions:
        sibs = container_questions[pid]
        for s in sibs:
            if s['question_instance_id'] == q['question_instance_id']:
                break
            s_raw = s['raw_text']
            if any(term in s_raw.lower() for term in ['linked list', 'singly', 'doubly', 'stack', 'queue', 'deque', 'sparse', 'array', 'tree', 'graph', 'heap', 'hanoi', 'discs', 'tower', 'selection sort']):
                sibling_context += " " + s_raw

    context_full = f"{parent_text} {sibling_context} {raw_text}".lower().replace('’', "'").replace('‘', "'")

    # Handle isolated single-token / genuinely unanswerable fragments that were classified as question_occurrence in raw extraction
    if text_clean.strip() in ['else', 'then', 'end', 'begin'] or len(text_clean.strip()) <= 4:
        return ("AMBIGUOUS", "AMBIGUOUS_INSUFFICIENT_ISOLATED_TOKEN", "Isolated token ('" + raw_text.strip() + "') lacking sufficient grammatical or semantic context to form an answerable question.")

    # --------------------------------------------------------------------------
    # 1. SPECIFIC OUT-OF-SCOPE CHECKS
    # --------------------------------------------------------------------------
    # Quick Sort Complexity Analysis
    if re.search(r'quick\s*sort', text_clean):
        if re.search(r'(worst\s*case\s*time\s*complexity\s*of\s*quick\s*sort.*recurrence|recurrence\s*relation.*quick\s*sort|derive.*complexity.*quick\s*sort|best.*worst.*average.*complexity.*quick\s*sort|analyze.*complexity.*quick\s*sort|derive.*worst\s*case.*time\s*complexity)', text_clean):
            return ("OUT_OF_SCOPE", "OOS_M4_QUICK_SORT_COMPLEXITY", "Quick Sort complexity analysis is explicitly excluded by the locked syllabus.")

    # Module 3 Trees
    is_tree_term = re.search(r'\b(binary\s+search\s+tree|bst\b|avl\b|avl\s+tree|b-tree|b\+\s*tree|b\s+trees|red\s*black|threaded\s+binary|tree\s+traversal|traversal\s+of\s+a\s+rooted\s+tree|traversal\s+of\s+the\s+given\s+tree|post\s*order|pre\s*order|in\s*order|in-?order|pre-?order|post-?order|huffman|trie|strictly\s+binary\s+tree|complete\s+binary\s+tree|extended\s+binary\s+tree|expression\s+tree|directed\s+trees|m-way\s+search\s+tree|forest|leaf\s+node\s+in\s+a\s+tree|nodes\s+in\s+a\s+tree|binary\s+tree|binary\s+trees|tree\s+data-?\s*structure|tree\s+construction|tree\s+having|ancestors.*tree|complete\s+trees)\b', text_clean)
    if is_tree_term:
        if "max-heap" in text_clean and "binary search tree be called a max-heap" in text_clean:
            return ("IN_SCOPE", "M4_SORT_HEAPIFY", "Comparison of Max-Heap property with binary search tree properties")
        return ("OUT_OF_SCOPE", "OOS_MODULE_3_TREE", "Topic belongs to Module 3 (Trees / BST / AVL / B-Tree), which is strictly out of scope.")

    # Module 3 Graphs
    if re.search(r'\b(graph|graphs|bfs\b|dfs\b|breadth\s+first|depth\s+first|dijkstra|prim|kruskal|kruskals|spanning\s+tree|spanning\s+trees|topological\s+sort|adjacency\s+matrix|adjacency\s+list|floyd|warshall|shortest\s+path|undirected\s+graph|directed\s+graph|connected\s+components|in-degree|out-degree|tunnel network)\b', text_clean):
        return ("OUT_OF_SCOPE", "OOS_MODULE_3_GRAPH", "Topic belongs to Module 3 (Graphs), which is strictly out of scope.")

    # Module 3 Hashing
    if re.search(r'\b(hash\s+table|hashing|hash\s+function|collision\s+resolution|linear\s+probing|quadratic\s+probing|double\s+hashing|open\s+addressing|chaining\s+method|hash\s+clash)\b', text_clean):
        return ("OUT_OF_SCOPE", "OOS_MODULE_3_HASHING", "Topic belongs to Module 3 (Hashing), which is strictly out of scope.")

    # Module 4 Excluded Sorts
    if re.search(r'\b(merge\s+sort|radix\s+sort|shell\s+sort|bucket\s+sort|counting\s+sort|external\s+sort)\b', text_clean):
        return ("OUT_OF_SCOPE", "OOS_MODULE_4_EXCLUDED_SORT", "Sorting algorithm (Merge/Radix/Shell/Bucket/Counting) is not in the locked syllabus whitelist.")

    # Heap Sort full algorithm (where not build-max-heap or max-heapify)
    if re.search(r'\b(heap\s*sort|heapsort)\b', text_clean) and not re.search(r'(max[-\s]*heap|min[-\s]*heap|heapify|build[-\s]*max[-\s]*heap)', text_clean):
        return ("OUT_OF_SCOPE", "OOS_MODULE_4_EXCLUDED_SORT", "Full Heap Sort algorithm is excluded; only Max-Heapify and Build-Max-Heap are in locked syllabus.")

    # External sorting / merging files / population sort
    if re.search(r'(merg(e|ing)\s+\d+\s+sorted\s+files|population\s+of\s+west\s+bengal.*age\s+in\s+months)', text_clean):
        return ("OUT_OF_SCOPE", "OOS_MODULE_4_EXCLUDED_SORT", "External sorting and specialized linear-time non-comparison sorting (Bucket/Counting Sort) are excluded.")

    # General programming / OS / Non-DSA topics outside syllabus
    if re.search(r'\b(sequential\s+files|garbage\s+collection|random\s+numbers\s+in\s+a\s+given\s+file|rdbms|network\s+data\s+model|hierarchical\s+data\s+model|greedy\s+algorithm|empty\s+string|terminating\s+null\s+character|what\s+is\s+a\s+string|substings\s+of\s+w|operations\s+that\s+can\s+be\s+performed\s+on\s+a\s+string|allocate\s+memory\s+dynamically\s+for\s+strings)\b', text_clean):
        return ("OUT_OF_SCOPE", "OOS_GENERAL_OUTSIDE_SYLLABUS", "Concept (String fundamentals / File storage / OS garbage collection / DBMS models / Greedy algorithms) is outside the syllabus.")

    # --------------------------------------------------------------------------
    # 2. IN-SCOPE DETERMINATION
    # --------------------------------------------------------------------------

    # Heapify lines (e.g. DOC-19 pseudocode lines)
    if re.search(r'(heap_size|exchange\(a\[i\]|r\s*←\s*right\(i\)|smallest\s*←|largest\s*←)', text_clean):
        return ("IN_SCOPE", "M4_SORT_HEAPIFY", "Max-Heapify and Build-Max-Heap algorithm mechanics")

    # Math lemma for Build-Max-Heap O(n) proof
    if re.search(r'h\s*2\s*[ℎh]\s*∞\s*[ℎh]=0\s*=\s*2', text_clean):
        return ("IN_SCOPE", "M4_SORT_HEAPIFY", "Mathematical lemma for Build-Max-Heap linear time O(n) analysis")

    # Max-Heapify and Build-Max-Heap
    if re.search(r'(max[-\s]*heapify|build[-\s]*max[-\s]*heap|max[-\s]*heap|min[-\s]*heap|min[-\s]*binary\s+heap|n-element\s+heap|\bheap\b)', text_clean):
        if not re.search(r'(heap\s+vs\.\s+on\s+the\s+stack|memory\s+heap)', text_clean):
            return ("IN_SCOPE", "M4_SORT_HEAPIFY", "Max-Heapify and Build-Max-Heap: properties, array indexing, construction, and operations")
        else:
            return ("IN_SCOPE", "M2_STACK_IMPL", "Stack memory vs heap memory concepts in programming / data structures")

    # Sorting Whitelist
    if re.search(r'(cocktail\s+shaker\s+sort|cocktail\s+sort|shaker\s+sort|bidirectional\s+bubble)', text_clean):
        return ("IN_SCOPE", "M4_SORT_COCKTAIL", "Cocktail Shaker Sort")

    if re.search(r'(bubble\s+sort|modified\s+bubble\s+sort|optimized\s+bubble\s+sort)', text_clean):
        return ("IN_SCOPE", "M4_SORT_BUBBLE", "Bubble Sort and Bubble Sort optimizations")

    if re.search(r'(insertion\s+sort|which\s+sorting\s+algorithm\s+is\s+best\s+if\s+the\s+list\s+is\s+already\s+sorted)', text_clean):
        return ("IN_SCOPE", "M4_SORT_INSERTION", "Insertion Sort: Best-case, Worst-case, Average-case analysis")

    if re.search(r'(selection\s*sort|selectionsort|sub\s+algorithm\s+to\s+find\s+the\s+smallest\s+element\s+in\s+the\s+array|sort:\s*20,\s*35,\s*40,\s*100,\s*3,\s*10,\s*15)', text_clean):
        return ("IN_SCOPE", "M4_SORT_SELECTION", "Selection Sort")

    if re.search(r'(quick\s*sort|quicksort|lomuto|hoare|partitioning\s+algorithm|what\s+are\s+partitions)', text_clean):
        return ("IN_SCOPE", "M4_SORT_QUICK", "Quick Sort (Algorithm and partitioning, without complexity analysis)")

    if re.search(r'(what\s+is\s+sorting|internal\s+sorting|stable\s+sort|popular\s+sorting\s+methods|compare\s+and\s+contrast\s+various\s+sorting)', text_clean):
        return ("IN_SCOPE", "M4_SORT_BUBBLE", "Sorting foundations and stability in syllabus sorting algorithms")

    # Searching Whitelist
    if re.search(r'(interpolation\s+search)', text_clean):
        return ("IN_SCOPE", "M4_SEARCH_INTERPOLATION", "Interpolation Search")

    if re.search(r'(binary\s+search)', text_clean):
        return ("IN_SCOPE", "M4_SEARCH_BINARY", "Binary Search: Worst-case and Average-case analysis")

    if re.search(r'(sequential\s+search|linear\s+search|brute\s+force\s+algorithm.*search|sentinel|second\s+largest\s+element.*single\s+pass)', text_clean):
        return ("IN_SCOPE", "M4_SEARCH_SEQUENTIAL", "Sequential Search (Linear Search)")

    if re.search(r'(expected\s+number\s+of\s+comparisons\s+required\s+to\s+find\s+an\s+element|uniformly\s+distributed.*comparisons\s+required\s+to\s+locate\s+a\s+key)', text_clean):
        return ("IN_SCOPE", "M4_SEARCH_SEQUENTIAL", "Sequential Search average-case analysis")

    # Module 1: Array
    if re.search(r'(row\s*major|column\s*major|address\s+of\s+the\s+element|base\s+address|address\s+calculation|2d\s+array|two-dimensional\s+array|multidimensional\s+array|row-major|column-major|upper\s+triangular\s+matrix|symmetric\s+matrices.*memory|multiplication\s+of\s+(two\s+)?matrices|complexity\s+of\s+multiplying\s+two\s+matrices|what\s+values\s+are\s+automatically\s+assigned\s+to\s+those\s+array\s+elements)', text_clean):
        return ("IN_SCOPE", "M1_ARRAY_REPRESENTATION", "Array representations: Row-major and Column-major order address calculations")

    if re.search(r'(sparse\s+matrix|triplet\s+array|triplet\s+format|triplet\s+representation|3-tuple|fast\s+transpose)', text_clean):
        return ("IN_SCOPE", "M1_ARRAY_SPARSE", "Sparse matrix: implementation, 3-tuple representation, and usage")

    if re.search(r'(polynomial.*array|array.*polynomial|represent\s+a\s+polynomial\s+using\s+array|evaluate\s+the\s+polynomial)', text_clean):
        return ("IN_SCOPE", "M1_ARRAY_POLYNOMIAL", "Array representation of polynomials")

    if re.search(r'(remove\s+duplicates\s+from\s+an\s+ordered\s+array|linear\s+array|merge\s+two\s+sorted\s+arrays\s+into\s+a\s+third\s+array|arr\[i\]|limitations\s+of\s+arrays)', text_clean):
        return ("IN_SCOPE", "M1_ARRAY_REPRESENTATION", "Array operations and memory representations")

    # Module 1: Linked List
    if re.search(r'(circular\s+doubly\s+linked|doubly\s+circular\s+linked|cdll)', text_clean) or re.search(r'(circular\s+doubly\s+linked|doubly\s+circular)', context_full):
        return ("IN_SCOPE", "M1_LL_DOUBLY_CIRCULAR", "Doubly circular linked list")

    if re.search(r'(doubly\s+linked|double\s+linked|dll\b)', text_clean) or re.search(r'(doubly\s+linked|double\s+linked)', context_full):
        return ("IN_SCOPE", "M1_LL_DOUBLY", "Doubly linked list")

    if re.search(r'(circular\s+linked|circular\s+singly|cll\b|circular\s+header\s+link\s+list)', text_clean) or re.search(r'(circular\s+linked|circular\s+singly)', context_full):
        return ("IN_SCOPE", "M1_LL_CIRCULAR", "Circular linked list")

    if re.search(r'(polynomial.*linked\s*list|linked\s*list.*polynomial|add\s+two\s+polynomials\s+using\s+linked\s*list)', text_clean):
        return ("IN_SCOPE", "M1_LL_POLYNOMIAL", "Linked list representation of polynomial and operations")

    if re.search(r'(advantage.*linked\s+list.*array|application.*linked\s+list|linked\s+list\s+vs\s+array|why\s+linked\s+list|multilinked\s+structures)', text_clean):
        return ("IN_SCOPE", "M1_LL_APPLICATIONS", "Applications and trade-offs of linked lists")

    if re.search(r'(linked\s+list|singly\s+linked|single\s+linked|node\s*\*|struct\s+node|insert\s+a\s+node|delete\s+a\s+node|reverse\s+a\s+singly\s+linked|reverse\s+the\s+linked\s+list|count\s+number\s+of\s+nodes|pointing\s+to\s+next\s+node|what\s+does\s+node\s+consist|pointer\s+to\s+a\s+node\s+x|delete\s+the\s+first\s+element|insert\s+a\s+new\s+element\s+as\s+a\s+first\s+element|delete\s+the\s+last\s+element|pointer\s+to\s+a\s+sorted\s+list)', text_clean) or 'singly linked list' in context_full:
        return ("IN_SCOPE", "M1_LL_SINGLY", "Singly linked list: node structure, insertion, deletion, reversal, and traversal")

    # Module 1: Introduction & Asymptotic Notations
    if re.search(r'(big[-\s]*o|big[-\s]*oh|big[-\s]*omega|big[-\s]*theta|\bo\(|ω\(|θ\(|\(|asymptotic|order\s+of\s+growth|tight\s+bound|upper\s+bound|lower\s+bound|f\(n\)\s*=\s*3n2\+10|n2\s*\+\s*100\s*n|t\(n\)\s*=\s*48n100|t\(n\)\s*=\s*t\(n/3\)\s*\+\s*c|compare\s+two\s+functions|execute\s+the\s+slowest\s+for\s+large\s+values\s+of\s+n)', text_clean):
        return ("IN_SCOPE", "M1_INTRO_ASYMPTOTIC", "Asymptotic notations: Big O, Ω, Θ notations")

    if re.search(r'(why\s+do\s+we\s+need\s+data\s+structure|need\s+for\s+data\s+structure|areas\s+in\s+which\s+data\s+structures\s+are\s+applied|definition\s+of\s+data\s+structure)', text_clean):
        return ("IN_SCOPE", "M1_INTRO_NEED", "Why do we need data structure?")

    if re.search(r'(abstract\s+data\s+type|adt\b|linear\s+(and|vs)\s+(a\s+)?non-?linear|primitive\s+and\s+non-?primitive|data\s+type\s+and\s+data\s+structure|how\s+does\s+an\s+array\s+differ\s+from\s+an\s+ordinary\s+variable)', text_clean):
        return ("IN_SCOPE", "M1_INTRO_CONCEPTS", "Concepts of data structures: Data, Data structure, ADT and Data Type")

    if re.search(r'(algorithm\s+and\s+program|difference\s+between\s+algorithm\s+and\s+program|pseudo-code|pseudocode|characteristics\s+of\s+a\s+good\s+algorithm|characteristics\s+of\s+an\s+algorithm|what\s+is\s+an\s+algorithm|problem\s+solving\s+techniques)', text_clean):
        return ("IN_SCOPE", "M1_INTRO_ALGO_PROG", "Algorithms and programs, basic idea of pseudo-code")

    if re.search(r'(algorithm\s+efficiency|time\s+and\s+space\s+analysis|frequency\s+count|space\s+complexity|time\s+complexity|worst\s+case\s+analysis\s+and\s+best\s+case\s+analysis|two\s+independent\s+time\s+complexities|relation\s+between\s+the\s+time\s+and\s+space\s+complexities)', text_clean):
        return ("IN_SCOPE", "M1_INTRO_EFFICIENCY", "Algorithm efficiency and analysis: Time and space analysis")

    # Module 2: Stack and Queue
    if re.search(r'(deque|double\s+ended\s+queue|input-restricted|output-restricted|input\s+restricted|output\s+restricted)', text_clean) or 'deque' in context_full:
        return ("IN_SCOPE", "M2_DEQUE", "Deque: implementation, input-restricted and output-restricted deque")

    if re.search(r'(circular\s+queue|queue\s+is\s+circular)', text_clean) or 'circular queue' in context_full:
        return ("IN_SCOPE", "M2_QUEUE_LINEAR_CIRCULAR", "Circular queue: operations, array and linked list implementation")

    if re.search(r'(queue\s+using\s+stack|two\s+stacks\s+to\s+implement\s+a\s+queue|stack\s+using\s+queue|two\s+stacks\s+on\s+the\s+same\s+array)', text_clean):
        return ("IN_SCOPE", "M2_STACK_IMPL", "Stack and Queue interplay / multiple stacks in single array")

    if re.search(r'(postfix|prefix|infix|reverse\s+polish|parenthes|balanced\s+parenthes|adjacent\s+duplicates.*stack|removing\s+adjacent\s+duplicates|arithmetic\s+expression.*prefix\s+and\s+postfix)', text_clean) or any(term in context_full for term in ['postfix', 'prefix', 'infix']):
        return ("IN_SCOPE", "M2_STACK_APPLICATIONS", "Applications of stack: Infix/Postfix/Prefix conversion/evaluation, parenthesis matching")

    if re.search(r'(stack\s+overflow|stack\s+underflow|lifo|top\s+of\s+stack|push.*pop|stack\s+using\s+array|stack\s+using\s+linked\s*list|\bstack\b|top\s*\(push)', text_clean) or 'stack' in context_full:
        return ("IN_SCOPE", "M2_STACK_IMPL", "Stack: concepts, array and linked list implementations, operations")

    if re.search(r'(application.*queue|queue.*scheduling|spooling|printer\s+queue|priority\s+queue)', text_clean):
        return ("IN_SCOPE", "M2_QUEUE_APPLICATIONS", "Applications of queue")

    if re.search(r'(fifo|enqueue|dequeue|front\s+and\s+rear|queue\s+using\s+array|queue\s+using\s+linked\s*list|linear\s+queue|\bqueue\b|add\s+1,\s*2,\s*3,\s*4,\s*5,\s*6|delete\s+two\s+numbers|delete\s+four\s+numbers)', text_clean) or 'queue' in context_full:
        return ("IN_SCOPE", "M2_QUEUE_LINEAR_CIRCULAR", "Queue: linear queue, array and linked list implementations, operations")

    # Module 2: Recursion
    if re.search(r'(tail\s+recursion|tail\s+recursive|convert.*tail\s+recursion|eliminate\s+tail\s+recursion)', text_clean):
        return ("IN_SCOPE", "M2_REC_TAIL", "Tail recursion: concept, elimination, and efficiency")

    if re.search(r'(tower.*hanoi|eight\s+queens|8\s*queens|backtracking|number\s+of\s+discs)', text_clean) or 'hanoi' in context_full or 'discs' in context_full:
        return ("IN_SCOPE", "M2_REC_APPLICATIONS", "Recursion Applications: Tower of Hanoi, Eight Queens, Backtracking")

    if re.search(r'(principles?\s+of\s+recursion|recursion\s+vs\s+iteration|difference\s+between\s+recursion\s+and\s+iteration|use\s+of\s+stack\s+in\s+recursion|recursive|base\s+case|base\s+condition|fibo\(5\)|fun\(5,\s*0,\s*1\)|gcd.*recursion|ackerman|recursive_sum_of_digits|int\s+f\(int\s+n\)|int\s+fun\(int\s+n\)|void\s+fn\(\s*\))', text_clean) or 'recursion' in context_full:
        return ("IN_SCOPE", "M2_REC_PRINCIPLES", "Principles of recursion, use of stack, recursion vs iteration")

    return ("AMBIGUOUS", "AMBIGUOUS_UNCLASSIFIED", "Wording insufficient or does not match definite syllabus keyword patterns.")

# Test
res = Counter()
ambigs = []
for q in questions:
    scope, topic_id, reason = classify_question_occurrence(q)
    res[scope] += 1
    if scope == 'AMBIGUOUS':
        ambigs.append(q)

print(f"Final Detailed Classification Results (Total {len(questions)}):")
for s, c in sorted(res.items()):
    print(f"  {s}: {c}")

print(f"\nRemaining ambiguous count: {len(ambigs)}")
if ambigs:
    for a in ambigs:
        print(f"[{a['question_instance_id']}] {a['raw_text']}")
