import sys

n = int(input())

zahyo_zero = [0] * 3

zahyo = [list(map(int, input().split())) for i in range(n)]

zahyo.insert(0, zahyo_zero)

can = True

for i in range(n):
    dt = zahyo[i+1][0] - zahyo[i][0]
    dist = abs(zahyo[i+1][1] - zahyo[i][1] + zahyo[i+1][2] - zahyo[i][2])
    if dt < dist:
        can = False
    if dist%2 != dt%2:
        can = False

print("Yes") if can else print("No")