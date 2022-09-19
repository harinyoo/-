def Hanoi(start, temp, end, n):
    if n == 1:
        print(start, end)
    else:
        Hanoi(start, end, temp, n-1)
        print(start, end)
        Hanoi(temp, start, end, n-1)


N = int(input())
print(2**N-1)
Hanoi(1, 2, 3, N)