T = input()
count = 10
for i in range(1, len(T)):
    if T[i] == T[i-1]:
        count += 5
    else:
        count += 10
print(count)