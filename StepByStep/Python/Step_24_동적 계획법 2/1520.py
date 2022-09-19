import sys

sys.setrecursionlimit(10**6)


def DFS(row, col):
    if row == M-1 and col == N-1:
        return 1

    if visited[row][col] != -1:
        return visited[row][col]

    visited[row][col] = 0
    for i in range(4):
        temp_row = row + dx[i]
        temp_col = col + dy[i]
        if 0 <= temp_row < M and 0 <= temp_col < N:
            if height[temp_row][temp_col] < height[row][col]:
                visited[row][col] += DFS(temp_row, temp_col)
    return visited[row][col]


M, N = map(int, sys.stdin.readline().split())
#height = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
height = []
for _ in range(M):
    height.append(list(map(int, sys.stdin.readline().split())))
visited = [[-1 for _ in range(N)] for _ in range(M)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

print(DFS(0, 0))
