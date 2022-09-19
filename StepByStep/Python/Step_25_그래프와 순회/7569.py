import sys
from collections import deque

directions = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]


def BFS():
    while queue:
        tmp = queue.popleft()
        z, x, y = tmp[0], tmp[1], tmp[2]
        for i in range(6):
            h = z + directions[i][0]
            r = x + directions[i][1]
            c = y + directions[i][2]
            if 0 <= h < H and 0 <= r < N and 0 <= c < M and tomatoes[h][r][c] == 0:
                queue.append([h, r, c])
                tomatoes[h][r][c] = tomatoes[z][x][y] + 1


M, N, H = map(int, sys.stdin.readline().split())
tomatoes = []
for _ in range(H):
    tomatoes.append([list(map(int, sys.stdin.readline().split())) for _ in range(N)])

queue = deque()
for height in range(H):
    for row in range(N):
        for col in range(M):
            if tomatoes[height][row][col] == 1:
                queue.append([height, row, col])

BFS()
days = -2
for height in range(H):
    for row in range(N):
        if 0 in tomatoes[height][row]:
            print(-1)
            exit()
        else:
            days = max(days, max(tomatoes[height][row]))
print(days - 1)
