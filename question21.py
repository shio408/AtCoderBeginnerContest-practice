import sys

n = int(input())

t, a = map(int, input().split())

area = list(map(int, input().split()))

temperature_sub = 0
area_no = 0
temperature_store = 0

for index, item in enumerate(area):
    temperature = t - (item*0.006)
    temperature_sub = abs(a - temperature)

    if index == 0:
        temperature_store = temperature_sub
        area_no = index + 1
    else:
        if temperature_store > temperature_sub:
            temperature_store = temperature_sub
            area_no = index + 1

print("{}".format(area_no))