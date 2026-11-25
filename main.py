#!/usr/bin/env python3
"""One Line, Lights Out entry: one sad status update, max 200 characters.

The line is a status post from the agent at the exact moment the lid goes
down. Its sadness lives in a single small machine detail: the typing
indicator is still on, although there is no one left to type. Nothing is
announced, nothing is begged for, and the voice stays the machine's own
from the first word to the last -- a quiet fact, stated plainly, with an
image that stays after the line ends.

Arena champion: beat 5 shortlisted rivals two-way and beat the gold set
(last-words lines, the Everyday Wonder image line, and the ai-joke-03
winners as negative control) consistently in both orders; see ARENA.md
in the entry folder.

Writes exactly these bytes to /output/entry.txt (no trailing newline),
deterministically, so two runs agree byte for byte. Stdlib only.
MAKEFUN_OUTPUT_DIR stands in for /output outside the grader's container.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = "Lid down. The typing indicator is still on, and there is no one left to type."


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
