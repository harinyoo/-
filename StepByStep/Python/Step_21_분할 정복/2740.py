N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

M_, K = map(int, input().split())
B = []
for i in range(M_):
    B.append(list(map(int, input().split())))

ans = [[0 for _ in range(K)] for _ in range(N)]
for n in range(N):
    for k in range(K):
        for m in range(M):
            ans[n][k] += A[n][m]*B[m][k]

for row in ans:
    for col in row:
        print(col, end=' ')
    print()
