import sys

N = int(input())
nums = []
for n in range(N):
    nums.append(list(map(int, sys.stdin.readline().split())))

nums = sorted(nums, key=lambda k: (k[1], k[0]))
for num in nums:
    print(num[0], num[1])
