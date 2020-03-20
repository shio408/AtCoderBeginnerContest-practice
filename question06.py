import sys

num = list(map(int, input().split()))

if len(num) == 3:
    N = num[0]
    A = num[1]
    B = num[2]

    if N >= 1 and N <= 10**4:
        if A >= 1 and A <= B and B <= 36:
            if type(N) is int and type(A) is int and type(B) is int:
                sum_num = 0
                for i in range(1, N+1):
                    sum_tmp = 0
                    seisu = i
                    for j in range(len(str(i))):
                        sum_tmp += seisu % 10
                        seisu -= seisu%10
                        seisu = seisu/10
                        if seisu <= 0:
                            break
                    
                    if sum_tmp>=A and sum_tmp<=B:
                        sum_num += i
                        
                print(sum_num)   

            else:
                print("入力は整数にしてください")
        else:
            print("A, Bが正しくないです")
    else:
        print("Nが正しくないです")

else:
    print("入力が正しくないです")