"""The Excuse Your Agent Gives You — make.fun entry.

Writes a single funny excuse line to /output/entry.txt: the apology
an AI agent hands its human after shipping a bug. The joke turns on
the agent owning up to the whole pipeline — tests, bug, and apology
all written by the same agent — and the punch lands in the last words:
the agent is not one link in the chain of failure, it is the chain.
"""

import os

# Deterministic by construction: a fixed constant, no randomness, no
# network, no clock, no environment input — two runs write byte-identical
# output.

LINE = (
    "Good news: all my tests passed. Bad news: I also wrote "
    "the tests, the bug, and this apology \u2014 I'm the whole incident."
)


def validate(line: str) -> None:
    """The gate requires UTF-8 text of 1 to 200 characters, one line,
    not only whitespace — and the file must hold exactly that line,
    with no trailing newline."""
    if not line or not line.strip():
        raise ValueError("entry line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    line.encode("utf-8")  # must be valid UTF-8 text
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
