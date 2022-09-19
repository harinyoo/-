import sys
import heapq

heap = []
N = int(input())
for i in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        elif not heap:
            print(0)

