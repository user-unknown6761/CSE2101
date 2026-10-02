# DOC-28 Page 2 Reconstruction & Integrity Audit
**Document ID:** `DOC-28`  
**Filename:** `DSA Practice Assignment.pdf`  
**Physical Source Path:** `SOURCE/DSA-20260930T180448Z-1-001/DSA/DSA Practice Assignment.pdf`  
**Target Page:** Page 2 (0-indexed page 1) & Boundary Page 3 (0-indexed page 2)  
**Audit Date:** 2026-10-02  
**Governance Standard:** Prompt 1.1 Sections 3, 4, 5, 6, 15  

---

## 1. Physical Layout Forensic Analysis

Visual rendering of Page 2 (`scratch_doc28_p2.png`) at 150 DPI demonstrates that the PDF page layout was generated via a multi-column desktop publishing tool with 3 horizontal bounding bands:
1. **Left Text Stream (x ≈ 59.8 – 244.6):** Contains starting fragments of questions 7, 8, 9, 10, 11, and left fragments of multiple-choice option lists.
2. **Center Text Stream (x ≈ 236.3 – 459.0):** Contains continuation fragments of question stems and right fragments of option lines.
3. **Right Text Stream (x ≈ 450.8 – 554.6):** Contains terminal phrases (e.g. `with only a start`, `following linked list:`, `data structure. One`, `lexity, using a 1D`).

In addition to text streams, Page 2 hosts two embedded raster images and one vector diagram region:
- **Raster Image xref 22** (`Rect(128.88, 161.76, 278.16, 252.12)`): Embedded bitmap containing the 10-line C code function `void fun(struct node* start)`.
- **Vector Graph Diagram Region** (`y ≈ 336.0 – 398.0`): 6-vertex undirected graph diagram with nodes $\{M, N, O, P, Q, R\}$.
- **Raster Image xref 24** (`Rect(196.56, 490.32, 238.32, 614.76)`): Embedded bitmap containing the 6-node binary tree structure.

### Naive Extraction Failure Mode (Prior Phase 1)
Sequential reading of stream blocks by naive PyMuPDF extraction generated cross-question interleaving:
- Stem of Q7 was truncated at `following state`, followed immediately by option fragments, then wrapped into Q8.
- The C code in Q8 was omitted from text stream.
- Center-stream blocks of Q7 (`ements is correct for a circular singly linked list w`) were injected into Q11.
- Q12 (which physically resides on Page 3) was misattributed to Page 2 due to a regex newline boundary offset and mislabeled as `STATE B`.

---

## 2. Release Gate Audit: Questions 7 to 12

Below is the verified audit demonstrating compliance with Prompt 1.1 Section 15.

### Question 7: Circular Singly Linked List (Intact)
- **Question Instance ID:** `DOC-28-P02-MCQ-Q07`
- **Physical Page:** Page 2
- **Wording State:** `STATE B — RECONSTRUCTED`
- **Reconstruction Method:** Visual layout reassembly from rendered source page 2 to resolve three-column horizontal text fragmentation and assemble intact stem and options.
- **Visual Source Reference:** `SOURCE/DSA-20260930T180448Z-1-001/DSA/DSA Practice Assignment.pdf Page 2`
- **Reconstruction Confidence:** `HIGH`
- **Source Visual Required:** `false` (All options and text are fully recovered textual statements)
- **Reconstructed Question Text:**
  ```text
  Which of the following statements is correct for a circular singly linked list with only a start pointer?
  (a) Both insertion and deletion at the front end take O(1) time
  (b) Only insertion at the front end takes O(1) time
  (c) Only deletion from the front end takes O(1) time
  (d) No insertion or deletion operation at either end is possible in O(1) time
  ```
- **Audit Verdict:** **PASS — Intact & Complete**.

---

