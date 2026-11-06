# Linux Mint home hardening checklist

This checklist is for a home user who wants to reduce the chance of a common compromise without turning the machine into a public target. It is intentionally practical and non-invasive. The goal is to reduce exposure, protect data, and avoid introducing confusing or fragile configuration changes.

## 1. Start with the basics

- Keep the operating system updated through the official Mint update mechanism.
- Keep the browser, browser extensions, and document apps current from official channels.
- Remove software that is no longer used or needed.
- Review the list of installed applications and ask: "Do I know why this is installed?"
- If a program is not needed, uninstall it rather than leaving it dormant.

## 2. Use local security boundaries

- Leave the firewall enabled on the Mint machine.
- Do not expose services to the public internet unless there is a clear, intentional reason and the system is protected appropriately.
- Avoid opening ports for remote desktop, file-sharing, or management unless you understand the risk and have a need.
- Consider keeping personal files, media, and sensitive documents on a separate partition or dedicated storage location if you want a clearer recovery boundary.

## 3. Protect accounts and access

- Use a unique password for each major account and service.
- Prefer a password manager for strong, unique passwords.
- Turn on multifactor authentication (MFA) for email, cloud accounts, and important services.
- Use separate accounts for daily work and administration when possible.
- Avoid logging in to sensitive accounts from the same browser profile used for public websites.

## 4. Reduce phishing and social-engineering damage

- Treat unexpected email, text, or chat messages as suspicious until verified by an independent channel.
- Check the sender domain or domain ownership rather than trusting the display name.
- Prefer direct navigation to a website instead of clicking a link in a message.
- Do not open unexpected attachments or run scripts from unknown sources.
- Keep browser download prompts explicit and avoid automatic execution of downloaded files.

## 5. Control software installation

- Install software only from official repositories or official vendor packages.
- Verify an installer or package source before running it.
- Disable or remove browser extensions you do not understand.
- Be careful with scripts copied from a blog, forum, or message board; these can contain malicious actions or drift from the original context.

## 6. Protect personal data

- Keep a current backup of important files.
- Store the backup outside the normal daily working area if you can.
- Test the restore process occasionally so a backup is usable when needed.
- Keep a copy of important contacts, documents, and files on storage that is not constantly online to your laptop or desktop.

## 7. Watch for suspicious local signs

- Unexpected prompts, browser redirects, new startup services, or program installations are worth checking.
- Check the system update logs and the local package manager output when you see unusual behavior.
- Review enabled services and startup entries if a system has become slow, unstable, or unexpectedly noisy.
- Monitor for unusual authentication failures or repeated login events in your local logs if you run an account or service for which that is relevant.

## 8. Decide when to investigate

- Use the local scan and the risk review script as a starting point, not as proof.
- If something seems unusual, confirm it with a trusted system check or official vendor documentation rather than following a random forum recommendation.
- Use a separate, isolated lab or VM for testing anything unusual, especially if it involves software changes or network behavior.

## 9. Recovery mindset

- If your machine is compromised, the first practical step is often to disconnect or isolate it from the network, preserve evidence, and then recover through a known-good backup or reinstall path.
- Recovery is easier when you have a record of software you installed, your key accounts, and a tested backup strategy.

This is a home-user checklist, not a complete enterprise security plan. The purpose is to reduce common risks, improve habit and awareness, and keep the operating model realistic and manageable.
