# def d(n):
#     sum = n
#     for num in list(str(n)):
#         sum += int(num)
#     return sum
#
# nums = []
# for i in range(1, 10001):
#     nums.append(d(i))
#
# for j in range(1, 10001):
#     if j in nums:
#         pass
#     else:
#         print(j)

def d(n):
    nums = str(n)
    sum = n
    for num in nums:
        sum += int(num)
    return sum

selfNum = []
for i in range(10036):
    selfNum.append(True)

for j in range(1, 10001):
    selfNum[d(j)] = False

for k in range(1, 10001):
    if selfNum[k]:
        print(k)