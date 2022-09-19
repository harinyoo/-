import sys

n = int(input())
sequence = []
stack = [0]
operator = []
for i in range(n):
    sequence.append(int(sys.stdin.readline()))

top = 1
isPossible = True
for i in sequence:
    while True:
        if stack[-1] == i:
            stack.pop()
            operator.append('-')
            break
        elif stack[-1] > i:
            isPossible = False
            break
        stack.append(top)
        operator.append('+')
        top += 1

if isPossible:
    for i in operator:
        print(i)
else:
    print('NO')
