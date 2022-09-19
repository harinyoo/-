N = int(input())
prime = 2
while N != 1:
    if N % prime == 0:
        N //= prime
        print(prime)
    else:
        prime += 1