import sys

T = int(input())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    for j in range(min(A, B), 0, -1):
        if A % j == 0 and B % j == 0:
            print(A * B // j)
            break
