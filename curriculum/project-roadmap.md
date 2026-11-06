# Project roadmap

This roadmap keeps `unhackable` focused on being a useful, honest learning resource for people and local AI assistants.

## Foundation

- Local, report-only Linux Mint scan.
- Cautious risk-review priority with `LOW`, `MEDIUM`, `HIGH`, and `UNKNOWN` outcomes.
- Public feed digest and curated incident case studies.
- Defensive learning modules for phishing, ransomware, hardening, and recovery.
- Optional best-effort local failed-login desktop notifications.
- Guidance for provider-managed online-account sign-in alerts.
- AI safeguards and isolated VM learning guidance.

## Next improvements

- Add automated tests using synthetic scan reports and journal records; never require real credentials or external targets.
- Improve scan parsing with structured output and explicit collection status instead of relying only on text matching.
- Add source freshness and provenance fields to the learning digest.
- Expand case studies from verified primary sources, recording publication date and review date.
- Document supported Mint versions, desktop notification requirements, and journald permission differences.
- Add an accessibility review for notification wording, screen readers, and quiet-hours behavior.

## Out of scope

- Guaranteeing that a PC is unhackable.
- Automatically blocking addresses, disabling accounts, deleting files, or remediating findings.
- Collecting online account credentials, MFA codes, session tokens, or recovery keys.
- Scanning third-party targets or providing working exploit and malware code.
- Sending raw logs or user data to remote AI services by default.

All proposed features should remain transparent, opt-in, local-first, non-destructive, and understandable to a home user.
