cnt_list = [i for i in range(1000001)]

N = int(input())
for j in range(4, N+1):
    cnt_list[j] = (cnt_list[j-1] + cnt_list[j-2]) % 15746

print(cnt_list[N])
