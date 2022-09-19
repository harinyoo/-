from collections import deque

N = int(input())
card = deque([i for i in range(1, N+1)])

while 1 < len(card):
    card.popleft()
    card.append(card.popleft())

print(card[0])
