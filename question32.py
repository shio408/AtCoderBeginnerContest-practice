import sys

n, l = map(int, input().split())

s = [input() for i in range(n)]

s.sort()

min_str = ""

for item in s:
    min_str += item

print("{}".format(min_str))