# unhackable

> **Learn → Scan → Review → Verify → Recover**
>
> `unhackable` is a defensive cybersecurity learning project for understanding real-world incidents and reducing risk on a personal Linux Mint computer. The name is aspirational—not a promise that any computer can be made impossible to compromise.

It brings together a local, report-only system scan, public advisories, curated incident lessons, and optional AI-assisted explanations. The aim is to help people make informed, safer decisions—not to act as an autonomous security agent.

## Who this is for

- Linux Mint and other home-computer users who want to understand practical security basics.
- Beginners learning how real incidents translate into safer habits.
- Educators who want a cautious, defensive teaching resource.
- People experimenting with local AI who want it to explain security information without treating it as an authority.

No prior cybersecurity experience is required. The project is not a substitute for professional incident response or official vendor support.

## Start here

1. **Learn** — Read the [beginner curriculum](curriculum/README.md) and [glossary](curriculum/glossary.md).
2. **Harden** — Review the [Linux Mint home checklist](learning/linux-mint-home-hardening.md); make changes only when you understand them.
3. **Scan** — Run the local report and inspect its output:
   ```bash
   bash scripts/security_scan.sh
   ```
4. **Review** — Generate a limited review priority:
   ```bash
   python3 scripts/risk_review.py
   ```
5. **Learn from incidents** — Browse the [case library](cases/README.md) and [lessons matrix](cases/lessons-matrix.md).
6. **Verify** — Check important claims against the linked official advisories before acting.
7. **Recover** — Maintain and test backups; use the [home-user incident playbook](docs/home-user-incident-playbook.md) if something seems wrong.

Optional: Fetch public feed entries and create a local learning digest:

```bash
python3 scripts/daily_intel.py
python3 scripts/learning_digest.py
```

If you have Ollama and a local model installed, you can also create an AI-assisted summary:

```bash
python3 scripts/ai_guard.py
```

The local login alert monitor is optional and separate from account-provider alerts:

```bash
python3 scripts/login_alert.py
```

See [Login alerts](docs/login-alerts.md) for details.

## A one-week beginner path

This is a suggested pace, not a certification or security guarantee. You can do the reading without changing system settings.

- **Day 1 — Understand the goal:** Read this page, the [curriculum](curriculum/README.md), and the [glossary](curriculum/glossary.md). Write down one thing the project can and cannot tell you.
- **Day 2 — Protect accounts:** Review important account providers' official security pages. Enable MFA and sign-in alerts where available. Never enter real credentials into repository demos.
- **Day 3 — Learn from incidents:** Read one case study and its original advisory. Separate source-backed facts from your own defensive lesson.
- **Day 4 — Review your baseline:** Read the hardening checklist, run the local scan, and inspect its report. Don't run the project as root to fill gaps.
- **Day 5 — Practice safe interpretation:** Run the risk review and optional local login monitor. Treat `UNKNOWN` as missing evidence, not as safe.
- **Day 6 — Prepare recovery:** Identify important files, check your backups, and confirm you know how to restore a file.
- **Day 7 — Review and reflect:** Generate the local learning digest or AI summary, verify one claim against its source, and note one safe habit to maintain.

For a conservative, offline estimate of a candidate password, see the [password checker guide](learning/password-checker.md) and run `python3 scripts/password_check.py` on a trusted personal device. It does not attempt logins, reveal the candidate, or estimate crack time.

## Mission

Help people understand how common security failures happen, learn from public incident reports, reduce unnecessary exposure on their own computer, and prepare to recover safely. The project is for education and personal defense; it is not a guarantee of security.

A useful security goal is not to become invincible. It is to be **informed, harder to compromise, quick to notice problems, and prepared to recover**.

## What this project does

- Collects a local snapshot of selected system information, including firewall status, listening sockets, enabled services, authentication-log excerpts, and available package updates.
- Offers a small, transparent, report-only review priority: `LOW`, `MEDIUM`, `HIGH`, or `UNKNOWN`.
- Fetches configured public cyber-news and advisory feeds into local files.
- Provides curated case studies and practical learning about phishing, credential abuse, ransomware, hardening, and recovery.
- Can ask a local Ollama model to explain scan results and incident lessons.
- Can optionally show desktop notifications for selected local failed-authentication events, when system journal access and a desktop session allow it.
- Provides an offline, conservative password-quality estimate that does not transmit or persist the candidate.

## What it does not do

