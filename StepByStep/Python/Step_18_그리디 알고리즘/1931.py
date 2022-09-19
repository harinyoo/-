N = int(input())
timetable = [[0] * 2 for _ in range(N)]
for i in range(N):
    timetable[i][0], timetable[i][1] = map(int, input().split())

timetable.sort(key=lambda x: (x[1], x[0]))
fin = 0
max_cnt = 0
for i, j in timetable:
    if i >= fin:
        max_cnt += 1
        fin = j

print(max_cnt)
