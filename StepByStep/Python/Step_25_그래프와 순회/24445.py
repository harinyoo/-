import sys
from collections import deque


def BFS(start):
    global cnt
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        ans[v] = cnt
        cnt += 1
        for num in graph[v]:
            if not visited[num]:
                queue.append(num)
                visited[num] = True


N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for m in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
for n in range(1, N+1):
    graph[n].sort(reverse=True)

visited = [False for _ in range(N+1)]
ans = [0 for _ in range(N+1)]
cnt = 1
BFS(R)
for i in ans[1:N+1]:
    print(i)
