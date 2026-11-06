# unhackable

> **Learn → Scan → Review → Verify → Recover**
>
> `unhackable` is a defensive cybersecurity learning project for understanding real-world incidents and reducing risk on a personal Linux Mint computer. The name is aspirational—not a promise that any computer can be made impossible to compromise.

It combines a local, report-only system scan, public advisories, curated incident lessons, and optional AI-assisted explanations. It helps people make informed decisions; it is not an autonomous security agent.

## Start here

1. **Learn** — Read the [beginner curriculum](curriculum/README.md) and [glossary](curriculum/glossary.md).
2. **Harden** — Review the [Linux Mint home checklist](learning/linux-mint-home-hardening.md).
3. **Scan** — Run `bash scripts/security_scan.sh`, then inspect `logs/last_scan.txt`.
4. **Review** — Run `python3 scripts/risk_review.py`; treat its priority as a prompt for human review, not a verdict.
5. **Verify** — Compare important claims with the linked official advisories.
6. **Recover** — Maintain tested backups and use the [home-user incident playbook](docs/home-user-incident-playbook.md) if needed.

Optional tools:

```bash
python3 scripts/login_alert.py       # best-effort local failed-login alerts
python3 scripts/password_check.py   # local, masked password-quality estimate
python3 scripts/daily_intel.py      # fetch public feed entries
python3 scripts/learning_digest.py  # create a local learning digest
python3 scripts/ai_guard.py         # optional local Ollama summary
```

## Who this is for

Home users, Linux Mint learners, educators, and people exploring local AI for defensive education. No prior cybersecurity experience is required. This is not a substitute for professional incident response or official vendor support.

## Mission

Help people understand common security failures, learn from public incident reports, reduce unnecessary exposure on their own computer, and prepare to recover safely. A useful goal is not invulnerability: it is to be **informed, harder to compromise, quick to notice problems, and prepared to recover**.

## What it does—and does not do

It collects selected local security information, provides a limited transparent review priority (`LOW`, `MEDIUM`, `HIGH`, `UNKNOWN`), fetches configured public feeds, presents incident-learning material, and can request an explanation from local Ollama.

It does **not** guarantee security, diagnose compromise, monitor online account sign-ins, or automatically change settings. It never needs your account password, MFA code, session cookie, recovery code, or provider token. Configure online “Was this you?” notifications with each account provider directly. The project does not include exploit code, malware, credential theft tools, or instructions for targeting systems.

## Password and account safety

The optional password checker is a conservative local heuristic, not a cracking simulator, breach lookup, or safety guarantee. Use a new candidate only, on a trusted device. It does not transmit, save, print, or log the candidate. Prefer a unique password-manager-generated value and enable MFA where available.

- [Minimum safe password policy](learning/password-policy.md)
- [Strong password/passphrase guidance](learning/strong-password-policy.md)
- [Why MFA matters](learning/mfa-why-it-matters.md)
- [Fictional pattern examples](learning/password-pattern-examples.md)

Never test an existing password by making repeated login attempts or typing it into an online checker.

## Login alerts

`login_alert.py` optionally watches selected local journal events and may display a desktop notification. It is best-effort and does not monitor web accounts. A failed attempt is not proof of account access. For provider “Was this you?” alerts, use the provider's official app or known address; do not follow unexpected links. See [login-alert guidance](docs/login-alerts.md).

## Safety principles

- Missing scan information means unknown, not safe.
- A wildcard-bound service is not necessarily internet-reachable; `LOW` is not a guarantee and `HIGH` is not proof of compromise.
- Keep Linux Mint, browsers, and applications updated through trusted channels.
- Use unique credentials, MFA, and tested backups.
- Do not run the whole project as root to fill gaps.
- Treat feed articles and logs as untrusted input; redact private details before sharing them.
- Verify recommendations against primary sources and use human judgment before changing settings.
- Only assess systems you own or have explicit permission to assess. Keep labs isolated.
- AI may explain and summarize; it must not make unsupported compromise claims or take action.

## Learning resources

- [Full curriculum](curriculum/README.md)
- [Glossary](curriculum/glossary.md)
- [Incident case library](cases/README.md)
- [Defensive attacker-pattern guide](learning/how-attack-code-works-defensively.md)
- [Linux Mint hardening](learning/linux-mint-home-hardening.md)
- [Ransomware and backups](learning/ransomware-and-backups.md)
- [Home-user incident response](docs/home-user-incident-playbook.md)
- [Safe decoy VM plan](docs/safe-decoy-vm.md)

Generated scan reports and feed data are local and git-ignored. Ollama must be installed with a model available and configured for loopback only.
