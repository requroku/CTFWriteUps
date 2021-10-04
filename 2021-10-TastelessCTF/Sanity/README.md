# H@cktivityCon 2021 Write-up. [misc] Sanity

## Description:
This challenge is locked down.

Locked down challenges will require a proof-of-work like this: sha1(abc123, input) prefix = 000000... you need to respond with a single line suffix to abc123, so that sha1(abc123[input]) has a 000000 prefix example: sha(abc12344739190).hexdigest = 000000872D5625DEE5FD0EA44B230D7A98C1B2CA

you can use `go run pow.go abc123 000000` or `python pow.py abc123 000000` to generate your own.

Connect at **hyper.tasteless.eu:10001** to retrieve your flag!

`nc hyper.tasteless.eu:10001`

<br>

| Value | Difficulty   |
| ----- | ------------ |
| 1     | Easy         |

<br>

## Write-up:
In this challenge we simply needed to solve a proof-of-work. The proof-of-work algorithm will be the same for the challenges in **guessing** category, so competition organizers already provide us with [scripts](./original_files) in Python and Go to solve it. And to solve it, we simply needed to connect to server using one the them:

```sh
python .\pow.py hyper.tasteless.eu 10001
solving 0abf7e61521d7f0f for prefix 00000
solved! 6978736
welcome to tasteless ctf 2021
tstlss{tchoo-tchoo-flag-train}
*** Connection closed by remote host ***
```

<br>

And flag is:
```log
tstlss{tchoo-tchoo-flag-train}
```
