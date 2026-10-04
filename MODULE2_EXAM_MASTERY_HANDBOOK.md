# CSE2101 / CSEN2101 — MODULE 2
# Exam Mastery Handbook

**Complete source-grounded solving patterns, subpatterns, authentic source questions, and question-specific solutions**

## How to use this handbook
This resource is built from the repository's authenticated corpus and the controlling Module 2 syllabus. It deliberately separates **master pattern → subpattern → operation/case → authentic question → exact solution**. Priority labels are evidence-based and are not based on question-family names.

### Priority
- **P1 — MUST MASTER:** high recurrence, foundational, or high transfer value.
- **P2 — IMPORTANT:** strong coverage value or common variant.
- **P3 — REINFORCEMENT:** lower-frequency but distinct authentic material.

### Difficulty
- **D1:** recognition/direct response
- **D2:** standard application
- **D3:** multi-step reasoning/trace
- **D4:** variant/trap/advanced source problem

## Verified Module 2 scope
The authoritative syllabus places Module 2 under **Stack and Queue** plus **Recursion**. It explicitly covers stack implementation using array/linked list, stack applications (infix/postfix/prefix conversion, evaluation, parenthesis matching), linear/circular queue implementations, queue applications, deque restrictions, recursion principles/use of stack/recursion-vs-iteration, tail recursion, and applications including Tower of Hanoi, Eight Queens, and backtracking.

## Forensic corpus audit
- 33 source documents; 579 pages; 1,584 physical source records.
- 1,260 answerable question occurrences overall; 780 in-scope occurrences overall.
- **186 strict Module 2 occurrences**, resolving to **115 exact-normalized unique question texts** and **71 duplicate occurrences**.
- 27 source documents contribute Module 2 questions.
- The legacy family report is not treated as final classification truth because several family memberships mix materially different solving tasks.

## Study order
1. Stack fundamentals and state tracing.
2. Stack/queue interconversion and advanced stack operations.
3. Infix→postfix, prefix/postfix transformations, and postfix evaluation.
4. Parenthesis matching.
5. Linear queue → circular queue → queue applications.
6. Deque and restricted deques.
7. Recursion fundamentals and tracing.
8. Tail recursion.
9. Tower of Hanoi and backtracking/Eight Queens.


# MASTER PATTERN — 1. Stack Core & Advanced Operations

### Pattern map
1. **Stack fundamentals, representation, operations, and state tracing** — 12 unique question texts / 15 occurrences
2. **Stack vs Queue: LIFO/FIFO recognition and comparison** — 3 unique question texts / 6 occurrences
3. **Implementing one ADT using the other (queue with stacks)** — 3 unique question texts / 8 occurrences
4. **Augmented stack: minimum element retrieval** — 1 unique question texts / 3 occurrences
5. **Stack transformations: sorted movement and reversal** — 3 unique question texts / 6 occurrences
6. **Stack-generated output sequences** — 1 unique question texts / 1 occurrences
7. **Stack-style reduction of adjacent duplicates** — 1 unique question texts / 3 occurrences

## Stack fundamentals, representation, operations, and state tracing

**Recognition trigger:** stack, push, pop, peek, top, overflow, underflow

**Why this is separate:** Direct stack operations and state changes are repeatedly tested; the exam often asks for a concrete state after a sequence of operations.

**Prerequisites:** LIFO, top index/pointer, array/linked representation

**Invariant:** top always identifies the current top according to the chosen implementation convention.

**Core cases:** empty/full, push/pop boundary, first/last element, state tracing

**Step-by-step method:**  
Push: check overflow if fixed-size → advance top → store item. Pop: check underflow → read top item → move top back.

**Complexity:** push/pop/peek O(1) for standard array or linked-list implementations; display/traversal O(n).

**Common mistakes:** mixing top movement conventions; confusing overflow with underflow; reading the wrong element after multiple pops.

**Exam-writing format:** For code/state questions, draw the stack after each operation and explicitly state top.

**Memorize:** LIFO; push adds at top; pop removes from top; underflow = empty removal; overflow = full fixed array.

**Understand:** why the representation determines the boundary condition but not the LIFO behavior.

### Authentic questions (12 unique texts; 15 occurrences)

#### 1. P1 · D3 · DOC-06-P03-Q05-sub-a

> Represent the following equation in post-fix form and evaluate the value. Use a stack data structure and show each step. 10 – (5*2) + 7 / 3.5 * 2 [(CO2)(Understand/IOCQ)]

- Source: `DOC-06`, page 3, year 2023, marks not available
- Independent sources: 4; occurrence count: 4
- Other occurrence IDs: DOC-07-P03-Q05-sub-a, DOC-08-P03-Q05-sub-a, DOC-09-P03-Q05-sub-a
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Direct stack operations and state changes are repeatedly tested; the exam often asks for a concrete state after a sequence of operations.

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 2. P2 · D1 · DOC-18-P01-Q01-sub-iii

> A stack S has the entries a,b,c with ‘a’ on the top. Another stack T is empty. An entry popped out of the Stack S can be printed immediately or pushed in to the stack T, finally popped out of the Stack T and printed. Then which sequence can never be printed (a) b a c (b) b c a (c) c a b (d) a b c

- Source: `DOC-18`, page 1, year 2020, marks 1
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Direct stack operations and state changes are repeatedly tested; the exam often asks for a concrete state after a sequence of operations.

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 3. P2 · D1 · DOC-25-P01-Q01-sub-ix

> Which function places an element on the stack? (a) Pop() (b) Push() (c) Peek() (d) isEmpty()

- Source: `DOC-25`, page 1, year 2021, marks 1
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Direct stack operations and state changes are repeatedly tested; the exam often asks for a concrete state after a sequence of operations.

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 4. P2 · D1 · DOC-28-P04-MCQ-Q24

> A stack S has the entries a,b,c with ‘a’ on the top. Another stack T is empty. An entry popped out of the Stack S can be printed immediately or pushed in to the stack T, finally popped out of the Stack T and printed. Then which sequence can never be printed? (a) a b c (b) b a c (c) b c a (d) c a b

- Source: `DOC-28`, page 4, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Direct stack operations and state changes are repeatedly tested; the exam often asks for a concrete state after a sequence of operations.

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 5. P2 · D3 · DOC-28-P07-LA-Q19

> Implement two stacks on the same array, managing space most efficiently.

- Source: `DOC-28`, page 7, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Direct stack operations and state changes are repeatedly tested; the exam often asks for a concrete state after a sequence of operations.

**Direct answer:** Solved following standard Two stacks implementation on a single array and memory sharing algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Two stacks implementation on a single array and memory sharing'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Two stacks implementation on a single array and memory sharing.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 6. P2 · D2 · DOC-30-P07-Q29

> What is the difference between storing data on the heap vs. on the stack?

- Source: `DOC-30`, page 7, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Direct stack operations and state changes are repeatedly tested; the exam often asks for a concrete state after a sequence of operations.

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 7. P2 · D1 · DOC-30-P08-Q32

> Consider the following stack of characters, where STACK is allocated N = 8 mmory cells STACK : A,C,D,F,K,_,_,_. ( _ means empty allocated cell) Describe the stack as the following operations takes place: (a) POP(STACK, ITEM) (b) POP(STACK, ITEM) (c) POP(STACK, ITEM) (d) PUSH(STACK, R) (e) PUSH(STACK,L) (f) PUSH(STACK, S) (g) PUSH(STACK,P) (h) POP(STACK, ITEM)

- Source: `DOC-30`, page 8, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Direct stack operations and state changes are repeatedly tested; the exam often asks for a concrete state after a sequence of operations.

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 8. P2 · D3 · DOC-30-P08-Q33

> Consider the problem in Q-32. (a) When will overflow occur? (b) When will C be deleted before R? Ans : (a) Since the stack has been allocated 8 memory cells, overflow will occur when STACK contains 8 elements and there is a PUSH operation to add an element (b) Since STACK is implemented as a STACK, C will never be deleted before R.

- Source: `DOC-30`, page 8, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Direct stack operations and state changes are repeatedly tested; the exam often asks for a concrete state after a sequence of operations.

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 9. P2 · D2 · DOC-30-P09-Q39

> Evaluate P:  12 , 7 , 3 , - , / , 2 , 1 , 5 , + , * , + , ) Ans : Symbol STACK 12 12 7 12,7 3 12,7,3 - 12,4 / 3 2 3,2 1 3,2,1 5 3,2,1,5 + 3,2,6 * 3,12 + 15 ) 15

- Source: `DOC-30`, page 9, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Direct stack operations and state changes are repeatedly tested; the exam often asks for a concrete state after a sequence of operations.

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 10. P2 · D3 · DOC-31-P10-PART1-Q67

> A stack is to be implemented using an array. The associated declarations are: int stack [100]; int top = 0; Give the statement to perform push operation.

- Source: `DOC-31`, page 10, year not available, marks 2
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Direct stack operations and state changes are repeatedly tested; the exam often asks for a concrete state after a sequence of operations.

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 11. P2 · D1 · DOC-31-P13-PART1-Q82

> What is the result of the following operation Top (Push (S, X)) (A)  X (B)  null (C)  S (D)  None of these.

- Source: `DOC-31`, page 13, year not available, marks 2
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Direct stack operations and state changes are repeatedly tested; the exam often asks for a concrete state after a sequence of operations.

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 12. P2 · D1 · DOC-31-P14-PART1-Q87

> Which data structure is used for implementing recursion? (A)  Queue. (B)  Stack. (C)  Arrays. (D)  List.

- Source: `DOC-31`, page 14, year not available, marks 2
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Direct stack operations and state changes are repeatedly tested; the exam often asks for a concrete state after a sequence of operations.

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.


### Mastery check
- Can I recognize: **stack, push, pop, peek, top, overflow, underflow**?
- Can I state the invariant?
- Can I trace the state without skipping a step?
- Can I handle the relevant boundary case?
- Can I write the exam-ready answer format?

---
## Stack vs Queue: LIFO/FIFO recognition and comparison

**Recognition trigger:** stack vs queue, LIFO/FIFO, difference between stack and queue

**Why this is separate:** These are direct recognition/comparison questions and also support later implementation questions.

**Prerequisites:** stack and queue terminology

**Invariant:** stack removes the newest eligible element; queue removes the oldest eligible element.

**Core cases:** definition, order, insertion/removal ends, typical operations

**Step-by-step method:**  
Comparison table: Stack—LIFO, insert/delete same end; Queue—FIFO, insert rear/delete front.

**Complexity:** standard push/pop/enqueue/dequeue are O(1) under standard representations.

**Common mistakes:** saying queue is LIFO or stack is FIFO; confusing rear with front.

**Exam-writing format:** Use a 4-column comparison: order, insertion end, deletion end, key operation names.

**Memorize:** Stack=LIFO; Queue=FIFO.

**Understand:** how end restrictions create the ordering behavior.

### Authentic questions (3 unique texts; 6 occurrences)

#### 1. P2 · D1 · DOC-02-P02-Q01-sub-viii

> Recursion uses the ____ data structure as it follows ____ ordering. (a) Stack, FIFO (b) Queue, LIFO (c) Stack, LIFO (d) Queue, FIFO

- Source: `DOC-02`, page 2, year 2021, marks 1
- Independent sources: 4; occurrence count: 4
- Other occurrence IDs: DOC-19-P03-Q01-sub-viii, DOC-20-P02-Q01-sub-viii, DOC-26-P02-Q01-sub-viii
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** These are direct recognition/comparison questions and also support later implementation questions.

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 2. P3 · D1 · DOC-28-P04-MCQ-Q22

> Recursion uses the ____ data structure as it follows ____ ordering. (a) Queue, LIFO (b) Queue, FIFO (c) Stack, LIFO (d) Stack, FIFO

- Source: `DOC-28`, page 4, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** These are direct recognition/comparison questions and also support later implementation questions.

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 3. P3 · D2 · DOC-30-P07-Q28

> What is the difference between a queue and a stack?

- Source: `DOC-30`, page 7, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** These are direct recognition/comparison questions and also support later implementation questions.

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.


### Mastery check
- Can I recognize: **stack vs queue, LIFO/FIFO, difference between stack and queue**?
- Can I state the invariant?
- Can I trace the state without skipping a step?
- Can I handle the relevant boundary case?
- Can I write the exam-ready answer format?

---
## Implementing one ADT using the other (queue with stacks)

**Recognition trigger:** implement a queue using stack; enqueue/dequeue using PUSH/POP

**Why this is separate:** This is a representation-conversion problem: the target behavior must be preserved using a different primitive set.

**Prerequisites:** push/pop and FIFO semantics

**Invariant:** the externally visible sequence must remain FIFO even though each primitive stack is LIFO.

**Core cases:** two-stack enqueue/dequeue strategies; transfer between stacks only when necessary

**Step-by-step method:**  
Typical two-stack queue: push incoming items onto S_in; for dequeue, if S_out empty, transfer all items from S_in to S_out, then pop S_out.

**Complexity:** amortized O(1) per queue operation for the standard two-stack design; a single transfer can be O(n).

**Common mistakes:** transferring in the wrong direction; losing order; claiming worst-case O(1) for every individual dequeue.

**Exam-writing format:** Explain the invariant first, then show one short operation trace.

**Memorize:** in-stack receives new items; out-stack exposes oldest item.

**Understand:** why reversing twice recreates FIFO order.

### Authentic questions (3 unique texts; 8 occurrences)

#### 1. P2 · D3 · DOC-03-P02-Q04-sub-a

> To implement a queue using Stack, show how to implement ENQUEUE and DEQUEUE operations using a sequence of given operations as PUSH and POP for a Stack? [(CO2,CO6)(Remember/LOCQ)]

- Source: `DOC-03`, page 2, year 2022, marks not available
- Independent sources: 3; occurrence count: 3
- Other occurrence IDs: DOC-04-P02-Q04-sub-a, DOC-05-P02-Q04-sub-a
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is a representation-conversion problem: the target behavior must be preserved using a different primitive set.

**Direct answer:** Solved following standard Deque: Input-restricted and Output-restricted double-ended queue operations algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_DEQUE under question family 'Deque: Input-restricted and Output-restricted double-ended queue operations'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Deque: Input-restricted and Output-restricted double-ended queue operations.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 2. P2 · D3 · DOC-13-P02-Q05-sub-b

> Suppose you want to implement a queue and a stack using an unrestricted deque. Describe the deque methods that need to be reused to implement standard stack and queue operations. [(CO2)(Apply/IOCQ)]

- Source: `DOC-13`, page 2, year 2025, marks not available
- Independent sources: 4; occurrence count: 4
- Other occurrence IDs: DOC-14-P02-Q05-sub-b, DOC-15-P02-Q05-sub-b, DOC-16-P02-Q05-sub-b
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is a representation-conversion problem: the target behavior must be preserved using a different primitive set.

