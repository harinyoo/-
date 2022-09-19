S = input()

# alphabet = []
# for i in range(26):
#     alphabet.append(-1)
#
# for j in range(len(S)):
#     for k in range(26):
#         if S[j] == chr(97+k) and alphabet[k] == -1:
#             alphabet[k] = j
#
# for l in alphabet:
#     print(l, end=' ')

alphabet = list(range(97, 123))
for i in alphabet:
    print(S.find(chr(i)), end=' ')