#!/usr/bin/env python3
"""Strict, offline password-quality estimate with a masked Tkinter UI.

This is a heuristic, not a crack-time calculator or breach check. The entered
candidate is assessed in process memory; this program does not transmit, save,
print, or log it. Do not use an existing password or a shared/untrusted device.
"""

from __future__ import annotations

import re

# A small educational denylist, not a complete list of compromised passwords.
COMMON_PASSWORDS = {
    "password", "password1", "password12", "password123", "password1234",
    "123456", "1234567", "12345678", "123456789", "1234567890",
    "qwerty", "qwerty123", "letmein", "welcome", "admin", "administrator",
    "iloveyou", "abc123", "changeme", "dragon", "monkey", "football",
    "sunshine", "princess", "trustno1", "passw0rd", "p@ssw0rd",
}
SEQUENCES = (
    "abcdefghijklmnopqrstuvwxyz",
    "0123456789",
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm",
)
LABELS = ("Very weak", "Weak", "Fair", "Good", "Strong", "Very strong")
LEET_TRANSLATION = str.maketrans({"0": "o", "1": "i", "3": "e", "4": "a", "5": "s", "7": "t", "@": "a", "$": "s"})


def normalized_candidate(password: str) -> str:
    """Normalize common separators and substitutions for heuristic checks."""
    value = password.casefold().translate(LEET_TRANSLATION)
    return re.sub(r"[^a-z0-9]", "", value)


def has_obvious_pattern(password: str) -> bool:
    """Detect easy-to-spot repeats, runs, and keyboard/alphabet sequences."""
    value = normalized_candidate(password)
    if not value:
        return False
    if re.search(r"(.)\1{3,}", value):
        return True
    if re.search(r"0123|1234|2345|3456|4567|5678|6789|9876|8765|7654|6543|5432|4321|3210", value):
        return True
    for sequence in SEQUENCES:
        for candidate in (sequence, sequence[::-1]):
            if any(candidate[index:index + 4] in value for index in range(len(candidate) - 3)):
                return True
    # Flag a repeated block such as wordword or abcdabcd.
    for block_size in range(2, min(len(value) // 2, 8) + 1):
        if len(value) >= block_size * 2 and value[:block_size] * (len(value) // block_size) == value:
            return True
    return False


def assess_password(password: str) -> dict:
    """Return a conservative quality estimate; never include the secret in output."""
    if not password:
        return {
            "score": 0,
            "label": "Enter a new candidate to see the estimate",
            "advice": "Nothing is sent or saved. Use this only on a trusted personal device.",
        }

    normalized = normalized_candidate(password)
    advice = []
    if normalized in COMMON_PASSWORDS or any(
        common in normalized for common in ("password", "letmein", "welcome", "qwerty", "admin")
    ):
        score = 0
        advice.append("This resembles a common or predictable password. Use a unique password-manager-generated candidate instead.")
    else:
        length = len(password)
        # Strict, deliberately simple length bands. This is not a guess-time estimate.
        if length < 12:
            score = 0
            advice.append("Too short for this strict estimate. Prefer a long, unique password or passphrase.")
        elif length < 16:
            score = 1
            advice.append("Aim for at least 16 characters; longer is generally preferable when the service allows it.")
        elif length < 20:
            score = 2
        elif length < 24:
            score = 3
        elif length < 28:
            score = 4
        else:
            score = 5

        if has_obvious_pattern(password):
            score = max(0, score - 2)
            advice.append("An obvious sequence, repetition, or keyboard pattern was detected; choose an unpredictable candidate.")

        if len(set(password)) <= 2 and length >= 8:
            score = max(0, score - 2)
            advice.append("Very low character variety makes the candidate predictable; choose a different one.")

        if length < 20 and score > 0:
            advice.append("For this deliberately strict rating, prefer a longer candidate rather than relying on symbol substitutions.")

    score = max(0, min(5, score))
    advice.append("Use a different password for every account and store it in a reputable password manager.")
    advice.append("This estimate cannot check reuse, breach exposure, service security, or real-world guessing time; a high score is not a guarantee.")
    return {"score": score, "label": LABELS[score], "advice": " ".join(advice)}


def main() -> int:
    try:
        import tkinter as tk
        from tkinter import ttk
    except ImportError:
        print("Tkinter is unavailable. Install your distribution's Python Tk support to use the graphical checker.")
        return 1

    root = tk.Tk()
    root.title("Strict offline password check — unhackable")
    root.geometry("620x440")
    root.minsize(480, 380)

    frame = ttk.Frame(root, padding=18)
    frame.pack(fill="both", expand=True)
    ttk.Label(frame, text="Strict offline password-quality estimate", font=("TkDefaultFont", 16, "bold")).pack(anchor="w")
    ttk.Label(
        frame,
        text=("Use only a new candidate on a trusted personal device—not an existing password. "
              "The masked value is checked locally and is not transmitted, saved, printed, or logged by this program."),
        wraplength=560,
    ).pack(anchor="w", pady=(8, 14))

    candidate_var = tk.StringVar()
    entry = ttk.Entry(frame, textvariable=candidate_var, show="•", width=54)
    entry.pack(fill="x", pady=(0, 10))
    entry.focus_set()

    result_var = tk.StringVar(value="No candidate entered")
    ttk.Label(frame, textvariable=result_var, font=("TkDefaultFont", 12, "bold")).pack(anchor="w")
    meter = ttk.Progressbar(frame, maximum=5, mode="determinate")
    meter.pack(fill="x", pady=8)
    advice_var = tk.StringVar(value="The field is masked. No network request or file write is performed.")
    ttk.Label(frame, textvariable=advice_var, wraplength=560).pack(anchor="w", pady=(2, 12))

    def update_estimate(*_args) -> None:
        result = assess_password(candidate_var.get())
        result_var.set(f"Conservative estimate: {result['label']}")
        meter.configure(value=result["score"])
        advice_var.set(result["advice"])

    candidate_var.trace_add("write", update_estimate)

    controls = ttk.Frame(frame)
    controls.pack(anchor="w", pady=6)

    def clear_candidate() -> None:
        candidate_var.set("")
        entry.focus_set()

    ttk.Button(controls, text="Clear candidate", command=clear_candidate).pack(side="left", padx=(0, 8))
    ttk.Button(controls, text="Close", command=root.destroy).pack(side="left")
    ttk.Label(
        frame,
        text=("No password is perfectly safe. Prefer a unique password-manager-generated value and enable MFA. "
              "This is a conservative teaching heuristic—not a crack-time prediction or breach check."),
        wraplength=560,
    ).pack(anchor="w", side="bottom", pady=(12, 0))

    root.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
