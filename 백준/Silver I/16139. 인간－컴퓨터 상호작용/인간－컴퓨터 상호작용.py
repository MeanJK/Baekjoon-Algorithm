import sys
input = sys.stdin.readline
S = input()
N = int(input())
question = [list(map(str, input().split())) for i in range(N)]

for q in question:
    result = 0
    for i in range(int(q[1]),int(q[2])+1):
        if S[i] == q[0]:
            result += 1
    print(result)