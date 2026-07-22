/**
 * quiz.js — Reusable multiple-choice quiz widget
 *
 * Usage: <div class="quiz" data-question="..." data-correct="B">
 *          <div class="quiz-option" data-key="A">...</div>
 *          <div class="quiz-option" data-key="B">...</div>
 *        </div>
 */
(function () {
  'use strict';

  const STYLES = `
    .quiz-section { margin: 2.5rem 0; }
    .quiz-section h2 { margin-bottom: 1.2rem; }
    .quiz {
      background: #fff;
      border: 2px solid #d8d4cc;
      border-radius: 8px;
      padding: 1.4em 1.6em;
      margin: 1.4em 0;
    }
    .quiz-question {
      font-weight: 600;
      margin-bottom: 1em;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      font-size: 0.95rem;
      line-height: 1.45;
    }
    .quiz-options { display: flex; flex-direction: column; gap: 0.5em; }
    .quiz-option {
      display: flex;
      align-items: flex-start;
      gap: 0.7em;
      padding: 0.65em 0.9em;
      border: 1.5px solid #d8d4cc;
      border-radius: 6px;
      cursor: pointer;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      font-size: 0.88rem;
      line-height: 1.45;
      transition: background .12s, border-color .12s;
      user-select: none;
    }
    .quiz-option:hover:not(.answered) { background: #f0f4ff; border-color: #0056b3; }
    .quiz-option .opt-key {
      flex-shrink: 0;
      width: 1.5em;
      height: 1.5em;
      border-radius: 50%;
      border: 1.5px solid #aaa;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 0.78rem;
      color: #555;
    }
    .quiz-option.correct  { background: #e6f9ec; border-color: #1e7e34; }
    .quiz-option.correct  .opt-key { background: #1e7e34; border-color: #1e7e34; color: #fff; }
    .quiz-option.wrong    { background: #fff0ee; border-color: #c0392b; }
    .quiz-option.wrong    .opt-key { background: #c0392b; border-color: #c0392b; color: #fff; }
    .quiz-option.revealed { background: #e6f9ec; border-color: #1e7e34; opacity: 0.7; }
    .quiz-option.answered { cursor: default; }
    .quiz-feedback {
      margin-top: 0.9em;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      font-size: 0.86rem;
      padding: 0.6em 0.9em;
      border-radius: 5px;
      display: none;
    }
    .quiz-feedback.show { display: block; }
    .quiz-feedback.correct { background: #e6f9ec; color: #155724; }
    .quiz-feedback.wrong   { background: #fff0ee; color: #721c24; }
    .quiz-progress {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      font-size: 0.8rem;
      color: #666;
      margin-top: 1.5em;
    }
    .quiz-score-bar {
      height: 6px;
      background: #e0e0e0;
      border-radius: 99px;
      margin-top: 0.5em;
      overflow: hidden;
    }
    .quiz-score-bar-fill {
      height: 100%;
      background: #1e7e34;
      border-radius: 99px;
      transition: width .4s;
    }
    .quiz-reset {
      margin-top: 1em;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      font-size: 0.8rem;
      color: #0056b3;
      cursor: pointer;
      border: none;
      background: none;
      padding: 0;
      text-decoration: underline;
    }
  `;

  function injectStyles() {
    if (document.getElementById('quiz-styles')) return;
    const s = document.createElement('style');
    s.id = 'quiz-styles';
    s.textContent = STYLES;
    document.head.appendChild(s);
  }

  function initQuizzes() {
    injectStyles();
    const sections = document.querySelectorAll('.quiz-section');
    sections.forEach(section => {
      const quizzes = section.querySelectorAll('.quiz');
      let answered = 0, correct = 0;

      const progress = document.createElement('div');
      progress.className = 'quiz-progress';
      const bar = document.createElement('div');
      bar.className = 'quiz-score-bar';
      const fill = document.createElement('div');
      fill.className = 'quiz-score-bar-fill';
      fill.style.width = '0%';
      bar.appendChild(fill);

      function updateProgress() {
        progress.textContent = `${answered} of ${quizzes.length} answered · ${correct} correct`;
        fill.style.width = quizzes.length ? (correct / quizzes.length * 100) + '%' : '0%';
      }
      updateProgress();

      quizzes.forEach(quiz => {
        const questionText = quiz.dataset.question;
        const correctKey   = (quiz.dataset.correct || '').toUpperCase();
        const options      = quiz.querySelectorAll('.quiz-option');

        const q = document.createElement('div');
        q.className = 'quiz-question';
        q.textContent = questionText;
        quiz.insertBefore(q, quiz.firstChild);

        const wrapper = document.createElement('div');
        wrapper.className = 'quiz-options';
        options.forEach(opt => wrapper.appendChild(opt));
        quiz.appendChild(wrapper);

        const fb = document.createElement('div');
        fb.className = 'quiz-feedback';
        quiz.appendChild(fb);

        let done = false;
        options.forEach(opt => {
          const key = (opt.dataset.key || '').toUpperCase();
          const keyBadge = document.createElement('span');
          keyBadge.className = 'opt-key';
          keyBadge.textContent = key;
          opt.prepend(keyBadge);

          opt.addEventListener('click', () => {
            if (done) return;
            done = true;
            answered++;
            const isCorrect = key === correctKey;
            if (isCorrect) correct++;

            options.forEach(o => {
              o.classList.add('answered');
              if ((o.dataset.key || '').toUpperCase() === correctKey) {
                o.classList.add(isCorrect && o === opt ? 'correct' : 'revealed');
              }
            });
            if (!isCorrect) opt.classList.add('wrong');
            else opt.classList.add('correct');

            fb.textContent = isCorrect
              ? (quiz.dataset.feedbackCorrect || '✓ Correct!')
              : (quiz.dataset.feedbackWrong || `✗ Not quite. The answer is ${correctKey}.`);
            fb.className = `quiz-feedback show ${isCorrect ? 'correct' : 'wrong'}`;
            updateProgress();
          });
        });
      });

      section.appendChild(progress);
      section.appendChild(bar);
      const reset = document.createElement('button');
      reset.className = 'quiz-reset';
      reset.textContent = 'Reset quiz';
      reset.addEventListener('click', () => location.reload());
      section.appendChild(reset);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initQuizzes);
  } else {
    initQuizzes();
  }
})();
