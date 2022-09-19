from math import factorial

N = int(input())
N_str = str(factorial(N))
length = len(N_str)

cnt = 0
for i in range(length-1, -1, -1):
    if N_str[i] == '0':
        cnt += 1
    else:
        break
print(cnt)
