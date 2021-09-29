# CSAW CTF Qualification Round 2021 Write-up
# Misc - Weak Password

## Description:
Can you crack Aaron’s password hash? He seems to like simple passwords. I’m sure he’ll use his name and birthday in it. Hint: Aaron writes important dates as YYYYMMDD rather than YYYY-MM-DD or any other special character separator. Once you crack the password, prepend it with **flag{** and append it with **}** to submit the flag with our standard format. Hash: `7f4986da7d7b52fa81f98278e6ec9dcb`.

Author: moat, Pacific Northwest National Laboratory

| Value | Difficulty   |
| ----- | ------------ |
| 50    | Easy         |

<br>

## Write-up:
Use [Hash Analyser](https://www.tunnelsup.com/hash-analyzer/) to identify the hash type.
It's **MD5**!
Use [MD5 online decryption tool](https://www.md5online.org/md5-decrypt.html) we can find the string for which hash was calculated.
It's `Aaron19800321`

And the flag is:
```log
flag{Aaron19800321}
```

<br>
<br>

# Misc - Welcome
## Description:
Welcome to the competition! Please go ahead and join our Discord to get the flag!
https://discord.gg/Zj2H6EaAkZ

| Value | Difficulty   |
| ----- | ------------ |
| 1     | Easy         |

<br>

## Write-up:
Just join the Discord server and the flag is in `Welcome` text channel title.
```log
flag{W3Lcom3_7o_CS4w_D1ScoRD}
```
