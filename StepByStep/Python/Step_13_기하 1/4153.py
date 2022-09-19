def triangle(x, y, z):
    if x == max(x, y, z):
        if x ** 2 == y ** 2 + z ** 2:
            print("right")
        else:
            print("wrong")
    elif y == max(x, y, z):
        if y ** 2 == x ** 2 + z ** 2:
            print("right")
        else:
            print("wrong")
    else:
        if z ** 2 == x ** 2 + y ** 2:
            print("right")
        else:
            print("wrong")


while True:
    l1, l2, l3 = map(int, input().split())
    if l1 == 0 and l2 == 0 and l3 == 0:
        break
    triangle(l1, l2, l3)

######################################################

# while True:
#     length = list(map(int, input().split()))
#     max_l = max(length)
#     if sum(length) == 0:
#         break
#     length.remove(max_l)
#     if length[0]**2 + length[1]**2 == max_l**2:
#         print("right")
#     else:
#         print("wrong")