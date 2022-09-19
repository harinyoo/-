N = int(input())
seq = list(map(int, input().split()))
dp = [0] * N

sub_sum = 0
max_sum = -1000
for i in range(N):
    sub_sum = max(seq[i], seq[i]+sub_sum)
    max_sum = max(sub_sum, max_sum)

print(max_sum)
