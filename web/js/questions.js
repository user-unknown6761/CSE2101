/**
 * CSE2101 DSA Exam Preparation System - Question Library Module
 */

window.QuestionsModule = {
  currentPage: 1,
  pageSize: 40,
  filteredQuestions: [],

  init() {
    this.bindFilters();
  },

  bindFilters() {
    const moduleSelect = document.getElementById('filter-module');
    const scopeSelect = document.getElementById('filter-scope');
    const tierSelect = document.getElementById('filter-tier');
    const searchInput = document.getElementById('filter-search');

    const triggerRender = () => {
      this.currentPage = 1;
      this.renderQuestions();
    };

    if (moduleSelect) moduleSelect.addEventListener('change', triggerRender);
    if (scopeSelect) scopeSelect.addEventListener('change', triggerRender);
    if (tierSelect) tierSelect.addEventListener('change', triggerRender);
    if (searchInput) searchInput.addEventListener('input', triggerRender);
  },

  renderQuestions() {
    const container = document.getElementById('questions-list-container');
    if (!container || !window.App.data.questions) return;

    const allQuestions = window.App.data.questions;
    const solutions = window.App.data.solutions.solutions_by_id || {};
    const families = window.App.data.families.families_by_id || {};

    // Get Filter Values
    const modVal = document.getElementById('filter-module') ? document.getElementById('filter-module').value : 'ALL';
    const scopeVal = document.getElementById('filter-scope') ? document.getElementById('filter-scope').value : 'IN_SCOPE';
    const tierVal = document.getElementById('filter-tier') ? document.getElementById('filter-tier').value : 'ALL';
    const searchVal = document.getElementById('filter-search') ? document.getElementById('filter-search').value.trim().toLowerCase() : '';

    // Filter Logic
    this.filteredQuestions = allQuestions.filter(q => {
      // 1. Scope filter
      if (scopeVal !== 'ALL' && q.scope_status !== scopeVal) {
        return false;
      }

      // 2. Module filter
      if (modVal !== 'ALL') {
        if (!q.topic_id) {
          if (q.scope_status === 'IN_SCOPE') return false;
        } else {
          const qMod = q.topic_id.split('_')[0].replace('M1', 'MODULE_1').replace('M2', 'MODULE_2').replace('M4', 'MODULE_4');
          if (qMod !== modVal) return false;
        }
      }

      // 3. Recurrence Tier filter
      if (tierVal !== 'ALL') {
        const sol = solutions[q.question_instance_id];
        if (!sol || !sol.family_id) return false;
        const fam = families[sol.family_id];
        if (!fam) return false;
        const count = fam.occurrence_count || 1;
        let tier = 'SPORADIC';
        if (count >= 15) tier = 'HIGH';
        else if (count >= 5) tier = 'MODERATE';
        if (tier !== tierVal) return false;
      }

      // 4. Search Filter
      if (searchVal) {
        const text = (q.raw_text || '').toLowerCase();
        const qid = (q.question_instance_id || '').toLowerCase();
        const doc = (q.document_id || '').toLowerCase();
        const top = (q.topic_id || '').toLowerCase();
        const reason = (q.classification_reason || '').toLowerCase();
        
        let famMatch = false;
        const sol = solutions[q.question_instance_id];
        if (sol && sol.family_id) {
          famMatch = sol.family_id.toLowerCase().includes(searchVal) || (sol.family_title || '').toLowerCase().includes(searchVal);
        }

        if (!text.includes(searchVal) && !qid.includes(searchVal) && !doc.includes(searchVal) && !top.includes(searchVal) && !reason.includes(searchVal) && !famMatch) {
          return false;
        }
      }

      return true;
    });

    // Accounting summary
    const inScopeCount = allQuestions.filter(q => q.scope_status === 'IN_SCOPE').length;
    const outOfScopeCount = allQuestions.filter(q => q.scope_status === 'OUT_OF_SCOPE').length;
    const ambiguousCount = allQuestions.filter(q => q.scope_status === 'AMBIGUOUS').length;

    let html = `
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; font-size: 0.88rem; color: var(--text-secondary); flex-wrap: wrap; gap: 0.5rem;">
        <div>
          Showing <strong>${Math.min(this.currentPage * this.pageSize, this.filteredQuestions.length)}</strong> of <strong>${this.filteredQuestions.length}</strong> matching questions (from 1,260 total corpus occurrences)
        </div>
        <div style="font-size: 0.8rem; color: var(--text-muted);">
          Total: ${allQuestions.length} = ${inScopeCount} In Scope + ${outOfScopeCount} Out of Scope + ${ambiguousCount} Ambiguous
        </div>
      </div>
    `;

    if (this.filteredQuestions.length === 0) {
      html += `
        <div class="card" style="text-align: center; padding: 3rem; color: var(--text-muted);">
          <h3>No questions matched your active filters</h3>
          <p style="margin-top: 0.5rem;">Try broadening your search or resetting scope/module filters.</p>
        </div>
      `;
      container.innerHTML = html;
      return;
    }

    // Render Paginated Slice
    const displayItems = this.filteredQuestions.slice(0, this.currentPage * this.pageSize);

    displayItems.forEach(q => {
      const sol = solutions[q.question_instance_id];
      const fam = sol && sol.family_id ? families[sol.family_id] : null;

      let tierBadge = '';
      if (fam) {
        const count = fam.occurrence_count || 1;
        if (count >= 15) {
          tierBadge = `<span class="badge badge-tier-high" title="${count} occurrences across papers">🔥 High Recurrence (${count})</span>`;
        } else if (count >= 5) {
          tierBadge = `<span class="badge badge-tier-moderate" title="${count} occurrences across papers">⚡ Moderate Recurrence (${count})</span>`;
        } else {
          tierBadge = `<span class="badge badge-tier-sporadic" title="${count} occurrences">Sporadic (${count})</span>`;
        }
      }

      html += `
        <div class="card" style="margin-bottom: 1rem; border-left: 4px solid ${q.scope_status === 'IN_SCOPE' ? 'var(--accent-cyan)' : (q.scope_status === 'AMBIGUOUS' ? 'var(--text-warning)' : 'var(--text-danger)')};">
          <div class="card-header">
            <div style="display: flex; gap: 0.4rem; align-items: center; flex-wrap: wrap;">
              <span class="badge" style="background: var(--bg-tertiary); color: var(--text-primary); font-family: var(--font-mono); font-size: 0.75rem;">
                ${q.question_instance_id}
              </span>
              <span class="badge" style="background: var(--bg-secondary); color: var(--text-secondary); border: 1px solid var(--border-subtle);">
                ${window.App.escapeHtml(q.source_file ? q.source_file.split('/').pop() : q.document_id)}
              </span>
              <span class="badge" style="background: var(--bg-secondary); color: var(--text-muted);">
                Page ${q.page} • Q${window.App.escapeHtml(q.official_question_number || '')}${q.sub_question_id ? '(' + q.sub_question_id + ')' : ''}
              </span>
              ${q.marks ? `<span class="badge" style="background: rgba(251, 191, 36, 0.1); color: #fbbf24; border: 1px solid rgba(251, 191, 36, 0.25);">⭐ ${q.marks} Marks</span>` : ''}
            </div>

            <div style="display: flex; gap: 0.4rem; align-items: center; flex-wrap: wrap;">
              ${tierBadge}
              <span class="badge ${q.scope_status === 'IN_SCOPE' ? 'badge-in-scope' : (q.scope_status === 'AMBIGUOUS' ? 'badge-ambiguous' : 'badge-out-of-scope')}">
                ${q.scope_status === 'IN_SCOPE' ? '✓ IN SCOPE' : (q.scope_status === 'AMBIGUOUS' ? '? AMBIGUOUS' : '✕ OUT OF SCOPE')}
              </span>
            </div>
          </div>

          <!-- Question Text -->
          <div style="font-size: 0.95rem; font-weight: 500; color: var(--text-primary); line-height: 1.5; margin: 0.5rem 0;">
            ${window.App.formatMath(window.App.escapeHtml(q.raw_text))}
          </div>

          <!-- Family / Scope Reason Footer -->
          <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 0.75rem; padding-top: 0.5rem; border-top: 1px solid var(--border-subtle); flex-wrap: wrap; gap: 0.5rem;">
            ${q.scope_status === 'IN_SCOPE' && fam ? `
              <div style="font-size: 0.78rem; color: var(--text-muted);">
                Family: <strong style="color: var(--text-secondary);">${window.App.escapeHtml(fam.title || fam.canonical_family_id)}</strong>
              </div>
            ` : (q.scope_status === 'AMBIGUOUS' ? `
              <div style="font-size: 0.78rem; color: var(--text-warning);">
                Ambiguous: Isolated token <code>"else"</code> in DOC-19
              </div>
            ` : `
              <div style="font-size: 0.78rem; color: var(--text-danger);">
                Excluded: ${window.App.escapeHtml(q.classification_reason || 'Out of locked syllabus scope')}
              </div>
            `)}

            ${q.scope_status === 'IN_SCOPE' ? `
              <button class="btn-reveal" onclick="window.App.openModal('${q.question_instance_id}')" style="background: var(--bg-tertiary); color: var(--accent-cyan); border-color: rgba(56, 189, 248, 0.3);">
                Inspect Solution & Exam Answer →
              </button>
            ` : `
              <span style="font-size: 0.75rem; color: var(--text-muted);">Not examinable</span>
            `}
          </div>
        </div>
      `;
    });

    // Load More Button
    if (displayItems.length < this.filteredQuestions.length) {
      html += `
        <div style="text-align: center; margin: 2rem 0;">
          <button class="btn-reveal" id="btn-load-more-q" style="padding: 0.75rem 2rem; font-size: 0.9rem; background: var(--bg-tertiary); color: var(--text-primary);">
            Load More Questions (${this.filteredQuestions.length - displayItems.length} remaining) ↓
          </button>
        </div>
      `;
    }

    container.innerHTML = html;

    // Attach Load More Listener
    const loadMoreBtn = document.getElementById('btn-load-more-q');
    if (loadMoreBtn) {
      loadMoreBtn.addEventListener('click', () => {
        this.currentPage++;
        this.renderQuestions();
      });
    }
  }
};
