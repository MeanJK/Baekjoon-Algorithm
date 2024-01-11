N = int(input())
At = Bt = 100
for i in range(N):
    A, B = map(int, input().split())
    if A > B:
        Bt -= A
    elif A < B:
        At -= B
print(At, Bt, sep="\n")