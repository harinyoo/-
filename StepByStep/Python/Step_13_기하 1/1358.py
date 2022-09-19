import sys
from math import sqrt


W, H, X, Y, P = map(int, sys.stdin.readline().split())
r = H//2
cnt = 0
for p in range(P):
    x, y = map(int, sys.stdin.readline().split())
    if X <= x <= X+W and Y <= y <= Y+H:
        cnt += 1
    elif sqrt((X-x)**2 + (Y+r-y)**2) <= r or sqrt((X+W-x)**2 + (Y+r-y)**2) <= r:
        cnt += 1
print(cnt)
