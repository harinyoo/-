def VPS(string):
    cnt = 0
    while len(string) > 0:
        c = string.pop()
        if c == ')':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    if cnt == 0:
        return True
    else:
        return False


T = int(input())
for i in range(T):
    PS = list(input())
    if VPS(PS):
        print('YES')
    else:
        print('NO')