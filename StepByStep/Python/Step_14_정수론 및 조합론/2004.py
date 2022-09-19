import sys


def two_cnt(num):
    cnt = 0
    while num >= 2:
        cnt += num//2
        num //= 2
    return cnt


def five_cnt(num):
    cnt = 0
    while num >= 5:
        cnt += num//5
        num //= 5
    return cnt


n, m = map(int, sys.stdin.readline().split())
two = two_cnt(n)-two_cnt(m)-two_cnt(n-m)
five = five_cnt(n)-five_cnt(m)-five_cnt(n-m)
print(min(two, five))
