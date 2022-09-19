N = int(input())
sequence = list(map(int, input().split()))
dp = [0 for i in range(N)]

for i in range(N):
    for j in range(i):
        if sequence[i] > sequence[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))
