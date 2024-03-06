n = int(input())
num_list = list(map(int, input().split()))
m = int(input())
check_list = list(map(int, input().split()))
num_dict = {}
for i in range(len(num_list)):
    if num_list[i] in num_dict:
        num_dict[num_list[i]] += 1
    else:
        num_dict[num_list[i]] = 1
for k in check_list:
    print(num_dict.get(k, 0), end = ' ')
  