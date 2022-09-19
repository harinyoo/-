import sys

N = int(input())
words = []
for n in range(N):
    words.append(sys.stdin.readline().strip())

words = list(set(words))
words.sort(key=lambda k: (len(k), k))
for word in words:
    print(word)