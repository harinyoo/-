N = int(input())
weight_list = []
height_list = []
for i in range(N):
    weight, height = map(int, input().split())
    weight_list.append(weight)
    height_list.append(height)

rank_list = [1]*N
for i in range(N):
    for j in range(N):
        if weight_list[i] < weight_list[j] and height_list[i] < height_list[j]:
            rank_list[i] += 1

for k in rank_list:
    print(k, end=' ')