import sys

def otoshidama(n, y):
    for i in range(n+1):
        for j in range(n-i+1):
            k = n -i - j
            if y - (10000*i) - (5000*j) - (1000*k) == 0:
                return [i, j, k]
    return[-1, -1, -1]


okane = list(map(int, input().split()))

output = otoshidama(okane[0], okane[1])

print("{} {} {}".format(output[0], output[1], output[2]))
