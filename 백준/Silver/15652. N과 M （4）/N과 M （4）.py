from itertools import combinations_with_replacement
n, m = map(int, input().split())
n_list = [i+1 for i in range(n)]
for combi in combinations_with_replacement(n_list, m):
    print(*combi)