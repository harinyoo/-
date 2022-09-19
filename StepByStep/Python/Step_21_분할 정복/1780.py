import sys

def nine_tree(x, y, n):
    global minus_one, zero, one
    check = matrix[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != matrix[i][j]:
                nine_tree(x, y, n // 3)
                nine_tree(x, y + n // 3, n // 3)
                nine_tree(x, y + n // 3 * 2, n // 3)
                nine_tree(x + n // 3, y, n // 3)
                nine_tree(x + n // 3, y + n // 3, n // 3)
                nine_tree(x + n // 3, y + n // 3 * 2, n // 3)
                nine_tree(x + n // 3 * 2, y, n // 3)
                nine_tree(x + n // 3 * 2, y + n // 3, n // 3)
                nine_tree(x + n // 3 * 2, y + n // 3 * 2, n // 3)
                return
    if check == -1:
        minus_one += 1
        return
    elif check == 0:
        zero += 1
        return
    else:
        one += 1
        return


N = int(input())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
minus_one = 0
zero = 0
one = 0
nine_tree(0, 0, N)
print(minus_one)
print(zero)
print(one)