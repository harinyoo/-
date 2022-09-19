import sys
import math

N = int(input())
nums = []
ans = []
for i in range(N):
    nums.append(int(sys.stdin.readline().strip()))

nums.sort()
for i in range(N-1):
    nums[i] = nums[i+1]-nums[i]
nums.sort()

gcdNum = nums[0]
for i in range(1, N-1):
    gcdNum = math.gcd(gcdNum, nums[i])

ans = []
for i in range(1, int(math.sqrt(gcdNum))+1):
    if gcdNum % i == 0:
        ans.append(i)
        ans.append(gcdNum//i)
ans = list(set(ans))
ans.sort()

for i in range(1, len(ans)):
    print(ans[i], end=' ')
