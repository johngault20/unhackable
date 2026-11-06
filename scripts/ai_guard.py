#!/usr/bin/env python3
import os
import sys
from pathlib import Path

import requests

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "llama3.1")

def read_if_exists(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")

def build_prompt() -> str:
    repo_root = Path(__file__).resolve().parent.parent
    scan_path = repo_root / "logs" / "last_scan.txt"
    intel_path = repo_root / "intel" / "daily_intel.json"

    scan_text = read_if_exists(scan_path)
    intel_text = read_if_exists(intel_path)

    return f"""
You are a local cyber-defense assistant for a Linux Mint system.
Your job is to summarize security-relevant information in plain language.
Do not give commands that would delete files or block other devices without explicit human approval.

SYSTEM SECURITY REPORT:
{scan_text or 'No scan report was found yet. Run bash scripts/security_scan.sh first.'}

PUBLIC INTELLIGENCE FEEDS:
{intel_text or 'No daily intel data was found yet. Run python3 scripts/daily_intel.py first.'}

Please provide:
1. A short status summary.
2. A list of likely risks or suspicious behaviors.
3. A list of what should be checked next.
4. A brief note about whether this looks like a local issue, a broader internet issue, or uncertain.
"""

def main() -> int:
    try:
        response = requests.post(
            f"{OLLAMA_HOST}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": build_prompt(),
                "stream": False,
                "temperature": 0.2,
            },
            timeout=60,
        )
        response.raise_for_status()
        payload = response.json()
        summary = payload.get("response", "No response was returned by Ollama.")
    except Exception as exc:
        print(f"[unhackable] Ollama is unavailable or not running: {exc}")
        print("Start it locally with: ollama serve")
        return 1

    print("\n=== Local AI security summary ===\n")
    print(summary)
    return 0

if __name__ == "__main__":
    sys.exit(main())
