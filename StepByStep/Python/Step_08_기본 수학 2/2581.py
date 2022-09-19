import math
M = int(input())
N = int(input())
min = N
sum = 0
for num in range(M, N+1):
    if num > 1:
        prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            sum += num
            if min > num:
                min = num
if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)