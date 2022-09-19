def binarySearch(start, end):
    if start > end:
        return end

    mid = (start + end) // 2
    cnt = 0
    for i in length:
        cnt += i // mid

    if cnt >= N:
        return binarySearch(mid + 1, end)
    else:
        return binarySearch(start, mid - 1)


K, N = map(int, input().split())
length = [int(input()) for _ in range(K)]
print(binarySearch(1, max(length)))
