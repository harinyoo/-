import sys
sys.setrecursionlimit(150000)


def DFS(V, E, start):
    global idx
    visited[start] = True
    idx += 1
    ans[start] = idx
    for num in E[start]:
        if not visited[num]:
            DFS(V, E, num)


N, M, R = map(int, sys.stdin.readline().split())
vertex = [i for i in range(N+1)]
graph = [[] for _ in range(N+1)]
for m in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for n in range(1, N+1):
    graph[n].sort()

visited = [False for _ in range(N+1)]
ans = [0 for _ in range(N+1)]
idx = 0
DFS(vertex, graph, R)
for n in range(1, N+1):
    print(ans[n])
