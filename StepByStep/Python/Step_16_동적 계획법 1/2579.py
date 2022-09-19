import sys
N = int(input())
score = [0] * 301
dp_score = [0] * 301

for s in range(N):
    score[s] = int(sys.stdin.readline())

dp_score[0] = score[0]
dp_score[1] = score[0]+score[1]
dp_score[2] = max(score[0]+score[2], score[1]+score[2])

for i in range(3, N):
    dp_score[i] = max(dp_score[i-3]+score[i-1]+score[i], dp_score[i-2]+score[i])

print(dp_score[N-1])

