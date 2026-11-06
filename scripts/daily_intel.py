#!/usr/bin/env python3
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import feedparser

DEFAULT_FEEDS = [
    "https://www.cisa.gov/uscert/ncas/alerts.xml",
    "https://feeds.feedburner.com/TheHackersNews",
    "https://www.darkreading.com/rss.xml",
]

def fetch_feed(url: str):
    feed = feedparser.parse(url)
    entries = []
    for item in getattr(feed, "entries", [])[:5]:
        title = (getattr(item, "title", "") or "").strip()
        link = (getattr(item, "link", "") or "").strip()
        summary = (getattr(item, "summary", "") or getattr(item, "description", "") or "").strip()
        published = (getattr(item, "published", "") or getattr(item, "updated", "") or "").strip()
        entries.append({
            "title": title,
            "link": link,
            "summary": summary,
            "published": published,
        })
    return entries

def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    intel_dir = repo_root / "intel"
    intel_dir.mkdir(exist_ok=True)

    configured_feeds = os.environ.get("UNHACKABLE_FEEDS")
    feed_sources = [f.strip() for f in configured_feeds.split(",")] if configured_feeds else DEFAULT_FEEDS
    feed_sources = [f for f in feed_sources if f]

    results = []
    for source in feed_sources:
        try:
            entries = fetch_feed(source)
            results.append({"source": source, "entries": entries})
            print(f"[unhackable] Fetched {len(entries)} entries from {source}")
        except Exception as exc:
            results.append({"source": source, "entries": [], "error": str(exc)})
            print(f"[unhackable] Failed to fetch {source}: {exc}")

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "feeds": results,
    }

    out_file = intel_dir / "daily_intel.json"
    out_file.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"[unhackable] Wrote intel summary to {out_file}")

    for feed in results:
        print(f"\n[unhackable] Source: {feed['source']}")
        if not feed.get("entries"):
            print("  no entries found or parsing failed.")
            continue
        for item in feed["entries"][:3]:
            title = item.get("title") or "Untitled"
            print(f"  - {title}")
            if item.get("link"):
                print(f"    {item['link']}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
