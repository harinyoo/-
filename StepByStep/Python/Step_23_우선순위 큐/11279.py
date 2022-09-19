import sys
import heapq

N = int(input())
heap = []
for i in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (-num))
    else:
        if heap:
            print(-1 * heapq.heappop(heap))
        elif not heap:
            print(0)
