import sys
import math

a, b = map(int, input().split())

kaibun_cnt = 0
length = len(str(a))
length_half = math.floor(len(str(a))/2)

for i in range(a, b+1):
    num_list = []
    num = i
    
    for j in range(len(str(i))):
        num_list.append(num%10)
        num = math.floor(num/10)
    
    cnt = 0
    for j in range(length_half):
        if num_list[j] == num_list[length-j-1]:
            cnt += 1
    
    if cnt == length_half:
        kaibun_cnt += 1

print("{}".format(kaibun_cnt))