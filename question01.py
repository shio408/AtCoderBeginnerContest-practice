# import sys

# def sum(a, b, c):
#      return int(a) + int(b) + int(c)

# data = []

# for i in range(4):
#     data.append(input())

# result = sum(data[0], data[1], data[2])

# print(result)
# print(data[3])

# answer
a = int(input())

b, c = map(int, input().split())

s = input()

print("{} {}".format(a+b+c, s))

# old_list = [0, 1, 2]

# new_list = list(filter(lambda x: x%2==0, old_list))

# print(new_list)
