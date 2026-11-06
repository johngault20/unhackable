# Home-user incident response playbook

This document is meant to help a person respond calmly and responsibly when they suspect something unusual on a home computer. It is not a general incident-response plan for large companies. It focuses on safe first steps, evidence preservation, and practical recovery.

## 1. Confirm the concern

Before taking action, ask:

- Did I see a suspicious website, pop-up, or message?
- Did a program appear that I did not expect?
- Did a system update or browser extension change without my input?
- Did I click a link or open an attachment I should not have?
- Is this a temporary glitch or a more serious change in behavior?

A false alarm is still acceptable to handle carefully; do not turn a normal issue into a panic-driven mistake.

## 2. Reduce the impact

If the situation seems active or suspicious:

- Disconnect the machine from the network if you can do so safely.
- Avoid downloading or running software from the internet until you understand the problem.
- Do not run random scripts or “cleanup” tools from random posts or chat messages.
- If there is a trusted backup path, make sure it is not compromised before attempting recovery.

## 3. Preserve important evidence

- Save any error messages, screenshots, or logs you have already observed.
- If you have a local system log relevant to the problem, keep a copy of the relevant lines.
- Avoid deleting or editing files until you understand the problem well enough to decide whether recovery is necessary.

## 4. Check the basics

- Confirm the system date and time is correct.
- Review the browser and app lists for unknown additions.
- Review the system's update and package list.
- Check whether the firewall is active and whether there are unexpected listening services.
- If you use a VM or isolated lab, restore it to a clean snapshot if you suspect a change or accidental exposure.

## 5. Recovery options

Choose the path that is least risky and most likely to restore a clean state:

- Restore from a known-good backup if you have one.
- Reinstall the operating system if the system has been heavily changed or the evidence points to a broad compromise.
- Revert a VM or lab environment instead of trying to salvage an uncertain system.

Do not continue to use a suspicious system as your normal working machine while the problem is uncertain.

## 6. Follow the trusted sources

- Use official vendor documentation and operating-system update channels.
- For a major alert, check the relevant government or vendor advisory before acting on a recommendation.
- If a threat is private or suspicious, rely on a trusted security professional rather than a random internet rumor.

## 7. Document what happened

Keep a short note with:

- what was observed
- when it occurred
- what you changed
- what was restored or reinstalled
- what was verified afterward

This helps you learn from the event and makes future recovery easier.

This playbook is intentionally cautious and practical. Its purpose is to reduce panic and improve decision-making, not to encourage hasty or high-risk actions.
