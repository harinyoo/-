##### 틀린 코드 (이유는 모름) #####
# import sys
#
# n = int(sys.stdin.readline())
# arr = []
# for _ in range(n):
#     r, c = map(int, sys.stdin.readline().split())
#     arr.append([r, c])
#
# if n == 1:
#     print(0)
# else:
#     D = [[arr[i][0]*arr[i][1] for i in range(n)] for _ in range(n)]
#     A = [[0 for _ in range(n)] for _ in range(n)]
#     for i in range(n-1):
#         D[i][i+1] = arr[i][0] * arr[i][1] * arr[i+1][1]
#         A[i][i+1] = i+1
#
#     for dig in range(2, n):
#         for i in range(n-dig):
#             j = dig + i
#             minNum = 2 ** 31
#             for k in range(A[i][j-1], A[i+1][j]+1):
#                 if i == k-1:
#                     tmp = D[i][i] * arr[j][1] + D[k][j]
#                 elif k == j:
#                     tmp = D[i][k-1] + D[j][j] * arr[i][0]
#                 else:
#                     tmp = D[i][k-1] + D[k][j] + arr[i][0] * arr[k][0] * arr[j][1]
#                 if minNum > tmp:
#                     minNum = tmp
#                     A[i][j] = k
#             D[i][j] = minNum
#     print(D[0][n-1])


# import sys
#
# N = int(sys.stdin.readline())
# sizes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# sizes = [a for a, _ in sizes] + [sizes[-1][1]]
# dp = [[0] * N for _ in range(N)]
#
# for l in range(1, N):    # l = 길이(곱할 행렬 개수)
#     for y in range(N-l): # y = 곱의 첫 행렬(시작하는 인덱스)
#         x = y + l        # x = 곱의 마지막 행렬(끝나는 인덱스)
#         m = sizes[y] * sizes[x+1]  #곱한 결과 행렬의 크기(시작하는 행렬의 행 * 끝나는 행렬의 열)
#         min_yx = min(yk + xk + sz * m for yk, xk, sz in zip(dp[y][y:x], dp[x][y+1:x+1], sizes[y+1:x+1]))
#         # dp[y][y:x]   >>>>>   y <= k < x
#         # dp[x][y+1:x+1]
#         # sizes[y+1:x+1]   >>>>>
#         # yk + xk + sz * m =
#         dp[y][x] = dp[x][y] = min_yx
#
# print(dp[0][-1])


import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr = [row for row, col in arr] + [arr[-1][1]]
D = [[0 for _ in range(N)] for _ in range(N)]

for dig in range(1, N):
    for x in range(N-dig):
        y = x + dig
        m = arr[x] * arr[y+1]
        D[x][y] = D[y][x] = min(xk + ky + k * m for xk, ky, k in zip(D[x][x:y], D[y][x+1:y+1], arr[x+1:y+1]))

print(D[0][-1])
