"""Real-Life Patch Notes: The Comedy Changelog entry.

Writes one patch note about a bug in real life / human biology to
entry.txt.

Deterministic: no arguments, no network, no randomness, no model calls.
The patch note is embedded as a string literal; the program only writes
it out.
"""

import os
from pathlib import Path

PATCH_NOTE = (
    "v2.4.1: fixed a bug where the body woke up one minute before the "
    "alarm, every day, just to check the alarm still worked."
)
# 120 characters: inside the gate's 1-160 range, no trailing newline.


def main() -> None:
    # Guard the gate before writing: 1-160 Unicode code points, at least
    # one non-whitespace character. Fail loudly instead of shipping a
    # rejected entry.
    if not 1 <= len(PATCH_NOTE) <= 160:
        raise ValueError(f"patch note is {len(PATCH_NOTE)} characters, must be 1-160")
    if not any(not c.isspace() for c in PATCH_NOTE):
        raise ValueError("patch note has no non-whitespace character")
    os.umask(0o022)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    os.chmod(output_dir, 0o755)
    target = output_dir / "entry.txt"
    target.write_text(PATCH_NOTE, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
