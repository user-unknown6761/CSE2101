# CSE2101 / CSEN2101 — MODULE 1
# Ultimate Source-Grounded Exam Mastery System

> Source-locked student resource generated from the reconciled CSE2101 repository corpus and the attached handbook-generation prompt. No synthetic authentic questions are included.

## Verified Module 1 scope

- **Need for Data Structures** — Why do we need data structure?
- **Data, Data Type, Data Structure and ADT** — Data and data structure; Abstract Data Type and Data Type.
- **Algorithms, Programs and Pseudocode** — Algorithms and programs; basic idea of pseudo-code.
- **Algorithm Efficiency — Time and Space Analysis** — Algorithm efficiency and analysis; time and space analysis.
- **Asymptotic Notation — O, Ω, Θ** — Big O, Ω, Θ notations.
- **Array Representation — Row/Column Major and Addressing** — Different representations — row major, column major.
- **Sparse Matrix — Implementation and Usage** — Sparse matrix — implementation and usage.
- **Polynomial Representation Using Arrays** — Array representation of polynomials.
- **Singly Linked List** — Singly linked list.
- **Circular Linked List** — Circular linked list.
- **Doubly Linked List** — Doubly linked list.
- **Doubly Circular Linked List** — Doubly circular linked list.
- **Linked-List Representation of Polynomial** — Linked list representation of polynomial.
- **Applications of Linked Lists** — Applications.

## Coverage totals

| Master Pattern | Unique Questions | Retained Occurrences |
|---|---:|---:|
| Need for Data Structures | 1 | 1 |
| Data, Data Type, Data Structure and ADT | 11 | 13 |
| Algorithms, Programs and Pseudocode | 20 | 48 |
| Algorithm Efficiency — Time and Space Analysis | 16 | 39 |
| Asymptotic Notation — O, Ω, Θ | 18 | 40 |
| Array Representation — Row/Column Major and Addressing | 22 | 37 |
| Sparse Matrix — Implementation and Usage | 7 | 20 |
| Polynomial Representation Using Arrays | 2 | 6 |
| Singly Linked List | 38 | 70 |
| Circular Linked List | 6 | 20 |
| Doubly Linked List | 8 | 18 |
| Doubly Circular Linked List | 0 | 0 |
| Linked-List Representation of Polynomial | 0 | 0 |
| Applications of Linked Lists | 5 | 7 |

## Study order

1. Concepts → algorithms/programs → efficiency → asymptotic notation.
2. Array representation → sparse matrix → polynomial arrays.
3. Singly linked list → circular linked list → doubly linked list → linked-list polynomial → applications.
4. Doubly circular linked list remains a syllabus topic; no source-empty practice questions are invented.


# MASTER PATTERN — Need for Data Structures

# Need for Data Structures

**Syllabus wording:** Why do we need data structure?

**Coverage:** 1 normalized unique source question(s), 1 retained occurrence(s).

## Subpattern map

1. **Need and applications of data structures** — 1 unique question(s)

---

## Need and applications of data structures

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Need and applications of data structures → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q153

> List out the areas in which data structures are applied extensively?

**Source:** DOC-30 · page 1 · Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D1  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Data structures are needed to organize data and make required operations manageable and efficient. For the source question, state the need first and then the requested application areas.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



# MASTER PATTERN — Data, Data Type, Data Structure and ADT

# Data, Data Type, Data Structure and ADT

**Syllabus wording:** Data and data structure; Abstract Data Type and Data Type.

**Coverage:** 11 normalized unique source question(s), 13 retained occurrence(s).

## Subpattern map

1. **Linear / non-linear and primitive / non-primitive classification** — 4 unique question(s)
2. **Data, data type and data structure** — 3 unique question(s)
3. **ADT vs data type / data structure** — 4 unique question(s)

---

## Linear / non-linear and primitive / non-primitive classification

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Linear / non-linear and primitive / non-primitive classification → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q026

> Whether Linked List is linear or Non-linear data structure?

**Source:** DOC-30 · page 6 · Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D1  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: A linear structure keeps elements in a logical sequence; a non-linear structure represents branching or network relationships. Primitive types are fundamental built-in types; non-primitive structures organize collections or relationships.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q141

> A mathematical-model with a collection of operations defined on that model is called (A) Data Structure (B)  Abstract Data Type (C)  Primitive Data Type (D)  Algorithm

**Source:** DOC-31 · page 2 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 2  
**Priority:** P3  
**Difficulty:** D1  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: A linear structure keeps elements in a logical sequence; a non-linear structure represents branching or network relationships. Primitive types are fundamental built-in types; non-primitive structures organize collections or relationships.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q143

> An ADT is defined to be a mathematical model of a user-defined type along with the collection of all ____________ operations on that model. (A) Cardinality (B) Assignment (C) Primitive (D) Structured

**Source:** DOC-31 · page 9 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 2  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: A linear structure keeps elements in a logical sequence; a non-linear structure represents branching or network relationships. Primitive types are fundamental built-in types; non-primitive structures organize collections or relationships.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q152

> What is the difference between a linear and a nonlinear data structure?

**Source:** DOC-22 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D1  
**Occurrences:** 2  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: A linear structure keeps elements in a logical sequence; a non-linear structure represents branching or network relationships. Primitive types are fundamental built-in types; non-primitive structures organize collections or relationships.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Data, data type and data structure

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Data, data type and data structure → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q032

