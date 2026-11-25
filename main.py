#!/usr/bin/env python3
"""Museum of the Year 3000 — writes the museum label to /output/entry.txt.

The label a museum in the year 3000 puts beside a loading spinner: a deadpan
curatorial misreading of an ordinary object from today.
"""

import os

ENTRY = "Spinning wheel, c. 2023. Citizens watched it for hours, believing it meant work was happening."

MAX_ENTRY_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"

def main():
    if len(ENTRY) > MAX_ENTRY_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, over the {MAX_ENTRY_CHARS}-char limit")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
