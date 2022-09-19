import sys

student, win = map(int, sys.stdin.readline().split())
score = list(map(int, sys.stdin.readline().split()))
score.sort(reverse=True)

print(score[win-1])


