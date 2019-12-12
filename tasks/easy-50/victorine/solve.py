#!/usr/bin/env python3

from pwn import *

context.log_level = 'DEBUG'

alph = string.ascii_lowercase


def caesar(s):
    s = ''.join(alph[(alph.find(c) - 1 + len(alph)) % len(alph)] for c in s)
    return s


def atbash(s):
    s = ''.join(alph[len(alph) - alph.find(c) - 1] for c in s)
    return s


def c_base64(s):
    s = base64.b64decode(s.encode()).decode()
    return s


def c_base32(s):
    s = base64.b32decode(s.encode()).decode()
    return s


def c_base85(s):
    s = base64.b85decode(s.encode()).decode()
    return s


ciphers = {
    'Base64': c_base64,
    'Base32': c_base32,
    'Base85': c_base85,
    'Caesar': caesar,
    'Atbash': atbash,
}

r = remote('localhost', 33002)

while True:
    r.recvuntil('a string for you: ')
    data = r.recvline().decode().strip()
    print(data)

    r.recvuntil('encrypted with ')
    cipher = r.recvline().decode().strip()
    print(cipher)

    for k, v in ciphers.items():
        if k in cipher:
            print('Decoding', k)
            res = v(data)
            print('Got', res)
            r.sendlineafter('decrypt it?\n>', res)
