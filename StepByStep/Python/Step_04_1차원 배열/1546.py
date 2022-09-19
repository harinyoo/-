N = int(input())
scores = list(map(int, input().split()))

maxNum = max(scores)
for j in range(N):
    scores[j] = scores[j] / maxNum * 100

print(sum(scores)/N)