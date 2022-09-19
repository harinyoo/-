import sys


def binary(start, end, num):
    if start > end:
        return start

    mid = (start + end) // 2
    if li[mid] == num:
        return mid
    elif li[mid] < num:
        return binary(mid + 1, end, num)
    else:
        return binary(start, mid - 1, num)


n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
li = [seq[0]]
for item in seq:
    if li[-1] < item:
        li.append(item)
    else:
        li[binary(0, len(li)-1, item)] = item

print(len(li))