### Question 8: Recursive Linked List Traversal C Function (Code Preserved)
- **Question Instance ID:** `DOC-28-P02-MCQ-Q08`
- **Physical Page:** Page 2
- **Wording State:** `STATE B — RECONSTRUCTED`
- **Source Visual Required:** `true`
- **Source Visual Page:** `2`
- **Source Visual Region:** `Page 2 Rect(128.88, 161.76, 278.16, 252.12) embedded C code image xref 22`
- **Source Visual Reason:** `C code snippet for recursive linked list traversal void fun(struct node* start)`
- **Reconstruction Method:** Visual layout reassembly from rendered source page 2 preserving C code block from image xref 22 and reassembling fragmented options.
- **Visual Source Reference:** `SOURCE/DSA-20260930T180448Z-1-001/DSA/DSA Practice Assignment.pdf Page 2`
- **Reconstruction Confidence:** `HIGH`
- **Reconstructed Question Text:**
  ```text
  What is the output of following function for start pointing to first node of the following linked list: 1->2->3->4->5->6?
  void fun(struct node* start)
  {
      if(start == NULL)
          return;
      printf("%d ", start->data);
      if(start->next != NULL )
          fun(start->next->next);
      printf("%d ", start->data);
  }
  (a) 1 4 6 6 4 1
  (b) 1 3 5 1 3 5
  (c) 1 2 3 5
  (d) 1 3 5 5 3 1
  ```
- **Audit Verdict:** **PASS — Essential C code snippet fully preserved and visual source provenance linked**.

---

### Question 9: BFS Traversal Order on Graph (Graph Preserved)
- **Question Instance ID:** `DOC-28-P02-MCQ-Q09`
- **Physical Page:** Page 2
- **Wording State:** `STATE B — RECONSTRUCTED`
- **Source Visual Required:** `true`
- **Source Visual Page:** `2`
- **Source Visual Region:** `Page 2 y=336-398 vector graph diagram region`
- **Source Visual Reason:** `Undirected graph diagram with 6 vertices {M, N, O, P, Q, R} required to trace BFS visiting orders`
- **Reconstruction Method:** Visual layout reassembly from rendered source page 2 linking referenced graph diagram and reassembling options.
- **Visual Source Reference:** `SOURCE/DSA-20260930T180448Z-1-001/DSA/DSA Practice Assignment.pdf Page 2`
- **Reconstruction Confidence:** `HIGH`
- **Reconstructed Question Text:**
  ```text
  The Breadth First Search algorithm has been implemented using the queue data structure. One possible order of visiting the nodes of the following graph is
  [Graph with 6 nodes {M, N, O, R, Q, P} and edges (M,N), (N,O), (M,R), (M,Q), (N,Q), (O,P), (Q,P)]
  (a) MNOPQR
  (b) NQMPOR
  (c) QMNPRO
  (d) QMNPOR
  ```
- **Audit Verdict:** **PASS — Graph reference explicitly captured with visual metadata**.

---

### Question 10: Binary Tree Post-Order Traversal (Tree Diagram Preserved)
- **Question Instance ID:** `DOC-28-P02-MCQ-Q10`
- **Physical Page:** Page 2
- **Wording State:** `STATE B — RECONSTRUCTED`
- **Source Visual Required:** `true`
- **Source Visual Page:** `2`
- **Source Visual Region:** `Page 2 Rect(196.56, 490.32, 238.32, 614.76) embedded binary tree diagram xref 24`
- **Source Visual Reason:** `Binary tree diagram required to determine post-order traversal sequence`
- **Reconstruction Method:** Visual layout reassembly from rendered source page 2 linking embedded tree diagram xref 24 and reassembling options.
- **Visual Source Reference:** `SOURCE/DSA-20260930T180448Z-1-001/DSA/DSA Practice Assignment.pdf Page 2`
- **Reconstruction Confidence:** `HIGH`
- **Reconstructed Question Text:**
  ```text
  What will be the post order traversal of the given tree?
  [Tree with root 1, right child 2, right child 5, children 3 and 6, child 4]
  (a) 1, 2, 3, 4, 5, 6
  (b) 5, 3, 4, 6, 2, 1
  (c) 4, 3, 6, 5, 2, 1
  (d) 3, 4, 6, 5, 2, 1
  ```
