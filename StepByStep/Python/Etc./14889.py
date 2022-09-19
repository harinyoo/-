import sys

N = int(input())
people = [p for p in range(N)]
skill = []
for s in range(N):
    skill.append(list(map(int, sys.stdin.readline().split())))
start = []
minimum = 100 * N - 1 * N


def solve(idx):
    global minimum
    if len(start) == N // 2:
        link = []
        start_score = 0
        link_score = 0
        for x in people:
            if x not in start:
                link.append(x)
        for y in start:
            for z in start:
                start_score += skill[y][z]
        for y in link:
            for z in link:
                link_score += skill[y][z]
        minimum = min(minimum, abs(start_score-link_score))
        return

    for i in range(idx, N):
        start.append(i)
        solve(i + 1)
        start.pop()


solve(0)
print(minimum)
