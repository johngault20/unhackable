#!/usr/bin/env python3
"""Create a cautious, report-only review priority from the local scan output."""

import sys
from datetime import datetime, timezone
from pathlib import Path


WILDCARD_MARKERS = ("0.0.0.0:", "*:", "[::]:", ":::" )


def section(text: str, heading: str) -> str:
    marker = f"--- {heading} ---"
    start = text.find(marker)
    if start < 0:
        return ""
    start += len(marker)
    end = text.find("\n--- ", start)
    return text[start:] if end < 0 else text[start:end]


def evaluate(report: str):
    firewall = section(report, "Firewall").lower()
    sockets = section(report, "Listening sockets")
    upgrades = section(report, "Upgradable packages")

    if not report.strip() or not firewall or not sockets or not upgrades:
        return "UNKNOWN", ["The scan report or one or more required sections are missing."], [
            "Run scripts/security_scan.sh and check whether firewall, listening-socket, and package sections were collected."
        ]

    firewall_active = "status: active" in firewall
    firewall_inactive = "status: inactive" in firewall
    if not firewall_active and not firewall_inactive:
        return "UNKNOWN", ["Firewall status could not be determined from the report."], [
            "Check firewall status using your Linux Mint firewall settings; this script does not change it."
        ]

    socket_lines = [line.strip() for line in sockets.splitlines() if line.strip()]
    # The first line is usually the ss table header. Match only rows with a wildcard
    # local-address marker; a wildcard bind does not establish internet reachability.
    wildcard_rows = [
        line for line in socket_lines
        if any(marker in line for marker in WILDCARD_MARKERS)
    ]
    upgrade_lines = [line.strip() for line in upgrades.splitlines() if line.strip()]
    package_rows = [
        line for line in upgrade_lines
        if not line.lower().startswith("listing...")
        and not line.lower().startswith("warning:")
        and not line.lower().startswith("reading package lists")
        and not line.lower().startswith("building dependency tree")
        and not line.lower().startswith("reading state information")
    ]
    has_upgrades = bool(package_rows)

    findings = []
    if firewall_inactive:
        findings.append("The scan reports the UFW firewall as inactive.")
    else:
        findings.append("The scan reports the UFW firewall as active.")
    if wildcard_rows:
        findings.append(
            f"The socket report contains {len(wildcard_rows)} wildcard-bound listener row(s); "
            "a wildcard bind alone does not mean a service is reachable from the internet."
        )
    else:
        findings.append("No wildcard-bound listening socket was identified by this simple text check.")
    if has_upgrades:
        findings.append("The package section appears to list updates; review them using the normal trusted update tools.")
    else:
        findings.append("No upgradable package rows were identified in the scan output.")

    if firewall_inactive and wildcard_rows:
        level = "HIGH"
        rationale = "Combined indicators warrant prompt human review; this is not proof of exposure or compromise."
    elif firewall_inactive or wildcard_rows or has_upgrades:
        level = "MEDIUM"
        rationale = "At least one item merits routine human review; the scan cannot establish exploitability."
    else:
        level = "LOW"
        rationale = "No indicators matched this small rule set. LOW is not a security guarantee."

    next_checks = []
    if firewall_inactive:
        next_checks.append("Review firewall configuration in Linux Mint and enable an appropriate policy if suitable for your setup.")
    if wildcard_rows:
        next_checks.append("Identify each wildcard-bound service and confirm it is needed and intended; check its own access controls.")
    if has_upgrades:
        next_checks.append("Review available updates and apply relevant updates through trusted system tools after normal checks.")
    if not next_checks:
        next_checks.append("Continue routine updates and review the original scan; this report cannot detect every security issue.")

    findings.insert(0, rationale)
    return level, findings, next_checks


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    scan_path = repo_root / "logs" / "last_scan.txt"
    output_path = repo_root / "intel" / "risk_review.md"

    if not scan_path.exists():
        report = ""
    else:
        report = scan_path.read_text(encoding="utf-8", errors="replace")

    level, findings, next_checks = evaluate(report)
    lines = [
        "# Local scan review priority",
        "",
        f"Generated at: {datetime.now(timezone.utc).isoformat()}",
        "",
        f"**Result: {level}**",
        "",
        "> This is a transparent, limited review of scan text—not a validated security rating, diagnosis, or proof of compromise. It does not test reachability or change system settings.",
        "",
        "## Evidence and interpretation",
        "",
    ]
    lines.extend(f"- {item}" for item in findings)
    lines.extend(["", "## Suggested human review", ""])
    lines.extend(f"- {item}" for item in next_checks)
    lines.extend([
        "",
        "## Limitations",
        "",
        "This small rule set can miss issues and can flag benign services or updates. A wildcard-bound socket is not necessarily reachable from the internet; routing, NAT, host firewall rules, and service configuration matter. LOW does not mean safe, and HIGH does not mean compromised. Verify findings with trusted system documentation or a qualified administrator.",
        "",
    ])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    print(f"\n[unhackable] Saved review to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
