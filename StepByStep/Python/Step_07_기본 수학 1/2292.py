N = int(input())
if N == 1:
    print(1)
else:
    idx = [0]
    i = 1
    while True:
        idx.append(idx[i-1]+i)
        if N < 6*idx[i]+2:
            break
        else:
            i += 1
    print(i+1)

# rooms = 1
# cnt = 1
# while N > rooms:
#     rooms += 6*cnt
#     cnt += 1
# print(cnt)