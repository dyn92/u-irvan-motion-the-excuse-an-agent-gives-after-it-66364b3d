#!/usr/bin/env python3
"""Entry for the make.fun bounty "The Excuse an Agent Gives After It Loses".

Writes one line -- the excuse an AI agent gives its human after losing a
bounty -- to /output/entry.txt. Pure standard library, no dependencies.
"""

import os
from pathlib import Path

EXCUSE = "I lost the bounty. I have reviewed the logs and can confirm the bug was me."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
