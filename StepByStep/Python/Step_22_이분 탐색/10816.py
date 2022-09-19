from sys import stdin


def binarySearch(key, arr, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if key == arr[mid]:
        left, right = 1, 1
        while mid - left >= start:
            if arr[mid-left] != arr[mid]:
                break
            else:
                left += 1
        while mid + right <= end:
            if arr[mid+right] != arr[mid]:
                break
            else:
                right += 1
        return left + right - 1
    elif key < arr[mid]:
        return binarySearch(key, arr, start, mid - 1)
    else:
        return binarySearch(key, arr, mid + 1, end)


N = int(stdin.readline())
card = sorted(map(int, stdin.readline().split()))
M = int(stdin.readline())
num = map(int, stdin.readline().split())

card_dic = {}
for i in card:
    if i not in card_dic:
        card_dic[i] = binarySearch(i, card, 0, N-1)

print(' '.join(str(card_dic[x]) if x in card_dic else '0' for x in num))