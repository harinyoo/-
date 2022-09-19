N = int(input())

for i in range(N):
    answers = list(input())
    O_cnt = 0
    score = 0
    for j in answers:
        if j == 'O':
            O_cnt += 1
            score += O_cnt
        else:
            O_cnt = 0
    print(score)