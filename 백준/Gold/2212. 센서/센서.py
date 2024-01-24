N = int(input())
K = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

array = []
for i in range(0, N-1):
    array.append(n_list[i+1] - n_list[i])
array.sort()
print(sum(array[:N-K]))