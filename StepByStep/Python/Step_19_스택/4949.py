def isBalanced(string):
    PS = []
    for i in string:
        if i == '(' or i == '[':
            PS.append(i)
        elif i == ')':
            if not PS or PS[-1] == '[':
                return False
            elif PS[-1] == '(':
                PS.pop()
        elif i == ']':
            if not PS or PS[-1] == '(':
                return False
            elif PS[-1] == '[':
                PS.pop()
    if not PS:
        return True
    else:
        return False


while True:
    sentence = input()
    if sentence == '.':
        break
    if isBalanced(list(sentence)):
        print('yes')
    else:
        print('no')
