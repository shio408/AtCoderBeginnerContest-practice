import sys

N = int(input())
card = list(map(int, input().split()))

card.sort(reverse=True)

flag = True

alice = 0
bob = 0

if N>=1 and N<=100:
    for item in card:
        if not type(item) is int:
            flag = False
            break
    if flag == True:
        cnt = len(card)
        for i in range(cnt):
            if i % 2 == 0:
                alice += card[0]
                card.pop(0)
            else:
                bob += card[0]
                card.pop(0)
        print(alice-bob)
    else:
        print("cardの数は整数です")
else:
    print("Nが正しくないです")