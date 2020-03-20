import sys
import math

n = int(input())

# str_n = str(n)

# harshad = 0
# for i in range(len(str_n)):
#     harshad += int(str_n[i])

# print("Yes") if n%harshad == 0 else print("No")

harshad = 0
num = n
for i in range(len(str(n))):
    harshad += num % 10
    num = math.floor(num / 10)

print("Yes") if n%harshad == 0 else print("No")