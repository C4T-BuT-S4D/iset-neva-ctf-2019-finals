good = "❤"
bad = "💔"

one = "🔥"
zero = "❄"

from random import randint

flag = "flag{l0v3_u_<3}"

m = ""

for i in flag:
    m += bin(ord(i))[2:].zfill(8)

enc = u""

i = 0
while i < len(m):
    fake = randint(0, 1)
    if fake == 1:
        enc += bad
        enc += [one, zero][randint(0, 1)]
    else:
        enc += good
        enc += [zero, one][int(m[i])]
        i += 1

with open("task/task.txt", "wb") as f:
    f.write(enc.encode("utf-8"))
