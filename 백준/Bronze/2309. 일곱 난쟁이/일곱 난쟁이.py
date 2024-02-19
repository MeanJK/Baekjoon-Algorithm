from itertools import combinations
tall = []
for i in range(9):
    tall.append(int(input()))
for member in combinations(tall, 7):
    member = list(member)
    if sum(member) == 100:
        member.sort()
        for n in member:
            print(n)
        break