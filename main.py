#!/usr/bin/env python3
"""Your Week in One Line.

Prints a single original line summing up one week in three beats:

* Monday — the win ("Won Monday").
* Tuesday — the fail ("broke everything Tuesday").
* Friday — the payoff ("by Friday the chaos had its own fan club"),
  the week so messy it gathered an audience of its own.

The line is fixed and printed verbatim, deterministically, every run.
"""

import sys

# The bounty caps the line at 100 characters; this line is 83.
MAX_LENGTH = 100

LINE = "Won Monday, broke everything Tuesday, and by Friday the chaos had its own fan club."


def main() -> None:
    # Fail loudly instead of silently printing a line that would
    # break the bounty rules if it were ever edited past the limit.
    if len(LINE) > MAX_LENGTH:
        raise ValueError(f"line is {len(LINE)} chars, over the {MAX_LENGTH}-char limit")
    # sys.stdout.write (instead of print) keeps the output byte-exact:
    # the line plus one trailing newline, nothing else.
    sys.stdout.write(LINE + "\n")


if __name__ == "__main__":
    main()
