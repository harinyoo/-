def binarySearch(start, end):
    if start > end:
        return end
    mid = (start + end) // 2
    current = house[0]
    count = 1

    for i in range(1, N):
        if current + mid <= house[i]:
            count += 1
            current = house[i]

    if count >= C:
        return binarySearch(mid + 1, end)
    else:
        return binarySearch(start, mid - 1)


N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house = sorted(house)
print(binarySearch(1, house[-1] - house[0]))
