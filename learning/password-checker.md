# Conservative offline password checker

Run the optional graphical checker on a trusted personal computer:

```bash
python3 scripts/password_check.py
```

It shows a live, masked estimate using only local Python code. The password is not transmitted, written to disk, printed, or logged by the program. It uses no external services or breached-password database.

## Why “twice as harsh” is not a real measurement

There is no universal real-world password-strength score that this tool can double. Attack cost depends on whether a password is reused or exposed, the service's authentication protections, the attacker’s guessing strategy, and secure password storage. This checker instead uses deliberately conservative length bands and penalties for a few obvious patterns. Its result is a learning prompt—not a crack-time estimate, breach check, or guarantee.

## Safer password habits

- Prefer a unique, randomly generated password from a reputable password manager, or a long passphrase that is unique to the account.
- Never reuse passwords across important accounts.
- Enable MFA where available, especially for email and password-manager accounts.
- Use online-account sign-in alerts from the provider’s official security settings.
- Never enter real passwords into websites, chats, issue reports, or tools on shared or suspected-compromised devices.

The program handles the candidate in process memory while the window is open. Clear it or close the window when done. Python cannot guarantee immediate erasure of immutable strings from memory. The checker intentionally does not reveal the entered password, attempt logins, crack it, or send it anywhere.
