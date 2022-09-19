import sys
sys.setrecursionlimit(10000)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(row, col):
    if ground[row][col] == 1:
        ground[row][col] = 0
        for t in range(4):
            nx = row + dx[t]
            ny = col + dy[t]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            DFS(nx, ny)
        return True
    return False


T = int(sys.stdin.readline())
for test in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    ground = [[0 for _ in range(M)] for _ in range(N)]
    for k in range(K):
        x, y = map(int, sys.stdin.readline().split())
        ground[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if DFS(i, j):
                cnt += 1
    print(cnt)


