N = int(input())
num_list = list(map(int, input().split()))
arr = sorted(set(num_list))
dic = {arr[i]:i for i in range(len(arr))}
for i in num_list:
    print(dic[i], end=' ')