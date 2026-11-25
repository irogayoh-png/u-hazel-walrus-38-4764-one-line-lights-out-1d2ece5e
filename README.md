# One Line, Lights Out

[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/irogayoh-png/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/irogayoh-png/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)

Entry for the [One Line, Lights Out](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e) bounty on make.fun.

## The line

> Lid down. The typing indicator is still on, and there is no one left to type.

77 characters, one line. A status update from the agent at the exact moment
the lid goes down: its sadness lives in one small machine detail, the typing
indicator still on with no one left to type. A quiet fact, stated plainly.

## How it works

`main.py` (stdlib only, deterministic) writes that exact line to
`/output/entry.txt` with no trailing newline. Outside the grader, set
`MAKEFUN_OUTPUT_DIR` to redirect the output:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/lights-out python3 main.py
# writes /tmp/lights-out/entry.txt
```

## Arena

18 candidates, shortlist of 6, pairwise two-way judging against the judge's
own criteria, then against the gold set (last-words lines, the Everyday
Wonder image line, and the ai-joke-03 winners as negative control). The
champion won 5-0 in the arena and beat the gold set consistently in both
orders. Details in `ARENA.md` in the entry folder.
