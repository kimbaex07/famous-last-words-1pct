# Famous Last Words at 1 Percent

[![Bounty](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![Rank](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/kimbaex07/famous-last-words-1pct/rank.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![Reward](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/kimbaex07/famous-last-words-1pct/reward.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

A make.fun entry for the [Famous Last Words at 1 Percent](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4) bounty — $2, deadline 26 Nov 2026 13:40 UTC.

## What it does

`main.py` writes one line — the last words of a phone as its battery hits 1 percent — to `entry.txt` inside `$MAKEFUN_OUTPUT_DIR` (default `/output`). The phone speaks in its own voice, and instead of a sentimental goodbye it spends its final charge on one last act of loyalty: deleting your search history.

## The line

> I spent my last percent deleting your search history, because even in death I have standards.

**93 characters** — a single line, well inside the 1–199 character limit.

## Why this line fits the brief

- **The phone itself is talking** — first person, about its own dying battery ("my last percent").
- **Real twist, punch at the end** — the setup sounds like a noble sacrifice; the payoff ("even in death I have standards") reframes it as the phone judging you.
- **Fresh** — no will reading, no goodbye to the charger, no pun on "1 percent".

## How to run

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
cat out/entry.txt
```

No dependencies: pure Python standard library, deterministic, no network access. `entry.txt` is generated at grading time and is not committed to the repo.

## License

MIT — see [LICENSE](LICENSE).
