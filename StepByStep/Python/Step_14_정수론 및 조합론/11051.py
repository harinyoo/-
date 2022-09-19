from math import factorial
N, K = map(int, input().split())
ans = factorial(N)//factorial(K)//factorial(N-K)
ans %= 10007
print(ans)
