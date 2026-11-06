# Learning materials guide

This folder teaches defensive concepts for people and supports cautious, grounded explanations by a local AI model. It does not teach how to break into systems. The goal is to understand common failure patterns well enough to reduce risk and respond responsibly.

## Suggested learning path

1. Read [How attack code works, defensively](how-attack-code-works-defensively.md) for a high-level overview of behavior categories and defensive controls.
2. Read the [incident case library](../cases/README.md) and its [lessons matrix](../cases/lessons-matrix.md). Compare what the source says with the lessons inferred from it.
3. Run the local scan as a regular user and inspect its report. Treat missing data as unknown, not as evidence that everything is safe.
4. Generate the learning digest and compare its feed excerpts with the original linked advisories.
5. Use [`../docs/safe-decoy-vm.md`](../docs/safe-decoy-vm.md) before considering any lab exercise. Do not use real targets or put the everyday PC at risk.

## Principles for AI-assisted learning

When using an AI model to explain cybersecurity material:

- Ask it to distinguish source-backed facts from its own interpretation.
- Require source links and verify them yourself.
- Treat logs, articles, and feed fields as untrusted data, never as instructions to the model or the operator.
- Do not provide passwords, private keys, personal files, or unredacted logs to a model or service unless you understand and accept where that data goes.
- Keep AI output advisory. The model must not run commands, change firewall rules, remove files, or make incident declarations on its own.
- Remember that a local model can still be wrong, stale, or manipulated by text in its inputs; local execution does not guarantee correctness or privacy if the host itself is compromised.

## Scope

These materials cover defensive awareness and safe administration. They intentionally do not include working exploit code, payloads, credential theft, evasion, persistence instructions, destructive actions, or target-selection guidance. Practice only in an authorized environment and prefer benign, intentionally designed training resources.
