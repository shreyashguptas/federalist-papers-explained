#!/usr/bin/env python3
"""
Episode 12 audio production script.
Chunks the script, renders via ElevenLabs API, assembles with ffmpeg, embeds ID3 tags.
"""

import json
import os
import subprocess
import sys
import time
import urllib.request
import urllib.error

VOICE_ID = "Ifu36BnEjjIY932etsqk"  # Nate - Natural, Warm, Podcast Voice
MODEL_ID = "eleven_multilingual_v2"
VOICE_SETTINGS = {
    "stability": 0.42,
    "similarity_boost": 0.75,
    "style": 0.0,
    "use_speaker_boost": True,
}
OUTPUT_FORMAT = "mp3_44100_192"

CHUNK_MIN = 1800
CHUNK_MAX = 2600
CHUNK_HARD_MAX = 3200

EPISODE_NUM = 12
EPISODE_TITLE = "Federalist No. 12 Explained: Where the Money Comes From"
SHOW_TITLE = "The Federalist Papers: Explained"
EPISODE_COMMENT = (
    "Hamilton on why a government can only tax wealth that moves, why a quiet duty on "
    "imported trade is the one tax that actually works — and why only a united America "
    "can collect it without a police state."
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERIES_DIR = os.path.dirname(BASE_DIR)
SCRIPT_PATH = os.path.join(BASE_DIR, "federalist-no-12-script.txt")
CHUNKS_DIR = os.path.join(BASE_DIR, "audio-chunks")
MANIFEST_PATH = os.path.join(CHUNKS_DIR, "manifest.json")
CONCAT_LIST_PATH = os.path.join(CHUNKS_DIR, "concat-list.txt")
ASSEMBLED_PATH = os.path.join(CHUNKS_DIR, "assembled.mp3")
FINAL_OUTPUT = os.path.join(BASE_DIR, "federalist-no-12-episode-final.mp3")
COVER_ART = os.path.join(SERIES_DIR, "Show Art.png")

ENV_PATH = os.path.join(SERIES_DIR, ".env")
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
            chunks.append(current)
            current = para
        elif len(candidate) <= CHUNK_HARD_MAX:
            current = candidate
        else:
            if current:
                chunks.append(current)
            current = para
    if current:
        chunks.append(current)
    return chunks


def render_chunk(chunk_num, text, total):
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
            with urllib.request.urlopen(req, timeout=180) as resp:
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
    with open(CONCAT_LIST_PATH, "w") as f:
        for path in chunk_paths:
            f.write(f"file '{os.path.basename(path)}'\n")

    print("\nAssembling chunks...")
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", CONCAT_LIST_PATH,
        "-c", "copy",
        ASSEMBLED_PATH,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ffmpeg concat error: {result.stderr}")
        sys.exit(1)
    print(f"Assembled: {ASSEMBLED_PATH}")


def tag_and_embed_art():
    print("\nEmbedding ID3 tags and cover art...")
    if not os.path.exists(COVER_ART):
        print(f"WARNING: cover art not found at {COVER_ART}; writing tags only")
        cmd = [
            "ffmpeg", "-y",
            "-i", ASSEMBLED_PATH,
            "-c:a", "copy",
            "-metadata", f"title={EPISODE_TITLE}",
            "-metadata", f"artist={SHOW_TITLE}",
            "-metadata", f"album={SHOW_TITLE}",
            "-metadata", f"album_artist={SHOW_TITLE}",
            "-metadata", f"track={EPISODE_NUM}",
            "-metadata", "genre=Podcast",
            "-metadata", f"comment={EPISODE_COMMENT}",
            "-id3v2_version", "3",
            FINAL_OUTPUT,
        ]
    else:
        cmd = [
            "ffmpeg", "-y",
            "-i", ASSEMBLED_PATH,
            "-i", COVER_ART,
            "-map", "0:a", "-map", "1:0",
            "-c:a", "copy", "-c:v:0", "copy",
            "-metadata", f"title={EPISODE_TITLE}",
            "-metadata", f"artist={SHOW_TITLE}",
            "-metadata", f"album={SHOW_TITLE}",
            "-metadata", f"album_artist={SHOW_TITLE}",
            "-metadata", f"track={EPISODE_NUM}",
            "-metadata", "genre=Podcast",
            "-metadata", f"comment={EPISODE_COMMENT}",
            "-id3v2_version", "3",
            "-disposition:v:0", "attached_pic",
            FINAL_OUTPUT,
        ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ffmpeg tagging error: {result.stderr}")
        sys.exit(1)
    print(f"Tagged: {FINAL_OUTPUT}")


def verify():
    print("\nVerifying final file...")
    cmd = [
        "ffprobe", "-v", "quiet",
        "-print_format", "json",
        "-show_format",
        "-show_streams",
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
    tags = fmt.get("tags", {})
    streams = info.get("streams", [])
    has_art = any(s.get("codec_type") == "video" for s in streams)

    minutes = int(duration // 60)
    seconds = int(duration % 60)
    size_mb = size / (1024 * 1024)

    print(f"  Duration: {minutes}:{seconds:02d}")
    print(f"  Size: {size_mb:.1f} MB")
    print(f"  Bitrate: {bitrate // 1000} kbps")
    print(f"  Title: {tags.get('title', '—')}")
    print(f"  Album: {tags.get('album', '—')}")
    print(f"  Track: {tags.get('track', '—')}")
    print(f"  Cover art embedded: {has_art}")


def main():
    os.makedirs(CHUNKS_DIR, exist_ok=True)

    with open(SCRIPT_PATH) as f:
        script_text = f.read()

    chunks = chunk_script(script_text)
    total_chars = sum(len(c) for c in chunks)

    print(f"Script: {total_chars:,} chars → {len(chunks)} chunks")
    print(f"Chunk sizes: {[len(c) for c in chunks]}")
    print()

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

    print("Rendering chunks via ElevenLabs API...")
    chunk_paths = []
    for i, chunk in enumerate(chunks, 1):
        path = render_chunk(i, chunk, len(chunks))
        chunk_paths.append(path)
        if i < len(chunks):
            time.sleep(1)

    assemble(chunk_paths)
    tag_and_embed_art()
    verify()

    print("\nDone! Episode 12 audio produced.")


if __name__ == "__main__":
    main()
