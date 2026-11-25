"""Passive-aggressive note from a smart fridge.

Writes one single-line note to /output/entry.txt (or $OUTPUT_PATH).
Pure Python stdlib, deterministic, no network access.
"""

import os
import sys

# Three beats: the sensor saw it, the fridge covered for the owner,
# and the fridge still wants credit. No explanation of the joke.
PARTS = (
    "The door alarm logged your 2 a.m. ice cream.",
    "I told it to keep quiet.",
    "You're welcome.",
)

NOTE = " ".join(PARTS)


def validate(text):
    """Gate check: UTF-8, 1-200 chars, single line, not blank."""
    if not text or text != text.strip():
        raise SystemExit("entry must be non-blank text")
    if not 1 <= len(text) <= 200:
        raise SystemExit("entry must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    text.encode("utf-8")
    return text


def main() -> int:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(out_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    text = validate(NOTE)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
