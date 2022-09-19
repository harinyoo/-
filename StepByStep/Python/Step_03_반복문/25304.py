import sys

total_price = int(sys.stdin.readline())
stuff = int(sys.stdin.readline())

cal_price = 0
for i in range(stuff):
    a, b = map(int, sys.stdin.readline().split())
    cal_price += a*b

print('Yes' if total_price == cal_price else 'No')
