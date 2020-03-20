import sys
import math

def minSum(n):
    min_sum = 0
    for i in range(1, n):
        a = i
        b = n - i
        min_sum_a, min_sum_b = 0, 0
        while  a > 0:
            min_sum_a += a%10
            a = math.floor(a/10)
        while b > 0:
            min_sum_b += b%10
            b = math.floor(b/10)
        
        if i == 1:
            min_sum = min_sum_a + min_sum_b
        else:
            if min_sum > min_sum_a + min_sum_b:
                min_sum = min_sum_a + min_sum_b
    return min_sum

n = int(input())

print("{}".format(minSum(n)))

