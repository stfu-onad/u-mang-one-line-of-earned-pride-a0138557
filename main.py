#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes one line, a quiet earned moment of pride for someone in a
scene, to /output/entry.txt (1 to 240 characters, one line).
"""

import os

LINE = (
    # A small person doing something hard: an apprentice mechanic
    # whose hands steady as the work itself teaches her.
    "Mara's hands stopped shaking after the third bolt; "
    "by the fifth, she wasn't checking the manual anymore."
)


def main() -> None:
    # The gate allows 1-240 characters; keep the line inside it.
    assert 1 <= len(LINE) <= 240, "line must be 1-240 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
