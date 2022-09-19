import sys
from collections import deque

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def BFS():
    while queue:
        tmp = queue.popleft()
        x = tmp[0]
        y = tmp[1]
        for i in range(4):
            r = x + directions[i][0]
            c = y + directions[i][1]
            if 0 <= r < N and 0 <= c < M and tomatoes[r][c] == 0:
                queue.append([r, c])
                tomatoes[r][c] = tomatoes[x][y] + 1


M, N = map(int, sys.stdin.readline().split())
tomatoes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

queue = deque([])
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            queue.append([i, j])
BFS()

days = -2
for row in tomatoes:
    if 0 in row:
        print(-1)
        exit()
    else:
        days = max(days, max(row))
print(days - 1)

