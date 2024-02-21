import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
group = 0
max_count = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def bfs(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    count = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                count += 1
                graph[nx][ny] = 0
                q.append((nx,ny))
    return count                
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            group += 1
            max_count = max(max_count, bfs(i,j))
if group == 0:
    print(0)
    print(0)
else:   
    print(group)
    print(max_count)