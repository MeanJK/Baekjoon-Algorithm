N = int(input())
M = int(input())


def isPrime(X):
    if X < 2:
        return False
    for i in range(2, int(X**0.5) + 1):
        if X % i == 0:
            return False
    return True


S_list = []
for i in range(N, M + 1):
    if isPrime(i) == True:
        S_list.append(i)
if len(S_list) == 0:
    print(-1)
else:
    print(sum(S_list), min(S_list))