# How attackers use code: a defender-focused overview

This lesson explains common behavior patterns without providing working attack code, exploit instructions, or steps for targeting a system. Real intrusions differ, and public reports may not reveal every detail. Treat these as broad concepts, not a checklist for reproducing an attack.

## Common patterns and defensive opportunities

| Broad behavior | What software may do (conceptually) | Defensive focus |
| --- | --- | --- |
| Reconnaissance | Collect publicly visible information or identify services that an operator is authorized to assess. | Minimize public information and unnecessary services; inventory what you intentionally expose. Do not probe systems without permission. |
| Initial access | Abuse a stolen password, trick a person, exploit a software flaw, or misuse a trusted update or application. | Use unique passwords and MFA, phishing awareness, timely updates, and trusted software sources. |
| Execution | Cause a program or script to run through a compromised account or vulnerable application. | Use standard accounts for daily work, install software only from trusted sources, and review unexpected prompts or startup items. |
| Persistence | Arrange for access to survive a reboot or account session. | Review enabled services and startup applications when investigating a concern; compare changes with known software installs. |
| Discovery and lateral movement | Enumerate accessible resources and attempt to reach other accounts or devices. | Separate devices and accounts, restrict privileges, and keep guest or IoT devices away from sensitive systems where practical. |
| Collection and exfiltration | Gather files or credentials and attempt to send information out. | Protect sensitive data, use reputable endpoint protections, review unusual account activity, and limit access to what each account needs. |
| Impact | Disrupt systems, encrypt or delete data, or misuse resources. | Keep tested backups, patch systems, use least privilege, and maintain a recovery plan. |

These categories resemble common incident-response frameworks, but they are not proof that any specific event followed every phase. A log entry or unusual process can have benign explanations and needs context.

## A safe coding example: defensive log review

A defender can use code to count authentication failures in logs they are authorized to inspect. This intentionally does not attempt logins, guess passwords, contact other machines, or block anyone. The project scan already gathers a limited local log excerpt; the example below illustrates how a defensive script can summarize lines without taking action:

```python
from pathlib import Path

log_path = Path("/var/log/auth.log")
markers = ("Failed password", "Invalid user")

if not log_path.is_file():
    print("Authentication log is unavailable; no conclusion can be drawn.")
else:
    matches = [
        line.rstrip()
        for line in log_path.read_text(encoding="utf-8", errors="replace").splitlines()
        if any(marker in line for marker in markers)
    ]
    print(f"Found {len(matches)} matching local log line(s). Review context manually.")
```

This simple example is incomplete: distributions may use journald, permissions may prevent reading the file, and failed logins can be routine or misconfigured services. Counts are not proof of compromise. Do not publish logs without removing usernames, addresses, hostnames, and other private details.

## What this project intentionally avoids

- Code that exploits vulnerabilities, steals credentials, deploys malware, evades detection, or persists on systems.
- Instructions for targeting public addresses or systems you do not own.
- Automatic blocking, deletion, or remediation based on an AI guess.

The learning goal is to understand defensive controls and incident response, not to reproduce harm. Practice only in an authorized, isolated lab and use benign training material.
