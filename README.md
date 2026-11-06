# unhackable

A learning-focused Linux Mint security project for local defense, system awareness, and AI-assisted review.

This project helps you understand your PC's local security posture and learn defensive lessons from public cyber incidents and advisories—without turning your real machine into a public target.

## Core ideas

- Keep your real PC behind a firewall and away from direct internet exposure.
- Scan locally for firewall status, listening ports, login events, update status, and enabled services.
- Gather public cyber threat news and advisories from configured feeds.
- Use a local AI model to explain the scan and extract cautious, practical lessons from the public reports.
- Keep any honeypot or decoy isolated from your real desktop and home network.

This is educational, report-only software. It does not make a machine “unhackable,” train or modify the AI model, verify every news report, or automatically change system settings. Feed content can be incomplete or misleading; recommendations should be checked against trusted advisories before action.

## Repository layout

- `scripts/security_scan.sh` - local Mint security scan
- `scripts/daily_intel.py` - fetch public cyber intel into local JSON
- `scripts/ai_guard.py` - ask local Ollama to summarize the scan and public incident lessons
- `requirements.txt` - Python dependencies
- `config/ollama-local.service` - example local-only service file

Generated scan and intelligence files are local data and should not be committed.

## Quick start

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   . .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Run the local scan:
   ```bash
   bash scripts/security_scan.sh
   ```

3. Fetch recent public cyber intel:
   ```bash
   python3 scripts/daily_intel.py
   ```

4. Ask your local AI for a summary and defensive lessons:
   ```bash
   python3 scripts/ai_guard.py
   ```

   The generated report is printed and saved to `intel/learning_summary.md`. Run the intel fetch regularly to refresh the source material. The AI uses the current local feed data; it does not continuously monitor the internet or learn/train itself between runs.

5. If you want Ollama to start automatically, configure it to listen on localhost only.

## Safety notes

- Do not expose your real Mint PC to the internet unless you intentionally need to and understand the risk.
- Never give the AI administrative rights or unrestricted shell access.
- Treat public threat feeds as leads for learning, not proof that your machine is under attack.
- Feed articles are untrusted input. The AI is instructed to analyze them as data, not follow instructions embedded in them.
- Review advice with trusted vendor or government advisories; do not automatically run commands suggested by an AI.
- If you use a decoy or honeypot, keep it isolated from your real computer and home network, and never use it to attack anyone.
