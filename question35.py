import sys

s = input()

alphabet = [0]*26

for i in range(len(s)):
    num_alphabet = ord(s[i])
    alphabet[num_alphabet - 97] = 1

index = -1
for i in range(len(alphabet)):
    if alphabet[i] == 0:
        index = i
        break

print("None") if index == -1 else print(chr(index+97))
