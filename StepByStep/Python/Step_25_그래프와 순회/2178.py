import sys
from collections import deque

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def BFS(row, col):
    queue = deque([[row, col]])
    visited[row][col] = True
    while queue:
        tmp = queue.popleft()
        x, y = tmp[0], tmp[1]
        for i in range(4):
            r = x+directions[i][0]
            c = y+directions[i][1]
            if r < 1 or r > N or c < 1 or c > M or not maze[r][c] or visited[r][c]:
                continue
            queue.append([r, c])
            visited[r][c] = True
            maze[r][c] += maze[x][y]
    return maze[N][M]


N, M = map(int, sys.stdin.readline().split())
maze = [[0 for _ in range(M+1)]]
for n in range(N):
    maze.append([0]+list(map(int, input())))

visited = [[False for _ in range(M+1)] for _ in range(N+1)]
print(BFS(1, 1))
