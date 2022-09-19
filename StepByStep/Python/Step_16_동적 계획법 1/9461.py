padovan = [1] * 101
for i in range(4, 101):
    padovan[i] = padovan[i-3] + padovan[i-2]

T = int(input())
for j in range(T):
    print(padovan[int(input())])
