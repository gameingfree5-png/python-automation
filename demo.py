"""Refresh demo status and a public sample video playlist."""

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path


def main():
    now = datetime.now(timezone.utc)
    india = timezone(timedelta(hours=5, minutes=30))
    folder = Path(__file__).resolve().parent
    playlist = [{
        "title": "Sintel - Trailer (public sample)",
        "page_url": "https://www.sintel.org/",
        "stream_url": "https://media.w3.org/2010/05/sintel/trailer.mp4",
        "thumbnail": "",
        "group": "Demo Samples",
        "updated_at": now.isoformat(timespec="seconds"),
    }]
    status = {
        "message": "Demo playlist refreshed successfully!",
        "last_updated_utc": now.isoformat(timespec="seconds"),
        "last_updated_ist": now.astimezone(india).isoformat(timespec="seconds"),
        "refresh_interval_hours": 5,
        "playlist_file": "playlist.json",
        "playlist_entries": len(playlist),
    }
    for filename, data in [("playlist.json", playlist), ("demo-status.json", status)]:
        output = folder / filename
        output.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        print(f"Saved {filename}")
    print(json.dumps(status, indent=2))


if __name__ == "__main__":
    main()
