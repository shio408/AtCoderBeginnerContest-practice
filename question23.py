import sys

s = input()

a_index = s.find("A")
z_index = s.rfind("Z")

print("{}".format(z_index - a_index + 1))

# a_index = 0
# z_index = 0

# for index, item in enumerate(s):
#     if item == "A":
#         a_index = index
#         break

# new_s = ''.join(list(reversed(s)))

# for index, item in enumerate(new_s):
#     if item == "Z":
#         z_index = index
#         break

# print("{} {} {}".format(a_index, len(s) - z_index, (len(s) - z_index) - a_index))