### 6. Conservative offline password estimate

**Learn:** Password length and uniqueness matter; no simple strength meter can guarantee safety or predict how quickly a password could be guessed. A password entered into a website or untrusted application may be exposed.

**Read:** [Offline password checker guide](../learning/password-checker.md).

**Practice:** On a trusted personal device, run `python3 scripts/password_check.py` and type a **new candidate**, not a password already used for an account, into the masked field. The script applies a deliberately strict local heuristic and does not transmit, print, or save the value. Do not use a shared or suspected-compromised device, and never enter a password into online testers, chat, or issue reports.
