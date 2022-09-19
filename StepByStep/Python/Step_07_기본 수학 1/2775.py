T = int(input())

for test in range(T):
    k = int(input())
    n = int(input())
    people = [i for i in range(n+1)]
    for floor in range(1, k+1):
        for num in range(1, n+1):
            people[num] += people[num-1]
    print(people[n])
