import sys

n = int(input())

a = list(map(int, input().split()))

a.sort()

max_sum = 0
for i in range(n):
    max_sum += a[3*n - 2*(i+1)]

print("{}".format(max_sum))