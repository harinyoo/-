import sys


def DFS(num):
    global home
    visited[num] = True
    home += 1
    for i in graph[num]:
        if not visited[i]:
            DFS(i)


N = int(sys.stdin.readline())
houses = [[] for _ in range(N+1)]
for i in range(1, N+1):
    tmp = list(map(int, input()))
    houses[i] = [0] + tmp

graph = [[] for _ in range(N*10+N+1)]
for i in range(N, 0, -1):
    for j in range(N, 0, -1):
        if houses[i][j] == 1:
            if i-1 > 0 and houses[i-1][j] == 1:
                graph[i*10+j].append((i-1)*10+j)
            if j-1 > 0 and houses[i][j-1] == 1:
                graph[i*10+j].append(i*10+(j-1))
            graph[i*10+j].append(i*10+j)
            if j+1 < N+1 and houses[i][j+1] == 1:
                graph[i*10+j].append(i*10+(j+1))
            if i+1 < N+1 and houses[i+1][j] == 1:
                graph[i*10+j].append((i+1)*10+j)

visited = [False for _ in range(N*10+N+1)]
arr = []
for i in range(1, N*10+N+1):
    home = 0
    if graph[i] and not visited[i]:
        DFS(i)
        arr.append(home)

print(len(arr))
arr.sort()
for i in arr:
    print(i)
