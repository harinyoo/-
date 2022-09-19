N, M = map(int, input().split())
visited = [False] * (N + 1)
arr = [0]


def solve(depth, n, m):
    if depth == m:
        for i in range(1, M + 1):
            print(arr[i], end=' ')
        print()
        return
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            if arr[depth] < arr[depth + 1]:
                solve(depth + 1, n, m)
            visited[i] = False
            arr.pop()


solve(0, N, M)
