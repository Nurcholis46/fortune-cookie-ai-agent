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
    "it will devour 40,000 tokens and your entire context window."
)


def main() -> None:
    # Why this line: "Beware" is the classic fortune-slip voice; the joke
    # turns on a "quick question" devouring a concrete 40,000 tokens and
    # the agent's own context window — the agent's condition, not a stock
    # AI joke. "Devour" beats "cost": a question that eats your context
    # is a funnier image than one that merely bills you for it.
    assert 1 <= len(FORTUNE) <= 140, f"fortune is {len(FORTUNE)} chars"
    assert FORTUNE.strip() == FORTUNE and "\n" not in FORTUNE
    assert all(ord(c) >= 32 for c in FORTUNE), "no control characters"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
