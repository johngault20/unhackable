# Offline password-quality checker

Run the optional graphical checker with:

```bash
python3 scripts/password_check.py
```

It uses a masked Tkinter field and a deliberately strict, local heuristic based on length and obvious patterns. It has no network code and does not write, print, or log the entered candidate. It does not submit login attempts, reveal the candidate, query breach databases, or estimate cracking time.

## Safe use

- Use a **new candidate**, not a password already used for any account.
- Run it only on a trusted, personally controlled device. Do not use it on a shared, public, or suspected-compromised computer.
- Clear the field and close the program when finished. Python cannot guarantee immediate erasure of immutable strings from process memory.
- Never provide account passwords, MFA codes, session cookies, or recovery codes to the project, an AI, or an online tester.

## Interpreting the score

The score is intentionally conservative and educational—not a universal or “real” security rating. It uses simple length and pattern rules and a small common-fragment list. It may miss predictable phrases or flag a benign pattern. It cannot determine whether a candidate has been reused, exposed in a breach, phished, or is accepted by a particular service. A high result is not a guarantee and is not a time-to-guess estimate.

For everyday accounts, prefer a unique, randomly generated password from a reputable password manager and enable MFA where available. Read the [minimum safe policy](password-policy.md), [strong password and passphrase guidance](strong-password-policy.md), [MFA explanation](mfa-why-it-matters.md), and [abstract pattern examples](password-pattern-examples.md).
