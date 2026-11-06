# Attack-pattern catalogue

This catalogue groups common attacker patterns into defensive categories. Each item teaches the pattern, the real-world examples that often show it, and the primary defensive control. It is intentionally high-level and non-operational. No exploit steps or malicious code are included.

## 1. Phishing and social engineering

Observed pattern:
- malicious messages impersonate trusted people or services
- attackers push urgency, fear, or curiosity
- victims are tricked into clicking links or opening files

Defensive controls:
- MFA on accounts and recovery channels
- password manager and unique passwords
- direct navigation to known websites
- browser extension review and safe email habits

Related files:
- `learning/phishing-and-credential-abuse.md`

## 2. Credential abuse and reuse

Observed pattern:
- stolen credentials are reused on multiple services
- password reuse makes a single compromise more damaging
- identity theft often follows a stolen email or password

Defensive controls:
- unique passwords
- MFA
- account recovery hygiene
- reviewing suspicious sign-ins

## 3. Vulnerable public services

Observed pattern:
- a service is reachable and exposed to exploitation
- an attacker sends unexpected input to trigger a vulnerability
- urgent patching is needed when a vendor advisory is published

Defensive controls:
- patch management
- service inventory
- exposure reduction
- official vendor advisories

Related files:
- `cases/moveit-2023.md`
- `cases/exchange-2021.md`

## 4. Supply-chain compromise

Observed pattern:
- trusted software or update channels are abused
- a user or enterprise trusts a dependency that later turns malicious
- downstream victims are affected through software they already installed

Defensive controls:
- software inventory
- update provenance
- least privilege and vendor verification
- trust decisions based on code and process integrity

Related files:
- `cases/solarwinds-2020.md`

## 5. Malware execution and persistence

Observed pattern:
- malicious code runs from a downloaded file, script, or browser path
- persistence is established to survive reboots or sessions
- a malicious process keeps operating beyond the initial trigger

Defensive controls:
- install only trusted software
- review startup entries and auto-executing processes
- run a clean restore path when necessary
- keep backups and a recovery plan

## 6. Ransomware and availability attacks

Observed pattern:
- files are encrypted or data becomes unusable
- systems are disrupted for business or personal operation
- the attacker demands payment or disrupts data access

Defensive controls:
- backups
- recovery drills
- least privilege and segmentation
- careful restoration from known-good states

Related files:
- `cases/colonial-pipeline-2021.md`
- `cases/wannacry-2017.md`
- `learning/ransomware-and-backups.md`

## 7. Lateral movement and privilege abuse

Observed pattern:
- a compromised account or host is used to reach other systems or accounts
- weak privilege boundaries increase the blast radius
- internal trust is abused

Defensive controls:
- separate accounts and roles
- endpoint and service segmentation
- reviewing unexpected SSH or remote-access events
- restricting shared credentials

## 8. Data theft and exfiltration

Observed pattern:
- attacker collects files, credentials, or sensitive data
- data is transmitted off the target system
- the victim sees a loss of confidentiality, not just disruption

Defensive controls:
- limit sensitive data exposure
- cloud and file access controls
- account monitoring
- backup integrity and recovery planning

## 9. Misconfiguration and weak defaults

Observed pattern:
- a service is left open or too permissive
- default security settings are not tightened
- trust boundaries are too broad

Defensive controls:
- firewall awareness
- service inventory
- least privilege
- regular local review and baseline understanding

## 10. Warning signs a home user can watch for

- browser redirects or suspicious prompts
- unknown startup items or services
- unexpected password reset messages
- repeated authentication failures or locks
- unusual network activity or inaccessible files
- sudden loss of access or restored files not matching your normal pattern

The catalogue is educational. It does not include exploit details or attack instructions. The goal is to understand patterns and the corresponding defensive controls.
