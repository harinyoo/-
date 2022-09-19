import sys

K = int(sys.stdin.readline())
horizontal, vertical, h_idx, v_idx = 1, 1, 0, 0
info = []
for i in range(6):
    direction, length = map(int, sys.stdin.readline().split())
    info.append([direction, length])
    if direction == 1 or direction == 2:
        if horizontal < length:
            horizontal = length
            h_idx = i
    elif direction == 3 or direction == 4:
        if vertical < length:
            vertical = length
            v_idx = i

if h_idx == 0:
    if v_idx == 1:
        print(K * (horizontal * vertical - info[3][1] * info[4][1]))
    else:
        print(K * (horizontal * vertical - info[2][1] * info[3][1]))

elif h_idx == 1:
    if v_idx == 2:
        print(K * (horizontal * vertical - info[4][1] * info[5][1]))
    else:
        print(K * (horizontal * vertical - info[3][1] * info[4][1]))

elif h_idx == 2:
    if v_idx == 3:
        print(K * (horizontal * vertical - info[0][1] * info[5][1]))
    else:
        print(K * (horizontal * vertical - info[4][1] * info[5][1]))

elif h_idx == 3:
    if v_idx == 4:
        print(K * (horizontal * vertical - info[0][1] * info[1][1]))
    else:
        print(K * (horizontal * vertical - info[0][1] * info[5][1]))

elif h_idx == 4:
    if v_idx == 5:
        print(K * (horizontal * vertical - info[1][1] * info[2][1]))
    else:
        print(K * (horizontal * vertical - info[0][1] * info[1][1]))

elif h_idx == 5:
    if v_idx == 0:
        print(K * (horizontal * vertical - info[2][1] * info[3][1]))
    else:
        print(K * (horizontal * vertical - info[1][1] * info[2][1]))



###################### 다른 방법 ######################
# import sys
#
# K = int(sys.stdin.readline())
# horizontal, vertical, h_idx, v_idx = 1, 1, 0, 0
# info = []
# for i in range(6):
#     direction, length = map(int, sys.stdin.readline().split())
#     info.append([direction, length])
#     if direction == 1 or direction == 2:
#         if horizontal < length:
#             horizontal = length
#             h_idx = i
#     elif direction == 3 or direction == 4:
#         if vertical < length:
#             vertical = length
#             v_idx = i
#
# print(K * (horizontal * vertical - abs(info[(v_idx+1)%6][1]-info[(v_idx-1)%6][1]) * abs(info[(h_idx+1)%6][1]-info[(h_idx-1)%6][1])))
