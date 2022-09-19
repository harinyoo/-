import sys
from collections import deque


def DFS(num):
    print(num, end=' ')
    visited[num] = True
    for n in graph[num]:
        if not visited[n]:
            DFS(n)


def BFS(num):
    queue = deque([num])
    visited[num] = True
    while queue:
        n = queue.popleft()
        print(n, end=' ')
        for m in graph[n]:
            if not visited[m]:
                queue.append(m)
                visited[m] = True


N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

visited = [False] * (N+1)
DFS(V)
print()
visited = [False] * (N+1)
BFS(V)
