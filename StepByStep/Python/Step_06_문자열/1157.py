words = input().upper()
unique_words = list(set(words))

cnt_list = []
for i in unique_words:
    cnt_list.append(words.count(i))

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    print(unique_words[cnt_list.index(max(cnt_list))])

