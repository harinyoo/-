def han(n):
    if n < 100:
        return n
    else:
        cnt = 99
        for i in range(100, n+1):
            num = str(i)
            if int(num[0]) - int(num[1]) == int(num[1]) - int(num[2]):
                cnt += 1
        return cnt



N = int(input())
print(han(N))