- Make a device “unhackable,” prove a device is safe, or diagnose compromise.
- Treat a public incident or feed match as proof that your computer is affected.
- Monitor website, email, banking, or cloud-account sign-ins. For “Was this you?” alerts, use the provider’s official account-security settings.
- Ask for or store your online account passwords, MFA codes, session cookies, recovery codes, or provider tokens.
- Automatically block addresses, disable accounts, delete files, or change system settings.
- Train the AI model continuously or make AI output authoritative.
- Provide working exploit code, malware, credential theft tools, or instructions for targeting systems.

## Quick setup

1. Install Python and create a virtual environment:
   ```bash
   python3 -m venv .venv
   . .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Run the scan and review:
   ```bash
   bash scripts/security_scan.sh
   python3 scripts/risk_review.py
   ```
3. Optionally start local failed-login notifications:
   ```bash
   python3 scripts/login_alert.py
   ```
4. Optionally check a candidate password locally:
   ```bash
   python3 scripts/password_check.py
   ```
5. Optionally fetch public intel, build a digest, and generate a local AI summary:
   ```bash
   python3 scripts/daily_intel.py
   python3 scripts/learning_digest.py
   python3 scripts/ai_guard.py
   ```

Generated reports and fetched feed data are local and git-ignored. Feed coverage is not comprehensive. Ollama must be installed with the selected model available; keep its service on loopback only.

## Understand the review priority

`risk_review.py` uses a small set of text checks from `logs/last_scan.txt`. Missing or unavailable required data should result in `UNKNOWN`, not an assumption that the machine is safe. Its labels are prompts for human review, not validated security scores. In particular, a wildcard-bound listener is not proof of internet reachability, `LOW` does not mean safe, and `HIGH` does not mean compromised. Inspect the evidence and verify it through trusted system documentation.

## Password checker limitations

The optional checker is intentionally conservative but is not literally “twice as harsh” as a standard, because no universal strength score exists to double. It uses local heuristics for length, common examples, and a few obvious patterns. It cannot determine whether a password is reused, exposed, or accepted by an account provider, and it does not estimate how long a real attacker would take. Prefer a unique password-manager-generated password and MFA. Do not use the tool on a shared or suspected-compromised device.

## Login alerts

`login_alert.py` watches selected new authentication events in the local system journal and may display a desktop notification. It is best-effort: it can miss events, produce false positives, and requires appropriate journal permissions. It does not send logs over the network, block users, or monitor online services. A failed login is not proof that someone gained access.

For online-account “Was this you?” notices, configure sign-in notifications directly with each provider. Open the provider's official app or navigate to its known website yourself—do not rely on unexpected alert links. Never give this project account credentials or authentication codes.

## Keep your real PC safe

- Keep Linux Mint, browsers, and applications updated through trusted channels.
- Use unique passwords and MFA for important accounts.
- Keep backups and periodically check that you can restore files.
- Avoid exposing services to the public internet unless you have a clear need and understand the risk.
- Do not run the whole project as root to fill in missing scan data.
- Treat local logs and feed articles as untrusted input; redact private details before sharing them.
- Verify recommendations against primary sources and use human judgment before changing settings.
- Keep labs isolated; see the [safe decoy VM plan](docs/safe-decoy-vm.md).

## Security principles

1. **Evidence over assumptions:** Missing data is unknown; headlines are not local evidence.
2. **Least privilege:** Do not give the AI or scripts administrative access they do not need.
3. **Defense in depth:** Updates, account security, firewall awareness, and backups complement one another.
4. **Human review:** AI may explain and summarize; it must not make unsupported compromise claims or take action.
5. **Safe learning:** Only assess systems you own or have explicit permission to assess.
6. **Recoverability:** A tested backup and calm response plan are core security controls.

## Learning resources

- [Full curriculum](curriculum/README.md)
- [Glossary](curriculum/glossary.md)
- [Incident case library](cases/README.md)
- [How attack code works—defensively](learning/how-attack-code-works-defensively.md)
- [Conservative password checker guide](learning/password-checker.md)
- [Phishing and credential abuse](learning/phishing-and-credential-abuse.md)
- [Ransomware and backups](learning/ransomware-and-backups.md)
- [Home-user incident response](docs/home-user-incident-playbook.md)
- [Login alerts](docs/login-alerts.md)
- [Safe decoy VM plan](docs/safe-decoy-vm.md)
