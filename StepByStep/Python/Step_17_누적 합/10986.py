import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

mods = [0 for _ in range(M)]
tmp = 0

for num in nums:
    tmp += num            #부분합
    mods[tmp % M] += 1

ans = 0
for mod in mods:
    ans += mod*(mod-1)//2    #nC2
ans += mods[0]               #나머지가 0이면 n 중에 2개 선택 안 해도 됨

print(ans)