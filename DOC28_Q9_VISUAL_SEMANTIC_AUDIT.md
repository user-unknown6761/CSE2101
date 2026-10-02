# CSE2101 — DOC-28 Question 9 Visual Semantic Audit & Forensic Verification
**Document ID:** `DOC-28` (`SOURCE/DSA-20260930T180448Z-1-001/DSA/DSA Practice Assignment.pdf`)  
**Question Instance ID:** `DOC-28-P02-MCQ-Q09`  
**Source Page:** Page 2 (0-indexed page 1, physical page 2 of 14)  
**Rendered Artifacts:**  
- Full Page 2: `rendered_pages/DOC-28_page_2.png`  
- High-Resolution Crop (600 DPI): `rendered_pages/DOC-28_Q9_graph_600dpi.png`  
- Region Zoom (300 DPI): `rendered_pages/DOC-28_Q9_zoom.png`  
**Audit Date:** 2026-10-02  
**Audit Standard:** Prompt 1.3 Forensic Visual Re-audit Requirement  
**Final Status:** **VERIFIED (CORRECTED SOURCE FAITHFUL)**

---

## 1. Executive Summary & Prior Defect Identification

In Phase 1.1 and Phase 1.2, Question 9 was reconstructed from Page 2 using an incorrect vertex label:
- **Prior Incorrect Reconstruction:** The bottom-left vertex was identified as `R`, yielding node set `{M, N, O, R, Q, P}` and edge `(M, R)`.
- **Authoritative Physical Source Visual:** Physical inspection of the rendered source page at 600 DPI proves that the bottom-left vertex in the diagram circle is labeled **`K`**, not `R`.
- **Root Cause of Prior Defect:** The MCQ answer options printed below the diagram list strings containing the letter `R` (e.g., `(a) MNOPQR`, `(b) NQMPOR`, `(c) QMNPRO`, `(d) QMNPOR`). The previous parser/reconstruction conflated the textual options with the diagram content, erroneously inferring that the diagram must contain `R`.
- **Governance Mandate:** The source visual is authoritative. Academic or typographical inconsistencies in source documents must be recorded verbatim and explicitly audited, never silently altered or synthesized.

---

## 2. Comprehensive Forensic Visual Analysis of the Source Graph

### 2.1 Graph Layout & Topology
The visual diagram is located on Page 2 in the vertical span $y \in [300, 450]$ pt. It consists of six circular vertex nodes arranged in two distinct horizontal tiers, embedded as an undirected planar graph:

```text
       [ M ] ────────────── [ N ] ────────────── [ O ]
      /      \             /                    /
     /        \           /                    /
    /          \         /                    /
[ K ]           \       /                    /
                 \     /                    /
                  [ Q ] ────────────────── [ P ]
```

### 2.2 Exact Vertex Labels (6 Nodes)
| Node Position | Source Circle Label | Node Degree | Adjacency List (Neighbors) | Visual Coordinates on Page 2 |
| :--- | :---: | :---: | :--- | :--- |
| **Top Left** | **`M`** | 3 | `{K, N, Q}` | Upper horizontal rail, left |
| **Top Center** | **`N`** | 3 | `{M, Q, O}` | Upper horizontal rail, center |
| **Top Right** | **`O`** | 2 | `{N, P}` | Upper horizontal rail, right |
| **Bottom Left** | **`K`** | 1 | `{M}` | Lower level, far left (leaf node) |
| **Bottom Center** | **`Q`** | 3 | `{M, N, P}` | Lower horizontal rail, center |
| **Bottom Right** | **`P`** | 2 | `{Q, O}` | Lower horizontal rail, right |

- **Total Vertices:** 6 (`{K, M, N, O, P, Q}`)
- **Vertex Count Verification:** Exactly 6 circular nodes rendered on page.

### 2.3 Exact Graph Edges (7 Undirected Edges)
Careful inspection of line paths connecting the node boundaries reveals exactly 7 undirected edges:
1. **Edge `(M, K)`:** Extends diagonally downwards to the left from node `M` to node `K`. (Only connection to node `K`; node `K` has degree 1).
2. **Edge `(M, N)`:** Extends horizontally from node `M` to node `N`.
3. **Edge `(M, Q)`:** Extends diagonally downwards to the right from node `M` to node `Q`.
4. **Edge `(N, O)`:** Extends horizontally from node `N` to node `O`.
5. **Edge `(N, Q)`:** Extends diagonally downwards to the left from node `N` to node `Q`.
6. **Edge `(Q, P)`:** Extends horizontally from node `Q` to node `P`.
7. **Edge `(P, O)`:** Extends diagonally upwards to the right from node `P` to node `O`.

- **Total Edges:** 7
- **Handshaking Lemma Verification:**
  $$\sum \text{deg}(v) = \text{deg}(K) + \text{deg}(M) + \text{deg}(N) + \text{deg}(Q) + \text{deg}(P) + \text{deg}(O) = 1 + 3 + 3 + 3 + 2 + 2 = 14 = 2 \times 7$$
- **Edge Crossings:** Exactly 0. Edges `(M, Q)` and `(N, Q)` terminate at common vertex `Q` and do not intersect other edges. The graph is planar.
- **Graph Connectivity:** The graph comprises a single connected component.

