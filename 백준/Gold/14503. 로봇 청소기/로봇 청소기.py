import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
r,c,d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
clean = 0

def bfs(x,y,d):
    global clean        
    q = deque()
    q.append((x,y))
    clean += 1
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        flag = 0
        for _ in range(4):
            d = (d+3)%4
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    clean += 1
                    q.append((nx,ny))
                    flag = 1
                    break
        if flag == 0:
            if graph[x-dx[d]][y-dy[d]] != 1:
                q.append((x-dx[d], y-dy[d]))
            else:
                print(clean)
                break
bfs(r,c,d)
                    