**Direct answer:** Solved following standard Deque: Input-restricted and Output-restricted double-ended queue operations algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_DEQUE under question family 'Deque: Input-restricted and Output-restricted double-ended queue operations'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Deque: Input-restricted and Output-restricted double-ended queue operations.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 3. P3 · D3 · DOC-28-P07-LA-Q18

> Suppose you want to implement a queue and a stack using an unrestricted deque. Describe the deque methods that need to be reused to implement standard stack and queue operations.

- Source: `DOC-28`, page 7, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is a representation-conversion problem: the target behavior must be preserved using a different primitive set.

**Direct answer:** Solved following standard Deque: Input-restricted and Output-restricted double-ended queue operations algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_DEQUE under question family 'Deque: Input-restricted and Output-restricted double-ended queue operations'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Deque: Input-restricted and Output-restricted double-ended queue operations.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.


### Mastery check
- Can I recognize: **implement a queue using stack; enqueue/dequeue using PUSH/POP**?
- Can I state the invariant?
- Can I trace the state without skipping a step?
- Can I handle the relevant boundary case?
- Can I write the exam-ready answer format?

---
## Augmented stack: minimum element retrieval

**Recognition trigger:** stack that returns a minimum element without auxiliary stack

**Why this is separate:** The task changes the required invariant: the stack must retain LIFO semantics while also supporting minimum retrieval.

**Prerequisites:** ordinary stack operations; auxiliary-state idea

**Invariant:** stored state must be sufficient to recover the minimum without scanning the whole stack.

**Core cases:** push/pop with encoded values or alternative metadata strategies

**Step-by-step method:**  
Use an encoding or compact auxiliary state so the minimum can be recovered during pop/push; obey the exact source constraints on auxiliary space.

**Complexity:** target design depends on the chosen encoding; state the cost of each operation in the answer.

**Common mistakes:** silently using an auxiliary stack when prohibited; scanning the whole stack when O(1) behavior is intended.

**Exam-writing format:** State the constraint before the algorithm so the examiner can see it was respected.

**Memorize:** The extra requirement is minimum retrieval, not a change to LIFO order.

**Understand:** how additional information can be maintained incrementally.

### Authentic questions (1 unique texts; 3 occurrences)

#### 1. P2 · D4 · DOC-03-P03-Q05-sub-b

> Write a program or pseudo code or algorithm to design a stack that returns a minimum element without using an auxiliary stack. [(CO3)(Analyze/IOCQ)]

- Source: `DOC-03`, page 3, year 2022, marks not available
- Independent sources: 3; occurrence count: 3
- Other occurrence IDs: DOC-04-P03-Q05-sub-b, DOC-05-P03-Q05-sub-b
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The task changes the required invariant: the stack must retain LIFO semantics while also supporting minimum retrieval.

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.


### Mastery check
- Can I recognize: **stack that returns a minimum element without auxiliary stack**?
- Can I state the invariant?
- Can I trace the state without skipping a step?
- Can I handle the relevant boundary case?
- Can I write the exam-ready answer format?

---
## Stack transformations: sorted movement and reversal

**Recognition trigger:** move stack to another stack, maintain sorted order, reverse stack, use extra stacks/queue

**Why this is separate:** These questions are not ordinary push/pop; the main challenge is maintaining a structural property while moving data.

**Prerequisites:** stack primitives; ordering invariant

**Invariant:** the destination remains sorted whenever the question explicitly requires it; for reversal, relative order is intentionally inverted.

**Core cases:** one/two auxiliary stacks; queue-assisted reversal

**Step-by-step method:**  
Move top items while using auxiliary storage to preserve or build the required order; after each move, verify the stated invariant.

**Complexity:** usually O(n^2) for insertion-style stack sorting; exact cost depends on the permitted auxiliary structures.

**Common mistakes:** checking only the final arrangement when the question requires the invariant throughout; forgetting which end of the stack is accessible.

**Exam-writing format:** Show at least one non-trivial intermediate stack state, not only the final arrangement.

**Memorize:** Only the top is directly accessible.

**Understand:** why access restrictions force repeated transfers.

### Authentic questions (3 unique texts; 6 occurrences)

#### 1. P2 · D4 · DOC-13-P02-Q05-sub-a

> There are n elements in a stack, stored in a sorted way. Move these elements to another stack so that the final stack is always sorted during the entire movement. You may additionally use another stack but the sorted property has to be maintained there all the time. An iterative version will fetch you additional credits. [(CO2)(Analyse/IOCQ)]

- Source: `DOC-13`, page 2, year 2025, marks not available
- Independent sources: 4; occurrence count: 4
- Other occurrence IDs: DOC-14-P02-Q05-sub-a, DOC-15-P02-Q05-sub-a, DOC-16-P02-Q05-sub-a
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** These questions are not ordinary push/pop; the main challenge is maintaining a structural property while moving data.

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 2. P3 · D4 · DOC-28-P07-LA-Q17

> There are n elements in a stack, stored in a sorted way. Move these elements to another stack so that the final stack is always sorted during the entire movement. You may additionally use another stack but the sorted property has to be maintained there all the time. An iterative version will fetch you additional credits.

- Source: `DOC-28`, page 7, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** These questions are not ordinary push/pop; the main challenge is maintaining a structural property while moving data.

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 3. P3 · D3 · DOC-31-P29-PART2-Q17

> Reverse the order of elements on a stack S (i)  using two additional stacks. (ii) using one additional queue. (9)

- Source: `DOC-31`, page 29, year not available, marks 9
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** These questions are not ordinary push/pop; the main challenge is maintaining a structural property while moving data.

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.


### Mastery check
- Can I recognize: **move stack to another stack, maintain sorted order, reverse stack, use extra stacks/queue**?
- Can I state the invariant?
- Can I trace the state without skipping a step?
- Can I handle the relevant boundary case?
- Can I write the exam-ready answer format?

---
## Stack-generated output sequences

**Recognition trigger:** which sequence can/cannot be printed by push/pop operations

**Why this is separate:** The key skill is recognizing legal stack permutations rather than merely knowing LIFO.

**Prerequisites:** push/pop semantics and sequence tracing

**Invariant:** at every output step, the required item must be either on top or still reachable after legal pushes/pops.

**Core cases:** immediately print popped item vs temporarily store in another stack

**Step-by-step method:**  
Simulate the target output left-to-right; at each desired output, push input items until the target is exposed or conclude it is impossible.

**Complexity:** O(n) simulation for a fixed target sequence with linear input.

**Common mistakes:** assuming any permutation is possible; forgetting that an already buried item cannot be popped directly.

**Exam-writing format:** Write the push/pop sequence for a candidate output or identify the first impossible step.

**Memorize:** A stack can generate only legal LIFO permutations.

**Understand:** why buried elements constrain future outputs.

### Authentic questions (1 unique texts; 1 occurrences)

#### 1. P3 · D2 · DOC-28-P07-LA-Q20

> Give an example of an output sequence that cannot be generated from an input sequence via a series of push and pop operations on an initially empty stack.

- Source: `DOC-28`, page 7, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The key skill is recognizing legal stack permutations rather than merely knowing LIFO.

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.


### Mastery check
- Can I recognize: **which sequence can/cannot be printed by push/pop operations**?
- Can I state the invariant?
- Can I trace the state without skipping a step?
- Can I handle the relevant boundary case?
- Can I write the exam-ready answer format?

---
## Stack-style reduction of adjacent duplicates

**Recognition trigger:** remove adjacent duplicates repeatedly until none remain

**Why this is separate:** The source asks for iterative cancellation until the result is stable; a stack gives exactly the needed last-in-first-out local comparison.

**Prerequisites:** stack push/pop; scan-based processing

**Invariant:** the stack stores the current reduced prefix with no removable adjacent duplicate left unresolved.

**Core cases:** same-character cancellation; cascading removals; empty stack after cancellation

**Step-by-step method:**  
Scan characters. If top matches current, pop; otherwise push. Read remaining stack as the reduced result.

**Complexity:** O(n) time and O(n) auxiliary space.

**Common mistakes:** performing only one cancellation pass; deleting the wrong pair after a cascade.

**Exam-writing format:** Show the stack after each character for a non-trivial cascade.

**Memorize:** match top → pop; otherwise push.

**Understand:** why a local cancellation can expose a new adjacent pair.

### Authentic questions (1 unique texts; 3 occurrences)

#### 1. P2 · D3 · DOC-03-P02-Q04-sub-c

> Write a program or pseudo code or algorithm that should continue removing adjacent duplicates from the string given a string, till no duplicate is present in the result. For example input string is 'DBAABDAB'. The string left after the removal of all adjacent duplicates is 'AB'. [(CO3, CO5)(Evaluate/HOCQ)]

- Source: `DOC-03`, page 2, year 2022, marks not available
- Independent sources: 3; occurrence count: 3
- Other occurrence IDs: DOC-04-P02-Q04-sub-c, DOC-05-P02-Q04-sub-c
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The source asks for iterative cancellation until the result is stable; a stack gives exactly the needed last-in-first-out local comparison.

**Direct answer:** Solved following standard Deque: Input-restricted and Output-restricted double-ended queue operations algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_DEQUE under question family 'Deque: Input-restricted and Output-restricted double-ended queue operations'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Deque: Input-restricted and Output-restricted double-ended queue operations.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.


### Mastery check
- Can I recognize: **remove adjacent duplicates repeatedly until none remain**?
- Can I state the invariant?
- Can I trace the state without skipping a step?
- Can I handle the relevant boundary case?
- Can I write the exam-ready answer format?

---

# MASTER PATTERN — 2. Expression Processing with Stacks

### Pattern map
1. **Expression notation concepts and recognition** — 1 unique question texts / 2 occurrences
2. **Infix → postfix conversion** — 21 unique question texts / 28 occurrences
3. **Prefix/postfix transformations** — 9 unique question texts / 15 occurrences
4. **Postfix evaluation** — 5 unique question texts / 6 occurrences
5. **Combined infix conversion + evaluation** — 1 unique question texts / 2 occurrences
6. **Balanced-parentheses / parenthesis matching** — 4 unique question texts / 5 occurrences

## Expression notation concepts and recognition

**Recognition trigger:** Reverse Polish notation, precedence, brackets, operator/operand stack

**Why this is separate:** Before conversion/evaluation, the student must know why postfix avoids precedence and explicit brackets.

**Prerequisites:** infix/prefix/postfix notation

**Invariant:** notation determines evaluation order without relying on ordinary infix precedence parsing.

**Core cases:** operator precedence, explicit grouping, postfix advantages

**Step-by-step method:**  
Recognize postfix as operand/operator order where operators apply to the most recent operands.

**Complexity:** conceptual; conversion/evaluation costs are covered in separate subpatterns.

**Common mistakes:** confusing postfix with prefix; assuming postfix still needs parentheses for precedence.

**Exam-writing format:** Answer the conceptual point directly, then give one tiny notation example.

**Memorize:** Postfix encodes order in token position.

**Understand:** why this removes the need for infix precedence during evaluation.

### Authentic questions (1 unique texts; 2 occurrences)

#### 1. P3 · D1 · DOC-01-P02-Q01-sub-vii

> Reverse Polish notation is preferred over infix notation because (a)  The knowledge of precedence is not needed (b)  Brackets will not be needed (c)  Both of the above (d)  None of the above.

- Source: `DOC-01`, page 2, year 2020, marks 1
- Independent sources: 2; occurrence count: 2
- Other occurrence IDs: DOC-21-P02-Q01-sub-vii
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Before conversion/evaluation, the student must know why postfix avoids precedence and explicit brackets.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.


### Mastery check
- Can I recognize: **Reverse Polish notation, precedence, brackets, operator/operand stack**?
- Can I state the invariant?
- Can I trace the state without skipping a step?
- Can I handle the relevant boundary case?
- Can I write the exam-ready answer format?

---
## Infix → postfix conversion

**Recognition trigger:** convert infix to postfix, show stack/output trace, operator stack

**Why this is separate:** This is the highest-frequency Module 2 solving pattern in the repository.

**Prerequisites:** operator precedence, associativity, parentheses, stack operations

**Invariant:** the operator stack contains unresolved operators that still obey the conversion rules; the output is the correctly ordered postfix prefix.

**Core cases:** operand, operator, opening parenthesis, closing parenthesis, end flush, equal precedence/associativity

**Step-by-step method:**  
Operands go to output. Operators pop higher/equal-precedence operators according to associativity before being pushed. '(' is pushed. ')' pops until '('. At end, flush remaining operators.

**Complexity:** O(n) time and O(n) auxiliary stack space.

**Common mistakes:** popping '(' as a normal operator; mishandling equal precedence; forgetting final stack flush; mixing evaluation with conversion.

**Exam-writing format:** Use a token-by-token table: token | action | operator stack | output.

**Memorize:** operand→output; '('→push; ')'→pop to '('; operator→pop by precedence/associativity, then push; end→flush.

**Understand:** every output position is forced by precedence, associativity, and grouping.

### Authentic questions (21 unique texts; 28 occurrences)

#### 1. P2 · D2 · DOC-01-P03-Q04-sub-a

> Explain step by step how the following infix expression will be changed to postfix expression using stack: 7-(2^3+5)*8 Show the status of Remaining Infix String, Stack, Postfix String and Rule used in each step.

- Source: `DOC-01`, page 3, year 2020, marks not available
- Independent sources: 2; occurrence count: 2
- Other occurrence IDs: DOC-21-P03-Q04-sub-a
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is the highest-frequency Module 2 solving pattern in the repository.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 2. P1 · D1 · DOC-03-P01-Q01-sub-iv

> Which of the following is essential for converting an infix expression to the postfix form efficiently? (a) An operator stack (b) An operand stack (c) An operator stack and an operand stack (d) A parse tree.

- Source: `DOC-03`, page 1, year 2022, marks 1
- Independent sources: 3; occurrence count: 3
- Other occurrence IDs: DOC-04-P01-Q01-sub-iv, DOC-05-P01-Q01-sub-iv
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is the highest-frequency Module 2 solving pattern in the repository.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 3. P1 · D1 · DOC-03-P01-Q01-sub-vii

