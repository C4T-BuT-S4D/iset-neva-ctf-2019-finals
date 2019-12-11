#!/usr/bin/env python3

import string
import secrets
import base64
import time

alph = string.ascii_lowercase
flag = open('flag.txt').read()


def caesar(n=10):
    s = ''.join(secrets.choice(string.ascii_lowercase) for _ in range(n))
    enc = ''.join(alph[(alph.find(c) + 1) % len(alph)] for c in s)
    return "Caesar cipher", s, enc


def atbash(n=10):
    s = ''.join(secrets.choice(string.ascii_lowercase) for _ in range(n))
    enc = ''.join(alph[len(alph) - alph.find(c) - 1] for c in s)
    return "Atbash cipher", s, enc


def c_base64(n=10):
    s = ''.join(secrets.choice(string.ascii_lowercase) for _ in range(n))
    enc = base64.b64encode(s.encode()).decode()
    return "Base64 encode", s, enc


def c_base32(n=10):
    s = ''.join(secrets.choice(string.ascii_lowercase) for _ in range(n))
    enc = base64.b32encode(s.encode()).decode()
    return "Base32 encode", s, enc


def c_base85(n=10):
    s = ''.join(secrets.choice(string.ascii_lowercase) for _ in range(n))
    enc = base64.b85encode(s.encode()).decode()
    return "Base85 encode", s, enc


ciphers = [
    caesar,
    atbash,
    c_base64,
    c_base32,
    c_base85,
]

print('Welcome!')
time.sleep(0.5)
print('I have a victorine for you!')
time.sleep(0.5)
print('Answer all my questions, and I\'ll give you the flag!')
time.sleep(0.5)

for i in range(15):
    try:
        c = secrets.choice(ciphers)
        t, pt, ct = c()
        print(f'Here\'s a string for you: {ct}')
        time.sleep(0.5)
        print(f'It\'s encrypted with {t}')
        time.sleep(0.5)
        inp = input('Can you decrypt it?\n>').strip()
        if inp != pt:
            print('You lose!')
            break
        print('Nice!')
        time.sleep(0.5)
    except:
        print('Error!')
        exit(1)
else:
    print('Well done!')
    time.sleep(0.5)
    print('Here\'s your flag:')
    time.sleep(0.5)
    print(flag)
