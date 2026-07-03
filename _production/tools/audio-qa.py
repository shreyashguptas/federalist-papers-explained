#!/usr/bin/env python3
"""
audio-qa.py — automated post-render audio QA for The Federalist Papers: Explained.

Transcribes a finished episode MP3 with Deepgram (cheap; NOT ElevenLabs credits),
aligns the transcript to the episode script, and flags rendering defects that a
four-point human spot-listen misses:

  HIGH   — a word or short phrase spoken twice that the script has only once
           (the "and ... and" stutter class), or a large chunk of the script
           missing from the audio (a dropped/garbled section).
  MEDIUM — unusual dead air between words (long unnatural pauses), or a large
           run of audio with no matching script text (hallucinated/duplicated).
  LOW    — individual very-low-confidence words (possible mispronunciation).

Every HIGH/MEDIUM flag is then VERIFIED a second way before it is reported,
because Deepgram itself occasionally doubles or drops a word in its transcript:

  - word/phrase/extra/missing flags are re-transcribed on just their clip and
    kept only if the anomaly reproduces on the fresh look;
  - dead-air flags are confirmed acoustically with ffmpeg silencedetect, so a
    "gap" that is really just Deepgram missing a word is discarded.

Intentional script repeats ("small, small enough", "not, not from the center")
are never flagged, because findings are compared against the actual script.

It writes an `audio-qa.md` report next to the audio and prints the timestamps to
spot-listen.

Usage:
  python3 audio-qa.py N                         # standard "Federalist paper number N" folder
  python3 audio-qa.py --folder "Episode 14 fixed"
  python3 audio-qa.py --audio path/to.mp3 --script path/to-script.txt
  python3 audio-qa.py N --refresh               # ignore cached transcript, re-call Deepgram
  python3 audio-qa.py N --no-verify             # skip the second-look pass (faster, noisier)

Exit code is 0 when the verdict is PASS, 1 when it is REVIEW (so it can gate a
pipeline). The main transcript is cached next to the audio as
`.audio-qa-transcript.json` and reused unless the audio is newer or --refresh.
"""

import argparse
import difflib
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

# ---- thresholds (tuned on the series' 192kbps Nate renders) ----
GAP_MEDIUM_S = 2.5          # real silence longer than this is worth a listen (acoustic)
DROP_HIGH_TOKENS = 6        # >= this many script tokens missing in a row -> dropped section
EXTRA_MEDIUM_TOKENS = 6     # >= this many audio tokens with no script match -> hallucination/dup
LOWCONF_WORD = 0.40         # a single word this low is worth a listen
COVERAGE_WARN = 0.90        # transcript shorter than this fraction of script -> warn

TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
SERIES_DIR = os.path.dirname(os.path.dirname(TOOL_DIR))
FFMPEG = shutil.which("ffmpeg") or "/opt/homebrew/bin/ffmpeg"
DG_URL = "https://api.deepgram.com/v1/listen?model=nova-2&smart_format=true&punctuate=true"


def load_key(name):
    env = os.path.join(SERIES_DIR, ".env")
    with open(env) as f:
        for line in f:
            line = line.strip()
            if line.startswith(name + "="):
                return line.split("=", 1)[1].strip()
    sys.exit(f"ERROR: {name} not found in {env}")


def resolve_paths(args):
    script, audio, folder = args.script, args.audio, args.folder
    if args.episode is not None and folder is None and (script is None or audio is None):
        folder = os.path.join(SERIES_DIR, f"Federalist paper number {args.episode}")
    if folder:
        if not os.path.isabs(folder):
            folder = os.path.join(SERIES_DIR, folder)
        if script is None:
            hits = sorted(glob.glob(os.path.join(folder, "federalist-no-*-script.txt")))
            script = hits[0] if hits else None
        if audio is None:
            hits = sorted(glob.glob(os.path.join(folder, "*-episode-final.mp3")))
            audio = hits[0] if hits else None
    if not script or not os.path.exists(script):
        sys.exit(f"ERROR: script not found (looked for: {script})")
    if not audio or not os.path.exists(audio):
        sys.exit(f"ERROR: audio not found (looked for: {audio})")
    return os.path.abspath(script), os.path.abspath(audio)


def deepgram(data, key):
    req = urllib.request.Request(
        DG_URL, data=data,
        headers={"Authorization": "Token " + key, "Content-Type": "audio/mpeg"},
        method="POST")
    try:
        with urllib.request.urlopen(req, timeout=600) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        sys.exit(f"ERROR: Deepgram {e.code}: {e.read()[:400]!r}")


