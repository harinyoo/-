import sys


def MulMetrix(a, b):
    if b == 1:
        return a

    elif b % 2:
        tmp = MulMetrix(a, b-1)
        c = [[0 for _ in range(N)] for _ in range(N)]
        for x in range(N):
            for y in range(N):
                for z in range(N):
                    c[x][y] += tmp[x][z] * a[z][y]
                c[x][y] %= 1000
        return c

    else:
        tmp = MulMetrix(a, b//2)
        c = [[0 for _ in range(N)] for _ in range(N)]
        for x in range(N):
            for y in range(N):
                for z in range(N):
                    c[x][y] += tmp[x][z] * tmp[z][y]
                c[x][y] %= 1000
        return c


N, B = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

result = MulMetrix(A, B)

for row in result:
    for col in row:
        print(col % 1000, end=' ')
    print()
