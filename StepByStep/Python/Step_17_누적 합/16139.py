import sys


def func(string):
    for alphabet in "abcdefghijklmnopqrstuvwxyz":
        cnt = 0
        tmp = []
        for s in string:
            if s == alphabet:
                cnt += 1
            tmp.append(cnt)
        arr.append(tmp)


def main(num):
    for x in range(num):
        inp = sys.stdin.readline().split()
        item, l, r = inp[0], int(inp[1]), int(inp[2])
        if l == 0:
            print(arr[ord(item) - 97][r])
        else:
            print(arr[ord(item) - 97][r] - arr[ord(item) - 97][l - 1])


S = sys.stdin.readline().strip()
arr = []
func(S)

q = int(sys.stdin.readline())
main(q)
