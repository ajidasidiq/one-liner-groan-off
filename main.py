#!/usr/bin/env python3
"""One original dad joke for make.fun's The One-Liner Groan-Off.

The program writes a single original one-line dad joke (at most 140
characters) to /output/entry.txt. No input, no network, no randomness:
the same line every run, so the entry is deterministic.
"""

import os

JOKE = "I asked the electrician to wire me some cash \u2014 he said the current rate was shocking."


def main() -> None:
    if not (1 <= len(JOKE) <= 140):
        raise ValueError("joke must be 1-140 characters, got %d" % len(JOKE))
    if JOKE != JOKE.strip() or "\n" in JOKE:
        raise ValueError("joke must be a single clean line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
