from base64 import b32decode, b64decode
from binascii import unhexlify
from hashlib import md5
from pwn import *

io = remote('5.101.72.234', '33022')

for i in range(2):
    io.recvuntil('data\n')
    message = io.recvuntil('\n')[:-1]
    io.sendline(unhexlify(message))
for i in range(2):
    io.recvuntil('data\n')
    message = io.recvuntil('\n')[:-1]
    io.sendline(b32decode(message))
for i in range(4):
    io.recvuntil('data\n')
    message = io.recvuntil('\n')[:-1]
    io.sendline(b64decode(message))
for i in range(2):
    io.recvuntil('data\n')
    md5_hash = io.recvuntil('\n')[:-1]
    for j in range(256):
        if md5(chr(j)).hexdigest() == md5_hash:
            io.sendline(chr(j))
            break
io.interactive()
