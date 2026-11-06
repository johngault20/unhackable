# Ransomware, recovery, and backups

This lesson explains the high-level mechanics of ransomware as a defensive concept. It is not a playbook for carrying out an attack. It focuses on the practical lesson: the easiest way to reduce ransomware damage is to deny the attacker a path to hold you hostage and to ensure you can recover cleanly.

## What ransomware usually tries to do

- Encrypt files or disrupt data availability.
- Spread to other devices or user accounts when access is shared or privileges are weak.
- Hold data hostage while the victim is forced into a recovery decision.
- Use common operating-system and application entry points, not just a single obvious hole.

## Why backups matter more than the ransom note

A good restore plan is often more valuable than a ransom negotiation. A home user can make recovery dramatically easier by maintaining backups that:

- are not continuously connected to the main machine
- are stored on a separate device or cloud destination that is not attached to the main working environment
- are tested periodically
- are not just a copy of the same directory that the ransomware can reach automatically

## Defensive lessons

- Keep important files in more than one place.
- Use MFA on cloud and backup stores where possible.
- Keep your operating system and applications current.
- Use separate accounts for daily use and administration.
- Review logs and unusual file activity if you suspect a machine is behaving oddly.
- Keep a known-good recovery path: reinstall or restore from tested backup rather than improvising.

## Practical personal checks

- Confirm that your most important files are backed up and readable.
- Check whether your backup system is protected by MFA and whether it allows restore tests.
- Review the list of applications and services that automatically start at login.
- Ensure you have a trusted way to disconnect a suspicious machine from the network.
- Keep documentation of your normal setup so you know what to reinstall or restore if there is a problem.

## Safety note

A ransomware incident is serious, but the right response is to isolate, recover, and verify, not to chase the attackers or run random cleanup utilities from untrusted sources. In an emergency, the safest next step is often: disconnect from the network, preserve evidence, and recover from a known-good backup or reinstall path.
