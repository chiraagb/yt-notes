from urllib.parse import urlparse, parse_qs

def get_video_id(url: str) -> str:
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)
    return qs.get("v", [None])[0]
