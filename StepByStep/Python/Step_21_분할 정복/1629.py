A, B, C = map(int, input().split())


def DivideConquer(a, b):
    if b == 1:
        return a % C

    temp = DivideConquer(a, b//2)
    if b % 2 == 0:
        return temp * temp % C
    else:
        return temp * temp * a % C


print(DivideConquer(A, B))