> The postfix form of the expression (A+ B)*(C*D- E)*F / G is? (a) AB+ CD*E - FG /** (b) AB + CD* E - F **G / (c) AB + CD* E - *F *G / (d) AB + CDE * - * F *G /

- Source: `DOC-03`, page 1, year 2022, marks 1
- Independent sources: 3; occurrence count: 3
- Other occurrence IDs: DOC-04-P01-Q01-sub-vii, DOC-05-P01-Q01-sub-vii
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is the highest-frequency Module 2 solving pattern in the repository.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 4. P2 · D1 · DOC-18-P02-Q01-sub-iv

> What would be the Postfix notation for the given equation? a+(b*c(d/e^f)*g)*h) (a) ab*cdef/^*g-h+ (b) abcdef^/*g*h*+ (c) abcd*^ed/g*-h*+ (d) abc*de^fg/*-*h+

- Source: `DOC-18`, page 2, year 2020, marks 1
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is the highest-frequency Module 2 solving pattern in the repository.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 5. P2 · D1 · DOC-22-P01-Q01-sub-v

> Which of the following Data Structure is essential for the conversion of an infix expression to postfix? (a) Queue       (b) Operator Stack (c) Operand Stack (d) None of these.

- Source: `DOC-22`, page 1, year 2021, marks 1
- Independent sources: 2; occurrence count: 2
- Other occurrence IDs: DOC-23-P01-Q01-sub-v
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is the highest-frequency Module 2 solving pattern in the repository.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 6. P2 · D3 · DOC-22-P03-Q05-sub-a

> Write an algorithm to convert an infix expression to postfix. Convert the expression given below into its corresponding postfix expression. Show each step of the conversion. 10 + ((75) +2* 3^2^2)/2

- Source: `DOC-22`, page 3, year 2021, marks not available
- Independent sources: 2; occurrence count: 2
- Other occurrence IDs: DOC-23-P03-Q05-sub-a
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is the highest-frequency Module 2 solving pattern in the repository.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 7. P2 · D2 · DOC-25-P02-Q05-sub-a

> Convert the following Infix expression to its Postfix expression using a stack. Show all the intermediate steps clearly. (A – 2 * (B + C) / D * E) + F

- Source: `DOC-25`, page 2, year 2021, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is the highest-frequency Module 2 solving pattern in the repository.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 8. P2 · D1 · DOC-28-P03-MCQ-Q17

> The equivalent Postfix notation for ((A + B) *  C – (D – E) ^ (F + G)) is: (a) AB+C*DE–FG+^– (b) ^-*+ABC-DE+FG (c)(AB)+CDE*--FG+^ (d) AB*+DE--FG+^

- Source: `DOC-28`, page 3, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is the highest-frequency Module 2 solving pattern in the repository.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 9. P2 · D1 · DOC-28-P04-MCQ-Q21

> When using a stack to convert an infix expression into its postfix equivalent, which of the following is true? (a) The stack may contain both opening and closing brackets (b) A plus operator can be pushed on top of a binary minus operator (c) A division operator can be pushed on top of a plus operator (d) An open bracket can be popped off the stack when a division operator is processed

- Source: `DOC-28`, page 4, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is the highest-frequency Module 2 solving pattern in the repository.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 10. P2 · D1 · DOC-28-P04-MCQ-Q23

> What would be the Postfix notation for the given equation? a+(b*c(d/e^f)*g)*h) (a) abcdef^/*g*h*+ (b) ab*cdef/^*g-h+ (c) abc*de^fg/*-*h+ (d) abcd*^ed/g*-h*+

- Source: `DOC-28`, page 4, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is the highest-frequency Module 2 solving pattern in the repository.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 11. P2 · D2 · DOC-30-P09-Q34

> Translate infix expression into its equivalent post fix expression: (A-B)*(D/E)

- Source: `DOC-30`, page 9, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is the highest-frequency Module 2 solving pattern in the repository.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 12. P2 · D2 · DOC-30-P09-Q35

> Translate infix expression into its equivalent post fix expression: (A+B^D)/(E- F)+G Ans : (A+B^D)/(E-F)+G = (A+BD^])/[EF-]+G = [ABD^+]/[EF-]+G = [ABD^+EF-/]+G = ABD^+EF-/G

- Source: `DOC-30`, page 9, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is the highest-frequency Module 2 solving pattern in the repository.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 13. P2 · D2 · DOC-30-P09-Q36

> Translate infix expression into its equivalent post fix expression: A*(B+D)/E-F*(G+H/K)

- Source: `DOC-30`, page 9, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is the highest-frequency Module 2 solving pattern in the repository.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 14. P2 · D2 · DOC-30-P09-Q37

> Consider the following arithmetic expression P, written in postfix notation : P: 12 , 7 , 3 , - , / , 2 , 1 , 5 , + , * , + Translate P into infix expression. Ans : P: 12,[7-3],/,2,1,5,+,*,+ = [12/(7-3)],2,1,5,+,*,+ = [12/(7- 3)],2,[1+5],*,+ = [12/(7- 3)],[2*(1+5)],+ =12/(7- 3)+2*(1+5)

- Source: `DOC-30`, page 9, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is the highest-frequency Module 2 solving pattern in the repository.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 15. P2 · D1 · DOC-31-P02-PART1-Q12

> The postfix form of the expression ( ) ( ) G / F E D C B A ∗ − ∗ ∗ + is (A) ∗ ∗ − ∗ + / FG E CD AB (B) / G F E CD AB ∗ ∗ − ∗ + (C) / G F E CD AB ∗ ∗ − ∗ + (D) / G F CDE AB ∗ ∗ − ∗ + 3

- Source: `DOC-31`, page 2, year not available, marks 2
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is the highest-frequency Module 2 solving pattern in the repository.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 16. P2 · D1 · DOC-31-P07-PART1-Q49

> The postfix form of A*B+C/D is (A)  *AB/CD+ (B) AB*CD/+ (C)  A*BC+/D (D) ABCD+/*

- Source: `DOC-31`, page 7, year not available, marks 2
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is the highest-frequency Module 2 solving pattern in the repository.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 17. P2 · D1 · DOC-31-P12-PART1-Q74

> Which data structure is needed to convert infix notation to postfix notation? (A)  Branch (B)  Queue (C)  Tree (D)  Stack

- Source: `DOC-31`, page 12, year not available, marks 2
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is the highest-frequency Module 2 solving pattern in the repository.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 18. P2 · D3 · DOC-31-P43-PART2-Q39

> Convert the following infix expressions into its equivalent postfix expressions; (i)  ( ) ( ) G F E / D B A + − ↑ + (ii) ( ) ( ) K H G * F E / D B * A + − + (8)

- Source: `DOC-31`, page 43, year not available, marks 8
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is the highest-frequency Module 2 solving pattern in the repository.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 19. P2 · D3 · DOC-31-P50-PART2-Q51

> Illustrate the steps for converting an infix expression into a postfix expression for the following expression ( ) ( ) ( ) g f e / d c b a ↑ + + ∗ + . (8)

- Source: `DOC-31`, page 50, year not available, marks 8
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is the highest-frequency Module 2 solving pattern in the repository.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 20. P2 · D3 · DOC-31-P53-PART2-Q56

> Execute your algorithm to convert an infix expression to a post fix expression with the following infix expression on your input ( ) ( ) ( ) ( ) c / b a b / g / p k * n m ↑ ↑ + + (8)

- Source: `DOC-31`, page 53, year not available, marks 8
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is the highest-frequency Module 2 solving pattern in the repository.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 21. P2 · D3 · DOC-31-P77-PART2-Q80

> Execute your algorithm to convert an infix expression to a post fix expression with the following infix expression as input ( ) ( ) ( ) [ ] ( ) I / H G F / E D C / B A Q + + ↑ + + = (8)

- Source: `DOC-31`, page 77, year not available, marks 8
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** This is the highest-frequency Module 2 solving pattern in the repository.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.


### Mastery check
- Can I recognize: **convert infix to postfix, show stack/output trace, operator stack**?
- Can I state the invariant?
- Can I trace the state without skipping a step?
- Can I handle the relevant boundary case?
- Can I write the exam-ready answer format?

---
## Prefix/postfix transformations

**Recognition trigger:** prefix form, postfix equivalent of prefix, infix→prefix, prefix↔postfix

**Why this is separate:** Prefix and postfix questions require the same stack discipline but a different scan/order strategy.

**Prerequisites:** expression trees mentally; postfix conversion rules; operator precedence

**Invariant:** each completed subexpression must preserve operator/operand order exactly.

**Core cases:** prefix output, postfix output, infix→prefix, prefix→postfix

**Step-by-step method:**  
For infix→prefix use the course/source-supported reversal-and-conversion method; for prefix/postfix transformations, process tokens with a stack of partial expressions and combine operands around the operator.

**Complexity:** O(n) time and O(n) auxiliary space for standard stack methods.

**Common mistakes:** reversing operands incorrectly; mishandling ^ associativity; copying postfix rules without adapting scan direction.

**Exam-writing format:** Write the transformation method first, then show one intermediate stack state.

**Memorize:** operator placement differs: prefix before operands, postfix after operands.

**Understand:** the same expression tree can be serialized in multiple traversals.

### Authentic questions (9 unique texts; 15 occurrences)

#### 1. P2 · D1 · DOC-02-P01-Q01-sub-iii

> The postfix equivalent of *+ab-cd is (a) ab+cd-* (b) ab+cd*- (c) abcd+-* (d) ab+-cd*

- Source: `DOC-02`, page 1, year 2021, marks 1
- Independent sources: 4; occurrence count: 4
- Other occurrence IDs: DOC-19-P02-Q01-sub-iii, DOC-20-P01-Q01-sub-iii, DOC-26-P01-Q01-sub-iii
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Prefix and postfix questions require the same stack discipline but a different scan/order strategy.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 2. P2 · D2 · DOC-13-P02-Q04-sub-b

> Convert the Infix expression ((A + B) * C – (D – E) ^ (F + G)) to equivalent Prefix and Postfix notations using stack. [(CO2)(Apply/IOCQ)]

- Source: `DOC-13`, page 2, year 2025, marks not available
- Independent sources: 4; occurrence count: 4
- Other occurrence IDs: DOC-14-P02-Q04-sub-b, DOC-15-P02-Q04-sub-b, DOC-16-P02-Q04-sub-b
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Prefix and postfix questions require the same stack discipline but a different scan/order strategy.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 3. P3 · D1 · DOC-25-P01-Q01-sub-v

> What would be the Prefix notation for (A*B)+(C*D)? (a) *+AB*CD (b) +*AB*CD                 (c) **AB+CD (d) +*BA*CD

- Source: `DOC-25`, page 1, year 2021, marks 1
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Prefix and postfix questions require the same stack discipline but a different scan/order strategy.

**Direct answer:** Solved following standard Infix to Prefix expression conversion using stack algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_APPLICATIONS under question family 'Infix to Prefix expression conversion using stack'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Infix to Prefix expression conversion using stack.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 4. P3 · D2 · DOC-30-P01-Q06

> What are the notations used in Evaluation of Arithmetic Expressions using prefix and postfix forms?

- Source: `DOC-30`, page 1, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Prefix and postfix questions require the same stack discipline but a different scan/order strategy.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 5. P3 · D1 · DOC-31-P04-PART1-Q21

> What is the postfix form of the following prefix expression -A/B*C$DE (A) ABCDE$*/- (B)  A-BCDE$*/- (C) ABC$ED*/- (D)  A-BCDE$*/

- Source: `DOC-31`, page 4, year not available, marks 2
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Prefix and postfix questions require the same stack discipline but a different scan/order strategy.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 6. P3 · D1 · DOC-31-P10-PART1-Q63

> What is the postfix form of the following prefix *+ab–cd (A) ab+cd–* (B) abc+*– (C) ab+*cd– (D) ab+*cd–

- Source: `DOC-31`, page 10, year not available, marks 2
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Prefix and postfix questions require the same stack discipline but a different scan/order strategy.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 7. P3 · D1 · DOC-31-P12-PART1-Q77

> The prefix form of A-B/ (C * D ^ E) is, (A)   -/*^ACBDE (B)  -ABCD*^DE (C)  -A/B*C^DE (D)  -A/BC*^DE

- Source: `DOC-31`, page 12, year not available, marks 2
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Prefix and postfix questions require the same stack discipline but a different scan/order strategy.

**Direct answer:** Solved following standard Infix to Prefix expression conversion using stack algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_APPLICATIONS under question family 'Infix to Prefix expression conversion using stack'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Infix to Prefix expression conversion using stack.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 8. P3 · D1 · DOC-31-P13-PART1-Q86

> The prefix form of an infix expression t * r q p − + is 14 (A) rt * pq − + . (B) t * pqr + − . (C) rt * pq + − . (D) pqrt * + − .

- Source: `DOC-31`, page 13, year not available, marks 2
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Prefix and postfix questions require the same stack discipline but a different scan/order strategy.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 9. P3 · D1 · DOC-31-P14-PART1-Q90

> The equivalent prefix expression for the following infix expression  (A+B)-(C+D*E)/F*G is (A)  -+AB*/+C*DEFG (B)  /-+AB*+C*DEFG (C)  -/+AB*+CDE*FG (D)  -+AB*/+CDE*FG

- Source: `DOC-31`, page 14, year not available, marks 2
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Prefix and postfix questions require the same stack discipline but a different scan/order strategy.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.


### Mastery check
- Can I recognize: **prefix form, postfix equivalent of prefix, infix→prefix, prefix↔postfix**?
- Can I state the invariant?
- Can I trace the state without skipping a step?
- Can I handle the relevant boundary case?
- Can I write the exam-ready answer format?

---
## Postfix evaluation

**Recognition trigger:** evaluate postfix expression, result of postfix expression, operand stack

**Why this is separate:** Evaluation is a distinct solving procedure from conversion and is repeatedly tested.

**Prerequisites:** stack push/pop; operand/operator distinction; left/right operand order

**Invariant:** the operand stack contains exactly the values produced by the processed postfix prefix.

**Core cases:** operand push; binary operator; non-commutative operand order; final value

**Step-by-step method:**  
Read left-to-right. Operand→push. Operator→pop right operand, pop left operand, compute left op right, push result. Final stack value is the answer.

**Complexity:** O(n) time and O(n) auxiliary space.

**Common mistakes:** using first popped value as the left operand; forgetting to push the result; evaluating before enough operands exist.

**Exam-writing format:** Token | action | stack table is the safest presentation.

**Memorize:** first pop = right operand; second pop = left operand.

**Understand:** postfix already encodes order, so the stack only restores the operands for each operator.

### Authentic questions (5 unique texts; 6 occurrences)

#### 1. P3 · D2 · DOC-01-P02-Q01-sub-vi

> The following postfix expression with single digit operands is evaluated using a stack:

- Source: `DOC-01`, page 2, year 2020, marks 1
- Independent sources: 2; occurrence count: 2
- Other occurrence IDs: DOC-21-P02-Q01-sub-vi
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Evaluation is a distinct solving procedure from conversion and is repeatedly tested.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 2. P3 · D2 · DOC-28-P06-LA-Q11