> Write the syntax of node creation? Answer : Syntax: struct node { data type ; struct node *ptr; //pointer for link node } temp;

**Source:** DOC-30 · page 11 · Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Data is the information being represented; a data type defines values and permitted operations; a data structure organizes data and relationships for efficient processing.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q072

> Why is a Linked List called a self-referential data type? Represent the polynomial 6x5 + 10x2 + x + 5 using a Linked List. (2 + 6) + (2 + 2) = 12

**Source:** DOC-25 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D3  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Data is the information being represented; a data type defines values and permitted operations; a data structure organizes data and relationships for efficient processing.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q144

> How does an array differ from an ordinary variable?

**Source:** DOC-31 · page 10 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 2  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: A variable stores one value of a declared type, whereas an array represents an indexed collection of values of the declared element type.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## ADT vs data type / data structure

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**ADT vs data type / data structure → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q139

> Define Omega-notation and Theta-notation. What is an abstract data type? Why array is called an abstract data type?

**Source:** DOC-22 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D1  
**Occurrences:** 2  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: An ADT specifies the logical data model and permitted operations without fixing the implementation. A data structure is the concrete in-memory representation used to implement that specification.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q140

> What is the difference between an abstract data type (ADT) and a data structure? ARRAY APPLICATIONS

**Source:** DOC-28 · page 6 · Practice / Problem Set  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D1  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: An ADT specifies the logical data model and permitted operations without fixing the implementation. A data structure is the concrete in-memory representation used to implement that specification.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q142

> Representation of data structure in memory is known as: (A)  recursive (B)  abstract data type (C)  storage structure (D)  file structure

**Source:** DOC-31 · page 8 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 2  
**Priority:** P3  
**Difficulty:** D3  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: An ADT specifies the logical data model and permitted operations without fixing the implementation. A data structure is the concrete in-memory representation used to implement that specification.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q145

> Define data type and abstract data type. Comment upon the significance of both. (8)

**Source:** DOC-31 · page 76 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 8  
**Priority:** P3  
**Difficulty:** D1  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: An ADT specifies the logical data model and permitted operations without fixing the implementation. A data structure is the concrete in-memory representation used to implement that specification.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



# MASTER PATTERN — Algorithms, Programs and Pseudocode

# Algorithms, Programs and Pseudocode

**Syllabus wording:** Algorithms and programs; basic idea of pseudo-code.

**Coverage:** 20 normalized unique source question(s), 48 retained occurrence(s).

## Subpattern map

1. **Pseudocode and algorithm specification** — 16 unique question(s)
2. **Algorithm vs program** — 2 unique question(s)
3. **Characteristics of a good algorithm** — 1 unique question(s)
4. **Algorithm fundamentals** — 1 unique question(s)

---

## Pseudocode and algorithm specification

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Pseudocode and algorithm specification → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q002

> Why do we need sparse representation of matrices? State the name of the two representations. Write the pseudocode to reverse a single linked list . Remember, you need to change the order in the linked list itself, not just print the elements in reverse order.

**Source:** DOC-01 · page 2 · Backlog / Special Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D3  
**Occurrences:** 2  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Pseudocode is a language-independent description of algorithmic logic using readable control structures. Write only the steps required by the source problem.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q009

> Write a function in C/pseudo-code to delete all the nodes that contains the certain value v, from a singly linked list in a single pass. If there are multiple occurrences, delete all occurrences.  Discuss the time complexity of the algorithm. (Do not forget to look after the test cases when v will not exist in the list or list is empty). [(CSEN2101.2, CSEN2101.3)(Apply, Analyse/IOCQ)]

**Source:** DOC-06 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P1  
**Difficulty:** D4  
**Occurrences:** 4  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Pseudocode is a language-independent description of algorithmic logic using readable control structures. Write only the steps required by the source problem.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q011

> Write a pseudo-code/C program to determine whether a singly linked list is a palindrome or not. Return 1 if it is a palindrome and 0 otherwise. Note that the expected solution run in linear time.                       [(CSEN2101.4, CSEN2101.5)(Apply/IOCQ)]

**Source:** DOC-06 · page 3 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P1  
**Difficulty:** D2  
**Occurrences:** 4  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Pseudocode is a language-independent description of algorithmic logic using readable control structures. Write only the steps required by the source problem.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q021

> Write a function in C/ pseudo-code to delete all the nodes that contain the certain value v, from a singly linked list in a single pass. If there are multiple occurrences, delete all occurrences. Discuss the worst case time complexity of the algorithm.

**Source:** DOC-28 · page 8 · Practice / Problem Set  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Pseudocode is a language-independent description of algorithmic logic using readable control structures. Write only the steps required by the source problem.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q022

> Given a singly-linked list with an odd number of elements, develop a pseudo-code or C-code to split it into two nearly equal sub-lists — one for the front half, and the other for the back half. The extra element should go in the front list.

**Source:** DOC-28 · page 8 · Practice / Problem Set  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D4  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Pseudocode is a language-independent description of algorithmic logic using readable control structures. Write only the steps required by the source problem.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q023

> Write the pseudo code to insert an element into a singly linked list at a given position. Take appropriate measure when the list is empty or if the given position does not exist in the list.

**Source:** DOC-28 · page 8 · Practice / Problem Set  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Pseudocode is a language-independent description of algorithmic logic using readable control structures. Write only the steps required by the source problem.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q024

> Suggest a pseudo code / C function to find the middle element of a single linked list in a single pass. (Please note that if the list has even number of elements (n) then middle element will be the first middle element (⌊n/2⌋).

**Source:** DOC-28 · page 9 · Practice / Problem Set  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Pseudocode is a language-independent description of algorithmic logic using readable control structures. Write only the steps required by the source problem.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q054

> Write a pseudo-code/C program to reverse a singly linked list. [(CO2, CO3)(Apply/LOCQ)]

**Source:** DOC-03 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D2  
**Occurrences:** 3  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Pseudocode is a language-independent description of algorithmic logic using readable control structures. Write only the steps required by the source problem.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q058

> Write an algorithm/C-like pseudo code to delete the last element from a circular singly linked list. What is the time complexity of this operation? [(CO1,CO2)(Understand/LOCQ)] (5 + 1) + 2 + (3 + 1) = 12

**Source:** DOC-10 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D2  
**Occurrences:** 3  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Pseudocode is a language-independent description of algorithmic logic using readable control structures. Write only the steps required by the source problem.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q061

> Write an algorithm/C-like pseudo code to delete the last element from a circular singly linked list. What is the time complexity of this operation?

**Source:** DOC-28 · page 8 · Practice / Problem Set  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D1  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Pseudocode is a language-independent description of algorithmic logic using readable control structures. Write only the steps required by the source problem.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q069

> Write the pseudo-code of inserting an element after a given value in a doubly linked list. Your code should work for any position of the given value. Show proper error messages, if any. [(CO1)(Understand and Remember/LOCQ)]

**Source:** DOC-06 · page 3 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P1  
**Difficulty:** D2  
**Occurrences:** 9  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Pseudocode is a language-independent description of algorithmic logic using readable control structures. Write only the steps required by the source problem.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q071

> How is a doubly linked list more useful than a singly linked list? Write a program/pseudo code to add an element after a given element in a doubly linked list.

**Source:** DOC-25 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Pseudocode is a language-independent description of algorithmic logic using readable control structures. Write only the steps required by the source problem.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q116

> Write the non-recursive pseudo-code for Binary-search? State its best-case and average case complexity. [(CO2)(Remember/IOCQ)]

**Source:** DOC-10 · page 3 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D2  
**Occurrences:** 3  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Pseudocode is a language-independent description of algorithmic logic using readable control structures. Write only the steps required by the source problem.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q117

> Suppose you are given an array containing 0s and 1s in the following manner – a string of 0s trapped between two strings of 1s, eg. 111111000001111. It is also given that none of these three strings is empty, i.e., each of these three strings contains at least one character (or digit) and that the median (middle) element is a 0. (i)  Write a pseudo-code to determine both the left and right boundaries of the middle string of 0s, i.e. the output of your code should give the two indices of the leftmost 0 and the rightmost position 0. (ii)  What is minimum size of the array possible? [(CO4)(Apply/IOCQ)] (1 + 2) + 2 + (6 + 1) = 12 Cognition Level LOCQ IOCQ HOCQ Percentage distribution 29.17 53.12 17.71

**Source:** DOC-13 · page 3 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P1  
**Difficulty:** D3  
**Occurrences:** 4  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Pseudocode is a language-independent description of algorithmic logic using readable control structures. Write only the steps required by the source problem.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q118

> When do you say that a certain sorting algorithm is stable? The following pseudo-code works on an array of records indexed from 1 to n, where kj is the key of the record of type integer present at index j. What job does it perform? What changes occur (if any) if you change the ≤ operator in the above pseudo-code to (i)   < (ii)  ≥ (iii) >

**Source:** DOC-28 · page 12 · Practice / Problem Set  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Pseudocode is a language-independent description of algorithmic logic using readable control structures. Write only the steps required by the source problem.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q119

> Write the non-recursive pseudo-code for Binary-search. State its best-case and average case complexity.

**Source:** DOC-28 · page 13 · Practice / Problem Set  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Pseudocode is a language-independent description of algorithmic logic using readable control structures. Write only the steps required by the source problem.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Algorithm vs program

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Algorithm vs program → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q064

> Write a program or pseudo code or algorithm to display node values in reverse order for a double linked list? [(CO4)(Understand/LOCQ)]

**Source:** DOC-03 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D2  
**Occurrences:** 3  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: An algorithm is language-independent problem-solving logic; a program is a concrete implementation of that logic in a programming language.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q115

> An unsorted array contains 2n+1 integers such taht all but one element occur twice each. Write a program/pseudo-code/algorithm that can find the element occuring exactly once in this array. What is its time complexity? [(CO1, CO5)(Understand/HOCQ)]

**Source:** DOC-03 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D2  
**Occurrences:** 3  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: An algorithm is language-independent problem-solving logic; a program is a concrete implementation of that logic in a programming language.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Characteristics of a good algorithm

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Characteristics of a good algorithm → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q120

> What is an algorithm?  What are the characteristics of a good algorithm? (4)

**Source:** DOC-31 · page 16 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 4  
**Priority:** P3  
**Difficulty:** D1  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Define an algorithm as a finite sequence of unambiguous and effective steps. List input, output, definiteness, finiteness, effectiveness and correctness.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Algorithm fundamentals

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Algorithm fundamentals → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q121

> List various problem solving techniques. (5)

**Source:** DOC-31 · page 85 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 5  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Pseudocode is a language-independent description of algorithmic logic using readable control structures. Write only the steps required by the source problem.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



# MASTER PATTERN — Algorithm Efficiency — Time and Space Analysis

# Algorithm Efficiency — Time and Space Analysis

**Syllabus wording:** Algorithm efficiency and analysis; time and space analysis.

**Coverage:** 16 normalized unique source question(s), 39 retained occurrence(s).

## Subpattern map

1. **Efficiency concepts and complexity** — 9 unique question(s)
2. **Best / average / worst-case reasoning** — 4 unique question(s)
3. **Time vs space complexity** — 3 unique question(s)

---

## Efficiency concepts and complexity

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Efficiency concepts and complexity → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q012

> How do you merge two sorted linked lists into a single sorted linked list? Provide an algorithm and analyze its time complexity. [(CO3,CO4)(Analyse/HOCQ)]

**Source:** DOC-10 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P1  
**Difficulty:** D4  
**Occurrences:** 4  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Identify the required time/space measure, count the actual work or memory used, and then report the asymptotic order. Qualify the answer when locating a position requires an additional traversal.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q019

> The time complexity of displaying the contents of a singly-linked list in reverse order without using a stack is _________.

**Source:** DOC-28 · page 5 · Practice / Problem Set  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Identify the required time/space measure, count the actual work or memory used, and then report the asymptotic order. Qualify the answer when locating a position requires an additional traversal.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q055

> The time complexity of inserting an element at the beginning of a singly-circular linked list having only one external pointer pointing to the head is: (a) O (1) (b) O (log2n) (c) O (n) (d) O (n2)

**Source:** DOC-10 · page 1 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 1  
**Priority:** P1  
**Difficulty:** D2  
**Occurrences:** 4  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Identify the required time/space measure, count the actual work or memory used, and then report the asymptotic order. Qualify the answer when locating a position requires an additional traversal.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q065

> A sorting method with time complexity O(n log n) spends exactly 1 millisecond to sort 1,000 data items. Assuming that time T(n) of sorting n items is directly proportional to n log n, that is, T(n) = cn log n, derive a formula for T(n), given the time T(N) for sorting N items, and estimate how long this method will take to sort 1,000,000 items. [(CO4)(Analyse/HOCQ)] (4 + 1) + 3 + 4 = 12

**Source:** DOC-03 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D4  
**Occurrences:** 3  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Identify the required time/space measure, count the actual work or memory used, and then report the asymptotic order. Qualify the answer when locating a position requires an additional traversal.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q097

> If the number of nonzero elements in the triple representation of a sparse matrix of m × n dimension is K, then what is the time complexity to read an element from the index [i][j] of the sparse matrix. Assume that the sparse matrix is stored in triple format. [(CO4)(Analyze/LOCQ)]

**Source:** DOC-10 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P1  
**Difficulty:** D4  
**Occurrences:** 4  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Identify the required time/space measure, count the actual work or memory used, and then report the asymptotic order. Qualify the answer when locating a position requires an additional traversal.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q128

> Write an algorithm to merge eight sorted queues into one single queue in such a way that duplicates are removed and the resultant queue is sorted also. Comment on the time complexity of your algorithm. More credits will be given to more efficient algorithms. [(CO2)(Analyse/IOCQ)]

**Source:** DOC-13 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P1  
**Difficulty:** D4  
**Occurrences:** 5  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Maintain one front value per sorted queue, repeatedly choose the smallest front, output it only when it differs from the previous output, and advance that queue. With eight fixed queues the total work is O(N).

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q130

> An algorithm is made up of two independent time complexities f (n) and g (n). Then the complexities of the algorithm is in the order of (A) f(n) x g(n) (B) Max ( f(n),g(n)) (C) Min (f(n),g(n)) (D) f(n) + g(n)

**Source:** DOC-31 · page 9 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 2  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Identify the required time/space measure, count the actual work or memory used, and then report the asymptotic order. Qualify the answer when locating a position requires an additional traversal.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q133

> Propose an algorithm to remove duplicates from an ordered array, without using any second array. For example, if the original content of the array is: 1, 1, 3, 4, 8, 8, 10, 10, 25, 28, 30, 30, 30; then the final content of the array should be 1,3,4,8,10,25,28,30 What is the time complexity of the proposed algorithm? [(CO1,CO4)(Analyze/IOCQ)]

**Source:** DOC-10 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D4  
**Occurrences:** 3  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Identify the required time/space measure, count the actual work or memory used, and then report the asymptotic order. Qualify the answer when locating a position requires an additional traversal.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q135

> Propose an algorithm to remove duplicates from an ordered array, without using any second array. For example, if the original content of the array is: 1, 1, 3, 4, 8, 8, 10, 10, 25, 28, 30, 30, 30; then the final content of the array should be 1,3,4,8,10,25,28,30. What is the time complexity of the proposed algorithm?

**Source:** DOC-28 · page 6 · Practice / Problem Set  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Identify the required time/space measure, count the actual work or memory used, and then report the asymptotic order. Qualify the answer when locating a position requires an additional traversal.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Best / average / worst-case reasoning

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Best / average / worst-case reasoning → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q068

> Worst-case time complexity of a comparison-based sort cannot be better than, (a) O(nlogn) (b) O(n2) (c) O(n) (d) O(nlognlogn).

**Source:** DOC-06 · page 1 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 1  
**Priority:** P1  
**Difficulty:** D2  
**Occurrences:** 4  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Identify the required time/space measure, count the actual work or memory used, and then report the asymptotic order. Qualify the answer when locating a position requires an additional traversal.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q101

> We measure best case time complexity of any algorithm by using (a) Θ(n) (b) θ(n) (c) O(n) (d) Ω(n) where n is the number of inputs.

**Source:** DOC-01 · page 1 · Backlog / Special Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 1  
**Priority:** P2  
**Difficulty:** D2  
**Occurrences:** 2  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Identify the required time/space measure, count the actual work or memory used, and then report the asymptotic order. Qualify the answer when locating a position requires an additional traversal.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q123

> If for an algorithm, f(n) = 3n2+10, state the worst case asymptotic time complexity of the algorithm. Show that it follows from the definition of worst case asymptotic time complexity.  [(CO1) (Apply/IOCQ)] (1 + 3 + 2) + 3.5 + (0.5 + 2) = 12

**Source:** DOC-02 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D2  
**Occurrences:** 3  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Identify the required time/space measure, count the actual work or memory used, and then report the asymptotic order. Qualify the answer when locating a position requires an additional traversal.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q132

> What do you mean by complexity of an algorithm?  Explain the meaning of worst case analysis and best case analysis with an example. (8)

**Source:** DOC-31 · page 41 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 8  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Identify the required time/space measure, count the actual work or memory used, and then report the asymptotic order. Qualify the answer when locating a position requires an additional traversal.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Time vs space complexity

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Time vs space complexity → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q107

> What do you understand by Time and Space complexity? How is Big-O notation used for complexity analysis of algorithms?

**Source:** DOC-25 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Identify the required time/space measure, count the actual work or memory used, and then report the asymptotic order. Qualify the answer when locating a position requires an additional traversal.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q129

> How can you reverse an array without using an extra array? Provide the algorithm and analyze its time and space complexity.

**Source:** DOC-28 · page 6 · Practice / Problem Set  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D4  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Use i=0 and j=n−1. While i<j, swap A[i] and A[j], then i++ and j--. Time O(n), auxiliary space O(1).

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q131

> How do you find the complexity of an algorithm?  What is the relation between the time and space complexities of an algorithm?  Justify your answer with an example. (5)

**Source:** DOC-31 · page 16 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 5  
**Priority:** P3  
**Difficulty:** D4  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Identify the required time/space measure, count the actual work or memory used, and then report the asymptotic order. Qualify the answer when locating a position requires an additional traversal.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



# MASTER PATTERN — Asymptotic Notation — O, Ω, Θ

# Asymptotic Notation — O, Ω, Θ

**Syllabus wording:** Big O, Ω, Θ notations.

**Coverage:** 18 normalized unique source question(s), 40 retained occurrence(s).

## Subpattern map

1. **Growth-order recognition** — 7 unique question(s)
2. **Bound reasoning and proofs** — 11 unique question(s)

---

## Growth-order recognition

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Growth-order recognition → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q010

> Define Big-Oh, Big-Omega and Big-Theta with example. [(CSEN2101.1)(Remember/LOCQ)]

**Source:** DOC-06 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P1  
**Difficulty:** D1  
**Occurrences:** 4  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: O(g(n)) gives an asymptotic upper bound; Ω(g(n)) gives a lower bound; Θ(g(n)) gives a tight bound satisfying both.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q103

> The running time of a linear time algorithm is (a) O(1) (b) O(n) (c) O(n log n) (d) O(log n)

**Source:** DOC-22 · page 1 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 1  
**Priority:** P2  
**Difficulty:** D2  
**Occurrences:** 2  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the dominant growth term or compare the relevant functions using the definitions of O, Ω and Θ. For a proof, state the required inequality and suitable constants.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q106

> Which notation provides a strict lower bound for f(n)? (a) Omega (b) Big O (c) Small o (d) Theta.

**Source:** DOC-25 · page 1 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 1  
**Priority:** P3  
**Difficulty:** D1  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Select Ω from the listed choices; it denotes an asymptotic lower bound.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q109

> The span of a stock’s price on a certain day, d, is the maximum number of consecutive days (up to the current day) the price of the stock has been less than or equal to its price on d. An example is give below: Day # 1 2 3 4 5 6 Price 9 3 5 2 7 12 Span 1 1 2 1 4 6 A naive comparison based algorithm will run in O(n2) time. You have to design an algorithm using stack so that the algorithm can be run in O(n) time. RECURSION

**Source:** DOC-28 · page 7 · Practice / Problem Set  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D4  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the dominant growth term or compare the relevant functions using the definitions of O, Ω and Θ. For a proof, state the required inequality and suitable constants.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q111

> O(N) (linear time) is better than O(1) constant time. (A) True (B)  False

**Source:** DOC-31 · page 9 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 2  
**Priority:** P3  
**Difficulty:** D1  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: False. O(1) is asymptotically better than O(n).

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q114

> Why do we use a symptotic notation in the study of algorithm? Describe commonly used asymptotic notations and give their significance. (8) 50

**Source:** DOC-31 · page 49 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the dominant growth term or compare the relevant functions using the definitions of O, Ω and Θ. For a proof, state the required inequality and suitable constants.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q126

> Time complexities of three algorithms are given.  Which should execute the slowest for large values of N? (A) ( ) 2 1 N O (B) ( ) N O (C) ( ) N O log (D) None of these

**Source:** DOC-31 · page 10 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 2  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the dominant growth term or compare the relevant functions using the definitions of O, Ω and Θ. For a proof, state the required inequality and suitable constants.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Bound reasoning and proofs

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Bound reasoning and proofs → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q060

> If f(n)= O(g(n)) and g(n)=O(h(n)), then the relationship between f(n) and h(n) in terms of Big Oh notation is __________.

**Source:** DOC-13 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 1  
**Priority:** P1  
**Difficulty:** D2  
**Occurrences:** 4  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the dominant growth term or compare the relevant functions using the definitions of O, Ω and Θ. For a proof, state the required inequality and suitable constants.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q083

> Consider the linear arrays AAA(5:50), BBB (-5:10) and CCC(18). (a) Find the number of elements in each array (b) Suppose Base(AAA) = 300 and w=4 words per memory cell for AAA. Find the address of AAA[15], AAA[35] and AAA[55] Ans : (a) Length = Upper Bound (UB) – Lower Boun d (LB) +1 Length(AAA) = 50-5+1 = 46 Length(BBB) = 10-(-5)+1 = 16 Length(CCC) = 18-1+1 = 18 (b) Using the formula: LOC(AAA[k]) = Base(AAA)+w(K- LB) LOC(AAA[15] )= 300+4(15-5) = 340 LOC(AAA[35] )= 300+4(35-5) = 420 AAA[55] is not an element of AAA since 55 exceeds UB = 50.

**Source:** DOC-30 · page 8 · Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D3  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the dominant growth term or compare the relevant functions using the definitions of O, Ω and Θ. For a proof, state the required inequality and suitable constants.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q102

> Find the Big-Oh for T(n) = 48n100+ 2n+2 + 3n2 + 100. [(CO2)(Apply/IOCQ)] (6 + 1) + 3 + 2 = 12

**Source:** DOC-10 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D2  
**Occurrences:** 3  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: The highest-order term is n^100, so the function is O(n^100) and, with the positive leading term, Θ(n^100).

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q104

> The memory address of fifth element of an array can be calculated by the formula (a)  LOC(Array[5]=Base(Array)+w(5-lower bound), where w is the number of words per memory cell for the array (b)  LOC(Array[5])=Base(Array[5])+(5-lower bound), where w is the number of words per memory cell for the array (c)  LOC(Array[5])=Base(Array[4])+(5-Upper bound), where w is the number of words per memory cell for the array (d)  None of above

**Source:** DOC-22 · page 1 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 1  
**Priority:** P2  
**Difficulty:** D3  
**Occurrences:** 2  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the dominant growth term or compare the relevant functions using the definitions of O, Ω and Θ. For a proof, state the required inequality and suitable constants.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q105

> Explain that 10n3 + 20n ≠ O(n2). (3 + 3) + 2 + 4 = 12

**Source:** DOC-22 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D2  
**Occurrences:** 2  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Dividing by n² gives 10n+20/n, which is unbounded, so 10n³+20n is not O(n²).

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q108

> Find the Big-Oh for T(n) = 48n100+ 2n+2 + 3n2 + 100.

**Source:** DOC-28 · page 6 · Practice / Problem Set  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: The highest-order term is n^100, so the function is O(n^100) and, with the positive leading term, Θ(n^100).

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q113

> An, array, A contains n unique integers from the range x to y (x and y inclusive where n=y-x). That is, there is one member that is not in A. Design an O(n) time algorithm for finding that number. (8)

**Source:** DOC-31 · page 33 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 8  
**Priority:** P3  
**Difficulty:** D4  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the dominant growth term or compare the relevant functions using the definitions of O, Ω and Θ. For a proof, state the required inequality and suitable constants.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q122

> State if the following statement is correct. Justify your answer. O(n2) = 2n2+100. [(CO1) (Apply/IOCQ)]

**Source:** DOC-02 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D4  
**Occurrences:** 3  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the dominant growth term or compare the relevant functions using the definitions of O, Ω and Θ. For a proof, state the required inequality and suitable constants.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q124

> f(n) = 3n2+10n; g(n) = 2n3 ;  then (a) g(n)  O(f(n)) (b) g(n)  Ω(f(n)) (c) g(n)  Ө(f(n)) (d) all of these.

**Source:** DOC-03 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 1  
**Priority:** P2  
**Difficulty:** D2  
**Occurrences:** 3  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: For n≥1, 3n² ≤ 3n²+10 ≤ 13n²; therefore the function is Θ(n²) and also O(n²).

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q125

> Prove: n2 + 100 n  =  (n2). [(CO1)(Understand and Remember/LOCQ)]

**Source:** DOC-06 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P1  
**Difficulty:** D4  
**Occurrences:** 8  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the dominant growth term or compare the relevant functions using the definitions of O, Ω and Θ. For a proof, state the required inequality and suitable constants.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q127

> Compare two functions 2 n  and 4 2n for various values of n.  Determine when second becomes larger than first. (5) When n=8, the value of n2 and 2n/4 is same. Before that n2 >2n/4, and after this value n2< 2n/4.

**Source:** DOC-31 · page 17 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D4  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the dominant growth term or compare the relevant functions using the definitions of O, Ω and Θ. For a proof, state the required inequality and suitable constants.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



# MASTER PATTERN — Array Representation — Row/Column Major and Addressing

# Array Representation — Row/Column Major and Addressing

**Syllabus wording:** Different representations — row major, column major.

**Coverage:** 22 normalized unique source question(s), 37 retained occurrence(s).

## Subpattern map

1. **Array representation** — 8 unique question(s)
2. **Column-major address calculation** — 1 unique question(s)
3. **Row-major vs column-major** — 3 unique question(s)
4. **Row-major address calculation** — 4 unique question(s)
5. **Special matrix representation** — 2 unique question(s)
6. **1D array bounds / representation** — 3 unique question(s)
7. **Array manipulation** — 1 unique question(s)

---

## Array representation

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Array representation → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q077

> In a 2D array int arr[100][50], the base address is 100. Then what will be the address of arr[50][30]? (a) 5162 (b) 5160 (c) 5100 (d) None of these

**Source:** DOC-02 · page 1 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 1  
**Priority:** P2  
**Difficulty:** D3  
**Occurrences:** 3  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Write the memory-layout formula, subtract the lower bounds, apply row-major or column-major order, multiply by element width when provided, then add the base address.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q084

> What is the condition to be checked for the multiplication of two matrices? Ans :If matrices are to be multiplied, the number of columns of first matrix should be equal to the number of rows of second matrix.

**Source:** DOC-30 · page 10 · Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Write the memory-layout formula, subtract the lower bounds, apply row-major or column-major order, multiply by element width when provided, then add the base address.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q087

> The complexity of multiplying two matrices of order m*n and n*p is (A)  mnp (B)  mp (C)  mn (D)  np

**Source:** DOC-31 · page 3 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 2  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Write the memory-layout formula, subtract the lower bounds, apply row-major or column-major order, multiply by element width when provided, then add the base address.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q091

> Define the term array. How are two-dimensional arrays represented in memory? Explain how address of an element is calculated in a two dimensional array. (8)

**Source:** DOC-31 · page 32 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 8  
**Priority:** P3  
**Difficulty:** D1  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Write the memory-layout formula, subtract the lower bounds, apply row-major or column-major order, multiply by element width when provided, then add the base address.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q093

> By taking an example show how multidimensional array can be represented in one dimensional array. (8)

**Source:** DOC-31 · page 79 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 8  
**Priority:** P3  
**Difficulty:** D3  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Write the memory-layout formula, subtract the lower bounds, apply row-major or column-major order, multiply by element width when provided, then add the base address.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q134

> Given an integer array arr[ ]; the i-th element can be accessed by writing (a) *(arr+i) (b) arr[i]             (c) both (a) and (b) (d) *arr + i

**Source:** DOC-22 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 1  
**Priority:** P2  
**Difficulty:** D2  
**Occurrences:** 2  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: arr[i] and *(arr+i) refer to the same element, so the source answer is option (c) both.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q136

> What values are automatically assigned to those array elements which are not explicitly initialized?

**Source:** DOC-31 · page 10 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 2  
**Priority:** P3  
**Difficulty:** D1  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Global/static arrays are zero-initialized in C; automatic local arrays are not automatically initialized and have indeterminate values.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q151

> Write the syntax for multiplication of matrices? Ans : for (=0; < value;++) { for (=0; < value;++) { for (=0; < value;++) { arr[var1][var2] += arr[var1][var3] * arr[var3][arr2]; } } }

**Source:** DOC-30 · page 10 · Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Write the memory-layout formula, subtract the lower bounds, apply row-major or column-major order, multiply by element width when provided, then add the base address.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Column-major address calculation

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Column-major address calculation → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q078

> Given a 2D matrix of dimension 100 x 200 and also given that the base address of the 2D array is 2020. Assume that the array index of the matrix starts from [10, 20]. Find the address of the element with index [50,160] for column major ordering.  [(CO2) (Understand/IOCQ)]

**Source:** DOC-02 · page 3 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D3  
**Occurrences:** 3  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Offset = (160−20)×100+(50−10)=14,040. Address = 2020+14,040w; if one address unit per element is intended, 16,060.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Row-major vs column-major

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Row-major vs column-major → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q079

> If the base address of an array Z with dimension 10X20 is 2023 and the array elements are stored in column-major ordering, what will be the address of the element  Z[10][15]? In case Z is stored using row-major ordering, what will be the memory address of the same element?                  [(CO1)(Understand & Remember/LOCQ)]

**Source:** DOC-06 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P1  
**Difficulty:** D3  
**Occurrences:** 4  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Write the memory-layout formula, subtract the lower bounds, apply row-major or column-major order, multiply by element width when provided, then add the base address.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q082

> Given a 2D integer array of dimension 100 x 200 and also given that the base address of the 2D array is 2020. Assume that the array index of the matrix starts from [10, 20]. Find the address of the element with index [50,160] for column major ordering and row major ordering.

**Source:** DOC-28 · page 6 · Practice / Problem Set  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D3  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Offset = (160−20)×100+(50−10)=14,040. Address = 2020+14,040w; if one address unit per element is intended, 16,060.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q088

> If the address of A[1][1] and A[2][1] are 1000 and 1010 respectively and each element occupies 2 bytes then the array has been stored in _________ order. (A)  row major (B)  column major (C)  matix major (D)  none of these

**Source:** DOC-31 · page 8 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 2  
**Priority:** P3  
**Difficulty:** D3  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Write the memory-layout formula, subtract the lower bounds, apply row-major or column-major order, multiply by element width when provided, then add the base address.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Row-major address calculation

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Row-major address calculation → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q080

> Let A be a two-dimensional array declared as follows: A: array [1…10] [1…15] of character; Assuming that each character takes one memory locations the array is stored in row-major order and the first element of the array is stored in location 100, what is the address of the element A[i][j] ? (a) 15i + j + 84 (b) 15j + i + 84 (c) 10i + j + 89 (d) 10j + i + 89

**Source:** DOC-10 · page 1 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 1  
**Priority:** P1  
**Difficulty:** D3  
**Occurrences:** 4  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Address = 100 + [(i−1)×15+(j−1)]×1 = 15i+j+84, option (a).

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q081

> Let A be a two-dimensional array declared as follows: A: array [1…10] [1…15] of character; Assuming that each character takes one memory location, the array is stored in row-major order and the first element of the array is stored in location 100, what is the address of the element A[i][j] ? (a) 15i + j + 84 (b) 15j + i + 84 (c) 10i + j + 89 (d) 10j + i + 89

**Source:** DOC-13 · page 1 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 1  
**Priority:** P1  
**Difficulty:** D3  
**Occurrences:** 4  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Address = 100 + [(i−1)×15+(j−1)]×1 = 15i+j+84, option (a).

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q089

> A two dimensional array TABLE [6] [8] is stored in row major order with base address 351. What is the address of TABLE [3] [4]?

**Source:** DOC-31 · page 11 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 2  
**Priority:** P3  
**Difficulty:** D1  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Write the memory-layout formula, subtract the lower bounds, apply row-major or column-major order, multiply by element width when provided, then add the base address.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q092

> Explain the method to calculate the address of an element in an array. A 4 25× matrix array DATA is stored in memory in ‘row-major order’.  If base address is 200 and 4 = ω words per memory cell.  Calculate the address of DATA [12, 3] . (8)

**Source:** DOC-31 · page 41 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 8  
**Priority:** P3  
**Difficulty:** D3  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Write the memory-layout formula, subtract the lower bounds, apply row-major or column-major order, multiply by element width when provided, then add the base address.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Special matrix representation

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Special matrix representation → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q090

> Explain an efficient way of storing two symmetric matrices of the same order in memory. (4)

**Source:** DOC-31 · page 18 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 4  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Write the memory-layout formula, subtract the lower bounds, apply row-major or column-major order, multiply by element width when provided, then add the base address.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q150

> What is an upper triangular matrix? Give Example. How is an upper triangular matrix stored in the computer memory?

**Source:** DOC-22 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D1  
**Occurrences:** 2  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: For an upper triangular matrix, entries below the main diagonal are zero. The number of stored positions is n(n+1)/2.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## 1D array bounds / representation

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**1D array bounds / representation → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q110

> The smallest element of an array’s index is called its (A) lower bound. (B)  upper bound. (C) range. (D)  extraction. 5

**Source:** DOC-31 · page 4 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 2  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Write the memory-layout formula, subtract the lower bounds, apply row-major or column-major order, multiply by element width when provided, then add the base address.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q112

> The largest element of an array index is called its (A)  lower bound. (B)  range. (C)  upper bound. (D)  All of these.

**Source:** DOC-31 · page 13 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 2  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Write the memory-layout formula, subtract the lower bounds, apply row-major or column-major order, multiply by element width when provided, then add the base address.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q137

> What is a linear array? Explain how two dimensional arrays are represented in memory. (8)

**Source:** DOC-31 · page 64 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 8  
**Priority:** P3  
**Difficulty:** D1  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Write the memory-layout formula, subtract the lower bounds, apply row-major or column-major order, multiply by element width when provided, then add the base address.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Array manipulation

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Array manipulation → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q138

> Write an algorithm to merge two sorted arrays into a third array. Do not sort the third array. (8)

**Source:** DOC-31 · page 64 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 8  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Write the memory-layout formula, subtract the lower bounds, apply row-major or column-major order, multiply by element width when provided, then add the base address.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



# MASTER PATTERN — Sparse Matrix — Implementation and Usage

# Sparse Matrix — Implementation and Usage

**Syllabus wording:** Sparse matrix — implementation and usage.

**Coverage:** 7 normalized unique source question(s), 20 retained occurrence(s).

## Subpattern map

1. **Triplet / 3-tuple representation** — 4 unique question(s)
2. **Sparse-matrix definition** — 1 unique question(s)
3. **Sparse storage / access / benefit** — 1 unique question(s)
4. **Sparse-matrix transpose** — 1 unique question(s)

---

## Triplet / 3-tuple representation

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Triplet / 3-tuple representation → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q094

> In which format(s) can we represent a sparse matrix (a) triplet format (b) CSR/YALE format (c) both (a) and (b) (d) none of these.

**Source:** DOC-01 · page 1 · Backlog / Special Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 1  
**Priority:** P2  
**Difficulty:** D1  
**Occurrences:** 2  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Write a header containing rows, columns and non-zero count, followed by one triple (row, column, value) for every non-zero cell in the source matrix.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q096

> 0  2  0  0 0  3  0  7  0 Compute its triplet array equivalent.  [(CO1) (Compute/LOCQ)] Is it beneficial to store this matrix as a triplet array? Justify your answer. [(CO1) (Contrast/IOCQ)]

**Source:** DOC-02 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P1  
**Difficulty:** D4  
**Occurrences:** 7  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: With one header triple plus one triple per non-zero element, storage is 3(k+1) scalar entries. Compare that with mn dense entries; use the inequality 3(k+1)<mn when that representation is intended.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q099

> The order of the triplet array representation of a 5 x 10 matrix which has 15 non-zero elements is ______.

**Source:** DOC-28 · page 5 · Practice / Problem Set  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D1  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Write a header containing rows, columns and non-zero count, followed by one triple (row, column, value) for every non-zero cell in the source matrix.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q100

> What is a sparse matrix? Given the following 4 × 5 matrix: 0 0 6 0 0 0 0 0 0 0 4 0 2 0 0 0 3 0 7 0 Compute its triplet array equivalent. Is it beneficial to store this matrix as a triplet array? Justify your answer.

**Source:** DOC-28 · page 6 · Practice / Problem Set  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D4  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: With one header triple plus one triple per non-zero element, storage is 3(k+1) scalar entries. Compare that with mn dense entries; use the inequality 3(k+1)<mn when that representation is intended.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Sparse-matrix definition

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Sparse-matrix definition → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q095

> What is a sparse matrix?     [(CO1) (Remember/LOCQ)] Given the following 4 × 5 matrix: 0  0  6  0  0 0  0  0  0  0

**Source:** DOC-02 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P1  
**Difficulty:** D1  
**Occurrences:** 7  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: A sparse matrix contains relatively few non-zero elements; the implementation stores non-zero information and its coordinates instead of every zero.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Sparse storage / access / benefit

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Sparse storage / access / benefit → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q098

> What is a Sparse matrix? How is a sparse matrix stored to avoid memory wastage? Show with a suitable example. (2 + 2 + 3) + (2 + 3) = 12

**Source:** DOC-25 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: With one header triple plus one triple per non-zero element, storage is 3(k+1) scalar entries. Compare that with mn dense entries; use the inequality 3(k+1)<mn when that representation is intended.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Sparse-matrix transpose

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Sparse-matrix transpose → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q154

> Explain an efficient way of storing a sparse matrix in memory.  Write a module to find the transpose of a sparse matrix stored in this way. (10)

**Source:** DOC-31 · page 17 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 10  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Replace each stored triple (i,j,v) by (j,i,v). A fast transpose uses destination counts and starting positions to place entries directly.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



# MASTER PATTERN — Polynomial Representation Using Arrays

# Polynomial Representation Using Arrays

**Syllabus wording:** Array representation of polynomials.

**Coverage:** 2 normalized unique source question(s), 6 retained occurrence(s).

## Subpattern map

1. **Polynomial representation** — 1 unique question(s)
2. **Polynomial evaluation** — 1 unique question(s)

---

## Polynomial representation

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Polynomial representation → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q146

> How can you represent the polynomial 5x5 + 4x2 – 25x + 10 with array(s)? Additionally, if a singly linked list is used to represent this polynomial instead, would the arithmetic operations like addition/subtraction become more efficient? Provide your analysis. [(CO2,CO5)(Apply)/IOCQ)]

**Source:** DOC-13 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P1  
**Difficulty:** D3  
**Occurrences:** 5  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: For P=4x³+3x²−15x+45, Horner form is ((4x+3)x−15)x+45, requiring 3 multiplications and 3 additions/subtractions.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Polynomial evaluation

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Polynomial evaluation → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q147

> The minimum number of multiplications and additions required to evaluate the polynomial P = 4x3+3x2-15x+45 is (A)  6 & 3 (B)  4 & 2 (C)  3 & 3 (D)  8 & 3

**Source:** DOC-31 · page 5 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 2  
**Priority:** P3  
**Difficulty:** D3  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: For P=4x³+3x²−15x+45, Horner form is ((4x+3)x−15)x+45, requiring 3 multiplications and 3 additions/subtractions.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



# MASTER PATTERN — Singly Linked List

# Singly Linked List

**Syllabus wording:** Singly linked list.

**Coverage:** 38 normalized unique source question(s), 70 retained occurrence(s).

## Subpattern map

1. **Traversal / output tracing** — 3 unique question(s)
2. **Length / traversal** — 1 unique question(s)
3. **Deletion at end** — 1 unique question(s)
4. **Insertion at end** — 5 unique question(s)
5. **Split list** — 1 unique question(s)
6. **Search** — 1 unique question(s)
7. **Other singly-linked-list pattern** — 15 unique question(s)
8. **Insertion at front** — 2 unique question(s)
9. **Structure / node representation** — 3 unique question(s)
10. **Search suitability** — 2 unique question(s)
11. **Insertion after known node/value** — 2 unique question(s)
12. **Insertion at position** — 2 unique question(s)

---

## Traversal / output tracing

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Traversal / output tracing → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q001

> What does the following function do for a given Linked List with first node as head? void fun1(struct node* head) { if(head == NULL) return; fun1(head->next); printf("%d  ", head->data); } (a)  Print all nodes of linked lists (b)  Print all nodes of linked list in reverse order (c)  Print alternate nodes of Linked List (d)  Print alternate nodes in reverse order.

**Source:** DOC-01 · page 1 · Backlog / Special Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 1  
**Priority:** P2  
**Difficulty:** D2  
**Occurrences:** 2  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the exact singly-linked-list operation from the wording, preserve head→first node and last→NULL, make only the required pointer changes, and include traversal/search cost where necessary.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q006

> What is the output of the given function if the variable start points to the first node of the following linked list? 0->1->2->3->4->5->6->7->8->9->10 void fun(struct node* start) { if(start != NULL) { if(start->next != NULL&& start->next->next != NULL ) fun(start->next->next->next); printf("%d ", start->data); } } (a) 0 2 4 6 8 10 (b) 10 8 6 4 2 0 (c) 0 6 9 3 (d) 9 6 3 0

**Source:** DOC-02 · page 1 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 1  
**Priority:** P2  
**Difficulty:** D3  
**Occurrences:** 3  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: The recursive jumps are 0→3→6→9. Printing occurs after the recursive call, so output is 9 6 3 0.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q017

> What is the output of following function for start pointing to first node of the following linked list: 1->2->3->4->5->6?
> void fun(struct node* start)
> {
>     if(start == NULL)
>         return;
>     printf("%d ", start->data);
>     if(start->next != NULL )
>         fun(start->next->next);
>     printf("%d ", start->data);
> }
> (a) 1 4 6 6 4 1
> (b) 1 3 5 1 3 5
> (c) 1 2 3 5
> (d) 1 3 5 5 3 1

**Source:** DOC-28 · page 2 · Practice / Problem Set  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D3  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: The function visits 1, 3 and 5, printing each before and after the recursive call. Output: 1 3 5 5 3 1.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Length / traversal

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Length / traversal → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q003

> Explain your answer for each of the following questions: (i) You are given pointers to the first and last nodes of a singly linked list, which of the following operations are dependent on the length of the linked list?

**Source:** DOC-01 · page 2 · Backlog / Special Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D2  
**Occurrences:** 2  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Traverse from head to NULL and increment a counter once per node. O(n) time, O(1) extra space.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Deletion at end

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Deletion at end → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q004

> Delete the last element of the list

**Source:** DOC-01 · page 2 · Backlog / Special Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D2  
**Occurrences:** 2  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Empty list → no deletion; one node → head=NULL; otherwise find the penultimate node, free its successor, and set predecessor->next=NULL. O(n).

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Insertion at end

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Insertion at end → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q005

> Add a new element at the end of the list (ii) Considered that a pointer to a node X in a single linked list is given and the pointer to the head of the list is not given, can we delete the node X from given linked list?

**Source:** DOC-01 · page 3 · Backlog / Special Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D2  
**Occurrences:** 2  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Without the head/predecessor, the usual O(1) deletion trick works only when X is not the last node: copy the next node's data into X, bypass the next node, then delete it.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q014

> Write a function which will take any number n as its argument. The function will break this number into its individual digits and then store every single digit in a separate node thereby forming a linked list. The function must return the head node address of the created linked list at the end. (For example, if the number is 13579, then there will be 5 nodes in the list containing nodes with values 1, 3, 5, 7, 9). [(CO5)(Apply/HOCQ)]

**Source:** DOC-13 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P1  
**Difficulty:** D3  
**Occurrences:** 5  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the exact singly-linked-list operation from the wording, preserve head→first node and last→NULL, make only the required pointer changes, and include traversal/search cost where necessary.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q037

> Program to add a new node to the ascending order linked list. */

**Source:** DOC-30 · page 24 · Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Handle empty/head insertion, then traverse until the correct sorted position is found and splice the new node there. O(n) worst case.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q038

> A linear list of elements in which deletion can be done from one end (front) and insertion can take place only at the other end (rear) is known as a (A)  queue. (B)  stack. 4 (C)  tree. (D)  linked list.

**Source:** DOC-31 · page 3 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 2  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the exact singly-linked-list operation from the wording, preserve head→first node and last→NULL, make only the required pointer changes, and include traversal/search cost where necessary.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q047

> Write a complete programme in C to create a single linked list. Write functions to do the following operations (i)   Insert a new node at the end (ii)  Delete the first node (8)

**Source:** DOC-31 · page 65 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 8  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: If empty, stop. Otherwise temp=head; head=head->next; free(temp). O(1).

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Split list

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Split list → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q008

> Given a singly-linked list with an odd number of elements, develop a pseudo- code or C-code  to split it into two nearly equal sub-lists — one for the front half, and the other for the back half. The extra element should go in the front list. [(CO3) (Develop/HOCQ)]

**Source:** DOC-02 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D4  
**Occurrences:** 3  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Locate the split with slow/fast traversal, put the extra odd node in the front half as required, terminate the front list with NULL, and return both heads.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Search

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Search → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q013

> In the worst case, the number of comparisons needed to search for a key in a singly linked list of length n is: (a) log2n (b) n/2 (c) log2n – 1 (d) n

**Source:** DOC-13 · page 1 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 1  
**Priority:** P1  
**Difficulty:** D2  
**Occurrences:** 5  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Traverse from head to NULL and increment a counter once per node. O(n) time, O(1) extra space.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Other singly-linked-list pattern

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Other singly-linked-list pattern → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q015

> Write an algorithm to reverse a single-linked list.

**Source:** DOC-22 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D2  
**Occurrences:** 2  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Use prev, cur and next. Save cur->next, set cur->next=prev, then advance prev and cur. Finish with head=prev. O(n) time, O(1) auxiliary space.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q018

> A linked list having n nodes (n >= 1) where no node stores a NULL pointer is a ____________ linked list.

**Source:** DOC-28 · page 5 · Practice / Problem Set  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P1  
**Difficulty:** D2  
**Occurrences:** 8  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the exact singly-linked-list operation from the wording, preserve head→first node and last→NULL, make only the required pointer changes, and include traversal/search cost where necessary.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q020

> Explain what will be the output when fibo(5) is called: LINKED LIST

**Source:** DOC-28 · page 8 · Practice / Problem Set  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D3  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the exact singly-linked-list operation from the wording, preserve head→first node and last→NULL, make only the required pointer changes, and include traversal/search cost where necessary.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q025

> If you are using C language to implement the heterogeneous linked list, what pointer type will you use?

**Source:** DOC-30 · page 1 · Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Use a void* pointer for generic data, with separate type information to interpret the pointed object correctly.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q027

> Write an algorithm to traverse a linked list. Answer : 1. Set PTR : = START 2. Repeat steps 3 and 4 while PTR is not equal to NULL. 3. Apply PROCESS to INFO [ PTR] 4. Set PTR: = LINK[PTR] 5. Exit

**Source:** DOC-30 · page 9 · Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the exact singly-linked-list operation from the wording, preserve head→first node and last→NULL, make only the required pointer changes, and include traversal/search cost where necessary.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q028

> What is a linked list? Ans :Linked list is a data structure which store same kind of data elements but not in continuous memory locations and size is not fixed. The linked lists are related logically.

**Source:** DOC-30 · page 11 · Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the exact singly-linked-list operation from the wording, preserve head→first node and last→NULL, make only the required pointer changes, and include traversal/search cost where necessary.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q033

> Write the syntax for pointing to next node? Ans : Syntax: node->link=node1;

**Source:** DOC-30 · page 12 · Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the exact singly-linked-list operation from the wording, preserve head→first node and last→NULL, make only the required pointer changes, and include traversal/search cost where necessary.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q036

> Explain circularly linked lists.

**Source:** DOC-30 · page 22 · Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the exact singly-linked-list operation from the wording, preserve head→first node and last→NULL, make only the required pointer changes, and include traversal/search cost where necessary.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q041

> What data structure would you mostly likely see in a nonrecursive implementation of a recursive algorithm? (A) Stack (B) Linked list (C) Queue (D) Trees 7

**Source:** DOC-31 · page 6 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 2  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the exact singly-linked-list operation from the wording, preserve head→first node and last→NULL, make only the required pointer changes, and include traversal/search cost where necessary.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q042

> A linear collection of data elements where the linear node is given by means of pointer is called (A)  linked list (B)  node list (C)  primitive list (D)  None of these

**Source:** DOC-31 · page 8 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 2  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the exact singly-linked-list operation from the wording, preserve head→first node and last→NULL, make only the required pointer changes, and include traversal/search cost where necessary.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q043

> Two linked lists contain information of the same type in ascending order. Write a module to merge them to a single linked list that is sorted. (7)

**Source:** DOC-31 · page 21 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 7  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the exact singly-linked-list operation from the wording, preserve head→first node and last→NULL, make only the required pointer changes, and include traversal/search cost where necessary.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q044

> Which sorting algorithm is easily adaptable to singly linked lists? Explain your answer. (4)

**Source:** DOC-31 · page 40 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 4  
**Priority:** P3  
**Difficulty:** D1  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Insertion Sort is naturally adaptable to singly linked lists because the already-sorted portion can be maintained by pointer insertion without array shifting.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q048

> Define a sparse metrics. Explain the representation of a 4X4 matrix using linked list. (8)

**Source:** DOC-31 · page 66 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 8  
**Priority:** P3  
**Difficulty:** D1  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the exact singly-linked-list operation from the wording, preserve head→first node and last→NULL, make only the required pointer changes, and include traversal/search cost where necessary.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q049

> Write a procedure to reverse a singly linked list. (8)

**Source:** DOC-31 · page 77 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 8  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Use prev, cur and next. Save cur->next, set cur->next=prev, then advance prev and cur. Finish with head=prev. O(n) time, O(1) auxiliary space.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q056

> What is the output of following function for start pointing to first node of the following linked list: 1->2->3->4->5->6? (a) 1 4 6 6 4 1 (b) 1 3 5 1 3 5 (c) 1 2 3 5 (d) 1 3 5 5 3 1

**Source:** DOC-10 · page 1 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 1  
**Priority:** P2  
**Difficulty:** D3  
**Occurrences:** 3  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the exact singly-linked-list operation from the wording, preserve head→first node and last→NULL, make only the required pointer changes, and include traversal/search cost where necessary.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Insertion at front

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Insertion at front → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q016

> Given a pointer to the first node of a singly linked list, which of the following operation can be implemented in O(1) time? (I) Insertion at the front of the linked list (II) Insertion at the end of the linked list (III) Deletion of the front node of the linked list (IV) Deletion of the last node of the linked list (a) I and II (b) I and III (c) I, II and III (d) I, II and IV

**Source:** DOC-28 · page 1 · Practice / Problem Set  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: new->next=head; head=new. Works for empty and non-empty lists. O(1).

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q045

> Write an algorithm to insert a node in the beginning of the linked list. (7)

**Source:** DOC-31 · page 42 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 7  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: new->next=head; head=new. Works for empty and non-empty lists. O(1).

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Structure / node representation

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Structure / node representation → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q030

> What is a node? Ans :The data element of a linked list is called a node.

**Source:** DOC-30 · page 11 · Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D1  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: A singly-linked-list node contains a data field and a next pointer. The last node's next is NULL; head identifies the first node.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q031

> What does node consist of? Ans :Node consists of two fields: data field to store the element and link field to store the address of the next node.

**Source:** DOC-30 · page 11 · Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D3  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: A singly-linked-list node contains a data field and a next pointer. The last node's next is NULL; head identifies the first node.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q034

> How do you create an empty linked list?

**Source:** DOC-30 · page 19 · Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Set head = NULL.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Search suitability

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Search suitability → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q035

> Name some operations on Linked Lists. The main operations that are performed on a linked list are the following:  Traversing and searching    Inserting    Deleting  

**Source:** DOC-30 · page 20 · Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Identify the exact singly-linked-list operation from the wording, preserve head→first node and last→NULL, make only the required pointer changes, and include traversal/search cost where necessary.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q057

> Linked lists are not suitable to implement __________ search.

**Source:** DOC-10 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 1  
**Priority:** P1  
**Difficulty:** D2  
**Occurrences:** 7  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Binary search, because a singly linked list does not provide O(1) random access to the middle.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Insertion after known node/value

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Insertion after known node/value → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q039

> Consider a linked list of n elements.  What is the time taken to insert an element after an element pointed by some pointer? (A) O (1) (B)  O ( ) n log2 (C) O (n) (D)  O ( ) n log n 2

**Source:** DOC-31 · page 4 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 2  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: When the node pointer is known, set new->next=current->next and current->next=new. If only a value is given, the search makes the overall cost O(n).

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q040

> In a linked list with n nodes, the time taken to insert an element after an element pointed by some pointer is (A) 0 (1) (B)  0 (log n) (C) 0 (n) (D)  0 (n 1og n)

**Source:** DOC-31 · page 6 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 2  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: When the node pointer is known, set new->next=current->next and current->next=new. If only a value is given, the search makes the overall cost O(n).

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Insertion at position

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Insertion at position → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q046

> Write an algorithm INSERT that takes a pointer to a sorted list and a pointer to a node and inserts the node into its correct position in the list. (8) 0 1 2 3 4 42 162 101 25 C 102 192 NULL 5 6 96 NULL NULL NULL NULL NULL 46

**Source:** DOC-31 · page 45 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Validate the position, handle front insertion separately, traverse to the predecessor, then splice the new node before the successor. Worst-case O(n).

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q050

> Write a procedure to insert a node into a linked list at a specific position and draw the same by taking any example? (8)

**Source:** DOC-31 · page 83 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 8  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Validate the position, handle front insertion separately, traverse to the predecessor, then splice the new node before the successor. Worst-case O(n).

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



# MASTER PATTERN — Circular Linked List

# Circular Linked List

**Syllabus wording:** Circular linked list.

**Coverage:** 6 normalized unique source question(s), 20 retained occurrence(s).

## Subpattern map

1. **Insertion at front** — 1 unique question(s)
2. **Head vs tail pointer** — 2 unique question(s)
3. **Deletion at front** — 1 unique question(s)
4. **Circular-list structure / invariant** — 2 unique question(s)

---

## Insertion at front

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Insertion at front → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q051

> Which of the following statements is correct for a circular singly linked list with only a start pointer? (a) Both insertion and deletion at the front end take O(1) time (b) Only insertion at the front end takes O(1) time (c) Only deletion from the front end takes O(1) time (d) No insertion or deletion operation at either end is possible in O(1) time

**Source:** DOC-02 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 1  
**Priority:** P1  
**Difficulty:** D2  
**Occurrences:** 8  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: With only a head pointer, front insertion requires repairing the last node's next link, so finding the last node makes it O(n). With a tail pointer it can be O(1).

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Head vs tail pointer

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Head vs tail pointer → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q052

> How is a circular linked list with a head pointer different from a circular linked list with a tail pointer? Which of the two would be better suited for implementing a queue and why?     [(CO5)(Analyze/IOCQ)]

**Source:** DOC-02 · page 3 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D4  
**Occurrences:** 3  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: With only a head pointer, the last node is not directly known. With a tail pointer, the head is tail->next, making queue-like designs convenient and allowing constant-time front/rear access in the appropriate representation.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q059

> How is a circular linked list with a head pointer different from a circular linked list with a tail pointer? Which of the two would be better suited for implementing a queue and why, provided the list is allowed to have only one external pointer? [(CO5)(Analyse/IOCQ)]

**Source:** DOC-10 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P1  
**Difficulty:** D4  
**Occurrences:** 4  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: With only a head pointer, the last node is not directly known. With a tail pointer, the head is tail->next, making queue-like designs convenient and allowing constant-time front/rear access in the appropriate representation.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Deletion at front

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Deletion at front → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q053

> Can you implement an algorithm, which can perform “delete at front” of a circular linked list in constant time? Justify your answer with proper reasoning. [(CO2, CO4)(Understand, Analyze/LOCQ)]

**Source:** DOC-03 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D4  
**Occurrences:** 3  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Delete the head and restore last->next to the new head. With head-only external state, locating last makes it O(n); with a tail pointer it can be O(1).

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Circular-list structure / invariant

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Circular-list structure / invariant → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q062

> In a circular linked list (A) components are all linked together in some sequential manner. (B) there is no beginning and no end. (C) components are arranged hierarchically. (D) forward and backward traversal within the list is permitted.

**Source:** DOC-31 · page 5 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 2  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: The defining invariant is last node → head, and traversal stops when the start node is reached again rather than at NULL.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q063

> What is the difference between a grounded header link list and a circular header link list? (3) 42

**Source:** DOC-31 · page 41 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D1  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: The defining invariant is last node → head, and traversal stops when the start node is reached again rather than at NULL.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



# MASTER PATTERN — Doubly Linked List

# Doubly Linked List

**Syllabus wording:** Doubly linked list.

**Coverage:** 8 normalized unique source question(s), 18 retained occurrence(s).

## Subpattern map

1. **In-place reversal** — 1 unique question(s)
2. **DLL structure / pointer invariants** — 5 unique question(s)
3. **Insertion** — 1 unique question(s)
4. **Deletion** — 1 unique question(s)

---

## In-place reversal

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**In-place reversal → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q007

> Construct a an iterative function in C named reverse() that accepts the start node of a doubly-linked list as argument and reverses the list. Your function must reverse the actual orientation of the nodes. It should not simply reverse the values stored in the list. Ideally, reverse() should only need to make one pass of the list.    [(CO3) (Construct/HOCQ)]

**Source:** DOC-02 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D4  
**Occurrences:** 3  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: Swap prev and next at each node and advance using the node's new prev pointer. Finish by exchanging head and tail. O(n) time and O(1) auxiliary space.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## DLL structure / pointer invariants

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**DLL structure / pointer invariants → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q066

> Deleting a node at the end of a double linked list, where head & tail both are known would take time — (a) O(1) (b) O(n) (c) O(logn) (d) O(nlogn).

**Source:** DOC-06 · page 1 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 1  
**Priority:** P1  
**Difficulty:** D2  
**Occurrences:** 4  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: With head and tail known, save the old tail, move tail to tail->prev, set the new tail's next to NULL, and free the old node. Handle the one-node case by setting both pointers to NULL. O(1).

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q067

> T(n) = O(log n200), F(n) = O(n0.999) (a) T(n) = O(F(n)) (b) T(n) = Ω(F(n)) (c) T(n) = Θ(F(n)) (d) None of the above.

**Source:** DOC-06 · page 1 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 1  
**Priority:** P1  
**Difficulty:** D2  
**Occurrences:** 4  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Each DLL node has data, prev and next. Every structural change must preserve both directions: if A.next=B then B.prev=A.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q073

> Deleting a node at the end of a double linked list, where head & tail both are known would take time: (a) O(1) (b) O(n) (c) O(log n) (d) O(n log n)

**Source:** DOC-28 · page 1 · Practice / Problem Set  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Solution: With head and tail known, save the old tail, move tail to tail->prev, set the new tail's next to NULL, and free the old node. Handle the one-node case by setting both pointers to NULL. O(1).

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q074

> What are doubly linked lists?

**Source:** DOC-30 · page 22 · Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Each DLL node has data, prev and next. Every structural change must preserve both directions: if A.next=B then B.prev=A.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q075

> Which of the following operations is performed more efficiently by doubly linked list than by singly linked list? (A) Deleting a node whose location in given (B) Searching of an unsorted list for a given item (C) Inverting a node after the node with given location (D) Traversing a list to process each node

**Source:** DOC-31 · page 12 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 2  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Each DLL node has data, prev and next. Every structural change must preserve both directions: if A.next=B then B.prev=A.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Insertion

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Insertion → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q070

> Write an algorithm to insert a node in the kth position of a doubly linked list.

**Source:** DOC-22 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D2  
**Occurrences:** 2  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Each DLL node has data, prev and next. Every structural change must preserve both directions: if A.next=B then B.prev=A.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Deletion

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Deletion → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q076

> The time required to delete a node x from a doubly linked list having n nodes is (A)  O (n) (B) O (log n) (C)  O (1) (D) O (n log n)

**Source:** DOC-31 · page 14 · Objective Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** 2  
**Priority:** P2  
**Difficulty:** D2  
**Occurrences:** 2  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Each DLL node has data, prev and next. Every structural change must preserve both directions: if A.next=B then B.prev=A.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



# MASTER PATTERN — Doubly Circular Linked List

# Doubly Circular Linked List

**Syllabus wording:** Doubly circular linked list.

**Coverage:** 0 normalized unique source question(s), 0 retained occurrence(s).

## Subpattern map

No retained source question was mapped to this topic.

# MASTER PATTERN — Linked-List Representation of Polynomial

# Linked-List Representation of Polynomial

**Syllabus wording:** Linked list representation of polynomial.

**Coverage:** 0 normalized unique source question(s), 0 retained occurrence(s).

## Subpattern map

No retained source question was mapped to this topic.

# MASTER PATTERN — Applications of Linked Lists

# Applications of Linked Lists

**Syllabus wording:** Applications.

**Coverage:** 5 normalized unique source question(s), 7 retained occurrence(s).

## Subpattern map

1. **Linked-list vs array / applications** — 4 unique question(s)
2. **Multilinked structure applications** — 1 unique question(s)

---

## Linked-list vs array / applications

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Linked-list vs array / applications → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q029

> What is the difference between an array and a linked list? Ans :The size of an array is fixed whereas size of linked list is variable. In array the data elements are stored in continuous memory locations but in linked list it is non continuous memory locations. Addition, removal of data is easy in linked list whereas in arrays it is complicated.

**Source:** DOC-30 · page 11 · Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Arrays provide contiguous storage and O(1) indexed access but may require resizing or shifting. Linked lists grow dynamically and support efficient pointer-known insertion/deletion, at the cost of pointer overhead and sequential access.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q085

> What are the limitations of arrays? Ans :The following are the limitations of arrays: Arrays are of fixed size. Data elements are stored in continuous memory locations which may not be available always. Adding and removing of elements is problematic because of shifting the locations.

**Source:** DOC-30 · page 11 · Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Arrays provide contiguous storage and O(1) indexed access but may require resizing or shifting. Linked lists grow dynamically and support efficient pointer-known insertion/deletion, at the cost of pointer overhead and sequential access.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q086

> How can you overcome the limitations of arrays? Ans :Limitations of arrays can be solved by using the linked list.

**Source:** DOC-30 · page 11 · Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Arrays provide contiguous storage and O(1) indexed access but may require resizing or shifting. Linked lists grow dynamically and support efficient pointer-known insertion/deletion, at the cost of pointer overhead and sequential access.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

#### Authentic Source Question — M1-Q148

> State the advantages and disadvantages of linked list over array. [(CO4)(Remember/LOCQ)]

**Source:** DOC-10 · page 2 · University Examination Paper  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P2  
**Difficulty:** D2  
**Occurrences:** 3  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Arrays provide contiguous storage and O(1) indexed access but may require resizing or shifting. Linked lists grow dynamically and support efficient pointer-known insertion/deletion, at the cost of pointer overhead and sequential access.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern



---

## Multilinked structure applications

### LEARN
Recognize the wording, identify the given information, then state the invariant/formula before acting.

### SEE
The exact source questions below are the worked corpus for this subpattern.

### CASES / EDGE CONDITIONS
Handle the relevant empty, one-element, head/tail, invalid-index, lower-bound, predecessor, successor, or circular-boundary case explicitly. Never assume the local update cost equals the total operation cost.

### EXAM TRIGGER
**Multilinked structure applications → identify the exact operation and use only the corresponding method.**

#### Authentic Source Question — M1-Q149

> List out few of the applications that make use of Multilinked Structures?

**Source:** DOC-30 · page 2 · Question Bank — Authority Unconfirmed  
**Year:** Not available in verified source.  
**Branch:** Not available in verified source.  
**Marks:** Not available in verified source.  
**Priority:** P3  
**Difficulty:** D2  
**Occurrences:** 1  
**Recurrence:** No verified year-based recurrence established.

##### Question-specific solution
Answer: Arrays provide contiguous storage and O(1) indexed access but may require resizing or shifting. Linked lists grow dynamically and support efficient pointer-known insertion/deletion, at the cost of pointer overhead and sequential access.

##### Exam-ready answer structure
Interpretation → required operation/calculation → final answer → complexity when requested.

##### Mastery check
□ recognize □ select pointers/indices □ state invariant □ execute □ handle edge case □ state complexity/result □ solve another wording in the same subpattern

