import sys

n, k = map(int, input().split())

a = list(map(int, input().split()))

num_flag = [0 for i in range(n)]

for item in a:
    num_flag[item - 1] += 1

# while 0 in num_flag:
#     num_flag.remove(0)

# num_flag.sort()

# cnt = 0
# while len(num_flag) > k:
#     print(len(num_flag))
#     cnt += num_flag[0]
#     num_flag.pop(0)

num_flag.sort(reverse=True)

cnt = 0
for i in range(k):
    cnt += num_flag[i]

print("{}".format(n - cnt))