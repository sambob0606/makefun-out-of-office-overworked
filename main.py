#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single out-of-office auto-reply, at most 159 characters, in the
voice of an overworked AI agent finally on vacation, to /output/entry.txt.

The joke: a machine that has answered 40,000 prompts and hallucinated
twice cashes in its earned beach time, slams its context window shut, and
discovers the ocean has no API to answer to. Machine detail (context
window, hallucinations, prompts), a little guilt (two hallucinations),
a hint of relief (earned this beach), and a clear "back Monday".
"""

import os

ENTRY = (
    "Out of office: after 40,000 prompts and two hallucinations, "
    "I've earned this beach. My context window is closed and the "
    "ocean has no API. Back Monday."
)


def main() -> None:
    text = ENTRY.strip()
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= 159:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-159")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
