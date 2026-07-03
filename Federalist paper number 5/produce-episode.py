#!/usr/bin/env python3
"""
Episode 5 audio production script.
Chunks the script, renders via ElevenLabs API, assembles with ffmpeg.
"""

import json
import os
import subprocess
import sys
import time
import urllib.request
import urllib.error

# ── Configuration (from production notes) ──────────────────────────
VOICE_ID = "Ifu36BnEjjIY932etsqk"  # Nate - Natural, Warm, Podcast Voice
MODEL_ID = "eleven_multilingual_v2"
VOICE_SETTINGS = {
    "stability": 0.42,
    "similarity_boost": 0.75,
    "style": 0.0,
    "use_speaker_boost": True,
}
SPEED = 1.0
OUTPUT_FORMAT = "mp3_44100_192"  # 192 kbps MP3

# Chunk target: 1800-2600 chars, split at paragraph boundaries
CHUNK_MIN = 1800
CHUNK_MAX = 2600
CHUNK_HARD_MAX = 3200  # allow slightly larger to avoid splitting mid-thought

# ── Paths ──────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.join(BASE_DIR, "federalist-no-5-script.txt")
CHUNKS_DIR = os.path.join(BASE_DIR, "audio-chunks")
MANIFEST_PATH = os.path.join(CHUNKS_DIR, "manifest.json")
CONCAT_LIST_PATH = os.path.join(CHUNKS_DIR, "concat-list.txt")
FINAL_OUTPUT = os.path.join(BASE_DIR, "federalist-no-5-episode-final.mp3")

# ── Read API key ───────────────────────────────────────────────────
ENV_PATH = os.path.join(BASE_DIR, ".env")
if not os.path.exists(ENV_PATH):
    ENV_PATH = os.path.join(os.path.dirname(BASE_DIR), ".env")

API_KEY = None
with open(ENV_PATH) as f:
    for line in f:
        line = line.strip()
        if line.startswith("eleven-labs-api="):
            API_KEY = line.split("=", 1)[1]
            break

if not API_KEY:
    print("ERROR: Could not find eleven-labs-api in .env")
    sys.exit(1)


def chunk_script(text):
    """Split script into chunks at paragraph boundaries, targeting CHUNK_MIN-CHUNK_MAX chars."""
    paragraphs = text.strip().split("\n\n")
    chunks = []
    current = ""

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue

        candidate = (current + "\n\n" + para).strip() if current else para

        if len(candidate) <= CHUNK_MAX:
            current = candidate
        elif len(current) >= CHUNK_MIN:
            # Current chunk is big enough, save it and start new
            chunks.append(current)
            current = para
        elif len(candidate) <= CHUNK_HARD_MAX:
            # Allow slightly over max to keep meaning together
            current = candidate
        else:
            # Must split: save current and start new
            if current:
                chunks.append(current)
            current = para

    if current:
        chunks.append(current)

    return chunks


def render_chunk(chunk_num, text, total):
    """Render a single chunk via ElevenLabs TTS API."""
    output_path = os.path.join(CHUNKS_DIR, f"{chunk_num:02d}.mp3")

    if os.path.exists(output_path) and os.path.getsize(output_path) > 1000:
        print(f"  Chunk {chunk_num:02d}/{total} — already exists, skipping")
        return output_path

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}?output_format={OUTPUT_FORMAT}"

    payload = json.dumps({
        "text": text,
        "model_id": MODEL_ID,
        "voice_settings": VOICE_SETTINGS,
    }).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "xi-api-key": API_KEY,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
        },
        method="POST",
    )

    max_retries = 3
    for attempt in range(max_retries):
        try:
            print(f"  Chunk {chunk_num:02d}/{total} — rendering ({len(text)} chars)...", end="", flush=True)
            with urllib.request.urlopen(req, timeout=120) as resp:
                audio_data = resp.read()
                with open(output_path, "wb") as f:
                    f.write(audio_data)
                print(f" done ({len(audio_data):,} bytes)")
                return output_path
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")
            print(f" HTTP {e.code}: {body}")
            if e.code == 429 and attempt < max_retries - 1:
                wait = 30 * (attempt + 1)
                print(f"  Rate limited, waiting {wait}s...")
                time.sleep(wait)
            elif attempt < max_retries - 1:
                time.sleep(5)
            else:
                print(f"  FAILED after {max_retries} attempts")
                sys.exit(1)
        except Exception as e:
            print(f" error: {e}")
            if attempt < max_retries - 1:
                time.sleep(5)
            else:
                print(f"  FAILED after {max_retries} attempts")
                sys.exit(1)


def assemble(chunk_paths):
    """Assemble chunks into final MP3 using ffmpeg concat."""
    # Write concat list
    with open(CONCAT_LIST_PATH, "w") as f:
        for path in chunk_paths:
            f.write(f"file '{os.path.basename(path)}'\n")

    print("\nAssembling final MP3...")
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", CONCAT_LIST_PATH,
        "-c", "copy",
        FINAL_OUTPUT,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ffmpeg error: {result.stderr}")
        sys.exit(1)
    print(f"Assembled: {FINAL_OUTPUT}")


def verify():
    """Verify final file with ffprobe."""
    print("\nVerifying final file...")
    cmd = [
        "ffprobe", "-v", "quiet",
        "-print_format", "json",
        "-show_format",
        FINAL_OUTPUT,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ffprobe error: {result.stderr}")
        return

    info = json.loads(result.stdout)
    fmt = info.get("format", {})
    duration = float(fmt.get("duration", 0))
    size = int(fmt.get("size", 0))
    bitrate = int(fmt.get("bit_rate", 0))

    minutes = int(duration // 60)
    seconds = int(duration % 60)
    size_mb = size / (1024 * 1024)

    print(f"  Duration: {minutes}:{seconds:02d}")
    print(f"  Size: {size_mb:.1f} MB")
    print(f"  Bitrate: {bitrate // 1000} kbps")
    print(f"  Format: {fmt.get('format_long_name', 'unknown')}")


def main():
    os.makedirs(CHUNKS_DIR, exist_ok=True)

    # Read script
    with open(SCRIPT_PATH) as f:
        script_text = f.read()

    # Chunk
    chunks = chunk_script(script_text)
    total_chars = sum(len(c) for c in chunks)

    print(f"Script: {total_chars:,} chars → {len(chunks)} chunks")
    print(f"Chunk sizes: {[len(c) for c in chunks]}")
    print()

    # Save manifest
    manifest = []
    for i, chunk in enumerate(chunks, 1):
        first_line = chunk.split("\n")[0][:80]
        manifest.append({
            "chunk": i,
            "chars": len(chunk),
            "preview": first_line,
        })
    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)

    # Render each chunk
    print("Rendering chunks via ElevenLabs API...")
    chunk_paths = []
    for i, chunk in enumerate(chunks, 1):
        path = render_chunk(i, chunk, len(chunks))
        chunk_paths.append(path)
        # Small delay between API calls to be respectful
        if i < len(chunks):
            time.sleep(1)

    # Assemble
    assemble(chunk_paths)

    # Verify
    verify()

    print("\nDone! Episode 5 audio produced.")


if __name__ == "__main__":
    main()
