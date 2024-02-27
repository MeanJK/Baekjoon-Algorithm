n, m = map(int, input().split())
n_list = [i+1 for i in range(n)]
def combinations(arr, r):
    for i in range(n):
        if r == 1:
            yield [arr[i]]
        else:
             for comb in combinations(arr, r-1):
                    yield[arr[i]] + comb
for combi in combinations(n_list, m):                 
    print(*combi)