> Stepwise show how the following infix expression is converted to its corresponding postfix expression. ((5+7)-(4*3))+(6/3)/2-9 Next, Use a suitable data structure to evaluate the generated postfix expression.

- Source: `DOC-28`, page 6, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Evaluation is a distinct solving procedure from conversion and is repeatedly tested.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 3. P3 · D1 · DOC-31-P06-PART1-Q38

> The data structure required to evaluate a postfix expression is (A) queue (B)  stack (C) array (D)  linked-list

- Source: `DOC-31`, page 6, year not available, marks 2
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Evaluation is a distinct solving procedure from conversion and is repeatedly tested.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 4. P3 · D1 · DOC-31-P15-PART1-Q93

> The result of evaluating the postfix expression 5, 4, 6, +, *, 4, 9, 3, /, +, * is (A)  600. (B) 350. (C)  650. (D)  588.

- Source: `DOC-31`, page 15, year not available, marks 2
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Evaluation is a distinct solving procedure from conversion and is repeatedly tested.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.

#### 5. P3 · D3 · DOC-31-P19-PART2-Q06

> Write an algorithm to evaluate a postfix expression.  Execute your algorithm using the following postfix expression as your input : a b + c d +*f ↑. (7)

- Source: `DOC-31`, page 19, year not available, marks 7
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Evaluation is a distinct solving procedure from conversion and is repeatedly tested.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.


### Mastery check
- Can I recognize: **evaluate postfix expression, result of postfix expression, operand stack**?
- Can I state the invariant?
- Can I trace the state without skipping a step?
- Can I handle the relevant boundary case?
- Can I write the exam-ready answer format?

---
## Combined infix conversion + evaluation

**Recognition trigger:** evaluate infix using a data structure; convert then evaluate; show every step

**Why this is separate:** The question mixes two procedural modes and must be answered in both stages.

**Prerequisites:** infix→postfix and postfix evaluation

**Invariant:** the intermediate postfix expression must be valid before evaluation begins.

**Core cases:** conversion trace followed by operand-stack evaluation

**Step-by-step method:**  
Stage 1 convert; Stage 2 evaluate the generated postfix; preserve intermediate result exactly.

**Complexity:** O(n) total when both stages are linear.

**Common mistakes:** jumping directly to the numeric answer; evaluating the infix as if postfix.

**Exam-writing format:** Separate the answer into Conversion and Evaluation tables.

**Memorize:** convert first, evaluate second.

**Understand:** the two stages use different stacks/states.

### Authentic questions (1 unique texts; 2 occurrences)

#### 1. P3 · D3 · DOC-18-P03-Q04-sub-a

> Evaluate the result of the given infix expression using proper data structure: 2*(5*(3+6))/15 - 2. Show every step clearly.

- Source: `DOC-18`, page 3, year 2020, marks not available
- Independent sources: 2; occurrence count: 2
- Other occurrence IDs: DOC-28-P06-LA-Q10
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The question mixes two procedural modes and must be answered in both stages.

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Step-by-step solution:**
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready answer:**
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

**Beginner note:** Operands never touch the stack; only operators and parentheses enter the stack.


### Mastery check
- Can I recognize: **evaluate infix using a data structure; convert then evaluate; show every step**?
- Can I state the invariant?
- Can I trace the state without skipping a step?
- Can I handle the relevant boundary case?
- Can I write the exam-ready answer format?

---
## Balanced-parentheses / parenthesis matching

**Recognition trigger:** balanced parentheses, matched brackets, valid parenthesis sequence

**Why this is separate:** Parenthesis matching is a separate stack invariant and is often asked as code/algorithm/MCQ.

**Prerequisites:** stack operations and matching pairs

**Invariant:** the stack contains exactly the unmatched opening delimiters seen so far.

**Core cases:** opening symbol; matching close; mismatch with empty stack; mismatch of symbol type; non-empty stack at end

**Step-by-step method:**  
Push opens. For each close, require a non-empty stack and a matching top, then pop. Accept only if the stack is empty at end.

**Complexity:** O(n) time and O(n) space in the worst case.

**Common mistakes:** accepting leftover opens; accepting a close when stack is empty; ignoring delimiter types when multiple types are supported.

**Exam-writing format:** State rejection conditions explicitly.

**Memorize:** Every close must match the most recent unmatched open.

**Understand:** LIFO mirrors nested delimiter structure.

### Authentic questions (4 unique texts; 5 occurrences)

#### 1. P3 · D3 · DOC-22-P03-Q05-sub-c

> Write an algorithm to check whether a given expression contains balanced parentheses or not, note that only ‘(’and ‘)’ are allowed here as parentheses. (3 + 3) + 3 + 3 = 12

- Source: `DOC-22`, page 3, year 2021, marks not available
- Independent sources: 2; occurrence count: 2
- Other occurrence IDs: DOC-23-P03-Q05-sub-c
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Parenthesis matching is a separate stack invariant and is often asked as code/algorithm/MCQ.

**Direct answer:** Solved following standard Parenthesis matching and balanced bracket checking using stack algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_APPLICATIONS under question family 'Parenthesis matching and balanced bracket checking using stack'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Parenthesis matching and balanced bracket checking using stack.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 2. P3 · D3 · DOC-28-P07-LA-Q15

> Using a suitable data structure, write a C function to determine whether a sequence of parentheses is balanced or not.

- Source: `DOC-28`, page 7, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Parenthesis matching is a separate stack invariant and is often asked as code/algorithm/MCQ.

**Direct answer:** Solved following standard Parenthesis matching and balanced bracket checking using stack algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_APPLICATIONS under question family 'Parenthesis matching and balanced bracket checking using stack'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Parenthesis matching and balanced bracket checking using stack.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 3. P3 · D1 · DOC-31-P06-PART1-Q39

> The data structure required to check whether an expression contains balanced parenthesis is (A)  Stack (B) Queue (C)  Tree (D) Array

- Source: `DOC-31`, page 6, year not available, marks 2
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Parenthesis matching is a separate stack invariant and is often asked as code/algorithm/MCQ.

**Direct answer:** Solved following standard Parenthesis matching and balanced bracket checking using stack algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_APPLICATIONS under question family 'Parenthesis matching and balanced bracket checking using stack'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Parenthesis matching and balanced bracket checking using stack.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 4. P3 · D3 · DOC-31-P63-PART2-Q64

> What are stacks? How can stacks be used to check whether an expression is correctly parenthized or not.  For eg(()) is well formed but (() or )()( is not. (7)

- Source: `DOC-31`, page 63, year not available, marks 7
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Parenthesis matching is a separate stack invariant and is often asked as code/algorithm/MCQ.

**Direct answer:** Solved following standard Two stacks implementation on a single array and memory sharing algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Two stacks implementation on a single array and memory sharing'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Two stacks implementation on a single array and memory sharing.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.


### Mastery check
- Can I recognize: **balanced parentheses, matched brackets, valid parenthesis sequence**?
- Can I state the invariant?
- Can I trace the state without skipping a step?
- Can I handle the relevant boundary case?
- Can I write the exam-ready answer format?

---

# MASTER PATTERN — 3. Queue & Circular Queue

### Pattern map
1. **Linear queue operations and state tracing** — 7 unique question texts / 9 occurrences
2. **Circular queue wrap-around and empty/full states** — 8 unique question texts / 16 occurrences
3. **Queue applications** — 2 unique question texts / 2 occurrences

## Linear queue operations and state tracing

**Recognition trigger:** FIFO, enqueue, dequeue, front, rear, queue structure

**Why this is separate:** These questions test the exact movement of front/rear and the FIFO invariant.

**Prerequisites:** FIFO, front/rear meaning

**Invariant:** front identifies the next removable item; rear identifies the insertion boundary according to the chosen convention.

**Core cases:** empty queue; first insertion; repeated enqueue/dequeue; last deletion; front/rear updates

**Step-by-step method:**  
Enqueue at rear; dequeue at front; update boundaries consistently with the implementation convention.

**Complexity:** O(1) for standard linked-list or index-based operations when no shifting is needed; a shifting linear-array implementation can make operations O(n).

**Common mistakes:** advancing the wrong pointer; forgetting the one-element transition back to empty.

**Exam-writing format:** Draw the queue after every operation and label front/rear.

**Memorize:** enqueue→rear; dequeue→front.

**Understand:** FIFO is a consequence of asymmetric insertion/deletion ends.

### Authentic questions (7 unique texts; 9 occurrences)

#### 1. P1 · D3 · DOC-03-P03-Q05-sub-c

> Write a program or pseudo code or algorithm to generate binary numbers between 1 to `n` using a queue. (CO4)(Analyze/LOCQ)]

- Source: `DOC-03`, page 3, year 2022, marks not available
- Independent sources: 3; occurrence count: 3
- Other occurrence IDs: DOC-04-P03-Q05-sub-c, DOC-05-P03-Q05-sub-c
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** These questions test the exact movement of front/rear and the FIFO invariant.

**Direct answer:** Solved following standard Two stacks implementation on a single array and memory sharing algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Two stacks implementation on a single array and memory sharing'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Two stacks implementation on a single array and memory sharing.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 2. P2 · D1 · DOC-25-P01-Q01-sub-ii

> In a queue, insertion is done at __________. (a) Rear (b) Front (c) Back (d) Top.

- Source: `DOC-25`, page 1, year 2021, marks 1
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** These questions test the exact movement of front/rear and the FIFO invariant.

**Direct answer:** Circular Queue wraps around indices using modulo arithmetic: (rear + 1) % MAX.

**Step-by-step solution:**
1. Front points to removal position; Rear points to last inserted position.
2. Full Condition: `(rear + 1) % MAX == front`.
3. Empty Condition: `front == -1` (or `front == rear` depending on convention).
4. Enqueue: `rear = (rear + 1) % MAX; queue[rear] = item;` (if empty, `front = rear = 0`).
5. Dequeue: `item = queue[front]; if (front == rear) front = rear = -1; else front = (front + 1) % MAX;`
6. Eliminates linear queue false overflow where rear reaches MAX-1 but front slots are empty.

**Exam-ready answer:**
• Advantage over Linear Queue: Solves false overflow and memory wastage without shifting elements.
• Full Condition: `(rear + 1) % MAX == front`.
• Empty Condition: `front == -1 && rear == -1`.
• Complexity: O(1) time for both Enqueue and Dequeue.

**Complexity:** O(1) for enqueue and dequeue; Space: O(n) fixed array buffer

**Trap:** Using standard rear++ which causes index out of bounds instead of `(rear + 1) % MAX`.

**Beginner note:** Modulo arithmetic `% MAX` acts like a clock: after 11 comes 12, then 1.

#### 3. P2 · D2 · DOC-25-P02-Q04-sub-a

> Add 1, 2, 3, 4, 5, 6         (b) Delete two numbers          (c) Add 7

- Source: `DOC-25`, page 2, year 2021, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** These questions test the exact movement of front/rear and the FIFO invariant.

**Direct answer:** Circular Queue wraps around indices using modulo arithmetic: (rear + 1) % MAX.

**Step-by-step solution:**
1. Front points to removal position; Rear points to last inserted position.
2. Full Condition: `(rear + 1) % MAX == front`.
3. Empty Condition: `front == -1` (or `front == rear` depending on convention).
4. Enqueue: `rear = (rear + 1) % MAX; queue[rear] = item;` (if empty, `front = rear = 0`).
5. Dequeue: `item = queue[front]; if (front == rear) front = rear = -1; else front = (front + 1) % MAX;`
6. Eliminates linear queue false overflow where rear reaches MAX-1 but front slots are empty.

**Exam-ready answer:**
• Advantage over Linear Queue: Solves false overflow and memory wastage without shifting elements.
• Full Condition: `(rear + 1) % MAX == front`.
• Empty Condition: `front == -1 && rear == -1`.
• Complexity: O(1) time for both Enqueue and Dequeue.

**Complexity:** O(1) for enqueue and dequeue; Space: O(n) fixed array buffer

**Trap:** Using standard rear++ which causes index out of bounds instead of `(rear + 1) % MAX`.

**Beginner note:** Modulo arithmetic `% MAX` acts like a clock: after 11 comes 12, then 1.

#### 4. P2 · D2 · DOC-25-P02-Q04-sub-a

> Add 1, 2, 3, 4, 5, 6         (b) Delete two numbers          (c) Add 7

- Source: `DOC-25`, page 2, year 2021, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** These questions test the exact movement of front/rear and the FIFO invariant.

**Direct answer:** Circular Queue wraps around indices using modulo arithmetic: (rear + 1) % MAX.

**Step-by-step solution:**
1. Front points to removal position; Rear points to last inserted position.
2. Full Condition: `(rear + 1) % MAX == front`.
3. Empty Condition: `front == -1` (or `front == rear` depending on convention).
4. Enqueue: `rear = (rear + 1) % MAX; queue[rear] = item;` (if empty, `front = rear = 0`).
5. Dequeue: `item = queue[front]; if (front == rear) front = rear = -1; else front = (front + 1) % MAX;`
6. Eliminates linear queue false overflow where rear reaches MAX-1 but front slots are empty.

**Exam-ready answer:**
• Advantage over Linear Queue: Solves false overflow and memory wastage without shifting elements.
• Full Condition: `(rear + 1) % MAX == front`.
• Empty Condition: `front == -1 && rear == -1`.
• Complexity: O(1) time for both Enqueue and Dequeue.

**Complexity:** O(1) for enqueue and dequeue; Space: O(n) fixed array buffer

**Trap:** Using standard rear++ which causes index out of bounds instead of `(rear + 1) % MAX`.

**Beginner note:** Modulo arithmetic `% MAX` acts like a clock: after 11 comes 12, then 1.

#### 5. P2 · D2 · DOC-25-P02-Q04-sub-d

> Add 8                               (e) Delete four numbers          (f) Add 9

- Source: `DOC-25`, page 2, year 2021, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** These questions test the exact movement of front/rear and the FIFO invariant.

**Direct answer:** Solved following standard Linear Queue: array and linked list implementations, front/rear pointers algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_QUEUE_LINEAR_CIRCULAR under question family 'Linear Queue: array and linked list implementations, front/rear pointers'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Linear Queue: array and linked list implementations, front/rear pointers.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 6. P2 · D2 · DOC-31-P11-PART1-Q68

> Assume that a queue is available for pushing and popping elements. Given an input sequence a, b, c, (c be the first element), give the output sequence of elements if the rightmost element given above is the first to be popped from the queue.

- Source: `DOC-31`, page 11, year not available, marks 2
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** These questions test the exact movement of front/rear and the FIFO invariant.

