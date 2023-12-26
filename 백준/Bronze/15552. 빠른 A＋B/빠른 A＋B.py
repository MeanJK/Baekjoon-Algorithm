import sys

N = int(input())
for i in range(N):
    Anum, Bnum = map(int, sys.stdin.readline().split())
    print(Anum + Bnum)
    