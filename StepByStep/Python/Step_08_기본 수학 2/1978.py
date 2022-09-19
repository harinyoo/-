import math
N = int(input())
nums = map(int, input().split())
cnt = 0
for num in nums:
    if num == 2:
        cnt += 1
    elif num > 2:
        prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            cnt += 1
print(cnt)