N = int(input())
chess = [0] * 14
cnt = 0


def is_promising(x):
    for i in range(x):
        if chess[x] == chess[i] or x-i == abs(chess[x]-chess[i]):
            return False
    return True


def N_Queen(row):
    global cnt
    if row == N:
        cnt += 1
        return

    for col in range(N):
        chess[row] = col
        if is_promising(row):
            N_Queen(row+1)


N_Queen(0)
print(cnt)

