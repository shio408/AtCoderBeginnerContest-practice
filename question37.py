import sys

w, h, n = map(int, input().split())

zahyo = [list(map(int, input().split())) for i in range(n)]

zahyo_hidarishita = [0, 0]
zahyo_migiue = [w, h]

for i in range(n):
    if zahyo[i][2] == 1:
        zahyo_hidarishita[0] = zahyo[i][0]
    elif zahyo[i][2] == 2:
        zahyo_migiue[0] = zahyo[i][0]
    elif zahyo[i][2] == 3:
        zahyo_hidarishita[1] = zahyo[i][1]
    elif zahyo[i][2] == 4:
        zahyo_migiue[1] = zahyo[i][1]

area = (zahyo_migiue[0] - zahyo_hidarishita[0]) * (zahyo_migiue[1] - zahyo_hidarishita[1])

print("{}".format(area))
     

# area = [[0 for i in range(h)] for j in range(w)]

# for i in range(n):
#     if zahyo[i][2] == 1:
#         for j in range(zahyo[i][0]):
#             for k in range(len(area[j])):
#                 area[j][k] = 1
#     elif zahyo[i][2] == 2:
#         for j in range(w - 1, zahyo[i][0] - 1, -1):
#             for k in range(len(area[j])):
#                 area[j][k] = 1
#     elif zahyo[i][2] == 3:
#         for j in range(len(area)):
#             for k in range(zahyo[i][1]):
#                 area[j][k] = 1
#     elif zahyo[i][2] == 4:
#         for j in range(len(area)):
#             for k in range(h - 1, zahyo[i][1] - 1, -1):
#                 area[j][k] = 1

# cnt_zero = 0
# for i in range(len(area)):
#     for j in range(len(area[i])):
#         if area[i][j] == 0:
#             cnt_zero += 1

# print("{}".format(cnt_zero))