import sys

N = int(input())
coordinates = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coordinates.append([x, y])

coordinates.sort(key=lambda k: (k[0], k[1]))
for num in coordinates:
    print(num[0], num[1])
