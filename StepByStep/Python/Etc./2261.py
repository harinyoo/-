n = int(input())
dot = []
for i in range(n):
    x, y = map(int, input().split())
    dot.append((x, y))

length = 800000000
for i in range(n-1):
    for j in range(i+1, n):
        tmp = (dot[i][0]-dot[j][0])**2 + (dot[i][1]-dot[j][1])**2
        length = min(length, tmp)

print(length)