N = int(input())
num_list =  []
for _ in range(N):
    num_list.append(list(map(int, input().split())))
num_list.sort(key = lambda x : (x[1], x[0]))
for num in num_list:
    print(*num)