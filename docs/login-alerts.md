# Login alerts: local computer vs online accounts

`unhackable` can optionally display a desktop notification when it observes a failed authentication event in the Linux system journal. This is a local, best-effort monitor for this computer. It is not guaranteed to capture every login path, and it does not monitor sign-ins to websites, email, cloud accounts, or other providers.

## Run once

On a Linux Mint desktop with `journalctl` and `notify-send` available:

```bash
python3 scripts/login_alert.py
```

Leave it running in a terminal to receive notifications. Stop it with `Ctrl+C`. If desktop notifications are unavailable, matching events are printed to the terminal. The current user must already have permission to read the relevant journal entries. If access is denied, use your normal system administration process to review permissions; do not run the whole project as root just to enable alerts.

## Optional user service

The example unit is `config/unhackable-login-alert.service`. Review it first and change the `ExecStart` path if your checkout is not `~/unhackable`. Then install and start it for your user:

```bash
mkdir -p ~/.config/systemd/user
cp config/unhackable-login-alert.service ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now unhackable-login-alert.service
```

Check its status with:

```bash
systemctl --user status unhackable-login-alert.service
```

Stop and disable it with:

```bash
systemctl --user disable --now unhackable-login-alert.service
```

This user service runs without root privileges. Journal permissions vary by distribution and configuration; if it cannot read events, it should fail rather than escalate privileges. Desktop notifications generally require an active graphical user session.

## What the alert means

The script watches new journal records and looks for common authentication-failure wording associated with local services such as SSH, sudo, login, or a display manager. It displays the service and, when safely parsed, the account name. It intentionally does not display raw log lines, remote addresses, or a clickable link. Matching is heuristic: it can miss events or produce false positives. A failed attempt is not proof of a successful intrusion; repeated failures may be routine background noise or a misconfiguration.

The monitor does not change firewall rules, block addresses, disable accounts, send email, or transmit journal data. It does not keep a history of alerts. Protect local logs and avoid posting usernames or other private details publicly.

## “Was this you?” alerts for online accounts

For email, banking, social, cloud, or other online accounts, enable sign-in notifications in that provider's official account security settings. Those providers have the account-side information needed to identify a new or unusual sign-in. `unhackable` cannot securely verify website sign-ins, and it should never ask for or store your passwords, MFA codes, session cookies, recovery codes, or account tokens. Do not build login links or ask users to click a link in an unexpected alert; open the provider's official app or type its known address yourself to review activity.

A provider alert and this local monitor answer different questions: the provider alert concerns access to an online account, while this monitor reports selected failed authentication events on the Linux computer.
