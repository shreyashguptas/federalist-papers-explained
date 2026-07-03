# Episode Production Workflow

This is the canonical end-to-end workflow for producing one episode of *The Federalist Papers: Explained*. Following this document together with the brand system (`brand-system.md`) should reproduce the quality of the series' best episodes.

If the user says **"create episode N"**, this is the document to follow.

## The gold standard — read this first

**The fixed gold standard is Episodes 5, 6, and 7.** Read all three before drafting anything, every single time, even on episode 40. They are *storytelling-first*: they convey each paper's argument by telling stories **about** it — a person, a scene, a vivid example given room to breathe — rather than walking through the paper paragraph by paragraph.

Episodes 8 onward drifted. The drift started subtly in Episode 8 (quote count creeping up, structure beginning to track the paper beat by beat), became a real structural problem in Episode 9 (length jumped, exegesis took over), and was full-blown in Episode 10 (~25 set-apart quotes, a relentless "the author opens… then says… then turns to…" march, listener-questions gone). Every sentence in 9 and 10 is plain English — they fail anyway, because the *shape* became an annotated read-through instead of an explainer.

The lesson baked into this rubric: **anchor every new episode on the fixed 5–6–7 standard, never on "the previous episode."** Small drift compounds when each episode copies the last one.

## Goal
Produce episodes that are:
- simple
- accurate
- natural-sounding
- technically clean
- consistent across the full 85-paper series
- stylistically continuous with all previously completed episodes

## Core voice strengths to preserve
- plain-English explanation
- a warm single-host voice
- **storytelling, not exegesis** — the episode tells stories *about* the paper's argument; it never walks through the paper paragraph by paragraph
- **4–8 substantial quote-plus-explanation moments per episode, no more** — and note that many small quotes, each individually explained, is still a quote dump
- **2–3 story set-pieces per episode** where the script slows down and tells something richly (a person, a scene, a concrete example, a piece of history)
- historical context around the author and moment
- modern parallels woven *through the body*, not bunched into a closing section
- a flowing narrative rather than a sequence of facts

## Inputs you start with for episode N
- `_production/source-texts/federalist-no-N.txt` — the original Federalist Paper text
- `Federalist paper number N/` — folder where the deliverable lives (script, art, metadata, audio)
- All earlier episode scripts at `Federalist paper number {1..N-1}/federalist-no-{1..N-1}-script.txt`
- All earlier episode metadata at `Federalist paper number {1..N-1}/episode-metadata.md`

## Outputs you produce for episode N
- `Federalist paper number N/federalist-no-N-script.txt` — the audio-ready script
- `Federalist paper number N/fact-check.md` — the Gate 4 web fact-check log (claim → verdict → source URL); required from Episode 12 onward
- `Federalist paper number N/episode-metadata.md` — title + descriptions
- `Federalist paper number N/produce-episode.py` — the episode's audio production script
- `Federalist paper number N/federalist-no-N-episode-final.mp3` — final audio (ID3-tagged, cover art embedded)
- `Federalist paper number N/audio-chunks/` — per-chunk mp3s + manifest (so partial re-renders are cheap)
- `Federalist paper number N/audio-qa.md` — the automated audio-QA report (Deepgram transcript diff). Required, like `fact-check.md`: it must read **PASS** (or every remaining flag understood and accepted) before the episode is done.

---

## Gate sequence (in strict order)

### Gate 1 — Read everything earlier first
- **Read Episodes 5, 6, and 7 first, every time — these are the fixed gold standard for voice and structure.** Study *how* they tell stories about the argument instead of marching through it. Do not skip this, ever.
- Read every prior completed episode script (1 through N−1) for **continuity facts and callbacks** — but treat them as *reference for what happened*, not as the *voice model*. The voice model is always 5–6–7. Do not anchor on episode N−1.
- Read each prior episode's `episode-metadata.md` for title style and description voice
- Read the source paper at `_production/source-texts/federalist-no-N.txt`
- Note: style, transitions, opening moves, vocabulary level, pacing patterns, listener-question rhythm
- Identify any meaningful factual or rhetorical connections between paper N and earlier papers (especially when the same author is continuing or sharpening a prior argument)

