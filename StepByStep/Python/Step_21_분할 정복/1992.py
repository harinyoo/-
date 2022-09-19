def quad_tree(x, y, n):
    global ans
    check = screen[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != screen[i][j]:
                ans += '('
                quad_tree(x, y, n//2)
                quad_tree(x, y+n//2, n//2)
                quad_tree(x+n//2, y, n//2)
                quad_tree(x+n//2, y+n//2, n//2)
                ans += ')'
                return
    if check == 0:
        ans += '0'
        return
    else:
        ans += '1'
        return


N = int(input())
screen = [list(map(int, input())) for _ in range(N)]
ans = ''
quad_tree(0, 0, N)
print(ans)
