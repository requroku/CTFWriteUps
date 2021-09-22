# H@cktivityCon 2021 Write-up. Warmups - Bass64

## Description:
It, uh... looks like someone bass-boosted this? Can you make any sense of it?

| Value | Difficulty   |
| ----- | ------------ |
| 50    | Easy         |

<br>

## Write-up:

The first thing was to open the file and understand whats inside. Opening it right away would give something strange with very long lines. However, using something like markdown `log` syntax highlighting area would automatically format long lines into ones we can easily distinguish. It can also be done with just adjusting width of any text editor window until characters are distinguishable.

```log
 ___ ____ _____  __   ____        __  _ _____ __  __    __     ___     _   _ __        _____        __  __ ____  ____  _     _   _           _____      __   ____        ________     __  __  ____ __  __ ____  __  __               _         __   ______     _ _     ____ _______   __   __  __ ____  _____ _      __  __  ____ _____ ___  
|_ _/ ___|__  /__\ \ / /\ \      / /_| |___  |  \/  |___\ \   / / |__ | \ | |\ \      / / _ \ __  _|  \/  |___ \|  _ \| |__ | \ | |_ __ ___ | ____|   _ \ \ / /\ \      / /__  / |__ |  \/  |/ ___|  \/  |___ \|  \/  |_ __ ___     | | _ __ __\ \ / /___ \   | | | __|__  /|  _ \ \ / /__|  \/  |  _ \|  ___| |__  |  \/  |/ ___|  ___/ _ \ 
 | | |  _  / // __\ V /  \ \ /\ / / _` |  / /| |\/| |_  /\ \ / /| '_ \|  \| | \ \ /\ / / | | |\ \/ / |\/| | __) | |_) | '_ \|  \| | '_ ` _ \|  _|| | | | \ V /  \ \ /\ / /  / /| '_ \| |\/| | |  _| |\/| | __) | |\/| | '_ ` _ \ _  | || '_ ` _ \ V /  __) |  | | |/ /  / / | | | \ V /_  / |\/| | | | | |_  | '_ \ | |\/| | |  _| |_ | (_) |
 | | |_| |/ /_\__ \| |    \ V  V / (_| | / / | |  | |/ /  \ V / | | | | |\  |  \ V  V /| |_| | >  <| |  | |/ __/|  _ <| | | | |\  | | | | | | |__| |_| |  | |    \ V  V /  / /_| | | | |  | | |_| | |  | |/ __/| |  | | | | | | | |_| || | | | | | |  / __/ |_| |   <  / /_ | |_| || | / /| |  | | |_| |  _| | | | || |  | | |_| |  _| \__, |
|___\____/____|___/|_|     \_/\_/ \__,_|/_/  |_|  |_/___|  \_/  |_| |_|_| \_|   \_/\_/  \__\_\/_/\_\_|  |_|_____|_| \_\_| |_|_| \_|_| |_| |_|_____\__, |  |_|     \_/\_/  /____|_| |_|_|  |_|\____|_|  |_|_____|_|  |_|_| |_| |_|\___/ |_| |_| |_|_| |_____\___/|_|\_\/____ |____/ |_|/___|_|  |_|____/|_|   |_| |_||_|  |_|\____|_|     /_/ 
                                                                                                                                                  |___/                                                                              
```

The text inside the file is:  
```log
IGZsYWd7MzVhNWQxM2RhNmEyYWZhMGM2MmJmY2JkZDYzMDFhMGF9
```

Using any Base64 encoder/decoder tool we can easily get the flag:
```log
flag{35a5d13da6a2afa0c62bfcbdd6301a0a}
```

<br>

The original file can be found [here](https://github.com/requroku/CTFWriteUps/tree/main/2021-09-H@cktivityCon/Bass64).
