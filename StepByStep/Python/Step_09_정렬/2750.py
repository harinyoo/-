N = int(input())
nums = []
for n in range(N):
    nums.append(int(input()))

for i in range(N-1):
    for j in range(N-(i+1)):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

#nums.sort()

for k in nums:
    print(k)
