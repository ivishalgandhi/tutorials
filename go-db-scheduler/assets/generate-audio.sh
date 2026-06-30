#!/usr/bin/env bash
# generate-audio.sh — Convert narration scripts to MP3 and copy to NAS
#
# Usage (from go-db-scheduler/ root):
#   ./assets/generate-audio.sh               # generate all 6 lessons
#   ./assets/generate-audio.sh audio/0001-*  # generate one lesson
#
# Requirements: macOS say, ffmpeg (brew install ffmpeg)
#
# ── Configuration ──────────────────────────────────────────────────
VOICE="Samantha"
RATE=175          # words per minute (175 = slightly slower than default for technical terms)
BITRATE="64k"     # 64kbps mono — speech quality, ~7 MB per lesson
NAS_MOUNT="/Volumes/nas/code_artifacts/tutorials/go-db-scheduler/audio"
# ───────────────────────────────────────────────────────────────────

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
WORKSPACE="$(cd "$SCRIPT_DIR/.." && pwd)"
AUDIO_DIR="$WORKSPACE/audio"

# ── Preflight checks ───────────────────────────────────────────────
if ! command -v ffmpeg &>/dev/null; then
  echo "❌  ffmpeg not found. Install with: brew install ffmpeg"
  exit 1
fi

if [[ ! -d "$NAS_MOUNT" ]]; then
  echo "⚠️   NAS not mounted at $NAS_MOUNT — will generate locally only."
  NAS_MOUNT=""
fi

# ── File list ──────────────────────────────────────────────────────
if [[ $# -gt 0 ]]; then
  SCRIPTS=("$@")
else
  SCRIPTS=("$AUDIO_DIR"/*.narration.txt)
fi

if [[ ${#SCRIPTS[@]} -eq 0 ]]; then
  echo "No .narration.txt files found in $AUDIO_DIR"
  exit 1
fi

# ── Generate each file ─────────────────────────────────────────────
for narration in "${SCRIPTS[@]}"; do
  [[ -f "$narration" ]] || { echo "Skipping (not found): $narration"; continue; }

  base="${narration%.narration.txt}"
  slug="$(basename "$base")"
  aiff="${base}.aiff"
  mp3="${base}.mp3"

  echo "▶  $slug"

  # Step 1 — text → AIFF
  say -v "$VOICE" -r "$RATE" -o "$aiff" -f "$narration"

  # Step 2 — AIFF → MP3 (64kbps mono, normalised)
  ffmpeg -y -i "$aiff" \
    -af "loudnorm=I=-16:TP=-1.5:LRA=11" \
    -codec:a libmp3lame -b:a "$BITRATE" -ac 1 \
    "$mp3" 2>/dev/null
  echo "   ✓ $(du -sh "$mp3" | cut -f1)  →  $mp3"

  # Step 3 — remove intermediate AIFF
  rm -f "$aiff"

  # Step 4 — copy to NAS if mounted
  if [[ -n "$NAS_MOUNT" ]]; then
    cp "$mp3" "$NAS_MOUNT/${slug}.mp3"
    echo "   ✓ copied to NAS: $NAS_MOUNT/${slug}.mp3"
  fi
done

echo ""
echo "Done. ${#SCRIPTS[@]} lesson(s) processed."
if [[ -z "$NAS_MOUNT" ]]; then
  echo "Note: NAS was not mounted — files are local only in $AUDIO_DIR"
fi
