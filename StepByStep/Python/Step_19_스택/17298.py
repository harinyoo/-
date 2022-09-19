import sys
N = int(input())
seq = list(map(int, sys.stdin.readline().split()))
idx = [0]
ans = [-1] * N


for i in range(1, N):
    while idx and seq[idx[-1]] < seq[i]:
        ans[idx.pop()] = seq[i]
    idx.append(i)

print(*ans)