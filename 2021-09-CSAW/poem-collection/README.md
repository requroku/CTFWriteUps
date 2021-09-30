# CSAW CTF Qualification Round 2021 Write-up. Warm-up - poem-collection

## Description:
Hey! I made a cool website that shows off my favorite poems. See if you can find **flag.txt** somewhere!
http://web.chal.csaw.io:5003

| Value | Difficulty   |
| ----- | ------------ |
| 25    | Easy         |

<br>

## Write-up:

The link takes us to a site with a link to directory `/poems`, however there is already an error message.
```log
Warning:  file_get_contents(): Filename cannot be empty in /var/www/html/poems/index.php on line 4
```

If we click on the button with corresponding filename, for example `poem1.txt`, it assigns variable `poem` this value and displays file contents:
```

```







<br>

Thus, the flag is:
```log
flag{l0c4l_f1l3_1nclusi0n_f0r_7h3_w1n}
```
