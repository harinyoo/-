from sys import stdin


def AC(function, num, arr):
    function.replace('RR', '')
    left, right, direction = 0, 0, True
    for j in function:
        if j == 'R':
            direction = not direction
        elif j == 'D':
            if direction:
                left += 1
            else:
                right += 1
    if left + right <= num:
        ans = arr[left:num - right]
        if direction:
            print('[' + ','.join(ans) + ']')
        else:
            print('[' + ','.join(ans[::-1]) + ']')
    else:
        print('error')


T = int(stdin.readline())
for i in range(T):
    p = input()
    n = int(input())
    string = input()[1:-1].split(',')
    AC(p, n, string)
