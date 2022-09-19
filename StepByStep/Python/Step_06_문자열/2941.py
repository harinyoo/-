croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

words = input()

for i in croatian:
    words = words.replace(i, '*')

print(len(words))

