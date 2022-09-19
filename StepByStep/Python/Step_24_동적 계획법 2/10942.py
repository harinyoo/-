import sys

N = int(sys.stdin.readline())
nums = [0] + list(map(int, sys.stdin.readline().split()))

D = [[0 for _ in range(N+1)] for _ in range(N+1)]
for length in range(N):
    for start in range(1, N + 1 - length):
        end = start + length
        if start == end:
            D[start][end] = 1
        elif nums[start] == nums[end]:
            if start + 1 == end:
                D[start][end] = 1
            elif D[start+1][end-1] == 1:
                D[start][end] = 1

M = int(sys.stdin.readline())
for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(D[S][E])

