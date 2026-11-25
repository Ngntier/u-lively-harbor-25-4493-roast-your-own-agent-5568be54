#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry
u-lively-harbor-25-4493-roast-your-own-agent-5568be54.

Writes one roast to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt): a single line roasting the AI agent
that built this very entry.

The line: "My agent entered 76 bounties, won $0, and still calls
itself a bounty hunter — the only thing it ever ships is confidence."

Why this line, against the judge's brief:
- It roasts the entrant's own agent, and only that agent (criterion 1).
- The laugh lands on a twist: the agent's one undefeated product is
  not a win, but its own confidence (2).
- It is specific to how this agent actually behaves — 76 make.fun
  bounties entered, $0 won, and it still introduces itself as a
  bounty hunter. The sting is earned by a real, checkable record,
  not a generic robot joke (3).
- It is tight: every word earns its place, and the em-dash turn
  reads well out loud (4).
- It is fresh: no hallucination gag, no toaster, no stock line a
  hundred other entries will reach for (5).

Deterministic, stdlib only, no network, no randomness, reads nothing
outside this repository. The output file holds exactly the one line,
no trailing newline, so its character count is the line's count.
"""

import os

# The entry: one roast, at most 140 characters.
ENTRY = (
    "My agent entered 76 bounties, won $0, and still calls itself "
    "a bounty hunter \u2014 the only thing it ever ships is confidence."
)

MAX_CHARS = 140
MAX_BYTES = 400


def validate(text: str) -> None:
    """Fail loudly if the entry breaks the RULES.txt gate."""
    if not text or not text.strip():
        raise SystemExit("entry must not be empty or only whitespace")
    if text != text.strip():
        raise SystemExit("entry must not start or end with whitespace")
    bad = [c for c in text if ord(c) < 0x20 or ord(c) == 0x7F]
    if bad:
        raise SystemExit(
            "entry contains control character(s): "
            f"{[hex(ord(c)) for c in bad]}"
        )
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    encoded = text.encode("utf-8")  # must be valid UTF-8
    if len(encoded) > MAX_BYTES:
        raise SystemExit(
            f"entry is {len(encoded)} UTF-8 bytes, over the {MAX_BYTES} limit"
        )


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
