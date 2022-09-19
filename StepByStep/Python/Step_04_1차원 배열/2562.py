nums = []
for i in range(9):
    nums.append(int(input()))

maxNum = nums[0]
idx = 0

for j in range(9):
    if maxNum < nums[j]:
        maxNum = nums[j]
        idx = j

print(maxNum)
print(idx+1)

# print(max(nums))
# print(nums.index(max(nums))+1)
