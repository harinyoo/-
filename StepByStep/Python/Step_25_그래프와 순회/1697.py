import sys
from collections import deque

SIZE = 1000001


def BFS():
    while queue:
        num = queue.popleft()
        if num == K:
            return visited[num]

        for nx in (num-1, num+1, num*2):
            if 0 <= nx < SIZE and not visited[nx]:
                visited[nx] = visited[num] + 1
                queue.append(nx)


N, K = map(int, sys.stdin.readline().split())
queue = deque([N])
visited = [0 for _ in range(SIZE)]
print(BFS())
