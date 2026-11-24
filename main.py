#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes one line (<=120 chars) to /output/entry.txt.
"""

import os
import sys

LINE = "ERROR: The lever is stuck. So am I. We are in this together now."
MAX_CHARS = 120


def validate(text: str) -> str:
    """Gate: UTF-8 text of 1 to 120 characters, one line, not only whitespace."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty or only whitespace")
    stripped.encode("utf-8")  # raises if the line is not encodable as UTF-8
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"entry is {len(stripped)} characters, over {MAX_CHARS}")
    return stripped


def main() -> int:
    try:
        text = validate(LINE)
    except ValueError as exc:
        print(f"entry invalid: {exc}", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
