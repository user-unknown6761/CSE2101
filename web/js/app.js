/**
 * CSE2101 DSA Exam Preparation System - Core Application State & Controller
 */

window.App = {
  data: {
    syllabus: null,
    topics: [],
    families: {},
    solutions: {},
    sources: [],
    questions: [],
    revision: {}
  },
  
  progress: {},
  activeTab: 'study',
  activeTopicId: 'M1_INTRO_NEED',
  
  // Initialize Application
  async init() {
    try {
      this.initTheme();
      this.loadProgress();
      await this.loadAllData();
      this.bindEvents();
      this.updateProgressBadges();
      
      // Initialize sub-modules
      if (window.StudyModule) window.StudyModule.init();
      if (window.QuestionsModule) window.QuestionsModule.init();
      if (window.PyqModule) window.PyqModule.init();
      if (window.RevisionModule) window.RevisionModule.init();
      if (window.MockModule) window.MockModule.init();
      if (window.ProgressModule) window.ProgressModule.init();
      
      // Default to study tab
      this.switchTab('study');
    } catch (err) {
      console.error('Initialization error:', err);
      const container = document.getElementById('study-topic-container');
      if (container) {
        container.innerHTML = `
          <div class="card" style="border-color: var(--text-danger); margin: 2rem;">
            <h3 style="color: var(--text-danger);">Error Loading Application Data</h3>
            <p style="margin-top: 0.5rem; color: var(--text-secondary);">${this.escapeHtml(err.message)}</p>
            <p style="margin-top: 0.5rem; font-size: 0.85rem;">Please ensure you are viewing this via a local web server (e.g. <code>python -m http.server</code>) so JSON assets can be loaded.</p>
          </div>
        `;
      }
    }
  },

  // Load all 7 structured JSON datasets in parallel
  async loadAllData() {
    const fetchJson = async (path) => {
      const res = await fetch(path);
      if (!res.ok) throw new Error(`HTTP ${res.status} fetching ${path}`);
      return await res.json();
    };

    const [syllabus, topics, families, solutions, sources, questions, revision] = await Promise.all([
      fetchJson('data/syllabus.json'),
      fetchJson('data/topics.json'),
      fetchJson('data/question-families.json'),
      fetchJson('data/solutions.json'),
      fetchJson('data/sources.json'),
      fetchJson('data/questions.json'),
      fetchJson('data/revision.json')
    ]);

    this.data.syllabus = syllabus;
    this.data.topics = topics;
    this.data.families = families;
    this.data.solutions = solutions;
    this.data.sources = sources;
    this.data.questions = questions;
    this.data.revision = revision;

    // Update counters in header
    const qCountBadge = document.getElementById('badge-question-count');
    if (qCountBadge) {
      const inScopeCount = questions.filter(q => q.scope_status === 'IN_SCOPE').length;
      qCountBadge.textContent = inScopeCount;
    }

    const pyqBadge = document.getElementById('badge-pyq-count');
    if (pyqBadge && sources.length) {
      pyqBadge.textContent = sources.length;
    }
  },

  // Theme Management
  initTheme() {
    const savedTheme = localStorage.getItem('cse2101_theme') || 'dark';
    document.documentElement.setAttribute('data-theme', savedTheme);
    const themeIcon = document.getElementById('theme-icon');
    if (themeIcon) {
      themeIcon.textContent = savedTheme === 'dark' ? '🌙' : '☀️';
    }
  },

  toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('cse2101_theme', next);
    const themeIcon = document.getElementById('theme-icon');
    if (themeIcon) {
      themeIcon.textContent = next === 'dark' ? '🌙' : '☀️';
    }
  },

  // Progress Management (localStorage)
  loadProgress() {
    try {
      const saved = localStorage.getItem('cse2101_progress');
      if (saved) {
        this.progress = JSON.parse(saved);
      } else {
        this.progress = {};
      }
    } catch (e) {
      this.progress = {};
    }
  },

  updateProgress(topicId, status) {
    this.progress[topicId] = status;
    localStorage.setItem('cse2101_progress', JSON.stringify(this.progress));
    this.updateProgressBadges();
    
    // Dispatch update to active components
    if (window.ProgressModule) window.ProgressModule.renderMasterTree();
    if (window.StudyModule) window.StudyModule.updateTopicStatusPills();
  },

  resetProgress() {
    if (confirm('Are you sure you want to reset all syllabus topic progress?')) {
      this.progress = {};
      localStorage.removeItem('cse2101_progress');
      this.updateProgressBadges();
      if (window.ProgressModule) window.ProgressModule.renderMasterTree();
      if (window.StudyModule) window.StudyModule.renderSidebarTree();
    }
  },

  updateProgressBadges() {
    const totalTopics = this.data.topics && this.data.topics.length ? this.data.topics.length : 31;
    let masteredCount = 0;
    Object.values(this.progress).forEach(st => {
      if (st === 'MASTERED') masteredCount++;
    });

    const pct = Math.round((masteredCount / totalTopics) * 100);
    const badge = document.getElementById('badge-progress-pct');
    if (badge) badge.textContent = `${pct}%`;

    const masterBar = document.getElementById('progress-bar-master');
    if (masterBar) masterBar.style.width = `${pct}%`;

    const label = document.getElementById('progress-percent-label');
    if (label) label.textContent = `${pct}% Complete (${masteredCount} / ${totalTopics} Topics Mastered)`;
  },

  // Navigation & Tab Switching
  switchTab(tabName) {
    this.activeTab = tabName;

    // Update active nav-link
    document.querySelectorAll('.nav-link').forEach(link => {
      if (link.getAttribute('data-tab') === tabName) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });

    // Update view panels
    document.querySelectorAll('.view-panel').forEach(panel => {
      if (panel.id === `panel-${tabName}`) {
        panel.classList.add('active');
      } else {
        panel.classList.remove('active');
      }
    });

    // Sidebar visibility toggle
    const sidebar = document.getElementById('app-sidebar');
    const studySidebar = document.getElementById('sidebar-study-content');
    if (tabName === 'study') {
      if (sidebar) sidebar.style.display = 'block';
      if (studySidebar) studySidebar.style.display = 'block';
    } else {
      if (studySidebar) studySidebar.style.display = 'none';
      if (sidebar) sidebar.style.display = 'none';
    }

    // Trigger tab-specific activation
    if (tabName === 'study' && window.StudyModule) {
      window.StudyModule.renderCurrentTopic();
    } else if (tabName === 'questions' && window.QuestionsModule) {
      window.QuestionsModule.renderQuestions();
    } else if (tabName === 'pyq' && window.PyqModule) {
      window.PyqModule.renderPaper();
    } else if (tabName === 'revision' && window.RevisionModule) {
      window.RevisionModule.renderActiveMode();
    } else if (tabName === 'mock' && window.MockModule) {
      window.MockModule.renderInitial();
    } else if (tabName === 'progress' && window.ProgressModule) {
      window.ProgressModule.renderMasterTree();
    }

    // Scroll to top of viewport
    window.scrollTo({ top: 0, behavior: 'smooth' });
  },

  // Modal Solution Viewer
  openModal(questionInstanceId) {
    const q = this.data.questions.find(item => item.question_instance_id === questionInstanceId);
    const sol = this.data.solutions.solutions_by_id ? this.data.solutions.solutions_by_id[questionInstanceId] : null;

    if (!q) {
      console.warn('Question not found:', questionInstanceId);
      return;
    }

    const modal = document.getElementById('solution-modal');
    const moduleBadge = document.getElementById('modal-q-module');
    const idBadge = document.getElementById('modal-q-id');
    const body = document.getElementById('modal-body-content');

    const modName = q.topic_id ? q.topic_id.split('_')[0].replace('M', 'MODULE ') : 'MODULE ?';
    if (moduleBadge) moduleBadge.textContent = modName;
    if (idBadge) idBadge.textContent = q.question_instance_id;

    let contentHtml = '';

    // Header info: Source, Page, Official No, Marks
    contentHtml += `
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1rem; align-items: center;">
        <span class="badge" style="background: var(--bg-tertiary); color: var(--text-primary); border: 1px solid var(--border-subtle);">
          📄 ${this.escapeHtml(q.source_file ? q.source_file.split('/').pop() : q.document_id)}
        </span>
        <span class="badge" style="background: var(--bg-tertiary); color: var(--text-secondary);">
          Page ${q.page} • Q${this.escapeHtml(q.official_question_number || '')}${q.sub_question_id ? '(' + q.sub_question_id + ')' : ''}
        </span>
        <span class="badge" style="background: rgba(251, 191, 36, 0.15); color: #fbbf24; border: 1px solid rgba(251, 191, 36, 0.3);">
          ⭐ ${q.marks ? q.marks + ' Marks' : 'Mark not recorded'}
        </span>
        <span class="badge ${q.scope_status === 'IN_SCOPE' ? 'badge-in-scope' : 'badge-out-of-scope'}">
          ${q.scope_status === 'IN_SCOPE' ? '✓ IN SCOPE' : '✕ OUT OF SCOPE'}
        </span>
      </div>
    `;

    // Question Text Card
    contentHtml += `
      <div class="card" style="background: var(--bg-primary); border-left: 4px solid var(--accent-cyan); margin-bottom: 1.25rem;">
        <div style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted); margin-bottom: 0.35rem;">
          Official Source Question
        </div>
        <div style="font-size: 1.05rem; font-weight: 600; color: var(--text-primary); line-height: 1.5;">
          ${this.formatMath(this.escapeHtml(q.raw_text))}
        </div>
      </div>
    `;

    // If Out of Scope or Ambiguous
    if (q.scope_status !== 'IN_SCOPE') {
      contentHtml += `
        <div class="callout-box warning">
          <div class="callout-title">Scope Notice</div>
          <p style="font-size: 0.9rem; color: var(--text-secondary);">
            ${this.escapeHtml(q.classification_reason || 'This topic is excluded from the controlling CSE2101 syllabus.')}
          </p>
        </div>
      `;
    }

    // Complete Solution (if In Scope)
    if (sol) {
      // Direct Answer Summary
      contentHtml += `
        <div class="callout-box tip">
          <div class="callout-title">Direct Answer Key</div>
          <div style="font-size: 0.95rem; font-weight: 600; color: var(--text-primary);">
            ${this.formatMath(this.escapeHtml(sol.direct_answer))}
          </div>
        </div>
      `;

      // Exam Ready Answer (Directly Writable in Exam)
      contentHtml += `
        <div class="callout-box exam-rule" style="background: rgba(192, 132, 252, 0.08);">
          <div class="callout-title" style="color: var(--accent-purple);">✍️ EXAM-READY ANSWER (Directly Writable in Exam)</div>
          <div style="font-size: 0.92rem; color: var(--text-primary); white-space: pre-line; line-height: 1.6; margin-top: 0.5rem;">
            ${this.formatMath(this.escapeHtml(sol.exam_ready_answer))}
          </div>
        </div>
      `;

      // Step by Step Explanation
      contentHtml += `
        <div style="margin: 1.25rem 0;">
          <h4 style="font-size: 0.95rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.5rem;">
            Detailed Step-by-Step Explanation
          </h4>
          <div style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6; white-space: pre-line;">
            ${this.formatMath(this.escapeHtml(sol.step_by_step_explanation))}
          </div>
        </div>
      `;

      // Diagram if present
      if (sol.diagram_svg) {
        contentHtml += `
          <div style="margin: 1.25rem 0;">
            <h4 style="font-size: 0.95rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.5rem;">
              Illustrative Diagram
            </h4>
            <div class="diagram-container">
              ${sol.diagram_svg}
            </div>
          </div>
        `;
      }

      // Time & Space Complexity
      contentHtml += `
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1.25rem 0;">
          <div class="card" style="margin-bottom: 0; background: var(--bg-tertiary);">
            <div style="font-size: 0.75rem; font-weight: 700; color: var(--accent-cyan); text-transform: uppercase;">Time Complexity</div>
            <div style="font-family: var(--font-mono); font-size: 0.9rem; margin-top: 0.25rem;">
              ${this.escapeHtml(sol.time_complexity || 'O(1)')}
            </div>
          </div>
          <div class="card" style="margin-bottom: 0; background: var(--bg-tertiary);">
            <div style="font-size: 0.75rem; font-weight: 700; color: var(--accent-emerald); text-transform: uppercase;">Space Complexity</div>
            <div style="font-family: var(--font-mono); font-size: 0.9rem; margin-top: 0.25rem;">
              ${this.escapeHtml(sol.space_complexity || 'O(1)')}
            </div>
          </div>
        </div>
      `;

      // Common Mistakes & Beginner Notes
      if (sol.common_mistakes) {
        contentHtml += `
          <div class="callout-box warning">
            <div class="callout-title">⚠️ Common Mistakes to Avoid in Exam</div>
            <div style="font-size: 0.88rem; color: var(--text-secondary);">
              ${this.escapeHtml(sol.common_mistakes)}
            </div>
          </div>
        `;
      }

      if (sol.beginner_notes) {
        contentHtml += `
          <div style="font-size: 0.82rem; color: var(--text-muted); margin-top: 1rem; font-style: italic;">
            💡 Note: ${this.escapeHtml(sol.beginner_notes)}
          </div>
        `;
      }
    } else if (q.scope_status === 'IN_SCOPE') {
      contentHtml += `
        <div class="callout-box tip">
          <p>Solution record available in topic chapter.</p>
        </div>
      `;
    }

    if (body) body.innerHTML = contentHtml;
    if (modal) modal.classList.add('active');
  },

  closeModal() {
    const modal = document.getElementById('solution-modal');
    if (modal) modal.classList.remove('active');
  },

  // Event Listeners
  bindEvents() {
    // Navigation link clicks
    document.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        const tab = link.getAttribute('data-tab');
        if (tab) this.switchTab(tab);
      });
    });

    // Theme toggle
    const themeBtn = document.getElementById('btn-theme-toggle');
    if (themeBtn) {
      themeBtn.addEventListener('click', () => this.toggleTheme());
    }

    // Print button
    const printBtn = document.getElementById('btn-print');
    if (printBtn) {
      printBtn.addEventListener('click', () => window.print());
    }

    // Global Search Bar
    const searchInput = document.getElementById('global-search-input');
    if (searchInput) {
      searchInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          const query = searchInput.value.trim();
          if (query) {
            this.switchTab('questions');
            const qFilter = document.getElementById('filter-search');
            if (qFilter) {
              qFilter.value = query;
              if (window.QuestionsModule) window.QuestionsModule.renderQuestions();
            }
          }
        }
      });
    }

    // Modal Close button and backdrop click
    const modalClose = document.getElementById('btn-modal-close');
    if (modalClose) {
      modalClose.addEventListener('click', () => this.closeModal());
    }

    const modal = document.getElementById('solution-modal');
    if (modal) {
      modal.addEventListener('click', (e) => {
        if (e.target === modal) this.closeModal();
      });
    }

    // Escape key closes modal
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') this.closeModal();
    });

    // Reset progress button
    const resetBtn = document.getElementById('btn-reset-progress');
    if (resetBtn) {
      resetBtn.addEventListener('click', () => this.resetProgress());
    }
  },

  // Math and String Formatting Helpers
  formatMath(str) {
    if (!str) return '';
    return str
      .replace(/&gt;=/g, '≥')
      .replace(/&lt;=/g, '≤')
      .replace(/>=/g, '≥')
      .replace(/<=/g, '≤')
      .replace(/!=/g, '≠')
      .replace(/->/g, '→')
      .replace(/\(n\^2\)/g, '(n²)')
      .replace(/O\(n\^2\)/g, 'O(n²)')
      .replace(/O\(1\)/g, 'O(1)')
      .replace(/O\(n\)/g, 'O(n)')
      .replace(/O\(log n\)/g, 'O(log n)')
      .replace(/O\(n log n\)/g, 'O(n log n)')
      .replace(/2\^n/g, '2ⁿ');
  },

  escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }
};

// Auto start when DOM ready
document.addEventListener('DOMContentLoaded', () => {
  window.App.init();
});
