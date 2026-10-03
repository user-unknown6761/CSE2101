/**
 * CSE2101 DSA Exam Preparation System - Mock Exam & Timed Practice Module
 */

window.MockModule = {
  activeSession: null,
  timerInterval: null,
  timeRemainingSec: 45 * 60, // 45 minutes default
  isTimerRunning: false,

  init() {
    this.renderInitial();
  },

  renderInitial() {
    const container = document.getElementById('mock-content-container');
    if (!container || !window.App.data.questions) return;

    if (this.activeSession) {
      this.renderActiveExam(container);
      return;
    }

    const sources = window.App.data.sources || [];

    let html = `
      <div class="card" style="background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.8)); margin-bottom: 2rem;">
        <h3 style="font-size: 1.25rem; font-weight: 800; color: var(--accent-cyan); margin-bottom: 0.5rem;">
          Configure Your Practice Session
        </h3>
        <p style="font-size: 0.92rem; color: var(--text-secondary); max-width: 800px; line-height: 1.6;">
          Test your exam readiness under authentic timed conditions. All practice questions originate from real past-year examinations. Zero fabricated questions.
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem; margin-top: 1.5rem;">
          <!-- Option A: Mixed Syllabus Set -->
          <div class="card" style="margin-bottom: 0; background: var(--bg-secondary); border: 1px solid var(--border-card);">
            <div style="font-size: 0.8rem; font-weight: 700; color: var(--accent-emerald); text-transform: uppercase;">
              RECOMMENDED PRACTICE
            </div>
            <h4 style="font-size: 1.1rem; font-weight: 700; margin: 0.4rem 0;">10-Question In-Scope Mixed Set</h4>
            <p style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 1rem;">
              Balanced examination paper: 3 Module 1 questions, 4 Module 2 questions, 3 Module 4 questions drawn directly from verified historical occurrences.
            </p>
            <button class="btn-reveal" onclick="window.MockModule.startMixedExam(45)" style="background: var(--accent-cyan); color: #030712; font-weight: 700; border: none; width: 100%;">
              Start 45-Min Mixed Practice →
            </button>
          </div>

          <!-- Option B: Full Historical Paper -->
          <div class="card" style="margin-bottom: 0; background: var(--bg-secondary); border: 1px solid var(--border-card);">
            <div style="font-size: 0.8rem; font-weight: 700; color: var(--accent-blue); text-transform: uppercase;">
              HISTORICAL SIMULATION
            </div>
            <h4 style="font-size: 1.1rem; font-weight: 700; margin: 0.4rem 0;">Attempt Full Historical Paper</h4>
            <p style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 0.5rem;">
              Select any past year exam and solve all in-scope questions in exam sequence.
            </p>
            <select id="mock-paper-picker" style="width: 100%; padding: 0.45rem; background: var(--bg-primary); border: 1px solid var(--border-subtle); color: var(--text-primary); border-radius: var(--radius-sm); margin-bottom: 1rem;">
              ${sources.map(s => `
                <option value="${s.document_id}">
                  ${s.document_id}: ${s.filename.replace('.pdf', '').replace(/_/g, ' ')} (${s.in_scope_count} in-scope Qs)
                </option>
              `).join('')}
            </select>
            <button class="btn-reveal" onclick="window.MockModule.startPaperExam(60)" style="background: var(--bg-tertiary); color: var(--text-primary); width: 100%; font-weight: 600;">
              Start Timed Paper Simulation →
            </button>
          </div>
        </div>
      </div>
    `;

    container.innerHTML = html;
  },

  // Start a source-derived mixed mock exam
  startMixedExam(minutes = 45) {
    const inScope = (window.App.data.questions || []).filter(q => q.scope_status === 'IN_SCOPE');
    
    // Group by module
    const m1 = inScope.filter(q => q.topic_id && q.topic_id.startsWith('M1_'));
    const m2 = inScope.filter(q => q.topic_id && q.topic_id.startsWith('M2_'));
    const m4 = inScope.filter(q => q.topic_id && q.topic_id.startsWith('M4_'));

    // Deterministic selection using diverse index spacing
    const selectSpaced = (arr, count) => {
      if (arr.length <= count) return [...arr];
      const step = Math.floor(arr.length / count);
      const res = [];
      for (let i = 0; i < count; i++) {
        res.push(arr[(i * step + 7) % arr.length]);
      }
      return res;
    };

    const selected = [
      ...selectSpaced(m1, 3),
      ...selectSpaced(m2, 4),
      ...selectSpaced(m4, 3)
    ];

    this.activeSession = {
      title: '10-Question Balanced Examination Practice',
      totalTimeSec: minutes * 60,
      questions: selected,
      userAnswers: {},
      isSubmitted: false
    };

    this.timeRemainingSec = minutes * 60;
    this.startTimer();
    this.renderActiveExam();
  },

  // Start paper-based mock exam
  startPaperExam(minutes = 60) {
    const picker = document.getElementById('mock-paper-picker');
    const docId = picker ? picker.value : 'DOC-01';
    const questions = (window.App.data.questions || []).filter(q => q.document_id === docId && q.scope_status === 'IN_SCOPE');

    if (!questions.length) {
      alert('Selected paper has no in-scope questions.');
      return;
    }

    const src = (window.App.data.sources || []).find(s => s.document_id === docId);

    this.activeSession = {
      title: `Paper Simulation: ${docId} (${questions.length} In-Scope Questions)`,
      totalTimeSec: minutes * 60,
      questions: questions,
      userAnswers: {},
      isSubmitted: false
    };

    this.timeRemainingSec = minutes * 60;
    this.startTimer();
    this.renderActiveExam();
  },

  startTimer() {
    this.isTimerRunning = true;
    clearInterval(this.timerInterval);
    this.updateTimerDisplay();

    this.timerInterval = setInterval(() => {
      if (this.timeRemainingSec > 0 && !this.activeSession.isSubmitted) {
        this.timeRemainingSec--;
        this.updateTimerDisplay();
      } else {
        clearInterval(this.timerInterval);
        this.isTimerRunning = false;
        if (!this.activeSession.isSubmitted) {
          alert('Time is up! Submitting your answers for verification.');
          this.submitExam();
        }
      }
    }, 1000);
  },

  updateTimerDisplay() {
    const display = document.getElementById('mock-timer-display');
    if (!display) return;
    const mins = Math.floor(this.timeRemainingSec / 60);
    const secs = this.timeRemainingSec % 60;
    display.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
  },

  renderActiveExam(targetContainer = null) {
    const container = targetContainer || document.getElementById('mock-content-container');
    if (!container || !this.activeSession) return;

    const session = this.activeSession;
    const solutions = window.App.data.solutions.solutions_by_id || {};

    let html = '';

    // Status bar
    html += `
      <div class="card" style="margin-bottom: 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
        <div>
          <div style="font-size: 0.8rem; font-weight: 700; color: var(--accent-cyan); text-transform: uppercase;">
            ACTIVE EXAMINATION SESSION
          </div>
          <h3 style="font-size: 1.25rem; font-weight: 800; color: var(--text-primary); margin-top: 0.2rem;">
            ${window.App.escapeHtml(session.title)}
          </h3>
          <div style="font-size: 0.85rem; color: var(--text-muted);">
            ${session.questions.length} Questions • Solutions ${session.isSubmitted ? 'REVEALED' : 'HIDDEN'}
          </div>
        </div>

        <div style="display: flex; gap: 0.75rem;">
          ${!session.isSubmitted ? `
            <button class="btn-reveal" onclick="window.MockModule.submitExam()" style="background: var(--accent-emerald); color: #030712; font-weight: 700; border: none; padding: 0.6rem 1.5rem;">
              Submit & Verify Answers ✓
            </button>
          ` : `
            <button class="btn-reveal" onclick="window.MockModule.exitSession()" style="background: var(--bg-tertiary); color: var(--text-primary);">
              Exit Session ✕
            </button>
          `}
        </div>
      </div>
    `;

    // Questions List
    session.questions.forEach((q, idx) => {
      const qId = q.question_instance_id;
      const userText = session.userAnswers[qId] || '';
      const sol = solutions[qId];

      html += `
        <div class="card" style="margin-bottom: 1.5rem; border-left: 4px solid var(--accent-cyan);">
          <div class="card-header">
            <div style="display: flex; gap: 0.5rem; align-items: center; flex-wrap: wrap;">
              <span style="font-size: 1.05rem; font-weight: 800; color: var(--accent-cyan);">
                Question ${idx + 1}
              </span>
              <span class="badge" style="background: var(--bg-tertiary); color: var(--text-muted); font-family: var(--font-mono); font-size: 0.72rem;">
                ${qId}
              </span>
              <span class="badge badge-module">
                ${q.topic_id ? q.topic_id.split('_')[0].replace('M', 'MODULE ') : 'DSA'}
              </span>
              ${q.marks ? `<span class="badge" style="background: rgba(251, 191, 36, 0.1); color: #fbbf24; border: 1px solid rgba(251, 191, 36, 0.25);">⭐ ${q.marks} Marks</span>` : ''}
            </div>

            <span style="font-size: 0.75rem; color: var(--text-muted);">
              ${window.App.escapeHtml(q.source_file ? q.source_file.split('/').pop() : q.document_id)}
            </span>
          </div>

          <!-- Question Body -->
          <div style="font-size: 1rem; color: var(--text-primary); line-height: 1.6; margin: 0.75rem 0;">
            ${window.App.formatMath(window.App.escapeHtml(q.raw_text))}
          </div>

          <!-- Student Workspace -->
          <div style="margin: 1rem 0;">
            <label style="font-size: 0.75rem; font-weight: 700; color: var(--text-muted); display: block; margin-bottom: 0.25rem;">
              YOUR ANSWER / REASONING OUTLINE:
            </label>
            <textarea 
              id="mock-ans-${qId}" 
              ${session.isSubmitted ? 'readonly' : ''} 
              oninput="window.MockModule.recordAnswer('${qId}', this.value)" 
              placeholder="Type your exam points, step-by-step trace, or algorithm outline here..." 
              style="width: 100%; min-height: 90px; padding: 0.65rem; background: var(--bg-primary); border: 1px solid var(--border-subtle); color: var(--text-primary); border-radius: var(--radius-sm); font-family: var(--font-mono); font-size: 0.85rem; resize: vertical;">${window.App.escapeHtml(userText)}</textarea>
          </div>

          <!-- Revealed Solution (Only after submit) -->
          ${session.isSubmitted && sol ? `
            <div style="margin-top: 1.25rem; padding-top: 1rem; border-top: 1px solid var(--border-subtle);">
              <div class="callout-box tip" style="margin-bottom: 1rem;">
                <div class="callout-title">Verified Solution Summary</div>
                <div style="font-size: 0.92rem; color: var(--text-primary);">
                  ${window.App.formatMath(window.App.escapeHtml(sol.direct_answer))}
                </div>
              </div>

              <div class="callout-box exam-rule">
                <div class="callout-title" style="color: var(--accent-purple);">✍️ EXAM-READY ANSWER TEMPLATE</div>
                <div style="font-size: 0.9rem; color: var(--text-primary); white-space: pre-line; line-height: 1.6; margin-top: 0.4rem;">
                  ${window.App.formatMath(window.App.escapeHtml(sol.exam_ready_answer))}
                </div>
              </div>

              <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1rem; flex-wrap: wrap; gap: 0.5rem;">
                <button class="btn-reveal" onclick="window.App.openModal('${qId}')" style="background: var(--bg-tertiary); color: var(--accent-cyan);">
                  View Full Deep Solution & Diagrams →
                </button>

                <div style="font-size: 0.8rem; color: var(--text-muted);">
                  Topic: <a href="#" onclick="window.App.activeTopicId='${sol.topic_id}'; window.App.switchTab('study'); return false;" style="color: var(--accent-cyan); text-decoration: underline;">
                    ${sol.topic_id}
                  </a>
                </div>
              </div>
            </div>
          ` : ''}
        </div>
      `;
    });

    container.innerHTML = html;
  },

  recordAnswer(qId, val) {
    if (this.activeSession) {
      this.activeSession.userAnswers[qId] = val;
    }
  },

  submitExam() {
    if (!this.activeSession) return;
    this.activeSession.isSubmitted = true;
    clearInterval(this.timerInterval);
    this.isTimerRunning = false;
    this.renderActiveExam();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  },

  exitSession() {
    if (confirm('Exit practice session and return to configuration?')) {
      clearInterval(this.timerInterval);
      this.activeSession = null;
      this.timeRemainingSec = 45 * 60;
      this.updateTimerDisplay();
      this.renderInitial();
    }
  }
};
