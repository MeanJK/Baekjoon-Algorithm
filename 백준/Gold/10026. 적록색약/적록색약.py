import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(input()) for _ in range(N)]
vis = [[0 for _ in range(N)] for _ in range(N)]
q = deque()
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def bfs(x,y):
    q.append((x,y))
    vis[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < N and vis[nx][ny] == 0 and graph[nx][ny] == graph[x][y]:
                vis[nx][ny] = 1
                q.append((nx,ny))
count = 0
rgb_count = 0
for i in range(N):
    for j in range(N):
        if not vis[i][j]:
            bfs(i, j)
            count += 1

vis = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'
for i in range(N):
    for j in range(N):
        if not vis[i][j]:
            bfs(i,j)
            rgb_count += 1
print(count, rgb_count)            