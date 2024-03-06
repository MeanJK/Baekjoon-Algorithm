n, m = map(int, input().split())
poketmon_list = []
for _ in range(n):
    poketmon_list.append(input())
check_list = []
for _ in range(m):
    check_list.append(input())
poketmon_dict = {poketmon_list[i-1] : i for i in range(1, n+1)}
reverse_poketmon_dict = {v:k for k,v in poketmon_dict.items()}
for check in check_list:
    if check.isalpha() == True:
        print(poketmon_dict.get(check))
    else:
        print(reverse_poketmon_dict.get(int(check)))