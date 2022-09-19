def gcd(n, m):
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            return i


N = int(input())
radius = list(map(int, input().split()))

for j in range(1, N):
    gcdNum = gcd(radius[0], radius[j])
    A = radius[0] // gcdNum
    B = radius[j] // gcdNum
    print(str(A) + '/' + str(B))
