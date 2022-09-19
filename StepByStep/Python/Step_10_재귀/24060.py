import sys


def merge_sort(arr, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)
    return


def merge(arr, p, q, r):
    global cnt
    i, j = p, q+1
    tmp = []
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    while i <= q:
        tmp.append(arr[i])
        i += 1
    while j <= r:
        tmp.append(arr[j])
        j += 1

    i, t = p, 0
    while i <= r:
        arr[i] = tmp[t]
        cnt += 1
        if cnt == K:
            print(arr[i])
            return
        i += 1
        t += 1
    return


N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
cnt = 0
merge_sort(A, 0, N-1)
if cnt < K:
    print(-1)