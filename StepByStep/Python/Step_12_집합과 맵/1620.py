import sys

N, M = map(int, sys.stdin.readline().split())
dictionary = {}
for n in range(N):
    name = sys.stdin.readline().strip()
    dictionary[name] = n
    dictionary[n] = name

for m in range(M):
    q = sys.stdin.readline().strip()
    if q.isdigit():
        print(dictionary[int(q)-1])
    else:
        print(dictionary[q]+1)
