A = int(input())
B = int(input())
C = int(input())
# result = str(A*B*C)
#
# nums = []
# for i in range(10):
#     nums.append(0)
#
# for j in range(len(result)):
#     nums[int(result[j])] += 1
#
# for k in nums:
#     print(k)

result = list(str(A*B*C))
for i in range(10):
    print(result.count(str(i)))
