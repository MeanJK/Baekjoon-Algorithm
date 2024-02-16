import sys
input = sys.stdin.readline

N, M = map(int, input().split())
height = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    tall, short = map(int, input().split())
    height[tall][short] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if height[i][j] == 1 or (height[i][k] == 1 and height[k][j] == 1):
                height[i][j] = 1
answer = 0
for i in range(1, N+1):
    known_height = 0
    for j in range(1, N+1):
        known_height += height[i][j] + height[j][i]
    if known_height == N-1:
        answer += 1
print(answer)
            