N = int(input())
nums = list(map(int, input().split()))
minNum = nums[0]
maxNum = nums[0]

for i in nums:
    if minNum > i:
        minNum = i
    if maxNum < i:
        maxNum = i

print(minNum, maxNum)