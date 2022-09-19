import sys

# T = int(input())
# for i in range(T):
#     n = int(input())
#     name = ['-'] * n
#     category = ['-'] * n
#     for j in range(n):
#         name[j], category[j] = sys.stdin.readline().split()
#     category_set = list(set(category))
#     cnt_list = [0] * len(category_set)
#     for k in range(len(category_set)):
#         for l in category:
#             if category_set[k] == l:
#                 cnt_list[k] += 1
#     ans = 1
#     for k in cnt_list:
#         ans *= k+1
#     print(ans-1)

T = int(input())
for i in range(T):
    n = int(input())
    if n == 0:
        print(0)
        continue

    wearable = dict()
    for j in range(n):
        name, category = sys.stdin.readline().split()

        if category in wearable.keys():
            wearable[category] += 1
        else:
            wearable[category] = 1

    ans = 1
    for key in wearable.keys():
        ans *= wearable[key]+1
    print(ans-1)


