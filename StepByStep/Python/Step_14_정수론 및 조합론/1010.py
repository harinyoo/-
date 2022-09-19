import sys
from math import factorial

T = int(input())
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(factorial(M)//factorial(N)//factorial(M-N))
