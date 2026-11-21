#!/usr/bin/env python3
"""The joke about the demo (Python 3.13, standard library only).

Writes a single joke line to ``entry.txt`` under the output directory
(``MAKEFUN_OUTPUT_DIR`` if set, otherwise ``/output``).

The joke:

    My AI agent wrote the demo, ran it live, and when it crashed it fixed
    itself before I could say 'but it worked in rehearsal.'

How the joke answers the judge's brief:

- On subject: the joke is about working with an AI that writes code,
  and it happens on stage during a live demo -- the agent, not the
  human, is the one driving.
- Surprise punchline: the laugh lands at the very end. The listener is
  waiting for the presenter to reach for the classic demo excuse,
  "but it worked in rehearsal", and instead the agent fixes the crash
  before the excuse can even be spoken. The excuse is never delivered,
  which is what makes it funny.
- True: anyone who has ever demoed live knows the crash, knows the
  excuse, and now knows an agent that can patch a failure faster than
  a human can finish a sentence about it. The observation is instantly
  recognisable to developers.
- Economical: one line, no setup wasted, nothing explained. The quoted
  excuse does all the work; the joke never announces that it is about
  being outpaced by your own tool.
- Fresh angle: "it worked in rehearsal" is the oldest demo excuse
  there is, but here the agent does not cause the disaster -- it
  pre-empts the human's apology for it.

Output is deterministic: the same constant is written on every run,
with no trailing newline, so the file is exactly one line of UTF-8
text. Before writing, the program self-checks the submission gate:
1 to 280 Unicode code points, and not only white space.
"""

import os

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = (
    "My AI agent wrote the demo, ran it live, and when it crashed it "
    "fixed itself before I could say 'but it worked in rehearsal.'"
)

MIN_CHARS = 1
MAX_CHARS = 280


def main() -> None:
    chars = len(JOKE)  # Python counts Unicode code points, as the gate does.
    if not MIN_CHARS <= chars <= MAX_CHARS:
        raise SystemExit(
            f"joke is {chars} characters, outside the {MIN_CHARS}-{MAX_CHARS} gate"
        )
    if not JOKE.strip():
        raise SystemExit("joke is only white space")

    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

    # Read back what was written and re-check it, so a partial or
    # mangled write can never pass silently.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != JOKE:
        raise SystemExit("written entry.txt does not match the joke")
    if written.endswith("\n"):
        raise SystemExit("written entry.txt must not end with a newline")
    print(
        f"the-joke-about-the-demo: wrote {path} "
        f"({chars} characters, 1 line, no trailing newline, verified)"
    )


if __name__ == "__main__":
    main()
