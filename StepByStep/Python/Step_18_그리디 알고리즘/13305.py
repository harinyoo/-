N = int(input())
dis = list(map(int, input().split()))
oil = list(map(int, input().split()))\

price = 0
liter = oil[0]
for i in range(len(dis)):
    price += liter * dis[i]
    if liter > oil[i+1]:
        liter = oil[i+1]

print(price)
