import sys

N = int(input())
wine = [0] * 10000
dp = [0] * 10000
for i in range(N):
    wine[i] = int(sys.stdin.readline())

dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
dp[2] = max(wine[0] + wine[1], wine[0] + wine[2], wine[1] + wine[2])
for i in range(3, N):
    dp[i] = max(dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i], dp[i-1])

print(dp[N-1])
