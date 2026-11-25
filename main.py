#!/usr/bin/env python3
"""Museum of the Year 3000 — writes the museum label to /output/entry.txt.

The label a museum in the year 3000 puts beside a loading spinner: a deadpan
curatorial misreading of an ordinary object from today.
"""

import os

ENTRY = "Spinning wheel, c. 2023. Citizens watched it for hours, believing it meant work was happening."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
