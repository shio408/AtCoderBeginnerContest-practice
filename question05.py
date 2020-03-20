import sys

coin_500 = int(input())
coin_100 = int(input())
coin_50 = int(input())

gokei = int(input())

pattern = 0

if coin_500<=50 and coin_500>=0 and coin_100<=50 and coin_100>=0 and coin_50<=50 and coin_50>=0:
    if coin_500+coin_100+coin_50>=1:
        if gokei<=20000 and gokei>=50:
            if type(coin_500) is int and type(coin_100) is int and type(coin_50) is int:
                if gokei%50 == 0:
                    for i in range(coin_500+1):
                        for j in range(coin_100+1):
                            for k in range(coin_50+1):
                                if (gokei - (500*i) - (100*j) - (50*k) )== 0:
                                    pattern += 1
                    
                    print(pattern)

                else:
                    print("合計金額は50の倍数にしてください")
            else:
                print("コインの枚数は整数にしてください")
        else:
            print("合計金額は50円以上20000円以下にしてください")
    else:
        print("合計枚数は1枚以上です")
else:
    print("0以下50枚以上は選択できません")