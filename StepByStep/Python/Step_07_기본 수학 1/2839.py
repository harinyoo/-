# N = int(input())
# x = 0
# while 3*x-N <= 0:
#     x += 1
#
# sum = 1667
# x_ = 0
# for i in range(x):
#     if (N-3*i) % 5 == 0:
#         if i+((N-3*i)/5) <= sum:
#             sum = i+(N-3*i)/5
#             x_ = i
# if 3*x_ + 5*(sum-x_) != N:
#     print(-1)
# else:
#     print(int(sum))

sugar = int(input())
bag = 0
while sugar >= 0:
    if sugar % 5 == 0:
        bag += sugar//5
        print(bag)
        break
    sugar -= 3
    bag += 1

else:
    print(-1)