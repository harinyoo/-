############ BFS ############
# import sys
# from collections import deque
#
#
# def BFS():
#     visited = [False for _ in range(V + 1)]
#     for j in range(1, V+1):
#         if not visited[j]:
#             queue = deque([j])
#             visited[j] = True
#             while queue:
#                 num = queue.popleft()
#                 for n in graph[num]:
#                     if not visited[n]:
#                         queue.append(n)
#                         visited[n] = -1 * visited[num]
#                     elif visited[n] == visited[num]:
#                         return "NO"
#     return "YES"
#
#
# K = int(input())
# for k in range(K):
#     V, E = map(int, sys.stdin.readline().split())
#     graph = [[] for _ in range(V+1)]
#     for e in range(E):
#         u, v = map(int, sys.stdin.readline().split())
#         graph[u].append(v)
#         graph[v].append(u)
#
#     for i in range(1, V+1):
#         graph[i].sort()
#
#     print(BFS())






############ DFS ############
import sys
sys.setrecursionlimit(10**6)


def DFS(start):
    for n in graph[start]:
        if not visited[n]:
            visited[n] = -1 * visited[start]
            if not DFS(n):
                return False
        elif visited[n] == visited[start]:
            return False
    return True


K = int(input())
for k in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    for e in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V+1):
        graph[i].sort()

    visited = [False for _ in range(V+1)]
    res = True
    for i in range(1, V+1):
        if not visited[i]:
            visited[i] = True
            res = DFS(i)
            if not res:
                break
    print("YES" if res else "NO")
