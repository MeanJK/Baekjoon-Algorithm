N = int(input())
char_list = []
for _ in range(N):
    char_list.append(input())
char_list = list(set(char_list))    
char_list.sort(key = lambda x : (len(x), x))  
for char in char_list:
    print(char)