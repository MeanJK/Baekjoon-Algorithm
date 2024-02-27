from itertools import combinations
result = []
while True:
    k, *s_list = map(int, input().split())
    answer_list = []
    if k == 0:
        break
    else:
        for combi in combinations(s_list, 6):
            answer_list.append(combi)
        result.append(answer_list)
for i in range(len(result)):
    if i != len(result)-1:
        for answer in result[i]:
            print(*answer)
        print()
    else:
        for answer in result[i]:
            print(*answer)