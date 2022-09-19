import sys


def binarysearch(word, start, end):
    global cnt
    if start > end:
        return

    mid = (start + end) // 2
    if arr[mid] == word:
        cnt += 1
    elif arr[mid] > word:
        return binarysearch(word, start, mid-1)
    else:
        return binarysearch(word, mid+1, end)


N, M = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline().strip() for _ in range(N))
arr.sort()
words = list(sys.stdin.readline().strip() for _ in range(M))

cnt = 0
for w in words:
    binarysearch(w, 0, N-1)

print(cnt)



########## 해시 사용 ##########
# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# cnt = 0
# S = dict()
#
# for i in range(n):
#     index = input().strip()
#     S[index] = True
#
# for j in range(m):
#     check = input().strip()
#     if check in S:
#         cnt += 1
# print(cnt)