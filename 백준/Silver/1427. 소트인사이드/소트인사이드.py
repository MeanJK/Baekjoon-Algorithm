N = int(input())
N = str(N)
num_list = []
for char in N:
    num_list.append(int(char))
num_list.sort(reverse=True)
print(''.join(map(str, num_list)))