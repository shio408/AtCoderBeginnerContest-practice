import sys

n, x = map(int, input().split())

a = list(map(int, input().split()))

a.sort()

# cnt_children = 0
# for i in range(n):
#     if x >= a[i]:
#         cnt_children += 1
#         x -= a[i]
#     else:
#         break

# if x > 0 and cnt_children == n:
#     cnt_children -= 1

# print("{}".format(cnt_children))

# cnt_candy = 0
# cnt_children = 0
# for item in a:
#     if cnt_candy < x:
#         cnt_candy += item
#         cnt_children += 1

# if cnt_candy != x:
#     cnt_children -= 1

# print("{}".format(cnt_children))

if x == sum(a):
    print("{}".format(n))
else:    
    cnt_candy = 0
    cnt_children = 0

    for index, item in enumerate(a):
        cnt_candy += item
        if x >= cnt_candy:
            cnt_children = index + 1

    if x > sum(a):
        print("{}".format(n-1))
    else:
        print("{}".format(cnt_children))