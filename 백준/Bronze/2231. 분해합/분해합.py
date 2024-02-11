N = int(input())
correct = []
for i in range(N):
    sum_all = []
    for j in str(i):
        sum_all.append(int(j))
    if sum(sum_all) + i == N:
        correct.append(i)
if len(correct) == 0:
    print(0)
else:
    print(min(correct))
