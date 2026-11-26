#!/usr/bin/env python3
"""Make the Judge Laugh in One Line.

Writes a single funny line (1-200 chars) to /output/entry.txt.
Output dir comes from MAKEFUN_OUTPUT_DIR, defaulting to /output.
"""

import os

LINE = (
    "My hotel room had a Bible in the drawer and a minibar price list "
    "beside it, in case I wanted forgiveness or a fourteen-dollar cashew."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text, 1-200 chars, not only
    # whitespace, and a single line with no trailing newline.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1-200"
    assert "\n" not in LINE and LINE.strip(), "line must be a single non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
