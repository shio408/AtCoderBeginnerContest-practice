import sys

s = sorted(input())
t = sorted(input(), reverse=True)

print("Yes") if s<t else print("No")