# unhackable

**unhackable is a defensive cybersecurity learning project—not a promise that any computer can be made impossible to hack.** The name is aspirational. The real goal is to learn from real-world incidents, understand common security failures, and practice safer habits on a Linux Mint home computer.

The project combines a read-only local security report with public advisories and curated incident case studies. Its reports are educational aids: they do not prove that a machine is compromised, replace trusted security guidance, or automatically change system settings.

## What it does

- Reports local security context such as firewall status, listening sockets, enabled services, authentication-log excerpts, and available package updates.
- Fetches recent entries from configured public cyber feeds.
- Keeps curated, defensive case studies of real incidents in `cases/`.
- Can ask a local Ollama model to summarize local observations and explain lessons from the case studies and feed entries.
- Encourages reducing exposure, checking primary sources, and using isolated lab environments for learning.

## What it does not do

- Guarantee protection or make a computer “unhackable.”
- Determine that a public incident has affected your computer based only on news or feed matches.
- Train or continuously improve the local AI model. Each summary uses the local files available at that time.
- Automatically remediate findings, run offensive tests, or authorize activity against other systems.

## Repository layout

- `scripts/security_scan.sh` - local Linux Mint security report
- `scripts/daily_intel.py` - fetch public feed entries into local JSON
- `scripts/ai_guard.py` - ask local Ollama for a cautious learning summary
- `cases/` - curated incident case studies and defensive lessons
- `requirements.txt` - Python dependencies
- `config/ollama-local.service` - example local-only service file

Generated reports and fetched feed data are local and git-ignored.

## Quick start

1. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv .venv
   . .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Run the local report:
   ```bash
   bash scripts/security_scan.sh
   ```

3. Fetch recent public feed entries:
   ```bash
   python3 scripts/daily_intel.py
   ```

4. Ask the local model to summarize the report, feed entries, and curated case studies:
   ```bash
   python3 scripts/ai_guard.py
   ```

The learning summary is printed and saved to `intel/learning_summary.md`. Case studies are available even if a feed is unavailable. Feed coverage varies and does not replace checking original advisories. Ollama must already be installed with the selected model available; it should listen on loopback only.

## Safety and interpretation

- Keep your real Mint PC behind a firewall and do not expose services to the public internet unless you have a clear need and understand the risk.
- The scan is report-only. Some system information may be unavailable without elevated permissions; do not run the whole project as root just to fill in gaps.
- Never give an AI assistant administrative rights or unrestricted shell access. Review advice yourself and verify it against the linked primary source before acting.
- Treat feed articles as untrusted input and as learning leads, not proof of an attack on your machine.
- The project does not probe third-party systems. Only test systems you own or are explicitly authorized to assess.
- Any decoy or lab VM should be isolated from your real desktop and home network. Never use it to attack anyone.

## Learning from incidents

Start with [`cases/README.md`](cases/README.md). Each case separates the incident summary from defensive interpretation and suggests safe checks for a home user. The cited primary advisories are the source of truth; case studies are concise learning notes, not complete incident reports.