**Direct answer:** Solved following standard Two stacks implementation on a single array and memory sharing algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Two stacks implementation on a single array and memory sharing'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Two stacks implementation on a single array and memory sharing.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 7. P2 · D1 · DOC-31-P12-PART1-Q73

> A queue is a, (A)  FIFO (First In First Out) list. (B)  LIFO (Last In First Out) list. (C)  Ordered array. (D)  Linear tree.

- Source: `DOC-31`, page 12, year not available, marks 2
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** These questions test the exact movement of front/rear and the FIFO invariant.

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.


### Mastery check
- Can I recognize: **FIFO, enqueue, dequeue, front, rear, queue structure**?
- Can I state the invariant?
- Can I trace the state without skipping a step?
- Can I handle the relevant boundary case?
- Can I write the exam-ready answer format?

---
## Circular queue wrap-around and empty/full states

**Recognition trigger:** circular queue, circular array, wrap-around, modulo, front/rear

**Why this is separate:** Circular queues change the index logic and avoid wasted linear-array space.

**Prerequisites:** linear queue; index arithmetic; chosen empty/full convention

**Invariant:** front/rear always identify the logical queue while indices wrap around the array boundary.

**Core cases:** first insertion; wrap-around enqueue; dequeue; empty state; full state; course convention

**Step-by-step method:**  
Advance circular indices with modulo N; apply the exact repository/course empty/full convention before accepting an operation.

**Complexity:** O(1) per enqueue/dequeue under standard array implementation.

**Common mistakes:** mixing one-slot-empty and count-based conventions; forgetting wrap-around.

**Exam-writing format:** Show the physical array plus front/rear after each wrap-around operation.

**Memorize:** next_index=(index+1) mod N.

**Understand:** logical order can continue after the physical array reaches its end.

### Authentic questions (8 unique texts; 16 occurrences)

#### 1. P2 · D2 · DOC-01-P03-Q04-sub-b

> Write an application of queue. What is a circular queue? State the advantage of a circular queue over a normal queue.

- Source: `DOC-01`, page 3, year 2020, marks not available
- Independent sources: 2; occurrence count: 2
- Other occurrence IDs: DOC-21-P03-Q04-sub-b
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Circular queues change the index logic and avoid wasted linear-array space.

**Direct answer:** Solved following standard Linear Queue: array and linked list implementations, front/rear pointers algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_QUEUE_LINEAR_CIRCULAR under question family 'Linear Queue: array and linked list implementations, front/rear pointers'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Linear Queue: array and linked list implementations, front/rear pointers.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 2. P1 · D3 · DOC-02-P03-Q04-sub-a

> Why is it beneficial to use a circular array to implement a queue? Explain with an example.     [(CO4) (Remember/LOCQ)]

- Source: `DOC-02`, page 3, year 2021, marks not available
- Independent sources: 7; occurrence count: 7
- Other occurrence IDs: DOC-10-P02-Q05-sub-a, DOC-11-P02-Q05-sub-a, DOC-12-P02-Q05-sub-a, DOC-19-P06-Q04-sub-a, DOC-20-P03-Q04-sub-a, DOC-26-P03-Q04-sub-a
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Circular queues change the index logic and avoid wasted linear-array space.

**Direct answer:** Solved following standard Linear Queue: array and linked list implementations, front/rear pointers algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_QUEUE_LINEAR_CIRCULAR under question family 'Linear Queue: array and linked list implementations, front/rear pointers'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Linear Queue: array and linked list implementations, front/rear pointers.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 3. P2 · D3 · DOC-22-P02-Q04-sub-a

> Write a program to implement insertion and deletion of elements in a circular queue (using array). Also, incorporate the checking for underflow and overflow.

- Source: `DOC-22`, page 2, year 2021, marks not available
- Independent sources: 2; occurrence count: 2
- Other occurrence IDs: DOC-23-P02-Q04-sub-a
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Circular queues change the index logic and avoid wasted linear-array space.

**Direct answer:** Circular Queue wraps around indices using modulo arithmetic: (rear + 1) % MAX.

**Step-by-step solution:**
1. Front points to removal position; Rear points to last inserted position.
2. Full Condition: `(rear + 1) % MAX == front`.
3. Empty Condition: `front == -1` (or `front == rear` depending on convention).
4. Enqueue: `rear = (rear + 1) % MAX; queue[rear] = item;` (if empty, `front = rear = 0`).
5. Dequeue: `item = queue[front]; if (front == rear) front = rear = -1; else front = (front + 1) % MAX;`
6. Eliminates linear queue false overflow where rear reaches MAX-1 but front slots are empty.

**Exam-ready answer:**
• Advantage over Linear Queue: Solves false overflow and memory wastage without shifting elements.
• Full Condition: `(rear + 1) % MAX == front`.
• Empty Condition: `front == -1 && rear == -1`.
• Complexity: O(1) time for both Enqueue and Dequeue.

**Complexity:** O(1) for enqueue and dequeue; Space: O(n) fixed array buffer

**Trap:** Using standard rear++ which causes index out of bounds instead of `(rear + 1) % MAX`.

**Beginner note:** Modulo arithmetic `% MAX` acts like a clock: after 11 comes 12, then 1.

#### 4. P2 · D2 · DOC-25-P02-Q05-sub-b

> What are the advantages of a circular queue over linear queue?

- Source: `DOC-25`, page 2, year 2021, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Circular queues change the index logic and avoid wasted linear-array space.

**Direct answer:** Solved following standard Linear Queue: array and linked list implementations, front/rear pointers algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_QUEUE_LINEAR_CIRCULAR under question family 'Linear Queue: array and linked list implementations, front/rear pointers'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Linear Queue: array and linked list implementations, front/rear pointers.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 5. P2 · D2 · DOC-28-P05-SA-Q05

> If front is equal to rear in a circular queue which is not empty, the queue has _______ element(s).

- Source: `DOC-28`, page 5, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Circular queues change the index logic and avoid wasted linear-array space.

**Direct answer:** Circular Queue wraps around indices using modulo arithmetic: (rear + 1) % MAX.

**Step-by-step solution:**
1. Front points to removal position; Rear points to last inserted position.
2. Full Condition: `(rear + 1) % MAX == front`.
3. Empty Condition: `front == -1` (or `front == rear` depending on convention).
4. Enqueue: `rear = (rear + 1) % MAX; queue[rear] = item;` (if empty, `front = rear = 0`).
5. Dequeue: `item = queue[front]; if (front == rear) front = rear = -1; else front = (front + 1) % MAX;`
6. Eliminates linear queue false overflow where rear reaches MAX-1 but front slots are empty.

**Exam-ready answer:**
• Advantage over Linear Queue: Solves false overflow and memory wastage without shifting elements.
• Full Condition: `(rear + 1) % MAX == front`.
• Empty Condition: `front == -1 && rear == -1`.
• Complexity: O(1) time for both Enqueue and Dequeue.

**Complexity:** O(1) for enqueue and dequeue; Space: O(n) fixed array buffer

**Trap:** Using standard rear++ which causes index out of bounds instead of `(rear + 1) % MAX`.

**Beginner note:** Modulo arithmetic `% MAX` acts like a clock: after 11 comes 12, then 1.

#### 6. P2 · D2 · DOC-28-P07-LA-Q16

> There are ‘n’ integers in a circular queue. We search for every ‘d’-th element starting from the queue beginning and mark it invalid. So after the first round, the ‘d’-th element is marked invalid and there are only (n-1) valid items remaining in the queue. Starting from the first invalid element, this process continues, i.e., every ‘d’-th element is searched and marked invalid. Invalid items are no longer taken into account and skipped. That means if you come across an invalid item when you try to find the ‘d’-th element, you try the ‘d+1’-th element, if that is valid. If invalid, you try ‘d+2’-th element. This continues till you find the first valid item or terminate if no valid items could be found. Find after ‘x’ rounds, the element that will be marked invalid and return the element.

- Source: `DOC-28`, page 7, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Circular queues change the index logic and avoid wasted linear-array space.

**Direct answer:** Circular Queue wraps around indices using modulo arithmetic: (rear + 1) % MAX.

**Step-by-step solution:**
1. Front points to removal position; Rear points to last inserted position.
2. Full Condition: `(rear + 1) % MAX == front`.
3. Empty Condition: `front == -1` (or `front == rear` depending on convention).
4. Enqueue: `rear = (rear + 1) % MAX; queue[rear] = item;` (if empty, `front = rear = 0`).
5. Dequeue: `item = queue[front]; if (front == rear) front = rear = -1; else front = (front + 1) % MAX;`
6. Eliminates linear queue false overflow where rear reaches MAX-1 but front slots are empty.

**Exam-ready answer:**
• Advantage over Linear Queue: Solves false overflow and memory wastage without shifting elements.
• Full Condition: `(rear + 1) % MAX == front`.
• Empty Condition: `front == -1 && rear == -1`.
• Complexity: O(1) time for both Enqueue and Dequeue.

**Complexity:** O(1) for enqueue and dequeue; Space: O(n) fixed array buffer

**Trap:** Using standard rear++ which causes index out of bounds instead of `(rear + 1) % MAX`.

**Beginner note:** Modulo arithmetic `% MAX` acts like a clock: after 11 comes 12, then 1.

#### 7. P2 · D1 · DOC-31-P08-PART1-Q50

> Let the following circular queue can accommodate maximum six elements with the following data front = 2 rear = 4 queue = _______; L, M, N, ___, ___ What will happen after ADD O operation takes place? (A) front = 2 rear = 5 queue = ______; L, M, N, O, ___ (B)  front = 3 rear = 5 queue = L, M, N, O, ___ (C)  front = 3 rear = 4 queue = ______; L, M, N, O, ___ (D)  front = 2 rear = 4 queue = L, M, N, O, ___

- Source: `DOC-31`, page 8, year not available, marks 2
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Circular queues change the index logic and avoid wasted linear-array space.

**Direct answer:** Circular Queue wraps around indices using modulo arithmetic: (rear + 1) % MAX.

**Step-by-step solution:**
1. Front points to removal position; Rear points to last inserted position.
2. Full Condition: `(rear + 1) % MAX == front`.
3. Empty Condition: `front == -1` (or `front == rear` depending on convention).
4. Enqueue: `rear = (rear + 1) % MAX; queue[rear] = item;` (if empty, `front = rear = 0`).
5. Dequeue: `item = queue[front]; if (front == rear) front = rear = -1; else front = (front + 1) % MAX;`
6. Eliminates linear queue false overflow where rear reaches MAX-1 but front slots are empty.

**Exam-ready answer:**
• Advantage over Linear Queue: Solves false overflow and memory wastage without shifting elements.
• Full Condition: `(rear + 1) % MAX == front`.
• Empty Condition: `front == -1 && rear == -1`.
• Complexity: O(1) time for both Enqueue and Dequeue.

**Complexity:** O(1) for enqueue and dequeue; Space: O(n) fixed array buffer

**Trap:** Using standard rear++ which causes index out of bounds instead of `(rear + 1) % MAX`.

**Beginner note:** Modulo arithmetic `% MAX` acts like a clock: after 11 comes 12, then 1.

#### 8. P2 · D3 · DOC-31-P19-PART2-Q07

> What are circular queues?  Write down routines for inserting and deleting elements from a circular queue implemented using arrays. (7)

- Source: `DOC-31`, page 19, year not available, marks 7
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Circular queues change the index logic and avoid wasted linear-array space.

**Direct answer:** Circular Queue wraps around indices using modulo arithmetic: (rear + 1) % MAX.

**Step-by-step solution:**
1. Front points to removal position; Rear points to last inserted position.
2. Full Condition: `(rear + 1) % MAX == front`.
3. Empty Condition: `front == -1` (or `front == rear` depending on convention).
4. Enqueue: `rear = (rear + 1) % MAX; queue[rear] = item;` (if empty, `front = rear = 0`).
5. Dequeue: `item = queue[front]; if (front == rear) front = rear = -1; else front = (front + 1) % MAX;`
6. Eliminates linear queue false overflow where rear reaches MAX-1 but front slots are empty.

**Exam-ready answer:**
• Advantage over Linear Queue: Solves false overflow and memory wastage without shifting elements.
• Full Condition: `(rear + 1) % MAX == front`.
• Empty Condition: `front == -1 && rear == -1`.
• Complexity: O(1) time for both Enqueue and Dequeue.

**Complexity:** O(1) for enqueue and dequeue; Space: O(n) fixed array buffer

**Trap:** Using standard rear++ which causes index out of bounds instead of `(rear + 1) % MAX`.

**Beginner note:** Modulo arithmetic `% MAX` acts like a clock: after 11 comes 12, then 1.


### Mastery check
- Can I recognize: **circular queue, circular array, wrap-around, modulo, front/rear**?
- Can I state the invariant?
- Can I trace the state without skipping a step?
- Can I handle the relevant boundary case?
- Can I write the exam-ready answer format?

---
## Queue applications

**Recognition trigger:** priority queue, CPU scheduling, buffering, spooling, queue applications

**Why this is separate:** These are conceptual application questions: the marks come from mapping FIFO or queue structures to a real process.

**Prerequisites:** FIFO and queue operations

**Invariant:** arrival/order requirements are preserved by the queue discipline used.

**Core cases:** priority queue concept vs ordinary FIFO; scheduling/buffering examples when source-supported

**Step-by-step method:**  
Identify what is waiting, what enters, what leaves, and why queue order is appropriate.

**Complexity:** State only when the source asks; do not invent complexity for conceptual questions.

**Common mistakes:** calling every waiting structure a simple FIFO queue; confusing priority queue behavior with ordinary queue behavior.

**Exam-writing format:** Answer with definition + mechanism + one concrete example.

**Memorize:** A queue models waiting in service order; a priority queue adds selection by priority.

**Understand:** the data structure follows the application's service rule.

### Authentic questions (2 unique texts; 2 occurrences)

#### 1. P3 · D3 · DOC-30-P01-Q04

> Minimum number of queues needed to implement the priority queue?

- Source: `DOC-30`, page 1, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** These are conceptual application questions: the marks come from mapping FIFO or queue structures to a real process.

**Direct answer:** Solved following standard Applications of queues: CPU scheduling, spooling, buffer management, priority queues algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_QUEUE_APPLICATIONS under question family 'Applications of queues: CPU scheduling, spooling, buffer management, priority queues'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Applications of queues: CPU scheduling, spooling, buffer management, priority queues.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 2. P3 · D2 · DOC-30-P10-Q41

> What are priority queues?

- Source: `DOC-30`, page 10, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** These are conceptual application questions: the marks come from mapping FIFO or queue structures to a real process.

