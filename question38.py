n = int(input())
s = [input() for i in range(n)]

m = int(input())
t = [input() for i in range(m)]

mojiretsu = {}

for item in s:
    if not item in mojiretsu:
        mojiretsu.setdefault(item, 1)
    else:
        mojiretsu[item] += 1

for item in t:
    if not item in mojiretsu:
        mojiretsu.setdefault(item, -1)
    else:
        mojiretsu[item] -= 1

# mojiretsu_sorted = sorted(mojiretsu.items(), key=lambda x:x[1], reverse=True)

# print("{}".format(mojiretsu_sorted.values()))

max_coin = 0
for i in mojiretsu.values():
    if max_coin < i:
        max_coin = i

print("{}".format(max_coin))