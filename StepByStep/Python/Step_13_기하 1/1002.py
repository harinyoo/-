from math import sqrt
T = int(input())
for test in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dis = sqrt((x1-x2)**2 + (y1-y2)**2)
    if dis == 0 and r1 == r2:
        print(-1)
    elif dis < abs(r1 - r2) or dis > r1 + r2:
        print(0)
    elif dis == abs(r1 - r2) or dis == r1 + r2:
        print(1)
    elif dis < r1 + r2:
        print(2)