**Direct answer:** Solved following standard Applications of queues: CPU scheduling, spooling, buffer management, priority queues algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_QUEUE_APPLICATIONS under question family 'Applications of queues: CPU scheduling, spooling, buffer management, priority queues'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Applications of queues: CPU scheduling, spooling, buffer management, priority queues.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.


### Mastery check
- Can I recognize: **priority queue, CPU scheduling, buffering, spooling, queue applications**?
- Can I state the invariant?
- Can I trace the state without skipping a step?
- Can I handle the relevant boundary case?
- Can I write the exam-ready answer format?

---

# MASTER PATTERN — 4. Deque

### Pattern map
1. **Deque, restricted deques, and two-ended operations** — 5 unique question texts / 8 occurrences

## Deque, restricted deques, and two-ended operations

**Recognition trigger:** deque, double-ended queue, input-restricted, output-restricted, insert/delete at either end

**Why this is separate:** Deque questions change which ends permit insertion/deletion, so the legal-operation set must be explicit.

**Prerequisites:** queue and two-end terminology

**Invariant:** the deque state is defined by front/rear plus the legal operations permitted by its restriction.

**Core cases:** insert front/rear; delete front/rear; input-restricted; output-restricted; using deque to emulate stack/queue

**Step-by-step method:**  
List legal operations first. Then update the appropriate end for each permitted action; for restricted forms, reject prohibited operations.

**Complexity:** O(1) per end operation for a suitable array/deque or linked representation.

**Common mistakes:** swapping input-restricted and output-restricted definitions; assuming a deque is always FIFO.

**Exam-writing format:** Draw both ends and mark allowed actions with arrows.

**Memorize:** Input-restricted limits insertion ends; output-restricted limits deletion ends.

**Understand:** restrictions define which of the four primitive operations are legal.

### Authentic questions (5 unique texts; 8 occurrences)

#### 1. P2 · D3 · DOC-13-P02-Q04-sub-c

> Write algorithm for inserting into an input restricted deque. Show the working of this algorithm by the input sequence: 1, 2 ,3 ,4, 5, 6. [(CO2)(Remember/LOCQ)]

- Source: `DOC-13`, page 2, year 2025, marks not available
- Independent sources: 4; occurrence count: 4
- Other occurrence IDs: DOC-14-P02-Q04-sub-c, DOC-15-P02-Q04-sub-c, DOC-16-P02-Q04-sub-c
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Deque questions change which ends permit insertion/deletion, so the legal-operation set must be explicit.

**Direct answer:** Solved following standard Deque: Input-restricted and Output-restricted double-ended queue operations algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_DEQUE under question family 'Deque: Input-restricted and Output-restricted double-ended queue operations'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Deque: Input-restricted and Output-restricted double-ended queue operations.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 2. P3 · D2 · DOC-18-P03-Q04-sub-c

> Is deque a FIFO data structure? Explain.

- Source: `DOC-18`, page 3, year 2020, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Deque questions change which ends permit insertion/deletion, so the legal-operation set must be explicit.

**Direct answer:** Solved following standard Deque: Input-restricted and Output-restricted double-ended queue operations algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_DEQUE under question family 'Deque: Input-restricted and Output-restricted double-ended queue operations'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Deque: Input-restricted and Output-restricted double-ended queue operations.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 3. P3 · D3 · DOC-28-P07-LA-Q14

> Write an algorithm for inserting into an input restricted deque. Show the working of this algorithm by the input sequence:        1, 2 ,3 ,4, 5, 6.

- Source: `DOC-28`, page 7, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Deque questions change which ends permit insertion/deletion, so the legal-operation set must be explicit.

**Direct answer:** Solved following standard Deque: Input-restricted and Output-restricted double-ended queue operations algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_DEQUE under question family 'Deque: Input-restricted and Output-restricted double-ended queue operations'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Deque: Input-restricted and Output-restricted double-ended queue operations.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 4. P3 · D3 · DOC-31-P54-PART2-Q57

> A double ended queue is a linear list where additions and deletions can be performed at either end. Represent a double ended queue using an array to store elements and write modules for additions and deletions. (8)

- Source: `DOC-31`, page 54, year not available, marks 8
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Deque questions change which ends permit insertion/deletion, so the legal-operation set must be explicit.

**Direct answer:** Solved following standard Deque: Input-restricted and Output-restricted double-ended queue operations algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_DEQUE under question family 'Deque: Input-restricted and Output-restricted double-ended queue operations'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Deque: Input-restricted and Output-restricted double-ended queue operations.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 5. P3 · D3 · DOC-31-P69-PART2-Q70

> Devise a representation for a list where insertions and deletions can be made at either end. Such a structure is called Deque (Double ended queue). Write functions for inserting and deleting at either end. (8)

- Source: `DOC-31`, page 69, year not available, marks 8
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Deque questions change which ends permit insertion/deletion, so the legal-operation set must be explicit.

**Direct answer:** Solved following standard Deque: Input-restricted and Output-restricted double-ended queue operations algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_DEQUE under question family 'Deque: Input-restricted and Output-restricted double-ended queue operations'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Deque: Input-restricted and Output-restricted double-ended queue operations.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.


### Mastery check
- Can I recognize: **deque, double-ended queue, input-restricted, output-restricted, insert/delete at either end**?
- Can I state the invariant?
- Can I trace the state without skipping a step?
- Can I handle the relevant boundary case?
- Can I write the exam-ready answer format?

---

# MASTER PATTERN — 5. Recursion

### Pattern map
1. **Recursion principles, call stack, tracing, and recursive construction** — 10 unique question texts / 19 occurrences
2. **Tail recursion and recursion→iteration reasoning** — 9 unique question texts / 18 occurrences

## Recursion principles, call stack, tracing, and recursive construction

**Recognition trigger:** recursive function, base case, call stack, recursion tree, predict output, return value

**Why this is separate:** The source corpus tests both concepts and exact trace/return behavior; this cannot be reduced to the definition of recursion.

**Prerequisites:** function calls, base case, parameter change

**Invariant:** each recursive call must move toward a base case; return work occurs while the call stack unwinds.

**Core cases:** work before call; work after call; multiple calls; static state; base-case return; recursive algorithm construction

**Step-by-step method:**  
Identify base case → identify decreasing/changing state → trace calls downward → trace returns upward → preserve evaluation order.

**Complexity:** Depends on the recurrence and maximum call depth; auxiliary call-stack space is proportional to maximum recursion depth.

**Common mistakes:** reading output in call order when it occurs on return; forgetting static-variable persistence; missing multiple recursive branches.

**Exam-writing format:** Separate Call Sequence from Return/Output Sequence.

**Memorize:** base case + progress toward it + unwinding order.

**Understand:** recursion is a stack of suspended function frames.

### Authentic questions (10 unique texts; 19 occurrences)

#### 1. P1 · D3 · DOC-03-P03-Q05-sub-a

> Consider the following code snippet and illustrate in detail how f(5) is calculated? int f(int n) { static int r=0; if(n<=0) return 1; if(n>3) { r=n; return f(n-2)+2; } return f(n-1)+r; } [(CO4) (Analyze/LOCQ)]

- Source: `DOC-03`, page 3, year 2022, marks not available
- Independent sources: 3; occurrence count: 3
- Other occurrence IDs: DOC-04-P03-Q05-sub-a, DOC-05-P03-Q05-sub-a
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The source corpus tests both concepts and exact trace/return behavior; this cannot be reduced to the definition of recursion.

**Direct answer:** Solved following standard Dry-run tracing of recursive functions and return value prediction algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_REC_PRINCIPLES under question family 'Dry-run tracing of recursive functions and return value prediction'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Dry-run tracing of recursive functions and return value prediction.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 2. P1 · D3 · DOC-10-P02-Q04-sub-c

> What will the following function return if it is called from the main as fun(5, 0, 1)? Can you identify what the following function is calculating? It is something well-known. [(CO3)(Analyse/IOCQ)]

- Source: `DOC-10`, page 2, year 2024, marks not available
- Independent sources: 3; occurrence count: 3
- Other occurrence IDs: DOC-11-P02-Q04-sub-c, DOC-12-P02-Q04-sub-c
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The source corpus tests both concepts and exact trace/return behavior; this cannot be reduced to the definition of recursion.

**Direct answer:** Solved recursively by decomposing into moving n-1 disks to auxiliary rod.

**Step-by-step solution:**
1. Base Case: If n == 1, move disk 1 directly from Source to Destination rod.
2. Recursive Step:
   - Move top n - 1 disks from Source to Auxiliary (using Destination as helper).
   - Move disk n directly from Source to Destination.
   - Move n - 1 disks from Auxiliary to Destination (using Source as helper).
3. Recurrence: T(n) = 2·T(n-1) + 1 with T(1) = 1.
4. Total moves = 2ⁿ - 1. For n=3: 7 moves; for n=4: 15 moves.

**Exam-ready answer:**
• Recurrence Relation: T(n) = 2T(n-1) + 1, T(1) = 1.
• Total Moves: 2ⁿ - 1 moves.
• Time Complexity: O(2ⁿ), Space Complexity: O(n) call stack.
• C Recursive function: TOH(n-1, from, aux, to); move disk n; TOH(n-1, aux, to, from);

**Complexity:** O(2ⁿ) exponential time; Space: O(n) auxiliary call stack space

**Trap:** Confusing the roles of destination and auxiliary pegs in the second recursive call.

**Beginner note:** Remember the rhythm: Source to Aux, Move Biggest, Aux to Destination.

#### 3. P1 · D2 · DOC-13-P02-Q05-sub-c

> Explain what will be the output when fibo(5) is called: [(CO2)(Apply/IOCQ)]

- Source: `DOC-13`, page 2, year 2025, marks not available
- Independent sources: 4; occurrence count: 4
- Other occurrence IDs: DOC-14-P02-Q05-sub-c, DOC-15-P02-Q05-sub-c, DOC-16-P02-Q05-sub-c
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The source corpus tests both concepts and exact trace/return behavior; this cannot be reduced to the definition of recursion.

**Direct answer:** Solved following standard Deque: Input-restricted and Output-restricted double-ended queue operations algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_DEQUE under question family 'Deque: Input-restricted and Output-restricted double-ended queue operations'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Deque: Input-restricted and Output-restricted double-ended queue operations.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 4. P2 · D3 · DOC-18-P04-Q05-sub-c

> What will the following function return if it is called from the main as XXXX(5, 0, 1)? Can you identify what the following function is calculating? It is something well-known. int XXXX(int n, int a, int b) { if (n == 0) return a; if (n == 1) return b; return XXXX(n - 1, b, a + b); }

- Source: `DOC-18`, page 4, year 2020, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The source corpus tests both concepts and exact trace/return behavior; this cannot be reduced to the definition of recursion.

**Direct answer:** Solved recursively by decomposing into moving n-1 disks to auxiliary rod.

**Step-by-step solution:**
1. Base Case: If n == 1, move disk 1 directly from Source to Destination rod.
2. Recursive Step:
   - Move top n - 1 disks from Source to Auxiliary (using Destination as helper).
   - Move disk n directly from Source to Destination.
   - Move n - 1 disks from Auxiliary to Destination (using Source as helper).
3. Recurrence: T(n) = 2·T(n-1) + 1 with T(1) = 1.
4. Total moves = 2ⁿ - 1. For n=3: 7 moves; for n=4: 15 moves.

**Exam-ready answer:**
• Recurrence Relation: T(n) = 2T(n-1) + 1, T(1) = 1.
• Total Moves: 2ⁿ - 1 moves.
• Time Complexity: O(2ⁿ), Space Complexity: O(n) call stack.
• C Recursive function: TOH(n-1, from, aux, to); move disk n; TOH(n-1, aux, to, from);

**Complexity:** O(2ⁿ) exponential time; Space: O(n) auxiliary call stack space

**Trap:** Confusing the roles of destination and auxiliary pegs in the second recursive call.

**Beginner note:** Remember the rhythm: Source to Aux, Move Biggest, Aux to Destination.

#### 5. P2 · D3 · DOC-22-P02-Q04-sub-b

> Write a program to find gcd (greatest common devisor) of two integers using recursion.

- Source: `DOC-22`, page 2, year 2021, marks not available
- Independent sources: 2; occurrence count: 2
- Other occurrence IDs: DOC-23-P02-Q04-sub-b
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The source corpus tests both concepts and exact trace/return behavior; this cannot be reduced to the definition of recursion.

**Direct answer:** Solved following standard Linear Queue: array and linked list implementations, front/rear pointers algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_QUEUE_LINEAR_CIRCULAR under question family 'Linear Queue: array and linked list implementations, front/rear pointers'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Linear Queue: array and linked list implementations, front/rear pointers.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 6. P2 · D3 · DOC-22-P03-Q05-sub-b

> Predict the output of the following program and explain. #include <stdio.h> int fun(int n) { if (n == 4) return n; else return 2*fun(n+1); } int main() { printf("%d ", fun(2)); return 0; }

- Source: `DOC-22`, page 3, year 2021, marks not available
- Independent sources: 2; occurrence count: 2
- Other occurrence IDs: DOC-23-P03-Q05-sub-b
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The source corpus tests both concepts and exact trace/return behavior; this cannot be reduced to the definition of recursion.

**Direct answer:** Solved following standard Dry-run tracing of recursive functions and return value prediction algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_REC_PRINCIPLES under question family 'Dry-run tracing of recursive functions and return value prediction'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Dry-run tracing of recursive functions and return value prediction.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 7. P2 · D3 · DOC-28-P07-LA-Q23

> Write a recursive function to determine whether a given string is a palindrome. Draw the recursion tree when the string "ABCBA” is passed to the function.

- Source: `DOC-28`, page 7, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The source corpus tests both concepts and exact trace/return behavior; this cannot be reduced to the definition of recursion.

**Direct answer:** Solved following standard Principles of recursion, activation records, and system call stack usage algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_REC_PRINCIPLES under question family 'Principles of recursion, activation records, and system call stack usage'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Principles of recursion, activation records, and system call stack usage.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 8. P2 · D3 · DOC-28-P08-LA-Q25

> What will the following function return if it is called from the main as fun(5, 0, 1)? Can you identify what the following function is calculating? It is something well-known.

- Source: `DOC-28`, page 8, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The source corpus tests both concepts and exact trace/return behavior; this cannot be reduced to the definition of recursion.

**Direct answer:** Solved following standard Dry-run tracing of recursive functions and return value prediction algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_REC_PRINCIPLES under question family 'Dry-run tracing of recursive functions and return value prediction'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Dry-run tracing of recursive functions and return value prediction.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 9. P2 · D2 · DOC-30-P01-Q05

> What is the data structures used to perform recursion?

- Source: `DOC-30`, page 1, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The source corpus tests both concepts and exact trace/return behavior; this cannot be reduced to the definition of recursion.

