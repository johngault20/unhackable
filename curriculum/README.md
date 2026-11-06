# unhackable curriculum

A defensive cybersecurity learning path for home users and local AI assistants. It uses public advisories, real-world case studies, and safe local exercises to teach safer habits—not how to attack systems.

## Course sequence

1. **Security mindset and vocabulary** — Read the project [README](../README.md), [glossary](glossary.md), and [learning guide](../learning/README.md). Explain why missing evidence is `UNKNOWN`, not safe.
2. **Attack patterns, defender’s view** — Read [how attack code works defensively](../learning/how-attack-code-works-defensively.md), [phishing and credential abuse](../learning/phishing-and-credential-abuse.md), and the [pattern catalogue](attack-pattern-catalogue.md). Describe prevention and safe checks, not attack steps.
3. **Real incidents** — Read the [case library](../cases/README.md) and [lessons matrix](../cases/lessons-matrix.md). Separate source-backed facts from your interpretation.
4. **Linux Mint baseline** — Review [home hardening](../learning/linux-mint-home-hardening.md), run `bash scripts/security_scan.sh`, inspect its report, then run `python3 scripts/risk_review.py`.
5. **Accounts and sign-in alerts** — Read [login alert guidance](../docs/login-alerts.md). Configure “Was this you?” alerts and MFA with account providers; optionally use the local failed-login monitor. Never provide this project account credentials or authentication codes.
6. **Password practices** — Read the [minimum policy](../learning/password-policy.md), [strong password/passphrase guide](../learning/strong-password-policy.md), [MFA explanation](../learning/mfa-why-it-matters.md), and [fictional patterns](../learning/password-pattern-examples.md). Optionally assess a *new candidate* locally with `python3 scripts/password_check.py`, only on a trusted device. It does not crack, reveal, or transmit the value.
7. **Backups and recovery** — Read [ransomware and backups](../learning/ransomware-and-backups.md) and the [home-user response playbook](../docs/home-user-incident-playbook.md). Verify you can restore a file.
8. **AI-assisted learning** — Read [AI safety rules](ai-safety-rules.md). Generate a digest and local model summary; verify claims against original sources.
9. **Safe lab practice** — Follow the [offline-first VM plan](../docs/safe-decoy-vm.md). Practice only with benign learning material in isolated, authorized environments.

## Outcomes

Learners should be able to explain common attacks at a high level, improve basic account and device hygiene, interpret local scan output cautiously, distinguish public news from local evidence, protect secrets, use MFA and backups, and recover calmly.

## Core rules

This curriculum avoids exploit instructions, malware, credential theft, evasion, destructive actions, and targeting guidance. Password tools must not transmit or persist entered secrets. AI is advisory and must not act autonomously or change settings. Verify claims and use human judgment.
