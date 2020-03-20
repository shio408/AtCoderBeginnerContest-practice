import sys

N = int(input())
omoti = []

flag = True

for i in range(N):
    omoti.append(int(input()))

omoti.sort(reverse=True)

if N>=1 and N<=100:
    for i in range(len(omoti)):
        if omoti[i]<1 or omoti[i]>100 or not type(omoti[i]) is int:
            flag = False
    if flag==True:
        kagamimoti = []
        kagamimoti_cnt = 0
        for i in range(len(omoti)):
            if i==0:
                kagamimoti.append(omoti[i])
                kagamimoti_cnt += 1
            else:
                if kagamimoti[kagamimoti_cnt-1] > omoti[i]:
                    kagamimoti.append(omoti[i])
                    kagamimoti_cnt += 1

        print(kagamimoti_cnt)      
    else:
        print("半径が正しくないです")
else:
    print("枚数が正しくないです")