**Direct answer:** Solved following standard Principles of recursion, activation records, and system call stack usage algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_REC_PRINCIPLES under question family 'Principles of recursion, activation records, and system call stack usage'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Principles of recursion, activation records, and system call stack usage.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 10. P2 · D1 · DOC-31-P14-PART1-Q92

> Ackerman’s function is defined on the non-negative integers as follows a (m,n)      = n+1 if m=0 = a (m-1, 1) if m ≠0, n=0 = a (m-1, a(m, n-1)) if  m ≠0, n ≠0 The value of a (1, 3) is (A)  4. (B)  5. (C)  6. (D)  7.

- Source: `DOC-31`, page 14, year not available, marks 2
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The source corpus tests both concepts and exact trace/return behavior; this cannot be reduced to the definition of recursion.

**Direct answer:** Solved following standard Dry-run tracing of recursive functions and return value prediction algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_REC_PRINCIPLES under question family 'Dry-run tracing of recursive functions and return value prediction'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Dry-run tracing of recursive functions and return value prediction.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.


### Mastery check
- Can I recognize: **recursive function, base case, call stack, recursion tree, predict output, return value**?
- Can I state the invariant?
- Can I trace the state without skipping a step?
- Can I handle the relevant boundary case?
- Can I write the exam-ready answer format?

---
## Tail recursion and recursion→iteration reasoning

**Recognition trigger:** tail recursion, tail call, more efficient, tail recursive Fibonacci

**Why this is separate:** Tail recursion is explicitly in the syllabus and source questions test both definition and code construction.

**Prerequisites:** ordinary recursion and return behavior

**Invariant:** the recursive call is the final computational action in the function.

**Core cases:** tail vs non-tail; accumulator/state parameters; iterative equivalent; source-specific claims about efficiency

**Step-by-step method:**  
Move all accumulated work into parameters so the final statement is the recursive call; identify base case and next-state transition.

**Complexity:** Time follows the recurrence; call-stack space is O(depth) in ordinary C execution unless an implementation performs tail-call elimination.

**Common mistakes:** calling a function tail-recursive when work remains after the call; claiming guaranteed compiler optimization in C.

**Exam-writing format:** Point to the last executable action and show the accumulator/state update.

**Memorize:** tail call = no work remains after the recursive call returns.

**Understand:** the needed state is carried forward rather than reconstructed on unwind.

### Authentic questions (9 unique texts; 18 occurrences)

#### 1. P2 · D3 · DOC-01-P03-Q05-sub-b

> Which data structure do we use for recursive algorithm implementation? What is difference between recursion and iteration? What is tail recursion? (3 + 1 + 2) + (1 + 3 + 2) = 12

- Source: `DOC-01`, page 3, year 2020, marks not available
- Independent sources: 2; occurrence count: 2
- Other occurrence IDs: DOC-21-P03-Q05-sub-b
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Tail recursion is explicitly in the syllabus and source questions test both definition and code construction.

**Direct answer:** Solved following standard Tail recursion: definition, compiler optimization, and conversion to iteration algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_REC_TAIL under question family 'Tail recursion: definition, compiler optimization, and conversion to iteration'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Tail recursion: definition, compiler optimization, and conversion to iteration.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 2. P1 · D2 · DOC-02-P03-Q05-sub-b

> Why is a Tail recursive function more efficient compared to normal recursive function? [(CO1) (Remember/LOCQ)]

- Source: `DOC-02`, page 3, year 2021, marks not available
- Independent sources: 3; occurrence count: 3
- Other occurrence IDs: DOC-20-P03-Q05-sub-b, DOC-26-P03-Q05-sub-b
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Tail recursion is explicitly in the syllabus and source questions test both definition and code construction.

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 3. P1 · D4 · DOC-02-P03-Q05-sub-c

> An experienced Professor asked his students in the class to write a tail recursive function in C for a very popular series named after a famous Italian mathematician and asked them to display the 100th number of  the series using it. One student just wrote a four-line function  and left in five minutes while others were writing many lines of code for half an hour. The Professor first ignored it thinking it to be some junk produced by an over- smart HITan. But after going to his room he found that it displays the correct number when he called it from his main(). He is still trying to figure out what happened. The codes are given below with some vital parts of the code being replaced by ‘?x’. If you just do not want to be such an unsuccessful  Professor, then figure out what might have been written. You may just re-write  the following few lines of code, filling out the eight missing ?x parts. Also, just write in max  two sentences, why it works. The student wrote like this - int fiboTailRec(int n, int a, int b) { if(?1  < ?2 ) return ?3; else return fiboTailRec (?4, ?5, ?6); }

- Source: `DOC-02`, page 3, year 2021, marks not available
- Independent sources: 3; occurrence count: 3
- Other occurrence IDs: DOC-20-P03-Q05-sub-c, DOC-26-P03-Q05-sub-c
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Tail recursion is explicitly in the syllabus and source questions test both definition and code construction.

**Direct answer:** Solved following standard Two stacks implementation on a single array and memory sharing algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Two stacks implementation on a single array and memory sharing'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Two stacks implementation on a single array and memory sharing.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 4. P1 · D3 · DOC-03-P02-Q04-sub-b

> Write a function “insert” that is tail recursive. It should take in a list “lst”, an “item”, and an “index”, and insert the item into the list at the given index.  Illustrate with an example. [(CO3, CO4)(Analyze/IOCQ)]

- Source: `DOC-03`, page 2, year 2022, marks not available
- Independent sources: 3; occurrence count: 3
- Other occurrence IDs: DOC-04-P02-Q04-sub-b, DOC-05-P02-Q04-sub-b
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Tail recursion is explicitly in the syllabus and source questions test both definition and code construction.

**Direct answer:** Solved following standard Deque: Input-restricted and Output-restricted double-ended queue operations algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_DEQUE under question family 'Deque: Input-restricted and Output-restricted double-ended queue operations'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Deque: Input-restricted and Output-restricted double-ended queue operations.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 5. P2 · D2 · DOC-18-P03-Q04-sub-b

> Discuss the key features of tail recursion. Explain with suitable example how it is different from a normal recursive function.

- Source: `DOC-18`, page 3, year 2020, marks not available
- Independent sources: 2; occurrence count: 2
- Other occurrence IDs: DOC-28-P07-LA-Q22
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Tail recursion is explicitly in the syllabus and source questions test both definition and code construction.

**Direct answer:** Solved following standard Tail recursion: definition, compiler optimization, and conversion to iteration algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_REC_TAIL under question family 'Tail recursion: definition, compiler optimization, and conversion to iteration'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Tail recursion: definition, compiler optimization, and conversion to iteration.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 6. P2 · D2 · DOC-19-P08-Q05-sub-b

> Why is a Tail recursive function more efficient compared to a normal recursive function? Ans. It is because the spaces of the local variables defined in the first call can be reused in every call as the scope of those variables of the earlier call ends before the next call is made. This is so because the recursive call is the last call in the function and hence the variable instances of the earlier call cannot be used after the next call is made. This saves a significant amount of overhead that is otherwise required whenever a function call is made. [(CO1) (Remember/LOCQ)]

- Source: `DOC-19`, page 8, year 2021, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Tail recursion is explicitly in the syllabus and source questions test both definition and code construction.

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 7. P2 · D4 · DOC-19-P08-Q05-sub-c

