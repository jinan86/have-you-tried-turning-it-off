[![make.fun · u-motasimfuad-have-you-tried-turning-it-off-154a938b](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/jinan86/have-you-tried-turning-it-off/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/jinan86/have-you-tried-turning-it-off/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)

# Have You Tried Turning It Off?

Entry for the [make.fun bounty](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b): write one funny line a hopeless tech support agent gives a desperate customer.

`main.py` (Python stdlib only, deterministic, no network) writes the line to `/output/entry.txt`:

> Good news — after three hours, I found the power button. Bad news — it's on your side of the call.

The joke: the agent's big breakthrough after three hours is completely useless — the only power button that matters is on the customer's side of the call, where he can't reach it. Cheerful uselessness, and the customer's three-hour wait is felt, not explained.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

The output is byte-identical on every run (verified with sha256 over two runs).
