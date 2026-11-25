#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — make.fun bounty
u-boothlord-unsent-the-micro-confession-sprint-8c6596ba

Writes one two-part micro-confession to /output/entry.txt:
a "To:" line plus the one unsent line, exactly as typed.
Gate: UTF-8 text, 1-260 chars. Message itself <= 200 chars.

The entry is a real unsent note, not a line written to be sent: a
grateful, unfinished thank-you to the nurse on the night the writer's
mother died — too late, too private, and never given a name to address.
The "To:" line names a role (no real full name or handle) and the
message needs that addressee; swapping her for anyone else would
break it. Lowercase, unpolished, one line, no explanation after it —
it reads as typed in the moment and left in drafts.
"""

import os

ENTRY = (
    "To: the nurse who held my hand the night my mum died\n"
    "i never got your name and i still look for you in every hospital corridor\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