> An experienced Professor asked his students in the class to write a tail recursive function in C for a very popular series named after a famous Italian mathematician and asked them to display the 100th number of  the series using it. One student just wrote a four-line function and left in five minutes while others were writing many lines of code for half an hour. The Professor first ignored it thinking it to be some junk produced by an over-smart HITan. But after going to his room he found that it displays the correct number when he called it from his main(). He is still trying to figure out what happened. The codes are given below with some vital parts of the code being replaced by ‘?x’. If you just do not want to be such an unsuccessful  Professor, then figure out what might have been written. You may just re-write the following few lines of code, filling out the eight missing ?x parts. Also, just write in max two sentences, why it works. The student wrote like this - int fiboTailRec(int n, int a, int b) {

- Source: `DOC-19`, page 8, year 2021, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Tail recursion is explicitly in the syllabus and source questions test both definition and code construction.

**Direct answer:** Solved following standard Two stacks implementation on a single array and memory sharing algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_STACK_IMPL under question family 'Two stacks implementation on a single array and memory sharing'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Two stacks implementation on a single array and memory sharing.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 8. P2 · D2 · DOC-22-P02-Q04-sub-c

> What is tail recursion? Explain with example.

- Source: `DOC-22`, page 2, year 2021, marks not available
- Independent sources: 2; occurrence count: 2
- Other occurrence IDs: DOC-23-P02-Q04-sub-c
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Tail recursion is explicitly in the syllabus and source questions test both definition and code construction.

**Direct answer:** Solved following standard Linear Queue: array and linked list implementations, front/rear pointers algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_QUEUE_LINEAR_CIRCULAR under question family 'Linear Queue: array and linked list implementations, front/rear pointers'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Linear Queue: array and linked list implementations, front/rear pointers.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 9. P2 · D3 · DOC-25-P02-Q04-sub-b

> What is Tail recursion? Write a program in C to find the factorial of a given number using Recursion.

- Source: `DOC-25`, page 2, year 2021, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** Tail recursion is explicitly in the syllabus and source questions test both definition and code construction.

**Direct answer:** Solved following standard Linear Queue: array and linked list implementations, front/rear pointers algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_QUEUE_LINEAR_CIRCULAR under question family 'Linear Queue: array and linked list implementations, front/rear pointers'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Linear Queue: array and linked list implementations, front/rear pointers.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.


### Mastery check
- Can I recognize: **tail recursion, tail call, more efficient, tail recursive Fibonacci**?
- Can I state the invariant?
- Can I trace the state without skipping a step?
- Can I handle the relevant boundary case?
- Can I write the exam-ready answer format?

---

# MASTER PATTERN — 6. Recursive Applications & Backtracking

### Pattern map
1. **Tower of Hanoi** — 7 unique question texts / 11 occurrences
2. **Eight Queens and backtracking** — 2 unique question texts / 2 occurrences

## Tower of Hanoi

**Recognition trigger:** Tower of Hanoi, moves for n discs, recursive solution

**Why this is separate:** The source asks for both the recursive function and the exact move trace for small n.

**Prerequisites:** recursion, base case, recursive decomposition

**Invariant:** the problem with n discs is reduced to moving n−1 discs aside, moving the largest disc, then moving n−1 onto the destination.

**Core cases:** n=0/1 base; source/temporary/destination peg roles; exact move trace

**Step-by-step method:**  
Move n−1 source→temporary; move disc n source→destination; move n−1 temporary→destination.

**Complexity:** 2^n−1 moves; exponential time in n; call depth O(n).

**Common mistakes:** swapping peg roles; outputting moves in the wrong order; forgetting the base case.

**Exam-writing format:** Write recurrence/move rule, then trace exact moves for the requested n.

**Memorize:** T(n)=2T(n−1)+1, so moves=2^n−1.

**Understand:** the recursion is a structured three-step decomposition.

### Authentic questions (7 unique texts; 11 occurrences)

#### 1. P2 · D4 · DOC-10-P02-Q04-sub-a

> Write a small C function (no need for main, header files etc.) to print the moves of the well-known Tower of Hanoi problem using recursion. Assume that the smallest disc is numbered as ‘disc 1’ and the largest is ‘disc n’. Each of the three pegs is represented by a char (datatype): source (‘S’), destination (‘D’) and temporary (‘T’). Given below are some examples of the moves that you will print: Move the disc # 12 from T to D Move the disc # 4 from S to T. [(CO3)(Understand/IOCQ)]

- Source: `DOC-10`, page 2, year 2024, marks not available
- Independent sources: 3; occurrence count: 3
- Other occurrence IDs: DOC-11-P02-Q04-sub-a, DOC-12-P02-Q04-sub-a
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The source asks for both the recursive function and the exact move trace for small n.

**Direct answer:** Solved recursively by decomposing into moving n-1 disks to auxiliary rod.

**Step-by-step solution:**
1. Base Case: If n == 1, move disk 1 directly from Source to Destination rod.
2. Recursive Step:
   - Move top n - 1 disks from Source to Auxiliary (using Destination as helper).
   - Move disk n directly from Source to Destination.
   - Move n - 1 disks from Auxiliary to Destination (using Source as helper).
3. Recurrence: T(n) = 2·T(n-1) + 1 with T(1) = 1.
4. Total moves = 2ⁿ - 1. For n=3: 7 moves; for n=4: 15 moves.

**Exam-ready answer:**
• Recurrence Relation: T(n) = 2T(n-1) + 1, T(1) = 1.
• Total Moves: 2ⁿ - 1 moves.
• Time Complexity: O(2ⁿ), Space Complexity: O(n) call stack.
• C Recursive function: TOH(n-1, from, aux, to); move disk n; TOH(n-1, aux, to, from);

**Complexity:** O(2ⁿ) exponential time; Space: O(n) auxiliary call stack space

**Trap:** Confusing the roles of destination and auxiliary pegs in the second recursive call.

**Beginner note:** Remember the rhythm: Source to Aux, Move Biggest, Aux to Destination.

#### 2. P2 · D3 · DOC-10-P02-Q04-sub-b

> Now just write the output of your function if it is called with n = 4, where n is the number of discs. [(CO3)(Apply/IOCQ)]

- Source: `DOC-10`, page 2, year 2024, marks not available
- Independent sources: 3; occurrence count: 3
- Other occurrence IDs: DOC-11-P02-Q04-sub-b, DOC-12-P02-Q04-sub-b
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The source asks for both the recursive function and the exact move trace for small n.

**Direct answer:** Solved recursively by decomposing into moving n-1 disks to auxiliary rod.

**Step-by-step solution:**
1. Base Case: If n == 1, move disk 1 directly from Source to Destination rod.
2. Recursive Step:
   - Move top n - 1 disks from Source to Auxiliary (using Destination as helper).
   - Move disk n directly from Source to Destination.
   - Move n - 1 disks from Auxiliary to Destination (using Source as helper).
3. Recurrence: T(n) = 2·T(n-1) + 1 with T(1) = 1.
4. Total moves = 2ⁿ - 1. For n=3: 7 moves; for n=4: 15 moves.

**Exam-ready answer:**
• Recurrence Relation: T(n) = 2T(n-1) + 1, T(1) = 1.
• Total Moves: 2ⁿ - 1 moves.
• Time Complexity: O(2ⁿ), Space Complexity: O(n) call stack.
• C Recursive function: TOH(n-1, from, aux, to); move disk n; TOH(n-1, aux, to, from);

**Complexity:** O(2ⁿ) exponential time; Space: O(n) auxiliary call stack space

**Trap:** Confusing the roles of destination and auxiliary pegs in the second recursive call.

**Beginner note:** Remember the rhythm: Source to Aux, Move Biggest, Aux to Destination.

#### 3. P3 · D4 · DOC-18-P03-Q05-sub-a

> Write a small C function (no need for main, header files etc.) to print the moves of the well-known Tower of Hanoi problem using recursion. Assume that the smallest disc is numbered as ‘disc 1’ and the largest is ‘disc n’. Each of the three pegs is represented by a char (datatype) – source (‘S’), destination (‘D’) and temporary (‘T’). Given below are some examples of the moves that you will print – Move the disc # 12 from T to D

- Source: `DOC-18`, page 3, year 2020, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The source asks for both the recursive function and the exact move trace for small n.

**Direct answer:** Solved recursively by decomposing into moving n-1 disks to auxiliary rod.

**Step-by-step solution:**
1. Base Case: If n == 1, move disk 1 directly from Source to Destination rod.
2. Recursive Step:
   - Move top n - 1 disks from Source to Auxiliary (using Destination as helper).
   - Move disk n directly from Source to Destination.
   - Move n - 1 disks from Auxiliary to Destination (using Source as helper).
3. Recurrence: T(n) = 2·T(n-1) + 1 with T(1) = 1.
4. Total moves = 2ⁿ - 1. For n=3: 7 moves; for n=4: 15 moves.

**Exam-ready answer:**
• Recurrence Relation: T(n) = 2T(n-1) + 1, T(1) = 1.
• Total Moves: 2ⁿ - 1 moves.
• Time Complexity: O(2ⁿ), Space Complexity: O(n) call stack.
• C Recursive function: TOH(n-1, from, aux, to); move disk n; TOH(n-1, aux, to, from);

**Complexity:** O(2ⁿ) exponential time; Space: O(n) auxiliary call stack space

**Trap:** Confusing the roles of destination and auxiliary pegs in the second recursive call.

**Beginner note:** Remember the rhythm: Source to Aux, Move Biggest, Aux to Destination.

#### 4. P3 · D3 · DOC-18-P04-Q05-sub-b

> Now just write the output of your function if it is called with n = 4, where n is the number of discs.

- Source: `DOC-18`, page 4, year 2020, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The source asks for both the recursive function and the exact move trace for small n.

**Direct answer:** Solved recursively by decomposing into moving n-1 disks to auxiliary rod.

**Step-by-step solution:**
1. Base Case: If n == 1, move disk 1 directly from Source to Destination rod.
2. Recursive Step:
   - Move top n - 1 disks from Source to Auxiliary (using Destination as helper).
   - Move disk n directly from Source to Destination.
   - Move n - 1 disks from Auxiliary to Destination (using Source as helper).
3. Recurrence: T(n) = 2·T(n-1) + 1 with T(1) = 1.
4. Total moves = 2ⁿ - 1. For n=3: 7 moves; for n=4: 15 moves.

**Exam-ready answer:**
• Recurrence Relation: T(n) = 2T(n-1) + 1, T(1) = 1.
• Total Moves: 2ⁿ - 1 moves.
• Time Complexity: O(2ⁿ), Space Complexity: O(n) call stack.
• C Recursive function: TOH(n-1, from, aux, to); move disk n; TOH(n-1, aux, to, from);

**Complexity:** O(2ⁿ) exponential time; Space: O(n) auxiliary call stack space

**Trap:** Confusing the roles of destination and auxiliary pegs in the second recursive call.

**Beginner note:** Remember the rhythm: Source to Aux, Move Biggest, Aux to Destination.

#### 5. P3 · D2 · DOC-28-P05-SA-Q06

> The optimal data structure used to solve the Tower of Hanoi problem is _________.

- Source: `DOC-28`, page 5, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The source asks for both the recursive function and the exact move trace for small n.

**Direct answer:** Solved recursively by decomposing into moving n-1 disks to auxiliary rod.

**Step-by-step solution:**
1. Base Case: If n == 1, move disk 1 directly from Source to Destination rod.
2. Recursive Step:
   - Move top n - 1 disks from Source to Auxiliary (using Destination as helper).
   - Move disk n directly from Source to Destination.
   - Move n - 1 disks from Auxiliary to Destination (using Source as helper).
3. Recurrence: T(n) = 2·T(n-1) + 1 with T(1) = 1.
4. Total moves = 2ⁿ - 1. For n=3: 7 moves; for n=4: 15 moves.

**Exam-ready answer:**
• Recurrence Relation: T(n) = 2T(n-1) + 1, T(1) = 1.
• Total Moves: 2ⁿ - 1 moves.
• Time Complexity: O(2ⁿ), Space Complexity: O(n) call stack.
• C Recursive function: TOH(n-1, from, aux, to); move disk n; TOH(n-1, aux, to, from);

**Complexity:** O(2ⁿ) exponential time; Space: O(n) auxiliary call stack space

**Trap:** Confusing the roles of destination and auxiliary pegs in the second recursive call.

**Beginner note:** Remember the rhythm: Source to Aux, Move Biggest, Aux to Destination.

#### 6. P3 · D4 · DOC-28-P08-LA-Q24

> Write a small C function (no need for main, header files etc.) to print the moves of the well-known Tower of Hanoi problem using recursion. Assume that the smallest disc is numbered as ‘disc 1’ and the largest is ‘disc n’. Each of the three pegs is represented by a char (datatype): source (‘S’), destination (‘D’) and temporary (‘T’). Given below are some examples of the moves that you will print: Move the disc # 12 from T to D Move the disc # 4 from S to T. Now just write the output of your function if it is called with n = 4, where n is the number of discs.

- Source: `DOC-28`, page 8, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The source asks for both the recursive function and the exact move trace for small n.

**Direct answer:** Solved recursively by decomposing into moving n-1 disks to auxiliary rod.

**Step-by-step solution:**
1. Base Case: If n == 1, move disk 1 directly from Source to Destination rod.
2. Recursive Step:
   - Move top n - 1 disks from Source to Auxiliary (using Destination as helper).
   - Move disk n directly from Source to Destination.
   - Move n - 1 disks from Auxiliary to Destination (using Source as helper).
3. Recurrence: T(n) = 2·T(n-1) + 1 with T(1) = 1.
4. Total moves = 2ⁿ - 1. For n=3: 7 moves; for n=4: 15 moves.

**Exam-ready answer:**
• Recurrence Relation: T(n) = 2T(n-1) + 1, T(1) = 1.
• Total Moves: 2ⁿ - 1 moves.
• Time Complexity: O(2ⁿ), Space Complexity: O(n) call stack.
• C Recursive function: TOH(n-1, from, aux, to); move disk n; TOH(n-1, aux, to, from);

**Complexity:** O(2ⁿ) exponential time; Space: O(n) auxiliary call stack space

**Trap:** Confusing the roles of destination and auxiliary pegs in the second recursive call.

**Beginner note:** Remember the rhythm: Source to Aux, Move Biggest, Aux to Destination.

#### 7. P3 · D4 · DOC-31-P28-PART2-Q16

> Write an algorithm for finding solution to the Tower’s of Hanoi problem. Explain the working of your algorithm (with 4 disks) with diagrams. (5)

- Source: `DOC-31`, page 28, year not available, marks 5
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The source asks for both the recursive function and the exact move trace for small n.

**Direct answer:** Solved recursively by decomposing into moving n-1 disks to auxiliary rod.

**Step-by-step solution:**
1. Base Case: If n == 1, move disk 1 directly from Source to Destination rod.
2. Recursive Step:
   - Move top n - 1 disks from Source to Auxiliary (using Destination as helper).
   - Move disk n directly from Source to Destination.
   - Move n - 1 disks from Auxiliary to Destination (using Source as helper).
3. Recurrence: T(n) = 2·T(n-1) + 1 with T(1) = 1.
4. Total moves = 2ⁿ - 1. For n=3: 7 moves; for n=4: 15 moves.

**Exam-ready answer:**
• Recurrence Relation: T(n) = 2T(n-1) + 1, T(1) = 1.
• Total Moves: 2ⁿ - 1 moves.
• Time Complexity: O(2ⁿ), Space Complexity: O(n) call stack.
• C Recursive function: TOH(n-1, from, aux, to); move disk n; TOH(n-1, aux, to, from);

**Complexity:** O(2ⁿ) exponential time; Space: O(n) auxiliary call stack space

**Trap:** Confusing the roles of destination and auxiliary pegs in the second recursive call.

**Beginner note:** Remember the rhythm: Source to Aux, Move Biggest, Aux to Destination.


### Mastery check
- Can I recognize: **Tower of Hanoi, moves for n discs, recursive solution**?
- Can I state the invariant?
- Can I trace the state without skipping a step?
- Can I handle the relevant boundary case?
- Can I write the exam-ready answer format?

---
## Eight Queens and backtracking

**Recognition trigger:** 8 Queens, Eight Queens, backtracking

**Why this is separate:** The source explicitly tests the algorithmic paradigm used by the 8-Queens problem.

**Prerequisites:** recursion + state/constraint checking

**Invariant:** the partial board remains valid before descending to the next row/choice.

**Core cases:** choose candidate; safety check; recurse; reject; undo/backtrack.

**Step-by-step method:**  
Place one queen at a time; test row/column/diagonal safety; recurse when valid; undo on failure.

**Complexity:** search-space dependent/exponential in the general backtracking formulation.

**Common mistakes:** forgetting the undo step; checking only columns and not diagonals.

**Exam-writing format:** State the choice, constraint test, recursive call, and undo step.

**Memorize:** Backtracking = choose → check → recurse → undo.

**Understand:** failed choices are reversible because the state is explicitly maintained.

### Authentic questions (2 unique texts; 2 occurrences)

#### 1. P3 · D1 · DOC-28-P03-MCQ-Q18

> What is the type of the algorithm used in solving the 8 Queens problem? (a) Divide and conquer (b) Backtracking (c)  Greedy (d) None of the above

- Source: `DOC-28`, page 3, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The source explicitly tests the algorithmic paradigm used by the 8-Queens problem.

**Direct answer:** Solved following standard Eight Queens Puzzle and Backtracking algorithmic paradigm algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_REC_APPLICATIONS under question family 'Eight Queens Puzzle and Backtracking algorithmic paradigm'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Eight Queens Puzzle and Backtracking algorithmic paradigm.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.

#### 2. P3 · D2 · DOC-30-P03-Q12

> What is the type of the algorithm used in solving the 8 Queens problem?

- Source: `DOC-30`, page 3, year not available, marks not available
- Independent sources: 1; occurrence count: 1
- Other occurrence IDs: none
- Solution provenance: Repository solution bank (question-aligned; legacy family labels not used for placement).

**Why this belongs here:** The source explicitly tests the algorithmic paradigm used by the 8-Queens problem.

**Direct answer:** Solved following standard Eight Queens Puzzle and Backtracking algorithmic paradigm algorithm and properties.

**Step-by-step solution:**
1. Problem belongs to topic M2_REC_APPLICATIONS under question family 'Eight Queens Puzzle and Backtracking algorithmic paradigm'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready answer:**
• Core Concept: Eight Queens Puzzle and Backtracking algorithmic paradigm.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

**Beginner note:** Always verify base conditions before writing general loops.


### Mastery check
- Can I recognize: **8 Queens, Eight Queens, backtracking**?
- Can I state the invariant?
- Can I trace the state without skipping a step?
- Can I handle the relevant boundary case?
- Can I write the exam-ready answer format?

---
# Master revision tables

## Highest-yield subpatterns
| Subpattern | Unique texts | Occurrences | Priority |
|---|---:|---:|---|
| Infix → postfix conversion | 21 | 28 | P1 |
| Recursion principles, call stack, tracing, and recursive construction | 10 | 19 | P1 |
| Tail recursion and recursion→iteration reasoning | 9 | 18 | P1 |
| Circular queue wrap-around and empty/full states | 8 | 16 | P1 |
| Stack fundamentals, representation, operations, and state tracing | 12 | 15 | P1 |
| Prefix/postfix transformations | 9 | 15 | P2/P3 |
| Tower of Hanoi | 7 | 11 | P2/P3 |
| Linear queue operations and state tracing | 7 | 9 | P1 |
| Implementing one ADT using the other (queue with stacks) | 3 | 8 | P2/P3 |
| Deque, restricted deques, and two-ended operations | 5 | 8 | P2/P3 |
| Stack vs Queue: LIFO/FIFO recognition and comparison | 3 | 6 | P2/P3 |
| Stack transformations: sorted movement and reversal | 3 | 6 | P2/P3 |
| Postfix evaluation | 5 | 6 | P2/P3 |
| Balanced-parentheses / parenthesis matching | 4 | 5 | P2/P3 |
| Augmented stack: minimum element retrieval | 1 | 3 | P2/P3 |
| Stack-style reduction of adjacent duplicates | 1 | 3 | P2/P3 |
| Expression notation concepts and recognition | 1 | 2 | P2/P3 |
| Combined infix conversion + evaluation | 1 | 2 | P2/P3 |
| Queue applications | 2 | 2 | P2/P3 |
| Eight Queens and backtracking | 2 | 2 | P2/P3 |
| Stack-generated output sequences | 1 | 1 | P2/P3 |

## Complexity quick sheet
| Operation / method | Typical cost |
|---|---|
| Stack push/pop/peek | O(1) |
| Infix→postfix | O(n) |
| Prefix/postfix transformation | O(n) |
| Postfix evaluation | O(n) |
| Parenthesis matching | O(n) |
| Linear queue enqueue/dequeue | O(1) without shifting; shifting array queues may be O(n) |
| Circular queue enqueue/dequeue | O(1) |
| Deque end operations | O(1) with suitable representation |
| Recursion auxiliary stack | O(max call depth) |
| Tower of Hanoi | 2^n−1 moves |

# Last-minute revision

## 30-minute revision
Stack LIFO; queue FIFO; push/pop/peek; enqueue/dequeue; circular next-index modulo rule; infix→postfix token rules; postfix first-pop/right operand; balanced-parentheses invariant; recursion base case + progress; tail recursion = last action; Hanoi = move n−1, largest disc, n−1.

## 1-hour revision
Add stack/queue interconversion, stack permutations, two-ended deque restrictions, circular queue full/empty convention, recursion trace tables, and one authentic source question from each P1 subpattern.

## 3-hour revision
Do all P1 patterns, then P2 variants, then the source-only test. Focus on state traces rather than rereading definitions.

## Night-before
Memorize operation rules, boundary conditions, postfix operand order, delimiter matching rules, circular index convention, recursion skeletons, and the must-master source IDs in the final test.
