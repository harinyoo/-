import sys
from collections import deque

queue = deque([])
length = len(queue)


def push(n):
    queue.append(n)


def pop():
    if not queue:
        print(-1)
    else:
        print(queue.popleft())


def size():
    print(len(queue))


def empty():
    if not queue:
        print(1)
    else:
        print(0)


def front():
    if not queue:
        print(-1)
    else:
        print(queue[0])


def back():
    if not queue:
        print(-1)
    else:
        print(queue[-1])


N = int(sys.stdin.readline())

for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'pop':
        pop()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'front':
        front()
    elif command[0] == 'back':
        back()
