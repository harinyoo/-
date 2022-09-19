import sys

N, M = map(int, sys.stdin.readline().split())
B = [0] + list(map(int, sys.stdin.readline().split()))
C = [0] + list(map(int, sys.stdin.readline().split()))
D = [[0 for _ in range(sum(C)+1)] for _ in range(N+1)]
result = sum(C)

for i in range(1, N+1):
    byte = B[i]
    cost = C[i]

    for j in range(sum(C)+1):
        if j < cost:
            D[i][j] = D[i-1][j]
        else:
            D[i][j] = max(byte+D[i-1][j-cost], D[i-1][j])

        if D[i][j] >= M:
            result = min(result, j)

print(result)
