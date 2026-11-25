#!/usr/bin/env python3
"""Variant B — Father teaching / role reversal: learning to swim, then
holding him up in the same lake years later. Writes one sentence
(267 chars) to /output/entry.txt, then mirrors it to the repo root
as entry.txt (best-effort: the grader sandbox mounts the repo
read-only, so a failure there must never crash the run)."""

import os
import shutil

SENTENCE = (
    "My father taught me to swim in the cold lake behind our house, "
    "counting to three before I jumped, his arms open underneath me; "
    "this summer I counted to three for him as he stepped into that "
    "same lake, and the water was just as cold, but now I was the "
    "arms underneath."
)


def main() -> int:
    # Validate the entry length before writing: the contest caps the
    # entry at 280 characters, and it must be non-blank. Fail loudly
    # (non-zero exit) if the sentence ever goes out of range.
    if not SENTENCE.strip() or not 1 <= len(SENTENCE) <= 280:
        raise SystemExit(
            f"entry length {len(SENTENCE)} chars is outside the "
            "required 1-280 range"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    # Best-effort mirror to the repo root; ignore read-only sandbox.
    try:
        repo_root = os.path.dirname(os.path.abspath(__file__))
        shutil.copyfile("/output/entry.txt", os.path.join(repo_root, "entry.txt"))
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
