import sys
from collections import deque
input = sys.stdin.readline
max_num = 100002
n,m = map(int, input().split())
dist = [0 for _ in range(max_num)]

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == m:
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx < max_num and dist[nx] == 0:
                dist[nx] = dist[x] + 1
                q.append(nx)
bfs()             
    