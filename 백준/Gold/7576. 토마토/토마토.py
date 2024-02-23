import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dist = [[0 for _ in range(n)] for _ in range(m)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
q = deque()
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            q.append((i,j))
        if graph[i][j] == 0:
            dist[i][j] = -1
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx,ny))
answer = 0
breaker = False
for i in range(m):
    for j in range(n):
        if dist[i][j] == -1:
            answer = -1
            breaker = True
            break
        else:
            answer = max(answer, dist[i][j])
    if breaker == True:
            break
print(answer)        