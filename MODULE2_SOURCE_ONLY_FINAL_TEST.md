# CSE2101 / CSEN2101 — Module 2 Source-Only Final Test

**Rules:** Every question below is an authentic repository question. No synthetic questions are included. Attempt the test before reading the answer key.

## Test paper
### Q1 — P2 · D1
**Source:** DOC-30, page 8, year not available, marks not available

> Consider the following stack of characters, where STACK is allocated N = 8 mmory cells STACK : A,C,D,F,K,_,_,_. ( _ means empty allocated cell) Describe the stack as the following operations takes place: (a) POP(STACK, ITEM) (b) POP(STACK, ITEM) (c) POP(STACK, ITEM) (d) PUSH(STACK, R) (e) PUSH(STACK,L) (f) PUSH(STACK, S) (g) PUSH(STACK,P) (h) POP(STACK, ITEM)

### Q2 — P2 · D3
**Source:** DOC-22, page 3, year 2021, marks not available

> Write an algorithm to convert an infix expression to postfix. Convert the expression given below into its corresponding postfix expression. Show each step of the conversion. 10 + ((75) +2* 3^2^2)/2

### Q3 — P3 · D3
**Source:** DOC-22, page 3, year 2021, marks not available

> Write an algorithm to check whether a given expression contains balanced parentheses or not, note that only ‘(’and ‘)’ are allowed here as parentheses. (3 + 3) + 3 + 3 = 12

### Q4 — P2 · D3
**Source:** DOC-22, page 2, year 2021, marks not available

> Write a program to implement insertion and deletion of elements in a circular queue (using array). Also, incorporate the checking for underflow and overflow.

### Q5 — P2 · D3
**Source:** DOC-31, page 19, year not available, marks 7

> What are circular queues?  Write down routines for inserting and deleting elements from a circular queue implemented using arrays. (7)

### Q6 — P3 · D3
**Source:** DOC-31, page 54, year not available, marks 8

> A double ended queue is a linear list where additions and deletions can be performed at either end. Represent a double ended queue using an array to store elements and write modules for additions and deletions. (8)

### Q7 — P3 · D4
**Source:** DOC-18, page 3, year 2020, marks not available

> Write a small C function (no need for main, header files etc.) to print the moves of the well-known Tower of Hanoi problem using recursion. Assume that the smallest disc is numbered as ‘disc 1’ and the largest is ‘disc n’. Each of the three pegs is represented by a char (datatype) – source (‘S’), destination (‘D’) and temporary (‘T’). Given below are some examples of the moves that you will print – Move the disc # 12 from T to D

### Q8 — P3 · D3
**Source:** DOC-31, page 19, year not available, marks 7

> Write an algorithm to evaluate a postfix expression.  Execute your algorithm using the following postfix expression as your input : a b + c d +*f ↑. (7)

### Q9 — P3 · D4
**Source:** DOC-31, page 28, year not available, marks 5

> Write an algorithm for finding solution to the Tower’s of Hanoi problem. Explain the working of your algorithm (with 4 disks) with diagrams. (5)

### Q10 — P3 · D1
**Source:** DOC-28, page 3, year not available, marks not available

> What is the type of the algorithm used in solving the 8 Queens problem? (a) Divide and conquer (b) Backtracking (c)  Greedy (d) None of the above


# Answer key and solutions

## Q1 — DOC-30-P08-Q32

**Direct answer:** Solved following standard Stack implementation using array and linked list, overflow and underflow conditions algorithm and properties.

**Solution:**  
1. Problem belongs to topic M2_STACK_IMPL under question family 'Stack implementation using array and linked list, overflow and underflow conditions'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready:**  
• Core Concept: Stack implementation using array and linked list, overflow and underflow conditions.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

## Q2 — DOC-22-P03-Q05-sub-a

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Solution:**  
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready:**  
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

## Q3 — DOC-22-P03-Q05-sub-c

**Direct answer:** Solved following standard Parenthesis matching and balanced bracket checking using stack algorithm and properties.

**Solution:**  
1. Problem belongs to topic M2_STACK_APPLICATIONS under question family 'Parenthesis matching and balanced bracket checking using stack'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready:**  
• Core Concept: Parenthesis matching and balanced bracket checking using stack.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

## Q4 — DOC-22-P02-Q04-sub-a

**Direct answer:** Circular Queue wraps around indices using modulo arithmetic: (rear + 1) % MAX.

**Solution:**  
1. Front points to removal position; Rear points to last inserted position.
2. Full Condition: `(rear + 1) % MAX == front`.
3. Empty Condition: `front == -1` (or `front == rear` depending on convention).
4. Enqueue: `rear = (rear + 1) % MAX; queue[rear] = item;` (if empty, `front = rear = 0`).
5. Dequeue: `item = queue[front]; if (front == rear) front = rear = -1; else front = (front + 1) % MAX;`
6. Eliminates linear queue false overflow where rear reaches MAX-1 but front slots are empty.

**Exam-ready:**  
• Advantage over Linear Queue: Solves false overflow and memory wastage without shifting elements.
• Full Condition: `(rear + 1) % MAX == front`.
• Empty Condition: `front == -1 && rear == -1`.
• Complexity: O(1) time for both Enqueue and Dequeue.

**Complexity:** O(1) for enqueue and dequeue; Space: O(n) fixed array buffer

**Trap:** Using standard rear++ which causes index out of bounds instead of `(rear + 1) % MAX`.

## Q5 — DOC-31-P19-PART2-Q07

**Direct answer:** Circular Queue wraps around indices using modulo arithmetic: (rear + 1) % MAX.

