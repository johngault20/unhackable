# Incident-to-defense learning matrix

Use this as a discussion guide, not as an automated threat match. A real incident may involve conditions that do not apply to a home Linux computer. Verify product-specific advice with the linked vendor or government advisory.

| Incident pattern | Case study | Defensive concept | Safe personal review |
| --- | --- | --- | --- |
| Compromise in a trusted software supply chain | [SolarWinds Orion](solarwinds-2020.md) | Software inventory, update provenance, and least privilege | Keep an inventory of applications; use trusted update channels; remove software that is no longer needed. |
| Ransomware disrupting operations | [Colonial Pipeline](colonial-pipeline-2021.md) | Availability, account security, and recovery | Maintain protected backups; test restoring files; use unique passwords and MFA where available. |
| Vulnerable file-transfer product targeted | [MOVEit Transfer](moveit-2023.md) | Asset inventory and vendor-advisory response | Check whether you actually use the named product; follow its official security notice; avoid unnecessary public services. |
| Ransomware spreading across vulnerable or poorly separated systems | [WannaCry](wannacry-2017.md) | Patching, service reduction, and segmentation | Install supported updates; review services you use; keep restorable backups. |
| Vulnerable internet-facing enterprise service compromised | [Microsoft Exchange](exchange-2021.md) | Exposure management and urgent advisory response | Check whether you operate the named product before applying product-specific guidance. |

## Applying lessons responsibly

1. Identify whether the affected product, service, or condition exists in your own environment.
2. Check the original advisory and current vendor guidance.
3. Prefer low-risk administrative checks and backups before system changes.
4. Do not equate public reporting, a feed match, or an AI-generated observation with evidence of compromise.
5. Do not test systems unless you own them or have explicit authorization.
