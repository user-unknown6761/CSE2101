# CSE2101 / CSEN2101 Syllabus Scope Audit Report

## 1. Executive Accounting Summary

| Classification Category | Question Count | Percentage | Definition / Gate Policy |
| :--- | :--- | :--- | :--- |
| **IN_SCOPE** | **780** | 61.90% | Rigorously maps to Module 1, Module 2, or whitelisted Module 4 topics |
| **OUT_OF_SCOPE** | **479** | 38.02% | Module 3 topics, excluded sorts, Quick Sort complexity analysis, or non-DSA topics |
| **AMBIGUOUS** | **1** | 0.08% | Genuinely insufficient wording / isolated tokens lacking semantic context |
| **TOTAL SOURCE QUESTIONS** | **1260** | **100.00%** | **Exact match against 1,260 true question occurrences** |

> [!IMPORTANT]
> **Accounting Invariant Check: PASS** (780 (IN_SCOPE) + 479 (OUT_OF_SCOPE) + 1 (AMBIGUOUS) == 1260). No questions created, zero lost.

---

## 2. In-Scope Questions Distribution Across Syllabus Topics

| Topic ID | Topic Description | Question Occurrences |
| :--- | :--- | :--- |
| `M1_LL_SINGLY` | Singly linked list (creation, insertion, deletion, traversal, reversal) | 111 |
| `M1_LL_CIRCULAR` | Circular linked list | 71 |
| `M4_SORT_HEAPIFY` | Max-Heapify and Build-Max-Heap | 58 |
| `M2_STACK_APPLICATIONS` | Applications of stack: Infix/Postfix/Prefix conversion, evaluation, parenthesis matching | 57 |
| `M1_INTRO_ASYMPTOTIC` | Asymptotic notations: Big O, Ω, Θ notations | 48 |
| `M1_LL_DOUBLY` | Doubly linked list | 47 |
| `M1_ARRAY_REPRESENTATION` | Different representations: Row major and Column major order | 45 |
| `M2_STACK_IMPL` | Stack: implementation using array and linked list | 45 |
| `M1_ARRAY_SPARSE` | Sparse matrix: implementation and usage | 28 |
| `M4_SORT_INSERTION` | Insertion Sort: Best-case, Worst-case, Average-case analysis | 27 |
| `M2_DEQUE` | Deque: implementation, input-restricted and output-restricted | 26 |
| `M2_QUEUE_LINEAR_CIRCULAR` | Queue and Circular queue: linear, circular, using array, using linked list | 25 |
| `M1_INTRO_ALGO_PROG` | Algorithms and programs, basic idea of pseudo-code | 23 |
| `M4_SEARCH_BINARY` | Binary Search: Worst-case and Average-case analysis | 22 |
| `M4_SORT_BUBBLE` | Bubble Sort and Bubble Sort optimizations | 20 |
| `M4_SEARCH_INTERPOLATION` | Interpolation Search | 19 |
| `M4_SEARCH_SEQUENTIAL` | Sequential Search | 18 |
| `M2_REC_APPLICATIONS` | Recursion Applications: Tower of Hanoi, Eight Queens Puzzle, concept of Backtracking | 17 |
| `M4_SORT_QUICK` | Quick Sort (WITHOUT complexity analysis) | 16 |
| `M1_INTRO_EFFICIENCY` | Algorithm efficiency and analysis: Time and space analysis of algorithms | 11 |
| `M1_INTRO_CONCEPTS` | Concepts of data structures: Data, Data structure, Abstract Data Type (ADT) and Data Type | 11 |
| `M2_REC_PRINCIPLES` | Principles of recursion, use of stack, recursion vs iteration | 10 |
| `M4_SORT_SELECTION` | Selection Sort | 7 |
| `M1_ARRAY_POLYNOMIAL` | Array representation of polynomials | 6 |
| `M2_REC_TAIL` | Tail recursion | 4 |
| `M1_LL_APPLICATIONS` | Applications of linked list | 4 |
| `M2_QUEUE_APPLICATIONS` | Applications of queue | 2 |
| `M1_INTRO_NEED` | Why do we need data structure? | 1 |
| `M4_SORT_COCKTAIL` | Cocktail Shaker Sort | 1 |

---

## 3. Out-Of-Scope Classification Breakdown

| Exclusion Category | Count | Primary Rationale |
| :--- | :--- | :--- |
| `OOS_MODULE_3_TREE` | 226 | Module 3 Tree topics (Binary Tree, BST, AVL Tree, B-Tree, Threaded Tree, Traversals, Huffman, Trie) permanently excluded. |
| `OOS_MODULE_3_GRAPH` | 125 | Module 3 Graph topics (BFS, DFS, Dijkstra, Prim, Kruskal, Topological Sort, Graph Matrix/List representations) permanently excluded. |
| `OOS_MODULE_3_HASHING` | 67 | Module 3 Hashing topics (Hash Tables, Linear/Quadratic Probing, Chaining, Collision Resolution) permanently excluded. |
| `OOS_MODULE_4_EXCLUDED_SORT` | 45 | Module 4 Excluded Sorting algorithms (Merge Sort, Radix Sort, Shell Sort, Bucket Sort, Counting Sort, full HeapSort algorithm). |
| `OOS_GENERAL_OUTSIDE_SYLLABUS` | 12 | Non-DSA questions from source question papers (String fundamentals, dynamic allocation, sequential files, OS garbage collection, DBMS models, Greedy algorithms). |
| `OOS_M4_QUICK_SORT_COMPLEXITY` | 4 | Quick Sort complexity analysis (recurrence derivation / worst-case analysis) explicitly locked out by syllabus. |

---

## 4. Ambiguous Questions Audit

The following question(s) contain insufficient wording or represent isolated code tokens where guessing is forbidden by system contract:

- **ID**: `DOC-19-P13-Q05` (DOC-19 Page 13)
  - **Raw Text**: `else`
  - **Reason**: Isolated token ('else') lacking sufficient grammatical or semantic context to form an answerable question.
