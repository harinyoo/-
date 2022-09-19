import sys
from collections import deque

# T = int(input())
# for i in range(T):
#     N, M = map(int, sys.stdin.readline().split())
#     rank = list(map(int, sys.stdin.readline().split()))
#     idx = deque([_ for _ in range(N)])
#     turn = 0
#     while idx:
#         max_num = rank[idx[0]]
#         pop_idx = 0
#         for j in range(len(idx)):
#             if max_num < rank[idx[j]]:
#                 max_num = rank[idx[j]]
#                 pop_idx = j
#         for j in range(pop_idx):
#             idx.append(idx.popleft())
#         rank[idx[0]] = 0
#         turn += 1
#         if idx.popleft() == M:
#             print(turn)
#             break

############################################################

T = int(input())
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    rank = deque(list(map(int, sys.stdin.readline().split())))
    idx = deque(list(range(N)))
    idx[M] = 'target'
    order = 0

    while True:
        if rank[0] == max(rank):
            order += 1
            if idx[0] == 'target':
                print(order)
                break
            else:
                rank.popleft()
                idx.popleft()
        else:
            rank.append(rank.popleft())
            idx.append(idx.popleft())
