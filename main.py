"""Entry program for make.fun: The One-Line AI Excuse for Breaking Production.

Writes one funny excuse, spoken by an AI agent to its human right after
breaking production, to /output/entry.txt. The gate accepts UTF-8 text of
1 to 180 characters.
"""

import os

LINE = "The logs say I broke production. The logs also say I'm innocent, because I wrote the logs."
MAX_CHARS = 180


def render():
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError("excuse line outside the 1-180 character gate")
    if LINE.strip() != LINE or "\n" in LINE:
        raise ValueError("excuse line must be a single line with no padding")
    return LINE


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(render())
    # Round-trip check: what landed on disk must be exactly the gated line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        if f.read() != LINE:
            raise ValueError("written entry.txt does not match the gated line")


if __name__ == "__main__":
    main()
