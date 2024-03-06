n = input()
list = []
j=0
while len(n) >= j:
    for i in range(len(n)-j):
        if j == 0:
            list.append(n[i])
        else:
            list.append(n[i:i+j+1])
    j+=1
print(len(set(list)))