# The Federalist Papers: Explained — Production Pipeline

The code, docs, and reference material for producing *The Federalist Papers: Explained*, a
single-host podcast that explains each of the 85 Federalist Papers in plain English. One episode
per paper.

This repository holds the **pipeline** — the workflow, the scripts, the source texts, and the
audio tooling. It deliberately does **not** contain the rendered audio (MP3s), the video/Final Cut
Pro edits, or any API keys. A fresh clone plus your own `.env` is enough to produce a new episode
exactly the way the series is produced today.

## What's here

```
_production/
  references/
    episode-production-workflow.md   # THE canonical end-to-end workflow — read this first
    brand-system.md                  # voice, titles, descriptions, brand rules
  source-texts/
    federalist-no-N.txt              # original paper text (Yale Avalon), the quote-check authority
  tools/
    audio-qa.py                      # automated post-render QA (Deepgram transcript diff)
    fix-segment.py                   # surgical single-sentence audio repair
Federalist paper number N/
  federalist-no-N-script.txt         # audio-ready script
  episode-metadata.md                # title + descriptions
  fact-check.md                      # Gate 4 fact-check log
  produce-episode.py                 # renders the script to audio via ElevenLabs
  audio-qa.md                        # audio-QA report (generated)
  # federalist-no-N-episode-final.mp3 and audio-chunks/ are produced locally, not committed
Show Art.png                         # series cover art, embedded into every episode
SERIES-STATUS.md                     # episode tracker + authorship reference
```

## Setup on a new machine

1. **Clone** this repo.
2. **Install prerequisites:** Python 3 and `ffmpeg`/`ffprobe` (`brew install ffmpeg` on macOS).
3. **Add your keys:** copy `.env.example` to `.env` and fill in `eleven-labs-api=` and `deepgram-api=`.
   - ElevenLabs needs the Creator tier or above for 192 kbps output.
4. That's it — no other dependencies. The scripts use only the Python standard library plus ffmpeg.

## Making an episode

The full, authoritative process is in **`_production/references/episode-production-workflow.md`**.
Read it end-to-end first. In short, for episode N:

1. Work through the six writing gates (read the gold-standard episodes 5/6/7, draft, storytelling
   pass, fact-check, runtime check, TTS-readability pass) to produce `federalist-no-N-script.txt`.
2. Render the audio:
   ```bash
   python3 "Federalist paper number N/produce-episode.py"
   ```
   It chunks the script, renders each chunk through ElevenLabs (cached, so re-renders are cheap),
   concatenates with ffmpeg, and embeds ID3 tags + `Show Art.png`.
3. **Run automated audio QA** (required — must read PASS):
   ```bash
   python3 _production/tools/audio-qa.py N
   ```
   It transcribes the finished MP3 with Deepgram, diffs it against the script, and flags stutters,
   doubled words, dropped sections, and dead air — then points you to exact timestamps to confirm.
4. If a spot is a real glitch, repair just that sentence cheaply (few cents, not a whole re-render):
   ```bash
   python3 _production/tools/fix-segment.py N --start <s> --end <s> --text "corrected sentence"   # dry run
   python3 _production/tools/fix-segment.py N --start <s> --end <s> --text "..." --apply
   ```

## Notes

- The voice is the ElevenLabs "Nate" voice with fixed settings (see any `produce-episode.py`);
  keep these constant across the series.
- Rendered audio, chunk caches, and the video edit are intentionally untracked (see `.gitignore`).
- Never commit `.env` — only `.env.example`.
