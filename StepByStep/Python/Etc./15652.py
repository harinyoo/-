N, M = map(int, input().split())
arr = [0]


def solve(idx):
    if len(arr) == M + 1:
        for i in range(1, M+1):
            print(arr[i], end = ' ')
        print()
        return
    for i in range(1, N+1):
        arr.append(i)
        if arr[idx] <= arr[idx + 1]:
            solve(idx + 1)
        arr.pop()


solve(0)
