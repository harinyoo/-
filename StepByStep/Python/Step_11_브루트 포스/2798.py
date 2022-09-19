N, M = map(int, input().split())
cards = list(map(int, input().split()))
sum = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if sum <= cards[i]+cards[j]+cards[k] <= M:
                sum = cards[i]+cards[j]+cards[k]

print(sum)