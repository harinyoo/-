from math import sqrt
k = 123456*2+1
prime = [True]*k
for i in range(1, k):
    if i == 1:
        continue
    for j in range(2, int(sqrt(i))+1):
        if i % j == 0:
            prime[i] = False
            break

T = int(input())
for test in range(T):
    num = int(input())
    for i in range(num//2, 1, -1):
        if prime[i] and prime[num-i]:
            print(i, num-i)
            break




######################################################
# from math import sqrt
# T = int(input())
# for test in range(T):
#     num = int(input())
#     for i in range(num//2, 1, -1):
#         prime = True
#         end = False
#         for j in range (2, int(sqrt(i))+1):
#             if i % j == 0:
#                 prime = False
#                 break
#         if prime:
#             prime_ = True
#             for k in range(2, int(sqrt(num-i))+1):
#                 if (num-i) % k == 0:
#                     prime_ = False
#                     break
#             if prime_:
#                 end = True
#                 print(i, num-i)
#                 break
#         if end:
#             break
