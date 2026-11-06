# unhackable curriculum

This document defines the learning path for the `unhackable` project. It is a defensive learning curriculum for home users and local AI assistants, grounded in public advisories, real-world incident patterns, and conservative security practice.

## Curriculum goals

- Learn how common attacks actually work at a high level.
- Understand the difference between a public advisory and evidence of local compromise.
- Reduce exposure on a Linux Mint home system.
- Learn how to keep a machine recoverable and resilient.
- Know what to check before acting on a warning, a feed item, or AI-generated advice.
- Practice safe, isolated lab behavior rather than risky or public testing.

## Learning path

### Module 1: Defensive mindset

Focus: what security means in practice, not in slogans.

Topics:
- What “unhackable” really means in a realistic home-user context.
- Why threat intelligence is not proof of compromise.
- Why local logs and public feeds must be treated as untrusted input.
- Why prevention, backups, and recovery matter more than hype.

Primary files:
- `README.md`
- `learning/README.md`
- `docs/home-user-incident-playbook.md`

### Module 2: Attack patterns and attacker behavior

Focus: understand how software misuse and system abuse generally happens.

Topics:
- reconnaissance
- phishing and credential abuse
- software exploitation and vulnerable services
- persistence and account abuse
- rights escalation and lateral movement
- ransomware and data disruption
- exfiltration and active collection
- social engineering and trust abuse

Primary files:
- `learning/how-attack-code-works-defensively.md`
- `learning/phishing-and-credential-abuse.md`
- `learning/ransomware-and-backups.md`

### Module 3: Real-world incident learning

Focus: relate general patterns to public incidents and advisories.

Topics:
- software supply-chain compromise
- ransomware outbreaks
- vulnerable file-transfer products
- internet-facing service exploitation
- credential misuse and phishing-driven compromise

Primary files:
- `cases/README.md`
- `cases/lessons-matrix.md`
- `cases/*.md`

### Module 4: Linux Mint home hardening

Focus: reduce exposure on a home device without unnecessary complexity.

Topics:
- system updates and supported software
- firewall awareness
- startup services and listening sockets
- software inventory
- browser and extension hygiene
- backups and recovery planning

Primary files:
- `learning/linux-mint-home-hardening.md`
- `scripts/security_scan.sh`
- `scripts/risk_review.py`

### Module 5: AI-assisted learning and safe review

Focus: teach people how to use AI without turning it into a dangerous authority.

Topics:
- local-only review with Ollama
- keeping logs and feed text as local, untrusted input
- verifying AI output against primary sources
- identifying the difference between summary and evidence
- refusing destructive or high-risk actions suggested by AI

Primary files:
- `scripts/ai_guard.py`
- `scripts/learning_digest.py`
- `intel/learning_summary.md`
- `intel/learning_digest.md`

### Module 6: Safe lab and decoy environment

Focus: practice in an isolated environment, never on a real home system.

Topics:
- virtual machine isolation
- offline-first decoy design
- removing shared folders, clipboard, and sensitive host data
- snapshot-based recovery and lab hygiene

Primary files:
- `docs/safe-decoy-vm.md`
- `docs/home-user-incident-playbook.md`

## Teaching principles

- A warning or article is not proof of compromise.
- Local security review is a starting point, not a verdict.
- AI should summarize, explain, and warn, not act on its own.
- Details should be checked against primary sources and official guidance.
- Recovery and backup are more important than heroic “cleanup” attempts.
- A safe home user is usually one who has fewer unnecessary exposures and a clear recovery plan.

## Suggested beginner workflow

1. Read `README.md` and `learning/README.md`.
2. Review `linux-mint-home-hardening.md` and apply the obviously safe items.
3. Run `scripts/security_scan.sh` and inspect the report.
4. Run `scripts/risk_review.py` to see whether the local scan suggests a need for human review.
5. Run `scripts/daily_intel.py` to fetch public advisories and news.
6. Run `scripts/learning_digest.py` to create a local digest of case studies and feed entries.
7. Run `scripts/ai_guard.py` to generate a cautious summary.
8. Read the primary source links from important advisories before making any system changes.
9. Keep a backup and recovery plan in place.
10. Practice in an isolated VM before trying anything more advanced.

## Safety mandate

This curriculum avoids destructive, exploitative, or targeting behavior. It teaches defensively:
- reduce exposure
- keep backups
- detect anomalies
- verify sources
- isolate experiments
- recover carefully
- never attack or target systems without explicit authorization

The purpose is educational and protective, not adversarial.
