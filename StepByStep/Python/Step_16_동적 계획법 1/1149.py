import sys
N = int(input())
colorCost = []

for i in range(N):
    r, g, b = map(int, sys.stdin.readline().split())
    colorCost.append([r, g, b])

for j in range(1, N):
    colorCost[j][0] = min(colorCost[j - 1][1], colorCost[j - 1][2]) + colorCost[j][0]
    colorCost[j][1] = min(colorCost[j - 1][0], colorCost[j - 1][2]) + colorCost[j][1]
    colorCost[j][2] = min(colorCost[j - 1][0], colorCost[j - 1][1]) + colorCost[j][2]

print(min(colorCost[N-1][0], colorCost[N-1][1], colorCost[N-1][2]))