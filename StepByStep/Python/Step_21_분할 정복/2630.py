def quad_tree(x, y, n):
    global white, blue
    check = color[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != color[i][j]:
                quad_tree(x, y, n//2)
                quad_tree(x, y+n//2, n//2)
                quad_tree(x+n//2, y, n//2)
                quad_tree(x+n//2, y+n//2, n//2)
                return
    if check == 0:
        white += 1
        return
    else:
        blue += 1
        return


N = int(input())
color = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0
quad_tree(0, 0, N)
print(white)
print(blue)

