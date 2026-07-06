# The Federalist Papers: Explained — Series Status

## Overview
- Total papers: 85
- Episodes completed: 25 (audio produced)
- Episodes scripted: 25
- Next episode to produce: Episode 26 (Federalist No. 26)

## Episode Status

| # | Title | Author | Script | Audio | Published |
|---|-------|--------|--------|-------|-----------|
| 1 | Why These Essays Matter | Hamilton | DONE | DONE | YES |
| 2 | Why the Union Matters | Jay | DONE | DONE | YES |
| 3 | Why Union Prevents War | Jay | DONE | DONE | In iCloud |
| 4 | Foreign Threats and National Unity | Jay | DONE | DONE | In iCloud |
| 5 | Why Rival Confederacies Turn Against Each Other | Jay | DONE | DONE | In iCloud |
| 6 | Why Disunion Means War | Hamilton | DONE | DONE | - |
| 7 | What States Would Fight Over | Hamilton | DONE | DONE | - |
| 8 | How Disunion Would Cost Us Our Freedom | Hamilton | DONE | DONE | - |
| 9 | How Union Saves Republics from Themselves | Hamilton | DONE | DONE | - |
| 10 | Why a Big Republic Beats Faction | Madison | DONE | DONE | - |
| 11 | Why Union Turns Trade Into Power | Hamilton | DONE | DONE | - |
| 12 | Where the Money Comes From | Hamilton | DONE | DONE | - |
| 13 | Why One Country Is Cheaper Than Several | Hamilton | DONE | DONE | - |
| 14 | Is America Too Big to Govern? | Madison | DONE | DONE | - |
| 15 | Why America's First Government Failed | Hamilton | DONE | DONE | - |
| 16 | You Can't Put a State in Jail | Hamilton | DONE | DONE | - |
| 17 | The Government You Can Feel | Hamilton | DONE | DONE | - |
| 18 | What Ancient Greece Got Wrong | Hamilton/Madison | DONE | DONE | - |
| 19 | A Thousand Years of Falling Apart | Hamilton/Madison | DONE | DONE | - |
| 20 | When the Sword Is All You Have | Hamilton/Madison | DONE | DONE | - |
| 21 | A Government With No Teeth | Hamilton | DONE | DONE | - |
| 22 | We the People, Not the States | Hamilton | DONE | DONE | - |
| 23 | Strong Enough to Defend Us | Hamilton | DONE | DONE | - |
| 24 | The Army That Scared Everyone | Hamilton | DONE | DONE | - |
| 25 | Who Should Hold the Army | Hamilton | DONE | DONE | - |
| 26-85 | Remaining papers | Various | NOT STARTED | NOT STARTED | - |

## Authorship reference (first 10 papers)
1. Hamilton
2. Jay
3. Jay
4. Jay
5. Jay
6. Hamilton
7. Hamilton
8. Hamilton
9. Hamilton
10. Madison

## Audio production
Every episode is produced through ElevenLabs using the Nate voice. Each episode folder has its own `produce-episode.py`. See `_production/references/episode-production-workflow.md` for the full pipeline.

## Folder structure
- `_production/references/` — production workflow + brand system docs
- `_production/source-texts/` — original Federalist Papers (Yale Avalon Project)
- `_production/tools/` — shared post-render scripts: `audio-qa.py` (automated QA — Deepgram transcript diff) and `fix-segment.py` (surgical single-sentence audio repair)
- `Federalist paper number {N}/` — per-episode folder
  - `federalist-no-{N}-script.txt` — audio-ready script
  - `episode-metadata.md` — title and descriptions
  - `produce-episode.py` — ElevenLabs audio production script
  - `federalist-no-{N}-episode-final.mp3` — final audio (ID3-tagged, cover art embedded)
  - `audio-qa.md` — automated audio-QA report (must read PASS before publish)
  - `audio-chunks/` — per-chunk mp3s + manifest
  - `Episode Art.png` (or named variant) — cover art
- `Show Art.png` — series cover art

## Production pace
ElevenLabs rendering bills per character (~21,000–22,000 characters per episode) and requires the Creator tier or above for 192 kbps output. Rendering a full episode takes a few minutes.
