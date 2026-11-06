# unhackable curriculum

A defensive cybersecurity learning path for home users and local AI assistants. It uses public advisories, incident case studies, and safe local exercises to teach safer habits—not to teach people how to attack systems.

> **Mission:** Learn how common security failures happen, reduce risk on your own computer, and be prepared to recover. `unhackable` is an aspirational name, not a guarantee.

## Learning outcomes

By the end, learners should be able to:

- Explain common attacker behavior at a high level without reproducing it.
- Distinguish public incident reporting from evidence about their own device.
- Review basic Linux Mint security information and recognize missing data.
- Improve account, update, firewall, and backup habits.
- Configure sign-in alerts with online account providers and understand the limits of local login monitoring.
- Assess a candidate password locally without exposing it to a website or service.
- Respond calmly to suspicious activity and know when to seek help.
- Use local AI as an assistant while verifying claims and protecting private data.

## Course sequence

### 1. Security mindset and vocabulary

**Learn:** risk reduction, uncertainty, evidence, authentication, least privilege, and defense in depth.

**Read:** [Project README](../README.md), [glossary](glossary.md), [learning guide](../learning/README.md).

**Practice:** Explain why `UNKNOWN` differs from `LOW`, and why a public advisory alone does not show that your PC is affected.

### 2. Common attack patterns—defender’s view

**Learn:** phishing, credential abuse, vulnerable services, supply-chain compromise, persistence, ransomware, and data theft at a high level.

**Read:** [Defensive code overview](../learning/how-attack-code-works-defensively.md), [phishing and credentials](../learning/phishing-and-credential-abuse.md), [attack-pattern catalogue](attack-pattern-catalogue.md).

**Practice:** For each pattern, name a prevention measure and a safe follow-up check. Do not run exploit code or test systems without authorization.

### 3. Real-world incidents

**Learn:** Separate source-backed facts from defensive interpretation.

**Read:** [Incident cases](../cases/README.md) and [lessons matrix](../cases/lessons-matrix.md).

**Practice:** For one case, identify one fact stated by the primary source, one defensive lesson, and one reason it might not apply to a home Mint PC.

### 4. Linux Mint baseline and hardening

**Learn:** Updates, firewall awareness, software inventory, startup services, listening sockets, browser hygiene, and recovery.

**Read:** [Linux Mint home checklist](../learning/linux-mint-home-hardening.md).

**Practice:** Run `bash scripts/security_scan.sh`, inspect `logs/last_scan.txt`, and run `python3 scripts/risk_review.py`. Treat missing information as unknown and review findings before changing anything.

### 5. Account security and login alerts

**Learn:** Local computer authentication differs from sign-ins to email, banking, and cloud services. The provider is the right source for online-account “Was this you?” alerts.

**Read:** [Login alert guide](../docs/login-alerts.md) and [phishing and credential abuse](../learning/phishing-and-credential-abuse.md).

**Practice:** Enable sign-in notifications and MFA through the official settings of important account providers. Optionally run `python3 scripts/login_alert.py` for selected local failed-authentication events. Never give the project passwords, MFA codes, session cookies, or recovery codes.

### 6. Conservative offline password estimate

**Learn:** Password length and uniqueness matter; no simple strength meter can guarantee safety or predict how quickly a password could be guessed. A password entered into a website or untrusted application may be exposed.

**Read:** [Offline password checker guide](../learning/password-checker.md).

**Practice:** On a trusted personal device, run `python3 scripts/password_check.py` and type a candidate into the masked field. The script estimates locally and does not transmit, print, or save the value. Do not use a shared or suspected-compromised device, and never enter a password into online testers, chat, or issue reports.

### 7. Ransomware, backups, and recovery

**Learn:** Availability, protected backups, restore tests, and calm first response.

**Read:** [Ransomware and backups](../learning/ransomware-and-backups.md) and [home-user response playbook](../docs/home-user-incident-playbook.md).

**Practice:** Identify important files, confirm they are backed up, and check that you know how to restore a copy.

### 8. AI-assisted learning

**Learn:** Untrusted input, source verification, model limitations, and human oversight.

**Read:** [AI safety rules](ai-safety-rules.md) and [learning guide](../learning/README.md).

**Practice:** Generate a local digest and AI summary, then verify at least one claim against its original source. Avoid sending sensitive logs to services you do not control.

### 9. Safe lab practice

**Learn:** VM isolation, clean snapshots, no personal data in a lab, and authorized practice.

**Read:** [Safe decoy VM plan](../docs/safe-decoy-vm.md) and [project roadmap](project-roadmap.md).

**Practice:** Confirm network mode and host-integration settings before any exercise. Use benign, intentionally designed training material only.

## Suggested beginner workflow

1. Read the mission and glossary.
2. Review the hardening checklist and account-provider security settings.
3. Run the local scan and inspect its raw report.
4. Generate the review priority; treat it as a prompt for human review, not a verdict.
5. Optionally run the local login alert monitor and check whether it can read journal events.
6. Use the offline password checker only on a trusted device and only if needed.
7. Fetch public intelligence, build a digest, and compare claims with original advisories.
8. Study an incident case and review backup readiness.
9. Keep any lab isolated and authorized.

## Teaching and safety rules

This curriculum avoids exploit instructions, malware, credential theft, evasion, destructive actions, and targeting guidance. Password tools must not transmit or persist entered secrets, and should only be used on a trusted device. AI may summarize and explain, but must not act autonomously, make unsupported compromise claims, or change system settings. People remain responsible for verifying sources and choosing actions.
