#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

A tiny program that writes a single pickup line, spoken by a vending
machine to a passing human, into entry.txt inside the output directory.

The line is stored here as one plain string. The program checks that it
fits the contest's 200-character cap, creates the output directory only
when it does not exist yet, writes the line to entry.txt, and prints a
short confirmation.
"""

import os

MAX_CHARS = 200

LINE = (
    "Hey cutie \u2014 press B7 and I'll drop something sweet, "
    "but fair warning: my coil's been saving its best spin just for you."
)


def main() -> None:
    line = LINE.strip()
    if not line:
        raise SystemExit("error: the pickup line is empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"error: line is {len(line)} characters, over the "
            f"{MAX_CHARS}-character limit"
        )
    if "\n" in line:
        raise SystemExit("error: the line must be a single line")

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")

    # Read the file back and make sure what landed on disk is exactly
    # the line we meant to write, newline aside.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read().rstrip("\n")
    if written != line:
        raise SystemExit("error: entry.txt on disk does not match the line")

    print(f"wrote {len(line)} characters to {path}")


if __name__ == "__main__":
    main()
