import sys

n, m = map(int, input().split())

toshi = [list(map(int, input().split())) for i in range(m)]

toshi_flag = [0] * n

for i in range(len(toshi)):
    for j in range(len(toshi[i])):
        toshi_flag[toshi[i][j] - 1] += 1

for item in toshi_flag:
    print("{}".format(item))