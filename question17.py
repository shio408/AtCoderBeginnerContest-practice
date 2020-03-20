import sys

word = input()

print(word[0] + str(len(word[1:-1])) + word[-1])