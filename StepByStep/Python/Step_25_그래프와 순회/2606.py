import sys


def DFS(num):
    global cnt
    visited[num] = True
    for j in graph[num]:
        if not visited[j]:
            cnt += 1
            DFS(j)


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

cnt = 0
visited = [False for _ in range(N+1)]
DFS(1)
print(cnt)
