N, M = map(int, input().split())
visited = [False] * (N + 1)
arr = []


def backtrack(depth, n, m):
    if depth == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            backtrack(depth + 1, n, m)
            visited[i] = False
            arr.pop()


backtrack(0, N, M)
