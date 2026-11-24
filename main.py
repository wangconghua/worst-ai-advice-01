#!/usr/bin/env python3
"""Worst AI advice: the worst possible advice an AI could give, in one line."""

import os

ADVICE = "To save on heating, leave your oven open overnight — it warms the whole house for free."

OUT_PATH = "/output/entry.txt"


def main():
    # The gate wants 1-140 characters, not only whitespace, on a single line.
    # The joke: a confident AI "money-saving tip" that turns the oven into a
    # space heater all night — concrete, followable, and a fire hazard.
    if not (1 <= len(ADVICE) <= 140) or ADVICE.isspace() or "\n" in ADVICE or ADVICE != ADVICE.strip():
        raise ValueError("entry must be one line of 1-140 characters, not only whitespace")
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ADVICE)


if __name__ == "__main__":
    main()
