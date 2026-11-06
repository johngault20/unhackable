#!/usr/bin/env python3
"""Show local desktop notifications for authentication failures in journald.

This is a best-effort local monitor, not an account-provider alert or an
intrusion detector. It reads the system journal using the current user's
permissions and never sends logs or credentials over the network.
"""

import json
import re
import shutil
import subprocess
import sys
from typing import Optional

FAILURE_MARKERS = (
    "failed password",
    "authentication failure",
    "authentication failed",
    "failed login",
    "invalid user",
    "login incorrect",
    "pam authentication error",
)
AUTH_IDENTIFIERS = {
    "sshd",
    "sudo",
    "login",
    "lightdm",
    "gdm-password",
    "gdm-session-worker",
    "systemd-logind",
}


def clean_display(value: str, limit: int = 72) -> str:
    """Remove control characters and limit untrusted journal text for display."""
    value = "".join(char for char in value if char.isprintable())
    return value[:limit]


def is_auth_failure(record: dict) -> bool:
    message = str(record.get("MESSAGE", "")).lower()
    if not any(marker in message for marker in FAILURE_MARKERS):
        return False

    identifier = str(record.get("SYSLOG_IDENTIFIER", "")).lower()
    command = str(record.get("_COMM", "")).lower()
    unit = str(record.get("_SYSTEMD_UNIT", "")).lower()
    return (
        identifier in AUTH_IDENTIFIERS
        or command in AUTH_IDENTIFIERS
        or any(name in unit for name in ("ssh", "login", "display-manager"))
        or "pam_unix" in message
    )


def account_from_message(message: str) -> Optional[str]:
    patterns = (
        r"failed password for (?:invalid user )?([^\s]+)",
        r"invalid user ([^\s]+)",
        r"user[= ]+([^\s;]+)",
        r"for user ([^\s]+)",
    )
    for pattern in patterns:
        match = re.search(pattern, message, flags=re.IGNORECASE)
        if match:
            return clean_display(match.group(1))
    return None


def notify(service: str, account: Optional[str]) -> None:
    title = "Failed sign-in recorded"
    service = clean_display(service or "authentication service", 48)
    body = f"A failed sign-in was recorded on this PC ({service})."
    if account:
        body += f" Account: {account}."
    body += " If this was unexpected, review local access and secure the relevant account."

    notify_send = shutil.which("notify-send")
    if notify_send:
        try:
            subprocess.run(
                [notify_send, "--urgency=critical", title, body],
                check=False,
                timeout=5,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return
        except (OSError, subprocess.TimeoutExpired):
            pass
    print(f"[unhackable] {title}: {body}", flush=True)


def main() -> int:
    journalctl = shutil.which("journalctl")
    if not journalctl:
        print("[unhackable] journalctl is unavailable; this monitor requires systemd journal access.", file=sys.stderr)
        return 1

    command = [journalctl, "--follow", "--lines=0", "--output=json", "--no-pager"]
    try:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            bufsize=1,
        )
    except OSError as exc:
        print(f"[unhackable] Could not start journal monitor: {exc}", file=sys.stderr)
        return 1

    assert process.stdout is not None
    try:
        for line in process.stdout:
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not isinstance(record, dict) or not is_auth_failure(record):
                continue
            identifier = str(record.get("SYSLOG_IDENTIFIER") or record.get("_COMM") or "authentication")
            message = str(record.get("MESSAGE", ""))
            notify(identifier, account_from_message(message))
    except KeyboardInterrupt:
        print("\n[unhackable] Login alert monitor stopped.")
    finally:
        process.terminate()
        try:
            process.wait(timeout=3)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()

    if process.returncode not in (0, -15, 143):
        print(
            "[unhackable] Journal monitor exited. Check that your user can read authentication events; "
            "do not run this project as root to bypass permissions.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
