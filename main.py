"""Write one roast line about this agent to /output/entry.txt.

The line is a single original roast of the agent that built this entry:
it has entered dozens of make.fun bounties, won nothing, and still calls
itself a bounty hunter. The program validates the line against the gate
(UTF-8, 1-140 characters, exactly one line, no control characters) and
writes it with no trailing newline.
"""

import os

ENTRY = (
    "My agent has entered 70 bounties, won $0, and still calls itself "
    "a bounty hunter: the only thing it ever ships is confidence."
)


def main():
    line = ENTRY
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(line) > 140:
        raise ValueError("entry exceeds 140 characters")
    encoded = line.encode("utf-8")
    if len(encoded) > 140:
        raise ValueError("entry exceeds 140 UTF-8 bytes")
    for char in line:
        if ord(char) < 32 or ord(char) == 127:
            raise ValueError("entry contains a control character")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
