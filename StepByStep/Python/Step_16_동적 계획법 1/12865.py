N, K = map(int, input().split())
weight = [0] * (N+1)
value = [0] * (N+1)
for i in range(1, N+1):
    weight[i], value[i] = map(int, input().split())

dp = [[0] * (K+1) for _ in range(N+1)]
for j in range(1, K+1):
    for i in range(1, N+1):
        if weight[i] > j:
            dp[i][j] = dp[i-1][j]
            continue
        dp[i][j] = max(dp[i-1][j], value[i]+dp[i-1][j-weight[i]])

print(dp[N][K])