import math
M, N = map(int, input().split())
for num in range(M, N+1):
    if num == 2:
        print(num)
    elif num > 2:
        prime = True
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                prime = False
                break
        if prime:
            print(num)
