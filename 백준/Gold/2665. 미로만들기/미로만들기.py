import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().strip())))
dx = [0, 1, 0, -1]
dy = [1,0,-1,0]
def bfs():
    q = deque()
    q.append((0,0))
    visited = [[-1] * N for i in range(N)]
    visited[0][0] = 0
    
    while q:
        x, y = q.popleft()
        if x == N-1 and y == N-1:
            return visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=0 and nx < N and ny >= 0 and ny < N and visited[nx][ny] == -1:
                if graph[nx][ny] == 1:
                    q.appendleft((nx,ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
print(bfs())