import sys

N = int(sys.stdin.readline())
xNum = list(map(int, sys.stdin.readline().split()))

xNum_ = list(set(xNum))
xNum_.sort()
dic = {xNum_[i]: i for i in range(len(xNum_))}

for x in xNum:
    print(dic[x], end=' ')
