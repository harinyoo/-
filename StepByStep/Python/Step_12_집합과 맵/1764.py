import sys


N, M = map(int, sys.stdin.readline().split())

arr1 = []
for i in range(N):
    arr1.append(sys.stdin.readline().strip())
arr1.sort()

dic1 = {}
for i in arr1:
    dic1[i] = 0

cnt = 0
for i in range(M):
    s = sys.stdin.readline().strip()
    if s in dic1:
        cnt += 1
        dic1[s] += 1

print(cnt)
for i in dic1:
    if dic1[i] != 0:
        print(i)


