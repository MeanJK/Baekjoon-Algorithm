from itertools import combinations
n, s = map(int, input().split())
s_list = list(map(int, input().split()))
count = 0
for i in range(1, n+1):
    for comb in combinations(s_list, i):
        if sum(list(comb)) == s:
            count += 1
print(count)
    