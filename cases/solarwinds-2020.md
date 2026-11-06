# SolarWinds Orion supply-chain compromise (2020)

## Incident summary

CISA's advisory describes a compromise involving SolarWinds Orion software and malicious activity affecting organizations. The event illustrates how a trusted software supply chain can become a route into downstream environments. Consult the advisory for scope, indicators, and response guidance; this note intentionally omits operational intrusion detail.

**Primary source:** [CISA Alert AA20-352A: Advanced Persistent Threat Compromise of Government Agencies, Critical Infrastructure, and Private Sector Organizations](https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-352a)

## Defensive lesson

Trust in a vendor or update channel is not a substitute for layered security. Keep an inventory of installed software and update sources, apply verified vendor guidance, and use supported software. For organizations, limit privileges and monitor for unexpected behavior even from trusted applications.

## Safe checks for a home user

- Review installed applications and remove software you no longer use.
- Install updates from the operating system's normal trusted update mechanism or the vendor's official channel.
- Check whether a device or application is still supported; consult its vendor's advisory if a relevant notice appears.
- Do not infer compromise from the incident alone, and do not download purported cleanup tools from links in unsolicited messages.

## Relevance to this project

This case supports learning about software inventory, update trust, and defense in depth. It does not by itself indicate risk to a typical Linux Mint installation.
