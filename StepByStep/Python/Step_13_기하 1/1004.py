import sys
from math import sqrt


T = int(sys.stdin.readline())
for t in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    cnt = 0
    for i in range(n):
        cx, cy, r = map(int, sys.stdin.readline().split())
        l1 = sqrt((cx-x1)**2 + (cy-y1)**2)
        l2 = sqrt((cx-x2)**2 + (cy-y2)**2)
        if (r-l1) * (r-l2) < 0:
            cnt += 1
    print(cnt)
