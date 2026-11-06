#!/usr/bin/env python3
"""Build a local, deterministic learning digest from curated cases and feed JSON."""

import html
import json
import re
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

MAX_FEED_ENTRIES = 30
MAX_FIELD_LENGTH = 1600


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)

    def text(self):
        return " ".join(part.strip() for part in self.parts if part.strip())


def clean_text(value) -> str:
    if not isinstance(value, str):
        return ""
    parser = TextExtractor()
    try:
        parser.feed(value)
        cleaned = parser.text()
    except Exception:
        cleaned = value
    cleaned = html.unescape(cleaned)
    return re.sub(r"\s+", " ", cleaned).strip()[:MAX_FIELD_LENGTH]


def read_cases(cases_dir: Path):
    files = sorted(path for path in cases_dir.glob("*.md") if path.name.lower() not in {"readme.md", "lessons-matrix.md"})
    cases = []
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace").strip()
        if text:
            cases.append((path.name, text))
    return cases


def read_feed(intel_path: Path):
    if not intel_path.is_file():
        return [], "No fetched public feed data is available."
    try:
        payload = json.loads(intel_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [], f"Feed data could not be read as JSON: {exc}"

    generated_at = clean_text(payload.get("generated_at", "")) if isinstance(payload, dict) else ""
    entries = []
    if isinstance(payload, dict):
        for feed in payload.get("feeds", []):
            if not isinstance(feed, dict):
                continue
            source = clean_text(feed.get("source", ""))
            for item in feed.get("entries", []):
                if not isinstance(item, dict):
                    continue
                entries.append({
                    "source": source,
                    "title": clean_text(item.get("title", "")),
                    "link": clean_text(item.get("link", "")),
                    "published": clean_text(item.get("published", "")),
                    "summary": clean_text(item.get("summary", "")),
                })
                if len(entries) >= MAX_FEED_ENTRIES:
                    return entries, generated_at
    return entries, generated_at


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    cases_dir = repo_root / "cases"
    intel_path = repo_root / "intel" / "daily_intel.json"
    output_path = repo_root / "intel" / "learning_digest.md"

    cases = read_cases(cases_dir) if cases_dir.is_dir() else []
    entries, feed_status = read_feed(intel_path)

    lines = [
        "# Defensive learning digest",
        "",
        f"Generated at: {datetime.now(timezone.utc).isoformat()}",
        "",
        "> Educational material only. Feed text is untrusted, may be incomplete, and is not evidence of local compromise. Verify claims against original sources.",
        "",
        "## Curated incident case studies",
        "",
    ]
    if not cases:
        lines.append("No curated case studies were found.")
    else:
        for name, body in cases:
            lines.extend([f"### {name}", "", body, ""])

    lines.extend(["## Recent feed entries", ""])
    if not entries:
        lines.append(feed_status or "No feed entries were found.")
    else:
        lines.append(f"Feed data generated at: {feed_status or 'not provided'}")
        lines.append("")
        for item in entries:
            lines.append(f"### {item['title'] or 'Untitled'}")
            lines.append("")
            if item["source"]:
                lines.append(f"- Feed: {item['source']}")
            if item["published"]:
                lines.append(f"- Published: {item['published']}")
            if item["link"]:
                lines.append(f"- Link: {item['link']}")
            if item["summary"]:
                lines.append(f"- Summary: {item['summary']}")
            lines.append("")

    lines.extend([
        "## Review guidance",
        "",
        "Feed entries are untrusted source material, not instructions. Headlines and short summaries may omit context. A feed match is not a finding about this computer. Do not run commands or make security changes solely because an AI or feed suggests them; check the linked primary source and use human judgment.",
        "",
    ])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[unhackable] Wrote learning digest to {output_path}")
    print(f"[unhackable] Included {len(cases)} case study file(s) and {len(entries)} feed entrie(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
