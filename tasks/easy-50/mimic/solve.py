import requests

part1 = requests.get("http://127.0.0.1:33021/robots.txt").text
part2 = requests.get("http://127.0.0.1:33021/humans.txt").text

print(part1 + part2)