### Gate 2 — Draft script
Write the full episode script following all rules below. Save at `Federalist paper number N/federalist-no-N-script.txt`.

#### Always do
- explain the paper in plain English a 14-year-old can follow
- sound like a smart, warm host, not a lecturer
- match the voice and rhythm of the **gold-standard episodes (5, 6, 7)** — not whatever the previous episode happened to do
- **structure the episode independently of the paper.** The episode's running order must not mirror the paper's paragraph order. You are the host deciding what to teach first, what to build to, what to set aside. A script whose skeleton is "the paper's paragraphs in sequence" has already failed, no matter how plain its sentences are.
- **convey the paper's spine** — its 3–4 load-bearing ideas — richly; summarize the connective material briskly in the host's own voice
- **pick 2–3 moments to slow down and tell as a story** — a person, a scene, a vivid concrete example, a piece of history given room (the Pericles story in Ep 6, the Wyoming Valley feud in Ep 7, the Northern Hive image in Ep 5). Depth comes from these set-pieces, not from even coverage of everything.
- include **4–8 substantial exact quotes** — the lines where the listener genuinely benefits from hearing Hamilton/Madison/Jay's own words. This is a ceiling, not a target; fewer is fine. Paraphrase attributions ("Madison says faction is permanent") do **not** count against the ceiling and are encouraged — they are how you cover the paper without quote-dumping.
- explain each quote in plain English right after it appears
- include useful historical context (who, when, what was happening politically)
- weave modern parallels through the body, next to the ideas they illuminate (Eisenhower's farewell address in ep 8 is a good example) — not bunched into a closing "for modern listeners" section
- include "listener question" moments — phrases like *"At this point you might be wondering..."*, *"A fair question here is..."*, *"So why does that matter?"* — **3–6 per episode, spread through the body**, used on purpose
- keep transitions smooth and conversational
- write with **TTS readability** in mind — see Gate 6 for the specific checks

#### Avoid
- **exegesis / annotated read-through — the single biggest failure mode.** Tell-tale sign: the connective tissue becomes *"[Author] opens with… He then says… Now [Author] turns to… Then [Author] delivers…"* — a chain that tracks the paper beat by beat. If a stretch of your script reads like a tour of the paper's table of contents, rewrite it as the host explaining the idea in their own words.
- **quote dumping in slow motion** — many quotes, each individually explained, is still a quote dump. The explanations do not redeem the count.
- quote dumping (back-to-back quotes without explanation)
- academic jargon when plain English works
- dramatic formatting that creates dead air (theatrical paragraph breaks, isolated single-word lines stacked)
- excessive ellipses or fragmented sentences in series
- forced callbacks to other episodes (only use a callback if the connection is genuine)
- letting the opening recap of prior episodes grow over time (recap only the *previous* episode, not 1+2+3+...+N−1)

#### Episode 1 special rule
Near the beginning, briefly explain:
- who this series is for
- what listeners will get from the show
- what the 85-episode series is trying to help them understand

Keep this short and welcoming. (For episodes 2+ this rule does not apply — start with the previous-episode recap.)

#### Episodes 2–85 continuity rule
Each episode's opener should briefly recap the previous episode (not the full series). When paper N is meaningfully connected to an earlier paper:
- include 1–3 brief, factual references to earlier episodes
- preserve the feel of a continuing conversation rather than a reset each week
- never force a callback — if the connection is weak, drop it
- **continuity is for *facts and callbacks* only.** For *voice and structure*, anchor on the fixed gold standard (Episodes 5–6–7), never on episode N−1. Anchoring on the previous episode is how small drift compounds across the series.

### Gate 3 — Storytelling and voice pass
The draft from Gate 2 is now reviewed against the voice standard the way Gate 4 reviews it against the facts. **This pass is mandatory and has explicit checks** — it exists because the mechanical rules (Gate 6) have always been followed while the voice rules quietly evaporated. Run it with the gold-standard episodes (5, 6, 7) open alongside the draft.

#### The exegesis test (the most important check)
🔍 Read only the connective sentences between paragraphs — just the transitions. If they form a chain like *"[Author] opens… He then admits… [Author] then gives… Now [Author] turns… Take the first… Take the second… Then [Author] says…"*, the script is an annotated read-through, not an explainer. **This is a failing draft.** Rewrite the structure so the host — not the paper — decides the order.

🔍 Lay the episode's section order next to the source paper's paragraph order. If they march in lockstep, that is the failure. Re-sequence by what is most teachable, not by what comes next in the paper.

#### Quote count
🔍 Count the substantial set-apart quotes — the ones you stop and explain. **Ceiling is 8. Target is 4–6.** If you are over 8, cut the weakest and replace them with paraphrase in the host's voice. Paraphrase attributions are unlimited and do not count.

🔍 Check that no two set-apart quotes sit back to back without real narrative between them.

#### Story set-pieces
🔍 Confirm there are **2–3 passages where the script genuinely slows down and tells something as a story** — a person, a scene, a concrete example, a piece of history. If the whole episode runs at one even pace, it has no shape. Add depth at 2–3 chosen moments; trim even coverage everywhere else.

#### Breathing room
🔍 Count listener-question moments (*"you might be wondering"*, *"a fair question here"*, *"so why does that matter"*). There must be **3–6, spread through the body**, not clustered.

🔍 Confirm modern parallels appear in the body next to the ideas they illuminate — not solely in a closing section.

#### Voice
🔍 Read a random middle paragraph aloud. Does it sound like a warm host talking, or like a lecturer annotating a text? If it is the second, the draft has not cleared this gate.

Revise the script. **If the exegesis test failed, that is a structural rewrite, not a trim.** Only move forward once the draft clears this gate.

### Gate 4 — Fact-check pass
Run a separate fact-check review against the actual paper, the relevant historical context, and any continuity references. This gate has two parts: a source check and a web cross-check.

#### Part A — Source and continuity check
- quotes are **exact** — word-for-word from the source paper at `_production/source-texts/federalist-no-N.txt`. That file is the authority; verify mechanically (a normalized substring check), not by eye. Do not "verify" a quote against the web — a web transcription can be worse than the source file.
- paraphrases are faithful to the paper
- authorship is correct (cross-check against the authorship reference in `SERIES-STATUS.md`)
- cross-episode references are factually grounded (check against the actual earlier scripts, not memory)

#### Part B — Web cross-check (Episode 12 onward)
Every **non-quote factual claim** in the script must be cross-checked against the open web. This covers dates, names, places, events, numbers, publication facts, biographical detail, the historical framing, and the modern parallels.

- Extract every discrete factual claim into a checklist.
- For each claim, run a targeted web search against high-quality sources — encyclopedias, `.edu` pages, primary-source archives. Require **two independent corroborating sources for any load-bearing claim**.
- Classify each claim:
  - ✅ **verified** — corroborated by reliable sources
  - ⚠️ **contested** — historians genuinely disagree; the script must hedge it honestly (do not force false certainty), or it fails
  - ❌ **wrong** — fix the script, then re-check
- Modern parallels get the same treatment: confirm they do not distort the original argument.
- The goal is **fully sourced, not "100% certain."** Some history is genuinely contested; the honest outcome there is a fair hedge in the script, not invented certainty.

Record the result in `Federalist paper number N/fact-check.md` — a table of claim → verdict → source URL(s). This artifact is required before the script can leave Gate 4.

Revise the script. If any claim came back ❌, fix it and run the fact-check pass again. Only move forward once every claim is ✅ verified or a fairly-hedged ⚠️.

### Gate 5 — Runtime/depth check
- Estimate spoken runtime before TTS (rough rule: ~150 words/minute = ~900 chars/minute). A 25-min episode ≈ 22,000 chars; a 30-min episode ≈ 27,000 chars.
- **Preferred runtime band: 25 to 40 minutes.** Most episodes should land in the lower-middle of that band — the gold-standard episodes 5, 6, and 7 run 24–34 minutes. Treat the upper half of the band as a warning zone, not a target.
- If the script is clearly below 25 minutes, do not send it to audio yet. Expand with more real explanation and an extra story set-piece — not filler, and not more quotes.
- **If the script is past 38 minutes, treat it as a red flag for exegesis — not as "a deep paper."** Length is almost never caused by the paper being long; it is caused by the script covering every paragraph and quoting too heavily. Go back to Gate 3. The fix is structural — convey the spine, cut the even coverage — not a light trim.
- **"Covered" means the listener can follow the whole argument — not that every paragraph and every quotable line made it in.** Convey the paper's spine: its 3–4 load-bearing ideas, told richly. A faithful explainer of the spine beats a complete transcription every time.

### Gate 6 — TTS-readability and sanitization pass
The final audio-ready script must contain spoken text only, written so the ElevenLabs Nate voice renders it cleanly.

#### Strip non-spoken artifacts
- markdown separators (`---`, `***`, `===`)
- headers or title blocks at the top
- section headers or chapter labels not meant to be spoken
- labels like INTRO, SEGMENT, OUTRO, END OF SCRIPT
- placeholder notes, stage directions, production notes
- chunk markers or manifest artifacts

#### TTS-readability checks (every script must pass these)

**Lists must have explicit verbal signposts.** A flat list — "Territory, with X. Commerce, with Y. Public debt, with Z." — sounds bad in audio: each item is just an abrupt topic change with a pause between. Listeners can't tell they're inside a list, which item they're on, or how many remain.

✅ Always enumerate: *"first, ... second, ... third, ... and fourth, ..."* — or use clear connective tissue (*"the first is X. The second is Y."*).

🔍 Find every place where the script names a count of items ("a list of five", "two things", "the answer was three-fold") and verify each item is preceded by an ordinal.

🔍 Find paragraphs where multiple parallel items appear without "and"+last-item phrasing — those are usually un-enumerated lists hiding as run-on sentences.

⚠️ Hamilton's own quotes can stay as-written even with flat parallelism (*"of towns taken and retaken, of battles that decide nothing, of retreats more beneficial than victories"*) — those scan fine because they're rhythmic anaphora, not topic-change lists.

**Numbers and dates must be spelled out for TTS.**
- Years: "1787" → "seventeen eighty-seven", "1961" → "nineteen sixty-one", "1688" → "sixteen eighty-eight"
- "No." → "Number" (e.g., "Federalist Number 8" not "Federalist No. 8")
- Roman numerals: "Charles II" → "Charles the Second", "King James II" → "King James the Second"
- Hyphenated period-spellings: "New-York Packet" → "New York Packet" (the hyphen gets read literally)

**Punctuation cues**
- Use em-dashes (—) for natural pause-and-pivot moments — the voice reads them as a beat. **But do not put an em-dash immediately before a short function word ("— and", "— but", "— or", "— a", "— to").** That exact pattern is the single most common trigger for the voice stuttering and doubling the next word — it is what caused the "notes — and … and raises his voice" glitch in Episode 14. In that spot use a comma or a period instead: the spoken words are identical, the pause still lands, and it does not stutter.
- Avoid back-to-back single-word sentences in stacks. *"Fast. Mobile. Open at the borders."* is fine as a punchy three. A stack of six single-word sentences feels mechanical.
- Avoid multi-paragraph theatrical pacing — it stacks with the model's natural sentence pauses and creates dead air.

**Quote framing**
- When the next paragraph is a quote, the prior paragraph should set it up clearly: *"...he gives the mechanism in one cold, clean line."* A clear verbal setup lets the voice land the quote with natural weight.
- Quote paragraphs ideally start with the quote text itself, immediately followed by attribution: *"Safety from external danger, he writes, is the most powerful director of national conduct."*

#### Final sanitization checks
- every line reads as natural spoken text
- paragraph breaks only where they help natural pacing
- the script starts directly with spoken content
- the script ends at the last spoken sentence with no trailing labels

---

## Audio production (after script clears all gates)

Audio is produced with the **ElevenLabs Nate voice** — the warm single-host voice the series has used throughout. Each episode has its own `produce-episode.py` in the episode folder: it chunks the script, renders each chunk through the ElevenLabs API, assembles the chunks with ffmpeg, and embeds ID3 tags + cover art.

Two shared, reusable tools live in `_production/tools/` and are used in QA and repair below (both read their API keys from the project-root `.env`):
- `audio-qa.py` — automated post-render QA: transcribes the finished MP3 with Deepgram and diffs it against the script to catch stutters, doubled words, dropped sections, and dead air. Writes `audio-qa.md`.
- `fix-segment.py` — surgical repair: regenerates a single flagged sentence and splices it in, so a glitch costs a few cents instead of a whole-chunk re-render.

### Step A — Create the episode's production script
Copy the previous episode's `produce-episode.py` into `Federalist paper number N/` and update the episode-specific constants at the top of the file:
- `EPISODE_NUM`
- `EPISODE_TITLE` — the full `Federalist No. N Explained: ...` title
- `EPISODE_COMMENT` — a one-to-two-sentence description for the ID3 comment tag
- `SCRIPT_PATH` and `FINAL_OUTPUT` — the filenames embed the episode number

Everything else is fixed across the series — do not change it without a specific reason:
- Voice: `Nate` (`VOICE_ID = Ifu36BnEjjIY932etsqk`)
- Model: `eleven_multilingual_v2`
- Voice settings: stability 0.42, similarity_boost 0.75, style 0.0, speaker boost on
- Output format: `mp3_44100_192` (requires the ElevenLabs Creator tier or above)
- The ElevenLabs API key is read from `.env` (`eleven-labs-api=`)

### Step B — Render
```bash
python3 "Federalist paper number N/produce-episode.py"
```
- Splits the script into roughly 1800–3200-character chunks on paragraph boundaries
- Renders each chunk via the ElevenLabs API into `audio-chunks/NN.mp3` — chunks are cached, so a chunk that already exists is skipped and partial re-renders are cheap
- Concatenates the chunks with ffmpeg into `audio-chunks/assembled.mp3`
- Embeds ID3 tags + cover art (`Show Art.png`) and writes `federalist-no-N-episode-final.mp3`
- Prints a verification summary (duration, size, bitrate, tags, cover-art check)
- Takes a few minutes for a full episode

### Step C — QA (automated sweep first, then a targeted listen)

**A four-point spot-listen is not enough.** Episode 14 shipped "DONE" with a stuttered "and … and" restart (2.4 seconds of dead air) at the 2:26 mark — none of the old sample points (open / middle / close / one join) would ever have caught it. The fix is to let the machine sweep the whole episode and tell you where to listen.

**1. Run the automated audio QA — required, produces an artifact:**
```bash
python3 _production/tools/audio-qa.py N
```
It transcribes the finished MP3 with **Deepgram** (cheap — this does *not* use ElevenLabs credits), diffs the transcript against the script, and flags the defects an ear skips on a sample listen: a word or short phrase spoken twice that the script has only once (the stutter class), a dropped or garbled section, unnatural dead air, and low-confidence mispronunciations. Because it compares against the actual script, intentional repeats ("small, small enough", "not, not from the center") are **not** flagged. Every HIGH/MEDIUM flag is then confirmed a second, independent way before it is reported — the finished "and … and" case survives; Deepgram's own transcription hiccups do not. It writes `Federalist paper number N/audio-qa.md` and prints the exact timestamps to check.

The report must read **PASS** before the episode is done. If it reads REVIEW, every HIGH must be repaired and every MEDIUM understood and consciously accepted (some MEDIUM dead-air is an intentional dramatic pause — that is fine, but decide it on purpose).

**2. Listen where it points.** Open the flagged timestamps and confirm each, plus a quick sanity listen of the open, one quote transition, and the sign-off. You are confirming specific spots, not hunting blind.

#### If a spot is a real glitch — repair it surgically (cheap)
The stutter / dropped-word class is almost always a few words, not a whole chunk. Regenerate **only** the affected sentence and splice it in — a few cents, not a whole-chunk re-render:
```bash
# 1) dry run (nothing changes): maps the timestamp to its chunk and prints the cut plan
python3 _production/tools/fix-segment.py N --start <glitch_start_s> --end <glitch_end_s> \
    --text "The corrected sentence, using a comma instead of the em-dash that stuttered."
# 2) once the plan looks right, apply it:
python3 _production/tools/fix-segment.py N --start <glitch_start_s> --end <glitch_end_s> --text "..." --apply
```
`fix-segment.py` snaps the cuts to natural pauses, **verifies the freshly generated sentence is clean before it splices anything** (and aborts without touching the episode if it can't get a clean take), backs up the original chunk as `NN.orig.mp3`, rebuilds the episode from the cached chunks (no extra ElevenLabs cost), and re-runs the audio QA automatically. Use a comma or period in the replacement text, not an em-dash — the em-dash is what triggers the stutter.

#### If a whole chunk is wrong (rare — usually a script problem, not a render glitch)
1. Fix the script.
2. Delete that chunk: `command rm "Federalist paper number N/audio-chunks/NN.mp3"`
3. Re-run Step B — only the missing chunk re-renders; all others use cache.
4. Re-run the audio QA (Step C) until it reads PASS.

### Step D — Episode metadata
Write `Federalist paper number N/episode-metadata.md` in this exact format:

```
# Federalist No. {N} Explained: {Punchy Title}

## Episode Description
{Long form. 2 to 4 sentences. Plain English. Walks the listener through what this episode covers and why it matters. No author name in the first words; lead with the idea, not the byline.}

## Short Episode Description
{1 sentence. The single-sentence pitch. A 14-year-old reads it and knows whether they want to listen.}

## Alternate Short Description
{1 sentence. A different angle on the same episode.}
```

Title style:
- Format: `Federalist No. {N} Explained: {Punchy Title}`
- Punchy title: 3–7 short, plain-English words. 14-year-old vocabulary at a glance.
- **Do not** include the author's name in the title (no "Hamilton on..." / "Madison on...").
- **Do not** use elevated vocabulary in the title even if the script uses it.
- Reference style: *"Why These Essays Matter," "Why the Union Matters," "Why Disunion Means War," "What States Would Fight Over."*

That is the entire metadata file. No status field, no runtime target, no production notes, no tags, no gate logs.

### Step E — ID3 tags and cover art
No separate step needed. `produce-episode.py` embeds the ID3 tags and cover art (`Show Art.png`) automatically during Step B, so the `federalist-no-N-episode-final.mp3` it writes is already distribution-ready. Just make sure `EPISODE_TITLE` and `EPISODE_COMMENT` in the production script match `episode-metadata.md`. Verify the result with `ffprobe -i "Federalist paper number N/federalist-no-N-episode-final.mp3" -show_format`.

---

## Final QA checklist
Before calling an episode final, verify:
- [ ] **checked against the fixed gold standard (Episodes 5–6–7)**, not just the previous episode
- [ ] **clears the Gate 3 exegesis test** — the episode's structure does not mirror the paper's paragraph order; transitions are not a "[Author] opens… then says… then turns to…" chain
- [ ] **8 or fewer substantial set-apart quotes; 2–3 story set-pieces present**
- [ ] **3–6 listener-question moments, spread through the body** (not clustered, not absent)
- [ ] **modern parallels woven through the body**, not only in a closing section
- [ ] title and descriptions match the brand system format
- [ ] intro structure is correct for the episode (Episode 1 has the series promise; episodes 2+ have a tight recap of just the previous episode)
- [ ] continuity references to earlier episodes are factually grounded
- [ ] **web fact-check done — `fact-check.md` exists and every claim is ✅ verified or a fairly-hedged ⚠️** (Episode 12 onward)
- [ ] explanations after each quote are simple and accurate
- [ ] no flat lists hiding as run-on sentences
- [ ] every list with a count has explicit ordinals
- [ ] all years and numerals are spelled out
- [ ] no Roman numerals or hyphenated proper nouns
- [ ] runtime in the 25–40 band, ideally the lower-middle; nothing past 38 min without a structural justification
- [ ] **automated audio QA (`audio-qa.py`) reads PASS** — no stutter, doubled word, dropped section, or unexplained dead-air survives; `audio-qa.md` exists and every remaining flag is understood and accepted
- [ ] quotes land with natural weight and a clear verbal setup (verify by spot-listen)
- [ ] inter-paragraph pacing feels human, not robotic
- [ ] final mp3 plays through normally end-to-end
- [ ] `SERIES-STATUS.md` updated to mark episode N as DONE
