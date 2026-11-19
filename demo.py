"""Refresh a public demo status file; scheduled by GitHub Actions."""

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path


def main():
    now = datetime.now(timezone.utc)
    india = timezone(timedelta(hours=5, minutes=30))
    status = {
        "message": "Demo refreshed successfully!",
        "last_updated_utc": now.isoformat(timespec="seconds"),
        "last_updated_ist": now.astimezone(india).isoformat(timespec="seconds"),
        "refresh_interval_hours": 5,
    }
    output = Path(__file__).resolve().with_name("demo-status.json")
    output.write_text(json.dumps(status, indent=2) + "\n", encoding="utf-8")
    print(output.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
