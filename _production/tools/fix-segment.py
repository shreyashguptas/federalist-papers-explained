#!/usr/bin/env python3
"""
fix-segment.py — surgical, cheap repair for a single rendered glitch.

When audio-qa.py flags a stutter/dropped word at a timestamp, this regenerates
ONLY the affected sentence through ElevenLabs (a few cents, not a whole chunk),
splices it in at natural pauses, rebuilds the episode, and re-runs audio QA.

It is deliberately careful:
  - It maps the global timestamp to the chunk that contains it and snaps the
    cut points to real silences, so no word gets clipped.
  - It VERIFIES the freshly generated sentence with Deepgram BEFORE splicing —
    the replacement must say the requested words and must not itself contain a
    gapped duplicate. If it can't get a clean take, it aborts without touching
    anything.
  - It defaults to a DRY RUN. Nothing is modified unless you pass --apply.
  - It backs up the original chunk as NN.orig.mp3 before writing.

Usage (dry run first — always):
  python3 fix-segment.py 14 --start 143.3 --end 150.2 \
      --text "The homework guy puts down his notes, and raises his voice."

  # then, once the plan looks right:
  python3 fix-segment.py 14 --start 143.3 --end 150.2 --text "..." --apply

  # provide your own replacement audio instead of generating (skips ElevenLabs):
  python3 fix-segment.py --folder "Episode 14 fixed" --start 143.3 --end 150.2 \
      --replacement-audio some.mp3 --apply

Notes:
  - --start/--end are seconds on the FINAL episode timeline (what audio-qa prints).
  - The region must fall inside a single chunk (glitches always do).
  - Prefer a comma or period over an em-dash in --text: the em-dash is what
    triggers the stutter class in the first place. The spoken words are identical.
"""

import argparse
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import urllib.error

VOICE_ID = "Ifu36BnEjjIY932etsqk"      # Nate (fixed across the series)
MODEL_ID = "eleven_multilingual_v2"
VOICE_SETTINGS = {"stability": 0.42, "similarity_boost": 0.75, "style": 0.0,
                  "use_speaker_boost": True}
OUTPUT_FORMAT = "mp3_44100_192"

TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
SERIES_DIR = os.path.dirname(os.path.dirname(TOOL_DIR))
FFMPEG = shutil.which("ffmpeg") or "/opt/homebrew/bin/ffmpeg"
FFPROBE = shutil.which("ffprobe") or "/opt/homebrew/bin/ffprobe"


def load_key(name):
    with open(os.path.join(SERIES_DIR, ".env")) as f:
        for line in f:
            line = line.strip()
            if line.startswith(name + "="):
                return line.split("=", 1)[1].strip()
    sys.exit(f"ERROR: {name} not found in .env")


def norm(t):
    return re.sub(r"[^a-z0-9]", "", t.lower())


def tokenize(s):
    return [norm(t) for t in re.split(r"[^A-Za-z0-9]+", s) if norm(t)]


def probe_dur(path):
    r = subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=noprint_wrappers=1:nokey=1", path],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


def silences(path, noise="-30dB", d="0.20"):
    r = subprocess.run([FFMPEG, "-hide_banner", "-i", path, "-af",
                        f"silencedetect=noise={noise}:d={d}", "-f", "null", "-"],
                       capture_output=True, text=True)
    out = []
    start = None
    for line in r.stderr.splitlines():
        m = re.search(r"silence_start:\s*([0-9.]+)", line)
        if m:
            start = float(m.group(1))
        m = re.search(r"silence_end:\s*([0-9.]+)", line)
        if m and start is not None:
            out.append((start, float(m.group(1))))
            start = None
    return out


def deepgram_words(path, key):
    with open(path, "rb") as f:
        data = f.read()
    req = urllib.request.Request(
        "https://api.deepgram.com/v1/listen?model=nova-2&smart_format=true&punctuate=true",
        data=data, headers={"Authorization": "Token " + key, "Content-Type": "audio/mpeg"},
        method="POST")
    with urllib.request.urlopen(req, timeout=180) as resp:
        out = json.loads(resp.read())
    return out["results"]["channels"][0]["alternatives"][0]["words"]


