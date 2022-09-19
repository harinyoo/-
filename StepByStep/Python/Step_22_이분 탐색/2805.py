def binarySearch(start, end):
    if start > end:
        return end

    mid = (start + end) // 2
    trees = 0
    for i in length:
        if i > mid:
            trees += i - mid

    if trees >= M:
        return binarySearch(mid + 1, end)
    else:
        return binarySearch(start, mid - 1)


N, M = map(int, input().split())
length = list(map(int, input().split()))
print(binarySearch(0, max(length)))
