from fastapi import FastAPI, HTTPException
from utils import get_video_id
from captions import get_youtube_captions
from whisper_transcribe import whisper_transcribe

app = FastAPI(title="YouTube Transcript API")

@app.post("/transcript")
def generate_transcript(payload: dict):
    url = payload.get("url")

    if not url:
        raise HTTPException(status_code=400, detail="URL is required")

    video_id = get_video_id(url)
    if not video_id:
        raise HTTPException(status_code=400, detail="Invalid YouTube URL")

    # 1️⃣ FAST: captions
    captions = get_youtube_captions(video_id)
    if captions:
        return {
            "video_id": video_id,
            "source": "captions",
            "segments": captions
        }

    # 2️⃣ ACCURATE: Whisper
    segments = whisper_transcribe(url)

    return {
        "video_id": video_id,
        "source": "whisper",
        "segments": segments
    }
