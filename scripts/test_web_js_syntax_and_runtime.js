const fs = require('fs');
const path = require('path');
const vm = require('vm');

console.log("=== Testing JavaScript Files Syntax and Client Simulation ===");

const jsFiles = [
  'app.js',
  'study.js',
  'questions.js',
  'pyq.js',
  'revision.js',
  'mock.js',
  'progress.js'
];

// Step 1: Syntax check all files
for (const file of jsFiles) {
  const filePath = path.join(__dirname, '..', 'web', 'js', file);
  const code = fs.readFileSync(filePath, 'utf8');
  try {
    new vm.Script(code, { filename: file });
    console.log(`  ✓ Syntax Valid: web/js/${file}`);
  } catch (err) {
    console.error(`  ✕ Syntax Error in web/js/${file}:`, err);
    process.exit(1);
  }
}

// Step 2: Create a simulated browser sandbox and execute
console.log("\n=== Simulating Client Execution ===");

// Load test data
const syllabus = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'web', 'data', 'syllabus.json'), 'utf8'));
const topics = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'web', 'data', 'topics.json'), 'utf8'));
const families = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'web', 'data', 'question-families.json'), 'utf8'));
const solutions = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'web', 'data', 'solutions.json'), 'utf8'));
const sources = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'web', 'data', 'sources.json'), 'utf8'));
const questions = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'web', 'data', 'questions.json'), 'utf8'));
const revision = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'web', 'data', 'revision.json'), 'utf8'));

// Mock DOM elements
function createMockElement(id = '', tag = 'div') {
  return {
    id,
    tagName: tag.toUpperCase(),
    classList: {
      _classes: new Set(),
      add(c) { this._classes.add(c); },
      remove(c) { this._classes.delete(c); },
      toggle(c) { 
        if (this._classes.has(c)) { this._classes.delete(c); return false; }
        else { this._classes.add(c); return true; }
      },
      has(c) { return this._classes.has(c); }
    },
    style: {},
    innerHTML: '',
    textContent: '',
    value: '',
    listeners: {},
    addEventListener(event, fn) {
      if (!this.listeners[event]) this.listeners[event] = [];
      this.listeners[event].push(fn);
    },
    querySelectorAll(sel) { return []; },
    querySelector(sel) { return null; },
    getAttribute(attr) { return this[attr] || null; },
    setAttribute(attr, val) { this[attr] = val; }
  };
}

const mockElements = {
  'study-topic-container': createMockElement('study-topic-container'),
  'syllabus-tree-container': createMockElement('syllabus-tree-container'),
  'badge-question-count': createMockElement('badge-question-count'),
  'badge-pyq-count': createMockElement('badge-pyq-count'),
  'badge-progress-pct': createMockElement('badge-progress-pct'),
  'progress-bar-master': createMockElement('progress-bar-master'),
  'progress-percent-label': createMockElement('progress-percent-label'),
  'app-sidebar': createMockElement('app-sidebar'),
  'sidebar-study-content': createMockElement('sidebar-study-content'),
  'theme-icon': createMockElement('theme-icon'),
  'solution-modal': createMockElement('solution-modal'),
  'modal-q-module': createMockElement('modal-q-module'),
  'modal-q-id': createMockElement('modal-q-id'),
  'modal-body-content': createMockElement('modal-body-content'),
  'filter-module': createMockElement('filter-module', 'select'),
  'filter-scope': createMockElement('filter-scope', 'select'),
  'filter-tier': createMockElement('filter-tier', 'select'),
  'filter-search': createMockElement('filter-search', 'input'),
  'questions-list-container': createMockElement('questions-list-container'),
  'pyq-paper-select': createMockElement('pyq-paper-select', 'select'),
  'pyq-content-container': createMockElement('pyq-content-container'),
  'revision-content-container': createMockElement('revision-content-container'),
  'mock-timer-display': createMockElement('mock-timer-display'),
  'mock-content-container': createMockElement('mock-content-container'),
  'progress-tree-container': createMockElement('progress-tree-container')
};

const mockLocalStorage = {
  store: {},
  getItem(k) { return this.store[k] || null; },
  setItem(k, v) { this.store[k] = String(v); },
  removeItem(k) { delete this.store[k]; }
};

