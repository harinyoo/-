###시간초과###
# from math import sqrt
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     cnt = 0
#     for num in range(n, 2*n+1):
#         if num == 1:
#             continue
#         elif num == 2:
#             cnt += 1
#             continue
#         else:
#             for i in range(2, int(sqrt(num))+1):
#                 if num % i == 0:
#                     break
#             else:
#                 cnt += 1
#     print(cnt)

from math import sqrt
k = 123456*2+1
prime = [1]*k
for i in range(1, k):
    if i == 1:
        continue
    for j in range(2, int(sqrt(i))+1):
        if i % j == 0:
            prime[i] = 0
            break

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for k in range(n+1, 2*n+1):
        cnt += prime[k]
    print(cnt)