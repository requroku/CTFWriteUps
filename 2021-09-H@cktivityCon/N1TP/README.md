# H@cktivityCon 2021 Write-up. Cryptography - N1TP

## Description:
Nina found some new encryption scheme that she apparently thinks is really cool. She's annoying but she found a flag or something, can you deal with her?

| Value | Difficulty   |
| ----- | ------------ |
| 50    | Easy         |

<br>

## Write-up:
Connecting to the service, we are provided with encrypted flag and allowed to encrypt any string we like.
```log
NINA: Hello! I found a flag, look!
      2b372f6747ea6adc33cd0f71ced9f039c3d803dd36c610eddc16007d63b73d1cd2c5876a01d8
NINA: But I encrypted it with a very special nonce, the same length as 
      the flag! I heard people say this encryption method is unbreakable!
      I'll even let you encrypt something to prove it!! What should we encrypt?
> flag{
NINA: Ta-daaa!! I think this is called a 'one' 'time' 'pad' or something?
      2b372f6747b5348a62d50d7f9888ea6ccbdd52c461cc44b894425c2567a8621383c3cd3d0fc4
NINA: Isn't that cool!?! Want to see it again? 
      Sorry, I forget already -- what was it you wanted to see again?
```


From the context of the challenge we can understand the applied encryption scheme here is a [One-Time Pad](https://en.wikipedia.org/wiki/One-time_pad).

An **OTP** is cryptographically secure unless being re-used:
$$C = M \oplus K$$ 

If a one-time pad is used just twice, simple mathematical operations can reduce it to a running key cipher. For example, if $P_1$ and $P_2$ represent two distinct plaintext messages and they are each encrypted by a common key $K$, then the respective ciphertexts are given by:

$ C_1 = P_1 \oplus K $
$ C_2 = P_2 \oplus K $,

where $\oplus$ means **XOR**. If an attacker were to have both ciphertexts $C_1$ and $C_2$, then simply taking the **XOR** of $C_1$ and $C_2$ yields the **XOR** of the two plaintexts $P_1 \oplus P_2$. (This is because taking the **XOR** of the common key $K$ with itself yields a constant bitstream of zeros.)

Thus, the plaintext flag $F$ can be obtained by the following equation:
$$ F = P \oplus P' \oplus F' $$

where $P$ - is submitted plaintext, $P'$ - encrypted by **OTP** plaintext and $F'$ is the **OTP** encrypted flag.

<br><br>

In order to get the plain flag I wrote a simple script. Because I copied terminal output, I needed a way to transform HEX string to ints:

```python
def HEXstr_to_ints(text: str, base=16):
    """ Convert groups of two chars from hex str to ints. """
    return [int(text[i]+text[i+1], base) for i in range(0, len(text), 2)]
```

I needed a function to convert a plain text to ints as well:

```python
def plain_to_ints(plain_text: str):
    """ Convert ASCII string to a list of ints. """
    return [ord(ch) for ch in plain_text]
```

After that I needed to XOR the corresponding values of encrypted flag, plain text and encrypted text. The result would be the flag.

```python
def main():
    flag_encrypted = '11fdfea632c2fe3807fcbdc68360e71166db3e57509c9880fba21cbb35f24fe5e68728d5cf00'
    text_plain = 'flag{flag{flag{flag{flag{flag{flag{fla'
    text_encrypted = '11fdfea6329da06e56e4bfc8d531fd446ede6f4e0796ccd5b3f640e331ed10eab7816282c11c'

    flag_encrypted_ints = HEXstr_to_ints(flag_encrypted)
    text_plain_ints = plain_to_ints(text_plain)
    text_encrypted_ints = HEXstr_to_ints(text_encrypted)

    flag_chars = []
    for p, p1, f1 in zip(text_plain_ints, text_encrypted_ints, flag_encrypted_ints):
        flag_chars.append(chr(p ^ p1 ^ f1))

    print(''.join(flag_chars))
```

<br>

Thus, the flag is:
```log
flag{9276cdb76a3dd6b1f523209cd9c0a11b}
```

<br>

The full source code can be found [here](https://github.com/requroku/CTFWriteUps/tree/main/2021-09-H@cktivityCon/N1TP).