const sandbox = {
  window: {},
  console: console,
  document: {
    documentElement: createMockElement('html'),
    getElementById(id) {
      if (!mockElements[id]) {
        mockElements[id] = createMockElement(id);
      }
      return mockElements[id];
    },
    querySelectorAll(sel) { return []; },
    querySelector(sel) { return null; },
    addEventListener(ev, fn) {}
  },
  localStorage: mockLocalStorage,
  fetch: async (url) => {
    if (url.includes('syllabus.json')) return { ok: true, json: async () => syllabus };
    if (url.includes('topics.json')) return { ok: true, json: async () => topics };
    if (url.includes('question-families.json')) return { ok: true, json: async () => families };
    if (url.includes('solutions.json')) return { ok: true, json: async () => solutions };
    if (url.includes('sources.json')) return { ok: true, json: async () => sources };
    if (url.includes('questions.json')) return { ok: true, json: async () => questions };
    if (url.includes('revision.json')) return { ok: true, json: async () => revision };
    throw new Error('Unknown URL: ' + url);
  },
  setTimeout: setTimeout,
  clearTimeout: clearTimeout,
  setInterval: setInterval,
  clearInterval: clearInterval,
  scrollTo: () => {}
};

sandbox.window = sandbox;

const context = vm.createContext(sandbox);

// Execute files in sandbox
for (const file of jsFiles) {
  const filePath = path.join(__dirname, '..', 'web', 'js', file);
  const code = fs.readFileSync(filePath, 'utf8');
  vm.runInContext(code, context, { filename: file });
  console.log(`  ✓ Loaded and evaluated: ${file}`);
}

// Now test App.init() in sandbox
(async () => {
  try {
    await sandbox.App.init();
    console.log("  ✓ App.init() succeeded");
    console.log(`    - Loaded ${sandbox.App.data.topics.length} topics`);
    console.log(`    - Loaded ${sandbox.App.data.questions.length} questions`);
    console.log(`    - Loaded ${sandbox.App.data.solutions.total_solutions} solutions`);
    console.log(`    - Loaded ${sandbox.App.data.families.total_families} question families`);

    // Test switching tabs
    sandbox.App.switchTab('questions');
    console.log("  ✓ Switched to Questions tab without error");

    sandbox.App.switchTab('pyq');
    console.log("  ✓ Switched to PYQ tab without error");

    sandbox.App.switchTab('revision');
    console.log("  ✓ Switched to Revision tab without error");

    sandbox.App.switchTab('mock');
    console.log("  ✓ Switched to Mock tab without error");

    sandbox.App.switchTab('progress');
    console.log("  ✓ Switched to Progress tab without error");

    sandbox.App.switchTab('study');
    console.log("  ✓ Switched back to Study tab without error");

    // Test opening modal on an in-scope question
    const firstInScope = sandbox.App.data.questions.find(q => q.scope_status === 'IN_SCOPE');
    sandbox.App.openModal(firstInScope.question_instance_id);
    console.log(`  ✓ Opened solution modal for ${firstInScope.question_instance_id}`);
    if (mockElements['modal-body-content'].innerHTML.length > 100) {
      console.log(`    - Modal body rendered ${mockElements['modal-body-content'].innerHTML.length} chars of verified solution HTML`);
    } else {
      throw new Error("Modal content was empty!");
    }
    sandbox.App.closeModal();
    console.log("  ✓ Closed solution modal");

    // Test Progress state update
    sandbox.App.updateProgress('M1_INTRO_NEED', 'MASTERED');
    const stored = JSON.parse(mockLocalStorage.getItem('cse2101_progress'));
    if (stored['M1_INTRO_NEED'] === 'MASTERED') {
      console.log("  ✓ LocalStorage progress persistence verified: M1_INTRO_NEED -> MASTERED");
    } else {
      throw new Error("Progress persistence failed!");
    }

    console.log("\nALL CLIENT-SIDE RUNTIME TESTS PASSED WITH ZERO ERRORS!");
  } catch (err) {
    console.error("  ✕ Runtime Error during client simulation:", err);
    process.exit(1);
  }
})();
