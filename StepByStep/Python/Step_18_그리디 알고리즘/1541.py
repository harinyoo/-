exp = input().split('-')
nums = []

for i in range(len(exp)):
    sub_sum = 0
    s = exp[i].split('+')
    for j in s:
        sub_sum += int(j)
    nums.append(sub_sum)

ans = nums[0]
for i in range(1, len(nums)):
    ans -= nums[i]

print(ans)