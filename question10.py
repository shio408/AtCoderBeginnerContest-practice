import sys

s = input()
s = s[::-1]

divide = ["dream", "dreamer", "erase", "eraser"]

for i in range(len(divide)):
    divide[i] = divide[i][::-1]

i = 0
can = True
while i < len(s):
    can2 = False
    for j in range(len(divide)):
        d = divide[j]
        if s[i:i+len(d)] == d:
            can2 = True
            i += len(d)
    if not can2:
        can = False
        break

if can:
    print("YES")
else:
    print("NO")
