import sys

a, b = list(map(int, input().split()))

x = 'Even' if (a*b)%2==0 else 'Odd'

print(x)