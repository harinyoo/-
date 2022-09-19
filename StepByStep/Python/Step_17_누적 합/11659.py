import sys

N, M = map(int, sys.stdin.readline().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))
for r in range(1, N+1):
    arr[r] += arr[r-1]

for r in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(arr[j]-arr[i-1])
