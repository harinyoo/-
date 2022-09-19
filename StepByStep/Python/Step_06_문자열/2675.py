T = int(input())

# for i in range(T):
#     cnt_str = input()
#     for j in range(len(cnt_str)-2):
#         for k in range(int(cnt_str[0])):
#             print(cnt_str[j+2], end='')
#     print()

for i in range(T):
    cnt, str = input().split()
    for j in str:
        print(j * int(cnt), end='')
    print()