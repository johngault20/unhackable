# unhackable

**unhackable is a defensive cybersecurity learning project—not a promise that any computer can be made impossible to hack.** The name is aspirational. The real goal is to help people understand common security failures, learn from real incidents, and practice safer habits that reduce the chance and impact of a compromise on their own computer.

The project combines a report-only local security scan with public advisories, curated incident case studies, and cautious AI-assisted explanations. It is designed to teach people and help AI explain defensive concepts. It is not an autonomous security agent: reports do not prove a machine is compromised, replace trusted guidance, or automatically change settings.

## Learn → Scan → Review → Verify → Recover

1. **Learn** from the [curriculum](curriculum/README.md), incident cases, and defensive guides.
2. **Scan** local system state with a read-only report.
3. **Review** the limited findings and treat missing data as unknown.
4. **Verify** important claims with official sources and your own judgment.
5. **Recover** using tested backups and a calm incident-response plan.

## What it does

- Reports local security context such as firewall status, listening sockets, enabled services, authentication-log excerpts, and available package updates.
- Optionally monitors selected local journal events and displays desktop notifications for likely failed sign-in attempts. This is best-effort and does not monitor web accounts.
- Fetches recent entries from configured public cyber feeds.
- Keeps curated, defensive case studies of real incidents in `cases/`.
- Explains common attacker code behaviors at a conceptual level and focuses on how defenders reduce risk and notice warning signs. It does not provide attack scripts or exploit instructions.
- Can ask a local Ollama model to summarize local observations and explain lessons from the case studies and feed entries.
- Offers a small, transparent scan review priority (`LOW`, `MEDIUM`, `HIGH`, or `UNKNOWN`) with evidence and limitations.
- Includes practical learning on phishing, credential abuse, ransomware, local hardening, incident response, and isolated VM use.

## What it does not do

- Guarantee protection or make a computer “unhackable.”
- Determine that a public incident has affected your computer based only on news or feed matches.
- Monitor sign-ins to websites, email, banking, or cloud accounts. Configure “Was this you?” or new-sign-in alerts directly with each provider in its official security settings.
- Ask for or store account passwords, MFA codes, session cookies, recovery codes, or provider tokens.
- Train or continuously improve the local AI model. Each summary uses the local files available at that time.
- Automatically remediate findings, run offensive tests, or authorize activity against other systems.
- Include working exploit code, credential theft tools, malware, or instructions for attacking real systems.

## Repository layout

- `scripts/security_scan.sh` - local Linux Mint security report
- `scripts/login_alert.py` - optional local failed-authentication desktop alert monitor
- `scripts/daily_intel.py` - fetch public feed entries into local JSON
- `scripts/ai_guard.py` - ask local Ollama for a cautious learning summary
- `scripts/risk_review.py` - classify scan output with a small, report-only rule set
- `scripts/learning_digest.py` - combine curated lessons and available feed metadata into a local learning document
- `cases/` - curated incident case studies and a lessons matrix
- `learning/` - high-level defensive lessons
- `curriculum/` - modules, glossary, safety rules, and project roadmap
- `docs/` - login-alert guide, safe VM plan, and home-user incident-response guidance
- `requirements.txt` - Python dependencies
- `config/` - example local-only Ollama service and optional user login-alert service

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

3. Generate the local scan review priority:
   ```bash
   python3 scripts/risk_review.py
   ```

4. Optionally monitor local failed sign-in events:
   ```bash
   python3 scripts/login_alert.py
   ```

   See [`docs/login-alerts.md`](docs/login-alerts.md) for desktop notification requirements and an optional user service. For online-account “Was this you?” notices, configure alerts with the account provider; this local script cannot see website sign-ins.

5. Fetch public feed entries and generate learning materials:
   ```bash
   python3 scripts/daily_intel.py
   python3 scripts/learning_digest.py
   ```

6. If Ollama is installed locally and listening on loopback, generate an AI-assisted learning summary:
   ```bash
   python3 scripts/ai_guard.py
   ```

The learning digest is saved to `intel/learning_digest.md`, the AI summary to `intel/learning_summary.md`, and the scan review to `intel/risk_review.md`. The digest works offline and case studies remain available if a feed is unavailable. Feed coverage varies and does not replace checking original advisories.

## Risk-review interpretation

The review script uses a small set of visible text checks: reported UFW status, availability of listening-socket data, and available-package output. It assigns `UNKNOWN` when required information is absent or a needed command was unavailable; `HIGH` only when UFW is reported inactive and the socket report includes wildcard-bound listener rows; `MEDIUM` when one or more review indicators are present; and `LOW` when none match. These are review priorities—not validated risk scores. A wildcard bind does not prove internet reachability, and LOW does not mean safe. Inspect the generated evidence and use human judgment.

## Learning and AI use

Start with [`curriculum/README.md`](curriculum/README.md), [`curriculum/glossary.md`](curriculum/glossary.md), [`learning/README.md`](learning/README.md), and [`cases/README.md`](cases/README.md). The curriculum moves from security mindset and common patterns through real incidents, Linux Mint hardening, account alerts, backups, AI-assisted review, and safe lab practice.

The local model is a teaching assistant, not a source of truth or a continuously learning system. Its input includes untrusted feed text and local logs. Verify claims against primary sources, do not paste sensitive data into services you do not control, and do not follow generated commands without human review.

## Safety and interpretation

- Keep your real Mint PC behind a firewall and do not expose services to the public internet unless you have a clear need and understand the risk.
- The scan and login monitor are report-only. Some system information may be unavailable without elevated permissions; do not run the whole project as root just to fill in gaps.
- A local failed-login notification is best-effort and may miss events or include false positives. It is not proof of successful intrusion.
- Never give an AI assistant administrative rights or unrestricted shell access. Review advice yourself and verify it against the linked primary source before acting.
- Treat feed articles and logs as untrusted input and as learning leads, not proof of an attack on your machine.
- The project does not probe third-party systems. Only test systems you own or are explicitly authorized to assess.
- Any decoy or lab VM should follow [`docs/safe-decoy-vm.md`](docs/safe-decoy-vm.md). Never use it to attack anyone.
