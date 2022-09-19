import sys
from collections import deque

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def BFS():
    queue = deque([[0, 0, 0]])
    visited[0][0][0] = 1
    while queue:
        flag, x, y = queue.popleft()
        if x == N-1 and y == M-1:
            return visited[flag][N-1][M-1]

        for p, q in direction:
            row = x + p
            col = y + q
            if 0 <= row < N and 0 <= col < M and not visited[flag][row][col]:
                if arr[row][col] == 1 and flag == 0:
                    queue.append([1, row, col])
                    visited[1][row][col] = visited[0][x][y] + 1
                elif arr[row][col] == 0:
                    queue.append([flag, row, col])
                    visited[flag][row][col] = visited[flag][x][y] + 1
    return -1


N, M = map(int, sys.stdin.readline().split())
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip())))

visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]
print(BFS())


