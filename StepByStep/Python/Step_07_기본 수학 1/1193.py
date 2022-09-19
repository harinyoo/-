X = int(input())  #4
sum = 2
num = 1
while X > num:
    num += sum
    sum += 1

if sum % 2 == 0:
    print(str(1+num-X) + '/' + str(sum-1-num+X))
else:
    print(str(sum-1-num+X) + '/' + str(1+num-X))