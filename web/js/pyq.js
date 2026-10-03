/**
 * CSE2101 DSA Exam Preparation System - Historical PYQ Explorer Module
 */

window.PyqModule = {
  currentDocId: 'DOC-01',

  init() {
    this.populatePaperSelector();
    this.bindEvents();
  },

  populatePaperSelector() {
    const select = document.getElementById('pyq-paper-select');
    if (!select || !window.App.data.sources) return;

    const sources = window.App.data.sources;
    let html = '';
    sources.forEach(src => {
      const cleanTitle = src.filename.replace('.pdf', '').replace(/_/g, ' ');
      html += `
        <option value="${src.document_id}" ${src.document_id === this.currentDocId ? 'selected' : ''}>
          ${src.document_id}: ${cleanTitle} (${src.in_scope_count} in-scope / ${src.total_questions} total)
        </option>
      `;
    });

    select.innerHTML = html;
  },

  bindEvents() {
    const select = document.getElementById('pyq-paper-select');
    if (select) {
      select.addEventListener('change', (e) => {
        this.currentDocId = e.target.value;
        this.renderPaper();
      });
    }
  },

  renderPaper() {
    const container = document.getElementById('pyq-content-container');
    if (!container || !window.App.data.sources || !window.App.data.questions) return;

    const sources = window.App.data.sources;
    const currentSource = sources.find(s => s.document_id === this.currentDocId) || sources[0];
    if (!currentSource) return;

    const questions = window.App.data.questions.filter(q => q.document_id === currentSource.document_id);
    const solutions = window.App.data.solutions.solutions_by_id || {};

    let html = '';

    // Paper Header Banner
    html += `
      <div class="card" style="background: linear-gradient(135deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.8)); border-left: 4px solid var(--accent-cyan); margin-bottom: 2rem;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1rem;">
          <div>
            <div style="font-size: 0.8rem; font-weight: 700; color: var(--accent-cyan); text-transform: uppercase;">
              ${currentSource.document_id} • OFFICIAL HISTORICAL EXAMINATION PAPER
            </div>
            <h2 style="font-size: 1.4rem; font-weight: 800; color: var(--text-primary); margin-top: 0.25rem;">
              ${window.App.escapeHtml(currentSource.filename.replace('.pdf', '').replace(/_/g, ' '))}
            </h2>
            <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.35rem;">
              Pages: ${currentSource.page_count} • Preserved Historical Exam Structure
            </div>
          </div>

          <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
            <span class="badge badge-in-scope" style="padding: 0.4rem 0.75rem; font-size: 0.8rem;">
              ✓ ${currentSource.in_scope_count} In Scope
            </span>
            <span class="badge badge-out-of-scope" style="padding: 0.4rem 0.75rem; font-size: 0.8rem;">
              ✕ ${currentSource.out_of_scope_count} Out of Scope (Module 3/Tree/Graph)
            </span>
            ${currentSource.ambiguous_count > 0 ? `
              <span class="badge badge-ambiguous" style="padding: 0.4rem 0.75rem; font-size: 0.8rem;">
                ? ${currentSource.ambiguous_count} Ambiguous
              </span>
            ` : ''}
          </div>
        </div>

        <div style="margin-top: 1rem; padding-top: 0.75rem; border-top: 1px solid var(--border-subtle); font-size: 0.82rem; color: var(--text-secondary);">
          ℹ️ <strong>Exam Policy Notice:</strong> Only questions classified as <strong>IN SCOPE</strong> belong to the controlling CSE2101 syllabus. Questions from Module 3 (Trees, Binary Trees, Graphs) are preserved for source fidelity but marked as non-examinable.
        </div>
      </div>
    `;

    // Group Questions by Page
    const pageMap = {};
    questions.forEach(q => {
      const p = q.page || 1;
      if (!pageMap[p]) pageMap[p] = [];
      pageMap[p].push(q);
    });

    Object.keys(pageMap).sort((a, b) => parseInt(a) - parseInt(b)).forEach(page => {
      const pageQuestions = pageMap[page];
      html += `
        <div style="margin-bottom: 2rem;">
          <div style="font-size: 0.85rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem;">
            <span>📄 Page ${page}</span>
            <span style="height: 1px; flex: 1; background: var(--border-subtle);"></span>
          </div>
      `;

      pageQuestions.forEach(q => {
        const sol = solutions[q.question_instance_id];
        const isInScope = q.scope_status === 'IN_SCOPE';

        html += `
          <div class="card" style="margin-bottom: 1rem; border-left: 4px solid ${isInScope ? 'var(--accent-cyan)' : 'var(--text-danger)'}; background: ${isInScope ? 'var(--bg-card)' : 'rgba(239, 68, 68, 0.03)'};">
            <div class="card-header">
              <div style="display: flex; gap: 0.5rem; align-items: center; flex-wrap: wrap;">
                <span style="font-weight: 800; font-size: 1.05rem; color: ${isInScope ? 'var(--accent-cyan)' : 'var(--text-secondary)'};">
                  Q${window.App.escapeHtml(q.official_question_number || '')}${q.sub_question_id ? '(' + q.sub_question_id + ')' : ''}
                </span>
                <span class="badge" style="background: var(--bg-tertiary); color: var(--text-muted); font-family: var(--font-mono); font-size: 0.72rem;">
                  ${q.question_instance_id}
                </span>
                ${q.marks ? `<span class="badge" style="background: rgba(251, 191, 36, 0.1); color: #fbbf24; border: 1px solid rgba(251, 191, 36, 0.25);">⭐ ${q.marks} Marks</span>` : ''}
              </div>

              <span class="badge ${isInScope ? 'badge-in-scope' : 'badge-out-of-scope'}">
                ${isInScope ? '✓ IN SCOPE' : '✕ OUT OF SCOPE'}
              </span>
            </div>

            <!-- Question Body -->
            <div style="font-size: 0.98rem; color: var(--text-primary); line-height: 1.6; margin: 0.5rem 0;">
              ${window.App.formatMath(window.App.escapeHtml(q.raw_text))}
            </div>

            <!-- Interactive Attempt & Solution Bar -->
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1rem; padding-top: 0.75rem; border-top: 1px solid var(--border-subtle); flex-wrap: wrap; gap: 0.5rem;">
              <div>
                ${!isInScope ? `
                  <span style="font-size: 0.8rem; color: var(--text-danger);">
                    ${window.App.escapeHtml(q.classification_reason || 'Out of syllabus scope (Module 3 Tree/Graph)')}
                  </span>
                ` : `
                  <button class="btn-reveal" onclick="window.PyqModule.toggleScratchpad('${q.question_instance_id}')" style="background: var(--bg-secondary); color: var(--text-secondary); margin-right: 0.5rem;">
                    📝 Toggle Practice Notes
                  </button>
                `}
              </div>

              ${isInScope ? `
                <button class="btn-reveal" onclick="window.App.openModal('${q.question_instance_id}')" style="background: var(--accent-cyan); color: #030712; font-weight: 700; border: none;">
                  Reveal Complete Solution & Exam Answer →
                </button>
              ` : `
                <span style="font-size: 0.75rem; color: var(--text-muted);">Excluded from exam</span>
              `}
            </div>

            <!-- Scratchpad Area -->
            <div id="scratchpad-${q.question_instance_id}" style="display: none; margin-top: 1rem; padding-top: 0.75rem; border-top: 1px dashed var(--border-subtle);">
              <label style="font-size: 0.75rem; font-weight: 700; color: var(--text-muted); display: block; margin-bottom: 0.25rem;">
                STUDENT PRACTICE SCRATCHPAD (Type your quick steps or outline):
              </label>
              <textarea placeholder="Write your exam outline or step-by-step reasoning here..." style="width: 100%; min-height: 80px; padding: 0.5rem; background: var(--bg-primary); border: 1px solid var(--border-subtle); color: var(--text-primary); border-radius: var(--radius-sm); font-family: var(--font-mono); font-size: 0.85rem; resize: vertical;"></textarea>
            </div>
          </div>
        `;
      });

      html += `</div>`;
    });

    container.innerHTML = html;
  },

  toggleScratchpad(id) {
    const pad = document.getElementById(`scratchpad-${id}`);
    if (pad) {
      pad.style.display = pad.style.display === 'none' ? 'block' : 'none';
    }
  }
};
