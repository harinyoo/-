N = int(input())
nums = [[0] * 2 for _ in range(N)]
for i in range(N):
    nums[i][0], nums[i][1] = map(int, input().split())

nums = sorted(nums)
dp = [0 for _ in range(N)]
for j in range(N):
    for k in range(j):
        if nums[j][1] > nums[k][1] and dp[j] < dp[k]:
            dp[j] = dp[k]
    dp[j] += 1

print(N - max(dp))
