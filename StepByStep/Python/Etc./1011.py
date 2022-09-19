import math
T = int(input())
for test in range(T):
    x, y = map(int, input().split())
    dis = y - x
    num = 1
    while num < math.sqrt(dis):
        num += 1
    if dis <= math.pow(num-1, 2) + (num-1):
        print((num-1)*2)
    else:
        print((num-1)*2+1)