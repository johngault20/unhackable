# Minimum safe password policy for personal accounts

This is a practical baseline for personal accounts, not a universal compliance standard. Follow the service's current requirements and use a password manager where possible.

## Baseline

1. **Unique per account:** Never reuse a password across services. Reuse lets one leaked credential put other accounts at risk.
2. **Prefer generated passwords:** Let a reputable password manager create a long, random value that the service accepts. Do not invent predictable substitutions or add a year to a familiar word.
3. **For memorable passwords:** Use a long passphrase made of unrelated words; avoid quotes, song lyrics, personal details, and familiar phrases. Longer is generally better, but unpredictability and uniqueness matter too.
4. **No arbitrary rotation:** Change a password promptly if it may have been exposed, reused, phished, or disclosed by a service. Routine forced changes can encourage predictable variations; follow provider guidance.
5. **Use MFA:** Enable multifactor authentication on email, password-manager, financial, and other important accounts. Prefer passkeys or security keys where supported; otherwise use an authenticator app. SMS may be better than no second factor but is more exposed to phone-number takeover.
6. **Protect recovery:** Secure recovery email and phone accounts with unique credentials and MFA. Store recovery codes in a safe place separate from the device where practical.
7. **Avoid password sharing:** Do not send passwords in chat or email. Use a password manager's secure sharing feature when necessary.
8. **Check breach notices safely:** Use the provider's official account security page or reputable breach-notification guidance. Never submit an existing password to a random checker.

## About minimum length

Length requirements vary by provider and authentication design. As a personal rule of thumb, prefer a password-manager-generated value of at least 16 characters where accepted, or a longer memorable passphrase. Do not interpret that number as a guarantee or as a prediction of cracking time. Some services impose limits or normalize characters; check their official documentation.

## If you think a password was exposed

- From a trusted device, open the service's official app or type its known address yourself.
- Change the affected password to a new, unique value; do not test it by repeatedly attempting logins.
- If reused, change it anywhere else it was used, prioritizing email and password-manager accounts.
- Review active sessions and sign-in activity; sign out unfamiliar sessions if the provider offers that option.
- Enable MFA and provider sign-in notifications.
- Treat unexpected “Was this you?” messages cautiously. Do not click surprise links; navigate to the provider directly.

This project never asks for account passwords, MFA codes, session cookies, or recovery codes.
