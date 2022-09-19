def DivideConquer(a, b):
    if b == 1:
        return a % p

    temp = DivideConquer(a, b // 2)
    if b % 2:
        return temp * temp * a % p
    else:
        return temp * temp % p


N, K = map(int, input().split())
p = 1000000007

factorial = [1 for _ in range(N + 1)]
for i in range(2, N + 1):
    factorial[i] = i * factorial[i-1] % p

A = factorial[N]
B = factorial[N - K] * factorial[K]
print((A % p) * (DivideConquer(B, p-2) % p) % p)
