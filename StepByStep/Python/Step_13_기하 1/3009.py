x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

x = 0
y = 0
if x1 == x2:
    x = x3
elif x1 == x3:
    x = x2
else:
    x = x1

if y1 == y2:
    y = y3
elif y1 == y3:
    y = y2
else:
    y = y1

print(x, y)

######################################################

# x_list = []
# y_list = []
# x = 0
# y = 0
# for i in range(3):
#     x_, y_ = map(int, input().split())
#     x_list.append(x_)
#     y_list.append(y_)
# for i in range(3):
#     if x_list.count(x_list[i]) == 1:
#         x = x_list[i]
#     if y_list.count(y_list[i]) == 1:
#         y = y_list[i]
# print(x, y)