def elevenlabs_tts(text, key, out_path):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}?output_format={OUTPUT_FORMAT}"
    payload = json.dumps({"text": text, "model_id": MODEL_ID,
                          "voice_settings": VOICE_SETTINGS}).encode()
    req = urllib.request.Request(url, data=payload,
                                 headers={"xi-api-key": key, "Content-Type": "application/json",
                                          "Accept": "audio/mpeg"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            audio = resp.read()
    except urllib.error.HTTPError as e:
        sys.exit(f"ERROR: ElevenLabs {e.code}: {e.read()[:300]!r}")
    with open(out_path, "wb") as f:
        f.write(audio)


def clip_is_clean(path, want_text, dg_key):
    """True if the clip says the requested words and has no gapped duplicate."""
    words = deepgram_words(path, dg_key)
    heard = [norm(w["word"]) for w in words]
    want = tokenize(want_text)
    coverage = sum(1 for t in set(want) if t in set(heard)) / max(1, len(set(want)))
    for i in range(1, len(words)):
        if heard[i - 1] and heard[i - 1] == heard[i]:
            gap = words[i]["start"] - words[i - 1]["end"]
            if gap >= 0.30:
                return False, f"replacement itself stutters ('{heard[i]}' with {gap:.1f}s gap)"
    if coverage < 0.8:
        return False, f"replacement only covers {coverage*100:.0f}% of requested words"
    return True, f"clean ({coverage*100:.0f}% word coverage, no gapped repeats)"


def resolve_folder(args):
    folder = args.folder
    if folder is None and args.episode is not None:
        folder = os.path.join(SERIES_DIR, f"Federalist paper number {args.episode}")
    if folder and not os.path.isabs(folder):
        folder = os.path.join(SERIES_DIR, folder)
    if not folder or not os.path.isdir(folder):
        sys.exit(f"ERROR: folder not found: {folder}")
    chunks = os.path.join(folder, "audio-chunks")
    produce = glob.glob(os.path.join(folder, "produce-episode.py"))
    if not produce:
        sys.exit(f"ERROR: produce-episode.py not found in {folder}")
    return folder, chunks, produce[0]


def main():
    ap = argparse.ArgumentParser(description="Surgical single-sentence audio repair.")
    ap.add_argument("episode", nargs="?", type=int)
    ap.add_argument("--folder")
    ap.add_argument("--start", type=float, required=True, help="glitch start (s, final timeline)")
    ap.add_argument("--end", type=float, required=True, help="glitch end (s, final timeline)")
    ap.add_argument("--text", help="replacement sentence to regenerate")
    ap.add_argument("--replacement-audio", help="use this mp3 instead of generating")
    ap.add_argument("--cut-start", type=float, help="override snap: local cut start (s in chunk)")
    ap.add_argument("--cut-end", type=float, help="override snap: local cut end (s in chunk)")
    ap.add_argument("--apply", action="store_true", help="actually modify (default: dry run)")
    ap.add_argument("--force", action="store_true", help="overwrite an existing .orig backup")
    args = ap.parse_args()

    if not args.text and not args.replacement_audio:
        sys.exit("ERROR: pass --text (to generate) or --replacement-audio (to reuse a clip).")

    folder, chunks_dir, produce = resolve_folder(args)
    chunk_paths = sorted(glob.glob(os.path.join(chunks_dir, "[0-9][0-9].mp3")))
    if not chunk_paths:
        sys.exit(f"ERROR: no NN.mp3 chunks in {chunks_dir}")

    # map global start/end -> chunk + local times
    durs = [probe_dur(p) for p in chunk_paths]
    bounds, acc = [], 0.0
    for d in durs:
        bounds.append((acc, acc + d))
        acc += d
    def chunk_of(t):
        for i, (lo, hi) in enumerate(bounds):
            if lo <= t < hi:
                return i
        return len(bounds) - 1
    ci_s, ci_e = chunk_of(args.start), chunk_of(args.end)
    if ci_s != ci_e:
        sys.exit(f"ERROR: region spans chunks {ci_s+1:02d}->{ci_e+1:02d}; narrow it to one chunk.")
    ci = ci_s
    chunk = chunk_paths[ci]
    lo, hi = bounds[ci]
    local_s, local_e = args.start - lo, args.end - lo
    cdur = durs[ci]

    # snap cut points to real silences in the chunk
    sils = silences(chunk)
    def snap(target, prefer_before):
        cands = [(abs(((a + b) / 2) - target), (a + b) / 2) for a, b in sils]
        if not cands:
            return None
        cands.sort()
        return cands[0][1]
    cut_start = args.cut_start if args.cut_start is not None else snap(local_s, True)
    if args.cut_end is not None:
        cut_end = args.cut_end
    elif local_e >= cdur - 0.6:
        cut_end = cdur                       # region is the tail of the chunk
    else:
        cut_end = snap(local_e, False)
    if cut_start is None or cut_end is None:
        sys.exit("ERROR: could not find silences to snap to; pass --cut-start/--cut-end.")

    print(f"Chunk {ci+1:02d} ({os.path.basename(chunk)}), chunk length {cdur:.2f}s")
    print(f"Glitch (final timeline): {args.start:.2f}-{args.end:.2f}s  ->  "
          f"local {local_s:.2f}-{local_e:.2f}s")
    print(f"Cut plan: head [0, {cut_start:.2f}]  +  replacement  +  "
          f"tail [{cut_end:.2f}, {cdur:.2f}]"
          + ("  (tail empty)" if cut_end >= cdur - 0.01 else ""))
    if args.text:
        print(f"Replacement: GENERATE {len(args.text)} chars via ElevenLabs Nate")
        print(f"  text: {args.text!r}")
    else:
        print(f"Replacement: reuse audio {args.replacement_audio}")

    if not args.apply:
        print("\nDRY RUN — nothing changed. Re-run with --apply to perform the repair.")
        return

    work = tempfile.mkdtemp(prefix="fixseg_")
    dg_key = load_key("deepgram-api")

    # produce the replacement clip
    repl = os.path.join(work, "repl.mp3")
    if args.text:
        el_key = load_key("eleven-labs-api")
        ok = False
        for attempt in range(2):
            elevenlabs_tts(args.text, el_key, repl)
            clean, why = clip_is_clean(repl, args.text, dg_key)
            print(f"  generate attempt {attempt+1}: {why}")
            if clean:
                ok = True
                break
        if not ok:
            sys.exit("ABORT: could not get a clean replacement take; nothing changed.")
    else:
        src = args.replacement_audio
        if not os.path.isabs(src):
            src = os.path.join(folder, src)
        shutil.copy(src, repl)
        clean, why = clip_is_clean(repl, args.text or "", dg_key) if args.text else (True, "not verified (provided audio)")
        print(f"  replacement: {why}")

    # cut head/tail (copy — no re-encode)
    head = os.path.join(work, "head.mp3")
    subprocess.run([FFMPEG, "-v", "error", "-y", "-t", f"{cut_start:.3f}", "-i", chunk,
                    "-c", "copy", head], check=True)
    parts = [head, repl]
    if cut_end < cdur - 0.01:
        tail = os.path.join(work, "tail.mp3")
        subprocess.run([FFMPEG, "-v", "error", "-y", "-ss", f"{cut_end:.3f}", "-i", chunk,
                        "-c", "copy", tail], check=True)
        parts.append(tail)

    listf = os.path.join(work, "list.txt")
    with open(listf, "w") as f:
        for p in parts:
            f.write(f"file '{p}'\n")

    # back up and write new chunk
    backup = chunk[:-4] + ".orig.mp3"
    if os.path.exists(backup) and not args.force:
        sys.exit(f"ABORT: backup already exists ({backup}); pass --force to overwrite.")
    shutil.copy(chunk, backup)
    subprocess.run([FFMPEG, "-v", "error", "-y", "-f", "concat", "-safe", "0",
                    "-i", listf, "-c", "copy", chunk], check=True)
    print(f"  wrote new {os.path.basename(chunk)} (original backed up to {os.path.basename(backup)})")

    # rebuild episode (chunks cached -> no ElevenLabs cost) and re-run QA
    print("\nRebuilding episode...")
    subprocess.run([sys.executable, produce], check=True)
    print("\nRe-running audio QA...")
    subprocess.run([sys.executable, os.path.join(TOOL_DIR, "audio-qa.py"),
                    "--folder", folder, "--refresh"])


if __name__ == "__main__":
    main()