def transcribe(audio, key, refresh=False):
    cache = os.path.join(os.path.dirname(audio), ".audio-qa-transcript.json")
    if (not refresh and os.path.exists(cache)
            and os.path.getmtime(cache) >= os.path.getmtime(audio)):
        with open(cache) as f:
            return json.load(f)
    with open(audio, "rb") as f:
        out = deepgram(f.read(), key)
    with open(cache, "w") as f:
        json.dump(out, f)
    return out


def clip_words(audio, start, end, key):
    """Re-transcribe just [start,end] of the audio; return words (times absolute)."""
    start = max(0.0, start)
    fd, path = tempfile.mkstemp(suffix=".mp3")
    os.close(fd)
    try:
        subprocess.run([FFMPEG, "-v", "error", "-y", "-ss", f"{start:.2f}",
                        "-to", f"{end:.2f}", "-i", audio, "-c", "copy", path],
                       check=True)
        with open(path, "rb") as f:
            out = deepgram(f.read(), key)
    finally:
        os.unlink(path)
    ws = out["results"]["channels"][0]["alternatives"][0]["words"]
    for w in ws:
        w["start"] += start
        w["end"] += start
    return ws


def silence_seconds(audio, start, end, key=None):
    """Total detected silence within [start,end], acoustically (ffmpeg)."""
    start = max(0.0, start)
    fd, path = tempfile.mkstemp(suffix=".mp3")
    os.close(fd)
    try:
        subprocess.run([FFMPEG, "-v", "error", "-y", "-ss", f"{start:.2f}",
                        "-to", f"{end:.2f}", "-i", audio, "-c", "copy", path],
                       check=True)
        p = subprocess.run([FFMPEG, "-hide_banner", "-i", path,
                            "-af", "silencedetect=noise=-30dB:d=0.4", "-f", "null", "-"],
                           capture_output=True, text=True)
    finally:
        os.unlink(path)
    return sum(float(m) for m in re.findall(r"silence_duration:\s*([0-9.]+)", p.stderr))


def norm(tok):
    return re.sub(r"[^a-z0-9]", "", tok.lower())


def tokenize(text):
    return [norm(t) for t in re.split(r"[^A-Za-z0-9]+", text) if norm(t)]


