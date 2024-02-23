from itertools import permutations
n, m = map(int, input().split())
num_list = [i for i in range(1, n+1)]
for per in permutations(num_list, m):
    print(*per)