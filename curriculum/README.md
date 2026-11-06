# unhackable curriculum

This curriculum is for home users and local AI assistants learning to protect personal computers. It is grounded in public advisories and incident case studies. It teaches how to reduce risk and respond carefully—not how to attack systems.

## Mission

**Learn → Scan → Review → Verify → Recover.**

The name `unhackable` is aspirational, not a guarantee. No scan or AI can prove that a computer is immune to compromise. The project is educational, report-only where it examines the system, and designed to leave changes and decisions to the human user.

## Learning outcomes

By the end, a learner should be able to:

- explain common attacker behavior at a high level without reproducing it
- distinguish a public incident from evidence about their own device
- review basic Linux Mint security information and recognize missing data
- configure safer account, update, firewall, and backup habits
- enable appropriate sign-in alerts from online account providers
- respond calmly to a suspicious event and know when to seek help
- use local AI as an assistant while verifying its claims and protecting private data

## Curriculum sequence

### Module 1 — Security mindset and vocabulary

**Learn:** risk reduction, uncertainty, evidence, incident, availability, authentication, and least privilege.

**Read:** `README.md`, `learning/README.md`, and [`glossary.md`](glossary.md).

**Practice:** Explain why `UNKNOWN` is different from `LOW`, and why a news alert alone does not show that your PC is affected.

### Module 2 — Common attack patterns (defender's view)

**Learn:** phishing, credential abuse, vulnerable services, supply-chain compromise, persistence, ransomware, and data theft at a high level.

**Read:** `learning/how-attack-code-works-defensively.md`, `learning/phishing-and-credential-abuse.md`, and [`attack-pattern-catalogue.md`](attack-pattern-catalogue.md).

**Practice:** For each pattern, name a prevention measure and a safe follow-up check. Do not run exploit code or test other people's systems.

### Module 3 — Real-world incidents and lessons

**Learn:** compare what a public source says with what a defender can reasonably infer.

**Read:** `cases/README.md` and `cases/lessons-matrix.md`.

**Practice:** Pick one case and write down a source-backed fact, a defensive lesson, and one reason it might not apply to a home Mint PC.

### Module 4 — Linux Mint baseline and hardening

**Learn:** updates, firewall awareness, software inventory, startup services, listening sockets, browser hygiene, and recoverability.

**Read:** `learning/linux-mint-home-hardening.md`.

**Practice:** Run `bash scripts/security_scan.sh`, inspect `logs/last_scan.txt`, then run `python3 scripts/risk_review.py`. Treat missing information as unknown and review findings before changing anything.

### Module 5 — Account protection and sign-in alerts

**Learn:** local computer authentication differs from sign-in to an online provider. The provider is the right source for “Was this you?” account alerts.

**Read:** [`../docs/login-alerts.md`](../docs/login-alerts.md) and `learning/phishing-and-credential-abuse.md`.

**Practice:** Enable sign-in notifications and MFA in the official security settings of important providers. Optionally run `python3 scripts/login_alert.py` to see selected local failed-login events. Never give this project account passwords, MFA codes, session cookies, or recovery codes.

### Module 6 — Ransomware, backups, and recovery

**Learn:** availability, protected backups, restore tests, and calm first response.

**Read:** `learning/ransomware-and-backups.md` and `../docs/home-user-incident-playbook.md`.

**Practice:** Identify important files, confirm they are backed up, and check that you know how to restore a copy.

### Module 7 — AI-assisted learning

**Learn:** untrusted input, source verification, local model limitations, and human oversight.

**Read:** `curriculum/ai-safety-rules.md` and `learning/README.md`.

**Practice:** Run `python3 scripts/daily_intel.py`, `python3 scripts/learning_digest.py`, and `python3 scripts/ai_guard.py`; verify at least one statement against its original source. Do not paste sensitive logs into services you do not control.

### Module 8 — Safe lab practice and project roadmap

**Learn:** VM isolation, clean snapshots, no personal data in a lab, and authorized practice.

**Read:** `../docs/safe-decoy-vm.md` and `project-roadmap.md`.

**Practice:** Verify VM network mode and host integration settings before any exercise. Use benign, intentionally designed training material only.

## Suggested beginner workflow

1. Read the mission, glossary, and home-user hardening checklist.
2. Review account-provider security settings and enable sign-in alerts and MFA where available.
3. Run the local scan and inspect the raw report.
4. Generate the risk-review report; treat it as a prompt for human review, not a verdict.
5. Optionally run the local login alert monitor and confirm it can read journal events.
6. Fetch public intelligence, build a digest, and compare claims with original advisories.
7. Review incident lessons, backup readiness, and the home-user response playbook.
8. Keep experiments isolated and authorized.

## Safety mandate

This curriculum is defensive and educational. It avoids exploit instructions, malware, credential theft, evasion, destructive actions, and targeting guidance. AI may summarize and explain, but must not act autonomously, make unsupported compromise claims, or change system settings. People remain responsible for verifying sources and choosing actions.
