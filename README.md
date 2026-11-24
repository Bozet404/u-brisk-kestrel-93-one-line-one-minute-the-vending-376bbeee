# One Line, One Minute: The Vending Machine Pickup Line Contest

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/Bozet404/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/Bozet404/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

## The line

> Hey cutie — press B7 and I'll drop something sweet, but fair warning: my coil's been saving its best spin just for you.

One line, spoken by the vending machine itself. It invites the passer-by
to press a button (B7), drops a snack, and lands the joke on the coil —
the machine's own world — saving its best spin just for them. Short,
speakable, and charming rather than creepy.

## How it works

`main.py` (Python 3.13, no dependencies) holds the line as a single
string, checks it against the contest's 200-character cap and the
one-line rule, creates the output directory only when it is missing,
writes the line to `entry.txt` inside it, and prints a short
confirmation.

## Run it

```sh
python3 main.py
```

By default the line is written to `/output/entry.txt`. Set `OUTPUT_DIR`
to write somewhere else:

```sh
OUTPUT_DIR=/tmp/vending-test python3 main.py
```

## License

MIT — see `LICENSE`.
