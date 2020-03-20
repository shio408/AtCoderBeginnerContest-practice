import sys
import math

n = int(input())

zahyo = [list(map(int, input().split())) for i in range(n)]

direction_store = 0
for i in range(len(zahyo)):
    for j in range(i, len(zahyo)):
        direction = math.sqrt((zahyo[j][0] - zahyo[i][0])*(zahyo[j][0] - zahyo[i][0])
                            + (zahyo[j][1] - zahyo[i][1])*(zahyo[j][1] - zahyo[i][1]))
        if i == 0 and j == 0:
            direction_store = direction
        else:
            if direction_store < direction:
                direction_store = direction


print("{}".format(direction_store))
