import json
import os
import sys
import re
from collections import defaultdict, Counter

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# 1. CONTROLLING SYLLABUS SPECIFICATION
# ==============================================================================

SYLLABUS_METADATA = {
    "course_code": "CSE2101 / CSEN2101",
    "course_title": "Data Structures and Algorithms",
    "provenance": "user_supplied_syllabus_image",
    "source_type": "user_supplied_syllabus_image",
    "controlling_source": "User-supplied syllabus image provided in current conversation",
    "hierarchy_status": "LEVEL_1_CONTROLLING",
    "institutional_verification_note": "Recorded as user_supplied_syllabus_image per system policy; no false claim of independent institutional verification.",
    "hard_scope_lock": {
        "in_scope_modules": ["MODULE_1", "MODULE_2", "MODULE_4"],
        "out_of_scope_modules": ["MODULE_3"],
        "module_4_restrictions": "Locked whitelist only. Quick Sort complexity analysis is strictly OUT OF SCOPE. Non-whitelisted sorting algorithms (Merge, Shell, Radix, Bucket, Counting) and external hashing/trees are strictly OUT OF SCOPE."
    }
}

MODULES_SPEC = [
    {
        "module_id": "MODULE_1",
        "module_number": 1,
        "module_title": "Introduction, Array, and Linked List",
        "lecture_hours": "10L",
        "scope_status": "FULL_IN_SCOPE",
        "sections": [
            {
                "section_id": "M1_SEC_INTRO",
                "section_title": "INTRODUCTION",
                "topics": [
                    {
                        "topic_id": "M1_INTRO_NEED",
                        "topic_title": "Why do we need data structure?",
                        "syllabus_wording": "Why do we need data structure?",
                        "keywords": ["need data structure", "why data structure", "importance of data structure", "definition of data structure"]
                    },
                    {
                        "topic_id": "M1_INTRO_CONCEPTS",
                        "topic_title": "Concepts of data structures: Data, Data structure, Abstract Data Type (ADT) and Data Type",
                        "syllabus_wording": "Concepts of data structures: a) Data and data structure b) Abstract Data Type and Data Type",
                        "keywords": ["abstract data type", "adt", "data type", "data and data structure", "primitive vs non-primitive", "linear vs non-linear", "linear data structure", "non-linear data structure"]
                    },
                    {
                        "topic_id": "M1_INTRO_ALGO_PROG",
                        "topic_title": "Algorithms and programs, basic idea of pseudo-code",
                        "syllabus_wording": "Algorithms and programs; Basic idea of pseudo-code",
                        "keywords": ["algorithm and program", "difference between algorithm and program", "pseudo-code", "pseudocode", "characteristics of algorithm"]
                    },
                    {
                        "topic_id": "M1_INTRO_EFFICIENCY",
                        "topic_title": "Algorithm efficiency and analysis: Time and space analysis of algorithms",
                        "syllabus_wording": "Algorithm efficiency and analysis; Time and space analysis of algorithms",
                        "keywords": ["algorithm efficiency", "time complexity", "space complexity", "time and space analysis", "frequency count", "step count"]
                    },
                    {
                        "topic_id": "M1_INTRO_ASYMPTOTIC",
                        "topic_title": "Asymptotic notations: Big O, Ω, Θ notations",
                        "syllabus_wording": "Big O, Ω, Θ notations",
                        "keywords": ["big o", "big-o", "omega", "theta", "asymptotic notation", "asymptotic analysis", "order of growth", "tight bound"]
                    }
                ]
            },
            {
                "section_id": "M1_SEC_ARRAY",
                "section_title": "ARRAY",
                "topics": [
                    {
                        "topic_id": "M1_ARRAY_REPRESENTATION",
                        "topic_title": "Different representations: Row major and Column major order",
                        "syllabus_wording": "Different representations: Row major, Column major",
                        "keywords": ["row major", "column major", "address calculation", "2d array address", "base address", "upper triangular matrix", "symmetric matrix"]
                    },
                    {
                        "topic_id": "M1_ARRAY_SPARSE",
                        "topic_title": "Sparse matrix: implementation and usage",
                        "syllabus_wording": "Sparse matrix: implementation and usage",
                        "keywords": ["sparse matrix", "triplet representation", "3-tuple", "sparse matrix transpose", "fast transpose"]
                    },
                    {
                        "topic_id": "M1_ARRAY_POLYNOMIAL",
                        "topic_title": "Array representation of polynomials",
                        "syllabus_wording": "Array representation of polynomials",
                        "keywords": ["array representation of polynomial", "polynomial representation using array", "polynomial addition using array"]
                    }
                ]
            },
            {
                "section_id": "M1_SEC_LINKED_LIST",
                "section_title": "LINKED LIST",
                "topics": [
                    {
                        "topic_id": "M1_LL_SINGLY",
                        "topic_title": "Singly linked list (creation, insertion, deletion, traversal, reversal)",
                        "syllabus_wording": "Singly linked list",
                        "keywords": ["singly linked list", "single linked list", "insert in linked list", "delete from linked list", "reverse linked list"]
                    },
                    {
                        "topic_id": "M1_LL_CIRCULAR",
                        "topic_title": "Circular linked list",
                        "syllabus_wording": "Circular linked list",
                        "keywords": ["circular linked list", "circular singly linked list", "cll"]
                    },
                    {
                        "topic_id": "M1_LL_DOUBLY",
                        "topic_title": "Doubly linked list",
                        "syllabus_wording": "Doubly linked list",
                        "keywords": ["doubly linked list", "double linked list", "dll"]
                    },
                    {
                        "topic_id": "M1_LL_DOUBLY_CIRCULAR",
                        "topic_title": "Doubly circular linked list",
                        "syllabus_wording": "Doubly circular linked list",
                        "keywords": ["doubly circular linked list", "circular doubly linked list", "cdll"]
                    },
                    {
                        "topic_id": "M1_LL_POLYNOMIAL",
                        "topic_title": "Linked list representation of polynomial",
                        "syllabus_wording": "Linked list representation of polynomial",
                        "keywords": ["polynomial using linked list", "linked list representation of polynomial", "polynomial addition using linked list"]
                    },
                    {
                        "topic_id": "M1_LL_APPLICATIONS",
                        "topic_title": "Applications of linked list",
                        "syllabus_wording": "Applications",
                        "keywords": ["applications of linked list", "advantage of linked list over array", "linked list applications"]
                    }
                ]
            }
        ]
    },
    {
        "module_id": "MODULE_2",
        "module_number": 2,
        "module_title": "Stack, Queue, and Recursion",
        "lecture_hours": "10L",
        "scope_status": "FULL_IN_SCOPE",
        "sections": [
            {
                "section_id": "M2_SEC_STACK_QUEUE",
                "section_title": "STACK AND QUEUE",
                "topics": [
                    {
                        "topic_id": "M2_STACK_IMPL",
                        "topic_title": "Stack: implementation using array and linked list",
                        "syllabus_wording": "Stack; Stack implementation using array; Stack implementation using linked list",
                        "keywords": ["stack", "push", "pop", "peek", "stack using array", "stack using linked list", "stack overflow", "stack underflow"]
                    },
                    {
                        "topic_id": "M2_STACK_APPLICATIONS",
                        "topic_title": "Applications of stack: Infix/Postfix/Prefix conversion, evaluation, parenthesis matching",
                        "syllabus_wording": "Applications",
                        "keywords": ["infix to postfix", "infix to prefix", "postfix evaluation", "prefix evaluation", "parenthesis matching", "balanced parentheses"]
                    },
                    {
                        "topic_id": "M2_QUEUE_LINEAR_CIRCULAR",
                        "topic_title": "Queue and Circular queue: linear, circular, using array, using linked list",
                        "syllabus_wording": "Queue; Circular queue; Queue implementation: linear, circular, using array, using linked list",
                        "keywords": ["queue", "circular queue", "fifo", "enqueue", "dequeue", "queue using array", "queue using linked list"]
                    },
                    {
                        "topic_id": "M2_QUEUE_APPLICATIONS",
                        "topic_title": "Applications of queue",
                        "syllabus_wording": "Applications",
                        "keywords": ["applications of queue", "queue applications", "cpu scheduling queue", "spooling", "printer queue"]
                    },
                    {
                        "topic_id": "M2_DEQUE",
                        "topic_title": "Deque: implementation, input-restricted and output-restricted",
                        "syllabus_wording": "Deque; Deque implementation: input restrictions, output restrictions",
                        "keywords": ["deque", "double ended queue", "input restricted deque", "output restricted deque"]
                    }
                ]
            },
            {
                "section_id": "M2_SEC_RECURSION",
                "section_title": "RECURSION",
                "topics": [
                    {
                        "topic_id": "M2_REC_PRINCIPLES",
                        "topic_title": "Principles of recursion, use of stack, recursion vs iteration",
                        "syllabus_wording": "Principles of recursion; Use of stack; Difference between recursion and iteration",
                        "keywords": ["principles of recursion", "recursion", "recursive", "base condition", "call stack", "use of stack", "recursion vs iteration"]
                    },
                    {
                        "topic_id": "M2_REC_TAIL",
                        "topic_title": "Tail recursion",
                        "syllabus_wording": "Tail recursion",
                        "keywords": ["tail recursion", "tail call", "tail recursive", "tail recursion elimination"]
                    },
                    {
                        "topic_id": "M2_REC_APPLICATIONS",
                        "topic_title": "Recursion Applications: Tower of Hanoi, Eight Queens Puzzle, concept of Backtracking",
                        "syllabus_wording": "Applications: Tower of Hanoi, Eight Queens Puzzle, concept of Backtracking",
                        "keywords": ["tower of hanoi", "eight queens", "8 queens", "backtracking", "concept of backtracking"]
                    }
                ]
            }
        ]
    },
    {
        "module_id": "MODULE_4",
        "module_number": 4,
        "module_title": "Sorting and Searching (Locked Whitelist)",
        "lecture_hours": "14L",
        "scope_status": "RESTRICTED_WHITELIST_IN_SCOPE",
        "sections": [
            {
                "section_id": "M4_SEC_SORTING",
                "section_title": "SORTING (LOCKED WHITELIST)",
                "topics": [
                    {
                        "topic_id": "M4_SORT_BUBBLE",
                        "topic_title": "Bubble Sort and Bubble Sort optimizations",
                        "syllabus_wording": "Bubble Sort; Bubble Sort optimizations",
                        "keywords": ["bubble sort", "modified bubble sort", "optimized bubble sort", "flagged bubble sort"]
                    },
                    {
                        "topic_id": "M4_SORT_COCKTAIL",
                        "topic_title": "Cocktail Shaker Sort",
                        "syllabus_wording": "Cocktail Shaker Sort",
                        "keywords": ["cocktail shaker sort", "cocktail sort", "shaker sort", "bidirectional bubble sort"]
                    },
                    {
                        "topic_id": "M4_SORT_INSERTION",
                        "topic_title": "Insertion Sort: Best-case, Worst-case, Average-case analysis",
                        "syllabus_wording": "Insertion Sort: Best-case analysis, Worst-case analysis, Average-case analysis",
                        "keywords": ["insertion sort", "insertion sort best case", "insertion sort worst case", "insertion sort average case"]
                    },
                    {
                        "topic_id": "M4_SORT_SELECTION",
                        "topic_title": "Selection Sort",
                        "syllabus_wording": "Selection Sort",
                        "keywords": ["selection sort", "selection sort pass"]
                    },
                    {
                        "topic_id": "M4_SORT_HEAPIFY",
                        "topic_title": "Max-Heapify and Build-Max-Heap",
                        "syllabus_wording": "Max-Heapify; Build-Max-Heap",
                        "keywords": ["max-heapify", "max heapify", "build-max-heap", "build max heap", "heap property", "max heap"]
                    },
                    {
                        "topic_id": "M4_SORT_QUICK",
                        "topic_title": "Quick Sort (WITHOUT complexity analysis)",
                        "syllabus_wording": "Quick Sort WITHOUT complexity analysis",
                        "keywords": ["quick sort", "quicksort", "partition", "pivot", "lomuto", "hoare", "partitioning algorithm"]
                    }
                ]
            },
            {
                "section_id": "M4_SEC_SEARCHING",
                "section_title": "SEARCHING",
                "topics": [
                    {
                        "topic_id": "M4_SEARCH_SEQUENTIAL",
                        "topic_title": "Sequential Search",
                        "syllabus_wording": "Sequential Search",
                        "keywords": ["sequential search", "linear search"]
                    },
                    {
                        "topic_id": "M4_SEARCH_BINARY",
                        "topic_title": "Binary Search: Worst-case and Average-case analysis",
                        "syllabus_wording": "Binary Search: Worst-case analysis, Average-case analysis",
                        "keywords": ["binary search", "binary search worst case", "binary search average case"]
                    },
                    {
                        "topic_id": "M4_SEARCH_INTERPOLATION",
                        "topic_title": "Interpolation Search",
                        "syllabus_wording": "Interpolation Search",
                        "keywords": ["interpolation search", "probe formula"]
                    }
                ]
            }
        ]
    }
]

print("Defined controlling syllabus structure.")
