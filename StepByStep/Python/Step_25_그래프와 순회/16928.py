import sys
from collections import deque

dice = [1, 2, 3, 4, 5, 6]


def BFS():
    queue = deque([1])
    visited[1] = 1
    while queue:
        num = queue.popleft()
        if num == 100:
            return visited[num]-1

        for i in dice:
            if num+i < 101 and not visited[num+i]:
                visited[num + i] = visited[num] + 1
                if num+i in ladder.keys():
                    if not visited[ladder[num+i]]:
                        visited[ladder[num+i]] = visited[num] + 1
                    queue.append(ladder[num+i])
                elif num+i in snake.keys():
                    if not visited[snake[num + i]]:
                        visited[snake[num+i]] = visited[num] + 1
                    queue.append(snake[num+i])
                else:
                    queue.append(num+i)


N, M = map(int, sys.stdin.readline().split())

ladder = {}
for n in range(N):
    x, y = map(int, sys.stdin.readline().split())
    ladder[x] = y

snake = {}
for m in range(M):
    u, v = map(int, sys.stdin.readline().split())
    snake[u] = v

visited = [0 for _ in range(101)]
print(BFS())
