import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('AUTHORITATIVE_SYLLABUS.json', 'r', encoding='utf-8') as f:
    syllabus = json.load(f)

with open('QUESTION_FAMILIES.json', 'r', encoding='utf-8') as f:
    families = json.load(f)

fams_by_topic = {}
for fam in families:
    tid = fam['topic_id']
    if tid not in fams_by_topic:
        fams_by_topic[tid] = []
    fams_by_topic[tid].append(fam)

# Pedagogical content database for all 31 syllabus topics
PEDAGOGY_DATA = {
    # --------------------------------------------------------------------------
    # MODULE 1: INTRODUCTION
    # --------------------------------------------------------------------------
    "M1_INTRO_NEED": {
        "what_it_is": "A data structure is a specialized format for organizing, processing, retrieving, and storing data in computer memory to enable efficient execution of operations.",
        "why_it_exists": "Modern software handles massive volumes of data. Without structured organization, searching, inserting, and deleting records becomes prohibitively slow (O(n) or worse), wasting CPU cycles and memory. Data structures provide tailored layouts to optimize time and space trade-offs.",
        "core_terminology": [
            {"term": "Data", "def": "Raw facts, values, or symbols without context."},
            {"term": "Data Structure", "def": "A mathematical or logical model of organizing data elements together with the operations applicable on them."},
            {"term": "Time Complexity", "def": "The amount of computational time taken by an algorithm to run as a function of the input size."},
            {"term": "Space Complexity", "def": "The total amount of memory space required by the algorithm during its execution."}
        ],
        "core_idea_and_intuition": "Think of a library: if books are piled randomly on the floor, finding a single book requires checking every book one by one. If books are sorted alphabetically on labeled shelves, finding a book takes seconds. Data structures are the organized shelves of computer memory.",
        "important_representations": "Memory is viewed as a linear sequence of addressable bytes. Data structures map logical relationships (linear sequence, hierarchical, or tabular) onto this linear address space.",
        "algorithm_procedure": "1. Analyze problem domain and data types.\n2. Identify primary operations (insert, search, delete, sort).\n3. Evaluate operation frequencies.\n4. Select data structure minimizing asymptotic cost of dominant operations.",
        "formula_rule_invariant": "Efficiency Invariant: Choose structure where dominant operations run in O(1) or O(log n) time without exceeding memory budget.",
        "common_mistakes_to_avoid": "Confusing a basic data type (e.g., int, float) with an organized data structure (e.g., array of structures, linked list).",
        "exam_writing_guidance": "Always give: (1) Formal definition, (2) Three key reasons for necessity (fast retrieval, optimal memory utilization, real-world modeling), (3) Mention time-space trade-off with an example.",
        "quick_recall_block": {
            "trigger_words": ["Need for data structures", "Importance of organization", "Why data structure"],
            "core_rule": "Organization determines operational efficiency.",
            "exam_checklist": ["Formal definition", "Time efficiency", "Space efficiency", "Real-world example"]
        }
    },
    "M1_INTRO_CONCEPTS": {
        "what_it_is": "Foundational taxonomy distinguishing raw data, composite structures, Abstract Data Types (ADTs), and concrete data types, along with Linear vs Non-Linear classifications.",
        "why_it_exists": "Separates the mathematical specification of what operations do (ADT) from how they are implemented in code and memory (concrete data structure), enabling modular, maintainable software design.",
        "core_terminology": [
            {"term": "Abstract Data Type (ADT)", "def": "A mathematical model for data types where a data type is defined by its behavior (semantics) from the point of view of a user of the data, specifically in terms of possible values, possible operations, and the behavior of these operations, without specifying implementation details."},
            {"term": "Data Type", "def": "A concrete programming language construct that defines the set of values and valid operations (e.g., int, float, char)."},
            {"term": "Linear Data Structure", "def": "Elements form a sequence; each element has unique predecessor and successor (except ends). Examples: Array, Linked List, Stack, Queue."},
            {"term": "Non-Linear Data Structure", "def": "Elements are not arranged in a sequential order; an element can be connected to multiple elements. Examples: Tree, Graph."}
        ],
        "core_idea_and_intuition": "An ADT is like a car dashboard: you have a steering wheel, accelerator, and brake. You know what they do without needing to know whether the engine is gasoline, diesel, or electric.",
        "important_representations": "Taxonomy table:\n- Primitive (int, char, float, pointer)\n- Non-Primitive:\n  - Linear (Arrays, Linked Lists, Stacks, Queues)\n  - Non-Linear (Trees, Graphs)",
        "algorithm_procedure": "Specifying an ADT:\n1. Define Type name.\n2. Define Data members abstractly.\n3. Define Function signatures (Name, Parameters, Return type, Pre-conditions, Post-conditions).",
        "formula_rule_invariant": "ADT Invariant: Behavior is invariant of implementation. Stack ADT is LIFO whether implemented via Array or Linked List.",
        "common_mistakes_to_avoid": "Writing C code when asked to define an ADT. An ADT is purely a conceptual specification.",
        "exam_writing_guidance": "In tabular comparisons, always include: Definition, Memory arrangement, Traversal method, Number of levels, and Examples.",
        "quick_recall_block": {
            "trigger_words": ["ADT vs Data Type", "Linear vs Non-Linear", "Primitive vs Non-Primitive"],
            "core_rule": "ADT = WHAT (interface); Data Structure = HOW (implementation).",
            "exam_checklist": ["Mathematical definition of ADT", "3 examples of ADT operations", "Linear vs Non-Linear table"]
        }
    },
    "M1_INTRO_ALGO_PROG": {
        "what_it_is": "The rigorous distinction between an algorithm (a finite, abstract sequence of well-defined steps to solve a problem) and a program (an implementation of an algorithm in a specific programming language).",
        "why_it_exists": "Allows analyzing problem-solving logic independent of hardware architecture, compiler optimizations, or language syntax.",
        "core_terminology": [
            {"term": "Algorithm", "def": "A finite set of unambiguous instructions that, given a set of inputs, produces an output and terminates in finite time."},
            {"term": "Program", "def": "An executable sequence of instructions written in a concrete programming language designed to run on a machine."},
            {"term": "Pseudo-code", "def": "An informal high-level description of an algorithm that uses structural conventions of programming languages without strict syntax."},
            {"term": "Finiteness", "def": "An algorithm must always terminate after a finite number of steps."}
        ],
        "core_idea_and_intuition": "An algorithm is a recipe written on paper; a program is cooking the actual meal in a specific kitchen using specific utensils.",
        "important_representations": "Five Essential Characteristics of an Algorithm (Knuth):\n1. Input: Zero or more quantities externally supplied.\n2. Output: At least one quantity produced.\n3. Definiteness: Each instruction is clear and unambiguous.\n4. Finiteness: Terminates after finite steps.\n5. Effectiveness: Every operation is basic enough to be done exactly in finite time.",
        "algorithm_procedure": "Algorithm Design Workflow:\n1. Problem specification.\n2. Model formulation.\n3. Pseudocode drafting.\n4. Correctness verification (invariants/induction).\n5. Asymptotic complexity analysis.",
        "formula_rule_invariant": "Invariant: An algorithm must terminate (Finiteness). A program may loop indefinitely (e.g. OS kernel, daemon).",
        "common_mistakes_to_avoid": "Listing language-specific details (like printf or include <stdio.h>) when writing pseudocode.",
        "exam_writing_guidance": "When asked for difference between Algorithm and Program, use a 4-point comparison table: Definition, Language dependency, Hardware dependency, and Finiteness.",
        "quick_recall_block": {
            "trigger_words": ["Algorithm vs Program", "Characteristics of algorithm", "Pseudo-code"],
            "core_rule": "Algorithm = Abstract, Machine-independent logic. Program = Concrete, Executable code.",
            "exam_checklist": ["5 Knuth characteristics", "Pseudocode definition", "Comparison table"]
        }
    },
    "M1_INTRO_EFFICIENCY": {
        "what_it_is": "The scientific measurement of an algorithm's resource consumption, specifically running time (instruction execution count) and storage (memory space used) as functions of input size n.",
        "why_it_exists": "Enables predicting execution performance on large datasets before writing code, and prevents algorithmic bottlenecks in production systems.",
        "core_terminology": [
            {"term": "Time Analysis", "def": "Counting the frequency of primitive statement executions as a function of input size n."},
            {"term": "Space Analysis", "def": "Sum of fixed space (code, constants) and variable space (dynamic variables, recursion stack)."},
            {"term": "Frequency Count", "def": "The exact number of times a particular statement executes in an algorithm loop."},
            {"term": "Best Case", "def": "Minimum resources required across all inputs of size n."},
            {"term": "Worst Case", "def": "Maximum resources required across all inputs of size n (guaranteed upper bound)."},
            {"term": "Average Case", "def": "Expected resource usage averaged over all valid inputs with an assumed probability distribution."}
        ],
        "core_idea_and_intuition": "Wall-clock seconds depend on whether your laptop has a fast CPU or background tasks. Step count depends purely on mathematics and input size n.",
        "important_representations": "Space Breakdown:\nS(P) = c + S_p(I)\nwhere c is constant space (instruction code, simple variables) and S_p(I) is instance characteristics (dynamic memory, recursion call stack depth).",
        "algorithm_procedure": "Step Count Method:\n1. Identify every basic operation (assignment, comparison, arithmetic).\n2. Write frequency count for each line.\n3. Sum the counts to form polynomial f(n).\n4. Extract dominant term.",
        "formula_rule_invariant": "Loop Invariant Rule: A loop running from i=1 to n with step 1 executes test statement (n+1) times and loop body n times.",
        "common_mistakes_to_avoid": "Assuming running time in seconds is an algorithmic metric. Time in seconds is an empirical benchmark, not an algorithmic time complexity.",
        "exam_writing_guidance": "When asked to analyze a code snippet, show line-by-line step count in a table: Statement, Cost per execution, Frequency, Total cost.",
        "quick_recall_block": {
            "trigger_words": ["Time and space analysis", "Frequency count", "Step count method"],
            "core_rule": "Count basic steps as f(n). Drop lower-order terms and constants.",
            "exam_checklist": ["Time vs Space definitions", "Frequency count table", "Best, Worst, Average case definitions"]
        }
    },
    "M1_INTRO_ASYMPTOTIC": {
        "what_it_is": "Mathematical notations used to describe the limiting behavior of an algorithm's running time as input size n approaches infinity: Big O (upper bound), Big Omega Ω (lower bound), and Big Theta Θ (tight bound).",
        "why_it_exists": "Allows comparing algorithms independent of hardware constants and focuses on how execution time scales as data grows arbitrarily large.",
        "core_terminology": [
            {"term": "Big-O (O)", "def": "Asymptotic Upper Bound: f(n) = O(g(n)) iff ∃ positive constants c and n0 such that 0 ≤ f(n) ≤ c·g(n) ∀ n ≥ n0."},
            {"term": "Big-Omega (Ω)", "def": "Asymptotic Lower Bound: f(n) = Ω(g(n)) iff ∃ positive constants c and n0 such that 0 ≤ c·g(n) ≤ f(n) ∀ n ≥ n0."},
            {"term": "Big-Theta (Θ)", "def": "Asymptotic Tight Bound: f(n) = Θ(g(n)) iff ∃ positive constants c1, c2 and n0 such that 0 ≤ c1·g(n) ≤ f(n) ≤ c2·g(n) ∀ n ≥ n0."}
        ],
        "core_idea_and_intuition": "Big-O guarantees your program will not be slower than c·g(n). Big-Omega guarantees it will not be faster than c·g(n). Big-Theta proves both sandwich the running time tightly.",
        "important_representations": "Hierarchy of growth rates:\nO(1) < O(log n) < O(√n) < O(n) < O(n log n) < O(n^2) < O(n^3) < O(2^n) < O(n!)",
        "algorithm_procedure": "Proving f(n) = O(g(n)):\n1. Write f(n) as given polynomial.\n2. Replace all lower powers of n with highest power for n ≥ 1.\n3. Sum coefficients to find constant c.\n4. State valid n0 (usually n0 = 1).",
        "formula_rule_invariant": "Theorem: f(n) = Θ(g(n)) if and only if f(n) = O(g(n)) and f(n) = Ω(g(n)).",
        "common_mistakes_to_avoid": "Writing negative constants or claiming Big-O must be the worst-case. Big-O can describe the best, worst, or average case upper bound.",
        "exam_writing_guidance": "In proof questions (e.g. Prove n^2 + 100n = Θ(n^2)), explicitly find and write the numerical values of c1, c2, and n0.",
        "quick_recall_block": {
            "trigger_words": ["Big-O", "Big-Omega", "Big-Theta", "Asymptotic bound", "Order of growth"],
            "core_rule": "O = Upper bound (≤), Ω = Lower bound (≥), Θ = Tight bound (sandwiched).",
            "exam_checklist": ["Exact mathematical definitions with c, n0", "Graph sketch", "Growth rate ordering"]
        }
    },

    # --------------------------------------------------------------------------
    # MODULE 1: ARRAY
    # --------------------------------------------------------------------------
    "M1_ARRAY_REPRESENTATION": {
        "what_it_is": "The linear mapping of multidimensional arrays (2D, 3D, and triangular) into contiguous computer memory using Row-Major Order (row by row) or Column-Major Order (column by column).",
        "why_it_exists": "Physical RAM is a 1D linear array of memory addresses. A mathematical matrix A[m][n] must be systematically serialized into contiguous linear addresses.",
        "core_terminology": [
            {"term": "Row-Major Order", "def": "Storing elements of an array row after row in contiguous memory locations (default in C, C++, Java)."},
            {"term": "Column-Major Order", "def": "Storing elements of an array column after column in contiguous memory locations (used in FORTRAN, MATLAB)."},
            {"term": "Base Address (B)", "def": "The memory address of the very first element A[0][0] or A[L1][L2]."},
            {"term": "Element Size (w)", "def": "The number of bytes occupied by a single element (e.g., 2 bytes for short, 4 bytes for int/float)."},
            {"term": "Upper Triangular Matrix", "def": "A square matrix where all entries below the main diagonal are zero (A[i][j] = 0 for i > j)."}
        ],
        "core_idea_and_intuition": "In Row-Major, to reach element (i, j), you first skip all i full rows that come before it (each row has C elements), then skip j elements in the current row.",
        "important_representations": "For 2D array A[L1..U1][L2..U2] with R = U1 - L1 + 1 and C = U2 - L2 + 1:\n- Row-Major Address: Addr(A[i][j]) = B + w · [ (i - L1) · C + (j - L2) ]\n- Column-Major Address: Addr(A[i][j]) = B + w · [ (j - L2) · R + (i - L1) ]",
        "algorithm_procedure": "Address Calculation Steps:\n1. Identify index bounds: L1, U1 (rows) and L2, U2 (columns).\n2. Compute dimensions: R = U1 - L1 + 1, C = U2 - L2 + 1.\n3. Identify element size w and base address B.\n4. Apply Row-Major or Column-Major formula.",
        "formula_rule_invariant": "Upper Triangular Matrix (0-indexed): Number of non-zero elements = n(n+1)/2. Linear array index for A[i][j] (i ≤ j) in row-major = i·n - i(i-1)/2 + (j - i).",
        "common_mistakes_to_avoid": "Mixing up R (number of rows) and C (number of columns). In Row-Major you multiply row index by number of columns C. In Column-Major you multiply column index by number of rows R.",
        "exam_writing_guidance": "Always write the general algebraic formula first, substitute values with units (bytes), show step-by-step arithmetic, and state final address.",
        "quick_recall_block": {
            "trigger_words": ["Row major", "Column major", "Address calculation", "Base address", "Upper triangular"],
            "core_rule": "Row-Major: B + w·[(i - L1)·C + (j - L2)]. Column-Major: B + w·[(j - L2)·R + (i - L1)].",
            "exam_checklist": ["Identify L1, U1, L2, U2", "Compute R and C", "Substitute into formula with w", "Show intermediate step"]
        }
    },
    "M1_ARRAY_SPARSE": {
        "what_it_is": "A sparse matrix is a matrix in which the majority of elements are zero. Efficient representations store only the non-zero elements using 3-tuple (triplet) arrays.",
        "why_it_exists": "Storing large matrices with 90%+ zeroes in standard 2D arrays wastes massive amounts of RAM and causes CPU cache thrashing on zero multiplications. Triplet format stores only meaningful data.",
        "core_terminology": [
            {"term": "Sparse Matrix", "def": "A matrix where the number of zero elements is substantially greater than the number of non-zero elements."},
            {"term": "3-Tuple / Triplet", "def": "A tabular representation where each row stores (Row, Column, Value) of a non-zero element."},
            {"term": "Header Row", "def": "Row 0 of the triplet array storing (Total Rows, Total Columns, Total Non-Zero Elements)."},
            {"term": "Simple Transpose", "def": "Transposing a triplet matrix by scanning columns 0 to n-1 in O(n · cols) time."},
            {"term": "Fast Transpose", "def": "Transposing a triplet matrix in O(cols + non-zeroes) time using row counts and starting position index arrays."}
        ],
        "core_idea_and_intuition": "Instead of storing a 1000×1000 matrix with 1,000,000 cells where only 5 elements are non-zero, store an array of 6 rows (1 header + 5 elements), saving 99.99% of memory.",
        "important_representations": "Triplet Array Structure:\n- Row 0: [m, n, k] (m rows, n cols, k non-zero elements)\n- Row 1..k: [r_i, c_i, val_i] in ascending row-major order.",
        "algorithm_procedure": "Fast Transpose Algorithm:\n1. Initialize count array of size cols with 0.\n2. For each element in triplet, increment count[col].\n3. Calculate starting positions: start_pos[0] = 1, start_pos[i] = start_pos[i-1] + count[i-1].\n4. For each element in input triplet, place into output at start_pos[col] and increment start_pos[col].",
        "formula_rule_invariant": "Storage Benefit Rule: Normal array size = m · n words. Triplet size = 3 · (k + 1) words. Triplet is beneficial when 3·(k + 1) < m · n, or roughly non-zero ratio k/(m·n) < 1/3 (~33.3%).",
        "common_mistakes_to_avoid": "Forgetting the header row [m, n, k] at index 0, or forgetting that triplet rows must remain sorted by row then column.",
        "exam_writing_guidance": "In justify questions ('Is it beneficial to store as triplet?'), calculate memory for both representations explicitly: 2D array = m×n×w bytes, Triplet = 3×(k+1)×w bytes. Compare and conclude.",
        "quick_recall_block": {
            "trigger_words": ["Sparse matrix", "Triplet representation", "3-tuple", "Fast transpose", "Benefit threshold"],
            "core_rule": "Header row = [Rows, Cols, NonZeros]. Each entry = [i, j, value]. Beneficial when k < (m·n)/3.",
            "exam_checklist": ["Header row [m, n, k]", "1-based or 0-based indexing noted", "Storage formula comparison", "Transposition logic"]
        }
    },
    "M1_ARRAY_POLYNOMIAL": {
        "what_it_is": "Representing a single-variable polynomial P(x) = a_n·x^n + ... + a_1·x + a_0 in computer memory using 1D arrays of coefficients or arrays of (coefficient, exponent) structures.",
        "why_it_exists": "Allows algebraic operations (polynomial addition, subtraction, multiplication, and evaluation via Horner's rule) to be performed deterministically by computer algorithms.",
        "core_terminology": [
            {"term": "Dense Representation", "def": "Array index represents exponent directly: A[i] stores the coefficient of x^i."},
            {"term": "Sparse Polynomial", "def": "Array of structures where each element explicitly stores struct { float coeff; int expo; }."},
            {"term": "Horner's Rule", "def": "Evaluating a polynomial P(x) with minimum multiplications by nesting: (...((a_n·x + a_{n-1})·x + ... )·x + a_0."}
        ],
        "core_idea_and_intuition": "In dense format, the array index is the exponent! To add polynomials, simply add matching array indices: C[i] = A[i] + B[i].",
        "important_representations": "Structure for sparse polynomial:\n```c\ntypedef struct {\n    float coeff;\n    int exp;\n} Term;\nTerm poly[MAX_TERMS];\n```",
        "algorithm_procedure": "Polynomial Addition:\n1. Maintain pointers/indices i for PolyA, j for PolyB, k for PolyC.\n2. While i < lenA and j < lenB:\n   - If expA == expB: C[k].coeff = A[i].coeff + B[j].coeff; C[k].exp = A[i].exp; i++; j++; k++;\n   - Else if expA > expB: Copy A[i] to C[k]; i++; k++;\n   - Else: Copy B[j] to C[k]; j++; k++;\n3. Copy remaining terms from PolyA or PolyB.",
        "formula_rule_invariant": "Horner's Invariant: Evaluating polynomial of degree n requires exactly n multiplications and n additions.",
        "common_mistakes_to_avoid": "Assuming dense array works efficiently for polynomials like x^1000 + 1 (wastes 999 cells). Use array of structures for sparse polynomials.",
        "exam_writing_guidance": "State whether you are using dense array or array of structures. Provide C struct definition and step-by-step addition algorithm.",
        "quick_recall_block": {
            "trigger_words": ["Array representation of polynomial", "Polynomial addition", "Horner's rule"],
            "core_rule": "Dense: index = exponent. Sparse: struct { coeff, exp }. Addition = merge sorted exponents.",
            "exam_checklist": ["Struct definition", "Dense vs Sparse choice", "Three comparison cases (>, <, ==) in addition"]
        }
    },

    # --------------------------------------------------------------------------
    # MODULE 1: LINKED LIST
    # --------------------------------------------------------------------------
    "M1_LL_SINGLY": {
        "what_it_is": "A linear dynamic collection of data nodes, where each node consists of two parts: a data field and a pointer (link) storing the memory address of the next node in the sequence.",
        "why_it_exists": "Overcomes static sizing and costly contiguous shifting required during array insertions and deletions.",
        "core_terminology": [
            {"term": "Node", "def": "A structure containing data payload and a next pointer."},
            {"term": "Head Pointer", "def": "A pointer holding the address of the first node of the list."},
            {"term": "NULL Pointer", "def": "Sentinel value indicating the end of the linked list."},
            {"term": "In-Place Reversal", "def": "Reversing list link directions using three pointers (prev, curr, next) without allocating new nodes."}
        ],
        "core_idea_and_intuition": "Like a treasure hunt: each clue gives you the prize at that spot and a slip of paper telling you where to find the next clue.",
        "important_representations": "C Node Definition:\n```c\nstruct Node {\n    int data;\n    struct Node* next;\n};\n```",
        "algorithm_procedure": "In-Place Reversal Algorithm:\n1. Initialize: prev = NULL, curr = head, next = NULL.\n2. While curr != NULL:\n   - next = curr->next;\n   - curr->next = prev;\n   - prev = curr;\n   - curr = next;\n3. head = prev;\n4. Return head.",
        "formula_rule_invariant": "Reversal Invariant: At each iteration, the sublist from head up to prev is completely reversed, and curr points to unreversed remainder.",
        "common_mistakes_to_avoid": "Losing the next pointer before redirecting curr->next (`curr->next = prev` without saving `next = curr->next` first cuts off the rest of the list!).",
        "exam_writing_guidance": "Draw pointer diagrams for insertion and deletion. For code, always check edge cases: empty list (`head == NULL`) and single-node list.",
        "quick_recall_block": {
            "trigger_words": ["Singly linked list", "Reverse singly linked list", "Insert/delete node in linked list"],
            "core_rule": "Three pointers to reverse: prev, curr, next. Always save next before redirecting link.",
            "exam_checklist": ["struct Node definition", "NULL check", "3-pointer reversal trace", "Pointer update order"]
        }
    },
    "M1_LL_CIRCULAR": {
        "what_it_is": "A linked list where the last node's link pointer does not point to NULL, but points back to the first node (head), forming a continuous closed loop.",
        "why_it_exists": "Allows uninterrupted cyclic traversals (e.g., Round-Robin OS scheduling) and allows reaching any node in the list starting from any other node.",
        "core_terminology": [
            {"term": "Circular Singly Linked List (CLL)", "def": "A singly linked list where tail->next == head."},
            {"term": "Tail Pointer Design", "def": "Maintaining a pointer to the tail node instead of head, allowing O(1) access to both first node (tail->next) and last node (tail)."}
        ],
        "core_idea_and_intuition": "A circle of people holding hands: there is no dead end or 'NULL' at the back.",
        "important_representations": "Memory layout: Node_1 -> Node_2 -> ... -> Node_n -> Node_1.",
        "algorithm_procedure": "Insertion at Beginning (with tail pointer):\n1. Allocate new_node with data.\n2. If tail == NULL: tail = new_node; new_node->next = new_node;\n3. Else: new_node->next = tail->next; tail->next = new_node;\n4. Return tail.",
        "formula_rule_invariant": "Loop termination condition: `do { ptr = ptr->next; } while (ptr != head);` instead of `while (ptr != NULL)`.",
        "common_mistakes_to_avoid": "Writing `while (ptr != NULL)` which creates an infinite loop in circular lists.",
        "exam_writing_guidance": "Always explain the benefit of keeping a `tail` pointer (makes insertion at both head and tail O(1) without O(n) traversal).",
        "quick_recall_block": {
            "trigger_words": ["Circular linked list", "CLL", "Header circular list", "Round robin"],
            "core_rule": "Tail points to head (`tail->next == head`). Never use `ptr != NULL`.",
            "exam_checklist": ["Tail pointer advantage", "do-while traversal loop", "Empty list and single node edge cases"]
        }
    },
    "M1_LL_DOUBLY": {
        "what_it_is": "A linear linked list where each node contains three fields: data, a next pointer to the succeeding node, and a prev pointer to the preceding node.",
        "why_it_exists": "Enables bidirectional traversal (forward and backward) and allows deleting a node in O(1) time given only a pointer to that node.",
        "core_terminology": [
            {"term": "prev pointer", "def": "Pointer pointing to the preceding node (or NULL if at head)."},
            {"term": "next pointer", "def": "Pointer pointing to the succeeding node (or NULL if at tail)."},
            {"term": "Two-Way List", "def": "Synonym for doubly linked list."}
        ],
        "core_idea_and_intuition": "A train where cars are linked both forwards and backwards: you can walk in either direction between cars.",
        "important_representations": "C Node Definition:\n```c\nstruct DNode {\n    int data;\n    struct DNode* prev;\n    struct DNode* next;\n};\n```",
        "algorithm_procedure": "Delete Given Node X (without head traversal):\n1. If X->prev != NULL: X->prev->next = X->next;\n2. If X->next != NULL: X->next->prev = X->prev;\n3. free(X);",
        "formula_rule_invariant": "Consistency Invariant: For any interior node X: `X->next->prev == X` and `X->prev->next == X`.",
        "common_mistakes_to_avoid": "Updating one direction pointer and forgetting the other (e.g., updating next but leaving prev pointing to old address).",
        "exam_writing_guidance": "Show 4 pointer adjustments for insertion between two nodes, and 2 pointer adjustments for deletion. Include diagrams with bidirectional arrows.",
        "quick_recall_block": {
            "trigger_words": ["Doubly linked list", "DLL", "Two-way list", "Delete node X without head"],
            "core_rule": "Every interior node has two pointers: `curr->next->prev = curr->prev` and `curr->prev->next = curr->next`.",
            "exam_checklist": ["struct DNode definition", "Bidirectional diagram", "O(1) deletion logic"]
        }
    },
    "M1_LL_DOUBLY_CIRCULAR": {
        "what_it_is": "A linked list combining both doubly linked and circular properties: head->prev points to the tail node, and tail->next points to the head node.",
        "why_it_exists": "Provides complete symmetric circularity in both forward and backward directions with zero NULL pointers. Ideal for circular buffers and music playlist queues.",
        "core_terminology": [
            {"term": "Doubly Circular Linked List (CDLL)", "def": "A doubly linked list where head->prev == tail and tail->next == head."},
            {"term": "Symmetric Invariant", "def": "Every node has both a valid predecessor and successor in a closed dual-loop."}
        ],
        "core_idea_and_intuition": "A carousel with mirrors: you can step forwards or backwards forever without ever falling off an edge.",
        "important_representations": "Diagram:\n`[Head] <===> [Node 2] <===> [Tail]` where Head->prev points to Tail and Tail->next points to Head.",
        "algorithm_procedure": "Insert at End in CDLL (given head):\n1. Allocate new_node.\n2. If head == NULL: new_node->next = new_node->prev = new_node; head = new_node;\n3. Else:\n   - tail = head->prev;\n   - new_node->next = head;\n   - new_node->prev = tail;\n   - tail->next = new_node;\n   - head->prev = new_node;\n4. Return head.",
        "formula_rule_invariant": "No NULL Invariant: In a non-empty CDLL, no pointer ever equals NULL.",
        "common_mistakes_to_avoid": "Setting pointers to NULL. A CDLL has strictly non-NULL circular links.",
        "exam_writing_guidance": "Clearly state: [Syllabus topic — no supplied question evidence in repository PYQs]. Present standard struct, pointer diagrams, and O(1) tail access logic.",
        "quick_recall_block": {
            "trigger_words": ["Doubly circular linked list", "CDLL", "Syllabus topic — no supplied question evidence"],
            "core_rule": "Dual circular links: `head->prev = tail` and `tail->next = head`. Zero NULL pointers.",
            "exam_checklist": ["Diagram showing circular links both ways", "Insertion algorithm", "Zero NULL pointers note"]
        }
    },
    "M1_LL_POLYNOMIAL": {
        "what_it_is": "Representing a polynomial by storing each non-zero term as an individual linked list node containing coefficient, exponent, and next pointer.",
        "why_it_exists": "Enables completely dynamic polynomial manipulation without pre-allocating an array sized to the highest power, perfectly handling arbitrarily sparse polynomials (e.g. 5x^10000 + 2).",
        "core_terminology": [
            {"term": "PolyNode", "def": "A node storing float coeff, int exp, and struct PolyNode* next."},
            {"term": "Ordered Exponents", "def": "Maintaining nodes in strictly descending order of exponents to enable O(n + m) linear addition."}
        ],
        "core_idea_and_intuition": "A chain of mathematical terms. Adding two polynomials is just like merging two sorted lists: combine terms with equal powers, or insert the higher power first.",
        "important_representations": "C Node Definition:\n```c\nstruct PolyNode {\n    float coeff;\n    int exp;\n    struct PolyNode* next;\n};\n```",
        "algorithm_procedure": "Polynomial Addition using Linked List:\n1. p1 = poly1, p2 = poly2, poly3 = NULL.\n2. While p1 != NULL and p2 != NULL:\n   - If p1->exp == p2->exp: add coeffs, if sum != 0 append to poly3; p1 = p1->next; p2 = p2->next;\n   - Else if p1->exp > p2->exp: append p1 term to poly3; p1 = p1->next;\n   - Else: append p2 term to poly3; p2 = p2->next;\n3. Append any remaining nodes from p1 or p2.",
        "formula_rule_invariant": "Time Complexity: O(m + n) where m and n are the number of non-zero terms in the two polynomials.",
        "common_mistakes_to_avoid": "Inserting zero coefficient results when terms cancel out (e.g. 3x^2 + (-3x^2) = 0).",
        "exam_writing_guidance": "Clearly state: [Syllabus topic — no supplied question evidence in repository PYQs]. Give the struct definition and the merge-style addition algorithm.",
        "quick_recall_block": {
            "trigger_words": ["Linked list polynomial", "Polynomial addition linked list", "Syllabus topic — no supplied question evidence"],
            "core_rule": "Each node = (coeff, exp, next). Addition = merge-walk comparing exponents.",
            "exam_checklist": ["struct PolyNode", "Three exponent comparison cases", "O(m+n) time complexity"]
        }
    },
    "M1_LL_APPLICATIONS": {
        "what_it_is": "Real-world engineering applications and structural trade-offs of linked lists compared to contiguous arrays.",
        "why_it_exists": "Guides software engineers in choosing linked lists when dynamic resizing and fast O(1) insertions/deletions outweigh cache locality and random access needs.",
        "core_terminology": [
            {"term": "Dynamic Memory Allocation", "def": "Growing and shrinking data structures at runtime on the heap."},
            {"term": "Pointer Overhead", "def": "Extra memory consumed by next/prev pointers (4 or 8 bytes per node)."},
            {"term": "Cache Locality", "def": "Array elements occupy adjacent memory blocks, maximizing CPU cache line hits, whereas linked list nodes are scattered."}
        ],
        "core_idea_and_intuition": "Use arrays when you know the size and need instant indexing A[i]. Use linked lists when size fluctuates continuously and you frequently insert or remove in the middle.",
        "important_representations": "Comparison Table:\n- Size: Array fixed; Linked List dynamic.\n- Access: Array O(1) random; Linked List O(n) sequential.\n- Insertion/Deletion: Array O(n) shifting; Linked List O(1) pointer updates if position known.\n- Memory: Array contiguous (no pointer overhead); Linked List non-contiguous (extra pointer storage).",
        "algorithm_procedure": "Key Applications of Linked Lists:\n1. Dynamic implementation of Stacks and Queues.\n2. Arithmetic on arbitrarily long integers and sparse polynomials.\n3. Memory management in OS (free memory block chains / free lists).\n4. Graph adjacency lists.",
        "formula_rule_invariant": "Memory Overhead Ratio: For an integer (4 bytes) in 64-bit OS (8-byte pointer), a singly linked list consumes 12 bytes (66.7% pointer overhead).",
        "common_mistakes_to_avoid": "Claiming linked list insertion is always O(1). Finding the position still takes O(n) unless a pointer to the location is already available.",
        "exam_writing_guidance": "Structure your answer with: (1) Array vs Linked List comparison table (4 parameters), (2) 4 distinct real-world applications.",
        "quick_recall_block": {
            "trigger_words": ["Applications of linked list", "Linked list vs array", "Advantage of linked list"],
            "core_rule": "Array = fast random access, static. Linked List = dynamic resizing, fast splice, pointer overhead.",
            "exam_checklist": ["Comparison table (Access, Insert, Memory, Size)", "Real-world applications list"]
        }
    },

    # --------------------------------------------------------------------------
    # MODULE 2: STACK AND QUEUE
    # --------------------------------------------------------------------------
    "M2_STACK_IMPL": {
        "what_it_is": "A linear data structure operating under the Last-In, First-Out (LIFO) discipline, supporting push (insertion), pop (deletion), and peek (top inspection) operations.",
        "why_it_exists": "Models nested, reversible operations such as function call activation records, undo mechanisms, and nested delimiter parsing.",
        "core_terminology": [
            {"term": "LIFO", "def": "Last-In, First-Out: the most recently inserted item is the first one removed."},
            {"term": "Top", "def": "The index or pointer referencing the most recently pushed item."},
            {"term": "Stack Overflow", "def": "Attempting to push an item onto a full stack (in fixed array implementation)."},
            {"term": "Stack Underflow", "def": "Attempting to pop an item from an empty stack (top == -1 or head == NULL)."}
        ],
        "core_idea_and_intuition": "A stack of dinner plates in a cafeteria: you add a new plate to the top, and you take a plate from the top.",
        "important_representations": "Array Implementation:\n- Empty condition: `top == -1`\n- Full condition: `top == MAX - 1`\n- Push: `stack[++top] = item`\n- Pop: `return stack[top--]`\nTwo Stacks in One Array: Stack 1 grows from 0 upwards (`top1++`), Stack 2 grows from MAX-1 downwards (`top2--`). Full when `top1 + 1 == top2`.",
        "algorithm_procedure": "Push Operation Algorithm:\n1. If top == MAX - 1: Print 'Stack Overflow' and exit.\n2. top = top + 1.\n3. stack[top] = value.\n4. Return success.",
        "formula_rule_invariant": "LIFO Invariant: For any sequence of operations, an element cannot be popped until all elements pushed after it have been popped.",
        "common_mistakes_to_avoid": "Writing `stack[top++]` instead of `stack[++top]` during push, which overwrites unadjusted memory.",
        "exam_writing_guidance": "Always give C code for both `push()` and `pop()`, explicitly including the Overflow and Underflow boundary checks.",
        "quick_recall_block": {
            "trigger_words": ["Stack implementation", "Push and Pop", "Stack overflow", "Two stacks one array"],
            "core_rule": "LIFO. Push: check `top == MAX-1`, then `++top`. Pop: check `top == -1`, then `top--`.",
            "exam_checklist": ["Empty/Full checks", "push() and pop() code", "Two stacks shared array condition"]
        }
    },
    "M2_STACK_APPLICATIONS": {
        "what_it_is": "Major algorithmic applications of the stack data structure: Infix to Postfix/Prefix conversion, Postfix evaluation, and Parenthesis matching.",
        "why_it_exists": "Enables compilers and calculators to eliminate operator precedence and parentheses ambiguities, processing arithmetic expressions linearly without backtracking.",
        "core_terminology": [
            {"term": "Infix", "def": "Operator between operands: A + B (human readable, requires precedence & brackets)."},
            {"term": "Postfix (Reverse Polish)", "def": "Operator after operands: A B + (parenthesis-free, easily evaluated via stack)."},
            {"term": "Prefix (Polish)", "def": "Operator before operands: + A B."},
            {"term": "Operator Precedence", "def": "Priority order: Parentheses () > Exponentiation ^ > Multiplicative *, / > Additive +, -."}
        ],
        "core_idea_and_intuition": "When converting infix to postfix: operands pass directly to the output. Operators wait on the stack until an operator of lower or equal precedence forces them to pop.",
        "important_representations": "Precedence Table:\n- `^`: Precedence 3, Right-to-Left associativity\n- `*`, `/`: Precedence 2, Left-to-Right associativity\n- `+`, `-`: Precedence 1, Left-to-Right associativity",
        "algorithm_procedure": "Infix to Postfix Conversion (Shunting-Yard):\n1. Scan infix from left to right.\n2. If operand: output directly.\n3. If '(': push to stack.\n4. If ')': pop and output until '(' is encountered; discard '('.\n5. If operator op: while stack not empty and precedence(top) ≥ precedence(op) [strict > if right-associative ^], pop and output top; push op.\n6. At end of expression: pop and output all remaining operators.",
        "formula_rule_invariant": "Postfix Evaluation Rule: When scanning postfix, push operands to stack. When operator is found, pop op2, then pop op1. Compute `res = op1 operator op2`, push res back.",
        "common_mistakes_to_avoid": "In postfix evaluation, popping operands in wrong order for non-commutative operations: `op2 = pop()`, `op1 = pop()`, then result is `op1 - op2` (NOT `op2 - op1`!).",
        "exam_writing_guidance": "In conversion and evaluation questions, always draw the complete 4-column execution table: [Symbol Scanned, Stack Status, Output/Action, Notes].",
        "quick_recall_block": {
            "trigger_words": ["Infix to postfix", "Postfix evaluation", "Reverse Polish notation", "Balanced parentheses"],
            "core_rule": "Conversion: Operands -> output; Operators -> stack (higher/equal precedence pops). Eval: operands -> stack, operator pops 2 operands (first popped is right operand!).",
            "exam_checklist": ["4-column trace table", "Operator precedence ranking", "Correct order of operands in subtraction/division"]
        }
    },
    "M2_QUEUE_LINEAR_CIRCULAR": {
        "what_it_is": "A linear data structure operating under the First-In, First-Out (FIFO) discipline. Linear queues suffer from memory leakage after deletions; Circular queues wrap around using modulo arithmetic to reuse empty slots.",
        "why_it_exists": "Models real-world waiting lines, resource buffering, and asynchronous request handling without starving early arrivals.",
        "core_terminology": [
            {"term": "FIFO", "def": "First-In, First-Out: the first element inserted is the first one removed."},
            {"term": "Front", "def": "Pointer/index from which elements are deleted (dequeued)."},
            {"term": "Rear", "def": "Pointer/index where elements are inserted (enqueued)."},
            {"term": "False Overflow", "def": "In linear queue, rear reaches MAX-1 but front has advanced, leaving unused empty slots at the front."},
            {"term": "Circular Queue", "def": "A queue where rear and front wrap around to 0 using modulo arithmetic: `(rear + 1) % MAX`."}
        ],
        "core_idea_and_intuition": "A cinema ticket queue: new people join at the back (rear), people who buy tickets leave from the front. In circular queue, the line wraps around the room in a ring.",
        "important_representations": "Circular Queue Indexing:\n- Empty condition: `front == -1 && rear == -1` (or `count == 0`)\n- Full condition: `(rear + 1) % MAX == front`\n- Enqueue: `rear = (rear + 1) % MAX; queue[rear] = item;` (if empty set `front = rear = 0`)\n- Dequeue: `item = queue[front]; if (front == rear) front = rear = -1; else front = (front + 1) % MAX;`",
        "algorithm_procedure": "Enqueue Algorithm in Circular Queue:\n1. If (rear + 1) % MAX == front: Print 'Queue Overflow' and exit.\n2. If front == -1: front = rear = 0;\n3. Else: rear = (rear + 1) % MAX;\n4. queue[rear] = value.",
        "formula_rule_invariant": "Circular Queue Capacity: In standard front/rear pointer representation without count variable, an array of size MAX holds at most MAX - 1 elements to distinguish full from empty.",
        "common_mistakes_to_avoid": "Writing linear increments `rear++` in circular queue instead of modular increment `(rear + 1) % MAX`.",
        "exam_writing_guidance": "Always explain: (1) Why linear queue has memory wastage ('false overflow'), (2) How circular queue solves it with modulo arithmetic, (3) Write exact C expressions for empty and full conditions.",
        "quick_recall_block": {
            "trigger_words": ["Circular queue", "Linear queue", "FIFO", "False overflow", "Enqueue and Dequeue"],
            "core_rule": "Circular Queue: Full is `(rear + 1) % MAX == front`. Empty is `front == -1` (or `front == rear`). Use `% MAX`.",
            "exam_checklist": ["Empty condition", "Full condition", "Modulo arithmetic explanation", "Step-by-step front/rear trace"]
        }
    },
    "M2_QUEUE_APPLICATIONS": {
        "what_it_is": "Key system and software applications of queues, including CPU process scheduling, I/O print spooling, disk request buffers, and Priority Queues.",
        "why_it_exists": "Queues decouple producers from consumers, smoothing out bursts of traffic when requests arrive faster than they can be processed.",
        "core_terminology": [
            {"term": "Print Spooling", "def": "Storing print jobs in a FIFO queue on disk until the printer is ready to print them."},
            {"term": "CPU Scheduling", "def": "Ready queues in operating systems (e.g. Round-Robin scheduling) holding runnable threads."},
            {"term": "Priority Queue", "def": "An extension of queue where each element has an assigned priority; elements with highest priority are dequeued before lower priority ones."}
        ],
        "core_idea_and_intuition": "When 10 users click 'Print' on the same office printer at the same second, the printer doesn't crash; it stores the 10 files in a FIFO queue and prints them one by one.",
        "important_representations": "Producer-Consumer Buffer diagram:\n`[Producer] ---> Enqueue ---> [ FIFO Buffer / Queue ] ---> Dequeue ---> [Consumer]`",
        "algorithm_procedure": "Round-Robin CPU Scheduling with Queue:\n1. Insert newly arriving processes at rear of ready queue.\n2. While queue is not empty:\n   - Dequeue process P from front.\n   - Run P for time quantum Q.\n   - If P has remaining execution time, Enqueue P at rear;\n   - Else terminate P.",
        "formula_rule_invariant": "Fairness Invariant: Under standard FIFO queuing with identical service times, wait time is directly proportional to arrival order.",
        "common_mistakes_to_avoid": "Confusing a Priority Queue (which serves by priority value) with a standard FIFO queue (which serves strictly by arrival order).",
        "exam_writing_guidance": "List at least 4 distinct real-world applications with 1-line explanations: (1) CPU Ready Queue, (2) Printer Spooling, (3) Asynchronous Data Buffering (e.g., IO buffers), (4) Breadth-First Search traversal buffer.",
        "quick_recall_block": {
            "trigger_words": ["Applications of queue", "Printer spooling", "CPU scheduling", "Priority queue"],
            "core_rule": "Queues manage asynchronous rate mismatch between producer and consumer.",
            "exam_checklist": ["4 real-world applications", "Spooling definition", "Priority queue concept"]
        }
    },
    "M2_DEQUE": {
        "what_it_is": "A Double-Ended Queue (Deque, pronounced 'deck') is a linear data structure in which insertions and deletions can be performed at both the front and rear ends.",
        "why_it_exists": "Provides a versatile generalized structure that can act as both a Stack (push/pop at same end) and a Queue (insert rear, delete front).",
        "core_terminology": [
            {"term": "Deque", "def": "Double-Ended Queue supporting insert_front, insert_rear, delete_front, and delete_rear."},
            {"term": "Input-Restricted Deque", "def": "Insertion allowed at only ONE end (usually rear), while deletions are allowed at BOTH ends (front and rear)."},
            {"term": "Output-Restricted Deque", "def": "Deletion allowed at only ONE end (usually front), while insertions are allowed at BOTH ends (front and rear)."}
        ],
        "core_idea_and_intuition": "A train track open at both ends: train cars can be attached or unhitched from either the front or the back.",
        "important_representations": "Classification Table:\n- General Deque: Insert Front, Insert Rear, Delete Front, Delete Rear.\n- Input-Restricted: Insert Rear ONLY; Delete Front & Delete Rear.\n- Output-Restricted: Insert Front & Insert Rear; Delete Front ONLY.",
        "algorithm_procedure": "Circular Array Deque Operations:\n- `insert_front(x)`: `front = (front - 1 + MAX) % MAX; deque[front] = x;`\n- `insert_rear(x)`: `rear = (rear + 1) % MAX; deque[rear] = x;`\n- `delete_front()`: `x = deque[front]; front = (front + 1) % MAX;`\n- `delete_rear()`: `x = deque[rear]; rear = (rear - 1 + MAX) % MAX;`",
        "formula_rule_invariant": "Wrap-around decrement: `(idx - 1 + MAX) % MAX` prevents negative indices in C modulo arithmetic.",
        "common_mistakes_to_avoid": "Swapping input-restricted and output-restricted definitions. Remember: 'Input-restricted' means restriction is on INPUT (only 1 insertion point).",
        "exam_writing_guidance": "Draw the 2-way box diagram with arrows. Explicitly define both Input-Restricted and Output-Restricted variants and show which operations are permitted.",
        "quick_recall_block": {
            "trigger_words": ["Deque", "Double ended queue", "Input restricted", "Output restricted"],
            "core_rule": "Input-Restricted = 1 end insert, 2 ends delete. Output-Restricted = 2 ends insert, 1 end delete.",
            "exam_checklist": ["Definition of general deque", "Input-Restricted rules", "Output-Restricted rules", "Circular array pointer updates"]
        }
    },
    "M2_REC_PRINCIPLES": {
        "what_it_is": "Recursion is a programming technique where a function calls itself directly or indirectly to solve a smaller instance of the same problem until a base condition is reached.",
        "why_it_exists": "Enables elegant, clean solutions for naturally recursive problems (divide-and-conquer, tree traversals, combinatorial backtracking) that would require complex manual state stacks if written iteratively.",
        "core_terminology": [
            {"term": "Base Case", "def": "The terminating condition that solves the smallest trivial subproblem directly without making further recursive calls."},
            {"term": "Recursive Step", "def": "The part of the function that divides the problem and invokes itself on smaller inputs."},
            {"term": "Activation Record (Stack Frame)", "def": "A memory block placed on the call stack storing function parameters, local variables, and the return address."},
            {"term": "Stack Overflow (Recursion)", "def": "Exhaustion of call stack memory caused by missing base case or excessively deep recursion."}
        ],
        "core_idea_and_intuition": "Russian nesting dolls: you open a big doll to find a slightly smaller doll inside, repeating until you reach the smallest solid doll (base case) that cannot be opened.",
        "important_representations": "Call Stack visualization for factorial(3):\n1. Push `fact(3)` -> calls `fact(2)`\n2. Push `fact(2)` -> calls `fact(1)`\n3. Push `fact(1)` -> base case returns 1\n4. Pop `fact(1)`, `fact(2)` returns 2*1 = 2\n5. Pop `fact(2)`, `fact(3)` returns 3*2 = 6.",
        "algorithm_procedure": "Designing a Recursive Function:\n1. Identify base case(s) where answer is immediately known.\n2. Express problem of size n in terms of size n-1 or n/2.\n3. Ensure recursive call progresses strictly towards the base case.",
        "formula_rule_invariant": "Recursion vs Iteration Comparison:\n- Speed: Iteration is faster (no stack frame push/pop overhead).\n- Space: Iteration uses O(1) auxiliary space; Recursion uses O(n) call stack space.\n- Code simplicity: Recursion is concise and natural for nested/hierarchical structures.",
        "common_mistakes_to_avoid": "Omitting the base condition or writing a recursive call that does not reduce the argument size, causing infinite recursion.",
        "exam_writing_guidance": "In code trace questions, draw the complete Call Stack diagram showing push operations on the way down and return values on the way up.",
        "quick_recall_block": {
            "trigger_words": ["Principles of recursion", "Recursion vs iteration", "Activation record", "Call stack", "Base condition"],
            "core_rule": "Every recursive function requires: (1) Base case to terminate, (2) Recursive case that shrinks input.",
            "exam_checklist": ["Base case + Recursive case definition", "Call stack trace diagram", "Recursion vs Iteration table"]
        }
    },
    "M2_REC_TAIL": {
        "what_it_is": "A recursive function is tail-recursive if the recursive self-call is the very last operation executed by the function, with no pending work or calculations remaining after the call returns.",
        "why_it_exists": "Enables Tail Call Optimization (TCO), where modern compilers reuse the existing stack frame instead of pushing a new one, reducing stack space from O(n) to O(1).",
        "core_terminology": [
            {"term": "Tail Recursion", "def": "A recursive call where nothing remains to be done after the call returns except returning the result."},
            {"term": "Non-Tail Recursion", "def": "A recursive call where operations (e.g. multiplication, addition) must be performed on the returned value."},
            {"term": "Accumulator", "def": "An auxiliary parameter used to carry the intermediate running result forward into the next recursive call."},
            {"term": "Tail Call Elimination", "def": "Compiler transformation converting tail-recursive calls into an efficient `while` loop."}
        ],
        "core_idea_and_intuition": "Non-tail: 'Go ask your friend, and when they answer, multiply it by 2' (you must wait). Tail: 'Go ask your friend with this running total, and their final answer will be the overall answer' (no waiting).",
        "important_representations": "Comparison:\n- Non-Tail Factorial: `return n * fact(n - 1);` (Multiplication is pending!)\n- Tail Factorial: `return fact_tail(n - 1, n * acc);` (No pending operation!)",
        "algorithm_procedure": "Converting Non-Tail to Tail Recursion:\n1. Introduce an accumulator parameter (e.g. `acc = 1` for multiplication, `acc = 0` for addition).\n2. Perform the arithmetic operation *before* the recursive call: pass `n * acc` as the new accumulator.\n3. When base case is reached, return `acc`.",
        "formula_rule_invariant": "Space Complexity: Standard recursion = O(n) stack frames. Tail recursion with TCO = O(1) stack space.",
        "common_mistakes_to_avoid": "Assuming `return fact(n-1) * n` is tail-recursive because the call is on the last line. The multiplication is still pending after `fact(n-1)` returns, so it is NON-tail.",
        "exam_writing_guidance": "Always show both versions side-by-side in C: (1) Non-tail `fact(n)`, (2) Tail-recursive `fact_tail(n, acc)`, and explain why the compiler can eliminate the call stack.",
        "quick_recall_block": {
            "trigger_words": ["Tail recursion", "Tail call optimization", "Eliminate tail recursion", "Accumulator"],
            "core_rule": "Tail recursion has ZERO pending operations after the self-call. Space drops from O(n) to O(1).",
            "exam_checklist": ["Definition of tail recursion", "Non-tail vs Tail code example", "Accumulator explanation", "O(1) space benefit"]
        }
    },
    "M2_REC_APPLICATIONS": {
        "what_it_is": "Classic algorithmic applications of recursion and backtracking: the Tower of Hanoi puzzle, the Eight Queens puzzle, and the general Backtracking paradigm.",
        "why_it_exists": "Demonstrates the power of recursive decomposition for complex combinatorial problems where iterative loops would be hopelessly convoluted.",
        "core_terminology": [
            {"term": "Tower of Hanoi", "def": "A mathematical puzzle with 3 rods and n disks of different sizes, moving all disks from source to destination rod without placing a larger disk on a smaller one."},
            {"term": "Backtracking", "def": "A systematic depth-first search strategy that builds candidate solutions incrementally, abandoning a candidate ('backtracking') as soon as it determines it cannot lead to a valid solution."},
            {"term": "Eight Queens Puzzle", "def": "Placing 8 non-attacking queens on an 8×8 chessboard such that no two queens share the same row, column, or diagonal."}
        ],
        "core_idea_and_intuition": "To move n disks from A to C using B:\n1. Move top n-1 disks from A to B (using C).\n2. Move largest nth disk directly from A to C.\n3. Move n-1 disks from B to C (using A).",
        "important_representations": "Tower of Hanoi Recurrence:\n- Recurrence: T(n) = 2·T(n-1) + 1, with T(1) = 1.\n- Closed Form: Total moves = 2^n - 1.\n- Time Complexity: O(2^n).",
        "algorithm_procedure": "C Tower of Hanoi Function:\n```c\nvoid TOH(int n, char from, char to, char aux) {\n    if (n == 1) {\n        printf(\"Move disk 1 from %c to %c\\n\", from, to);\n        return;\n    }\n    TOH(n - 1, from, aux, to);\n    printf(\"Move disk %d from %c to %c\\n\", n, from, to);\n    TOH(n - 1, aux, to, from);\n}\n```",
        "formula_rule_invariant": "Hanoi Rule: For n=3, moves = 2^3 - 1 = 7. For n=4, moves = 2^4 - 1 = 15.",
        "common_mistakes_to_avoid": "Swapping auxiliary and destination peg parameters in the second recursive call of Tower of Hanoi.",
        "exam_writing_guidance": "In Tower of Hanoi for n=3 or n=4, write the full 7 or 15 line move sequence: 'Move disk 1 from A to C', etc. For Eight Queens, explain the state-space tree pruning.",
        "quick_recall_block": {
            "trigger_words": ["Tower of Hanoi", "Eight Queens", "Backtracking", "2^n - 1 moves"],
            "core_rule": "TOH: Move n-1 to aux, move 1 to dest, move n-1 to dest. Total moves = 2^n - 1.",
            "exam_checklist": ["Recurrence relation T(n) = 2T(n-1)+1", "Closed form 2^n - 1", "C recursive code", "Complete move sequence trace"]
        }
    },

    # --------------------------------------------------------------------------
    # MODULE 4: SORTING
    # --------------------------------------------------------------------------
    "M4_SORT_BUBBLE": {
        "what_it_is": "A simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.",
        "why_it_exists": "Serves as the foundational introductory sorting algorithm; with early termination flag, it detects pre-sorted arrays in O(n) linear time.",
        "core_terminology": [
            {"term": "Bubble Sort", "def": "Sorting by swapping adjacent out-of-order elements; after pass i, the ith largest element bubbles up to its final position."},
            {"term": "Pass", "def": "One full traversal of the unsorted portion of the array from index 0 to n - 1 - i."},
            {"term": "Optimized / Modified Bubble Sort", "def": "Using a boolean swapped flag that terminates the algorithm immediately if a pass completes with zero swaps."},
            {"term": "Stability", "def": "A sorting algorithm is stable if elements with identical keys maintain their relative original order. Bubble Sort is STABLE."}
        ],
        "core_idea_and_intuition": "Heavier bubbles sink to the bottom, or larger values float up to the end of the array one pass at a time.",
        "important_representations": "Complexity:\n- Best Case (Already sorted, optimized): O(n) time, 0 swaps.\n- Worst Case (Reverse sorted): O(n^2) time, n(n-1)/2 swaps.\n- Average Case: O(n^2) time.\n- Space Complexity: O(1) auxiliary (in-place).",
        "algorithm_procedure": "Optimized Bubble Sort in C:\n```c\nvoid bubbleSort(int arr[], int n) {\n    for (int i = 0; i < n - 1; i++) {\n        int swapped = 0;\n        for (int j = 0; j < n - 1 - i; j++) {\n            if (arr[j] > arr[j + 1]) {\n                int temp = arr[j];\n                arr[j] = arr[j + 1];\n                arr[j + 1] = temp;\n                swapped = 1;\n            }\n        }\n        if (swapped == 0) break; // Early termination!\n    }\n}\n```",
        "formula_rule_invariant": "Pass Invariant: After pass i (0-indexed), the sub-array `arr[n - 1 - i .. n - 1]` contains the (i + 1) largest elements in their final sorted positions.",
        "common_mistakes_to_avoid": "Letting the inner loop run up to `n - 1` instead of `n - 1 - i`, doing redundant comparisons on already-sorted tail elements.",
        "exam_writing_guidance": "Always explain the optimization flag `swapped`. When asked to trace, show the array state after EVERY pass.",
        "quick_recall_block": {
            "trigger_words": ["Bubble sort", "Optimized bubble sort", "Swapped flag", "Stable sort"],
            "core_rule": "Compare adjacent elements. Pass i puts (i+1)th largest at end. Flag gives O(n) best case.",
            "exam_checklist": ["Inner loop limit n-1-i", "swapped flag early exit", "Best O(n), Worst O(n^2)", "Stable property"]
        }
    },
    "M4_SORT_COCKTAIL": {
        "what_it_is": "Cocktail Shaker Sort (Bidirectional Bubble Sort) is a variation of Bubble Sort that traverses the array alternately in both directions: left-to-right (bubbling largest to the end), then right-to-left (bubbling smallest to the beginning).",
        "why_it_exists": "Overcomes the 'turtle' problem in standard Bubble Sort, where small elements near the end of the array take many passes to crawl to the beginning.",
        "core_terminology": [
            {"term": "Cocktail Shaker Sort", "def": "Bidirectional bubble sort alternating forward and backward passes."},
            {"term": "Turtle", "def": "A small element positioned near the end of the array that moves towards the start very slowly in standard Bubble Sort."},
            {"term": "Rabbit", "def": "A large element near the start that moves quickly to the end."}
        ],
        "core_idea_and_intuition": "Shaking a cocktail back and forth: push the heaviest rock to the right, then immediately push the lightest feather to the left.",
        "important_representations": "Complexity:\n- Best Case (Already sorted): O(n) with swapped flag.\n- Worst Case (Reverse sorted): O(n^2).\n- Average Case: O(n^2).\n- Space: O(1) in-place.",
        "algorithm_procedure": "Cocktail Shaker Sort Steps:\n1. Set `start = 0`, `end = n - 1`, `swapped = 1`.\n2. While `swapped == 1`:\n   - `swapped = 0`\n   - Forward pass: for `i` from `start` to `end - 1`: if `arr[i] > arr[i+1]` swap and `swapped = 1`.\n   - If `swapped == 0` break;\n   - `end = end - 1`\n   - Backward pass: for `i` from `end - 1` down to `start`: if `arr[i] > arr[i+1]` swap and `swapped = 1`.\n   - `start = start + 1`.",
        "formula_rule_invariant": "Bound Invariant: After each complete forward-and-backward cycle, both `start` advances right and `end` shrinks left.",
        "common_mistakes_to_avoid": "Forgetting to update `end--` after forward pass and `start++` after backward pass.",
        "exam_writing_guidance": "Explain the concept of 'turtles and rabbits' and show both the forward pass and backward pass clearly.",
        "quick_recall_block": {
            "trigger_words": ["Cocktail shaker sort", "Bidirectional bubble sort", "Turtles and rabbits"],
            "core_rule": "Alternates: Forward pass bubbles largest to right; Backward pass bubbles smallest to left.",
            "exam_checklist": ["Bidirectional mechanism", "start++ and end-- bounds", "Turtle problem explanation", "O(n) best / O(n^2) worst"]
        }
    },
    "M4_SORT_INSERTION": {
        "what_it_is": "An efficient in-place comparison sort that builds the final sorted array one item at a time, by repeatedly taking the next unsorted element and inserting it into its correct position within the already-sorted prefix.",
        "why_it_exists": "Highly efficient for small arrays (n ≤ 50) and nearly sorted data; runs in O(n) best-case time and is online (can sort a stream of data as it arrives).",
        "core_terminology": [
            {"term": "Key", "def": "The current element being inserted into the sorted subarray."},
            {"term": "Sorted Subarray", "def": "The prefix `arr[0 .. i - 1]` which is maintained in sorted order at the start of iteration i."},
            {"term": "Inversion", "def": "A pair of elements (arr[i], arr[j]) such that i < j but arr[i] > arr[j]. Insertion sort swaps equal the number of inversions."}
        ],
        "core_idea_and_intuition": "Sorting playing cards in your hand: you pick a card from the deck, slide it past cards that are greater, and drop it into its proper spot.",
        "important_representations": "Three-Case Complexity Analysis:\n- Best Case (Already sorted): Loop body executes 0 times. Exactly (n - 1) comparisons, 0 shifts. Time = O(n).\n- Worst Case (Reverse sorted): Element i compares against all i elements. Total comparisons = ∑_{i=1}^{n-1} i = n(n-1)/2. Time = O(n^2).\n- Average Case (Random array): On average, element i compares against i/2 elements. Total comparisons ≈ n(n-1)/4. Time = O(n^2).",
        "algorithm_procedure": "Insertion Sort in C:\n```c\nvoid insertionSort(int arr[], int n) {\n    for (int i = 1; i < n; i++) {\n        int key = arr[i];\n        int j = i - 1;\n        while (j >= 0 && arr[j] > key) {\n            arr[j + 1] = arr[j]; // Shift right\n            j--;\n        }\n        arr[j + 1] = key; // Insert key\n    }\n}\n```",
        "formula_rule_invariant": "Loop Invariant: At the start of each iteration of the outer loop, the subarray `arr[0 .. i - 1]` consists of the elements originally in `arr[0 .. i - 1]`, but in sorted order.",
        "common_mistakes_to_avoid": "Writing `arr[j] >= key` instead of `arr[j] > key`, which destroys the stability of the sort.",
        "exam_writing_guidance": "The syllabus explicitly mandates Best, Worst, and Average case analysis! Always write the summation: Best = O(n), Worst = ∑ i = n(n-1)/2 = O(n^2), Average = ∑ (i/2) = n(n-1)/4 = O(n^2).",
        "quick_recall_block": {
            "trigger_words": ["Insertion sort", "Best-case analysis", "Worst-case analysis", "Average-case analysis", "Playing cards"],
            "core_rule": "Insert key into sorted prefix. Best O(n), Worst O(n^2), Avg O(n^2). Stable and in-place.",
            "exam_checklist": ["C code with key & shift", "Loop invariant statement", "Explicit math for all 3 cases"]
        }
    },
    "M4_SORT_SELECTION": {
        "what_it_is": "An in-place comparison sort that divides the array into a sorted prefix and an unsorted suffix. In each pass, it finds the smallest element in the unsorted suffix and swaps it with the first unsorted element.",
        "why_it_exists": "Minimizes memory writes: Selection Sort performs at most O(n) swaps (exactly n - 1 swaps in total), making it useful when write operations are extremely costly (e.g., Flash EEPROM memory).",
        "core_terminology": [
            {"term": "min_idx", "def": "Index of the smallest element discovered in the current unsorted suffix."},
            {"term": "Selection Pass", "def": "Scanning from i+1 to n-1 to find the minimum and performing a single swap with index i."},
            {"term": "Unstable Sort", "def": "Selection Sort is UNSTABLE by default due to long-distance swaps (e.g. [4a, 4b, 2] -> [2, 4b, 4a])."}
        ],
        "core_idea_and_intuition": "Scan the entire unsorted crowd, find the shortest person, and swap them into the first spot. Repeat for the second spot.",
        "important_representations": "Complexity:\n- Best Case: O(n^2) comparisons, O(1) swaps.\n- Worst Case: O(n^2) comparisons, O(n) swaps.\n- Average Case: O(n^2) comparisons, O(n) swaps.\n- Total Comparisons: Always exactly n(n-1)/2 in ALL cases!",
        "algorithm_procedure": "Selection Sort in C:\n```c\nvoid selectionSort(int arr[], int n) {\n    for (int i = 0; i < n - 1; i++) {\n        int min_idx = i;\n        for (int j = i + 1; j < n; j++) {\n            if (arr[j] < arr[min_idx])\n                min_idx = j;\n        }\n        if (min_idx != i) {\n            int temp = arr[i];\n            arr[i] = arr[min_idx];\n            arr[min_idx] = temp;\n        }\n    }\n}\n```",
        "formula_rule_invariant": "Comparisons Invariant: Selection sort always makes exactly n(n-1)/2 comparisons regardless of initial array ordering.",
        "common_mistakes_to_avoid": "Claiming Selection Sort runs in O(n) on sorted arrays. It still scans the remaining array to verify the minimum, taking O(n^2) comparisons.",
        "exam_writing_guidance": "Emphasize: Comparisons are always O(n^2), but swaps are strictly O(n) (at most n-1 swaps). Show array state after each pass.",
        "quick_recall_block": {
            "trigger_words": ["Selection sort", "Minimum swaps", "Unstable sorting", "Pass trace"],
            "core_rule": "Find minimum in unsorted remainder, swap once. Comparisons = n(n-1)/2 always. Swaps ≤ n-1.",
            "exam_checklist": ["min_idx search loop", "Single swap per pass", "Always O(n^2) comparisons", "Unstable explanation"]
        }
    },
    "M4_SORT_HEAPIFY": {
        "what_it_is": "Max-Heapify is the procedure that restores the max-heap property at a subtree rooted at index i. Build-Max-Heap is the linear-time algorithm that converts an arbitrary array into a valid Max-Heap.",
        "why_it_exists": "Provides the foundational building block for Heap data structures and priority queues, running in guaranteed O(n) construction time.",
        "core_terminology": [
            {"term": "Max-Heap Property", "def": "For every node i other than the root: A[parent(i)] ≥ A[i]. The maximum element is always at the root."},
            {"term": "Complete Binary Tree", "def": "A binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible."},
            {"term": "Array Indexing (1-based)", "def": "parent(i) = ⌊i/2⌋, left_child(i) = 2i, right_child(i) = 2i + 1."},
            {"term": "Array Indexing (0-based)", "def": "parent(i) = ⌊(i - 1)/2⌋, left_child(i) = 2i + 1, right_child(i) = 2i + 2."},
            {"term": "Leaves in Array", "def": "In an n-element heap (1-based), leaves are indexed from ⌊n/2⌋ + 1 to n."}
        ],
        "core_idea_and_intuition": "Max-Heapify floats a small value down the tree by repeatedly swapping it with its largest child until the heap property is satisfied. Build-Max-Heap calls Max-Heapify from the last non-leaf node down to the root.",
        "important_representations": "Tree vs Array correspondence:\nRoot is at index 1 (or 0). Array stores levels sequentially without pointers.",
        "algorithm_procedure": "Max-Heapify (1-based, array A, size n, node i):\n1. l = 2*i, r = 2*i + 1, largest = i.\n2. If l ≤ n and A[l] > A[largest]: largest = l.\n3. If r ≤ n and A[r] > A[largest]: largest = r.\n4. If largest != i:\n   - Swap A[i] and A[largest];\n   - Max-Heapify(A, n, largest);\n\nBuild-Max-Heap(A, n):\n1. For i = ⌊n/2⌋ down to 1: Max-Heapify(A, n, i).",
        "formula_rule_invariant": "O(n) Linear Time Proof:\nTime = ∑_{h=0}^{⌊log n⌋} ⌈n/2^{h+1}⌉ · O(h) = O(n · ∑_{h=0}^∞ h/2^h). Since ∑_{h=0}^∞ h/2^h = 2, total time is O(n · 2) = O(n).",
        "common_mistakes_to_avoid": "Starting Build-Max-Heap from 1 up to n instead of from ⌊n/2⌋ down to 1.",
        "exam_writing_guidance": "In construction questions, draw the complete binary tree at each step of Build-Max-Heap as each non-leaf node is heapified. Show the mathematical summation for the O(n) proof.",
        "quick_recall_block": {
            "trigger_words": ["Max-Heapify", "Build-Max-Heap", "Heap property", "Parent/child indices", "O(n) heap build proof"],
            "core_rule": "1-based: left = 2i, right = 2i+1, parent = i/2. Build-Max-Heap runs i = n/2 down to 1 in O(n) time.",
            "exam_checklist": ["Parent/child indexing formulas", "Max-Heapify pseudocode", "Build-Max-Heap loop (n/2 down to 1)", "O(n) summation proof"]
        }
    },
    "M4_SORT_QUICK": {
        "what_it_is": "A divide-and-conquer sorting algorithm that partitions an array around a selected pivot element such that elements smaller than the pivot are placed to its left and larger elements to its right, then recursively sorts the subarrays.",
        "why_it_exists": "One of the most practical and fastest in-memory general-purpose sorting algorithms, with excellent cache performance and in-place partitioning.",
        "core_terminology": [
            {"term": "Pivot", "def": "The reference element chosen from the array around which partitioning is performed."},
            {"term": "Partitioning", "def": "Rearranging array elements so that all elements < pivot precede it, and all elements > pivot follow it."},
            {"term": "Lomuto Partition", "def": "Uses pivot as the last element and a single scanner index to partition in one forward pass."},
            {"term": "Hoare Partition", "def": "Uses two pointer indices starting from both ends moving towards each other; faster with fewer swaps than Lomuto."}
        ],
        "core_idea_and_intuition": "Pick a benchmark student in class: send everyone shorter than them to the left, everyone taller to the right. The benchmark student is now in their permanent spot.",
        "important_representations": "Partitioning State:\n`[ Elements ≤ Pivot ] [ Pivot in Final Spot ] [ Elements ≥ Pivot ]`",
        "algorithm_procedure": "Lomuto Partition Algorithm (A, low, high):\n1. pivot = A[high]\n2. i = low - 1\n3. for j = low to high - 1:\n   - if A[j] <= pivot:\n       i = i + 1\n       swap A[i] with A[j]\n4. swap A[i + 1] with A[high]\n5. return (i + 1)\n\nQuickSort(A, low, high):\n1. if low < high:\n   - pi = Partition(A, low, high)\n   - QuickSort(A, low, pi - 1)\n   - QuickSort(A, pi + 1, high)",
        "formula_rule_invariant": "Partition Invariant: At return, `A[pi]` is in its final sorted position and will never be moved again.",
        "common_mistakes_to_avoid": "Writing a full recurrence complexity derivation! NOTE: Quick Sort complexity analysis is explicitly OUT OF SCOPE per controlling syllabus. Do not write T(n) = 2T(n/2) + cn derivations.",
        "exam_writing_guidance": "Focus on the Partitioning Algorithm: Explain pivot choice, write clean C/pseudocode for Partition, and show a step-by-step dry run on a sample array.",
        "quick_recall_block": {
            "trigger_words": ["Quick sort", "Partition algorithm", "Pivot", "Lomuto", "Hoare", "Without complexity analysis"],
            "core_rule": "Divide-and-conquer: Partition puts pivot in final spot. Recurse left and right. Complexity derivation is locked out!",
            "exam_checklist": ["Partition algorithm pseudocode", "Pivot selection", "Step-by-step trace of pointers i and j", "No complexity analysis needed"]
        }
    },

    # --------------------------------------------------------------------------
    # MODULE 4: SEARCHING
    # --------------------------------------------------------------------------
    "M4_SEARCH_SEQUENTIAL": {
        "what_it_is": "Sequential Search (Linear Search) checks each element of a list sequentially from beginning to end until the target key is found or the end of the list is reached.",
        "why_it_exists": "The only searching algorithm that works on completely unordered / unsorted data and arbitrary linked lists without extra preprocessing.",
        "core_terminology": [
            {"term": "Linear Search", "def": "Examining items one by one in sequence."},
            {"term": "Sentinel Search", "def": "Placing the target key at the end of the array to eliminate the loop index boundary check `i < n` on every step."},
            {"term": "Average Case Comparisons", "def": "Under uniform probability of successful search, expected comparisons = (n + 1) / 2. If target appears twice, expected comparisons = (n + 1) / 3."}
        ],
        "core_idea_and_intuition": "Looking for your lost keys: you look on table 1, then table 2, then shelf 3, until you find them or run out of places.",
        "important_representations": "Complexity:\n- Best Case: O(1) (key found at index 0).\n- Worst Case: O(n) (key at index n-1 or not present).\n- Average Case: (n + 1)/2 comparisons = O(n).\n- Space: O(1) auxiliary.",
        "algorithm_procedure": "Sentinel Linear Search in C:\n```c\nint sentinelSearch(int arr[], int n, int key) {\n    int last = arr[n - 1];\n    arr[n - 1] = key; // Place sentinel\n    int i = 0;\n    while (arr[i] != key)\n        i++;\n    arr[n - 1] = last; // Restore\n    if (i < n - 1 || last == key)\n        return i; // Found\n    return -1; // Not found\n}\n```",
        "formula_rule_invariant": "Average Case Derivation: E[C] = ∑_{i=1}^n i · P(i) = ∑_{i=1}^n i · (1/n) = (1/n) · [n(n+1)/2] = (n + 1) / 2.",
        "common_mistakes_to_avoid": "Forgetting that linear search is O(n) average and worst case. Missing the sentinel technique when asked how to optimize the loop.",
        "exam_writing_guidance": "When asked for average case, write out the discrete expectation formula E = (1/n) ∑ i = (n+1)/2. For twice-occurring items, write E = (n+1)/3.",
        "quick_recall_block": {
            "trigger_words": ["Sequential search", "Linear search", "Sentinel", "Expected comparisons (n+1)/2"],
            "core_rule": "Sequential check from start to end. Works on unsorted data. Expected comparisons = (n+1)/2.",
            "exam_checklist": ["Sequential search C code", "Average case expectation derivation", "Sentinel optimization"]
        }
    },
    "M4_SEARCH_BINARY": {
        "what_it_is": "A fast divide-and-conquer search algorithm that repeatedly divides a sorted search interval in half by comparing the target key with the middle element.",
        "why_it_exists": "Provides ultra-fast O(log n) logarithmic searching on sorted data, requiring at most 30 comparisons even in an array of 1 billion items.",
        "core_terminology": [
            {"term": "Sorted Precondition", "def": "Binary search REQUIRES the input array to be sorted beforehand."},
            {"term": "Mid Calculation", "def": "`mid = low + (high - low) / 2` (prevents integer overflow compared to `(low + high) / 2`)."},
            {"term": "Decision Tree", "def": "A binary tree representing all possible comparison paths of binary search on n items, having height ⌊log2 n⌋ + 1."}
        ],
        "core_idea_and_intuition": "Guessing a secret number between 1 and 100: you guess 50. If told 'higher', you eliminate 1 to 50 in one step and test 75.",
        "important_representations": "Complexity:\n- Best Case: O(1) (key found at initial mid).\n- Worst Case: ⌊log2 n⌋ + 1 comparisons = O(log n).\n- Average Case: O(log n).\n- Space: Iterative is O(1); Recursive is O(log n) stack space.",
        "algorithm_procedure": "Iterative Binary Search in C:\n```c\nint binarySearch(int arr[], int n, int key) {\n    int low = 0, high = n - 1;\n    while (low <= high) {\n        int mid = low + (high - low) / 2;\n        if (arr[mid] == key)\n            return mid;\n        else if (arr[mid] < key)\n            low = mid + 1;\n        else\n            high = mid - 1;\n    }\n    return -1; // Not found\n}\n```",
        "formula_rule_invariant": "Recurrence for Worst-Case: T(n) = T(n/2) + 1, with T(1) = 1. Solution: T(n) = ⌊log2 n⌋ + 1 = O(log n).",
        "common_mistakes_to_avoid": "Writing `mid = (low + high) / 2` which can cause integer overflow in 32-bit systems when `low + high > INT_MAX`.",
        "exam_writing_guidance": "The syllabus explicitly mandates Worst-case and Average-case analysis! Show the recurrence relation `T(n) = T(n/2) + 1` and draw the decision tree.",
        "quick_recall_block": {
            "trigger_words": ["Binary search", "Worst-case analysis", "Average-case analysis", "Sorted array", "mid calculation"],
            "core_rule": "Array MUST be sorted. Compare mid: discard half each step. Time = O(log n) worst and average.",
            "exam_checklist": ["Precondition (sorted array)", "mid formula with overflow protection", "Worst-case recurrence derivation", "Decision tree height"]
        }
    },
    "M4_SEARCH_INTERPOLATION": {
        "what_it_is": "An improved search algorithm for uniformly distributed sorted arrays that estimates the probable position of the search key based on its numerical value, similar to opening a phonebook.",
        "why_it_exists": "Achieves O(log log n) average search time on uniformly distributed data, outperforming standard binary search on large datasets.",
        "core_terminology": [
            {"term": "Probe Position", "def": "The computed index where key is estimated to reside: pos = low + ⌊((key - arr[low]) · (high - low)) / (arr[high] - arr[low])⌋."},
            {"term": "Uniform Distribution", "def": "Precondition where values increase at a roughly constant rate across array indices."},
            {"term": "O(log log n)", "def": "Extremely fast sub-logarithmic average time complexity."}
        ],
        "core_idea_and_intuition": "When opening a dictionary to look up 'Zebra', you don't open to the middle (letter M); you open near the very back. Interpolation search does the same with numerical values.",
        "important_representations": "Slope Formula Derivation:\n`(pos - low) / (high - low) = (key - arr[low]) / (arr[high] - arr[low])`\nSolving for pos gives:\n`pos = low + [ (key - arr[low]) / (arr[high] - arr[low]) ] · (high - low)`",
        "algorithm_procedure": "Interpolation Search in C:\n```c\nint interpolationSearch(int arr[], int n, int key) {\n    int low = 0, high = n - 1;\n    while (low <= high && key >= arr[low] && key <= arr[high]) {\n        if (low == high) {\n            if (arr[low] == key) return low;\n            return -1;\n        }\n        int pos = low + (((double)(high - low) / (arr[high] - arr[low])) * (key - arr[low]));\n        if (arr[pos] == key)\n            return pos;\n        if (arr[pos] < key)\n            low = pos + 1;\n        else\n            high = pos - 1;\n    }\n    return -1;\n}\n```",
        "formula_rule_invariant": "Complexity:\n- Average Case (Uniform distribution): O(log(log n)).\n- Worst Case (Exponential distribution e.g. [1, 2, 4, 8, 16, ...]): O(n).",
        "common_mistakes_to_avoid": "Forgetting the range check `key >= arr[low] && key <= arr[high]`, which can cause probe index `pos` to calculate outside array bounds `[0..n-1]`.",
        "exam_writing_guidance": "Write the exact probe position formula, show its linear interpolation derivation from the slope equation, and contrast O(log log n) average vs O(n) worst case.",
        "quick_recall_block": {
            "trigger_words": ["Interpolation search", "Probe formula", "Uniform distribution", "O(log log n)"],
            "core_rule": "Probe formula: `pos = low + [(key - arr[low])*(high - low)] / (arr[high] - arr[low])`. Avg O(log log n), Worst O(n).",
            "exam_checklist": ["Probe position formula", "Linear interpolation derivation", "Uniform distribution requirement", "O(log log n) vs O(n)"]
        }
    }
}

