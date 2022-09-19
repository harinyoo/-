import sys


def binarysearch(start, end, number):
    if start > end:
        return 0

    mid = (start + end) // 2
    if cards[mid] == number:
        return 1
    elif cards[mid] > number:
        return binarysearch(start, mid-1, number)
    elif cards[mid] < number:
        return binarysearch(mid+1, end, number)


N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

for num in nums:
    print(binarysearch(0, N-1, num), end=' ')