---

## 3. Printed Source Text & Options Reconciliation

### 3.1 Question Stem (Verbatim Source)
```text
9. The Breadth First Search algorithm has been implemented using the queue data structure. One possible order of visiting the nodes of the following graph is
```

### 3.2 Printed Multiple-Choice Options (Verbatim Source)
```text
(a) MNOPQR
(b) NQMPOR
(c) QMNPRO
(d) QMNPOR
```

### 3.3 Institutional Inconsistency Audit
- **Observation:** All four printed MCQ options contain the character `R` as the terminal or sixth node.
- **Physical Reality:** The diagram node is visibly and unequivocally labeled `K`.
- **Audit Decision:**
  1. The reconstructed text strictly reflects the physical visual graph: `[Graph with 6 nodes {M, N, O, K, Q, P} and 7 edges (M,K), (M,N), (M,Q), (N,O), (N,Q), (Q,P), (P,O)]`.
  2. The options text strictly preserves the physical source print: `(a) MNOPQR`, `(b) NQMPOR`, `(c) QMNPRO`, `(d) QMNPOR`.
  3. No artificial mutation of the source options (e.g. changing `R` to `K` in the options) is permitted, as that would alter source evidence.
  4. The discrepancy is explicitly cataloged as an institutional document defect in the damage and audit registries.

---

## 4. Reconstructed Representation Comparison & Verification

| Element | Phase 1.2 Representation | Phase 1.3 Corrected Representation | Source Visual Truth | Match Result |
| :--- | :--- | :--- | :--- | :---: |
| **Node Set** | `{M, N, O, R, Q, P}` | **`{M, N, O, K, Q, P}`** | `{M, N, O, K, Q, P}` | **MATCH** |
| **Bottom-Left Node** | `R` *(ERRONEOUS)* | **`K`** | **`K`** | **MATCH** |
| **Edges Set** | `(M,N), (N,O), (M,R), (M,Q), (N,Q), (O,P), (Q,P)` | **`(M,K), (M,N), (M,Q), (N,O), (N,Q), (Q,P), (P,O)`** | 7 physical line strokes | **MATCH** |
| **Edge Count** | 7 | **7** | 7 | **MATCH** |
| **Planar Embedding** | Preserved | **Preserved (0 crossings)** | 0 crossings | **MATCH** |
| **Question Stem** | BFS queue order | **BFS queue order (verbatim)** | Verbatim digital text | **MATCH** |
| **MCQ Options** | (a) to (d) | **(a) to (d) (verbatim)** | Verbatim digital text | **MATCH** |
| **Confidence** | HIGH *(unwarranted)* | **HIGH (Evidenced by 600 DPI render)** | Rendered artifact verified | **VERIFIED** |

---

## 5. Verification Metadata Payload

The following structured semantic verification payload is embedded into `RAW_EXTRACTED_QUESTIONS.json` under `DOC-28-P02-MCQ-Q09`:

```json
{
  "visual_semantic_verification": {
    "status": "VERIFIED",
    "verification_basis": "Rendered source-page inspection at 600 DPI (rendered_pages/DOC-28_Q9_graph_600dpi.png)",
    "source_page": 2,
    "source_region": "DOC-28 Page 2, middle visual container (y ≈ 300 to 450 pt)",
    "elements_checked": [
      "vertex_labels",
      "edges",
      "graph_connectivity",
      "planar_layout",
      "question_stem",
      "mcq_options"
    ],
    "element_level_findings": [
      {
        "element": "vertex_labels",
        "source": "6 circular nodes: {M, N, O, K, Q, P} (top row M, N, O; bottom row K, Q, P)",
        "reconstructed": "6 nodes {M, N, O, K, Q, P}",
        "match": true
      },
      {
        "element": "edges",
        "source": "7 edges: (M,K), (M,N), (M,Q), (N,O), (N,Q), (Q,P), (P,O)",
        "reconstructed": "7 edges (M,K), (M,N), (M,Q), (N,O), (N,Q), (Q,P), (P,O)",
        "match": true
      },
      {
        "element": "graph_connectivity",
        "source": "Single connected component, degree sequence: K:1, M:3, N:3, Q:3, P:2, O:2",
        "reconstructed": "Single connected component with 7 edges",
        "match": true
      },
      {
        "element": "question_stem",
        "source": "The Breadth First Search algorithm has been implemented using the queue data structure. One possible order of visiting the nodes of the following graph is",
        "reconstructed": "The Breadth First Search algorithm has been implemented using the queue data structure. One possible order of visiting the nodes of the following graph is",
        "match": true
      },
      {
        "element": "mcq_options",
        "source": "(a) MNOPQR\n(b) NQMPOR\n(c) QMNPRO\n(d) QMNPOR",
        "reconstructed": "(a) MNOPQR\n(b) NQMPOR\n(c) QMNPRO\n(d) QMNPOR",
        "match": true
      }
    ],
    "verification_confidence": "HIGH"
  }
}
```

---

## 6. Certification Conclusion

The defect wherein vertex `R` was incorrectly stated in the visual reconstruction has been fully rectified. The reconstructed representation now perfectly matches the authoritative physical visual source (vertex `K`, 7 edges, complete planar topology).
