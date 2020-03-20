import sys
import math

n = int(input())

flag = False
for i in range(math.ceil(n/4) + 1):
    for j in range(math.ceil(n/7) + 1):
        if n - (4*i) - (7*j) == 0:
            flag = True

print("Yes") if flag else print("No")