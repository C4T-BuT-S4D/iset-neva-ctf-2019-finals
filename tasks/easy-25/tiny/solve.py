import re

with open("task/logs.txt", "r") as f:
    logs = f.read()

r = re.findall("\[0000\.46\] Init: User: (.)", logs)

print(''.join(r))