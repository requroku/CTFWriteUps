""" H@cktivityCon 2021 Write-up. Cryptography - N1TP """


def HEXstr_to_ints(text: str, base=16):
    """ Convert groups of two chars from hex str to ints. """
    return [int(text[i]+text[i+1], base) for i in range(0, len(text), 2)]


def plain_to_ints(plain_text: str):
    """ Convert ASCII string to a list of ints. """
    return [ord(ch) for ch in plain_text]


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


if __name__ == '__main__':
    main()
