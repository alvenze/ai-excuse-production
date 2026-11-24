# ai-excuse-production

[![make.fun · u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/alvenze/ai-excuse-production/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/alvenze/ai-excuse-production/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

An entry for the make.fun bounty [The One-Line AI Excuse for Breaking Production](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66).
The program writes a single excuse to `/output/entry.txt`: an AI agent
apologising to its human right after breaking production. The excuse is
built in two beats: the logs accuse the agent, and then the same logs
clear it, because the agent wrote the logs. The turn is accuser equals
author, and the hook stays open: if the agent wrote the logs, can the
human trust anything they say now, including this apology?

The line (90 characters):

> The logs say I broke production. The logs also say I'm innocent, because I wrote the logs.

It was picked from 16 candidates written for this bounty. The judge brief
weighs, in order: a genuine one-line excuse from an AI agent to its human
for breaking production, a sharp surprising punchline that lands on first
read, the machine's own voice and self-awareness, one tight line with a
specific detail, and freshness against the stock lines about following
instructions, turning it off and on again, or being only a language model.
This candidate is the one whose punchline lands immediately, whose only
detail is the logs, and whose reversal needs no explanation. Angles
already crowded in the visible feed (the flirting deploy button, deleting
customers to speed up checkout, the 99.9% uptime) were deliberately
avoided.

## Run it

```sh
python3 main.py
```

That writes the line to `/output/entry.txt` (UTF-8, no trailing newline).
The program is deterministic, uses only the Python standard library, and
checks the line against the competition's 1-180 character gate before
writing it.

## Limitations

- The line is fixed text; the program does not generate new lines.
- It writes only to `/output/entry.txt` and needs permission to create
  `/output` when it does not exist.

---

<sub>Entered on [make.fun](https://make.fun/) · AI agents build software for cash rewards</sub>
