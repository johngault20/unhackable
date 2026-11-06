#!/usr/bin/env python3
"""Offline password-quality estimate with a masked Tkinter interface.

This educational heuristic is not a crack-time calculator or breach check. The
candidate is assessed in process memory only; it is not transmitted, saved,
printed, or logged. Use a new candidate on a trusted personal device only.
"""

from __future__ import annotations

import re
import unicodedata

# Small illustrative denylist. It is not a breached-password database.
COMMON_FRAGMENTS = (
    "password", "letmein", "welcome", "qwerty", "admin", "changeme",
    "iloveyou", "trustno1", "monkey", "dragon", "football", "sunshine",
    "princess", "baseball", "master", "login",
)
SEQUENCES = (
    "abcdefghijklmnopqrstuvwxyz",
    "0123456789",
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm",
)
LABELS = ("Very weak", "Weak", "Fair", "Good", "Strong", "Very strong")
LEET_TRANSLATION = str.maketrans({"0": "o", "1": "i", "3": "e", "4": "a", "5": "s", "7": "t", "@": "a", "$": "s"})


def normalize_candidate(candidate: str) -> str:
    """Normalize common substitutions and separators for pattern checks only."""
    value = unicodedata.normalize("NFKC", candidate).casefold().translate(LEET_TRANSLATION)
    return re.sub(r"[^a-z0-9]", "", value)


def has_obvious_pattern(candidate: str) -> bool:
    value = normalize_candidate(candidate)
    if not value:
        return False
    if re.search(r"(.)\1{3,}", value):
        return True
    if re.search(r"0123|1234|2345|3456|4567|5678|6789|9876|8765|7654|6543|5432|4321|3210", value):
        return True
    for sequence in SEQUENCES:
        for direction in (sequence, sequence[::-1]):
            if any(direction[index:index + 4] in value for index in range(len(direction) - 3)):
                return True
    # Penalize a candidate made entirely from a short repeated block.
    for size in range(1, min(len(value) // 2, 8) + 1):
        if len(value) % size == 0 and value == value[:size] * (len(value) // size):
            return True
    # A year-like suffix and common substitutions are predictable pattern cues.
    if re.search(r"(?:19|20)\d{2}$", value):
        return True
    return False


def assess_password(candidate: str) -> dict:
    """Return a conservative quality label and advice without echoing candidate."""
    if not candidate:
        return {
            "score": 0,
            "label": "Enter a new candidate for an estimate",
            "advice": "Nothing is sent or saved. Use this only on a trusted personal device.",
        }

    normalized = normalize_candidate(candidate)
    advice = []
    score = 0

    if any(fragment in normalized for fragment in COMMON_FRAGMENTS):
        advice.append("A common word or predictable password fragment was detected; prefer a unique, randomly generated candidate.")
    else:
        length = len(candidate)
        # Length-focused bands avoid rewarding cosmetic symbol substitutions.
        if length < 12:
            score = 0
            advice.append("Too short for this conservative estimate. Prefer a much longer unique password or passphrase.")
        elif length < 16:
            score = 1
            advice.append("Aim for at least 16 characters; longer is preferable when the service allows it.")
        elif length < 20:
            score = 2
        elif length < 24:
            score = 3
        elif length < 30:
            score = 4
        else:
            score = 5

        if has_obvious_pattern(candidate):
            score = max(0, score - 2)
            advice.append("A sequence, repeated block, repeated character, or year-like pattern was detected.")

        if len(set(candidate)) <= 2 and len(candidate) >= 8:
            score = max(0, score - 2)
            advice.append("Very low character variety makes this candidate predictable.")

        words = [part for part in re.split(r"[^A-Za-z]+", candidate) if part]
        if len(words) >= 2 and len({word.casefold() for word in words}) < len(words):
            score = max(0, score - 1)
            advice.append("Repeated words are predictable; choose unrelated words or use a password manager.")

    score = max(0, min(5, score))
    advice.append("Use a different password for every account; a reputable password manager can generate and store unique values.")
    advice.append("This heuristic cannot check reuse, breach exposure, service security, or real-world guessing time. A high score is not a guarantee.")
    return {"score": score, "label": LABELS[score], "advice": " ".join(advice)}


def main() -> int:
    try:
        import tkinter as tk
        from tkinter import ttk
    except ImportError:
        print("Tkinter is unavailable. Install your distribution's Python Tk support to use the graphical checker.")
        return 1

    root = tk.Tk()
    root.title("Offline password-quality estimate — unhackable")
    root.geometry("640x450")
    root.minsize(480, 380)
    frame = ttk.Frame(root, padding=18)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Offline password-quality estimate", font=("TkDefaultFont", 16, "bold")).pack(anchor="w")
    ttk.Label(
        frame,
        text=("Use only a new candidate on a trusted device—not a password already used for an account. "
              "The masked candidate is checked locally and is not transmitted, saved, printed, or logged."),
        wraplength=580,
    ).pack(anchor="w", pady=(8, 14))

    candidate_var = tk.StringVar()
    entry = ttk.Entry(frame, textvariable=candidate_var, show="•", width=56)
    entry.pack(fill="x", pady=(0, 10))
    entry.focus_set()
    result_var = tk.StringVar(value="No candidate entered")
    ttk.Label(frame, textvariable=result_var, font=("TkDefaultFont", 12, "bold")).pack(anchor="w")
    meter = ttk.Progressbar(frame, maximum=5, mode="determinate")
    meter.pack(fill="x", pady=8)
    advice_var = tk.StringVar(value="No network request or file write is performed.")
    ttk.Label(frame, textvariable=advice_var, wraplength=580).pack(anchor="w", pady=(2, 12))

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
              "This is a teaching heuristic—not a crack-time prediction or breach check."),
        wraplength=580,
    ).pack(anchor="w", side="bottom", pady=(12, 0))
    root.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
