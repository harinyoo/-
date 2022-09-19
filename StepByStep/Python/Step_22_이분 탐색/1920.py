def binarySearch(key, array, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if key == array[mid]:
        return mid
    elif key < array[mid]:
        return binarySearch(key, array, start, mid-1)
    else:
        return binarySearch(key, array, mid+1, end)


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
num = list(map(int, input().split()))

for i in num:
    if binarySearch(i, arr, 0, N-1) == -1:
        print(0)
    else:
        print(1)
