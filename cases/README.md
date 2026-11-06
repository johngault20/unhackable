# Incident learning library

These short case studies use public incidents to teach defensive principles. They focus on what defenders can learn, not on reproducing attacks. Read the linked original advisories for authoritative detail; summaries and recommendations here are educational and may omit context.

## How to use a case

For each incident, ask:

1. What does the cited source actually establish?
2. What security weakness or operational dependency is relevant to the incident?
3. What can I safely review on systems I own or administer?
4. What evidence would be needed before concluding that my own system is affected?

A vulnerability or incident being in the news does not mean your computer is affected. Check software versions and vendor guidance before deciding whether a mitigation applies. Do not copy exploit instructions or test public systems.

## Cases

- [SolarWinds Orion supply-chain compromise (2020)](solarwinds-2020.md) — vendor and software-update trust.
- [Colonial Pipeline ransomware incident (2021)](colonial-pipeline-2021.md) — resilience, remote access, and recovery readiness.
- [MOVEit Transfer exploitation campaign (2023)](moveit-2023.md) — asset inventory, timely vendor guidance, and response.

## Project limitations

The cases are curated notes, not an exhaustive or continuously updated incident database. Public feeds can be incomplete, delayed, noisy, or wrong. The local AI may misread source material; verify any specific claim against the linked source. This library does not assess whether a particular incident affected your device.
