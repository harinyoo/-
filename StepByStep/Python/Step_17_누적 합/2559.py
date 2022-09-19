N, K = map(int, input().split())
temp = list(map(int, input().split()))

arr = [sum(temp[:K])]

for i in range(1, N-K+1):
    arr.append(arr[i-1] - temp[i-1] + temp[i-1+K])

print(max(arr))
