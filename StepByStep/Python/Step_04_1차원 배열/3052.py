nums = []
for i in range(10):
    nums.append(int(input()) % 42)

# remain = []
# for j in range(42):
#     remain.append(0)
#
# for k in nums:
#     remain[k] += 1
#
# cnt = 0
# for l in remain:
#     if l != 0:
#         cnt += 1
#
# print(cnt)

nums = set(nums)
print(len(nums))
