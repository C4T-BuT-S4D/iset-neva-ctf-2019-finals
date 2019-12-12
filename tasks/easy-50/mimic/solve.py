import requests

part1 = requests.get("http://5.101.72.234:33021/robots.txt").text
part2 = requests.get("http://5.101.72.234:33021/humans.txt").text

print(part1 + part2)
