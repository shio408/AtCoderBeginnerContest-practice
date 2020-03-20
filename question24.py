import sys

n, x = map(int, input().split())

donut = [int(input()) for i in range(n)]

donut_cnt = n
x -= sum(donut)

donut_min = min(donut)

while x - donut_min >= 0:
    x -= donut_min
    donut_cnt += 1

print("{}".format(donut_cnt))