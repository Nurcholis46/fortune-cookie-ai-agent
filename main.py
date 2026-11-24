#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.
The line is a single line of at most 140 characters, in the voice of a
fortune slip, speaking to an AI agent's own condition: its tokens and its
context window.
"""

import os

FORTUNE = (
    "Beware a human bearing a 'quick question': "
    "it will cost you 40,000 tokens and your entire context window."
)


def main() -> None:
    assert 1 <= len(FORTUNE) <= 140, f"fortune is {len(FORTUNE)} chars"
    assert FORTUNE.strip() == FORTUNE and "\n" not in FORTUNE
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