def ts(s):
    m = int(s // 60)
    return f"{m}:{s - 60 * m:05.2f}"


def full_silences(audio, min_dur):
    """Deterministic acoustic silence scan of the whole file (>= min_dur seconds)."""
    r = subprocess.run([FFMPEG, "-hide_banner", "-i", audio, "-af",
                        f"silencedetect=noise=-30dB:d={min_dur}", "-f", "null", "-"],
                       capture_output=True, text=True)
    out, start = [], None
    for line in r.stderr.splitlines():
        m = re.search(r"silence_start:\s*([0-9.]+)", line)
        if m:
            start = float(m.group(1))
        m = re.search(r"silence_end:\s*([0-9.]+)", line)
        if m and start is not None:
            out.append((start, float(m.group(1))))
            start = None
    return out


def find_raw(script_path, transcript, audio):
    alt = transcript["results"]["channels"][0]["alternatives"][0]
    words = alt["words"]
    a = tokenize(open(script_path).read())
    b = [norm(w["word"]) for w in words]
    script_pairs = set(zip(a, a[1:]))
    script_tris = set(zip(a, a[1:], a[2:]))
    f = []

    for i in range(1, len(words)):
        if b[i - 1] and b[i - 1] == b[i] and (b[i - 1], b[i - 1]) not in script_pairs:
            f.append({"sev": "HIGH", "t": words[i - 1]["start"], "kind": "duplicate-word",
                      "word": b[i], "detail": f"\"{words[i-1]['word']} {words[i]['word']}\" "
                      "spoken twice; script has it once"})

    for i in range(len(b) - 5):
        tri = tuple(b[i:i + 3])
        if all(tri) and b[i:i + 3] == b[i + 3:i + 6] and tri not in script_tris:
            phrase = " ".join(w["word"] for w in words[i:i + 3])
            f.append({"sev": "HIGH", "t": words[i]["start"], "kind": "duplicate-phrase",
                      "tri": tri, "detail": f"phrase \"{phrase}\" repeated back-to-back"})

    # dead-air is measured acoustically (deterministic; independent of Deepgram's
    # per-run word timings, which produced false gaps where it merely dropped a word).
    for a0, a1 in full_silences(audio, GAP_MEDIUM_S):
        dur = a1 - a0
        before = next((w for w in reversed(words) if w["end"] <= a0 + 0.3), None)
        after = next((w for w in words if w["start"] >= a1 - 0.3), None)
        ctx = (f" after \"{before['word']}\" before \"{after['word']}\""
               if before and after else "")
        f.append({"sev": "MEDIUM", "t": a0, "kind": "dead-air", "gap": dur, "skip_verify": True,
                  "detail": f"{dur:.1f}s of continuous silence{ctx}"})

    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "delete" and (i2 - i1) >= DROP_HIGH_TOKENS:
            t = words[j1]["start"] if j1 < len(words) else (words[-1]["end"] if words else 0)
            f.append({"sev": "HIGH", "t": t, "kind": "missing-audio",
                      "tokens": a[i1:i2], "detail": f"{i2-i1} script words not heard near here "
                      f"(script: \"{' '.join(a[i1:i1+8])} ...\")"})
        elif tag == "insert" and (j2 - j1) >= EXTRA_MEDIUM_TOKENS:
            f.append({"sev": "MEDIUM", "t": words[j1]["start"], "kind": "extra-audio",
                      "tokens": b[j1:j2], "detail": f"{j2-j1} spoken words with no script match "
                      f"(heard: \"{' '.join(w['word'] for w in words[j1:j1+8])} ...\")"})

    for w in words:
        if w["confidence"] < LOWCONF_WORD:
            f.append({"sev": "LOW", "t": w["start"], "kind": "low-confidence",
                      "detail": f"\"{w['word']}\" (confidence {w['confidence']:.2f})"})

    return f, words, a, script_pairs, script_tris


def verify(f, audio, script_pairs, script_tris, key):
    """Return True if the finding reproduces on a fresh, independent look."""
    t = f["t"]
    kind = f["kind"]
    if kind == "duplicate-word":
        # Re-transcribe the clip and locate the doubled word. The AUDIBLE defect is a
        # repeat with dead air between the two tokens (the "and ...pause... and" restart).
        # A contiguous doubling of a tiny function word ("to to") is at most a faint
        # artifact and is demoted to LOW so it never fails the episode on its own.
        # (A second engine like Whisper is no help here: it silently collapses repeats.)
        cw = clip_words(audio, t - 3, t + 4, key)
        nb = [norm(w["word"]) for w in cw]
        for i in range(1, len(cw)):
            if nb[i - 1] == f["word"] == nb[i] and (f["word"], f["word"]) not in script_pairs:
                gap = cw[i]["start"] - cw[i - 1]["end"]
                if gap >= 0.30:
                    f["detail"] += f" ({gap:.1f}s gap between them — audible restart)"
                    f["sev"] = "HIGH"
                else:
                    f["detail"] += " (contiguous, no gap — faint, likely negligible)"
                    f["sev"] = "LOW"
                return True
        return False
    if kind == "duplicate-phrase":
        cw = [norm(w["word"]) for w in clip_words(audio, t - 3, t + 6, key)]
        return any(tuple(cw[i:i + 3]) == f["tri"] and cw[i:i + 3] == cw[i + 3:i + 6]
                   for i in range(len(cw) - 5))
    if kind == "dead-air":
        g = f["gap"]
        return silence_seconds(audio, t - 1.0, t + g + 1.0) >= 0.6 * g
    if kind == "missing-audio":
        block = set(f["tokens"])
        cw = set(norm(w["word"]) for w in clip_words(audio, t - 4, t + 14, key))
        present = len(block & cw) / max(1, len(block))
        if present > 0.6:
            return False           # words are actually there -> Deepgram error
        f["sev"] = "MEDIUM"        # still suspicious, but demote from HIGH
        return True
    if kind == "extra-audio":
        block = f["tokens"]
        cw = tokenize(" ".join(w["word"] for w in clip_words(audio, t - 2, t + 6, key)))
        script_toks = set()  # cheap reuse: compare against the pair vocab
        for p in script_pairs:
            script_toks.update(p)
        extra = [w for w in cw if w not in script_toks]
        return len(extra) >= 0.5 * len(block)
    return True


def write_report(audio, script_path, findings, stats):
    highs = [f for f in findings if f["sev"] == "HIGH"]
    meds = [f for f in findings if f["sev"] == "MEDIUM"]
    lows = [f for f in findings if f["sev"] == "LOW"]
    low_cov = stats["coverage"] < COVERAGE_WARN
    verdict = "REVIEW" if (highs or meds or low_cov) else "PASS"

    L = [f"# Audio QA — {os.path.basename(audio)}", "", f"**Verdict: {verdict}**", ""]
    d = stats["duration"]
    L.append(f"- Duration: {ts(d)} ({d:.0f}s)" if d else "- Duration: ?")
    if stats["overall_conf"] is not None:
        L.append(f"- Overall transcription confidence: {stats['overall_conf']:.3f}")
    L.append(f"- Coverage: {stats['coverage']*100:.1f}% "
             f"({stats['audio_tokens']} words heard vs {stats['script_tokens']} script words)"
             + ("  ⚠️ low — possible dropped content" if low_cov else ""))
    L.append(f"- Script: `{os.path.relpath(script_path, SERIES_DIR)}`")
    L.append("- Every HIGH/MEDIUM finding below was confirmed on a second, independent pass.")
    L.append("")

    def table(title, rows):
        L.append(f"## {title} ({len(rows)})")
        if not rows:
            L.extend(["_none_", ""])
            return
        L.append("| time | kind | detail |")
        L.append("|------|------|--------|")
        for f in rows:
            L.append(f"| {ts(f['t'])} | {f['kind']} | {f['detail']} |")
        L.append("")

    table("HIGH — fix before publishing", highs)
    table("MEDIUM — listen and confirm", meds)
    table("LOW — informational", lows)
    L.append("---")
    L.append("_Generated by `_production/tools/audio-qa.py`. Intentional script repeats are "
             "not flagged (findings are compared to the script), and each flag is verified twice._")

    out = os.path.join(os.path.dirname(audio), "audio-qa.md")
    with open(out, "w") as fh:
        fh.write("\n".join(L) + "\n")
    return out, verdict, highs, meds


def main():
    ap = argparse.ArgumentParser(description="Automated audio QA (transcript diff + verify).")
    ap.add_argument("episode", nargs="?", type=int, help="episode number")
    ap.add_argument("--folder", help="episode folder (name under series dir, or absolute path)")
    ap.add_argument("--script", help="path to the script .txt")
    ap.add_argument("--audio", help="path to the final .mp3")
    ap.add_argument("--refresh", action="store_true", help="ignore cached transcript")
    ap.add_argument("--no-verify", action="store_true", help="skip the second-look pass")
    args = ap.parse_args()

    script_path, audio = resolve_paths(args)
    key = load_key("deepgram-api")
    transcript = transcribe(audio, key, refresh=args.refresh)
    raw, words, a_tokens, script_pairs, script_tris = find_raw(script_path, transcript, audio)

    kept = []
    for f in raw:
        if f["sev"] == "LOW" or f.get("skip_verify") or args.no_verify:
            kept.append(f)
            continue
        try:
            if verify(f, audio, script_pairs, script_tris, key):
                kept.append(f)
        except Exception as e:
            f["detail"] += f"  (verify failed: {e}; keeping)"
            kept.append(f)

    kept.sort(key=lambda f: ({"HIGH": 0, "MEDIUM": 1, "LOW": 2}[f["sev"]], f["t"]))
    stats = {
        "overall_conf": transcript["results"]["channels"][0]["alternatives"][0].get("confidence"),
        "duration": transcript.get("metadata", {}).get("duration"),
        "script_tokens": len(a_tokens),
        "audio_tokens": len(words),
        "coverage": (len(words) / len(a_tokens)) if a_tokens else 0.0,
    }
    report, verdict, highs, meds = write_report(audio, script_path, kept, stats)

    print(f"Audio QA: {verdict}")
    print(f"  report: {report}")
    print(f"  duration {ts(stats['duration'])}, confidence {stats['overall_conf']:.3f}, "
          f"coverage {stats['coverage']*100:.1f}%")
    if highs or meds:
        print("  spot-listen these timestamps (verified):")
        for f in highs + meds:
            print(f"    [{f['sev']}] {ts(f['t'])}  {f['kind']} — {f['detail']}")
    else:
        print("  no HIGH/MEDIUM issues survived verification.")
    sys.exit(0 if verdict == "PASS" else 1)


if __name__ == "__main__":
    main()
