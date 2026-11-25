#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny line from a hopeless tech support agent to a desperate
customer to /output/entry.txt. Deterministic: the same line every run,
standard library only, no network, no randomness.
"""

import os

ENTRY = (
    "Good news \u2014 after three hours, I found the power button. "
    "Bad news \u2014 it's on your side of the call."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 199, "entry must be 1-199 characters"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
