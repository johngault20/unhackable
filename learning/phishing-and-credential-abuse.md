# Phishing, credential abuse, and account compromise

This lesson explains common real-world failure patterns without teaching how to do harm. It focuses on how an attacker abuses trust and weak security hygiene, and how a home user can reduce exposure.

## Typical attacker flow

1. A user receives a message that looks trustworthy.
2. The message pushes urgency, fear, or curiosity.
3. The user clicks a link or opens an attachment.
4. The malicious content steals credentials, installs malware, or tricks the user into granting access.
5. The attacker reuses the stolen credentials on other services, because many people reuse passwords or use the same email and sign-in patterns across sites.

## Why this works

- People reuse passwords between multiple services.
- Email is often both a communication channel and a recovery channel.
- Attackers rely on urgency and confusion.
- Attackers target trust relationships and weak verification steps.
- A single stolen email password may unlock other accounts if the user has reused it.

## Defensive lessons

- Use a password manager and unique passwords.
- Turn on MFA for email, cloud accounts, and important services.
- Treat unexpected requests to log in, change a password, or approve a push notification as suspect until verified by an independent channel.
- Verify the site you are visiting directly instead of trusting a link in an email.
- Never run scripts or loaders that arrive by email or chat.
- Keep a single recovery email or phone number under your control and ensure it is protected with MFA.

## What to check on your own system

- Review the list of browser extensions and remove anything unknown.
- Check whether your browser has a suspicious homepage, search engine, or extension behavior.
- Review your login activity for major services like email and cloud providers.
- Search for saved credentials or password manager entries that are duplicated or obviously reused.
- Confirm a trusted device is still the one used for sign-ins and not a rogue or unfamiliar browser profile.

## What this project should not do

This project should not teach how to steal credentials, clone sessions, bypass MFA, or automate phishing campaigns. The learning point is simple: attackers rely on trust, weak habits, and common reuse. Defenders reduce that risk by using strong identity controls and checking the source of a message before acting.
