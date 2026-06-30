/**
 * audio-player.js — Reusable lesson audio player
 *
 * Usage: add data-audio="filename.mp3" to the .lesson-meta div,
 * then include this script at the bottom of the lesson.
 *
 * The player renders a compact bar just below the lesson header.
 * It hides itself silently if the audio file cannot be loaded.
 *
 * --- CONFIGURATION ---
 * Change AUDIO_BASE to point at your NAS/CDN once HTTP serving is set up.
 * For local dev: '../audio/'
 * For NAS:       'https://your-nas-url/code/tutorials/audio/'
 */

(function () {
  'use strict';

  // ── Configuration ──────────────────────────────────────────────
  // Local dev:
  // const AUDIO_BASE = '../audio/';
  // Production: audio served via Dokploy HTTPS on /audio path
  const AUDIO_BASE = 'https://dokploy.tail48fe8.ts.net/audio/tutorials/go-db-scheduler/audio/';
  // ───────────────────────────────────────────────────────────────

  const STYLES = `
    .audio-player-bar {
      display: flex;
      align-items: center;
      gap: 0.9rem;
      background: #fff;
      border: 1px solid #b3dde8;
      border-radius: 8px;
      padding: 0.65rem 1rem;
      margin: 0 0 1.8rem;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    .audio-player-icon {
      flex-shrink: 0;
      width: 2rem;
      height: 2rem;
      background: #007d9c;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      font-size: 0.9rem;
      cursor: pointer;
      border: none;
      transition: background 0.15s;
    }
    .audio-player-icon:hover { background: #005f78; }
    .audio-player-icon svg { display: block; }
    .audio-player-label {
      font-size: 0.78rem;
      font-weight: 600;
      color: #007d9c;
      white-space: nowrap;
      flex-shrink: 0;
    }
    .audio-player-bar audio {
      flex: 1;
      height: 28px;
      min-width: 0;
      accent-color: #007d9c;
    }
    .audio-player-bar audio::-webkit-media-controls-panel {
      background: #e6f7fb;
    }
  `;

  const ICON_PLAY = `<svg width="12" height="14" viewBox="0 0 12 14" fill="currentColor">
    <path d="M1 1l10 6L1 13V1z"/>
  </svg>`;

  function injectStyles () {
    if (document.getElementById('audio-player-styles')) return;
    const s = document.createElement('style');
    s.id = 'audio-player-styles';
    s.textContent = STYLES;
    document.head.appendChild(s);
  }

  function init () {
    const meta = document.querySelector('[data-audio]');
    if (!meta) return;

    const filename = meta.getAttribute('data-audio');
    if (!filename) return;

    const src = AUDIO_BASE + filename;

    injectStyles();

    // Build the player bar
    const bar = document.createElement('div');
    bar.className = 'audio-player-bar';

    const icon = document.createElement('button');
    icon.className = 'audio-player-icon';
    icon.setAttribute('aria-label', 'Play audio lesson');
    icon.innerHTML = ICON_PLAY;

    const label = document.createElement('span');
    label.className = 'audio-player-label';
    label.textContent = 'Listen';

    const audio = document.createElement('audio');
    audio.controls = true;
    audio.preload = 'none';
    audio.src = src;

    // Hide the bar entirely if the file can't be loaded
    audio.addEventListener('error', function () {
      bar.style.display = 'none';
    });

    // Icon click toggles play/pause
    icon.addEventListener('click', function () {
      if (audio.paused) {
        audio.play();
        icon.innerHTML = `<svg width="12" height="14" viewBox="0 0 10 14" fill="currentColor">
          <rect x="0" y="0" width="3.5" height="14" rx="1"/>
          <rect x="6.5" y="0" width="3.5" height="14" rx="1"/>
        </svg>`;
      } else {
        audio.pause();
        icon.innerHTML = ICON_PLAY;
      }
    });

    audio.addEventListener('ended', function () {
      icon.innerHTML = ICON_PLAY;
    });

    bar.appendChild(icon);
    bar.appendChild(label);
    bar.appendChild(audio);

    // Insert the bar immediately before the <h1>
    const h1 = document.querySelector('h1');
    if (h1) {
      h1.parentNode.insertBefore(bar, h1);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
