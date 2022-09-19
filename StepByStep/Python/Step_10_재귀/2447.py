def draw_star(n):
    global pattern

    if n == 3:
        pattern[0][:3] = pattern[2][:3] = '*' * 3
        pattern[1][:3] = ['*', ' ', '*']
        return

    a = n//3
    draw_star(n//3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                pattern[a*i+k][a*j:a*(j+1)] = pattern[k][:a]


N = int(input())
pattern = [[' ' for i in range(N)] for j in range(N)]
draw_star(N)

for x in pattern:
    for y in x:
        print(y, end='')
    print()