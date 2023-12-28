import sys

N, X = map(int, sys.stdin.readline().split())
a_list = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    if a_list[i] < X:
        print(a_list[i])
    
 