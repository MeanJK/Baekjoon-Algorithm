import sys
input = sys.stdin.readline
N = int(input())
time = sorted([tuple(map(int, input().split())) for _ in range(N)], key = lambda x : (x[1], x[0]))

answer = end = 0
for s, e in time:
    if s >= end:
        end = e
        answer += 1
print(answer)        
