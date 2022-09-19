import sys


def binarysearch(start, end, number):
    if start > end:
        return 0

    mid = (start + end) // 2
    if number == cards[mid]:
        left, right = 1, 1
        while start <= mid - left:
            if number != cards[mid - left]:
                break
            left += 1
        while mid + right <= end:
            if number != cards[mid + right]:
                break
            right += 1
        return left + right - 1
    elif number < cards[mid]:
        return binarysearch(start, mid - 1, number)
    else:
        return binarysearch(mid + 1, end, number)


N = int(sys.stdin.readline())
cards = sorted(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

cards_dic = {}
for card in cards:
    if card not in cards_dic:
        cards_dic[card] = binarysearch(0, N-1, card)

print(' '.join(str(cards_dic[i]) if i in cards_dic else '0' for i in nums))


