# unhackable

A learning-focused Linux Mint security project for local defense, system awareness, and AI-assisted review.

This project is designed to help you understand how your PC is exposed and what is happening around it, without turning your real machine into a public target.

Core ideas:
- Keep your real PC behind a firewall and away from direct internet exposure.
- Scan locally for firewall status, listening ports, login events, update status, and enabled services.
- Gather public cyber threat news and advisories from trusted feeds.
- Use a local AI model only on your own laptop to explain what the scan and intel mean.
- Keep any honeypot or decoy isolated from your real desktop and home network.

This project is educational and defensive. It is not a guarantee of being unhackable.

Repository layout:
- `scripts/security_scan.sh` - local Mint security scan
- `scripts/daily_intel.py` - fetch public cyber intel into local JSON
- `scripts/ai_guard.py` - ask your local Ollama model to summarize scan + intel
- `requirements.txt` - Python dependencies
- `config/ollama-local.service` - example local-only service file

Quick start:

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

3. Fetch the latest public cyber intel:
   ```bash
   python3 scripts/daily_intel.py
   ```

4. Ask your local AI for a summary:
   ```bash
   python3 scripts/ai_guard.py
   ```

5. If you want Ollama to start automatically, configure it to listen on localhost only.

Important safety notes:
- Do not expose your real Mint PC to the internet unless you intentionally need to.
- Never give the AI administrative rights or unrestricted shell access.
- Treat public threat feeds as intelligence, not proof that your machine is under attack.
- If you use a decoy or honeypot, keep it isolated from your real computer and never use it to attack anyone.
