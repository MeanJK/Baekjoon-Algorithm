import sys

N, M = map(int, sys.stdin.readline().split())
basket = [k for k in range(1,N+1)]
temp = 0
for r in range(M):
    i, j = map(int, sys.stdin.readline().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp
for l in range(N):
    print(basket[l], end=' ')