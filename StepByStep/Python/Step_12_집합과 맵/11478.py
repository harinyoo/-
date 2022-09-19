import sys


S = sys.stdin.readline().strip()
arr = []
for i in range(1, len(S)+1):
    for j in range(len(S)-i+1):
        arr.append(S[j:j+i])

print(len(set(arr)))