- **Audit Verdict:** **PASS — Tree diagram linked with image xref 24 bounding box**.

---

### Question 11: 1D Array Optimum Space Complexity Tree (Pure Content — Fixed)
- **Question Instance ID:** `DOC-28-P02-MCQ-Q11`
- **Physical Page:** Page 2
- **Wording State:** `STATE B — RECONSTRUCTED`
- **Source Visual Required:** `false`
- **Reconstruction Method:** Visual layout reassembly from rendered source page 2 to resolve three-column layout fragmentation at page bottom; completely purged of cross-question contamination from Q7/Q8.
- **Visual Source Reference:** `SOURCE/DSA-20260930T180448Z-1-001/DSA/DSA Practice Assignment.pdf Page 2`
- **Reconstruction Confidence:** `HIGH`
- **Reconstructed Question Text:**
  ```text
  Which of the following tree can always be stored with optimum space complexity, using a 1D array?
  (a) Full Binary Tree
  (b) Almost complete Binary Tree
  (c) Binary Search Tree
  ```
- **Contamination Check:**
  - `singly linked list` in text: **FALSE (0 occurrences)**
  - `start pointer` in text: **FALSE (0 occurrences)**
  - `front end` in text: **FALSE (0 occurrences)**
- **Audit Verdict:** **PASS — Completely clean, zero cross-question fragment contamination**.

---

### Question 12: Complete Undirected Graph Edges (Page 3 Verbatim Source)
- **Question Instance ID:** `DOC-28-P03-MCQ-Q12`
- **Physical Page:** **Page 3** (Confirmed via `doc[2].get_text()`, absolute character index 2684)
- **Wording State:** `STATE A — EXACT` (Not State B)
- **Reconstruction Metadata:** `null`
- **Source Visual Required:** `false`
- **Question Text (Verbatim Extraction):**
  ```text
  The number of edges in a complete undirected graph with n vertices is (a) n(n-l) (b) n(n-l)/2 (c) n2 (d) 2n-1
  ```
- **Audit Verdict:** **PASS — Resides on Page 3, intact verbatim extraction, correct STATE A classification**.

---

## 3. Comparison Matrix: Prior vs Corrected State

| Question | Prior Page | Prior State | Prior Contamination / Flaw | Corrected Page | Corrected State | Corrected Integrity Status |
| :---: | :---: | :---: | :--- | :---: | :---: | :--- |
| **Q7** | Page 1 *(erroneous)* | STATE B | Truncated options, misassigned to Page 1 | **Page 2** | **STATE B** | Fully intact text & options reassembled |
| **Q8** | Page 2 | STATE B | Missing C code block | **Page 2** | **STATE B** | Embedded C code snippet preserved; xref 22 |
| **Q9** | Page 2 | STATE B | Unreferenced graph | **Page 2** | **STATE B** | BFS graph diagram region preserved |
| **Q10** | Page 2 | STATE B | Unreferenced tree | **Page 2** | **STATE B** | Tree diagram preserved; xref 24 |
| **Q11** | Page 2 | STATE B | Contaminated with Q7/Q8 fragments | **Page 2** | **STATE B** | Purged; contains ONLY genuine Q11 content |
| **Q12** | Page 2 *(erroneous)* | STATE B *(erroneous)* | Misattributed to P2 and labeled State B | **Page 3** | **STATE A** | Verbatim text extraction from Page 3 |

---

## 4. Release Certification

All 6 items (Questions 7 through 12) have been physically verified against the rendered PDF source and automated rule validation (Rules 13, 14, 15, 20, 21). 

**DOC-28 Page 2 Release Gate Status:** **PASSED**.
