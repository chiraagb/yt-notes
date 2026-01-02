import requests
import xml.etree.ElementTree as ET

def get_youtube_captions(video_id: str):
    url = f"https://video.google.com/timedtext?lang=en&v={video_id}"
    res = requests.get(url, timeout=10)

    if res.status_code != 200 or not res.text.strip():
        return None

    root = ET.fromstring(res.text)
    segments = []

    for node in root.findall("text"):
        start = float(node.attrib.get("start", 0))
        dur = float(node.attrib.get("dur", 0))
        text = (node.text or "").replace("\n", " ").strip()

        if text:
            segments.append({
                "start": start,
                "end": start + dur,
                "text": text
            })

    return segments if segments else None
