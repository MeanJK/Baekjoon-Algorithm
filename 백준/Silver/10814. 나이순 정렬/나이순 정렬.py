N = int(input())
char_list = []
for _ in range(N):
    char_list.append(list(map(str, input().split())))
char_list.sort(key = lambda x : int(x[0]))
for char in char_list:
    print(*char)