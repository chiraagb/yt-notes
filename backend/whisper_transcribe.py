import subprocess
import whisper
import os
import uuid

TMP_DIR = "tmp"
os.makedirs(TMP_DIR, exist_ok=True)

model = whisper.load_model("small")  # best speed/accuracy balance

def whisper_transcribe(youtube_url: str):
    audio_path = f"{TMP_DIR}/{uuid.uuid4()}.wav"

    # Download audio
    subprocess.run(
        [
            "yt-dlp",
            "-x",
            "--audio-format", "wav",
            "-o", audio_path,
            youtube_url
        ],
        check=True
    )

    # Transcribe
    result = model.transcribe(audio_path)

    os.remove(audio_path)

    segments = []
    for seg in result["segments"]:
        segments.append({
            "start": seg["start"],
            "end": seg["end"],
            "text": seg["text"].strip()
        })

    return segments
