N, K = map(int, input().split())
coin = []
for i in range(N):
    coin.append(int(input()))

cnt = 0
for i in range(N-1, -1, -1):
    if K == 0:
        break
    if coin[i] <= K:
        cnt += K // coin[i]
        K = K % coin[i]

print(cnt)
