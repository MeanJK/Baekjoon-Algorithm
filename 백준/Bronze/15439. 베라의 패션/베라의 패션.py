N = int(input())
T = [i for i in range(N)]
J = [i for i in range(N)]
count = 0
for i in range(N):
    for j in range(N):
        if T[i] != J[j]:
            count += 1
print(count)