import sys
sys.setrecursionlimit(150000)


def DFS(start):
    global cnt
    visited[start] = cnt
    cnt += 1
    for num in graph[start]:
        if not visited[num]:
            DFS(num)


N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for m in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for n in range(N+1):
    graph[n].sort(reverse=True)

visited = [0 for _ in range(N+1)]
cnt = 1
DFS(R)
for i in visited[1:N+1]:
    print(i)