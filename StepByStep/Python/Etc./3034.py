import sys
import math

N, W, H = map(int, sys.stdin.readline().split())
D = math.sqrt(W ** 2 + H ** 2)

for n in range(N):
    length = int(sys.stdin.readline())
    if length <= D:
        print("DA")
    else:
        print("NE")
