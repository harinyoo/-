N = int(input())
num = N
cycle = 0

while True:
    sum = (num//10) + (num%10)
    num = (num%10)*10 + (sum%10)
    cycle = cycle + 1
    if num == N:
        break

print(cycle)