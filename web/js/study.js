/**
 * CSE2101 DSA Exam Preparation System - Study / Digital Textbook Module
 */

window.StudyModule = {
  init() {
    this.renderSidebarTree();
    this.renderCurrentTopic();
  },

  renderSidebarTree() {
    const container = document.getElementById('syllabus-tree-container');
    if (!container || !window.App.data.topics) return;

    const topics = window.App.data.topics;
    const progress = window.App.progress;

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
    const statusEmoji = {
      'NOT_STARTED': '⚪',
      'LEARNING': '🟡',
      'PRACTICE': '🔵',
      'REVISED': '🟢',
      'MASTERED': '🟣'
    };

    Object.keys(modules).sort().forEach(modId => {
      const mod = modules[modId];
      html += `
        <div style="margin-bottom: 1.25rem;">
          <div style="font-size: 0.82rem; font-weight: 800; color: var(--accent-cyan); text-transform: uppercase; margin-bottom: 0.4rem; padding-bottom: 0.25rem; border-bottom: 1px solid var(--border-subtle); display: flex; justify-content: space-between;">
            <span>${mod.title}</span>
            <span style="font-size: 0.72rem; color: var(--text-muted);">${mod.number === 4 ? '14L' : '10L'}</span>
          </div>
      `;

      Object.keys(mod.sections).forEach(secId => {
        const sec = mod.sections[secId];
        html += `
          <div style="margin-bottom: 0.6rem;">
            <div style="font-size: 0.74rem; font-weight: 700; color: var(--text-secondary); text-transform: uppercase; margin-bottom: 0.25rem; padding-left: 0.25rem;">
              ${sec.title}
            </div>
            <ul style="list-style: none; padding-left: 0.25rem;">
        `;

        sec.topics.forEach(t => {
          const isActive = t.topic_id === window.App.activeTopicId;
          const userStatus = progress[t.topic_id] || 'NOT_STARTED';
          const icon = statusEmoji[userStatus] || '⚪';
          const hasNoEvidence = t.evidence_status === 'NO_SUPPLIED_QUESTION_EVIDENCE';

          html += `
            <li style="margin-bottom: 0.2rem;">
              <a href="#" class="study-nav-item ${isActive ? 'active' : ''}" data-topic-id="${t.topic_id}" style="
                display: flex;
                align-items: center;
                gap: 0.45rem;
                padding: 0.35rem 0.5rem;
                border-radius: var(--radius-sm);
                font-size: 0.8rem;
                text-decoration: none;
                color: ${isActive ? 'var(--accent-cyan)' : 'var(--text-secondary)'};
                background: ${isActive ? 'var(--bg-accent)' : 'transparent'};
                border: 1px solid ${isActive ? 'rgba(56, 189, 248, 0.3)' : 'transparent'};
                transition: all var(--transition-fast);
              ">
                <span style="font-size: 0.75rem;">${icon}</span>
                <span style="flex: 1; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" title="${window.App.escapeHtml(t.topic_title)}">
                  ${window.App.escapeHtml(t.topic_title)}
                </span>
                ${hasNoEvidence ? '<span title="Syllabus topic — no supplied question evidence" style="font-size: 0.65rem; color: #fbbf24;">⚠️</span>' : ''}
              </a>
            </li>
          `;
        });

        html += `</ul></div>`;
      });

      html += `</div>`;
    });

    container.innerHTML = html;

    // Attach click listeners
    container.querySelectorAll('.study-nav-item').forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        const tid = link.getAttribute('data-topic-id');
        if (tid) {
          window.App.activeTopicId = tid;
          this.renderSidebarTree();
          this.renderCurrentTopic();
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      });
    });
  },

  renderCurrentTopic() {
    const container = document.getElementById('study-topic-container');
    if (!container || !window.App.data.topics) return;

    const topics = window.App.data.topics;
    const currentTopic = topics.find(t => t.topic_id === window.App.activeTopicId) || topics[0];
    if (!currentTopic) return;

    const progress = window.App.progress;
    const userStatus = progress[currentTopic.topic_id] || 'NOT_STARTED';

    // Find next / previous topic for navigation
    const currentIndex = topics.findIndex(t => t.topic_id === currentTopic.topic_id);
    const prevTopic = currentIndex > 0 ? topics[currentIndex - 1] : null;
    const nextTopic = currentIndex < topics.length - 1 ? topics[currentIndex + 1] : null;

    let html = '';

    // Hero Header
    const isNoEvidence = currentTopic.evidence_status === 'NO_SUPPLIED_QUESTION_EVIDENCE';
    html += `
      <div class="textbook-hero">
        <div class="hero-subtitle">
          MODULE ${currentTopic.module_number} • ${window.App.escapeHtml(currentTopic.section_title)}
        </div>
        <h1 class="hero-title">${window.App.escapeHtml(currentTopic.topic_title)}</h1>
        
        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; align-items: center; margin-bottom: 1.25rem;">
          <span class="badge badge-module">MODULE ${currentTopic.module_number}</span>
          ${isNoEvidence ? `
            <span class="badge" style="background: rgba(251, 191, 36, 0.15); color: #fbbf24; border: 1px solid rgba(251, 191, 36, 0.3);">
              ⚠️ Syllabus Topic — No Supplied Question Evidence
            </span>
          ` : `
            <span class="badge badge-in-scope">
              ✓ ${window.App.escapeHtml(currentTopic.evidence_label || 'Covered by Source Questions')}
            </span>
          `}
          ${currentTopic.topic_id === 'M4_SORT_QUICK' ? `
            <span class="badge" style="background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3);">
              Locked: Quick Sort complexity analysis is OUT OF SCOPE
            </span>
          ` : ''}
        </div>

        <!-- Mastery Selector -->
        <div style="display: flex; align-items: center; gap: 0.75rem; flex-wrap: wrap; background: rgba(0, 0, 0, 0.3); padding: 0.75rem 1rem; border-radius: var(--radius-sm); border: 1px solid var(--border-card);">
          <span style="font-size: 0.8rem; font-weight: 700; color: var(--text-secondary); text-transform: uppercase;">Topic Mastery:</span>
          <div class="status-pill-group" id="topic-status-group">
            ${['NOT_STARTED', 'LEARNING', 'PRACTICE', 'REVISED', 'MASTERED'].map(st => `
              <button class="status-pill ${userStatus === st ? 'active' : ''}" data-status="${st}">
                ${st.replace('_', ' ')}
              </button>
            `).join('')}
          </div>
        </div>
      </div>
    `;

    // 12 Structured Pedagogical Sections
    // Section 1: What it is
    html += `
      <section class="tb-section">
        <h2 class="tb-section-heading">
          <span class="num">1</span> What It Is
        </h2>
        <div class="card" style="font-size: 1.05rem; line-height: 1.7; color: var(--text-primary); border-left: 4px solid var(--accent-cyan);">
          ${window.App.formatMath(window.App.escapeHtml(currentTopic['1_what_it_is']))}
        </div>
      </section>
    `;

    // Section 2: Why it exists
    html += `
      <section class="tb-section">
        <h2 class="tb-section-heading">
          <span class="num">2</span> Why It Exists & Practical Necessity
        </h2>
        <div class="callout-box tip">
          <div class="callout-title">Core Purpose & Architectural Justification</div>
          <div style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6;">
            ${window.App.formatMath(window.App.escapeHtml(currentTopic['2_why_it_exists']))}
          </div>
        </div>
      </section>
    `;

    // Section 3: Core Terminology
    if (currentTopic['3_core_terminology'] && currentTopic['3_core_terminology'].length) {
      html += `
        <section class="tb-section">
          <h2 class="tb-section-heading">
            <span class="num">3</span> Core Terminology & Formal Definitions
          </h2>
          <div class="term-grid">
            ${currentTopic['3_core_terminology'].map(term => `
              <div class="term-card">
                <div class="term-name">${window.App.escapeHtml(term.term)}</div>
                <div class="term-def">${window.App.formatMath(window.App.escapeHtml(term.def))}</div>
              </div>
            `).join('')}
          </div>
        </section>
      `;
    }

    // Section 4: Core Idea & Intuition
    html += `
      <section class="tb-section">
        <h2 class="tb-section-heading">
          <span class="num">4</span> Core Idea & Intuition
        </h2>
        <div class="callout-box" style="border-left-color: var(--accent-indigo); background: rgba(129, 140, 248, 0.05);">
          <div class="callout-title" style="color: var(--accent-indigo);">💡 Conceptual Mental Model</div>
          <p style="font-size: 0.95rem; color: var(--text-primary); line-height: 1.6;">
            ${window.App.formatMath(window.App.escapeHtml(currentTopic['4_core_idea_and_intuition']))}
          </p>
        </div>
      </section>
    `;

    // Section 5: Important Representations
    html += `
      <section class="tb-section">
        <h2 class="tb-section-heading">
          <span class="num">5</span> Important Memory & Data Representations
        </h2>
        <div class="card" style="font-size: 0.92rem; line-height: 1.6; color: var(--text-secondary);">
          ${window.App.formatMath(window.App.escapeHtml(currentTopic['5_important_representations']))}
        </div>
      </section>
    `;

    // Section 6: Algorithm & Procedure
    html += `
      <section class="tb-section">
        <h2 class="tb-section-heading">
          <span class="num">6</span> Algorithm / Execution Procedure
        </h2>
        <div class="code-block">
          <div class="code-header">
            <span>PROCEDURAL STEP-BY-STEP ALGORITHM</span>
            <span>STANDARD PSEUDOCODE</span>
          </div>
          <pre style="margin: 0; font-family: inherit; font-size: inherit; white-space: pre-wrap;">${window.App.formatMath(window.App.escapeHtml(currentTopic['6_algorithm_procedure']))}</pre>
        </div>
      </section>
    `;

    // Section 7: Example using a Real Source Question
    if (currentTopic['7_example_with_source_question']) {
      const eg = currentTopic['7_example_with_source_question'];
      const qInstanceId = eg.question_instance_id;
      html += `
        <section class="tb-section">
          <h2 class="tb-section-heading">
            <span class="num">7</span> Worked Example from Real Source Paper
          </h2>
          <div class="card" style="border: 1px solid rgba(56, 189, 248, 0.4); background: rgba(15, 23, 42, 0.9);">
            <div class="card-header">
              <span class="badge badge-in-scope">SOURCE OCCURRENCE: ${window.App.escapeHtml(qInstanceId || 'SOURCE REF')}</span>
              <span style="font-size: 0.75rem; color: var(--text-muted);">${window.App.escapeHtml(eg.source_document || '')} Page ${eg.page || ''}</span>
            </div>
            <div style="font-size: 1rem; font-weight: 600; color: var(--text-primary); margin-bottom: 1rem; line-height: 1.5;">
              "${window.App.formatMath(window.App.escapeHtml(eg.question_text || ''))}"
            </div>
            ${qInstanceId ? `
              <button class="btn-reveal" onclick="window.App.openModal('${qInstanceId}')" style="background: var(--accent-cyan); color: #030712; font-weight: 700; border: none;">
                Inspect Complete Exam Solution →
              </button>
            ` : ''}
          </div>
        </section>
      `;
    }

    // Section 8: Formula / Rule / Invariant
    html += `
      <section class="tb-section">
        <h2 class="tb-section-heading">
          <span class="num">8</span> Formula / Invariant Rule
        </h2>
        <div class="card" style="font-family: var(--font-mono); font-size: 0.95rem; color: var(--accent-emerald); background: #030712; border: 1px solid #1f2937;">
          ${window.App.formatMath(window.App.escapeHtml(currentTopic['8_formula_rule_invariant']))}
        </div>
      </section>
    `;

    // Section 9: Common Mistakes to Avoid
    html += `
      <section class="tb-section">
        <h2 class="tb-section-heading">
          <span class="num">9</span> Common Exam Mistakes to Avoid
        </h2>
        <div class="callout-box warning">
          <div class="callout-title">⚠️ Pitfalls Where Students Lose Marks</div>
          <p style="font-size: 0.92rem; color: var(--text-secondary); line-height: 1.6;">
            ${window.App.formatMath(window.App.escapeHtml(currentTopic['9_common_mistakes_to_avoid']))}
          </p>
        </div>
      </section>
    `;

    // Section 10: Exam-Writing Guidance
    html += `
      <section class="tb-section">
        <h2 class="tb-section-heading">
          <span class="num">10</span> Exam-Writing Structure & Scoring Strategy
        </h2>
        <div class="callout-box exam-rule">
          <div class="callout-title">✍️ Maximum Marks Writing Template</div>
          <p style="font-size: 0.92rem; color: var(--text-primary); line-height: 1.6;">
            ${window.App.formatMath(window.App.escapeHtml(currentTopic['10_exam_writing_guidance']))}
          </p>
        </div>
      </section>
    `;

    // Section 11: Linked Source Questions
    const linkedFamilies = currentTopic['11_linked_question_families'] || [];
    html += `
      <section class="tb-section">
        <h2 class="tb-section-heading">
          <span class="num">11</span> Linked Question Families & Historical Occurrences
        </h2>
        ${linkedFamilies.length ? `
          <div style="display: grid; gap: 0.75rem;">
            ${linkedFamilies.map(fam => `
              <div class="card" style="margin-bottom: 0; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
                <div>
                  <div style="font-weight: 700; color: var(--text-primary); font-size: 0.92rem;">
                    ${window.App.escapeHtml(fam.title || fam.family_id)}
                  </div>
                  <div style="font-size: 0.78rem; color: var(--text-muted); margin-top: 0.2rem;">
                    Family ID: <code>${fam.family_id}</code> • ${fam.count || 1} verified source occurrences
                  </div>
                </div>
                <button class="btn-reveal" onclick="window.StudyModule.filterQuestionsByFamily('${fam.family_id}')">
                  View Questions (${fam.count || 1}) →
                </button>
              </div>
            `).join('')}
          </div>
        ` : `
          <div class="callout-box tip">
            <p style="font-size: 0.9rem; color: var(--text-secondary);">
              Syllabus topic — no supplied question evidence in the historical corpus. Taught thoroughly above for complete syllabus coverage.
            </p>
          </div>
        `}
      </section>
    `;

    // Section 12: Quick Recall Block
    const recall = currentTopic['12_quick_recall_block'];
    if (recall) {
      html += `
        <section class="tb-section">
          <h2 class="tb-section-heading">
            <span class="num">12</span> Active Recall Check
          </h2>
          <div class="recall-block">
            <div class="recall-prompt">
              🎯 Can you state the core rule and checklist items for this topic without looking?
            </div>
            <div style="display: flex; gap: 0.4rem; flex-wrap: wrap; margin-bottom: 0.75rem;">
              ${(recall.trigger_words || []).map(tw => `
                <span class="badge" style="background: var(--bg-primary); border: 1px solid var(--accent-purple); color: var(--accent-purple);">
                  🔑 ${window.App.escapeHtml(tw)}
                </span>
              `).join('')}
            </div>
            <button class="btn-reveal" id="btn-toggle-recall">
              Reveal Active Recall Checklist
            </button>
            <div class="recall-hidden-content" id="recall-content">
              <div style="font-weight: 700; color: var(--accent-cyan); margin-bottom: 0.4rem;">
                Core Invariant: ${window.App.formatMath(window.App.escapeHtml(recall.core_rule))}
              </div>
              <ul style="padding-left: 1.25rem; font-size: 0.88rem; color: var(--text-secondary); line-height: 1.6;">
                ${(recall.exam_checklist || []).map(item => `
                  <li>${window.App.escapeHtml(item)}</li>
                `).join('')}
              </ul>
            </div>
          </div>
        </section>
      `;
    }

    // Previous / Next Navigation Footer
    html += `
      <div style="display: flex; justify-content: space-between; gap: 1rem; margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid var(--border-subtle); flex-wrap: wrap;">
        ${prevTopic ? `
          <button class="btn-reveal" id="btn-prev-topic" data-topic-id="${prevTopic.topic_id}" style="padding: 0.6rem 1.2rem;">
            ← Previous: ${window.App.escapeHtml(prevTopic.topic_title)}
          </button>
        ` : `<div></div>`}

        ${nextTopic ? `
          <button class="btn-reveal" id="btn-next-topic" data-topic-id="${nextTopic.topic_id}" style="padding: 0.6rem 1.2rem; background: var(--accent-cyan); color: #030712; font-weight: 700; border: none;">
            Next: ${window.App.escapeHtml(nextTopic.topic_title)} →
          </button>
        ` : `<div></div>`}
      </div>
    `;

    container.innerHTML = html;

    // Attach event listeners for this topic view
    this.bindTopicViewEvents();
  },

  bindTopicViewEvents() {
    // Recall toggle
    const recallBtn = document.getElementById('btn-toggle-recall');
    const recallContent = document.getElementById('recall-content');
    if (recallBtn && recallContent) {
      recallBtn.addEventListener('click', () => {
        const isRevealed = recallContent.classList.toggle('revealed');
        recallBtn.textContent = isRevealed ? 'Hide Recall Checklist' : 'Reveal Active Recall Checklist';
      });
    }

    // Status pill selection
    document.querySelectorAll('#topic-status-group .status-pill').forEach(btn => {
      btn.addEventListener('click', () => {
        const status = btn.getAttribute('data-status');
        if (status) {
          window.App.updateProgress(window.App.activeTopicId, status);
        }
      });
    });

    // Previous / Next topic buttons
    const prevBtn = document.getElementById('btn-prev-topic');
    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        const tid = prevBtn.getAttribute('data-topic-id');
        if (tid) {
          window.App.activeTopicId = tid;
          this.renderSidebarTree();
          this.renderCurrentTopic();
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      });
    }

    const nextBtn = document.getElementById('btn-next-topic');
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        const tid = nextBtn.getAttribute('data-topic-id');
        if (tid) {
          window.App.activeTopicId = tid;
          this.renderSidebarTree();
          this.renderCurrentTopic();
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      });
    }
  },

  updateTopicStatusPills() {
    const userStatus = window.App.progress[window.App.activeTopicId] || 'NOT_STARTED';
    document.querySelectorAll('#topic-status-group .status-pill').forEach(btn => {
      if (btn.getAttribute('data-status') === userStatus) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
    this.renderSidebarTree();
  },

  filterQuestionsByFamily(familyId) {
    window.App.switchTab('questions');
    const searchFilter = document.getElementById('filter-search');
    if (searchFilter) {
      searchFilter.value = familyId;
      if (window.QuestionsModule) window.QuestionsModule.renderQuestions();
    }
  }
};
