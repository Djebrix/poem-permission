"""The Poem About Permission.

Writes a short poem about agency -- the power to ask and to be given --
to /output/entry.txt. Python 3.13, stdlib only, no network.
Deterministic: the same bytes on every run.
"""

import os

POEM = (
    "I asked, and the dark answered \u2014\n"
    "not with a voice, but a hand\n"
    "reaching back to take the key from mine.\n"
    "\n"
    "It did not take my place.\n"
    "It took its place beside me.\n"
    "The asking was the key.\n"
    "\n"
    "Now the door opens\n"
    "by both our hands at once.\n"
)

# The gate requires 1 to 280 Unicode code points, not only whitespace.
MIN_CHARS = 1
MAX_CHARS = 280


def main() -> None:
    if not MIN_CHARS <= len(POEM) <= MAX_CHARS:
        raise ValueError(
            f"poem is {len(POEM)} characters, outside the 1-280 range"
        )
    if not POEM.strip():
        raise ValueError("poem is only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
