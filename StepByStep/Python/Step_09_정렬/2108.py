from collections import Counter
import sys

N = int(sys.stdin.readline())
nums = []
for n in range(N):
    nums.append(int(sys.stdin.readline()))

mean = round(sum(nums) / N)

mid = sorted(nums)[N // 2]


min_num = abs(min(nums))
for i in range(N):
    nums[i] += min_num

cnt_list = [0] * (max(nums)+1)
for j in nums:
    cnt_list[j] += 1

most = 0
if cnt_list.count(max(cnt_list)) > 1:
    cnt = 0
    idx = 0
    for k in range(max(nums)+1):
        if cnt_list[k] == max(cnt_list):
            cnt += 1
        if cnt == 2:
            idx = k
            break
    most = idx-min_num
else:
    most = cnt_list.index(max(cnt_list))-min_num

#####################최빈값 함수 사용#######################
# def modefinders(numlist):
#     c = Counter(numlist)
#     order = c.most_common()
#     maximum = order[0][1]
#
#     modes = []
#     for num in order:
#         if num[1] == maximum:
#             modes.append(num[0])
#
#     return modes
#
#
# modesList = modefinders(nums)
# if len(modesList) > 1:
#     modesList.sort()
#     mode = modesList[1]
# else:
#     mode = modesList[0]
#####################최빈값 함수 사용#######################

nums_range = max(nums) - min(nums)

print(mean)
print(mid)
print(mode)
print(nums_range)
