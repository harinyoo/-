import sys
SIZE = 21
dp = [[[0] * SIZE for i in range(SIZE)] for j in range(SIZE)]


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]


while True:
    A, B, C = map(int, sys.stdin.readline().split())
    if A == -1 and B == -1 and C == -1:
        break
    print(f'w({A}, {B}, {C}) = {w(A, B, C)}')
