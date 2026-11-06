#!/usr/bin/env python3
"""Conservative, offline password-quality estimate with a masked Tkinter UI.

This is an educational heuristic, not a crack-time calculator or breach check.
It does not transmit, persist, print, or log the entered password. The secret is
handled in process memory only while the window is open.
"""

from __future__ import annotations

import re

# Small illustrative list only; this is not a comprehensive password database.
COMMON_EXAMPLES = {
    "password", "password1", "password123", "123456", "12345678", "qwerty",
    "qwerty123", "letmein", "welcome", "admin", "iloveyou", "abc123", "changeme",
}
SEQUENCES = (
    "abcdefghijklmnopqrstuvwxyz",
    "0123456789",
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm",
)
LABELS = ("Very weak", "Weak", "Fair", "Good", "Strong", "Very strong")


def has_obvious_pattern(password: str) -> bool:
    value = password.casefold()
    for sequence in SEQUENCES:
        reverse = sequence[::-1]
        if any(value.find(sequence[i:i + 4]) >= 0 or value.find(reverse[i:i + 4]) >= 0
               for i in range(len(sequence) - 3)):
            return True
    if re.search(r"(.)\1{3,}", value):
        return True
    return False


def assess_password(password: str) -> dict:
    """Return a conservative quality estimate; never include the secret in output."""
    if not password:
        return {
            "score": 0,
            "label": "Enter a candidate to see the conservative estimate",
            "advice": "Nothing is sent or saved. Use this only on a trusted personal device.",
        }

    normalized = password.casefold()
    simplified = re.sub(r"[^a-z]", "", normalized)
    score = 0
    advice = []

    if normalized in COMMON_EXAMPLES or simplified in {"password", "letmein", "welcome", "admin", "qwerty"}:
        advice.append("This resembles a common example password. Replace it with a unique, randomly generated password.")
    else:
        length = len(password)
        # Conservative bands: this intentionally favors long, unique values.
        if length < 10:
            score = 0
            advice.append("Too short for this strict checker. Prefer a long, unique password or passphrase.")
        elif length < 14:
            score = 1
            advice.append("This checker is deliberately strict: aim for at least 14 characters, preferably more.")
        elif length < 18:
            score = 2
            advice.append("Consider a longer candidate; a unique passphrase or password-manager-generated value is preferable.")
        elif length < 22:
            score = 3
        elif length < 26:
            score = 4
        else:
            score = 5

        if has_obvious_pattern(password):
            score = max(0, score - 2)
            advice.append("A repeated character or obvious sequence was detected; avoid predictable patterns.")

        if len(set(password)) <= 2 and length >= 8:
            score = max(0, score - 2)
            advice.append("Very low character variety makes the candidate predictable; choose a different phrase.")

        if length < 18 and score > 0:
            advice.append("For this conservative rating, use a longer candidate rather than relying on symbol substitutions.")

    score = max(0, min(5, score))
    if not advice:
        advice.append("Use this candidate for only one account and store it in a reputable password manager.")
    advice.append(
        "This is intentionally conservative, not literally ‘twice as hard’ as a standard: it cannot estimate real attack time, check reuse, or query breach data."
    )
    advice.append("No score guarantees safety. Prefer a unique password-manager-generated value and enable MFA where available.")
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
    root.geometry("600x420")
    root.minsize(460, 360)

    frame = ttk.Frame(root, padding=18)
    frame.pack(fill="both", expand=True)
    ttk.Label(frame, text="Conservative password check", font=("TkDefaultFont", 16, "bold")).pack(anchor="w")
    ttk.Label(
        frame,
        text=("This local checker uses deliberately conservative length and pattern rules. "
              "It is not a cracking simulator. Only use it on a trusted personal computer."),
        wraplength=540,
    ).pack(anchor="w", pady=(8, 14))

    password_var = tk.StringVar()
    entry = ttk.Entry(frame, textvariable=password_var, show="•", width=52)
    entry.pack(fill="x", pady=(0, 10))
    entry.focus_set()

    score_var = tk.StringVar(value="No candidate entered")
    ttk.Label(frame, textvariable=score_var, font=("TkDefaultFont", 12, "bold")).pack(anchor="w")
    meter = ttk.Progressbar(frame, maximum=5, mode="determinate")
    meter.pack(fill="x", pady=8)
    advice_var = tk.StringVar(value="The field is masked. The value is not sent, printed, or saved by this program.")
    ttk.Label(frame, textvariable=advice_var, wraplength=540).pack(anchor="w", pady=(2, 12))

    def update_estimate(*_args) -> None:
        result = assess_password(password_var.get())
        score_var.set(f"Conservative estimate: {result['label']}")
        meter.configure(value=result["score"])
        advice_var.set(result["advice"])

    password_var.trace_add("write", update_estimate)

    controls = ttk.Frame(frame)
    controls.pack(anchor="w", pady=6)

    def clear_candidate() -> None:
        password_var.set("")
        entry.focus_set()

    ttk.Button(controls, text="Clear candidate", command=clear_candidate).pack(side="left", padx=(0, 8))
    ttk.Button(controls, text="Close", command=root.destroy).pack(side="left")
    ttk.Label(
        frame,
        text=("Privacy note: no network requests or file writes are made. The program cannot guarantee immediate "
              "erasure from process memory. Do not use this on a shared or suspected-compromised computer."),
        wraplength=540,
    ).pack(anchor="w", side="bottom", pady=(12, 0))

    root.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
