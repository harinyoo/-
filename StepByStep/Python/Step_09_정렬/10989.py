import sys

N = int(sys.stdin.readline())
count = [0]*10001

for i in range(N):
    count[int(sys.stdin.readline())] += 1

for j in range(10001):
    if count[j] != 0:
        for k in range(count[j]):
            print(j)