# Assemble complete pedagogical dataset for all syllabus topics
pedagogical_content_list = []

for mod in syllabus["modules"]:
    mod_id = mod["module_id"]
    mod_num = mod["module_number"]
    for sec in mod["sections"]:
        for top in sec["topics"]:
            tid = top["topic_id"]
            title = top["topic_title"]
            linked_fams = fams_by_topic.get(tid, [])
            
            # Evidence status
            if len(linked_fams) == 0:
                evidence_status = "NO_SUPPLIED_QUESTION_EVIDENCE"
                evidence_label = "Syllabus topic — no supplied question evidence"
                example_qa = {
                    "note": "Syllabus topic — no supplied question evidence in repository source corpus.",
                    "question_text": "Syllabus topic — no supplied question evidence",
                    "solution_walkthrough": "Conceptual pedagogical walkthrough provided based on syllabus specification."
                }
            else:
                evidence_status = "SUPPLIED_SOURCE_EVIDENCE"
                evidence_label = f"Covered by {sum(f['occurrence_count'] for f in linked_fams)} source questions across {len(linked_fams)} families"
                rep_fam = linked_fams[0]
                example_qa = {
                    "representative_family_id": rep_fam["family_id"],
                    "representative_family_title": rep_fam["canonical_title"],
                    "question_instance_id": rep_fam["representative_question_instance_id"],
                    "question_text": rep_fam["representative_text"],
                    "source_document": rep_fam["representative_document_id"],
                    "page": rep_fam["representative_page"]
                }
                
            p_data = PEDAGOGY_DATA.get(tid, {
                "what_it_is": f"Core data structures concept covering {title}.",
                "why_it_exists": "Essential for organizing data and executing operations within defined computational bounds.",
                "core_terminology": [{"term": title, "def": "Core syllabus topic."}],
                "core_idea_and_intuition": f"Understanding how {title} operates and why it is chosen.",
                "important_representations": "Standard memory and logical representations.",
                "algorithm_procedure": "Procedural step-by-step definition.",
                "formula_rule_invariant": "Core algorithmic invariant.",
                "common_mistakes_to_avoid": "Common implementation or conceptual errors.",
                "exam_writing_guidance": "Key points required for full marks in semester examinations.",
                "quick_recall_block": {
                    "trigger_words": [title],
                    "core_rule": "Key syllabus concept.",
                    "exam_checklist": ["Definition", "Algorithm", "Complexity"]
                }
            })
            
            record = {
                "topic_id": tid,
                "topic_title": title,
                "module_id": mod_id,
                "module_number": mod_num,
                "section_id": sec["section_id"],
                "section_title": sec["section_title"],
                "evidence_status": evidence_status,
                "evidence_label": evidence_label,
                "1_what_it_is": p_data["what_it_is"],
                "2_why_it_exists": p_data["why_it_exists"],
                "3_core_terminology": p_data["core_terminology"],
                "4_core_idea_and_intuition": p_data["core_idea_and_intuition"],
                "5_important_representations": p_data["important_representations"],
                "6_algorithm_procedure": p_data["algorithm_procedure"],
                "7_example_with_source_question": example_qa,
                "8_formula_rule_invariant": p_data["formula_rule_invariant"],
                "9_common_mistakes_to_avoid": p_data["common_mistakes_to_avoid"],
                "10_exam_writing_guidance": p_data["exam_writing_guidance"],
                "11_linked_question_families": [
                    {"family_id": f["family_id"], "title": f["canonical_title"], "count": f["occurrence_count"]}
                    for f in linked_fams
                ],
                "12_quick_recall_block": p_data["quick_recall_block"]
            }
            pedagogical_content_list.append(record)

print(f"Generated pedagogical content for {len(pedagogical_content_list)} syllabus topics.")

with open('PEDAGOGICAL_CONTENT.json', 'w', encoding='utf-8') as f:
    json.dump(pedagogical_content_list, f, indent=2, ensure_ascii=False)

print("Saved PEDAGOGICAL_CONTENT.json successfully.")
