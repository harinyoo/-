from collections import deque

N, K = map(int, input().split())
seq = deque([i for i in range(1, N+1)])

print('<', end='')
while seq:
    for i in range(K-1):
        seq.append(seq.popleft())
    print(seq.popleft(), end='')
    if seq:
        print(',', end=' ')
print('>')