**Solution:**  
1. Front points to removal position; Rear points to last inserted position.
2. Full Condition: `(rear + 1) % MAX == front`.
3. Empty Condition: `front == -1` (or `front == rear` depending on convention).
4. Enqueue: `rear = (rear + 1) % MAX; queue[rear] = item;` (if empty, `front = rear = 0`).
5. Dequeue: `item = queue[front]; if (front == rear) front = rear = -1; else front = (front + 1) % MAX;`
6. Eliminates linear queue false overflow where rear reaches MAX-1 but front slots are empty.

**Exam-ready:**  
• Advantage over Linear Queue: Solves false overflow and memory wastage without shifting elements.
• Full Condition: `(rear + 1) % MAX == front`.
• Empty Condition: `front == -1 && rear == -1`.
• Complexity: O(1) time for both Enqueue and Dequeue.

**Complexity:** O(1) for enqueue and dequeue; Space: O(n) fixed array buffer

**Trap:** Using standard rear++ which causes index out of bounds instead of `(rear + 1) % MAX`.

## Q6 — DOC-31-P54-PART2-Q57

**Direct answer:** Solved following standard Deque: Input-restricted and Output-restricted double-ended queue operations algorithm and properties.

**Solution:**  
1. Problem belongs to topic M2_DEQUE under question family 'Deque: Input-restricted and Output-restricted double-ended queue operations'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready:**  
• Core Concept: Deque: Input-restricted and Output-restricted double-ended queue operations.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

## Q7 — DOC-18-P03-Q05-sub-a

**Direct answer:** Solved recursively by decomposing into moving n-1 disks to auxiliary rod.

**Solution:**  
1. Base Case: If n == 1, move disk 1 directly from Source to Destination rod.
2. Recursive Step:
   - Move top n - 1 disks from Source to Auxiliary (using Destination as helper).
   - Move disk n directly from Source to Destination.
   - Move n - 1 disks from Auxiliary to Destination (using Source as helper).
3. Recurrence: T(n) = 2·T(n-1) + 1 with T(1) = 1.
4. Total moves = 2ⁿ - 1. For n=3: 7 moves; for n=4: 15 moves.

**Exam-ready:**  
• Recurrence Relation: T(n) = 2T(n-1) + 1, T(1) = 1.
• Total Moves: 2ⁿ - 1 moves.
• Time Complexity: O(2ⁿ), Space Complexity: O(n) call stack.
• C Recursive function: TOH(n-1, from, aux, to); move disk n; TOH(n-1, aux, to, from);

**Complexity:** O(2ⁿ) exponential time; Space: O(n) auxiliary call stack space

**Trap:** Confusing the roles of destination and auxiliary pegs in the second recursive call.

## Q8 — DOC-31-P19-PART2-Q06

**Direct answer:** Converted by Shunting-Yard algorithm using an operator stack.

**Solution:**  
1. Initialize an empty operator stack and empty output string.
2. Scan infix expression from left to right:
   - If operand: append directly to output.
   - If '(': push onto stack.
   - If ')': pop and append to output until '(' is encountered; discard '('.
   - If operator op: while stack top has higher or equal precedence (strict > if right-associative ^), pop and append to output; then push op.
3. At end of input, pop and append all remaining operators from stack.

**Exam-ready:**  
• Method: Use an operator stack based on operator precedence: () > ^ > *, / > +, -.
• Table of Execution: [Symbol Scanned, Stack Contents, Output Expression].
• Operands pass directly to output; operators wait on stack until lower precedence arrives.
• Final Postfix Expression is verified parenthesis-free.

**Complexity:** O(n) linear scan; Space: O(n) stack space

**Trap:** Treating ^ as left-associative instead of right-associative, or outputting '(' into the postfix string.

## Q9 — DOC-31-P28-PART2-Q16

**Direct answer:** Solved recursively by decomposing into moving n-1 disks to auxiliary rod.

**Solution:**  
1. Base Case: If n == 1, move disk 1 directly from Source to Destination rod.
2. Recursive Step:
   - Move top n - 1 disks from Source to Auxiliary (using Destination as helper).
   - Move disk n directly from Source to Destination.
   - Move n - 1 disks from Auxiliary to Destination (using Source as helper).
3. Recurrence: T(n) = 2·T(n-1) + 1 with T(1) = 1.
4. Total moves = 2ⁿ - 1. For n=3: 7 moves; for n=4: 15 moves.

**Exam-ready:**  
• Recurrence Relation: T(n) = 2T(n-1) + 1, T(1) = 1.
• Total Moves: 2ⁿ - 1 moves.
• Time Complexity: O(2ⁿ), Space Complexity: O(n) call stack.
• C Recursive function: TOH(n-1, from, aux, to); move disk n; TOH(n-1, aux, to, from);

**Complexity:** O(2ⁿ) exponential time; Space: O(n) auxiliary call stack space

**Trap:** Confusing the roles of destination and auxiliary pegs in the second recursive call.

## Q10 — DOC-28-P03-MCQ-Q18

**Direct answer:** Solved following standard Eight Queens Puzzle and Backtracking algorithmic paradigm algorithm and properties.

**Solution:**  
1. Problem belongs to topic M2_REC_APPLICATIONS under question family 'Eight Queens Puzzle and Backtracking algorithmic paradigm'.
2. Identify input parameters and boundary conditions from problem statement.
3. Apply standard data structure invariant and execution procedure.
4. Verify correctness and state final result clearly.

**Exam-ready:**  
• Core Concept: Eight Queens Puzzle and Backtracking algorithmic paradigm.
• State formal definition and structural rules.
• Provide step-by-step algorithm or calculation.
• State asymptotic time and space bounds.

**Complexity:** O(n) / O(1) depending on operation; Space: O(1) auxiliary

**Trap:** Overlooking edge cases (empty structure, single element).

