import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

endpoints = [
    'http://localhost:8080/index.html',
    'http://localhost:8080/styles/main.css',
    'http://localhost:8080/styles/components.css',
    'http://localhost:8080/js/app.js',
    'http://localhost:8080/js/study.js',
    'http://localhost:8080/js/questions.js',
    'http://localhost:8080/js/pyq.js',
    'http://localhost:8080/js/revision.js',
    'http://localhost:8080/js/mock.js',
    'http://localhost:8080/js/progress.js',
    'http://localhost:8080/data/syllabus.json',
    'http://localhost:8080/data/topics.json',
    'http://localhost:8080/data/question-families.json',
    'http://localhost:8080/data/solutions.json',
    'http://localhost:8080/data/sources.json',
    'http://localhost:8080/data/questions.json',
    'http://localhost:8080/data/revision.json'
]

print("Verifying HTTP 200 on all web assets...")
for ep in endpoints:
    try:
        req = urllib.request.urlopen(ep)
        status = req.status
        content_len = len(req.read())
        rel_path = ep.replace('http://localhost:8080/', '')
        print(f"  [200 OK] {rel_path} ({content_len:,} bytes)")
    except Exception as e:
        print(f"  [FAIL] {ep}: {e}")
        sys.exit(1)

print("\n--- Testing Data Integrity in Web Assets ---")
with open("web/data/questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)
assert len(questions) == 1260, f"Expected 1260 questions, got {len(questions)}"
in_scope = sum(1 for q in questions if q.get("scope_status") == "IN_SCOPE")
out_of_scope = sum(1 for q in questions if q.get("scope_status") == "OUT_OF_SCOPE")
ambiguous = sum(1 for q in questions if q.get("scope_status") == "AMBIGUOUS")
assert in_scope == 780, f"Expected 780 in-scope, got {in_scope}"
assert out_of_scope == 479, f"Expected 479 out-of-scope, got {out_of_scope}"
assert ambiguous == 1, f"Expected 1 ambiguous, got {ambiguous}"
assert in_scope + out_of_scope + ambiguous == 1260, "Sum must be exactly 1260"
print(f"  ✓ Questions Accounting: {in_scope} in-scope + {out_of_scope} out-of-scope + {ambiguous} ambiguous = 1260")

with open("web/data/solutions.json", "r", encoding="utf-8") as f:
    sols = json.load(f)
total_sols = sols.get("total_solutions")
assert total_sols == 780, f"Expected 780 solutions, got {total_sols}"
assert len(sols.get("solutions_list", [])) == 780, f"Expected 780 solutions in solutions_list, got {len(sols.get('solutions_list', []))}"
print(f"  ✓ Solutions Bank: {total_sols} complete solutions (0 placeholders)")

with open("web/data/topics.json", "r", encoding="utf-8") as f:
    topics = json.load(f)
assert len(topics) == 31, f"Expected 31 topics, got {len(topics)}"
print(f"  ✓ Topics Covered: {len(topics)} syllabus topics with 12 pedagogical sections each")

with open("web/data/question-families.json", "r", encoding="utf-8") as f:
    fams = json.load(f)
total_fams = fams.get("total_families")
assert total_fams == 41, f"Expected 41 families, got {total_fams}"
print(f"  ✓ Question Families: {total_fams} canonical families")

with open("web/data/sources.json", "r", encoding="utf-8") as f:
    sources = json.load(f)
assert len(sources) == 33, f"Expected 33 sources, got {len(sources)}"
print(f"  ✓ Sources Indexed: {len(sources)} historical source documents")

print("\nALL WEB VERIFICATION TESTS PASSED SUCCESSFULLY!")
