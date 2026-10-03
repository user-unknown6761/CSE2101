/**
 * CSE2101 DSA Exam Preparation System - Fast Revision Engine Module
 */

window.RevisionModule = {
  activeMode: '5min',

  init() {
    this.bindModeButtons();
  },

  bindModeButtons() {
    document.querySelectorAll('.status-pill[data-rev-mode]').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.status-pill[data-rev-mode]').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        this.activeMode = btn.getAttribute('data-rev-mode');
        this.renderActiveMode();
      });
    });
  },

  renderActiveMode() {
    const container = document.getElementById('revision-content-container');
    if (!container || !window.App.data.revision) return;

    if (this.activeMode === '5min') {
      this.render5Min(container);
    } else if (this.activeMode === '15min') {
      this.render15Min(container);
    } else if (this.activeMode === '30min') {
      this.render30Min(container);
    }
  },

  // 1. 5-Minute Final Look Before Exam Hall
  render5Min(container) {
    const rev = window.App.data.revision.five_minute_cram;
    if (!rev) return;

    let html = '';

    // Hero Callout
    html += `
      <div class="callout-box exam-rule" style="margin-top: 0; margin-bottom: 2rem;">
        <div class="callout-title" style="color: var(--accent-purple); font-size: 1rem;">
          ⚡ 5-MINUTE FINAL EXAM COUNTDOWN
        </div>
        <p style="font-size: 0.95rem; color: var(--text-primary); margin-top: 0.25rem;">
          Essential formulas, triggers, asymptotic bounds, and zero-mistake invariants to read right before walking into the examination hall.
        </p>
      </div>
    `;

    // Formulas Grid
    html += `
      <div style="margin-bottom: 2rem;">
        <h3 style="font-size: 1.15rem; font-weight: 700; color: var(--accent-cyan); margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;">
          <span>📐 Critical Formulas & Invariants</span>
        </h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1rem;">
          ${(rev.formulas || []).map(f => `
            <div class="card" style="margin-bottom: 0; background: #030712; border: 1px solid #1f2937;">
              <div style="font-size: 0.8rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase;">
                ${window.App.escapeHtml(f.name)}
              </div>
              <div style="font-family: var(--font-mono); font-size: 0.92rem; color: var(--accent-emerald); margin-top: 0.4rem; line-height: 1.5;">
                ${window.App.formatMath(window.App.escapeHtml(f.formula))}
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `;

    // Algorithm Complexity Matrix
    html += `
      <div style="margin-bottom: 2rem;">
        <h3 style="font-size: 1.15rem; font-weight: 700; color: var(--accent-cyan); margin-bottom: 1rem;">
          📊 Master Algorithm Complexity & Stability Matrix
        </h3>
        <div class="table-wrapper">
          <table class="custom-table">
            <thead>
              <tr>
                <th>Algorithm</th>
                <th>Best Case</th>
                <th>Worst Case</th>
                <th>Average Case</th>
                <th>Aux Space</th>
                <th>Stable?</th>
              </tr>
            </thead>
            <tbody>
              ${(rev.complexity_table || []).map(row => `
                <tr>
                  <td><strong>${window.App.escapeHtml(row.algorithm)}</strong></td>
                  <td style="font-family: var(--font-mono); color: var(--text-success);">${window.App.formatMath(row.best)}</td>
                  <td style="font-family: var(--font-mono); color: var(--text-danger);">${window.App.formatMath(row.worst)}</td>
                  <td style="font-family: var(--font-mono); color: var(--accent-cyan);">${window.App.formatMath(row.avg)}</td>
                  <td style="font-family: var(--font-mono);">${window.App.formatMath(row.space)}</td>
                  <td>${row.stable === 'Yes' ? '✅ Yes' : (row.stable === 'No' ? '❌ No' : '—')}</td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      </div>
    `;

    // Common Traps
    html += `
      <div>
        <h3 style="font-size: 1.15rem; font-weight: 700; color: var(--accent-amber); margin-bottom: 1rem;">
          ⚠️ 5 Critical Exam Traps Where Marks Are Lost
        </h3>
        <div style="display: grid; gap: 0.75rem;">
          ${(rev.common_traps || []).map((trap, idx) => `
            <div class="card" style="margin-bottom: 0; border-left: 4px solid var(--accent-amber); display: flex; gap: 0.75rem; align-items: flex-start;">
              <span style="background: rgba(251, 191, 36, 0.2); color: #fbbf24; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 800; flex-shrink: 0;">
                ${idx + 1}
              </span>
              <div style="font-size: 0.92rem; color: var(--text-primary); line-height: 1.5;">
                ${window.App.formatMath(window.App.escapeHtml(trap))}
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `;

    container.innerHTML = html;
  },

  // 2. 15-Minute Core Comparisons & Differences
  render15Min(container) {
    const comparisons = window.App.data.revision.fifteen_minute_review ? window.App.data.revision.fifteen_minute_review.comparisons : [];

    let html = `
      <div class="callout-box tip" style="margin-top: 0; margin-bottom: 2rem;">
        <div class="callout-title" style="color: var(--accent-emerald);">
          ⚖️ 15-MINUTE HIGH-PROBABILITY EXAM COMPARISONS
        </div>
        <p style="font-size: 0.92rem; color: var(--text-secondary);">
          Classical differences frequently tested across semester examinations. Tabulate these exact bullet points for maximum scoring.
        </p>
      </div>

      <div style="display: grid; gap: 1.5rem;">
        ${comparisons.map(comp => `
          <div class="card">
            <h3 style="font-size: 1.1rem; font-weight: 700; color: var(--accent-cyan); margin-bottom: 0.75rem; padding-bottom: 0.4rem; border-bottom: 1px solid var(--border-subtle);">
              ${window.App.escapeHtml(comp.topic)}
            </h3>
            <ul style="padding-left: 1.25rem; font-size: 0.92rem; color: var(--text-secondary); line-height: 1.7;">
              ${comp.points.map(pt => `
                <li>${window.App.formatMath(window.App.escapeHtml(pt))}</li>
              `).join('')}
            </ul>
          </div>
        `).join('')}
      </div>
    `;

    container.innerHTML = html;
  },

  // 3. 30-Minute High-Yield Families Review
  render30Min(container) {
    const families = window.App.data.families.question_families || [];
    // Sort by occurrence count descending
    const sortedFamilies = [...families].sort((a, b) => (b.occurrence_count || 0) - (a.occurrence_count || 0)).slice(0, 12);

    let html = `
      <div class="callout-box" style="margin-top: 0; margin-bottom: 2rem; border-left-color: var(--accent-indigo); background: rgba(129, 140, 248, 0.05);">
        <div class="callout-title" style="color: var(--accent-indigo);">
          🔥 30-MINUTE HIGH-RECURRENCE QUESTION FAMILIES
        </div>
        <p style="font-size: 0.92rem; color: var(--text-secondary);">
          These question concepts have appeared repeatedly across 15+ historical exam papers. Review their representative problem and exam answers.
        </p>
      </div>

      <div style="display: grid; gap: 1.25rem;">
        ${sortedFamilies.map((fam, idx) => {
          const rep = fam.canonical_representative || {};
          const qId = rep.question_instance_id;
          return `
            <div class="card" style="border-left: 4px solid var(--accent-cyan);">
              <div class="card-header">
                <div style="display: flex; gap: 0.5rem; align-items: center; flex-wrap: wrap;">
                  <span class="badge" style="background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3);">
                    Rank #${idx + 1} • ${fam.occurrence_count} Occurrences
                  </span>
                  <span class="badge badge-module">${window.App.escapeHtml(fam.module_id || '')}</span>
                  <span style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--text-muted);">${fam.canonical_family_id}</span>
                </div>

                ${qId ? `
                  <button class="btn-reveal" onclick="window.App.openModal('${qId}')" style="background: var(--accent-cyan); color: #030712; font-weight: 700; border: none;">
                    Inspect Master Solution →
                  </button>
                ` : ''}
              </div>

              <h4 style="font-size: 1.05rem; font-weight: 700; color: var(--text-primary); margin: 0.4rem 0;">
                ${window.App.escapeHtml(fam.title)}
              </h4>

              <div style="background: var(--bg-secondary); border-radius: var(--radius-sm); padding: 0.75rem 1rem; margin: 0.75rem 0; border: 1px solid var(--border-subtle); font-size: 0.92rem; color: var(--text-secondary); line-height: 1.5;">
                <div style="font-size: 0.72rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; margin-bottom: 0.2rem;">
                  Representative Historical Question:
                </div>
                "${window.App.formatMath(window.App.escapeHtml(rep.raw_text || ''))}"
              </div>

              <div style="display: flex; gap: 1rem; font-size: 0.8rem; color: var(--text-muted); flex-wrap: wrap;">
                <span>Distinct Papers: <strong>${(fam.observed_sources || []).length}</strong></span>
                <span>Exact Repeats: <strong>${fam.variant_breakdown ? fam.variant_breakdown.exact_or_near_duplicate || 0 : 0}</strong></span>
                <span>Wording Variants: <strong>${fam.variant_breakdown ? fam.variant_breakdown.wording_variant || 0 : 0}</strong></span>
              </div>
            </div>
          `;
        }).join('')}
      </div>
    `;

    container.innerHTML = html;
  }
};
