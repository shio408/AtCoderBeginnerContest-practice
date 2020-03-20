import sys

N = int(input())

num = list(map(int, input().split()))

num_list = []
for item in num:
    num_list.append(item)

if N == len(num):
    
    cnt = 0
    frag = False

    while True:

        for item in num_list:
            if item%2 != 0:
                frag = True

        if frag == True:
            break
        
        for i in range(len(num_list)):
            num_list[i] = num_list[i] / 2

        cnt += 1

    print(cnt)
else:
    print("整数の数が正しくありません")