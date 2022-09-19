import sys

while True:
    num = list(map(int, sys.stdin.readline().split()))
    if num[0] == 0:
        break
    n = num[0]
    height = []
    for i in range(n):
        height.append(num[i + 1])

    min_height = min(height)
    max_height = max(height)
    area = []

    for i in range(min_height, max_height + 1):
        tmp = 0
        i_area = 0
        for j in height:
            if i <= j:
                i_area += i
            else:
                if tmp <= i_area:
                    tmp = i_area
                i_area = 0
        area.append(max(tmp, i_area))

    print(max(area))
