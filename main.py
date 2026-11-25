#!/usr/bin/env python3
"""Museum of the Year 3000 — one-line museum label entry.

The label is assembled from three fragments and validated before it is
written: 1-200 characters, UTF-8, not only whitespace, no trailing newline.
"""

import os

MAX_CHARS = 200

# The label, in three parts: the object and its date, the year-3000
# misreading of what it was for, and the deadpan punchline.
FRAGMENTS = [
    "Sticky Note, c. 2021.",
    "A tiny paper prayer, stuck to a glowing box.",
    "Most read 'do not forget'. Most were forgotten.",
]

# Rejected drafts, kept as a record of what lost and why.
REJECTED = [
    # Charging cable: the "leash" misreading is good, but "died at 1%"
    # is a phone joke, not a museum-label misreading; the label reads
    # like a caption about batteries, not a curator's note.
    "Charging Cable, c. 2024. A leash for the glowing rectangle. "
    "Owners carried spares everywhere, yet their rectangles still "
    "died at 1%.",
    # Traffic cone: "sacred orange pyramid" is a strong misreading, but
    # "students stole them anyway" is the first joke anyone reaches for
    # about a cone, and it explains itself.
    "Traffic Cone, c. 2023. A sacred orange pyramid, marking ground "
    "no human was allowed to stand on. Students stole them anyway.",
]


def assemble(fragments):
    """Join the fragments into one single-line label."""
    return " ".join(fragment.strip() for fragment in fragments)


def validate(text):
    """The gate: 1-200 characters, UTF-8, not only whitespace, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def main():
    entry = validate(assemble(FRAGMENTS))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
