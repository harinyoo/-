import sys

N = int(input())
seq = list(map(int, sys.stdin.readline().split()))
dp_asc = [0 for _ in range(N)]
dp_des = [0 for _ in range(N)]

for i in range(N):
    for j in range(i+1):
        if seq[i] > seq[j] and dp_asc[i] < dp_asc[j]:
            dp_asc[i] = dp_asc[j]
    dp_asc[i] += 1

for k in range(N-1, -1, -1):
    for l in range(N-1, k-1, -1):
        if seq[k] > seq[l] and dp_des[k] < dp_des[l]:
            dp_des[k] = dp_des[l]
    dp_des[k] += 1

for m in range(N):
    dp_asc[m] += dp_des[m]

print(max(dp_asc)-1)
