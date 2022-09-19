import sys

N = int(input())
nums = []
for n in range(N):
    nums.append(int(sys.stdin.readline()))

for i in sorted(nums):
    sys.stdout.write(str(i)+'\n')
