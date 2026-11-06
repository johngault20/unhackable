# unhackable

**unhackable is a defensive cybersecurity learning project—not a promise that any computer can be made impossible to hack.** The name is aspirational. The real goal is to learn from real-world incidents, understand common security failures, and practice safer habits on a Linux Mint home computer.

The project combines a report-only local security scan with public advisories and curated incident case studies. Its reports are educational aids: they do not prove that a machine is compromised, replace trusted security guidance, or automatically change system settings.

## What it does

- Reports local security context such as firewall status, listening sockets, enabled services, authentication-log excerpts, and available package updates.
- Fetches recent entries from configured public cyber feeds.
- Keeps curated, defensive case studies of real incidents in `cases/`.
- Explains common attacker code behaviors at a conceptual level and focuses on how defenders reduce risk and notice warning signs. It does not provide attack scripts or exploit instructions.
- Can ask a local Ollama model to summarize local observations and explain lessons from the case studies and feed entries.
- Offers a small, transparent scan review priority (`LOW`, `MEDIUM`, `HIGH`, or `UNKNOWN`) with evidence and limitations.
- Includes a conservative, isolated, offline-first decoy VM learning plan.

## What it does not do

- Guarantee protection or make a computer “unhackable.”
- Determine that a public incident has affected your computer based only on news or feed matches.
- Train or continuously improve the local AI model. Each summary uses the local files available at that time.
- Automatically remediate findings, run offensive tests, or authorize activity against other systems.
- Include working exploit code, credential theft tools, malware, or instructions for attacking real systems.

## Repository layout

- `scripts/security_scan.sh` - local Linux Mint security report
- `scripts/daily_intel.py` - fetch public feed entries into local JSON
- `scripts/ai_guard.py` - ask local Ollama for a cautious learning summary
- `scripts/risk_review.py` - classify scan output with a small, report-only rule set
- `scripts/learning_digest.py` - combine curated lessons and available feed metadata into a local learning document
- `cases/` - curated incident case studies and a lessons matrix
- `learning/` - high-level explanations of attacker behavior and defensive concepts
- `docs/safe-decoy-vm.md` - offline-first isolated VM safety plan
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

4. Generate the local scan review priority:
   ```bash
   python3 scripts/risk_review.py
   ```

5. Create a learning digest from curated case studies and feed entries:
   ```bash
   python3 scripts/learning_digest.py
   ```

6. Ask the local model to summarize the report, feed entries, and curated case studies:
   ```bash
   python3 scripts/ai_guard.py
   ```

The learning digest is saved to `intel/learning_digest.md`, the AI summary to `intel/learning_summary.md`, and the scan review to `intel/risk_review.md`. The digest works offline and case studies remain available if a feed is unavailable. Feed coverage varies and does not replace checking original advisories. Ollama must already be installed with the selected model available; it should listen on loopback only.

## Risk-review interpretation

The review script uses a small set of visible text checks: reported UFW status, availability of listening-socket data, and available-package output. It assigns `UNKNOWN` when required information is absent or a needed command was unavailable; `HIGH` only when UFW is reported inactive and the socket report includes wildcard-bound listener rows; `MEDIUM` when one or more review indicators are present; and `LOW` when none match. These are review priorities—not validated risk scores. A wildcard bind does not prove internet reachability, and LOW does not mean safe. Inspect the generated evidence and use human judgment.

## Safety and interpretation

- Keep your real Mint PC behind a firewall and do not expose services to the public internet unless you have a clear need and understand the risk.
- The scan is report-only. Some system information may be unavailable without elevated permissions; do not run the whole project as root just to fill in gaps.
- Never give an AI assistant administrative rights or unrestricted shell access. Review advice yourself and verify it against the linked primary source before acting.
- Treat feed articles as untrusted input and as learning leads, not proof of an attack on your machine.
- The project does not probe third-party systems. Only test systems you own or are explicitly authorized to assess.
- Any decoy or lab VM should follow [`docs/safe-decoy-vm.md`](docs/safe-decoy-vm.md). Never use it to attack anyone.

## Learning from incidents and attacker code

Start with [`cases/README.md`](cases/README.md), [`cases/lessons-matrix.md`](cases/lessons-matrix.md), and [`learning/how-attack-code-works-defensively.md`](learning/how-attack-code-works-defensively.md). The learning material describes attacker techniques at a high level, then focuses on prevention, detection, and recovery. It intentionally does not include deployable attack code, exploit steps, or instructions for targeting systems.

