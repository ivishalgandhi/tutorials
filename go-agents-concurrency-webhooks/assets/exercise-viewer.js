(function () {
  const viewers = document.querySelectorAll('.exercise-viewer');
  if (!viewers.length) return;

  viewers.forEach(function (viewer) {
    const base = viewer.dataset.base;
    let exercises = [];
    try {
      exercises = JSON.parse(viewer.dataset.exercises || '[]');
    } catch (e) {
      viewer.innerHTML = '<div class="ex-desc">Error parsing exercise viewer config.</div>';
      return;
    }
    if (!exercises.length) {
      viewer.innerHTML = '<div class="ex-desc">No exercises configured.</div>';
      return;
    }

    let currentEx = exercises[0].id;
    let currentFile = 'problem';

    viewer.innerHTML =
      '<div class="ex-tabs"></div>' +
      '<div class="ex-desc"></div>' +
      '<div class="ex-toolbar">' +
      '  <button class="ex-file-toggle ex-file-toggle-active" data-file="problem">problem.go</button>' +
      '  <button class="ex-file-toggle" data-file="solution">solution.go</button>' +
      '  <span class="ex-copy" title="Copy to clipboard">⎘ copy</span>' +
      '</div>' +
      '<div class="ex-code-wrap"><pre><code class="ex-code-inner">Loading…</code></pre></div>' +
      '<div class="ex-status"></div>';

    const tabsEl = viewer.querySelector('.ex-tabs');
    const descEl = viewer.querySelector('.ex-desc');
    const codeEl = viewer.querySelector('.ex-code-inner');
    const statusEl = viewer.querySelector('.ex-status');

    exercises.forEach(function (ex) {
      const btn = document.createElement('button');
      btn.className = 'ex-tab' + (ex.id === currentEx ? ' ex-tab-active' : '');
      btn.textContent = ex.label;
      btn.dataset.ex = ex.id;
      tabsEl.appendChild(btn);
    });

    function setStatus(msg) {
      statusEl.textContent = msg;
    }

    async function loadFile() {
      const path = base + currentEx + '/' + currentFile + '.go';
      setStatus('Loading ' + path + '…');
      try {
        const r = await fetch(path);
        if (!r.ok) throw new Error('HTTP ' + r.status);
        const text = await r.text();
        codeEl.textContent = text;
        setStatus(path + ' · ' + text.split('\n').length + ' lines · ' + (text.length / 1024).toFixed(1) + ' KB');
      } catch (e) {
        codeEl.textContent = 'Could not load file: ' + e.message;
        setStatus('Error loading file');
      }
    }

    tabsEl.addEventListener('click', function (e) {
      if (!e.target.classList.contains('ex-tab')) return;
      tabsEl.querySelectorAll('.ex-tab').forEach(function (b) { b.classList.remove('ex-tab-active'); });
      e.target.classList.add('ex-tab-active');
      currentEx = e.target.dataset.ex;
      const ex = exercises.find(function (x) { return x.id === currentEx; });
      descEl.textContent = ex ? ex.description : '';
      loadFile();
    });

    viewer.querySelector('.ex-toolbar').addEventListener('click', function (e) {
      if (!e.target.classList.contains('ex-file-toggle')) return;
      viewer.querySelectorAll('.ex-file-toggle').forEach(function (b) { b.classList.remove('ex-file-toggle-active'); });
      e.target.classList.add('ex-file-toggle-active');
      currentFile = e.target.dataset.file;
      loadFile();
    });

    viewer.querySelector('.ex-copy').addEventListener('click', function () {
      navigator.clipboard.writeText(codeEl.textContent).then(function () {
        const btn = viewer.querySelector('.ex-copy');
        btn.textContent = '✓ copied';
        setTimeout(function () { btn.textContent = '⎘ copy'; }, 1500);
      });
    });

    descEl.textContent = exercises[0].description;
    loadFile();
  });
})();
