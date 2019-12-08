good = "❤"
bad = "💔"

one = "🔥"
zero = "❄"

with open("task/task.txt", "rb") as f:
    enc = f.read().decode("utf-8")

m = ""

for i in range(0, len(enc), 2):
    if enc[i] == good:
        if enc[i + 1] == zero:
            m += "0"
        else:
            m += "1"

for i in range(0, len(m), 8):
    print(chr(int(m[i:i+8], 2)), end='')
print()