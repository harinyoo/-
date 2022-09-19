dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

words = input()
sec = 0
for i in words:
    for j in range(8):
        if dial[j].find(i) >= 0:
            sec += j+3

print(sec)



