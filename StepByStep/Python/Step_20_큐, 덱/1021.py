from collections import deque

N, M = map(int, input().split())
queue = deque(list(range(N)))
position = list(map(int, input().split()))
for i in range(M):
    position[i] -= 1

cnt = 0
for i in position:
    if queue.index(i) <= len(queue)/2:
        for j in range(queue.index(i)):
            queue.append(queue.popleft())
            cnt += 1
        queue.popleft()
    else:
        for j in range(len(queue)-queue.index(i)):
            queue.appendleft(queue.pop())
            cnt += 1
        queue.popleft()

print(cnt)
