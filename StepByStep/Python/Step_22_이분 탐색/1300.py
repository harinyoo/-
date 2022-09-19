def binarySearch(start, end):
    if start > end:
        return start

    mid = (start + end) // 2
    cnt = 0
    for i in range(1, N+1):
        cnt += min(mid//i, N)

    if cnt >= k:
        return binarySearch(start, mid - 1)
    else:
        return binarySearch(mid + 1, end)


N = int(input())
k = int(input())
print(binarySearch(1, N**2))

