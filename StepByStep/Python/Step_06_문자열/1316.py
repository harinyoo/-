N = int(input())
cnt = N
for i in range(N):
    flag = True
    word = input()
    unique_word = list(set(word))
    for j in unique_word:
        idx = word.index(j)
        for k in range(idx+1, len(word)):
            if j == word[k]:
                if k-idx == 1:
                    idx = k
                else:
                    cnt -= 1
                    flag = False
                    break
        if flag == False:
            break
print(cnt)

# for i in range(N):
#     word = input()
#     for index in range(len(word)-1):
#         if word[index] != word[index+1]:
#             sub_word = word[index+1:]
#             if sub_word.count(word[index]) > 0:
#                 cnt -= 1
#                 break
# print(cnt)
