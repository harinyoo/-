import sys
from collections import deque

directions = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]


def BFS():
    while queue:
        [x, y] = queue.popleft()
        if x == ex and y == ey:
            return visited[ex][ey]

        for i, j in directions:
            if 0 <= x+i < l and 0 <= y+j < l and not visited[x+i][y+j]:
                visited[x+i][y+j] = visited[x][y] + 1
                queue.append([x+i, y+j])


T = int(input())
for test in range(T):
    l = int(sys.stdin.readline())
    sx, sy = map(int, sys.stdin.readline().split())
    ex, ey = map(int, sys.stdin.readline().split())

    queue = deque([[sx, sy]])
    visited = [[0 for _ in range(l)] for _ in range(l)]
    print(BFS())