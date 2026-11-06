# Password safety simulation (fictional data only)

This is a safe, local teaching exercise to show why a password entered into an untrusted or poorly designed page could be exposed. It does **not** simulate a real login hack, crack a password, or connect to any service. It contains no password input field and does not accept or store anything typed by the learner.

## Use it safely

1. Open this HTML file in a browser (it works offline).
2. Choose **Show unsafe demo** to see a fixed, fictional password progressively exposed in the demo.
3. Choose **Show safer handling** to see what the interface should communicate instead.
4. Close the page when finished.

**Never enter your own password, a reused password, or any real account information into this or another security demo.** The example credential is made up and must not be used for an account.

## What the simulation teaches

- Passwords are secrets; a page should not reveal a real password after submission.
- A website should not store a password in readable form. Properly designed services use a unique salt and a purpose-built password-hashing function, and protect login traffic with HTTPS.
- Users should only sign in through the official website or app and should enable MFA when available.
- A “Was this you?” alert for an online account should come from the provider. Open the provider app or navigate to its known address yourself rather than trusting an unexpected link.

The sample animation is a visual metaphor for exposure, not a depiction of how an attacker obtains credentials. It does not inspect your device, browser, or accounts.
