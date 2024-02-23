import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(str, input())) for _ in range(n)]
dist = [[0 for _ in range(m)] for _ in range(n)]
fire_dist = [[0 for _ in range(m)] for _ in range(n)]
q = deque()
fire_q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'J':
            q.append((i,j))
            dist[i][j] = 1
        if graph[i][j] == 'F':
            fire_q.append((i,j))
            fire_dist[i][j] = 1
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    while fire_q:
        x, y = fire_q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != '#' and fire_dist[nx][ny] == 0:
                fire_dist[nx][ny] = fire_dist[x][y] + 1
                fire_q.append((nx,ny))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != '#' and dist[nx][ny] == 0:
                    if not fire_dist[nx][ny] or fire_dist[nx][ny] > dist[x][y] + 1:
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx,ny))
            else:
                return dist[x][y]
    return "IMPOSSIBLE"
print(bfs())    