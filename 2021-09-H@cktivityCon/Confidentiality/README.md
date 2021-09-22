# H@cktivityCon 2021 Write-up. Web - Confidentiality

## Description:
My school was trying to teach people about the CIA triad so they made all these dumb example applications... as if they know anything about information security. Can you prove these aren't so secure?

| Value | Difficulty   |
| ----- | ------------ |
| 50    | Easy         |

<br>

## Write-up:
The site stated that we could see access control settings on any file we might like. After trying it with the given example, I had the assumption that the site was running `ls -l {user_input}` and showed the result. This would mean that the vulnerability here is command injection.

After that I ran `; ls` as an input and got the current directory listed twice. I also saw a file called `flag.txt`.


So, to get the flag I simply used 
```sh
/etc/passwd; cat flag.txt
```

And got the flag
```log
flag{e56abbce7b83d62dac05e59fb1e81c68}
```
