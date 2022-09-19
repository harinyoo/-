str01 = input()
str02 = input()
len01 = len(str01)
len02 = len(str02)
dp = [[0] * (len01+1) for _ in range(len02+1)]

for i in range(len01):
    for j in range(len02):
        if str01[i] == str02[j]:
            dp[j+1][i+1] = dp[j][i] + 1
        else:
            dp[j+1][i+1] = max(dp[j][i+1], dp[j+1][i])

print(dp[len02][len01])
