S = list(input())
N = 'abcdefghijklmnopqrstuvwxyz'
for i in N:
    if i in S:
        print(S.index(i), end=' ')
    else:
        print(-1, end=' ')