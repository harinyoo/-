import sys

N = int(input())
info = []
for n in range(N):
    info.append(sys.stdin.readline().split())

info.sort(key=lambda x: (int(x[0])))
for i in info:
    print(i[0], i[1])
