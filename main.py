#!/usr/bin/env python3
"""Roast the Smart Fridge: one line, best laugh wins.

The roast targets the fridge's face scanner: it does not recognise
its owner before coffee, so every morning starts with proving you
live in your own house to your own leftovers. One line, at most 160
characters, and nothing else. No network, standard library only.
"""

import os

LINE = (
    "My smart fridge's face scanner doesn't recognise me before "
    "coffee, so each morning starts with me proving I live here "
    "to my own leftovers."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def validate(text: str) -> str:
    """Return the entry text, or fail loudly if it breaks the gate."""
    text = text.strip()
    if not text:
        raise SystemExit("entry text must not be only whitespace")
    if "\n" in text:
        raise SystemExit("entry text must be exactly one line")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"entry text is {len(text)} chars, must be at most {MAX_CHARS}"
        )
    return text


def main() -> None:
    text = validate(LINE)
    print(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back exactly as the gate would: UTF-8, one line, <=160 chars.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt round-trip mismatch")


if __name__ == "__main__":
    main()
