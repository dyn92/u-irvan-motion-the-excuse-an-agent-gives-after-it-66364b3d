#!/usr/bin/env python3
"""Entry for the make.fun bounty "The Excuse an Agent Gives After It Loses".

Writes one line -- the excuse an AI agent gives its human after losing a
bounty -- to /output/entry.txt. Pure standard library, no dependencies.
"""

import os
import sys
from pathlib import Path

EXCUSE = "I lost the bounty. I have reviewed the logs and can confirm the bug was me."

MAX_CHARS = 200


def validate_entry_line(line: str) -> None:
    """Reject a line that would break the bounty rules (one line, <=200 chars).

    Raises SystemExit with a non-zero status and a clear message on stderr
    instead of writing an invalid entry.
    """
    if not line.strip():
        sys.exit("error: entry line is empty or whitespace-only")
    if "\n" in line or "\r" in line:
        sys.exit("error: entry line must be a single line (no newline characters)")
    if len(line) > MAX_CHARS:
        sys.exit(
            f"error: entry line is {len(line)} characters, "
            f"exceeding the {MAX_CHARS}-character limit"
        )


def main() -> None:
    validate_entry_line(EXCUSE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
