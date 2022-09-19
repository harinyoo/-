import sys

board = []
zero = []
cnt = 0
for i in range(9):
    board.append(list(map(int, sys.stdin.readline().split())))
    for j in range(9):
        if board[i][j] == 0:
            zero.append([i, j])
            cnt += 1


def is_promising(row, col):
    for c in range(9):
        if c == col:
            continue
        if board[row][c] == board[row][col]:
            return False
    for r in range(9):
        if r == row:
            continue
        if board[r][col] == board[row][col]:
            return False
    for r in range(row//3*3, row//3*3+3):
        for c in range(col//3*3, col//3*3+3):
            if r == row and c == col:
                continue
            if board[r][c] == board[row][col]:
                return False
    return True


def sudoku(blank):
    if blank == cnt:
        for idx in range(9):
            print(' '.join(map(str, board[idx])))
        sys.exit(0)

    for n in range(1, 10):
        board[zero[blank][0]][zero[blank][1]] = n
        if is_promising(zero[blank][0], zero[blank][1]):
            sudoku(blank + 1)
        board[zero[blank][0]][zero[blank][1]] = 0


sudoku(0)

