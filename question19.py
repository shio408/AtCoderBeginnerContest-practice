import sys

n = int(input())

div_max = 0
div = 1

for i in range(1,n+1):
    cnt = 0
    num = i
    while num%2==0:
        num = num/2
        cnt += 1
    
    if div_max < cnt:
        div_max = cnt
        div = i

print("{}".format(div))