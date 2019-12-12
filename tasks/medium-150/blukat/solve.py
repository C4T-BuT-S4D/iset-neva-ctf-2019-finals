from pwn import *
from binascii import unhexlify

FLAG_LEN = 30

freq = [{} for _ in range(FLAG_LEN * 8)]

while True:
    try:
        r = remote("5.101.72.234", 33043)
        r.sendlineafter("Enter option: ", "1")
        r.sendlineafter("Enter your message: ", "a")
        while True:
            r.sendlineafter("Enter option: ", "3")
            r.sendlineafter("Enter option: ", "2")
            r.recvuntil("Encoded message: ")
            message = unhexlify(r.recvline()[:-1][40:-2])
            for i in range(FLAG_LEN):
                for j in range(8):
                    freq[i * 8 + 7 - j][(message[i] >> j) & 1] = freq[i * 8 + 7 - j].get((message[i] >> j) & 1, 0) + 1
            flag_bits = [0 for _ in range(FLAG_LEN * 8)]
            for i in range(FLAG_LEN * 8):
                flag_bits[i] = sorted([(freq[i][c], c) for c in freq[i]])[-1][1]
            flag_bits = ''.join(map(str, flag_bits))
            flag = []
            for i in range(0, len(flag_bits), 8):
                flag.append(int(flag_bits[i:i+8], 2))
            for i in range(8, 16):
                print(freq[i], end='')
            print()
            print(flag_bits)
            print(bytes(flag))
            
    except:
        r.close()
        sleep(1)