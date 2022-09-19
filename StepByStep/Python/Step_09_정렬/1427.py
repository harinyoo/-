N = input()
numList = [int(n) for n in N]

numList.sort(reverse=True)
for i in numList:
    print(i, end='')
