/**
 * CSE2101 DSA Exam Preparation System - Master Syllabus Progress Module
 */

window.ProgressModule = {
  init() {
    this.renderMasterTree();
  },

  renderMasterTree() {
    const container = document.getElementById('progress-tree-container');
    if (!container || !window.App.data.topics) return;

    const topics = window.App.data.topics;
    const progress = window.App.progress || {};

    // Group by Module -> Section
    const modules = {};
    topics.forEach(t => {
      if (!modules[t.module_id]) {
        modules[t.module_id] = {
          number: t.module_number,
          title: `Module ${t.module_number}`,
          sections: {}
        };
      }
      if (!modules[t.module_id].sections[t.section_id]) {
        modules[t.module_id].sections[t.section_id] = {
          title: t.section_title,
          topics: []
        };
      }
      modules[t.module_id].sections[t.section_id].topics.push(t);
    });

    let html = '';

    // Unmastered Concepts Callout (Alert for Exam Eve)
    const unmastered = topics.filter(t => (progress[t.topic_id] || 'NOT_STARTED') !== 'MASTERED');
    if (unmastered.length > 0) {
      html += `
        <div class="card" style="border-left: 4px solid var(--accent-amber); margin-bottom: 2rem;">
          <div style="font-size: 0.8rem; font-weight: 700; color: var(--accent-amber); text-transform: uppercase;">
            ⚠️ HIGH-PRIORITY EXAM-EVE CHECKLIST
          </div>
          <h3 style="font-size: 1.15rem; font-weight: 700; color: var(--text-primary); margin: 0.25rem 0;">
            ${unmastered.length} Topics Still Require Final Revision / Mastery
          </h3>
          <p style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 0.75rem;">
            Click on any topic below to jump directly to its textbook chapter, formulas, and verified questions:
          </p>
          <div style="display: flex; gap: 0.4rem; flex-wrap: wrap;">
            ${unmastered.slice(0, 10).map(t => `
              <button class="btn-reveal" onclick="window.App.activeTopicId='${t.topic_id}'; window.App.switchTab('study');" style="background: var(--bg-tertiary); color: var(--text-primary); font-size: 0.78rem;">
                ${window.App.escapeHtml(t.topic_title)} →
              </button>
            `).join('')}
            ${unmastered.length > 10 ? `
              <span style="font-size: 0.8rem; color: var(--text-muted); align-self: center;">
                + ${unmastered.length - 10} more below
              </span>
            ` : ''}
          </div>
        </div>
      `;
    }

    // Module Trees
    Object.keys(modules).sort().forEach(modId => {
      const mod = modules[modId];
      const allModTopics = [];
      Object.values(mod.sections).forEach(s => allModTopics.push(...s.topics));
      const modMastered = allModTopics.filter(t => (progress[t.topic_id] || 'NOT_STARTED') === 'MASTERED').length;
      const modPct = Math.round((modMastered / allModTopics.length) * 100);

      html += `
        <div class="card" style="margin-bottom: 2rem;">
          <div class="card-header">
            <div>
              <div style="font-size: 0.8rem; font-weight: 700; color: var(--accent-cyan); text-transform: uppercase;">
                ${mod.title} • ${mod.number === 4 ? '14 LECTURE HOURS' : '10 LECTURE HOURS'}
              </div>
              <h3 style="font-size: 1.3rem; font-weight: 800; color: var(--text-primary); margin-top: 0.2rem;">
                ${modId.replace('_', ' ')}
              </h3>
            </div>

            <div style="text-align: right;">
              <span style="font-size: 1.1rem; font-weight: 800; color: var(--accent-cyan);">${modPct}%</span>
              <div style="font-size: 0.75rem; color: var(--text-muted);">${modMastered} / ${allModTopics.length} Mastered</div>
            </div>
          </div>

          <div class="progress-bar-container" style="margin-bottom: 1.5rem;">
            <div class="progress-bar-fill" style="width: ${modPct}%;"></div>
          </div>
      `;

      Object.keys(mod.sections).forEach(secId => {
        const sec = mod.sections[secId];
        html += `
          <div style="margin-bottom: 1.5rem;">
            <h4 style="font-size: 0.92rem; font-weight: 700; color: var(--text-secondary); text-transform: uppercase; margin-bottom: 0.75rem; padding-bottom: 0.25rem; border-bottom: 1px solid var(--border-subtle);">
              ${sec.title}
            </h4>
            <div style="display: grid; gap: 0.75rem;">
        `;

        sec.topics.forEach(t => {
          const currentStatus = progress[t.topic_id] || 'NOT_STARTED';
          const isNoEvidence = t.evidence_status === 'NO_SUPPLIED_QUESTION_EVIDENCE';

          html += `
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.65rem 0.85rem; background: var(--bg-secondary); border-radius: var(--radius-sm); border: 1px solid var(--border-subtle); flex-wrap: wrap; gap: 0.5rem;">
              <div style="flex: 1; min-width: 250px;">
                <a href="#" onclick="window.App.activeTopicId='${t.topic_id}'; window.App.switchTab('study'); return false;" style="font-weight: 600; color: var(--text-primary); text-decoration: none; font-size: 0.92rem;">
                  ${window.App.escapeHtml(t.topic_title)}
                </a>
                <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 0.15rem;">
                  <code>${t.topic_id}</code> • ${isNoEvidence ? '<span style="color: #fbbf24;">Syllabus topic — no supplied question evidence</span>' : window.App.escapeHtml(t.evidence_label)}
                </div>
              </div>

              <!-- Status Radio Group -->
              <div class="status-pill-group">
                ${['NOT_STARTED', 'LEARNING', 'PRACTICE', 'REVISED', 'MASTERED'].map(st => `
                  <button 
                    class="status-pill ${currentStatus === st ? 'active' : ''}" 
                    onclick="window.App.updateProgress('${t.topic_id}', '${st}')"
                    style="font-size: 0.7rem; padding: 0.2rem 0.5rem;">
                    ${st.replace('_', ' ')}
                  </button>
                `).join('')}
              </div>
            </div>
          `;
        });

        html += `</div></div>`;
      });

      html += `</div>`;
    });

    container.innerHTML = html;
  }
};
