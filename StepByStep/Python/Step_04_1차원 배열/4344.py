C = int(input())
for i in range(C):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:]) / nums[0]
    cnt = 0
    for score in nums[1:]:
        if avg < score:
            cnt += 1
    print(str("{:.3f}".format(cnt/nums[0]*100)) + '%')